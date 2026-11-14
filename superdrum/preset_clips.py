"""Turn the step grids the research found (copied from owner's manuals) into MIDI clips that play the
matching rebuilt kit. Clips go to User Library/Clips/Drum Machine Patterns/<kit>/."""
import json, os, re, struct, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from layout import load_specs, pad_labels

from config import CLIPS_DIR as CLIPS, WORK
PPQ = 96


def vlq(n):
    out = [n & 0x7F]
    while n > 0x7F:
        n >>= 7
        out.insert(0, (n & 0x7F) | 0x80)
    return bytes(out)


def write_mid(path, grid, note_of, bpm=120):
    num = int(grid.get("time_signature", "4/4").split("/")[0])
    steps = grid["steps_per_bar"] * grid.get("bars", 1)
    step_ticks = PPQ * num // grid["steps_per_bar"]
    events = []
    for lane, pattern in grid["lanes"].items():
        note = note_of.get(lane)
        if note is None:
            continue
        for i, ch in enumerate(pattern[:steps]):
            if ch in "xX":
                vel = 127 if ch == "X" else 90
                events.append((i * step_ticks, 0x90, note, vel))
                events.append((i * step_ticks + max(1, step_ticks * 9 // 10), 0x80, note, 0))
    events.sort(key=lambda e: (e[0], e[1] == 0x90))
    trk = b"\x00\xff\x51\x03" + struct.pack(">I", 60_000_000 // bpm)[1:]
    trk += b"\x00\xff\x58\x04" + bytes([num, 2, 24, 8])
    t = 0
    for tick, status, note, vel in events:
        trk += vlq(tick - t) + bytes([status, note, vel]); t = tick
    end = steps * step_ticks
    trk += vlq(max(0, end - t)) + b"\xff\x2f\x00"
    with open(path, "wb") as fh:
        fh.write(b"MThd" + struct.pack(">IHHH", 6, 0, 1, PPQ) + b"MTrk" + struct.pack(">I", len(trk)) + trk)


def clip_name(raw):
    m = re.search(r"Pattern number (\d+)", raw)
    if m:
        return f"Pattern {m.group(1)} (manual example)"
    name = raw.split(":", 1)[-1].strip()
    name = re.split(r"[,;]", name)[0].strip().strip("'\"")
    return re.sub(r"[/\\:]", "-", name.title() if name.isupper() else name)


def main():
    specs = load_specs()
    report = json.load(open(os.path.join(WORK, "build_report.json")))["built"]
    made = []
    for b in report:
        spec = specs.get(b["pack"])
        if not spec or b["layout_kind"] != "machine layout":
            continue
        grids = [(p.get("name") or "", p["grid"]) for p in spec.get("preset_patterns") or [] if p.get("grid")]
        grids += [(f"{t.get('artist')} - {t.get('title')}", t["grid"]) for t in spec.get("famous_tracks") or [] if t.get("grid")]
        if not grids:
            continue
        voices = [v for v in spec["voices"] if v.get("type") and v.get("type") != "Other"]
        labels = pad_labels(voices)                  # the voice's pad, wherever it sits in the kit
        note_by_label = {l: n for n, l, *_ in b["layout"]}
        note_of = {v["label"]: note_by_label[labels[i]] for i, v in enumerate(voices) if labels[i] in note_by_label}
        folder = os.path.join(CLIPS, b["preset"][:-4])
        os.makedirs(folder, exist_ok=True)
        for raw, grid in grids:
            missing = [lane for lane in grid["lanes"] if lane not in note_of]
            path = os.path.join(folder, clip_name(raw) + ".mid")
            write_mid(path, grid, note_of)
            made.append((b["preset"][:-4], os.path.basename(path), missing))
    for kit, clip, missing in made:
        print(f"{kit:28s} {clip:40s}" + (f"  (no pad for: {', '.join(missing)})" if missing else ""))
    print(len(made), "clips")


if __name__ == "__main__":
    main()

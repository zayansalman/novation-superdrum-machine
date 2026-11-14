"""Turn the drum patterns of famous records (research/beats/*.json, see research/beats/README.md) into MIDI clips
that play every rebuilt kit of the machine the record was made on.

Each lane goes to the pad with that sound type; guiro/cabasa/maracas are found by pad name, and low/mid/high
toms, congas and bongos by the pad's name or, failing that, the measured pitch of its samples.
Clips: User Library/Clips/Drum Machine Patterns/<kit>/<Artist> - <Title> (<BPM> BPM).mid

usage: python3 superdrum/beat_clips.py [--out DIR] [--beats DIR]"""
import glob, json, os, re, struct, sys
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from packs import PACKS_ROOT
from layout import load_specs, plan_pack, BODY_PITCH
from build_kits import load_types, safe

from config import BEATS, CLIPS_DIR as CLIPS, WORK
MANIFEST = os.path.join(WORK, "beat_clips_manifest.json")
PPQ = 480
SOFT, LOUD = 90, 127

# lane -> (pad types to try, in order; which one: index in panel order or pitch position; pad-name pattern that wins)
LANES = {
    "Kick": (["Kick"], 0, None), "Kick 2": (["Kick"], 1, None),
    "Snare": (["Snare"], 0, None), "Snare 2": (["Snare"], 1, None),
    "Rim": (["Rim"], 0, r"rim|side ?stick"), "Clap": (["Clap"], 0, None), "Snap": (["Snap", "Clap"], 0, None),
    "Closed Hat": (["Closed Hat", "Pedal Hat"], 0, None), "Pedal Hat": (["Pedal Hat", "Closed Hat"], 0, None),
    "Open Hat": (["Open Hat"], 0, None),
    "Low Tom": (["Tom"], "low", None), "Mid Tom": (["Tom"], "mid", None), "High Tom": (["Tom"], "high", None),
    "Low Conga": (["Conga"], "low", None), "Mid Conga": (["Conga"], "mid", None),
    "High Conga": (["Conga"], "high", None),
    "Low Bongo": (["Bongo"], "low", None), "High Bongo": (["Bongo"], "high", None),
    "Timbale": (["Timbale"], 0, None), "Cowbell": (["Cowbell"], 0, None), "Agogo": (["Agogo"], 0, None),
    "Clave": (["Clave", "Wood Block"], 0, r"clave"), "Wood Block": (["Wood Block", "Clave"], 0, r"block"),
    "Shaker": (["Shaker"], 0, r"marac|shak"), "Cabasa": (["Shaker"], 0, r"cabasa|afuche"),
    "Tambourine": (["Tambourine"], 0, None), "Triangle": (["Triangle"], 0, None),
    "Guiro": ([], 0, r"g[uü]iro"),
    "Crash": (["Crash", "Cymbal"], 0, None), "Ride": (["Ride", "Cymbal"], 0, None),
    "Cymbal": (["Cymbal", "Crash", "Ride", "Open Hat"], 0, None),   # CR-78 packs file the cymbal as 'Hat_O'
}
MIN_COVER = 0.5      # write a clip only if at least half its hits have a pad in the kit
# research notes say these grids were worked out rather than published
APPROX = {("Jean-Michel Jarre", "Oxygène (Part IV)")}
# lanes the research itself calls a guess (the tab's 'vibraslap' is not a DR-55 sound)
LANE_DROPS = {("The Cure", "One Hundred Years"): {"Rim"}}
# whole words first; two-letter codes (LT, MC...) only when no word says it ('Mt High Conga' = muted, high)
WORDS = [(re.compile(p, re.I), h) for p, h in ((r"\b(low|lo|lowest|floor)\b", 0), (r"\b(mid|md|middle)\b", 1),
                                               (r"\b(high|hi|highest)\b", 2))]
CODES = [(re.compile(p, re.I), h) for p, h in ((r"\b(lt|lc|lb)\b", 0), (r"\b(mt|mc)\b", 1), (r"\b(ht|hc|hb)\b", 2))]


def hint(text):
    """0 = low, 1 = mid, 2 = high, None = the name doesn't say (or says two things)."""
    for table in (WORDS, CODES):
        found = {h for pat, h in table if pat.search(text)}
        if found:
            return found.pop() if len(found) == 1 else None
    return None


def pitch_order(pads, f0, names):
    """Sort same-type pads from lowest to highest pitch.
    1. Every pad's name says low/mid/high -> use that.
    2. Numbered pads (Tom 1..6) -> number order; the machine's voice notes ('Tom 1 (highest)') give the
       direction, and drummers' convention (tom 1 = highest) when they don't.
    3. Otherwise the median measured pitch of the pad's samples."""
    hints = [hint(names.get(p[1], p[1])) for p in pads]
    if None not in hints and len(set(hints)) == len(pads):
        return [p for _, p in sorted(zip(hints, pads), key=lambda hp: hp[0])]
    nums = [re.findall(r"\d+", p[1]) for p in pads]
    if all(nums) and len({int(n[-1]) for n in nums}) == len(pads):
        by_num = [p for _, p in sorted(zip((int(n[-1]) for n in nums), pads), key=lambda np_: np_[0])]
        first, last = hint(names.get(by_num[0][1], "")), hint(names.get(by_num[-1][1], ""))
        rising = first == 0 or last == 2
        return by_num if rising else by_num[::-1]
    return sorted(pads, key=lambda p: float(np.median([BODY_PITCH.get(f, f0.get(f, 0.0)) for f in p[3]] or [0.0])))


def pad_for(lane, pads, f0, names=None):
    names = names or {}
    types, which, name_pat = LANES[lane]
    if name_pat:
        named = [p for p in pads if re.search(name_pat, p[1], re.I)]
        if named and (not types or any(p[2] in types for p in named)):
            named = [p for p in named if not types or p[2] in types] or named
            return named[0]
        if not types:
            return None
    for t in types:
        cands = sorted((p for p in pads if p[2] == t), key=lambda p: p[0])
        if not cands:
            continue
        if isinstance(which, int):
            return cands[min(which, len(cands) - 1)]
        want = {"low": 0, "mid": 1, "high": 2}[which]
        if len(cands) == 1:     # one pad only: fine unless its name says it is a different one
            h = hint(names.get(cands[0][1], cands[0][1]))
            return cands[0] if h in (None, want) else None
        cands = pitch_order(cands, f0, names)
        return {"low": cands[0], "high": cands[-1], "mid": cands[len(cands) // 2]}[which]
    return None


def bar_ticks(ts):
    num, den = (int(x) for x in ts.split("/"))
    return PPQ * 4 * num // den


def pattern_events(pat, note_of):
    """-> [(tick, note, velocity)], clip length in ticks."""
    ts = pat.get("time_signature") or "4/4"
    spb, bars = int(pat["steps_per_bar"]), int(pat.get("bars") or 1)
    step = bar_ticks(ts) / spb
    swing = float(pat.get("swing_percent") or 50)
    accent = pat["lanes"].get("Accent", "")
    open_steps = {i for i, ch in enumerate(pat["lanes"].get("Open Hat", "")) if ch in "xX"}
    hits = {}
    for lane, row in pat["lanes"].items():
        note = note_of.get(lane)
        if note is None:
            continue
        for i, ch in enumerate(row[:spb * bars]):
            if ch not in "xX":
                continue
            if lane in ("Closed Hat", "Pedal Hat") and i in open_steps and "Open Hat" in note_of:
                continue        # one hi-hat voice: the open hat wins the step (a closed one would choke it)
            t = i * step
            if spb in (8, 16) and i % 2 == 1:
                t += (swing - 50) / 50 * step
            vel = LOUD if ch == "X" or (i < len(accent) and accent[i] in "xX") else SOFT
            key = (int(round(t)), note)
            hits[key] = max(vel, hits.get(key, 0))
    return sorted((t, n, v) for (t, n), v in hits.items()), int(round(bar_ticks(ts) * bars)), ts, step


def vlq(n):
    out = [n & 0x7F]
    while n > 0x7F:
        n >>= 7
        out.insert(0, (n & 0x7F) | 0x80)
    return bytes(out)


def write_mid(path, events, length, ts, bpm, step):
    num, den = (int(x) for x in ts.split("/"))
    dur = max(1, int(step // 2))
    ev = []
    for t, n, v in events:
        ev.append((t, 1, bytes([0x90, n, v])))
        ev.append((min(t + dur, length), 0, bytes([0x80, n, 0])))
    ev.sort(key=lambda e: (e[0], e[1]))
    trk = b"\x00\xff\x51\x03" + struct.pack(">I", int(round(60_000_000 / (bpm or 120))))[1:]
    trk += b"\x00\xff\x58\x04" + bytes([num, den.bit_length() - 1, 24, 8])
    now = 0
    for t, _, msg in ev:
        trk += vlq(t - now) + msg
        now = t
    trk += vlq(length - now) + b"\xff\x2f\x00"
    with open(path, "wb") as fh:
        fh.write(b"MThd" + struct.pack(">IHHH", 6, 0, 1, PPQ) + b"MTrk" + struct.pack(">I", len(trk)) + trk)


def read_mid(path):
    """-> (ppq, [(tick, note, velocity) note-ons], end tick) for the files written above."""
    data = open(path, "rb").read()
    assert data[:4] == b"MThd"
    ppq = struct.unpack(">H", data[12:14])[0]
    pos, end = 22, 22 + struct.unpack(">I", data[18:22])[0]
    t, ons = 0, []
    while pos < end:
        d = 0
        while True:
            b = data[pos]; pos += 1
            d = (d << 7) | (b & 0x7F)
            if b < 0x80:
                break
        t += d
        st = data[pos]
        if st == 0xFF:
            ln = data[pos + 2]
            pos += 3 + ln
        else:
            if st & 0xF0 == 0x90 and data[pos + 2] > 0:
                ons.append((t, data[pos + 1], data[pos + 2]))
            pos += 3
    return ppq, ons, t


def short_section(sec):
    """'main groove: CR-78 Rock 1, variation A (factory preset)' -> 'CR-78 Rock 1, var. A'"""
    s = re.sub(r"\(.*?\)|\[.*?\]", "", sec or "")
    s = re.sub(r"^\s*(main groove|reference)\s*[:\-]?\s*", "", s, flags=re.I)
    s = re.sub(r"\b(factory )?preset\b.*$", "", s, flags=re.I)              # '... factory preset as printed'
    s = re.sub(r"\b[A-Z]{2,3}-?\d{2,4}[A-Z]?\b\s*", "", s)                  # the kit folder already says 'CR-78'
    s = re.sub(r"\bvariation\s+([A-D])\b", r"var. \1", s, flags=re.I)
    s = re.sub(r"\s+", " ", s).strip(" ,;:-")
    return s if len(s) <= 48 else s[:48].rsplit(" ", 1)[0].rstrip(" ,;:-")


def clip_name(track, pat, n_pats, partial):
    bpm = track.get("bpm")
    bpm_s = f" ({float(bpm):g} BPM)" if isinstance(bpm, (int, float)) and bpm else ""
    sec = short_section(pat.get("section")) if n_pats > 1 else ""
    part = f" - {sec}" if sec else ""
    approx = (track.get("pattern_confidence") == "description"
              or (track.get("artist"), track.get("title")) in APPROX)
    used = [l for l, row in pat["lanes"].items() if l != "Accent" and set(row) & set("xX")]
    only = (f" ({' + '.join(l.lower() for l in used)} only)"
            if len(used) <= 2 and re.search(r"\bonly\b", pat.get("section") or "", re.I) else "")
    tags = only + (" (approx)" if approx else "") + (" (partial)" if partial else "")
    name = f"{track['artist']} - {track['title']}{part}{bpm_s}{tags}"
    return re.sub(r'[/\\:*?"<>|]', "-", re.sub(r"\s+", " ", name)).strip()[:150]


def check_pattern(pat):
    spb, bars = int(pat["steps_per_bar"]), int(pat.get("bars") or 1)
    bad = [l for l in pat["lanes"] if l != "Accent" and l not in LANES]
    short = [l for l, row in pat["lanes"].items() if len(row) != spb * bars]
    return bad, short


def main(out_root=CLIPS, beats_dir=BEATS):
    entries = [m for f in sorted(glob.glob(os.path.join(beats_dir, "*.json"))) for m in json.load(open(f))]
    specs = load_specs()
    built = json.load(open(os.path.join(WORK, "build_report.json")))["built"]
    types, f0 = load_types()
    plans = {}

    def pads_of(b):
        if b["pack"] not in plans:
            units, _ = plan_pack(b["pack"], os.path.join(PACKS_ROOT, b["pack"]), specs, types, f0)
            plans[b["pack"]] = {safe(u) + ".adg": pads for u, pads, _, _ in units}
        pads = plans[b["pack"]].get(b["preset"])
        if pads is None or [(p[0], p[1]) for p in pads] != [(n, l) for n, l, *_ in b["layout"]]:
            raise RuntimeError(f"{b['preset']}: plan no longer matches the built kit")
        return pads

    old = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) and out_root == CLIPS else []
    for p in old:
        if os.path.exists(p):
            os.remove(p)
    written, report, problems, skipped = [], [], [], []
    for m in entries:
        kits = [b for b in built if (b["pack"] in (m.get("pack_folders") or [])
                                     and (specs.get(b["pack"]) or {}).get("machine") == b["machine"])
                or b["machine"] == m.get("machine")]
        for track in m.get("tracks") or []:
            pats = track.get("patterns") or []
            drop = LANE_DROPS.get((track.get("artist"), track.get("title")), set())
            pats = [dict(p, lanes={l: r for l, r in p["lanes"].items() if l not in drop}) for p in pats]
            for pat in pats:
                bad, short = check_pattern(pat)
                if bad or short:
                    problems.append((m["machine"], track["title"], f"bad lanes {bad}, wrong length {short}"))
                    continue
                for b in kits:
                    pads = pads_of(b)
                    spec = specs.get(b["pack"]) or {}
                    names = {}       # pad label -> label + the machine's full voice name ('Tom 1 (highest)')
                    for v in spec.get("voices") or []:
                        for key in (v.get("label"), v.get("name")):
                            if key:
                                names.setdefault(key, f"{v.get('label', '')} {v.get('name', '')}")
                    lanes = [l for l in pat["lanes"] if l != "Accent" and set(pat["lanes"][l]) & set("xX")]
                    note_of = {l: p[0] for l in lanes if (p := pad_for(l, pads, f0, names))}
                    missing = [l for l in lanes if l not in note_of]
                    n_hits = {l: sum(ch in "xX" for ch in pat["lanes"][l]) for l in lanes}
                    cover = sum(n_hits[l] for l in note_of) / max(1, sum(n_hits.values()))
                    core_lost = [l for l in ("Kick", "Snare") if l in missing]
                    if cover < MIN_COVER or core_lost:
                        skipped.append({"kit": b["preset"][:-4], "track": f"{track['artist']} - {track['title']}",
                                        "section": pat.get("section"), "cover": round(cover, 2), "missing": missing})
                        continue
                    events, length, ts, step = pattern_events(pat, note_of)
                    folder = os.path.join(out_root, b["preset"][:-4])
                    os.makedirs(folder, exist_ok=True)
                    path = os.path.join(folder, clip_name(track, pat, len(pats), cover < 0.8) + ".mid")
                    write_mid(path, events, length, ts, track.get("bpm"), step)
                    # read it back: right pads, right number of hits, right length
                    ppq, ons, end = read_mid(path)
                    kit_notes = {p[0] for p in pads}
                    assert ppq == PPQ and end == length, path
                    assert len(ons) == len(events) and {n for _, n, _ in ons} <= kit_notes, path
                    written.append(path)
                    report.append({"kit": b["preset"][:-4], "clip": os.path.basename(path),
                                   "machine": m["machine"], "confidence": track.get("pattern_confidence"),
                                   "cover": round(cover, 2),
                                   "lanes": {l: next(p[1] for p in pads if p[0] == n) for l, n in note_of.items()},
                                   "missing": missing})
    if out_root == CLIPS:
        json.dump(written, open(MANIFEST, "w"), indent=1)
    json.dump({"clips": report, "skipped": skipped, "problems": problems},
              open(os.path.join(WORK, "beat_clips_report.json"), "w"), indent=1)
    for r in report:
        print(f"{r['kit'][:26]:26s} {r['clip'][:80]:80s}" + (f"  no pad: {', '.join(r['missing'])}" if r["missing"] else ""))
    for s in skipped:
        print(f"NOT WRITTEN (kit lacks the sounds): {s['kit']} | {s['track']} | {s['section']} | cover {s['cover']} | missing {s['missing']}")
    for p in problems:
        print("BAD GRID:", *p)
    print(f"{len(written)} clips in {len({r['kit'] for r in report})} kit folders")


if __name__ == "__main__":
    args = sys.argv[1:]
    kw = {}
    if "--out" in args:
        kw["out_root"] = args[args.index("--out") + 1]
    if "--beats" in args:
        kw["beats_dir"] = args[args.index("--beats") + 1]
    main(**kw)

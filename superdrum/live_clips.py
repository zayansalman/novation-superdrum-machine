"""Live Clips (.alc): each beat clip together with its kit, so one drag loads both.

An .alc is a one-track Live Set. Live keeps a rack inside a set in 'device form' (Branches/DrumBranch),
while our kits are presets in 'preset form' (BranchPresets/DrumBranchPreset). This converts one to the other,
using Ableton's own '808 Core Kit Electro 127 bpm.alc' (read from your Live installation) as the
skeleton for the set, track, clip and chains. Every pad, sample, macro mapping, choke
group and send is carried over unchanged.

usage: python3 superdrum/live_clips.py KIT CLIP.mid [OUT.alc]     (one clip)
       python3 superdrum/live_clips.py --all                       (every .mid under Drum Machine Patterns)"""
import copy, glob, gzip, os, re, struct, sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from config import CORE_LIBRARY as CORE, KITS_DIR as KITS, CLIPS_DIR as CLIPS
TEMPLATE = os.path.join(CORE, "MIDI Clips", "Drums", "Drum Machines", "808 Core Kit Electro 127 bpm.alc")
GLOBAL_ID = re.compile(r"^(AutomationTarget|ModulationTarget|Pointee|ControllerTargets\.\d+|\w+ModulationTarget)$")

_T = {}


def return_skeleton(drum_branch):
    """A Drum Rack return chain, as Live keeps it in a set: a pad chain that carries audio instead of MIDI
    and has no note settings."""
    b = copy.deepcopy(drum_branch)
    b.tag = "ReturnBranch"
    b.remove(b.find("BranchInfo"))
    b.find("DeviceChain/MidiToAudioDeviceChain").tag = "AudioToAudioDeviceChain"
    return b


def tmpl():
    if not _T:
        t = ET.fromstring(gzip.open(TEMPLATE).read())
        dg = t.find(".//DrumGroupDevice")
        drum_branch = dg.find("Branches/DrumBranch")
        inst_branch = drum_branch.find(".//InstrumentGroupDevice/Branches/InstrumentBranch")
        return_branch = return_skeleton(drum_branch)
        _T.update(set=t, drum=copy.deepcopy(drum_branch), inst=copy.deepcopy(inst_branch),
                  ret=copy.deepcopy(return_branch))
    return _T


def clear(e):
    for c in list(e):
        e.remove(c)
    return e


def replace_child(parent, tag, new):
    old = parent.find(tag)
    idx = list(parent).index(old)
    parent.remove(old)
    new = copy.deepcopy(new)
    new.tag = tag
    parent.insert(idx, new)


def device_of(preset):
    """A preset element (AbletonDevicePreset / GroupDevicePreset) -> the device as Live keeps it in a set."""
    dev = copy.deepcopy(preset.find("Device")[0])
    if preset.tag == "GroupDevicePreset":
        clear(dev.find("Branches")).extend(branch_of(bp, i) for i, bp in enumerate(preset.find("BranchPresets")))
        rb = dev.find("ReturnBranches")
        if rb is not None:
            rps = preset.find("ReturnBranchPresets")
            clear(rb).extend(return_of(rp, i) for i, rp in enumerate(list(rps) if rps is not None else []))
    return dev


def fill_chain(b, bp, chain_tag):
    devices = b.find(f"DeviceChain/{chain_tag}/Devices")
    clear(devices).extend(device_of(d) for d in bp.find("DevicePresets"))
    sm = b.find(f"DeviceChain/{chain_tag}/SignalModulations")
    if sm is not None:
        clear(sm)
    for tag in ("BranchSelectorRange", "IsSoloed", "SessionViewBranchWidth", "AutoColored", "AutoColorScheme"):
        if bp.find(tag) is not None and b.find(tag) is not None:
            replace_child(b, tag, bp.find(tag))
    b.find("Color").set("Value", bp.find("DocumentColorIndex").get("Value"))
    clear(b.find("SourceContext")).append(ET.Element("Value"))
    mixer = bp.find("MixerPreset/AbletonDevicePreset/Device")[0]
    clear(b.find("MixerDevice")).extend(copy.deepcopy(list(mixer)))
    name = bp.find("Name").get("Value")
    first = b.find(f"DeviceChain/{chain_tag}/Devices")
    shown = name or next((d.find("UserName").get("Value") for d in first if d.find("UserName") is not None
                          and d.find("UserName").get("Value")), "")
    b.find("Name/EffectiveName").set("Value", shown)
    b.find("Name/UserName").set("Value", name)


def branch_of(bp, i):
    if bp.tag == "DrumBranchPreset":
        b = copy.deepcopy(tmpl()["drum"])
        fill_chain(b, bp, "MidiToAudioDeviceChain")
        zs, bi = bp.find("ZoneSettings"), b.find("BranchInfo")
        for tag in ("ReceivingNote", "SendingNote", "ChokeGroup"):
            bi.find(tag).set("Value", zs.find(tag).get("Value"))
    elif bp.tag == "InstrumentBranchPreset":
        b = copy.deepcopy(tmpl()["inst"])
        fill_chain(b, bp, "MidiToAudioDeviceChain")
        replace_child(b, "ZoneSettings", bp.find("ZoneSettings"))
    else:
        raise ValueError("unexpected chain type " + bp.tag)
    b.set("Id", str(i))
    return b


def return_of(rp, i):
    b = copy.deepcopy(tmpl()["ret"])
    fill_chain(b, rp, "AudioToAudioDeviceChain")
    b.set("Id", str(i))
    return b


def read_mid(path):
    """Our own .mid files -> (ppq, numerator, denominator, [(on tick, off tick, note, velocity)], end tick)."""
    data = open(path, "rb").read()
    ppq = struct.unpack(">H", data[12:14])[0]
    pos, end = 22, 22 + struct.unpack(">I", data[18:22])[0]
    t, num, den, open_, notes = 0, 4, 4, {}, []
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
            kind, ln = data[pos + 1], data[pos + 2]
            if kind == 0x58:
                num, den = data[pos + 3], 2 ** data[pos + 4]
            pos += 3 + ln
            continue
        note, vel = data[pos + 1], data[pos + 2]
        if st & 0xF0 == 0x90 and vel > 0:
            open_[note] = (t, vel)
        elif note in open_:
            on, v = open_.pop(note)
            notes.append((on, t, note, v))
        pos += 3
    return ppq, num, den, sorted(notes), t


def fill_clip(clip, name, mid):
    ppq, num, den, notes, end = read_mid(mid)
    beats = end / ppq
    clip.find("Name").set("Value", name)
    for tag, val in (("CurrentStart", 0), ("CurrentEnd", beats)):
        clip.find(tag).set("Value", format(val, ".10g"))
    loop = clip.find("Loop")
    for tag, val in (("LoopStart", 0), ("LoopEnd", beats), ("StartRelative", 0), ("OutMarker", beats),
                     ("HiddenLoopStart", 0), ("HiddenLoopEnd", beats)):
        loop.find(tag).set("Value", format(val, ".10g"))
    loop.find("LoopOn").set("Value", "true")
    ts = clip.find("TimeSignature/TimeSignatures/RemoteableTimeSignature")
    ts.find("Numerator").set("Value", str(num))
    ts.find("Denominator").set("Value", str(den))
    clear(clip.find("Envelopes/Envelopes")) if clip.find("Envelopes/Envelopes") is not None else None
    kts = clear(clip.find("Notes/KeyTracks"))
    by_key = {}
    for on, off, note, vel in notes:
        by_key.setdefault(note, []).append((on, off, vel))
    nid = 0
    for k, note in enumerate(sorted(by_key)):
        kt = ET.SubElement(kts, "KeyTrack", {"Id": str(k)})
        ns = ET.SubElement(kt, "Notes")
        for on, off, vel in by_key[note]:
            nid += 1
            ET.SubElement(ns, "MidiNoteEvent", {"Time": format(on / ppq, ".10g"), "Duration": format((off - on) / ppq, ".10g"),
                                                "Velocity": str(vel), "OffVelocity": "64", "NoteId": str(nid)})
        ET.SubElement(kt, "MidiKey", {"Value": str(note)})
    pnes = clip.find("Notes/PerNoteEventStore/EventLists")
    if pnes is not None:
        clear(pnes)
    npg = clip.find("Notes/NoteProbabilityGroups")
    if npg is not None:
        clear(npg)
    clip.find("Notes/NoteIdGenerator/NextId").set("Value", str(nid + 1))
    return len(notes), beats


def renumber(root):
    """Ids Live expects to be unique across the whole set; returns the next free one."""
    n = 0
    for e in root.iter():
        if GLOBAL_ID.match(e.tag) and "Id" in e.attrib:
            n += 1
            e.set("Id", str(n))
    return n + 1


def build_alc(kit_adg, mid, out, clip_name, track_name):
    s = copy.deepcopy(tmpl()["set"])
    ls = s.find("LiveSet")
    trk = ls.find("Tracks/MidiTrack")
    trk.find("Name/EffectiveName").set("Value", track_name)
    trk.find("Name/UserName").set("Value", track_name)
    ae = trk.find("AutomationEnvelopes/Envelopes")
    if ae is not None:
        clear(ae)
    kit = ET.fromstring(gzip.open(kit_adg).read()).find("GroupDevicePreset")
    rack = device_of(kit)
    rack.set("Id", "0")
    clear(trk.find("DeviceChain/DeviceChain/Devices")).append(rack)
    clip = trk.find("DeviceChain/MainSequencer/ClipSlotList/ClipSlot/ClipSlot/Value/MidiClip")
    if clip is None:
        clip = trk.find(".//ClipSlot/Value/MidiClip")
    n_notes, beats = fill_clip(clip, clip_name, mid)
    ls.find("NextPointeeId").set("Value", str(renumber(s)))
    ET.indent(s, space="\t")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(s, encoding="unicode") + "\n"
    with gzip.open(out, "wb") as fh:
        fh.write(xml.encode("utf-8"))
    return n_notes, beats


def verify_alc(out, kit_adg, mid):
    s = ET.fromstring(gzip.open(out).read())
    kit = ET.fromstring(gzip.open(kit_adg).read()).find("GroupDevicePreset")
    want = kit.findall("BranchPresets/DrumBranchPreset")
    dg = s.find("LiveSet/Tracks/MidiTrack/DeviceChain/DeviceChain/Devices/DrumGroupDevice")
    got = dg.findall("Branches/DrumBranch")
    assert len(got) == len(want), (len(got), len(want))
    t = tmpl()
    for b, bp in zip(got, want):
        assert [c.tag for c in b] == [c.tag for c in t["drum"]], "pad layout differs from Live's"
        for tag in ("ReceivingNote", "SendingNote", "ChokeGroup"):
            assert b.find(f"BranchInfo/{tag}").get("Value") == bp.find(f"ZoneSettings/{tag}").get("Value")
        wav = lambda e: [p.get("Value") for p in e.iter("Path") if p.get("Value", "").lower().endswith((".wav", ".aif", ".aiff"))]
        assert wav(b) == wav(bp) and all(os.path.exists(x) for x in wav(b)), "samples differ"
        assert len(list(b.iter("MultiSamplePart"))) == len(list(bp.iter("MultiSamplePart")))
        assert len(list(b.iter("KeyMidi"))) == len(list(bp.iter("KeyMidi")))
    assert len(dg.findall("ReturnBranches/ReturnBranch")) == len(kit.findall("ReturnBranchPresets/*"))
    assert not s.findall(".//BranchPresets") and not s.findall(".//DrumBranchPreset"), "preset-form leftovers"
    ids = [int(e.get("Id")) for e in s.iter() if GLOBAL_ID.match(e.tag) and "Id" in e.attrib]
    assert len(ids) == len(set(ids)) and int(s.find("LiveSet/NextPointeeId").get("Value")) > max(ids)
    pads = {128 - int(b.find("BranchInfo/ReceivingNote").get("Value")) for b in got}
    keys = [int(k.find("MidiKey").get("Value")) for k in s.iter("KeyTrack")]
    assert set(keys) <= pads, sorted(set(keys) - pads)
    n = len(list(s.iter("MidiNoteEvent")))
    assert n == len(read_mid(mid)[3])
    return n


def alc_name(kit, clip_stem):
    m = re.search(r"\s*\((\d+(?:\.\d+)?) BPM\)", clip_stem)
    base = re.sub(r"\s*\(\d+(?:\.\d+)? BPM\)", "", clip_stem).strip()
    return f"{kit} - {base}" + (f" {m.group(1)} bpm" if m else "")


def build_all():
    """A Live Clip next to every .mid clip whose kit exists."""
    made = 0
    for kit in sorted(os.listdir(CLIPS)):
        adg = os.path.join(KITS, kit + ".adg")
        if not os.path.isfile(adg):
            continue
        for mid in sorted(glob.glob(os.path.join(CLIPS, kit, "*.mid"))):
            stem = os.path.splitext(os.path.basename(mid))[0]
            out = os.path.join(CLIPS, kit, alc_name(kit, stem) + ".alc")
            build_alc(adg, mid, out, re.sub(r"\s*\(\d+(?:\.\d+)? BPM\)", "", stem), kit)
            verify_alc(out, adg, mid)
            made += 1
    print(made, "Live Clips")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--all":
        build_all()
    elif args:
        kit, mid = args[0], args[1]
        stem = os.path.splitext(os.path.basename(mid))[0]
        out = args[2] if len(args) > 2 else os.path.join(os.path.dirname(mid), alc_name(kit, stem) + ".alc")
        adg = os.path.join(KITS, kit + ".adg")
        n, beats = build_alc(adg, mid, out, re.sub(r"\s*\(\d+(?:\.\d+)? BPM\)", "", stem), kit)
        print("wrote", out, "|", n, "notes,", beats, "beats | checked", verify_alc(out, adg, mid), "notes")

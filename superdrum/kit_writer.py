import copy, gzip, os, sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ableton_xml import (USER_LIB, HEADER, OPN, ZERO_ID_TAGS, wav_info, natural_key,
                          normalize_ids, browser_path, set_fileref)
from drum_names import classify
from config import CORE_LIBRARY, TEMPLATES
from effects import add_returns, verify_returns

FIXED = {"Kick": 36, "Rim": 37, "Snare": 38, "Clap": 39, "Closed Hat": 42, "Open Hat": 46}
FLOATING = ["Tom", "Crash", "Ride", "Pedal Hat", "Cymbal", "Cowbell", "Clave", "Conga", "Shaker",
            "Tambourine", "Bongo", "Timbale", "Agogo", "Wood Block", "Triangle", "Snap", "Perc", "FX"]
HATS = {"Closed Hat", "Pedal Hat", "Open Hat"}
MAX_VARIATIONS = 128
MAX_MACROS = 4
TUNE_RANGE = (-12, 12)
DECAY_RANGE = (20, 30000)
TONE_RANGE = (200, 22000)
LEVEL_RANGE = (0.0003162277571, 1.99526238)
LEVEL_0DB_MACRO = 107.950005


def fmt(v):
    v = float(v)
    return str(int(v)) if v.is_integer() else format(v, ".10g")


def chunk(files, label):
    if len(files) <= MAX_VARIATIONS:
        return [(label, files)]
    n = -(-len(files) // MAX_VARIATIONS)
    size = -(-len(files) // n)
    return [(f"{label} {i + 1}", files[i * size:(i + 1) * size]) for i in range(n)]


def count_pads(groups, singles=()):
    return sum(len(chunk(fs, cat)) for cat, fs in groups.items()) + len(singles)


def layout(groups, singles=()):
    """groups: {drum type: [wav]} -> one pad each (Sound knob picks the variation).
    singles: [(label, wav)] -> one pad per sample, placed after the drum-type pads."""
    pads, used, floating = [], set(), []
    for cat, note in FIXED.items():
        if cat not in groups:
            continue
        parts = chunk(groups[cat], cat)
        pads.append((note, parts[0][0], cat, parts[0][1]))
        used.add(note)
        floating += [(lbl, cat, fs) for lbl, fs in parts[1:]]
    for cat in FLOATING:
        if cat in groups:
            floating += [(lbl, cat, fs) for lbl, fs in chunk(groups[cat], cat)]
    floating += [(lbl, None, [wav]) for lbl, wav in singles]
    free = [n for n in range(36, 52) if n not in used] + list(range(52, 128))
    if len(floating) > len(free):
        raise ValueError("more pads than MIDI notes")
    for (lbl, cat, fs), note in zip(floating, free):
        pads.append((note, lbl, cat, fs))
    return sorted(pads, key=lambda p: p[0])


def map_param(param, macro_idx, lo, hi, value):
    km = param.find("KeyMidi")
    if km is None:
        km = ET.Element("KeyMidi")
        for tag, v in (("PersistentKeyString", ""), ("IsNote", "false"), ("Channel", "16"),
                       ("NoteOrController", "0"), ("LowerRangeNote", "-1"), ("UpperRangeNote", "-1"),
                       ("ControllerMapMode", "0")):
            ET.SubElement(km, tag, {"Value": v})
        param.insert(1 if len(param) and param[0].tag == "LomId" else 0, km)
    km.find("NoteOrController").set("Value", str(macro_idx))
    param.find("MidiControllerRange/Min").set("Value", fmt(lo))
    param.find("MidiControllerRange/Max").set("Value", fmt(hi))
    param.find("Manual").set("Value", fmt(value))


def strip_mappings(e):
    for p in list(e.iter()):
        for km in p.findall("KeyMidi"):
            p.remove(km)


def core_preset(rel):
    """A preset from Ableton Live's own Core Library, read from your Live installation (never shipped)."""
    return ET.fromstring(gzip.open(os.path.join(CORE_LIBRARY, rel)).read())


def load_templates():
    default = core_preset(os.path.join("Defaults", "Slicing", "Default.adg"))
    pad_tmpl = copy.deepcopy(default.find("GroupDevicePreset/BranchPresets/DrumBranchPreset"))
    dp = pad_tmpl.find("DevicePresets")
    for c in list(dp):
        dp.remove(c)

    k909 = core_preset(os.path.join("Racks", "Drum Racks", "Drum Machines", "909 Core Kit.adg"))
    kick = [p for p in k909.findall("GroupDevicePreset/BranchPresets/DrumBranchPreset")
            if p.find("ZoneSettings/ReceivingNote").get("Value") == "92"][0]
    rack_gdp = copy.deepcopy(kick.find("DevicePresets/GroupDevicePreset"))
    strip_mappings(rack_gdp)
    rack = rack_gdp.find("Device/InstrumentGroupDevice")
    for tag in ("LockId", "LockSeal"):
        rack.find(tag).set("Value", "0")
    rack.find("Annotation").set("Value", "")
    for i in range(16):
        rack.find(f"MacroDisplayNames.{i}").set("Value", f"Macro {i + 1}")
        rack.find(f"MacroControls.{i}/Manual").set("Value", "0")
        rack.find(f"MacroDefaults.{i}").set("Value", "-1")
        rack.find(f"MacroAnnotations.{i}").set("Value", "")
        rack.find(f"MacroColor.{i}").set("Value", "-1")
        rack.find(f"ForceDisplayGenericValue.{i}").set("Value", "false")
    snaps = rack.find("MacroVariations/MacroSnapshots")
    if snaps is not None:
        for s in list(snaps):
            snaps.remove(s)
    chains = rack_gdp.findall("BranchPresets/InstrumentBranchPreset")
    assert len(chains) == 1
    chain = chains[0]
    chain.find("Name").set("Value", "")
    holder = chain.find("DevicePresets/AbletonDevicePreset/Device")
    for c in list(holder):
        holder.remove(c)

    simpler = ET.parse(os.path.join(TEMPLATES, "simpler.xml")).getroot()
    normalize_ids(simpler)
    strip_mappings(simpler)
    simpler.find("UserName").set("Value", "")
    simpler.find("Globals/PlaybackMode").set("Value", "0")
    env = simpler.find("VolumeAndPan/Envelope")
    env.find("LoopMode/Manual").set("Value", "4")
    env.find("AttackTime/Manual").set("Value", "0.1000000015")
    env.find("DecayTime/Manual").set("Value", "1")
    env.find("DecayLevel/Manual").set("Value", "1")
    env.find("SustainLevel/Manual").set("Value", "1")
    env.find("ReleaseSlope/Manual").set("Value", "0")
    simpler.find("Filter/IsOn/Manual").set("Value", "true")
    sf = simpler.find("Filter/Slot/Value/SimplerFilter")
    sf.find("Type/Manual").set("Value", "0")
    sf.find("CircuitLpHp/Manual").set("Value", "0")
    sf.find("Res/Manual").set("Value", "0")
    sf.find("Drive/Manual").set("Value", "0")
    parts = simpler.find("Player/MultiSampleMap/SampleParts")
    part_tmpl = parts.find("MultiSamplePart")
    parts.remove(part_tmpl)
    for tag in ("InitialSlicePointsFromOnsets", "SlicePoints", "ManualSlicePoints", "BeatSlicePoints", "RegionSlicePoints"):
        for sp in list(part_tmpl.find(tag)):
            part_tmpl.find(tag).remove(sp)

    shell = ET.parse(os.path.join(TEMPLATES, "drum_rack.xml")).getroot()
    for b in list(shell.find("Branches")):
        shell.find("Branches").remove(b)
    idx = list(shell).index(shell.find("SourceContext"))
    shell.remove(shell.find("SourceContext"))
    shell.insert(idx, copy.deepcopy(default.find("GroupDevicePreset/Device/DrumGroupDevice/SourceContext")))
    for e in (pad_tmpl, rack_gdp, shell):
        normalize_ids(e)
    return default, pad_tmpl, rack_gdp, simpler, part_tmpl, shell


def make_part(part_tmpl, i, wav, preset_dir):
    p = copy.deepcopy(part_tmpl)
    p.set("Id", str(i))
    frames, rate = wav_info(wav)
    p.find("Name").set("Value", os.path.splitext(os.path.basename(wav))[0])
    p.find("Selection").set("Value", "true")
    for rng, lo, hi in (("KeyRange", 0, 127), ("SelectorRange", i + 1, i + 1)):
        for t, v in (("Min", lo), ("Max", hi), ("CrossfadeMin", lo), ("CrossfadeMax", hi)):
            p.find(f"{rng}/{t}").set("Value", str(v))
    p.find("RootKey").set("Value", "60")
    p.find("SampleStart").set("Value", "0")
    p.find("SampleEnd").set("Value", str(frames - 1))
    for loop in ("SustainLoop", "ReleaseLoop"):
        p.find(loop + "/Start").set("Value", "0")
        p.find(loop + "/End").set("Value", str(frames - 1))
    sr = p.find("SampleRef")
    rel = os.path.relpath(wav, preset_dir)
    set_fileref(sr.find("FileRef"), 1, rel, wav)
    set_fileref(sr.find("SourceContext/SourceContext/OriginalFileRef/FileRef"), 1, rel, wav)
    sr.find("SourceContext/SourceContext/BrowserContentPath").set("Value", browser_path(wav))
    sr.find("LastModDate").set("Value", str(int(os.path.getmtime(wav))))
    sr.find("DefaultDuration").set("Value", str(frames))
    sr.find("DefaultSampleRate").set("Value", str(rate))
    return p


def make_pad(t, pad_id, note, label, cat, files, preset_dir, choke=None):
    """choke: the machine's own cut-off group number (1-16), or None to use the hi-hat default."""
    default, pad_tmpl, rack_tmpl, simpler_tmpl, part_tmpl, shell = t
    pad = copy.deepcopy(pad_tmpl)
    pad.set("Id", str(pad_id))
    pad.find("Name").set("Value", "")
    zs = pad.find("ZoneSettings")
    zs.find("ReceivingNote").set("Value", str(128 - note))
    zs.find("SendingNote").set("Value", "60")
    zs.find("ChokeGroup").set("Value", str(choke) if choke is not None else ("1" if cat in HATS else "0"))
    pad.find("SourceContext/BranchSourceContext/BrowserContentPath").set("Value", "")

    rack_gdp = copy.deepcopy(rack_tmpl)
    rack = rack_gdp.find("Device/InstrumentGroupDevice")
    rack.find("UserName").set("Value", label)
    chain = rack_gdp.find("BranchPresets/InstrumentBranchPreset")
    s = copy.deepcopy(simpler_tmpl)
    parts = s.find("Player/MultiSampleMap/SampleParts")
    for i, wav in enumerate(files):
        parts.append(make_part(part_tmpl, i, wav, preset_dir))
    chain.find("DevicePresets/AbletonDevicePreset/Device").append(s)

    # Max 4 knobs per pad (2x2, like Ableton's own kits). Slot 1 picks the variation when the pad
    # has several sounds, otherwise it is Level; Tune / Decay / Tone always sit in the same spots.
    s.find("Player/SampleSelector/Manual").set("Value", "1")
    if len(files) > 1:
        first = ("Sound", 0, [(s.find("Player/SampleSelector"), 1, len(files), 1)])
    else:
        first = ("Level", LEVEL_0DB_MACRO, [(chain.find("MixerPreset/AbletonDevicePreset/Device/AudioBranchMixerDevice/Volume"), *LEVEL_RANGE, 1)])
    macros = [
        first,
        ("Tune", 63.5, [(s.find("Pitch/TransposeKey"), *TUNE_RANGE, 0)]),
        ("Decay", 127, [(s.find("VolumeAndPan/Envelope/ReleaseTime"), *DECAY_RANGE, DECAY_RANGE[1])]),
        ("Tone", 127, [(s.find("Filter/Slot/Value/SimplerFilter/Freq"), *TONE_RANGE, TONE_RANGE[1])]),
    ]
    assert len(macros) <= MAX_MACROS
    rack.find("AreDevicesVisible").set("Value", "true")  # show the Simpler (waveform) next to the knobs
    for i, (name, pos, targets) in enumerate(macros):
        rack.find(f"MacroDisplayNames.{i}").set("Value", name)
        rack.find(f"MacroControls.{i}/Manual").set("Value", fmt(pos))
        rack.find(f"MacroDefaults.{i}").set("Value", fmt(pos))
        for param, lo, hi, val in targets:
            map_param(param, i, lo, hi, val)
    rack.find("NumVisibleMacroControls").set("Value", str(len(macros)))
    pad.find("DevicePresets").append(rack_gdp)
    return pad


_TEMPLATES = None


def build_kit(pads, out_path, fx=None):
    """pads: [(note, label, drum type or None, [wav])] as returned by layout()."""
    global _TEMPLATES
    if _TEMPLATES is None:
        _TEMPLATES = load_templates()
    t = _TEMPLATES
    default, _, _, _, _, shell = t
    preset_dir = os.path.dirname(out_path)
    root = ET.Element("Ableton", HEADER)
    gdp = ET.SubElement(root, "GroupDevicePreset")
    ET.SubElement(gdp, "OverwriteProtectionNumber", {"Value": OPN})
    ET.SubElement(gdp, "Device").append(copy.deepcopy(shell))
    preset_ref = copy.deepcopy(default.find("GroupDevicePreset/PresetRef"))
    set_fileref(preset_ref.find("FilePresetRef/FileRef"), 6, os.path.relpath(out_path, USER_LIB), out_path)
    gdp.append(preset_ref)
    bp = ET.SubElement(gdp, "BranchPresets")
    for i, (note, label, cat, fs, *rest) in enumerate(pads):
        bp.append(make_pad(t, i, note, label, cat, fs, preset_dir, rest[0] if rest else None))
    ET.SubElement(gdp, "ReturnBranchPresets")
    if fx:                      # the machine's built-in effects as return chains
        add_returns(gdp, pads, fx, strip_mappings)
    normalize_ids(root)
    ET.indent(root, space="\t")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n"
    with gzip.open(out_path, "wb") as fh:
        fh.write(xml.encode("utf-8"))
    return pads


def verify(out_path, pads, fx=None):
    r = ET.fromstring(gzip.open(out_path).read())
    parent = {c: p for p in r.iter() for c in p}
    got = r.findall("GroupDevicePreset/BranchPresets/DrumBranchPreset")
    assert len(got) == len(pads)
    for pad, (note, label, cat, fs, *rest) in zip(got, pads):
        assert int(pad.find("ZoneSettings/ReceivingNote").get("Value")) == 128 - note
        if rest and rest[0] is not None:
            assert pad.find("ZoneSettings/ChokeGroup").get("Value") == str(rest[0]), (label, rest[0])
        rack = pad.find("DevicePresets/GroupDevicePreset/Device/InstrumentGroupDevice")
        assert rack.find("UserName").get("Value") == label
        n_macros = int(rack.find("NumVisibleMacroControls").get("Value"))
        assert n_macros == MAX_MACROS, (label, n_macros)
        assert rack.find("AreDevicesVisible").get("Value") == "true", label
        mapped = sorted(int(k.find("NoteOrController").get("Value")) for k in pad.iter("KeyMidi"))
        assert mapped == list(range(n_macros)), (label, mapped, n_macros)
        names = [rack.find(f"MacroDisplayNames.{i}").get("Value") for i in range(n_macros)]
        assert names == [("Sound" if len(fs) > 1 else "Level"), "Tune", "Decay", "Tone"], (label, names)
        s = pad.find(".//OriginalSimpler")
        msp = s.findall("Player/MultiSampleMap/SampleParts/MultiSamplePart")
        assert len(msp) == len(fs)
        for i, (part, wav) in enumerate(zip(msp, fs)):
            path = part.find("SampleRef/FileRef/Path").get("Value")
            assert path == wav and os.path.isfile(path)
            assert part.find("SelectorRange/Min").get("Value") == str(i + 1)
        assert s.find("Player/SampleSelector/Manual").get("Value") == "1"
        if len(fs) > 1:
            assert s.find("Player/SampleSelector/MidiControllerRange/Max").get("Value") == str(len(fs))
    verify_returns(r, pads, fx)
    for x in r.iter():
        if x.tag in ZERO_ID_TAGS:
            assert x.get("Id") == "0"
        if x.tag in ("LockId", "LockSeal"):
            assert x.get("Value") == "0"
    text = gzip.open(out_path).read().decode()
    for bad in ("ltisamples", "Kick 909 Tune", "Bass Drum 909"):
        assert bad not in text, "template leftover: " + bad
    return True


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_name(n):
    return f"{NOTE_NAMES[n % 12]}{n // 12 - 2}"

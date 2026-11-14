"""The machines' built-in effects as Drum Rack return chains.

Each machine with an effects processor gets one return chain per hardware effect (reverb, chorus,
flanger, delay), built from Live's own factory device presets, and every pad gets a send to each return
(the hardware's per-instrument send / depth / on-off switch). Effects that were on for drums by default
(the reverb) start with sends up; special effects (chorus, flanger, delay) start with sends down.

Live's preset format stores a return chain as an AudioEffectBranchPreset inside ReturnBranchPresets,
and a pad's send as an AudioBranchSendInfo in its mixer's SendInfos (layout copied from Live's own files:
a factory Audio Effect Rack and a Live Set)."""
import copy, gzip, math, os, sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from config import CORE_LIBRARY as CORE
AE = os.path.join(CORE, "Devices", "Audio Effects")
RACK_TMPL = os.path.join(CORE, "Racks", "Audio Effect Racks", "Performance & DJ", "Knob 1 Fade to Grey.adg")
SEND_MIN = 0.0003162277571                               # -70 dB = off

# hardware effect type -> (Live factory preset, device folder)
KINDS = {
    "room":       ("Reverb/Room/Medium Room.adv", "Reverb"),
    "small room": ("Reverb/Room/Small Room.adv", "Reverb"),
    "hall":       ("Reverb/Hall/Medium Hall.adv", "Reverb"),
    "plate":      ("Reverb/Room/Plate Damped.adv", "Reverb"),
    "chorus":     ("Chorus-Ensemble/Chorus Vintage.adv", "Chorus-Ensemble"),
    "flanger":    ("Phaser-Flanger/Flanger Default.adv", "Phaser-Flanger"),
    "delay":      ("Delay/Clean Delay/8th Note.adv", "Delay"),
}

# machine (as named in the setup research) -> its effects: (return name, type, on for drums by default)
# 'mix': the hardware fed the whole drum mix to the effect at one level (no per-instrument amount)
MACHINE_FX = {
    "Boss DR-660 Dr. Rhythm": {"returns": [("Reverb", "room", True), ("Chorus", "chorus", False)]},
    "Boss DR-202 Dr. Groove": {"returns": [("Reverb-Delay", "small room", True), ("Flanger", "flanger", False)]},
    "Quasimidi Rave-O-Lution 309": {"returns": [("FX-1 Reverb", "room", True), ("FX-2 Chorus", "chorus", False)]},
    "Korg M1 Music Workstation (drum kits)": {"mix": True, "returns": [("Effect 1 Reverb", "hall", True), ("Effect 2 Delay", "delay", False)]},
    "Roland MC-303 Groovebox": {"returns": [("Reverb", "room", True), ("Chorus", "chorus", False)]},
    "Roland D-110 Multi Timbral Sound Module (rhythm part)": {"mix": True, "returns": [("Reverb", "small room", True)]},
    "Roland D-70 Super LA Synthesizer (rhythm part)": {"returns": [("Reverb", "hall", True), ("Chorus", "chorus", False)]},
    "Roland JD-990 Super JD Synthesizer Module (rhythm set)": {"returns": [("Reverb", "hall", True), ("Chorus", "chorus", False), ("Delay", "delay", False)]},
    "Roland MT-32 Multi-Timbre Sound Module (rhythm part)": {"mix": True, "returns": [("Reverb", "room", True)]},
    "Yamaha CS6x / CS6R synthesizer (drum voices)": {"returns": [("Reverb", "hall", True), ("Chorus", "chorus", False)]},
    "Yamaha EX5 / EX5R / EX7 (drum voices)": {"returns": [("Reverb", "hall", True), ("Chorus", "chorus", False)]},
    "Yamaha TG33 vector tone generator (DR:Kit drum voice)": {"mix": True, "returns": [("Reverb Plate", "plate", True)]},
    "Kawai XD-5 Percussion Synthesizer": {"returns": [("Delay", "delay", False)]},
}
PREFIX = {"Korg T3": "Korg T3 Music Workstation", "Roland JD-800": "Roland JD-800 Programmable Synthesizer"}


def fx_for(machine):
    if not machine:
        return None
    if machine in MACHINE_FX:
        return MACHINE_FX[machine]
    if machine.startswith(PREFIX["Korg T3"]):           # same effect section as the M1
        return MACHINE_FX["Korg M1 Music Workstation (drum kits)"]
    if machine.startswith(PREFIX["Roland JD-800"]):
        return {"returns": [("Reverb", "hall", True), ("Chorus", "chorus", False), ("Delay", "delay", False)]}
    return None


def db(x):
    return 10 ** (x / 20)


def default_send(cat, on, mix):
    """Starting send level for one pad: reverb on, kick and bass dry, cymbals light."""
    if not on:
        return SEND_MIN
    if mix:
        return db(-14)
    if cat in ("Kick", "Bass"):
        return SEND_MIN
    if cat in ("Closed Hat", "Pedal Hat", "Open Hat", "Ride", "Crash", "Cymbal"):
        return db(-20)
    return db(-12)


def send_template():
    """One pad-to-return send, as Live writes it (level -70 dB = off)."""
    s = ET.Element("AudioBranchSendInfo", {"Id": "0"})
    send = ET.SubElement(s, "Send")
    ET.SubElement(send, "LomId", {"Value": "0"})
    ET.SubElement(send, "Manual", {"Value": "0.0003162277571"})
    rng = ET.SubElement(send, "MidiControllerRange")
    ET.SubElement(rng, "Min", {"Value": "0.0003162277571"})
    ET.SubElement(rng, "Max", {"Value": "1"})
    for tag in ("AutomationTarget", "ModulationTarget"):
        ET.SubElement(ET.SubElement(send, tag, {"Id": "0"}), "LockEnvelope", {"Value": "0"})
    ET.SubElement(s, "EnabledByUser", {"Value": "false"})
    ET.SubElement(s, "Index", {"Value": "0"})
    return s


_T = None


def templates():
    global _T
    if _T is None:
        rack = ET.fromstring(gzip.open(RACK_TMPL).read())
        branch = rack.find(".//BranchPresets/AudioEffectBranchPreset")
        wrapper = copy.deepcopy(branch.find("DevicePresets")[0])
        branch = copy.deepcopy(branch)
        for d in list(branch.find("DevicePresets")):
            branch.find("DevicePresets").remove(d)
        send = send_template()
        _T = branch, wrapper, send
    return _T


def send_info(idx, value, enabled):
    _, _, tmpl = templates()
    s = copy.deepcopy(tmpl)
    s.set("Id", str(idx))
    s.find("Send/Manual").set("Value", format(value, ".10g"))
    s.find("EnabledByUser").set("Value", "true" if enabled else "false")
    s.find("Index").set("Value", str(idx))
    return s


def device_preset(kind):
    rel, folder = KINDS[kind]
    dev = copy.deepcopy(ET.fromstring(gzip.open(os.path.join(AE, rel)).read())[0])
    if dev.find("DryWet/Manual") is not None:                 # a return chain is 100% wet
        dev.find("DryWet/Manual").set("Value", "1")
    if dev.tag == "Reverb":
        dev.find("MixDirect/Manual").set("Value", "1")
    _, wrapper, _ = templates()
    w = copy.deepcopy(wrapper)
    holder = w.find("Device")
    for c in list(holder):
        holder.remove(c)
    holder.append(dev)
    ref = w.find("PresetRef/AbletonDefaultPresetRef")
    fr = ref.find("FileRef")
    fr.find("RelativePath").set("Value", f"Devices/Audio Effects/{folder}")
    fr.find("Path").set("Value", os.path.join(AE, folder))
    ref.find("DeviceId").set("Name", dev.tag)
    return w


def strip(e, strip_mappings):
    strip_mappings(e)
    sc = e.find("SourceContext")
    if sc is not None:
        for c in list(sc):
            sc.remove(c)
        ET.SubElement(sc, "Value")


def add_returns(gdp, pads, fx, strip_mappings):
    """Append the return chains to ReturnBranchPresets and a send per return to every pad's mixer."""
    rets = fx["returns"]
    branch_tmpl, _, _ = templates()
    holder = gdp.find("ReturnBranchPresets")
    for k, (name, kind, on) in enumerate(rets):
        b = copy.deepcopy(branch_tmpl)
        b.set("Id", str(k))
        b.find("Name").set("Value", name)
        b.find("DevicePresets").append(device_preset(kind))
        mix = b.find("MixerPreset/AbletonDevicePreset/Device/AudioBranchMixerDevice")
        mix.find("Volume/Manual").set("Value", "1")
        sends = mix.find("SendInfos")
        for c in list(sends):
            sends.remove(c)
        for j in range(len(rets)):                           # return-to-return sends exist but stay off
            sends.append(send_info(j, SEND_MIN, False))
        strip(b, strip_mappings)
        holder.append(b)
    for pad_el, (note, label, cat, fs, *rest) in zip(gdp.find("BranchPresets"), pads):
        sends = pad_el.find("MixerPreset/AbletonDevicePreset/Device/AudioBranchMixerDevice/SendInfos")
        for c in list(sends):
            sends.remove(c)
        for j, (name, kind, on) in enumerate(rets):
            sends.append(send_info(j, default_send(cat, on, fx.get("mix")), True))
    gdp.find("Device/DrumGroupDevice/IsReturnBranchesListVisible").set("Value", "true")


def verify_returns(root, pads, fx):
    gdp = root.find("GroupDevicePreset")
    rets = gdp.findall("ReturnBranchPresets/AudioEffectBranchPreset")
    want = (fx or {}).get("returns", [])
    assert len(rets) == len(want), (len(rets), len(want))
    for b, (name, kind, on) in zip(rets, want):
        assert b.find("Name").get("Value") == name
        devs = b.findall("DevicePresets/AbletonDevicePreset/Device/*")
        assert len(devs) == 1 and devs[0].tag in ("Reverb", "Chorus2", "PhaserNew", "Delay"), [d.tag for d in devs]
        assert len(b.findall(".//SendInfos/AudioBranchSendInfo")) == len(want)
    for pad_el, (note, label, cat, fs, *rest) in zip(gdp.findall("BranchPresets/DrumBranchPreset"), pads):
        sends = pad_el.findall("MixerPreset/AbletonDevicePreset/Device/AudioBranchMixerDevice/SendInfos/AudioBranchSendInfo")
        assert len(sends) == len(want), (label, len(sends))
        for j, (s, (name, kind, on)) in enumerate(zip(sends, want)):
            v = float(s.find("Send/Manual").get("Value"))
            assert abs(v - default_send(cat, on, (fx or {}).get("mix"))) < 1e-6, (label, name, v)
    return True

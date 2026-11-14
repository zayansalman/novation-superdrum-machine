"""WAV header reading and small helpers for writing Ableton preset XML."""
import copy, gzip, os, re, struct, sys, urllib.parse
import xml.etree.ElementTree as ET

from config import PACKS_ROOT, USER_LIBRARY as USER_LIB


HEADER = {"MajorVersion": "5", "MinorVersion": "12.0_12402", "SchemaChangeCount": "5",
          "Creator": "Ableton Live 12.4.16", "Revision": "e33287a1c79501580a1e0f9f907e320757d3be44"}


OPN = "3076"


ZERO_ID_TAGS = {"AutomationTarget", "ModulationTarget", "Pointee", "AbletonDefaultPresetRef"}


def wav_info(path):
    with open(path, "rb") as f:
        b = f.read()
    if b[:4] != b"RIFF" or b[8:12] != b"WAVE":
        raise ValueError("not a RIFF/WAVE file")
    i, rate, align, data_size = 12, None, None, None
    while i + 8 <= len(b):
        cid, size = b[i:i + 4], struct.unpack("<I", b[i + 4:i + 8])[0]
        if cid == b"fmt ":
            _, _, rate, _, align = struct.unpack("<HHIIH", b[i + 8:i + 22])
        elif cid == b"data":
            data_size = min(size, len(b) - i - 8)
        i += 8 + size + (size & 1)
    if not rate or not align or data_size is None:
        raise ValueError("missing fmt/data chunk")
    frames = data_size // align
    if frames < 2:
        raise ValueError("empty audio")
    return frames, rate


def natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def normalize_ids(e):
    for x in e.iter():
        if x.tag in ZERO_ID_TAGS and "Id" in x.attrib:
            x.set("Id", "0")
        if x.tag == "OverwriteProtectionNumber":
            x.set("Value", OPN)


def browser_path(path):
    rel = os.path.relpath(path, PACKS_ROOT).split(os.sep)
    return "userfolder:" + PACKS_ROOT + "#" + ":".join(urllib.parse.quote(p, safe="") for p in rel)


def set_fileref(fr, rel_type, rel_path, abs_path):
    vals = {"RelativePathType": str(rel_type), "RelativePath": rel_path, "Path": abs_path, "Type": "2",
            "LivePackName": "", "LivePackId": "", "OriginalFileSize": "0", "OriginalCrc": "0", "SourceHint": ""}
    for k, v in vals.items():
        fr.find(k).set("Value", v)

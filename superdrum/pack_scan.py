"""Finding the samples in a pack, and splitting packs that hold more than one machine."""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ableton_xml import wav_info, natural_key
from drum_names import is_loop


KIT_FOLDER = re.compile(r"^kit\s*(\d+)$", re.I)


EXTRA_SPLITS = {("Linn LM1", "MT-32"): "Linn LM1 - MT-32"}


def pack_files(pack_dir):
    """Readable, non-loop WAVs. Returns (files, skipped[(relpath, reason)])."""
    files, skipped = [], []
    for dp, dn, fn in os.walk(pack_dir):
        dn.sort()
        for f in sorted(fn):
            if not f.lower().endswith(".wav") or f.startswith("._"):
                continue
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, pack_dir)
            if is_loop(rel):
                skipped.append((rel, "loop"))
                continue
            try:
                wav_info(path)
            except Exception as e:
                skipped.append((rel, str(e)))
                continue
            files.append(path)
    return files, skipped


def stem(path):
    return os.path.splitext(os.path.basename(path))[0]


def split_units(pack_name, pack_dir, files):
    """One unit per preset: (preset name, folder the names are read relative to, files)."""
    by_top = {}
    for f in files:
        rel = os.path.relpath(f, pack_dir)
        by_top.setdefault(rel.split(os.sep)[0] if os.sep in rel else "", []).append(f)
    if "" not in by_top and by_top and all(KIT_FOLDER.match(t) for t in by_top):
        return [(f"{pack_name} Kit {KIT_FOLDER.match(t).group(1)}", os.path.join(pack_dir, t), fs)
                for t, fs in sorted(by_top.items(), key=lambda kv: natural_key(kv[0]))]
    units, rest = [], []
    for top, fs in by_top.items():
        if (pack_name, top) in EXTRA_SPLITS:
            units.append((EXTRA_SPLITS[(pack_name, top)], os.path.join(pack_dir, top), fs))
        else:
            rest += fs
    if rest:
        units.insert(0, (pack_name, pack_dir, rest))
    return units

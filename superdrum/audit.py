"""Audit: tom/conga/bongo/timbale/agogo samples whose file name says low/mid/high but sit on a pad that
says otherwise; and pads whose default (first) sample is such a mismatch."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import load_specs, plan_pack, pos_hint, file_pos, PITCHED
from build_kits import load_types, safe
from packs import PACKS_ROOT, pack_names

specs = load_specs(); types, f0 = load_types()
wrong, first_wrong, kits = [], [], set()
for pack in pack_names():
    units, _ = plan_pack(pack, os.path.join(PACKS_ROOT, pack), specs, types, f0)
    for u, pads, how, m in units:
        for note, label, typ, fs, ch in pads:
            if typ not in PITCHED or (ph := pos_hint(label)) is None:
                continue
            bad = [f for f in fs if (fp := file_pos(f)) is not None and fp != ph]
            wrong += [(safe(u), label, os.path.basename(f)) for f in bad]
            if bad:
                kits.add(safe(u))
            if fs and fs[0] in bad:
                first_wrong.append((safe(u), label, os.path.basename(fs[0])))
print(f"{len(wrong)} samples on a pad that names a different pitch, in {len(kits)} kits; "
      f"{len(first_wrong)} pads play one by default")
for w in wrong[:40]:
    print("  wrong:", w)
for w in first_wrong:
    print("  DEFAULT wrong:", w)

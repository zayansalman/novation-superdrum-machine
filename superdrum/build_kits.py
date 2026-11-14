"""Build a Drum Rack preset for every pack, laid out like the real machine, and verify each file.

usage: python3 superdrum/build_kits.py [--effects] [PACK ...]
  --effects   add the machine's built-in effects as return chains (beta)
  PACK        only these packs (folder names); prints their pad layout"""
import json, os, re, shutil, sys, time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from packs import pack_names, PACKS_ROOT
from layout import load_specs, plan_pack, GROUP, PROBS, RM50_FAMILY
from kit_writer import build_kit, verify, note_name

from config import KITS_DIR as OUT_DIR, WORK
from data_files import sample_labels, sample_pitch
from effects import fx_for


def safe(name):
    return name.replace("/", "-").replace(":", "-").strip()


def load_types():
    final = sample_labels()
    for p, v in final.items():
        if v.get("probs"):
            PROBS[p] = v["probs"]
        nm = v.get("name")
        if nm and "/Yamaha RM 50/" in p:
            fam = re.sub(r"\d+$", "", nm.split()[-1]).lower()
            for key, label in RM50_FAMILY.items():
                if fam.startswith(key):
                    GROUP[p] = label
    f0 = {p: v["f0"] for p, v in sample_pitch().items() if v.get("f0") is not None}
    return {p: v["type"] for p, v in final.items()}, f0


def main(only=None, show=(), effects=False):
    t0 = time.time()
    types, f0 = load_types()
    specs = load_specs()
    built, report, failures = set(), [], []
    for pack in pack_names():
        if only and pack not in only:
            continue
        units, skipped = plan_pack(pack, os.path.join(PACKS_ROOT, pack), specs, types, f0)
        for unit, pads, how, machine in units:
            if not pads:
                failures.append((unit, "nothing playable"))
                continue
            out = os.path.join(OUT_DIR, safe(unit) + ".adg")
            fx = fx_for(machine) if effects else None
            try:
                os.makedirs(OUT_DIR, exist_ok=True)
                build_kit(pads, out, fx)
                verify(out, pads, fx)
            except Exception as e:
                failures.append((unit, repr(e)))
                continue
            built.add(os.path.basename(out))
            report.append({"pack": pack, "preset": os.path.basename(out), "machine": machine, "layout_kind": how,
                           "pads": len(pads), "samples": sum(len(p[3]) for p in pads),
                           "layout": [(p[0], p[1], len(p[3]), p[4]) for p in pads], "skipped": skipped})
            if unit in show:
                print(f"\n{unit}  ({how}; {machine})")
                for note, label, typ, fs, ch in pads:
                    print(f"  {note_name(note):4s} {label[:24]:24s} {len(fs):3d} sounds  choke {ch or '-'}")
    if not only:
        with open(os.path.join(WORK, "build_report.json"), "w") as fh:
            json.dump({"built": report, "failures": failures}, fh, indent=1)
    print(f"\nbuilt {len(report)} presets, {sum(r['samples'] for r in report)} samples in {time.time() - t0:.0f}s")
    for name, err in failures:
        print("FAILED:", name, "-", err)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--effects"]
    main(set(args) or None, show=set(args), effects="--effects" in sys.argv[1:])

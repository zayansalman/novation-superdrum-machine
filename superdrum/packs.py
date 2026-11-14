"""The 124 vintage drum machine packs the kits are built from (folder names under the packs folder)."""
import json, os

from config import DATA, PACKS_ROOT


def pack_names():
    with open(os.path.join(DATA, "packs.json")) as fh:
        return sorted(json.load(fh))

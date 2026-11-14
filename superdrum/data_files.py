"""Per-sample data that ships with the project, keyed by path relative to the packs folder:
sample_labels.json (what each sample is, and how we know) and sample_pitch.json (measured pitch)."""
import json, os

from config import DATA, PACKS_ROOT


def _load(name):
    with open(os.path.join(DATA, name)) as fh:
        return {os.path.join(PACKS_ROOT, k): v for k, v in json.load(fh).items()}


def sample_labels():
    return _load("sample_labels.json")


def sample_pitch():
    return _load("sample_pitch.json")

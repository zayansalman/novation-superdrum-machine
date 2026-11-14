"""Measure the pitch of every tunable drum sample (toms, congas, bongos, timbales, agogos, cowbells, wood
blocks) as the strongest spectral peak in the body of the sound: 10-300 ms after the hit, 40 Hz - 4 kHz.
The general pitch tracker in features.npz fails on many toms (it reads 1,575 Hz for nearly all of them).
Writes the 'body' field of data/sample_pitch.json."""
import json, os, sys, warnings

import numpy as np
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from config import DATA, PACKS_ROOT
from data_files import sample_labels
PITCHED = {"Tom", "Conga", "Bongo", "Timbale", "Agogo", "Cowbell", "Wood Block", "Perc"}   # Perc: may be retyped


def measure(path):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sr, x = wavfile.read(path)
    x = x.astype(np.float64)
    if x.ndim > 1:
        x = x.mean(axis=1)
    peak = np.max(np.abs(x)) if len(x) else 0
    if peak == 0:
        return None
    x = x / peak
    on = int(np.argmax(np.abs(x) > 0.1))
    a, b = on + int(0.010 * sr), min(len(x), on + int(0.300 * sr))
    seg = x[a:b] if b - a > int(0.020 * sr) else x[on:]
    if len(seg) < 64:
        return None
    seg = seg * np.hanning(len(seg))
    n = 1 << 16
    spec = np.abs(np.fft.rfft(seg, n))
    freqs = np.fft.rfftfreq(n, 1.0 / sr)
    band = (freqs >= 40) & (freqs <= 4000)
    return float(freqs[band][np.argmax(spec[band])])


def main():
    path = os.path.join(DATA, "sample_pitch.json")
    table = json.load(open(path)) if os.path.exists(path) else {}
    n, bad = 0, []
    for p, v in sample_labels().items():
        if v["type"] in PITCHED and os.path.exists(p):
            try:
                hz = measure(p)
            except Exception as e:
                hz = None
                bad.append((p, repr(e)[:80]))
            if hz:
                table.setdefault(os.path.relpath(p, PACKS_ROOT), {})["body"] = round(hz, 1)
                n += 1
    with open(path, "w") as fh:
        json.dump(table, fh, indent=0, sort_keys=True)
    print(f"measured {n} samples; {len(bad)} unreadable")
    for p, e in bad[:10]:
        print("  unreadable:", os.path.basename(p), e)


if __name__ == "__main__":
    main()

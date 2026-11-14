"""Lay each pack out like the real machine.

- Pads follow the machine's own voice order (front panel, or key map for synth kits), named as on the
  hardware. A voice's pad holds every sample of that voice (the Sound knob steps through them).
- Sounds that share a voice or cut each other off on the hardware get the same choke group.
- Samples the machine doesn't list (expansion chips, extras) go on extra pads after the panel voices.
- ROM modules and synths whose packs are just numbered waves are laid out by instrument instead.
Every sample's instrument comes from final_types.json (file name, official name, or the sound model).
"""
import glob, json, os, re, sys
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from drum_names import tokens
from ableton_xml import natural_key
from pack_scan import pack_files, split_units, stem

from config import RESEARCH
from data_files import sample_pitch
FIRST_NOTE, MAX_NOTE, MAX_VARIATIONS = 36, 127, 128
ORDER = ["Kick", "Snare", "Rim", "Clap", "Snap", "Closed Hat", "Pedal Hat", "Open Hat", "Tom", "Conga", "Bongo",
         "Timbale", "Cowbell", "Agogo", "Clave", "Wood Block", "Shaker", "Tambourine", "Triangle", "Crash", "Ride",
         "Cymbal", "Perc", "FX", "Bass", "Other"]
COMPAT = {"Cymbal": {"Cymbal", "Crash", "Ride"}, "Crash": {"Crash", "Cymbal"}, "Ride": {"Ride", "Cymbal"},
          "Closed Hat": {"Closed Hat", "Pedal Hat"}, "Perc": {"Perc"}}
HATS = {"Closed Hat", "Pedal Hat", "Open Hat"}
PITCHED = {"Tom", "Conga", "Bongo", "Timbale", "Agogo", "Cowbell", "Wood Block"}
GENERIC_TOKENS = {"drum", "drums", "tom", "toms", "snare", "bass", "kick", "hat", "hats", "hihat", "hi", "cymbal",
                  "conga", "bongo", "the", "and", "voice", "sound", "of", "a"}
SPLIT_SPECS = {"Linn LM1 - MT-32": "Roland MT-32"}     # a different machine's sounds inside a pack
BANK_TYPES = {"Cymbal": ["Closed Hat", "Pedal Hat", "Open Hat", "Ride", "Crash", "Cymbal"],
              "Perc": ["Conga", "Bongo", "Timbale", "Cowbell", "Agogo", "Clave", "Wood Block", "Shaker",
                       "Tambourine", "Triangle", "Clap", "Snap", "Rim", "Perc"],
              "FX": ["FX", "Bass"]}


def load_specs():
    specs = {}
    for f in sorted(glob.glob(os.path.join(RESEARCH, "*.json"))):
        for m in json.load(open(f)):
            for p in m.get("pack_folders", []):
                specs[p] = m
    for unit, pack in SPLIT_SPECS.items():
        specs[unit] = specs[pack]
    return specs


def ntokens(text):
    """Word tokens with numbers normalised ('01' == '1')."""
    return [str(int(t)) if t.isdigit() else t for t in tokens(text or "")]


def alias_tokens(text):
    out = set()
    for t in ntokens(text):
        out.add(t)
        if t in ("low", "lo", "l"):
            out |= {"low", "lo"}
        if t in ("high", "hi", "h"):
            out |= {"high", "hi"}
        if t in ("mid", "md", "m", "med", "middle"):
            out |= {"mid", "md", "med"}
    return out - GENERIC_TOKENS


def voice_rank(v, i):
    """Higher number = lower pitch, so pitch-sorted samples can be dealt out to same-type voices."""
    n = (v.get("label", "") + " " + v.get("name", "")).lower()
    if re.search(r"\b(low|lo|floor)\b|\blt\b|\blc\b", n):
        return 2
    if re.search(r"\b(mid|md)\b|\bmt\b|\bmc\b", n):
        return 1
    if re.search(r"\b(high|hi)\b|\bht\b|\bhc\b", n):
        return 0
    d = re.findall(r"\d+", v.get("label", ""))
    return int(d[-1]) if d else i


POS_WORDS = {"low": 0, "lo": 0, "lowest": 0, "floor": 0, "bottom": 0, "mid": 1, "md": 1, "med": 1, "middle": 1,
             "high": 2, "hi": 2, "highest": 2, "top": 2}
POS_CODES = {"lt": 0, "lc": 0, "lb": 0, "ft": 0, "mt": 1, "mc": 1, "ht": 2, "hc": 2, "hb": 2}
POS_LETTERS = {"l": 0, "m": 1, "h": 2}
ABBREV = {"op": "open", "opn": "open", "mut": "mute", "mte": "mute", "slp": "slap"}   # 'TR-727Conga_HiOp'
TECH = {"mute": "mute", "muted": "mute", "damp": "mute", "dampened": "mute", "open": "open", "slap": "slap"}


def technique(tokens_, hand_drum=False):
    """Playing technique a name gives: mute / open / slap, or None. On a hand-drum voice 'Mt' means muted."""
    found = {TECH[t] for t in tokens_ if t in TECH}
    if hand_drum and "mt" in tokens_:
        found.add("mute")
    return found.pop() if len(found) == 1 else None
DRUM_WORDS = ("tom", "cong", "bong", "timb", "tumba", "quinto", "agogo", "cowbel", "bell", "block", "wood")


def pos_hint(text, letters=False):
    """Low/mid/high written in a name -> 0/1/2 (None if it says nothing or two things).
    Whole words first ('Hi Tom'), then codes ('LT'); single letters ('Tom H') only for file names that
    also name the drum."""
    toks = ntokens(text)
    for table in (POS_WORDS, POS_CODES):
        found = {table[t] for t in toks if t in table}
        if found:
            return found.pop() if len(found) == 1 else None
    if letters and any(t.startswith(DRUM_WORDS) for t in toks):
        found = {POS_LETTERS[t] for t in toks if t in POS_LETTERS}
        if len(found) == 1:
            return found.pop()
    return None


def voice_pos(v):
    return pos_hint(f"{v.get('label', '')} {v.get('name', '')}")


def file_pos(path):
    return pos_hint(stem(path), letters=True)


# path -> Hz of the strongest peak in the body of the hit (measured by pitch.py)
BODY_PITCH = {p: v["body"] for p, v in sample_pitch().items() if v.get("body")}


def pad_name(v):
    """Voice name as printed on the machine, without research notes in brackets."""
    n = re.sub(r"\s*\(.*?\)", "", v.get("name") or "").strip() or (v.get("label") or "").strip()
    return n.title() if n.isupper() else n


def voice_accepts(v, typ):
    return typ in COMPAT.get(v["type"], {v["type"]})


def is_sound_voice(v):
    return v.get("type") not in (None, "", "Other") or "accent" not in (v.get("name", "") + v.get("label", "")).lower()


def deal_by_pitch(samples, voices, f0, placed=None):
    """Split pitched samples over same-type voices. When every voice already holds samples named for it
    ('Tom H' on Hi Tom), each sample goes to the voice whose named samples are nearest in pitch;
    otherwise highest pitch to the highest voice."""
    hz = lambda s: BODY_PITCH.get(s) or f0.get(s) or 0
    empty = [iv for iv in voices if not (placed or {}).get(iv[0])]
    if placed and empty and len(empty) < len(voices) and len(samples) <= len(empty):
        voices = empty      # DX: 'Tom Hi' and 'Tom Lo' are named, so the unnamed 'Tom_E' is the mid tom
    anchors = {i: [hz(s) for s in (placed or {}).get(i, []) if hz(s)] for i, _ in voices}
    span = [h for a in anchors.values() for h in a]
    inside = span and all(min(span) / 1.25 <= hz(s) <= max(span) * 1.25 for s in samples if hz(s))
    if all(anchors.values()) and inside:      # the named samples bracket the unnamed ones
        out = defaultdict(list)
        for s in samples:
            if hz(s):
                i = min(anchors, key=lambda i: abs(np.log(hz(s)) - np.log(float(np.median(anchors[i])))))
                out[i].append(s)
            else:
                out[voices[0][0]].append(s)
        return out
    vs = sorted(voices, key=lambda iv: voice_rank(iv[1], iv[0]))           # high .. low
    ss = sorted(samples, key=lambda s: -BODY_PITCH.get(s, f0.get(s, 0)))    # high .. low
    out = defaultdict(list)
    for k, s in enumerate(ss):
        out[vs[min(len(vs) - 1, k * len(vs) // max(1, len(ss)))][0]].append(s)
    return out


PROBS = {}          # path -> {type: probability} from the sound model (filled by the builder)
GENERIC_WORDS = {"perc", "percussion", "per", "prc", "fx", "sfx", "misc", "other", "sound", "snd", "hit"}


def is_flexible(path, typ):
    """A sample named only 'Perc 3' / 'FX 2': its file name doesn't say which instrument it is."""
    return typ in ("Perc", "FX") and bool(GENERIC_WORDS & set(tokens(stem(path))))


def retype_flexible(voices, files, types):
    """Offer generically named samples to the machine's own voices, preferring voices still empty."""
    vtypes = {v["type"] for v in voices}
    filled = {types[f] for f in files if not is_flexible(f, types[f])}
    out = dict(types)
    for f in files:
        if not is_flexible(f, types[f]) or f not in PROBS:
            continue
        best, score = None, 0.0
        for t in vtypes - {"Perc", "FX"}:
            sc = PROBS[f].get("Crash" if t == "Cymbal" else t, 0) + (0.15 if t not in filled else 0)
            if sc > score:
                best, score = t, sc
        if best and score >= 0.25:
            out[f] = best
    return out


def pitch_groups(hz):
    """How many clearly different pitches (neighbours more than 25% apart)."""
    hz = sorted(h for h in hz if h)
    return (1 + sum(b / a > 1.25 for a, b in zip(hz, hz[1:]))) if hz else 0


def deal_hand_drums(voices, by_type, by_voice):
    """Packs often call every hand drum 'Conga': the CR-78 packs' 'Conga H/M/L' (and 'CR78Perc04-06') are
    its High Bongo, Low Bongo and Low Conga - the same three pitches, ~620/410/208 Hz, in both packs.
    When a machine has bongos and its conga-named samples come in more clearly different pitches than it
    has conga voices, deal them (with any bongo samples) over all its hand drums, highest pitch to the
    highest bongo. Moves the dealt files out of by_type."""
    bongos = [(i, v) for i, v in enumerate(voices) if v["type"] == "Bongo"]
    congas = [(i, v) for i, v in enumerate(voices) if v["type"] == "Conga"]
    loose = [f for f in by_type.get("Conga", []) if "bong" not in stem(f).lower()]
    if not bongos or not congas or pitch_groups(BODY_PITCH.get(f) for f in loose) <= len(congas):
        return
    fs = by_type.pop("Conga", []) + by_type.pop("Bongo", [])
    vs = sorted(bongos, key=lambda iv: voice_rank(iv[1], iv[0])) + sorted(congas, key=lambda iv: voice_rank(iv[1], iv[0]))
    ss = sorted(fs, key=lambda s: -BODY_PITCH.get(s, 0))
    for k, s in enumerate(ss):
        by_voice[vs[min(len(vs) - 1, k * len(vs) // len(ss))][0]].append(s)


def assign(voices, files, types, f0):
    """-> ({voice index: [files]}, {type: [extra files]}, name-matched share)."""
    by_voice, extras, matched = defaultdict(list), defaultdict(list), 0
    types = retype_flexible(voices, files, types)
    by_type = defaultdict(list)
    for f in files:
        by_type[types[f]].append(f)
    deal_hand_drums(voices, by_type, by_voice)
    # words every file shares (pack prefix such as "M1", "TR-707") say nothing about the voice
    df = defaultdict(int)
    for f in files:
        for tk in set(ntokens(stem(f))):
            df[tk] += 1
    shared = {tk for tk, n in df.items() if len(files) >= 5 and n >= 0.8 * len(files)}
    ftok = {f: {ABBREV.get(t, t) for t in ntokens(stem(f))} - shared for f in files}
    for typ, fs in by_type.items():
        cand = [(i, v) for i, v in enumerate(voices) if voice_accepts(v, typ)]
        if not cand:
            extras[typ] += fs
            continue
        if len(cand) == 1:
            by_voice[cand[0][0]] += fs
            continue
        left = []
        for f in fs:
            ft = ftok[f]
            pool = cand
            if typ in PITCHED and (fp := file_pos(f)) is not None and all(voice_pos(v) is not None for _, v in cand):
                # 'Tom H' / 'TR-909Tom Hi 02' / 'Conga L-01' go to the voice with the same low/mid/high
                # (only when every voice says which it is: DMX 'Tom 1'..'Tom 6' are dealt by pitch instead)
                pool = [iv for iv in cand if voice_pos(iv[1]) == fp] or cand
                if len(pool) > 1:   # 'Mute Hi Conga' vs 'Open Hi Conga': a plain 'Conga H' is the open one
                    want = technique(ft) or "open"
                    pool = [iv for iv in pool if (technique(ntokens(f"{iv[1].get('label', '')} {iv[1].get('name', '')}"),
                                                            hand_drum=iv[1]["type"] in ("Conga", "Bongo", "Timbale")) or "open") == want] or pool
            best = max(pool, key=lambda iv: len(alias_tokens(iv[1].get("label")) & ft) * 2
                       + len(alias_tokens(iv[1].get("name")) & ft))
            score = len((alias_tokens(best[1].get("label")) | alias_tokens(best[1].get("name"))) & ft)
            if score or pool is not cand:
                by_voice[best[0]].append(f); matched += 1
            else:
                left.append(f)
        if left:
            exact = [iv for iv in cand if iv[1]["type"] == typ] or cand
            if typ in PITCHED and len(exact) > 1:
                for i, fl in deal_by_pitch(left, exact, f0, by_voice).items():
                    by_voice[i] += fl
            else:
                by_voice[exact[0][0]] += left
    # a pad's first sample is the one it plays by default: on a 'Low Conga' pad put 'Conga L' before 'Conga H'
    order = {f: k for k, f in enumerate(files)}
    for i, fl in by_voice.items():
        vp = voice_pos(voices[i]) if voices[i]["type"] in PITCHED else None
        if vp is not None:
            fl.sort(key=lambda f: (1 if file_pos(f) is None else 2 * abs(file_pos(f) - vp), order.get(f, 0)))
    return by_voice, extras, matched / max(1, len(files))


RM50_FAMILY = {"log": "Log Drum", "talk": "Talking Drum", "bott": "Bottle", "whist": "Whistle", "guiro": "Guiro",
               "yoru": "Yoru", "metal": "Metal", "popm": "Pop Perc", "melob": "Melodic Bell", "anamu": "Analog Perc",
               "tekd": "Tek Perc", "tmpl": "Temple Block", "casc": "Cascara"}
GROUP = {}          # path -> pad name for instruments the type list has no word for (filled by the builder)


def group_of(path, typ):
    return GROUP.get(path) or typ


def by_instrument(files, types, order):
    """-> [(pad name, type, files)] in the given type order."""
    groups = defaultdict(list)
    for f in files:
        groups[(types[f], group_of(f, types[f]))].append(f)
    rank = {t: k for k, t in enumerate(list(order) + [t for t in ORDER if t not in order])}
    keys = sorted(groups, key=lambda tg: (rank.get(tg[0], 999), tg[1] != tg[0], tg[1]))
    return [(g, t, sorted(groups[(t, g)], key=lambda p: natural_key(os.path.basename(p)))) for t, g in keys]


def pad_labels(voices):
    """{voice index: pad name}; the bracket stays when it is what tells two pads apart."""
    label_of = {i: pad_name(v) for i, v in enumerate(voices)}
    dup = {n for n in label_of.values() if list(label_of.values()).count(n) > 1}
    for i, v in enumerate(voices):
        if label_of[i] in dup:
            full = re.sub(r"\s+", " ", v.get("name") or "").strip()
            label_of[i] = full if full != label_of[i] else f"{label_of[i]} {v.get('label', '')}".strip()
    return label_of


def chunked(label, typ, fs, choke):
    if len(fs) <= MAX_VARIATIONS:
        return [(label, typ, fs, choke)]
    n = -(-len(fs) // MAX_VARIATIONS); size = -(-len(fs) // n)
    return [(f"{label} {k + 1}", typ, fs[k * size:(k + 1) * size], choke) for k in range(n)]


def plan_unit(name, base_dir, files, spec, types, f0):
    """-> pads [(note, label, type, files, choke)] and a note on how it was laid out."""
    voices = [v for v in (spec or {}).get("voices") or [] if v.get("type") and v.get("type") != "Other"]
    files = sorted(files, key=lambda p: natural_key(os.path.relpath(p, base_dir)))
    bank_style = voices and (all("bank" in (v.get("name") or "").lower() for v in voices)
                             or any(re.search(r"\bsection\b|on key", v.get("name") or "", re.I) for v in voices))
    slots, how = [], ""
    if voices and not bank_style:
        by_voice, extras, share = assign(voices, files, types, f0)
        synth_kit = (spec.get("kind") in ("synth with drum kit", "drum sound module", "sampler/groovebox")
                     and len(voices) > 20 and share < 0.3)
        if not synth_kit:
            label_of = pad_labels(voices)
            choke_of = {}
            for g, members in enumerate(spec.get("choke_groups") or [], start=1):
                for i, v in enumerate(voices):
                    if v.get("label") in members:
                        choke_of.setdefault(i, g)
            for i, v in enumerate(voices):
                if by_voice.get(i):
                    slots.append((i, label_of[i], v["type"], by_voice[i], choke_of.get(i)))
            nxt = len(voices)
            for label, typ, fs in by_instrument([f for fl in extras.values() for f in fl], types, ORDER):
                slots.append((nxt, label, typ, fs, None)); nxt += 1
            how = "machine layout"
    if not slots:
        order = []
        if bank_style:
            for v in voices:
                order += BANK_TYPES.get(v["type"], [v["type"]])
        for k, (label, typ, fs) in enumerate(by_instrument(files, types, order or ORDER)):
            slots.append((k, label, typ, fs, None))
        how = "by instrument (machine's section order)" if bank_style else "by instrument"
    # hats cut each other off unless the research gave the machine its own groups
    used = {s[4] for s in slots if s[4]}
    if not any(s[4] for s in slots if s[2] in HATS):
        g = max(used, default=0) + 1
        slots = [(i, l, t, fs, g if t in HATS else c) for i, l, t, fs, c in slots]
    pads = []           # in the machine's order, one after another: missing voices leave no empty pad
    for i, label, typ, fs, choke in slots:
        for lab, t, part, ch in chunked(label, typ, fs, choke):
            pads.append((FIRST_NOTE + len(pads), lab, t, part, ch))
    if pads and pads[-1][0] > MAX_NOTE:
        raise ValueError(f"{name}: needs {pads[-1][0] - FIRST_NOTE + 1} pads")
    return pads, how


def plan_pack(pack, pack_dir, specs, types, f0):
    files, skipped = pack_files(pack_dir)
    files = [f for f in files if f in types]
    out = []
    for unit, base, fs in split_units(pack, pack_dir, files):
        spec = specs.get(unit) or specs.get(pack)
        pads, how = plan_unit(unit, base, fs, spec, types, f0)
        out.append((unit, pads, how, spec["machine"] if spec else None))
    return out, skipped


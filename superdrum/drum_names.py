"""Guess the drum type of a sample from its file name (falling back to its folder name)."""
import re

CATEGORIES = [
    "Kick", "Rim", "Snare", "Clap", "Closed Hat", "Pedal Hat", "Open Hat", "Tom", "Crash", "Ride",
    "Cowbell", "Clave", "Conga", "Bongo", "Timbale", "Agogo", "Shaker", "Tambourine", "Triangle",
    "Wood Block", "Snap", "Cymbal", "Perc", "FX",
]

# A melodic sample named after a note, e.g. "fatbass-c2" or "bass_F#3".
NOTE_SUFFIX = re.compile(r"[-_ ][a-g](#|s|b)?-?\d$", re.I)
LOOP = re.compile(r"loop|(^|[^a-z])lp\d", re.I)


def tokens(text):
    text = re.sub(r"\.wav$", "", text, flags=re.I)
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", text)
    text = re.sub(r"([A-Za-z])(\d)", r"\1 \2", text)
    text = re.sub(r"(\d)([A-Za-z])", r"\1 \2", text)
    return [t for t in re.split(r"[^a-z0-9]+", text.lower()) if t]


def is_loop(relpath):
    return bool(LOOP.search(relpath))


def classify(relpath):
    parts = relpath.split("/")
    stem = re.sub(r"\.wav$", "", parts[-1], flags=re.I)
    cat = _classify(tokens(stem), melodic=bool(NOTE_SUFFIX.search(stem)))
    if cat is None and len(parts) > 1:
        cat = _classify(tokens(" ".join(parts[:-1])), melodic=False)
    return cat


def _classify(ts, melodic):
    j = "".join(ts)

    def has(*words):
        return any(w in ts for w in words)

    def sub(*subs):
        return any(s in j for s in subs)

    def starts(*prefixes):
        return any(t.startswith(p) for t in ts for p in prefixes)

    def ends(*suffixes):
        return any(t.endswith(s) for t in ts for s in suffixes)

    if sub("rimshot", "sidestick", "crossstick") or has("rim", "rims", "rs", "stick", "sticks") or starts("rim"):
        return "Rim"
    if sub("agogo", "agog"):
        return "Agogo"
    if sub("cowbell") or has("cow", "cb", "cowb"):
        return "Cowbell"
    if not melodic and (sub("kick", "bassdrum", "bassdr") or has("bd", "kik", "kck")
                        or (sub("bass") and not has("conga", "tom", "toms"))):
        return "Kick"
    if sub("handclap", "clap") or has("cp", "clp", "hc", "cla"):
        return "Clap"
    if sub("hihat", "hat") or has("hh", "hhc", "hho", "chh", "ohh", "phh", "ch", "oh", "ph", "cht", "oht", "pht",
                                  "longhi", "shorthi") or starts("hh"):
        if has("oh", "ohh", "hho", "o", "open", "op", "opn", "oht", "longhi") or sub("open") or starts("hhop", "hho"):
            return "Open Hat"
        if has("ph", "phh", "pedal", "ped", "foot", "pht") or sub("pedal") or starts("hhp"):
            return "Pedal Hat"
        return "Closed Hat"
    if sub("snare", "brush") or has("sd", "snr", "sn", "snar", "longsn", "shortsn") or starts("snar", "nare"):
        return "Snare"
    if sub("conga", "tumba", "quinto", "cng") or has("cga"):
        return "Conga"
    if sub("bongo") or has("bgo"):
        return "Bongo"
    if sub("timbale", "timbal") or has("timb", "tmb"):
        return "Timbale"
    if has("tt", "lt", "ht", "ft") or starts("tom") or ends("tom", "toms"):
        return "Tom"
    if sub("crash", "splash", "china"):
        return "Crash"
    if sub("ride") or has("rd", "rde", "cup") or ends("cup"):
        return "Ride"
    if sub("cymbal") or has("cym", "cy", "cymb", "edge", "choke") or starts("cym"):
        return "Cymbal"
    if sub("clave") or has("clv", "cl"):
        return "Clave"
    if sub("shaker", "shake", "maraca", "cabasa", "cabassa", "afuche") or has("shk", "shkr", "mrc", "cab"):
        return "Shaker"
    if sub("tamb", "tamborine", "tambourine", "tambourin") or has("tmbrn"):
        return "Tambourine"
    if sub("triangle") or has("tri", "trngl"):
        return "Triangle"
    if sub("woodblock", "block", "wood", "temple") or has("wb", "blk", "log"):
        return "Wood Block"
    if sub("snap", "finger"):
        return "Snap"
    if sub("perc", "cuica", "cuic", "whistle", "vibra", "chime", "gong", "click", "metal", "quijada", "guiro",
           "guira", "surdo", "slap", "castanet", "tsuzumi", "timp", "bell", "hiq") or has("per"):
        return "Perc"
    if sub("noise", "fx", "sfx", "laser", "sweep", "rev", "scratch", "hit", "orch", "zap", "blast"):
        return "FX"
    return None

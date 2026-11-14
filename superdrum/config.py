"""Where things live. Every path can be overridden with an environment variable."""
import glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _live_app():
    if os.environ.get("SUPERDRUM_LIVE_APP"):
        return os.environ["SUPERDRUM_LIVE_APP"]
    apps = sorted(glob.glob("/Applications/Ableton Live 12*.app"))
    return apps[-1] if apps else ""


# the vintage drum machine sample packs (one folder per pack, as Splice downloads them)
PACKS_ROOT = os.environ.get("SUPERDRUM_PACKS", os.path.expanduser("~/Splice/sounds/packs"))
# your Ableton User Library: kits go to Presets/Instruments/Drum Rack, clips to Clips/Drum Machine Patterns
USER_LIBRARY = os.environ.get("SUPERDRUM_USER_LIBRARY", os.path.expanduser("~/Music/Ableton/User Library"))
# Ableton's Core Library inside your Live installation (templates and effect presets are read from it)
CORE_LIBRARY = os.environ.get("SUPERDRUM_CORE_LIBRARY",
                              os.path.join(_live_app(), "Contents", "App-Resources", "Core Library"))

KITS_DIR = os.path.join(USER_LIBRARY, "Presets", "Instruments", "Drum Rack")
CLIPS_DIR = os.path.join(USER_LIBRARY, "Clips", "Drum Machine Patterns")
RESEARCH = os.path.join(ROOT, "research", "machine-setups")
BEATS = os.environ.get("SUPERDRUM_BEATS", os.path.join(ROOT, "research", "beats"))
DATA = os.path.join(ROOT, "data")
TEMPLATES = os.path.join(ROOT, "templates")
WORK = os.environ.get("SUPERDRUM_WORK", os.path.join(ROOT, "work"))      # build reports and caches
os.makedirs(WORK, exist_ok=True)

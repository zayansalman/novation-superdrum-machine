# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed

- README: the samples come from free vintage drum-machine sample archives, not Splice. Those archives allow
  use in music but not re-sharing, so the samples are still not included.

## [0.1.0] - 2026-11-14

First public release.

### Added

- Kit builder (`superdrum/build_kits.py`): 146 Drum Rack presets from 124 vintage drum-machine packs
  covering 96 machines.
- Machine-accurate layouts. Pads start at C1 in the hardware's panel order, with no empty pads. They carry
  the hardware's voice names, and extra sounds sit after the panel voices. Packs that hold two machines
  (for example, MT-32 sounds inside the Linn LM-1 pack) become separate kits.
- Choke groups taken from the hardware: shared circuits, hi-hat pairs, the TR-808 tom/conga and
  claves/rim switches, and the DMX channels.
- Four knobs per pad in a 2x2 grid (Sound or Level, Tune, Decay, Tone). Every recorded variation of a voice
  sits on one pad, and the Sound knob picks between them.
- Low/mid/high placement for toms, congas, bongos, timbales and agogos. Names such as "Hi", "Lo",
  "Tom H" and "Conga L-01" are read first. The rest are placed by the measured pitch of each sample's body
  (`superdrum/pitch.py`, `data/sample_pitch.json`).
- Hand-drum identification. The CR-78 packs' "Conga H/M/L" samples are its high bongo, low bongo and low
  conga, identified by the machine's voice list and their pitches (about 620, 410 and 208 Hz).
- Open/mute/slap matching for congas: "Op", "Mut" and "Slp" in file names.
- Built-in effects as Drum Rack return chains (`--effects`, beta) for 15 machines with an effects
  processor, with a send on every pad. Reverb is on by default; chorus, flanger and delay start at zero.
- MIDI clip writers: `beat_clips.py` writes patterns of famous records from your own pattern files, and
  `preset_clips.py` writes factory preset rhythms. Lanes are matched to pads by sound type and name, swing
  and accents are supported, and every file is read back to check it.
- Live Clip writer (`live_clips.py`, experimental): a kit and a beat in one `.alc` file.
- Audit tool (`superdrum/audit.py`) for tom/conga placement.
- Research notes for all 96 machines (`research/`), and labels for all 6,078 samples (`data/`).

### Not included

- Audio samples (their archives allow use but not re-sharing), Ableton factory content (read from your Live installation), and
  transcribed drum patterns (third-party sources). See the README for details.

[0.1.0]: https://github.com/zayansalman/novation-superdrum-machine/releases/tag/v0.1.0

# novation-superdrum-machine

**Ableton Live Drum Racks for 96 vintage drum machines, laid out the way the real machines were.**

This project turns 124 vintage drum-machine sample packs into 146 ready-to-play Ableton Live Drum Rack
presets. Each kit follows the real hardware: the pads come in the machine's own front-panel order and carry
the names printed on the hardware. Sounds that cut each other off on the machine (open and closed hi-hats, the
TR-808's tom/conga switch, the DMX's shared channels) share a choke group. Each pad holds every recorded
variation of its voice, with four knobs: **Sound** (or **Level**), **Tune**, **Decay** and **Tone**.

Every machine's layout comes from research into its manual, service notes, reviews and teardowns. That
research is included, with sources, in [`research/`](research/).

> Not affiliated with or endorsed by Novation, Focusrite, Ableton, Splice, Roland, Linn, Oberheim, E-mu,
> Yamaha, Korg, Boss, Alesis or any other manufacturer named here. All trademarks belong to their owners.

## What you get

- **146 Drum Rack presets** for 96 machines, from the Roland TR-808, CR-78 and LinnDrum to the Oberheim
  DMX, Yamaha RX5, Korg Mini Pops and Boss DR-55.
- **Machine-accurate layouts:**
  - pads start at C1 in panel order, with no empty pads;
  - extra sounds (expansion chips, alternate takes) sit after the panel voices;
  - packs that hold two machines are split into two kits.
- **Choke groups** wherever the hardware cut sounds off.
- **Right drum, right pad.** Low, mid and high toms, congas and bongos are matched by name first, then by the
  measured pitch of each sample.
- **Built-in effects (beta).** Machines with an effects processor get it as Drum Rack return chains, using
  each machine's own effect types, with a send on every pad:
  - Boss: DR-660, DR-202.
  - Roland: D-110, D-70, JD-800, JD-990, MT-32, MC-303.
  - Korg: M1, T3.
  - Yamaha: CS6x, EX5, TG33.
  - Others: Quasimidi 309, Kawai XD-5.
- **Clip tools:**
  - write MIDI clips from step-grid pattern data;
  - turn a clip and its kit into a Live Clip (`.alc`, experimental) so one drag loads both.

## What is not included, and why

| Not included | Why | What to do |
|---|---|---|
| The audio samples | Splice's licence lets you use samples in your music but not redistribute them | Download the packs to your own Splice library ([`data/packs.json`](data/packs.json) lists them) |
| Ableton's factory files | Ableton's content licence | Read from your own Live installation at build time |
| Drum patterns of famous records and factory preset rhythms | Transcribed from third-party charts, tabs and manuals | Add your own pattern files; see [`research/beats/README.md`](research/beats/README.md) |

## Requirements

- macOS (Windows should work with the environment variables below, but is untested)
- Ableton Live 12 (built and tested with 12.4 Suite; the Core Library must be installed)
- Python 3.10 or newer, with `numpy` and `scipy`
- The vintage drum-machine packs in your Splice library, at `~/Splice/sounds/packs` by default

## Quick start

```bash
git clone https://github.com/zayansalman/novation-superdrum-machine.git
cd novation-superdrum-machine
python3 -m pip install -r requirements.txt
python3 superdrum/build_kits.py
```

The kits land in your User Library. In Live's browser, find them under **Drums**, or under
**User Library → Presets → Instruments → Drum Rack**.

More commands:

```bash
python3 superdrum/build_kits.py --effects            # add built-in effects as return chains (beta)
python3 superdrum/build_kits.py "Roland TR-808"      # one pack, and print its pad layout
python3 superdrum/audit.py                           # check toms/congas sit on the right pads
python3 superdrum/beat_clips.py                      # MIDI clips from research/beats/*.json
python3 superdrum/live_clips.py --all                # a Live Clip (kit + beat) next to every .mid clip
```

### Configuration

Every location can be overridden with an environment variable:

| Variable | Default | What it is |
|---|---|---|
| `SUPERDRUM_PACKS` | `~/Splice/sounds/packs` | Folder that holds one folder per sample pack |
| `SUPERDRUM_USER_LIBRARY` | `~/Music/Ableton/User Library` | Where kits and clips are written |
| `SUPERDRUM_LIVE_APP` | newest `/Applications/Ableton Live 12*.app` | Your Live installation |
| `SUPERDRUM_CORE_LIBRARY` | Core Library inside the Live app | Ableton's factory content |
| `SUPERDRUM_BEATS` | `research/beats` | Your pattern files for `beat_clips.py` |
| `SUPERDRUM_WORK` | `work/` | Build reports and caches |

## How it works

1. **What is each sample?** [`data/sample_labels.json`](data/sample_labels.json) says what each of the 6,078
   samples is and how we know. The answer comes from, in order: the machine's official sound list (for
   numbered banks, such as the Yamaha RM50's), the file name, or a sound model checked against machines it
   had not heard.
2. **How was the real machine laid out?**
   [`research/machine-setups/`](research/machine-setups/) holds one entry per machine: voices in panel order,
   which voices share a circuit or cut each other off, per-voice controls, built-in effects, and sources. The
   full write-up is [`research/vintage-drum-machine-setups.md`](research/vintage-drum-machine-setups.md).
3. **Lay out the pads** ([`superdrum/layout.py`](superdrum/layout.py)). Samples go to the machine's voices
   by name. Toms, congas and bongos are placed by the low/mid/high in their names, then by measured pitch
   ([`data/sample_pitch.json`](data/sample_pitch.json)).
4. **Write the Drum Rack** ([`superdrum/kit_writer.py`](superdrum/kit_writer.py)) with the structure Live
   itself uses, then read every file back to verify it: pads, notes, choke groups, knobs and sample paths.
5. **Optional extras:**
   - effects ([`effects.py`](superdrum/effects.py));
   - MIDI clips ([`beat_clips.py`](superdrum/beat_clips.py), [`preset_clips.py`](superdrum/preset_clips.py));
   - Live Clips ([`live_clips.py`](superdrum/live_clips.py)).

## Status and known limitations

- **Built-in effects** and **Live Clips** pass the file checks but have not been confirmed loading in every
  Live version yet.
- Some packs only number their files. For those, labels come from the sound model, and the research notes
  how confident each kit is. Corrections are very welcome.
- The scripts that made the sample labels (feature extraction, sound model, official-list alignment) are not
  published yet. Their output ships as data, so builds are reproducible.
- Effect types use Live's own devices (Reverb, Chorus-Ensemble, Phaser-Flanger, Delay) as stand-ins for the
  hardware's effects.

## Contributing

Corrections to machine layouts are the most valuable contribution: a wrong voice order, a missing choke
group, a mislabelled sample. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE) for the code, research notes and data in this repository. The samples, Ableton's content and
the sources cited in the research belong to their respective owners.

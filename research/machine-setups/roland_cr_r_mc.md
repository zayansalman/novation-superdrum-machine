# Roland CompuRhythm (CR-78, CR-8000, CR-1000), R-series (R-5, R-8), DDR-30 and MC-series (MC-303, MC-09, MC-202): hardware setup, presets, famous beats, pack contents

Research notes, 2026-11-13. Two scanned Roland owner's manuals were read page by page: CR-78 (print code "'80 NOV A-3") and CR-8000 (print code "'83 JUL B-3"). They are the primary sources for the CR section. The R-5, R-8, MC-303, DDR-30, MC-09 and MC-202 owner's manuals could not be opened. ManualsLib shows a bot-check page, archive.org was unreachable from this environment, soundprogramming.net PDF links redirect to its homepage, and Roland's own manual pages sit behind a licence click-through. For those machines, the notes rely on period magazine reviews, Roland spec and feature pages, and Wikipedia (secondary). The shared web-search budget ran out partway through, so the coverage of famous recordings is thin for every machine except the CR-78.

## Q1. Voices in front-panel or owner's-manual order, with exact labels

### Takeaway
The CR-78 has 11 programmable sounds plus 3 extra sounds controlled by sliders (Tambourine, Guiro, Metallic Beat). The CR-8000 has 14 sound names, set by 6 level knobs, and only 11 of them (plus Accent) can be programmed. The R-5 and R-8 have no fixed voices: they have 68 ROM instruments assigned to 16 pads. The DDR-30 has 6 fixed voice channels (bass drum, snare, toms 1 to 4). The MC-202 has no drum voices at all.

### Cited Findings
**CR-78 (1978)**
- Manual intro text: "With 11 kinds of percussion instruments as the sound source, there are 34 different preset rhythm patterns. Along with this, 2 kinds of ADD VOICE and METALLIC BEAT, plus CANCEL VOICE…" — [CR-78 Owner's Manual (scan)](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- SOUND SOURCE list in the spec sheet, in order: BASS DRUM, SNARE DRUM, RIM SHOT, HI-HAT, CYMBAL, MARACAS, CLAVES, COW BELL, HIGH BONGO, LOW BONGO, LOW CONGA. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- ADD VOICE control sliders: TAMBOURINE LEVEL, GUIRO LEVEL. "CY HH METALLIC BEAT" control slider: METALLIC BEAT LEVEL. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- Programmer INSTRUMENTS SELECTOR knob positions: Bass Drum, Snare Drum, Rim Shot, High Hat, Cymbal, Maracas, Claves, High Bongo, Low Bongo, Low Conga, Accent. Tambourine, Guiro and Metallic Beat cannot be programmed. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- The manual's text abbreviates only a few voices: "cymbal (CY.)", "high hat (HH.)", "HB: High Bongo, SD: Snare Drum". Everything else is printed in full words. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- Default MIDI notes in the Cherry Audio CR-78 emulation (software, not the hardware, which had no MIDI): BD 36, RS 37, SD 38, Claves 39, Accent 40, Low Conga 41, HH 42, Low Bongo 43, Metallic Beat 44, High Bongo 45, Tambourine 46, Low Guiro 48, Cymbal 49, High Guiro 50, Maracas 51, Cowbell 52. The emulation splits the guiro into "Low Guiro" and "High Guiro". — [Cherry Audio CR-78 docs](https://docs.cherryaudio.com/cherry-audio/instruments/cr-78/midi-sound-module)
- Roland's own history article lists "high hats" in the plural, and describes the Metallic Beat as a "buzzy, electronic-sounding" extra cymbal/hi-hat pattern. — [Roland, "CR-78: The Whole Story"](https://articles.roland.com/?p=75463)

**CR-8000 (1981)**
- VOICE LEVEL knobs, left to right on the front panel: BASS DRUM | TOM TOM / RIM SHOT / SNARE DRUM | CONGA | CLAVES / COWBELL | CYMBAL / HI HAT | HAND CLAP. ACCENT and VOLUME knobs follow. — [CR-8000 Owner's Manual p.4 (scan)](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- SOUND SOURCES in the spec sheet: BASS DRUM, SNARE DRUM, LOW TOM, HI TOM, HI-HAT, OPEN HI-HAT, CYMBAL, RIM SHOT, LOW CONGA, MIDDLE CONGA, HI CONGA, COWBELL, CLAVES, HAND CLAP. — [CR-8000 manual p.19](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- PROGRAM INSTRUMENT SELECTOR, as listed in the spec sheet: BASS DRUM, SNARE DRUM, LOW TOM, HI TOM, HI-HAT, OPEN HI-HAT, CYMBAL, COWBELL, MIDDLE CONGA, LOW CONGA, HAND CLAP, ACCENT. The knob is printed BD, SD, LT, HT, HH, OHH, CY, CB, MC, LC, CP, AC. Rim shot, claves and hi conga do not appear on it. — [CR-8000 manual pp.4, 19](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- The preset grids also use the row labels RS (rim shot, in Bossa Nova), HC (hi conga, in Samba and Mambo) and "C" (in Rhumba and Beguine). — [CR-8000 manual pp.12-15](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- A secondary source lists 13 sounds and says they sit on 6 sound channels: ch1 kick; ch2 snare, toms and rimshot; ch3 conga; ch4 claves and cowbell; ch5 cymbal and hi-hats; ch6 claps. — [polynominal CR-8000](https://www.polynominal.com/roland-cr8000/)

**CR-1000 "Digital Drummer" (1986)**
- Secondary source only: 16 PCM sounds (8-bit, 25 kHz, 128 kb ROM, not expandable), listed as "kick, snare, rimshot, clap, tom (x3), timbale, hh (open/close), crash, cymbal, tambourine, claves, conga (x2)". The page also calls the unit a preset-only version of the TR-505 with the same samples. Panel labels and order are not given. — [polynominal CR-1000](https://www.polynominal.com/roland-cr1000/)

**R-8 (1989)**
- 68 internal instruments, 26 "copy" instruments (internal sounds with their own settings), and 26 "external" instruments from a ROM card. — [Music Technology, Feb 1989 (Simon Trask)](https://www.muzines.co.uk/articles/roland-r8/2188); [Roland R-8 spec page (search snippet)](https://support.roland.com/hc/en-us/articles/201940509-R-8-Technical-Specifications)
- 16 instrument pads, velocity- and pressure-sensitive. One review counts 20 pads in total, including start/stop/continue, roll, flam and erase/shift. — [Home & Studio Recording, Mar 1989 (Derek Johnson)](https://www.muzines.co.uk/articles/roland-r8/1373)
- Instruments are grouped into Pad Banks: five kits of 16 pads, so 80 instruments are available at once. The same review later says "six Pad Banks", which conflicts. — [Music Technology, Feb 1989](https://www.muzines.co.uk/articles/roland-r8/2188); [H&SR, Mar 1989](https://www.muzines.co.uk/articles/roland-r8/1373)

**R-5 (1989)**
- Same instrument count as the R-8 (68 internal, 26 copy). 20 of the voices differ from the R-8, among them electronic kick and snare, jazz snare, rimshot 3, electronic and jazz toms, timbale, bongo, surdo and blast. — [Music Technology, Jul 1989 (Nigel Lord)](https://www.muzines.co.uk/articles/roland-r5/102)
- The R-5 owner's manual is 259 pages. Its table of contents puts the "Instrument List" on p.229, followed by default settings and preset patterns. — [ManualsLib R-5 (TOC via search)](https://www.manualslib.com/manual/691657/Roland-R-5.html)

**DDR-30 (1985)**
- 6 voices: bass drum, snare and four toms. The bass-to-tom-4 order comes from prototype knob labels that were later removed. — [Wikipedia DDR-30](https://en.wikipedia.org/wiki/Roland_DDR-30)
- 6 XLR pad inputs (PD-20 pads, PD-10/PD-11 kick). The module can also be triggered over MIDI, e.g. from an Octapad (Pad-8). — [Wikipedia DDR-30](https://en.wikipedia.org/wiki/Roland_DDR-30)

**MC-303 (1996)**
- One rhythm part and seven melodic parts. 12 rhythm kits, using sounds drawn from the TR-909, TR-808 and CR-78 plus general drums and percussion. — [Sound On Sound, Aug 1996](https://www.soundonsound.com/reviews/roland-mc303)
- Wikipedia lists the kits as including CR-78, TR-808, TR-606 and TR-909, plus electro, techno, jungle, house, drum & bass and breakbeat kits. — [Wikipedia MC-303](https://en.wikipedia.org/wiki/Roland_MC-303)

**MC-09 PhraseLab (2002)**
- "Rhythm" part with 3-voice polyphony and 10 preset rhythm tones. "Analog-type rhythm sounds". Drum patterns are programmed TR-REC style. The individual drum instruments are not named on Roland's pages. — [Roland MC-09 specs](https://www.roland.com/us/products/mc-09/specifications/); [Roland MC-09 features](https://www.roland.com/us/products/mc-09/features/)

**MC-202 (1983)**
- A monophonic synth with no drum voices: one VCO (saw plus square/pulse-width plus a sub-octave square), a 24 dB resonant low-pass filter, a single ADSR, and an LFO with delay. It lacks the SH-101's noise generator. — [Wikipedia MC-202](https://en.wikipedia.org/wiki/Roland_MC-202); [Vintage Synth Explorer MC-202](https://www.vintagesynth.com/roland/mc-202)

### Inferences
- CR-78: the hardware has one HI-HAT voice. Neither manual mentions an open hi-hat, so a separate open-hat sample in a pack is not a hardware voice (inferred). It may be the cymbal, the metallic beat, or an accented or long hat.
- CR-8000: in the RHUMBA and BEGUINE grids, "C" is claves (inferred). Those grids use CB for cowbell and CY for cymbal, and claves is the only other C-instrument left.
- MC-09: the pack holds exactly 10 each of Kick, Snare, closed hat and open hat. That suggests each of the 10 preset rhythm tones is a 4-instrument kit (BD, SD, CH, OH), but no Roland source confirms it (inferred).

### Gaps
- Official ordered instrument lists for the R-5 (manual p.229) and R-8, the MC-303's 12 rhythm-set names and its tone list, and the DDR-30's per-voice waveform names. The manuals hold them but could not be opened (bot-check or unreachable hosts).
- Exact panel labels and order for the CR-1000 (only a secondary source was available).

## Q2. Sounds that share one voice or cut each other off (open/closed hat and others)

### Takeaway
The CR-78 documents no chokes. Its cancel buttons mute CY+HH and CB+CL in pairs. On the CR-8000, SD/RS/LT/HT, CB/CL and CY/HH/OHH each share one level knob, and per a secondary source they share one sound channel. The R-8 and R-5 have assignable exclusive groups 1 to 8. Choke behaviour for the other machines is undocumented.

### Cited Findings
- CR-78 CANCEL BUTTONS (4): "CYMBAL + HIGH HAT, BASS DRUM, SNARE DRUM, COW BELL + CLAVES". These mute voices in the presets. The manual does not say any voices cut each other off. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- CR-78: Metallic Beat follows the cymbal/hi-hat pattern of the preset. With the Cymbal/High Hat cancel on, the cymbal and hi-hat are cancelled and Metallic Beat plays an 8-beat rhythm instead. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- CR-8000 shared level knobs: "SNARE DRUM/RIM SHOT/TOM TOM", "COWBELL/CLAVES", "CYMBAL/HI HAT/OPEN HI-HAT". — [CR-8000 manual p.19](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- CR-8000 shared channels: ch2 snare/toms/rimshot, ch4 claves/cowbell, ch5 cymbal/hi-hats. — [polynominal CR-8000](https://www.polynominal.com/roland-cr8000/)
- R-8: each instrument has an assign mode (Mono, Poly or Exclusive). Exclusive groups are numbered 1 to 8, "so instruments such as open and closed hi-hats can be prevented from sounding together". — [Music Technology, Feb 1989](https://www.muzines.co.uk/articles/roland-r8/2188); [H&SR, Mar 1989](https://www.muzines.co.uk/articles/roland-r8/1373)
- Attack Magazine's CR-78-sample beat explicitly uses "no chokes or mute groups". — [Attack, "CR-78 Redux" (2016)](https://www.attackmagazine.com/technique/beat-dissected/cr-78-redux/)

### Inferences
- CR-8000: HH/OHH should be a choke group in a Drum Rack. A shared channel means SD/RS/LT/HT and CB/CL probably cannot sound at the same instant (inferred, not verified by measurement). The factory fill grids never stack those voices on one step, which fits a shared channel.
- R-5: probably uses the same assign/exclusive system as the R-8, since the MT review says it shares the R-8's architecture (inferred).
- DDR-30: each of the 6 voices has its own channel and individual output, so a hit re-triggers its own voice only (inferred).

### Gaps
- Default exclusive-group settings on the R-5 and R-8, and the hat behaviour on the CR-1000, MC-303 and MC-09: not found.

## Q3. Per-voice controls, accent, flam, shuffle, feel and tuning

### Takeaway
The CR machines have no per-voice tuning or decay. The CR-78 offers balance, cancel buttons, add-voice levels and a global accent. The CR-8000 offers 6 group level knobs, a global accent, a shuffle button and a crash button. The R-8 and R-5 add per-instrument pitch, decay, nuance, pan and velocity curve, plus Feel Patches and flam/roll pads. The DDR-30 edits attack, decay, pitch, EQ, bend and gate per voice. The MC-202 and MC-09 have TB-303-style accent and slide in their sequencers.

### Cited Findings
**CR-78**
- ACCENT ("Accent Volume") knob: "regulates the amount of accentuation. Turning it to the right strengthens the accent." Accents are built into the presets. In the programmer, the ACCENT position of the instrument selector records accents. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- BALANCE: "Sliding it upward will emphasize the high percussion sounds (cymbal, high hat, maracas) and sliding it downward will emphasize the low percussion sounds (bass drum)." A secondary source describes it as a "simple lowpass filter". — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf); [polynominal CR-78](https://www.polynominal.com/roland-cr78/)
- VARIATION selector: FILL IN 1-7, BREAK (one bar of rhythm, then one bar of rest), RHYTHM (A-B) (switches to the other variation), ROLLING-HB / SD (adds a high bongo or snare roll). MEASURE selector 2/4/8/12/16 sets the variation cycle. AUTO/MANUAL switch, MANUAL button, and FADE IN / FADE OUT (long and short). — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- Pressing two rhythm buttons at once combines the two patterns. Pressing three selects two of them by priority. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- Programmer: "Four voices can be used for each rhythmic pattern and four rhythmic patterns, each of two measures (96 counts), can be memorized." Program buttons I-IV and track LEDs 1-4. Patterns are written in real time with the TS-1 switch or a DP-1/DP-2 pedal on the WRITE jack. The optional WS-1 "divides the rhythm pattern into steps of either 8-12-24 or 48." — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- Rear panel: TRIG OUT with an "8"/16"/COMBI" switch. COMBI outputs "the pulse of the output of the bass drum, and the high bongo combined". EXT CLOCK at 48 counts per measure (+5 to +15 V). — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)

**CR-8000**
- "The Accent can give emphasis to any other voices programmed on the same step. The Level control adjusts the amount of emphasis." Accent is a global step row (AC). — [CR-8000 manual pp.1, 5](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- ARRANGER buttons: CY-4" (4-beat cymbal), CY-8" (8-beat cymbal), HH-4" (4-beat hi-hat), HH-16" (16-beat hi-hat), Open HH (8-beat after-beat open hi-hat), CONGA (a combination of hi, mid and lo conga), HAND CLAP (4-beat hand clap, after-beat), SHUFFLE. — [CR-8000 manual p.7](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- SHUFFLE changes every rhythm to a shuffle beat, except WALTZ, SWING-1, SWING-2, SLOW ROCK and programs written with 12-step bars. CRASH inserts the cymbal's crash sound on the first beat when a rhythm moves from intro/fill-in to basic. REGISTER plays two patterns alternately. — [CR-8000 manual pp.7-8](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- Programming: 16 steps per bar and two bars (32 steps). With shuffle, 12 steps per bar (24 steps). 8 programmable basic rhythms. Intro/fill-in programs #9-#12 hold one bar each. Intro/fill-in presets 1-8, with auto fill every 16/12/8/4/2 bars or manual. — [CR-8000 manual pp.6, 9](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- Trigger out (+5 V, 10 ms) selectable 8"/16"/ACC. DIN SYNC IN/OUT (CSQ-600, MC-4, JP-8 arpeggio). Remote jacks: START/STOP, RESTART, INTRO/FILL-IN, REGISTER. — [CR-8000 manual pp.3, 19](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)

**CR-1000**
- Variation controls are listed as shuffle groove amount, accent button, intro/ending, fill-in, rhythm variation, accent level and clap variation. 9 knobs. MIDI IN/THRU responds to note on/off only. Tempo 40-240. — [polynominal CR-1000](https://www.polynominal.com/roland-cr1000/)

**R-8 and R-5**
- R-8 per-instrument settings: Pitch ±4800 cents, Decay, Nuance (strike position), velocity curve 1-8, assign mode, and output/pan (7 stereo positions or 8 separate outs). Pads can add offsets to pitch, decay, nuance and pan. — [Music Technology, Feb 1989](https://www.muzines.co.uk/articles/roland-r8/2188); [H&SR, Mar 1989](https://www.muzines.co.uk/articles/roland-r8/1373)
- Eight Feel Patches, each with Groove and Random settings that vary velocity, pitch, nuance and decay. Roll and Flam are pad functions. Quantise 1/4 to 1/96, with micro-shift to 1/384. Tempo 20-250. — [H&SR, Mar 1989](https://www.muzines.co.uk/articles/roland-r8/1373); [Wikipedia R-8](https://en.wikipedia.org/wiki/Roland_R-8)
- R-5: eight Feel Patches. The feel and nuance parameters carry over from the R-8. Quantise is limited to 1/96. Lower tempo limit is 40 bpm. Micro/Macro timing shift and naming are missing. — [Music Technology, Jul 1989](https://www.muzines.co.uk/articles/roland-r5/102)

**DDR-30**
- 16 editable parameters in edit groups: Attack, Decay, Pitch, EQ, Bend, Gate. Mix section: volume, treble, bass for all voices. No panning. — [Wikipedia DDR-30](https://en.wikipedia.org/wiki/Roland_DDR-30)

**MC-303**
- Per part: a three-stage envelope (attack, decay, release), filter cutoff and resonance, LFO, portamento, and two effects. Edits are saved with the pattern. In drum step recording, Shift plus a pad picks the drum sound, with four editable velocity values. Quantise options are Grid, Shuffle and Groove. — [Sound On Sound, Aug 1996](https://www.soundonsound.com/reviews/roland-mc303); [Wikipedia MC-303](https://en.wikipedia.org/wiki/Roland_MC-303)

**MC-09**
- Step sequencer up to 32 steps at 16th-note resolution, emulating TB-303 sequencing including slides and accents. Six control knobs. — [Roland MC-09 specs](https://www.roland.com/us/products/mc-09/specifications/); [Roland MC-09 features](https://www.roland.com/us/products/mc-09/features/)

**MC-202**
- Each sequencer note can carry an accent and a slide, "similar to the TB-303". Two sequencer channels: one plays the internal synth, the other goes out via CV/gate. DIN sync in/out works with the TB-303 and TR-808. FSK tape sync. — [Wikipedia MC-202](https://en.wikipedia.org/wiki/Roland_MC-202)
- Synth controls: VCO (saw, square/PWM, sub-oscillator); VCF cutoff, resonance, envelope, modulation and keyboard tracking; VCA set to envelope or gate; LFO rate and delay. — [Vintage Synth Explorer MC-202](https://www.vintagesynth.com/roland/mc-202)

### Inferences
- Drum Rack mapping for the CR-78 and CR-8000: one global accent, applied to every voice on accented steps, is the faithful choice. Do not add per-voice tune or decay macros, because the hardware has none. Group level macros fit the CR-8000.
- MC-202 drum sounds (inferred from its architecture; no source describes this): short pitched thumps for kicks and toms from a self-oscillating or high-resonance filter, or a low VCO note with fast decay, punched up with the step accent. Clicks from a very short envelope with the filter open. Snares, hats and cymbals cannot be made properly without noise, so the usual approach is a drum machine slaved over DIN sync (e.g. TR-606/TR-808). The pack's "Bassdrum", "Click" and "Tom H" samples fit this kind of pitched synth percussion (inferred).

### Gaps
- Factory pitch ranges and per-pad defaults for the R-5. DDR-30 parameter ranges and velocity response. MC-09 rhythm-tone parameters. CR-1000 accent behaviour beyond the control names.

## Q4. Built-in effects

### Takeaway
None on the CR-78, CR-8000, CR-1000, R-5, R-8, DDR-30 or MC-202. The MC-303 has reverb/delay and chorus/flanger, plus a low-boost knob. The MC-09 has 30 effect types, among them filter, isolator, phaser, slicer, overdrive, distortion and ring mod.

### Cited Findings
- CR-78: no effects are listed in the manual specs. Fade in/out and the Balance slider are the only tone and level shaping. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- CR-8000: no effects in the specs. Single mono output. — [CR-8000 manual p.19](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- R-8: "No audio effects are described". Roll, Flam and Macros are performance functions, not audio effects. — [Music Technology, Feb 1989](https://www.muzines.co.uk/articles/roland-r8/2188)
- DDR-30: no effects mentioned. The only tone shaping is per-voice EQ and global treble/bass. — [Wikipedia DDR-30](https://en.wikipedia.org/wiki/Roland_DDR-30)
- MC-303: Reverb/Delay and Chorus/Flanger, two effects per sound, plus a rear-panel Low Boost knob. — [Sound On Sound, Aug 1996](https://www.soundonsound.com/reviews/roland-mc303); [Wikipedia MC-303](https://en.wikipedia.org/wiki/Roland_MC-303)
- MC-09: 30 effect types. Four built-in algorithms (Filter, Isolator, Phaser, Slicer) can be driven from the step sequencer. The lead group adds Overdrive, Distortion, Phaser, Slicer and Ring Modulator. — [Roland MC-09 specs](https://www.roland.com/us/products/mc-09/specifications/)

### Inferences
- Whether the MC-303's reverb and chorus can be applied to the rhythm part is not stated. SOS does not say. It is likely, since effects are set per part (inferred).

### Gaps
- MC-303 effect routing for the drum part. CR-1000 outputs beyond the mono out.

## Q5. ROM machines: sound counts, categories, official ordered lists, kit layout and MIDI map

### Takeaway
Counts are well sourced: R-8 and R-5 have 68 internal + 26 copy instruments; MC-303 has 448 tones and 12 rhythm sets; DDR-30 has 48 preset sounds (8 per voice); MC-09 has 10 rhythm tones; CR-1000 has 16 PCM sounds. No official ordered list or default MIDI note map could be retrieved for any of them.

### Cited Findings
- R-8 categories (review counts, no number ranges): 9 bass drums, 12 snares + 2 side sticks (H&SR) or 14 snares (MT), 13 toms, 3 hi-hats (one pedal-closed), 5 cymbals, 1 TR-808-style hand clap, 13 Latin/ethnic (agogo, cowbell, congas, whistle, clave, plus a Japanese taiko), 2 whistles, reversed snare/tom/cymbal, effect sounds ("Surf", "Wheel1"), and a silent "Rest". Named copy instruments include Shadow, Gunshot, Pipe and Thriller. — [H&SR, Mar 1989](https://www.muzines.co.uk/articles/roland-r8/1373); [Music Technology, Feb 1989](https://www.muzines.co.uk/articles/roland-r8/2188)
- R-8: 16-bit samples, 32-voice polyphony, 4-part multitimbral, 32 preset and 100 user patterns, 10 songs, 32 user kits. ROM cards SN-R8-01 to SN-R8-11: Contemporary Percussion, Jazz Brush, Sound Effects, Electronic, Jazz, Ethnic Percussion, Mallet, Dry, Power Drums U.S.A., Dance, Metallic Percussion. — [soundprogramming R-8](https://soundprogramming.net/drum-machines/roland/roland-r-8); [Wikipedia R-8](https://en.wikipedia.org/wiki/Roland_R-8)
- R-5: 68 internal instrument voices and 26 copy voices (Roland spec, via search snippet). 32 preset and 100 user patterns. — [Roland R-5 spec (search snippet)](https://support.roland.com/hc/en-us/articles/201937679-R-5-Technical-Specifications); [Music Technology, Jul 1989](https://www.muzines.co.uk/articles/roland-r5/102)
- MC-303: 448 tones and 12 complete rhythm sets ("448 Tones und 12 kompletten Rhythmus Sets"). 40 synth basses, 35 synth leads and 33 synth pads are among the tones. 28-voice polyphony. — [Roland DE MC-303 page (search snippet)](https://www.roland.com/de/products/mc-303/); [Wikipedia MC-303](https://en.wikipedia.org/wiki/Roland_MC-303)
- DDR-30: "48 ROM sounds" (8 bass drums, 8 snares, 32 toms), 32 user kits (soundprogramming). Wikipedia says four 12-bit PCM samples per voice (24 in all), plus 48 patches (8 per voice) and 32 kits. A search-result excerpt of the manual says "up to 8 different sounds per voice (total of 48 sounds)". — [soundprogramming DDR-30](https://soundprogramming.net/drum-machines/roland/roland-ddr-30); [Wikipedia DDR-30](https://en.wikipedia.org/wiki/Roland_DDR-30)
- MC-09: preset tones are Lead 128, Bass 128, Rhythm 10. Polyphony is Lead 1, Bass 1, Rhythm 3. — [Roland MC-09 specs](https://www.roland.com/us/products/mc-09/specifications/)
- CR-1000: 16 PCM sounds, 8 voices of polyphony, MIDI IN/THRU, note on/off only. — [polynominal CR-1000](https://www.polynominal.com/roland-cr1000/)
- MC-303 documents on Roland's site: Owner's Manual, Quick Start, a System Exclusive PDF, TurboStart and Advanced MIDI Programming. — [Roland MC-303 owner's manuals](https://www.roland.com/global/support/by_product/mc-303/owners_manuals/)

### Inferences
- The DDR-30 numbers fit one scheme: 4 PCM samples per voice, shaped into 8 factory patches per voice, giving 48 "sounds" (8 BD + 8 SD + 4×8 toms). The pack has 8 BD, 8 SD and 8 tom files, which matches one patch set per voice type (inferred).

### Gaps
- Official ordered lists: R-8 and R-5 instrument lists (R-5 manual p.229), MC-303 tone and rhythm-set lists, DDR-30 waveform names, and the MC-09 rhythm-tone list. Default MIDI note maps and pad bank layouts for all of them. All are inside manuals that could not be opened in this session.

## Q6. Pack folder contents (read-only `ls -R`)

### Takeaway
The CR packs are small one-shot kits with inconsistent names: misspellings, generic "Perc01-06", and voices the hardware never had. The R-8 pack (243 samples plus Ableton .asd files) is far bigger than the 68-sound ROM and evidently includes card or MKII sounds. MC-303 has 148 short 8.3-style names. MC-09 has 10 × 4 drum samples. MC-202 has 9 synth percussion samples.

### Cited Findings (all from a local listing of ~/Splice/sounds/packs/<folder>)
- **Roland CR-78** (14 wav, flat): CR78Cowbell, CR78Guiro, CR78Hat_C, CR78Hat_O, CR78Kick, CR78Perc01-06, CR78Rimshot, CR78Snare, CR78Tamborine [sic]. Not named: cymbal, maracas, claves, high/low bongo, low conga, metallic beat. Some of these may be among Perc01-06 (unknown).
- **Roland CompuRhythm-78** (20 wav, flat): Bassdrum, Conga H, Conga M, Conga L, Cowbell, Hat Closed-01/02, Hat Open-01/02, Hit, Quid-01..04, Snaredrum, Tambourine, Woodblock-01..04. The hardware has only one conga (low) plus two bongos, so "Conga H/M" are probably the bongos (inferred). "Quid" is probably guiro (inferred). "Woodblock" may be claves (inferred). No rim shot, cymbal or maracas are named.
- **Roland CR-8000** (13 wav): CR8000Clap, Clave, CongaHi, CongaLo, Cowbell, Cymbal, Hat_C, Hat_O, Kick, Rimshot, Snare, Tom_Hi, Tom_Lo. Middle conga is missing.
- **Roland CompuRhythm 8000** (13 wav): Bassdrum, Clap, Claves, Cowbell, Cr8kmcng (probably the CR-8000 mid conga; inferred), Cymball [sic], Hat Closed, Hat Open, Rimshot, Snarderum [sic], Tom H, Tom M, Tom L. The hardware has only LOW TOM and HI TOM, so "Tom M" is not a hardware voice (inferred).
- **Roland CompuRhythm 1000** (15 wav): Bassdrum, Clap, Conga H, Conga L, Cowbell, Crash, Hat Closed, Hat Open, Ride, Rimshot, Snaredrum, Timbale, Tom H, Tom M, Tom L. There is no tambourine or claves, although the secondary source lists both.
- **Roland R-5** (64 wav, descriptive names): 10 kicks (Double Head Kick 1/2, Dry Kick 1/2, Electronic, Mondo, Room Ambient Kick 1/2, Solid, Wood); 15 snares + Side Stick (Back Snare, Brush Hit, Brush Roll, Electronic, Fat, Impact, Jazz, Open, Ouchi, Reverb, Rimshot Snare 1-3, Tight, Wood); 13 toms (Dry 1-3, Electronic 1-3, FX, Jazz 1-3, Room Ambient 1-3); 3 hats (Closed, Open, Pedal Closed); 6 cymbals (Back Cymbal, Crash, Mallet Crash, Ride, "Ride Bell Cymbal" and "Ride Cymbal Bell", possibly duplicates); 808 Hand Clap; 15 percussion (Agogo, Blast, Bongo, Cabasa, Can, Claves, Cowbell, Mute High Conga, Open Low Conga, Shaker, Slap High Conga, Surdo, Tambourine, Timbale, Whistle). That is 64 of the 68 ROM sounds. "Back …" = reversed (inferred).
- **Roland R-8** (243 wav + 243 Ableton .asd analysis files, flat, "R8<Name><nn>"): Kick01-33, Snare01-46, Tom01-38 + TomB/TomE/TomH2/TomHeavy, Rim01-05, Brush01-06, Hat_C01-05, Hat_O01-06, Hat_P01, Crash01-09, Ride01-08, Splash01-02, Chinese, CymbHand, FingerCym, Clap01-02, FingerSnap, plus 74 percussion/FX files. These include ethnic and mallet sounds such as Djembe, Darbuka, Tabla1-4, Daiko1-3, TsuzumiHi/Lo, Pandiero1-3, Caxixi, Kalimba, Vibra, Timpani, Gong, and FX such as Thriller, Ohkawa, Satellite, Spark and Noise. 243 is far more than 68 internal sounds, so the pack evidently includes SN-R8 card and/or R-8 MKII sounds (inferred).
- **Roland R8** (52 wav in 5 subfolders): Bassdrums (Bassdrum-01..07), CYMBALS (Crash, Hat Closed, Hat Open, Hat Pedal, Ride-01/02), Percussion (Bell-01/02, Bongo H/L, Cabasa1/2, Clap, Conga, Cowbell, Metal, Tambourine, Whistle, Wood Block), SNARES (Rimshot1/2, Snaredrum-01..12), Toms (Tom H/M/L-01..04).
- **Roland Digital Drum Brain DDR-30** (24 wav): Bassdrum-01..08, Snaredrum-01..08, Tom-01..08.
- **Roland MC-303** (148 wav in 6 subfolders, 8.3-style names): Bassdrums 16 (606bd1-3, Afrofeet, Blipbd, Cavebd/Cavebd2, Distbd1-3, Drybd1-3, Elecbd, Junglebd/Jnglebd2); Cymbals 14 (606ch, 707ch, 707oh, 78ch, 78oh, Asiangon, Realch1/2, Realoh1/2, Ridecymb/Ridecym2, Roomch, Roomoh); Misc 9; Percussion 59 (e.g. 626shake, 707clap, 78cowbel, 78guiro, 78metalb, 78tamb, Hiagogo/Loagogo, Hicongao/Hicongas/Locongao, Hibongoo/Lobongoo, Hitimbal/Lotimbal, Hihyoshi/Lohyoshi, Mutetria/Opentria, Mutesurd, Mutecuic/Opencuic in Misc); Snaredrums 32 (606sd1-3, 78sd, 80809sd, Rimshot, Tinyrim2-4, Jnglesd1-4…); Toms 18 (78hitom/78midtom/78lotom, acoustic, electronic and synth toms, Opensurd, Udo). The "606", "707", "626" and "78" prefixes indicate TR-606, TR-707, TR-626 and CR-78-derived sounds (inferred from names). The "78" toms cannot come from the CR-78, which has no toms.
- **Roland MC09** (40 wav): Kick01-10, Snare01-10, HatC_01-10, HatO_01-10.
- **Roland MC-202** (9 wav): Bassdrum-01..05, Click, Tom H-02..04 (no Tom H-01).
- None of the folders contain loops or MIDI.

### Inferences
- When building racks, treat the CR-78 "Hat_O" and the CR-8000 "Tom M" as extras, not hardware voices. Map the CompuRhythm-78 "Conga H/M" to the bongos only after listening (inferred).

### Gaps
- Which R-8 pack files are internal ROM sounds and which are card or MKII sounds cannot be told without the official list.

## Q7. Factory preset patterns and published step grids

### Takeaway
The CR-8000 manual prints an official step chart (● = hit) for every preset, arranger pattern and fill. Eight are transcribed below, all checked against the staff notation above each chart. The CR-78 manual prints all 34 presets, but only in staff notation, too small in the scan to transcribe reliably.

### Cited Findings
- CR-78 RHYTHM SELECTION BUTTONS (spec): ROCK 1-4, DISCO 1-2, WALTZ, SHUFFLE, SLOW ROCK, SWING, FOX TROT, TANGO, BOOGIE, ENKA ("a general in Japanese music"), BOSSANOVA, SAMBA, MAMBO, CHACHA, BEGUINE, RHUMBA. "Each RHYTHM SELECTION BUTTON has two kinds of pre-set rhythm patterns" (A/B), giving 34 presets. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- CR-78: the manual's "RHYTHM PATERN" pages give every preset in drum-staff notation with A/B, with a key: Bass Drum, Low Conga, Low Bongo, High Bongo, Snare Drum, Rim Shot, Claves, Cow Bell, Maracas, Hi-Hat, Cymbal. Fill-ins 1-7 are notated too. — [CR-78 manual](https://www.synthmanuals.com/manuals/roland/cr-78/owners_manual/roland_cr-78_owners_manual_rvgm.pdf)
- 17 preset buttons × A/B = 34 patterns. — [Wikipedia CR-78](https://en.wikipedia.org/wiki/Roland_CR-78); [polynominal CR-78](https://www.polynominal.com/roland-cr78/)
- CR-8000 presets by bank (panel, p.4): Bank I: WALTZ, SWING 1, SWING 2, S.ROCK, TANGO, HABANERA, ENKA, BD-4". Bank II: ROCK 1-6, DISCO, FOX TROT. Bank III: SAMBA 1, SAMBA 2, MERENGUE, MAMBO, CHACHA, RHUMBA, BEGUINE, BOSSANOVA. The spec page omits S.ROCK from Bank 1 and spells WALTZ "WALTS". — [CR-8000 manual pp.4, 19](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- CR-8000: the "PRE-SET RHYTHM PATTERN" charts (pp.12-16; "● = ♪, No Mark = rest") cover all 24 presets, the arranger patterns and intro/fill-ins 1-8 (8 = BREAK). ROCK 4, ROCK 5, MAMBO, RHUMBA, BEGUINE and BOSSA NOVA have A/B charts. "Bass Drum 4" in Basic Rhythm Bank I can be used for a Metronome." — [CR-8000 manual pp.10, 12-16](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
- CR-8000 Fig. 1 (p.9) shows the DISCO preset again as a programming example in a 16-step grid, and asks the reader to check that "Preset DISCO rhythm and programmed DISCO rhythm are same pattern". — [CR-8000 manual p.9](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)

**CR-8000 official grids, transcribed** (x = hit, X = hit on a step where the global ACC row is set, . = rest). Source for all: [CR-8000 manual pp.12-16](https://www.synthmanuals.com/manuals/roland/cr-8000/owners_manual/roland_cr-8000_owners_manual_rvgm.pdf)
```
WALTZ (3/4, 12 steps)     CY  X...........   SD  ....x...x...   BD  X...........
SWING 1 (4/4, 12 triplet steps)  HH ...X.x...X.x   OHH x.....x.....   BD x..X..x..X..
SWING 2 (4/4, 12 triplet steps)  CY x..X.xx..X.x   BD  x..X..x..X..
TANGO (4/4, 16)           OHH ..............X.   SD x...x...x...x.X.   BD x...x...x...x...
DISCO (4/4, 16)           OHH ..X...X...X...X.   SD ....X.......X...   BD X...X...X...X...
ARRANGER OPEN HH (16)     OHH ..x...x...x...x.
ARRANGER HAND CLAP (16)   CP  ....x.......x...
ARRANGER CONGA (16)       HC  ....x.....x.....   MC x...............   LC ............x.x.
```
- Not transcribed, because the scan is too low-resolution for exact accent reading: ROCK 1-6, S.ROCK, HABANERA, ENKA, FOX TROT, SAMBA 1/2, MERENGUE, MAMBO, CHACHA, RHUMBA, BEGUINE, BOSSANOVA, and fills 1-7. All are in the manual as step charts.
- CR-1000: 24 fixed ROM rhythms. Named: rock ×4, disco ×2, 16 beat ×2, swing ×2, shuffle, ballad, reggae, tango, samba ×2, merengue, mambo, chacha, rumba, beguine, bossanova (22 names for "24"). — [polynominal CR-1000](https://www.polynominal.com/roland-cr1000/)
- R-8/R-5: 32 preset patterns each. Names not found. — [Music Technology, Feb 1989](https://www.muzines.co.uk/articles/roland-r8/2188); [Music Technology, Jul 1989](https://www.muzines.co.uk/articles/roland-r5/102)
- MC-303: 133 preset patterns (SOS). Other sources say 120 (VSE) or "300 variation patterns" (Wikipedia). Genres include trance, Goa, techno, house, hip hop, jazz funk, jungle, trip hop, salsa and samba. — [Sound On Sound, Aug 1996](https://www.soundonsound.com/reviews/roland-mc303); [VSE MC-303](https://www.vintagesynth.com/roland/mc-303); [Wikipedia MC-303](https://en.wikipedia.org/wiki/Roland_MC-303)
- MC-09: preset patterns are Lead 40, Bass 60, Rhythm 100, Effect 30. — [Roland MC-09 specs](https://www.roland.com/us/products/mc-09/specifications/)
- Attack Magazine "CR-78 Redux" (Beat Dissected, 29 Jan 2016): a 2-bar beat built from CR-78 samples layered with TR-707/727 hits, 120-125 bpm, 53-55% swing. The step grid is published only as images, so it was not transcribed. — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/cr-78-redux/)

### Inferences
- From my reading of the CR-78 staff pages (low-resolution, medium confidence), three buttons appear to carry two differently named rhythms as A/B: FOX TROT (A) / TANGO (B), MAMBO / CHA CHA, and BEGUINE / RHUMBA. That is consistent with 20 names on 17 buttons (inferred).

### Gaps
- CR-78 step grids (only staff notation exists in the manual). R-5, R-8, MC-303 and MC-09 preset grids and names. The CR-8000 rock and Latin grids are in the source but not transcribed.

## Q8. Famous recordings and published grooves

### Takeaway
Only the CR-78 has well-documented famous recordings, several tied to named presets by Roland itself. No published text step charts of those songs were found. For the other machines, the sources name users (artists or bands) but no specific recordings.

### Cited Findings
- Blondie, "Heart of Glass" (1978 LP / 1979 single): the opening rhythm combines the CR-78's Mambo and Beguine presets, and the trigger out modulated an SH-5 filter for the bassline. — [Roland article](https://articles.roland.com/?p=75463); also [Guardian 2013 via Wikipedia](https://www.theguardian.com/music/2013/apr/29/how-we-made-heart-glass)
- Phil Collins, "In the Air Tonight" (1981): "Disco 2" in its A variation. — [Roland article](https://articles.roland.com/?p=75463); Collins, *Not Dead Yet*, p.168 (cited by [Wikipedia CR-78](https://en.wikipedia.org/wiki/Roland_CR-78))
- Daryl Hall & John Oates, "I Can't Go for That (No Can Do)" (1981): Rock 1 pattern. — [Roland article](https://articles.roland.com/?p=75463); [Guardian 2018](https://www.theguardian.com/music/2018/apr/02/hall-and-oates-how-we-made-i-cant-go-for-that-no-can-do-interview)
- Ultravox, "Vienna" (1980): Rock 4 pattern. — [Roland article](https://articles.roland.com/?p=75463)
- OMD, "Enola Gay" (1980): CR-78, per MusicRadar as cited by Wikipedia. — [Wikipedia CR-78](https://en.wikipedia.org/wiki/Roland_CR-78)
- Also: Chris de Burgh, "The Lady in Red" (Enka pattern), and John Foxx's *Metamatic* (CR-78 on "pretty much every track"). — [Roland article](https://articles.roland.com/?p=75463). Tears for Fears, "Mad World" (Guardian 2013). — [Wikipedia CR-78](https://en.wikipedia.org/wiki/Roland_CR-78)
- CR-8000 users listed by VSE: Fluke, BT, Jimmy Edgar, Blondie. No songs named. — [VSE CR-8000](https://www.vintagesynth.com/roland/cr-8000)
- R-8 users listed by VSE: Orbital, Underworld, Autechre, 808 State, Fluke, The Human League, The Shamen. No songs named. — [VSE R-8](https://www.vintagesynth.com/roland/r-8)
- DDR-30: A Flock of Seagulls' drummer Ali Score used the "Roland DDR 30 for several tours" (no recordings named). Wikipedia also lists Peter Gill (FGTH), Michael Giles and Front 242. — [Modern Drummer 2018](https://www.moderndrummer.com/2018/06/on-the-beat-with-alister-score-of-a-flock-of-seagulls/); [Wikipedia DDR-30](https://en.wikipedia.org/wiki/Roland_DDR-30)
- MC-303: VSE says ATB used it. theprodigy.info lists it among Liam Howlett's gear but names no tracks. — [VSE MC-303](https://www.vintagesynth.com/roland/mc-303); [theprodigy.info](https://theprodigy.info/equipment/roland-mc-303-groovebox.html)
- MC-202 users listed by VSE: Autechre, FSOL, Coldcut, Human League, Underworld, Aphex Twin, LFO, Plastikman and others. No songs named. — [VSE MC-202](https://www.vintagesynth.com/roland/mc-202)

### Inferences
- The CR-78 famous grooves are factory presets: Disco 2-A, Rock 1, Rock 4, Mambo+Beguine and Enka. Their exact patterns are therefore in the CR-78 manual's staff notation. A careful transcription from a higher-resolution scan, or from the real or Roland-software CR-78, would give exact MIDI. This was not done here.

### Gaps
- No published step charts for any of these songs were found. Searches did not reach Attack, MusicRadar or SOS song breakdowns before the search budget ran out. No verified famous recordings were found for the CR-8000, CR-1000, R-5, R-8, DDR-30, MC-303, MC-09 or MC-202.

## Q9. Free, clearly licensed MIDI pattern files

### Takeaway
None found.

### Cited Findings
- No source in this session offered free MIDI files with a clear licence for these machines. Attack's CR-78 Redux grid is an image inside an article, not a licensed file. — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/cr-78-redux/)

### Inferences
- The CR-8000 manual's official preset charts (Q7) are the best route to faithful MIDI for that machine. They are Roland documentation, not a licensed MIDI file.

### Gaps
- Dedicated searches for licensed MIDI packs (GitHub, Splice, Roland) were not possible after the search budget ran out.

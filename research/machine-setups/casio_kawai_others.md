# Casio (RZ-1, SK-1, VL-1), Kawai (R-50, R-50e, XD-5, K3, SX-240), Cheetah MD16, Quasimidi Rave-O-Lution 309 and Novation DrumStation: hardware setup, sound lists, patterns and pack contents

Scope note for the report writer: web search hit the shared session limit part-way through this task, so some gaps below (R-50 sound list, SK-1 percussion layout, RZ-1 note map, step grids) are there because I could not search further, not because I proved nothing exists. ManualsLib and archive.org were blocked or unreachable, so I couldn't read the RZ-1, VL-1, SK-1 or DrumStation owner's manuals directly. The Quasimidi 309 manual (German edition, 28 pages) was read in full. "Local inspection" means I ran `ls -R` and read the WAV headers on 2026-11-13. Nothing was played, moved or changed.

## 1. What voices does each machine have, in front-panel, pad or key order, with the exact labels?

### Takeaway
Only the Quasimidi 309 (official manual), the Novation DrumStation (MIDI map, review and the pack's kit Readme) and the Cheetah MD16 (reviews name all 41 ROM sounds) have voice sets that are well documented. The RZ-1's 12 voices are confirmed, but their left-to-right panel order and exact legends are not. For the SK-1, VL-1, R-50, R-50e and XD-5, the voice sets are known only from secondary sources plus the pack file names. The K3 and SX-240 are synths with no drum voices.

### Cited Findings
**Casio RZ-1 (1986)**
- The RZ-1 has 12 on-board PCM voices: "three toms, bass, snare, rim, hi hat open, hi hat closed, claps, cowbell, ride, and crash". It also has 4 user-sample voices. The voice buttons are "large rectangular buttons ranged along the bottom", black for on-board voices and grey for sampled ones. To their left are yellow Start/Stop and Continue buttons and purple Accent and Mute buttons. The review does not give the left-to-right order of the voice buttons. — [International Musician review, Apr 1986 (muzines)](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164)
- Vintage Synth Explorer (VSE) lists the 12 sounds as "Tom 1, Tom 2, Tom 3, Snare, Kick, Rim, Open HH, Closed HH, Ride, Crash, Clap, Cowbell", plus four sample pads. — [VSE RZ-1](https://www.vintagesynth.com/casio/rz-1)
- The same 12 names appear on another site, which describes the RZ-1 as having "16 pads", four of them used for sampling. — [Polynominal RZ-1](https://www.polynominal.com/sample-packs/casio-rz1/)

**Casio SK-1 (1985)**
- The SK-1 has 8 preset tones. Five are PCM (piano, brass ensemble, trumpet, synth drums, human voice) and three are synth tones (flute, pipe organ, jazz organ). It has 11 built-in drum patterns. VSE lists no separate drum sounds and no pad count. — [VSE SK-1](https://www.vintagesynth.com/casio/sk-1)
- English Wikipedia mentions only "preset rhythms" and a rhythm machine, with no drum-sound names or pads. — [Wikipedia SK-1](https://en.wikipedia.org/wiki/Casio_SK-1)

**Casio VL-1 / VL-Tone**
- The rhythms use three basic drum sounds, which Casio called "Po" (30 ms), "Pi" (20 ms) and "Sha" (160 ms) internally. This section of the article has no citation. — [Wikipedia VL-1](https://en.wikipedia.org/wiki/Casio_VL-1)
- The preset tones are Piano, Fantasy, Violin, Flute and Guitar. — [German Wikipedia VL-1](https://de.wikipedia.org/wiki/Casio_VL-1)

**Kawai R-50 / R-50e**
- The R-50 (listed with the R-100) has 24 samples at 12-bit, 32 kHz, 8 voices, and per-sound pan, volume, tuning and dynamics. The R-100 has dynamic pads; the R-50 has "10 pads without dynamics". Sound names are not listed. — [sequencer.de R100/R50](https://www.sequencer.de/syns/kawai/R100_R50.html)
- Sonic State gives the release year as "1988?" and describes the sounds as 12-bit, 32K-sampled. It links to photos of the ROM chips. It does not list the R-50e's sounds. — [Sonic State R-50](https://sonicstate.com/synth/kawai_r50/)

**Kawai XD-5 (1989-90)**
- The XD-5 is a drum synth module with 256 waveforms, combining 1 to 4 of them per voice. It has 64 patches, 16 DrumKits and 16-voice polyphony. Kit structure and names are not given. — [VSE XD-5](https://www.vintagesynth.com/kawai/xd-5)

**Kawai K3 / K3m (1986) and Kawai SX-240 (1984)**
- The K3 is a 6-voice hybrid synth with 32 digital waveforms plus a user-programmable waveform. It has no drum section. — [VSE K3](https://www.vintagesynth.com/kawai/k3)
- The SX-240 is an 8-voice analog polysynth with a noise generator. It has no drum section. — [VSE SX-240](https://www.vintagesynth.com/kawai/sx-240)

**Cheetah MD16 (shown 1990, reviewed 1991)**
- The MD16 has 16 velocity-sensitive rubber pads, about ¾" across. Four pad "levels" act as four 16-pad kits, plus an auxiliary set, for 128 pad assignments in total. — [Music Technology review, Mar 1991](https://www.muzines.co.uk/articles/cheetah-md16/792)
- It has 41 ROM samples. The same review names them by category:
  - Bass drums: 'Gated', 'Hip', 'Slap', 'Thump', 'Electro'
  - Snares: 'Killer', 'Acoustic', 'Fusion', 'Ska', 'House', 'Up'
  - Toms: 'Electro', 'Hi', 'Mid', 'Low', 'Deep'
  - Hi-hats: 'Closed', 'Mid', 'Open', 'Pedal Closed'
  - Cymbals: 'Crash', 'Ride', 'Splash'
  - Percussion: 'Cowbell', 'Electro Bell', 'Acid Flick', 'Sidestick', 'Temple Block', 'Claves', 'Castanet', 'Snap', 'Tambourine', 'Shaker', 'Cabasa', 'Tabla', 'High Bongo', 'Agogo', 'Samba Whistle', 'Claps', 'Timbale'
  - One slap bass-guitar sample

  — [Music Technology review](https://www.muzines.co.uk/articles/cheetah-md16/792)
- Sound On Sound gives the same breakdown: 5 kicks, 6 snares, 5 toms, 4 hi-hats, 3 cymbals, 17 percussion sounds and 1 sampled slap bass. — [SOS retro review, Apr 1997](https://www.soundonsound.com/reviews/cheetah-md16)
- Pads are freely assignable, so there is no fixed per-pad voice layout. — [Music Technology review](https://www.muzines.co.uk/articles/cheetah-md16/792)

**Quasimidi Rave-O-Lution 309 (1996)**
- The 309 has five sections: KICK-DRUM, SNARE-DRUM, HIHAT, PERCUSSION-SET and BASS/LEAD synthesizer. This is the order of the manual's parameter table and of the SOS review. That it matches left-to-right panel order is likely but unconfirmed. — [309 manual (German)](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf); [SOS review](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)
- The HIHAT section is duophonic: "zweistimmig spielbar für offene und geschlossene Hihat" (two voices, one for open and one for closed hi-hat). In the drumgrid you choose "ClosedHH" or "OpenHH". — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- The PERCUSSION-SET plays 12 voices at once. Its 12 instruments sit on the keys C, C#, D, D#, E, F, F#, G, G#, A, A#, H (B) of the mini keyboard. The manual's example display reads "Edit Set 3 - C / Ins:808Kic1F". — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- Spec sheet: "Monophoner BASS-LEAD-Synthesizer, 16 Drum- und Percussionstimmen" (a monophonic bass/lead synth plus 16 drum and percussion voices). — [309 manual, p. 28](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- SOS says "All instruments are monophonic, apart from the Percussion Set". — [SOS](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)

**Novation DrumStation (1996)**
- The DrumStation is a 1U MIDI module that clones the TR-808 and TR-909. It has no sequencer. — [Wikipedia DrumStation](https://en.wikipedia.org/wiki/Novation_DrumStation); [Zoë Blade notebook](https://notebook.zoeblade.com/DrumStation.html)
- The MIDI map covers 808 BD, RS, SD, CP, LT, MT, HT, CH, OH, cymbal ("crash"), CB, HC, MC, LC, MA and CL, plus 909 BD, RS, SD, CP, LT, MT, HT, CH, OH, crash and ride. That is 16 TR-808 voices and 11 TR-909 voices. — [DrumStation MIDI map](https://notebook.zoeblade.com/DrumStation_MIDI_map.html)
- Front-panel controls are shared. Instruments that share a set of controls are chosen with a 3-position switch. — [SOS review, Jul 1996](https://www.soundonsound.com/reviews/novation-drumstation)
- There is a tom section with a switch "selecting one of 3 toms". All 22 knobs send MIDI CC. — [Polynominal DrumStation](https://www.polynominal.com/novation-drum-station/index.html)

### Inferences
- **RZ-1 panel order:** VSE and Polynominal list the voices in the same order (Tom 1, Tom 2, Tom 3, Snare, Kick, Rim, Open HH, Closed HH, Ride, Crash, Clap, Cowbell, then Sample 1-4). This may be the button order, but no source confirms it. It's also not documented which of Tom 1/2/3 is high or low. Many Japanese machines number toms from high to low, but that is a guess.
- **VL-1 sounds:** The VL-1 pack files match the three Wikipedia sounds by length and character. "Bassdrum.wav" (50 ms, low) is probably "Po". "Hi Hat.wav" (28 ms, a pitched blip rather than noise) is probably "Pi". "Snaredrum-01.wav" (194 ms, noise) is probably "Sha".
- **SK-1, R-50, R-50e, XD-5 voice lists:** These can only be taken from the pack file names. The R-50 and R-50e folders each hold 24 files, which matches the R-50's documented 24 ROM sounds. That suggests one file per ROM sound.
- **R-50e ROM:** The R-50e pack contains orchestra hits, guitar, timpani, Hi-Q and snap. So its ROM differs from the R-50's: it looks like an alternative or effects sound set.
- **DrumStation panel:** The likely layout is BD, SD, Toms (Lo/Mid/Hi switch), Hi-hat, Cymbal and an "other instruments" section with Tune and Level. The switch assignments outside the toms are not confirmed.

### Gaps
- No source gave the RZ-1's printed button legends or their left-to-right order. The manual on ManualsLib was blocked.
- It's unknown how the SK-1's drum sounds are triggered: rhythm patterns only, the "synth drums" tone on the keys, or pads. No hardware labels were found.
- No official sound names or order were found for the Kawai R-50 or R-50e. The R-50's pad count ("10 pads") comes from one secondary site.
- The XD-5's waveform names and the contents of its 16 kits were not found.
- The exact DrumStation panel legends and which instruments share each 3-way switch (beyond the toms) were not found.

## 2. Which sounds share one voice or cut each other off?

### Takeaway
Shared voices are clearly documented for only two machines: the RZ-1's shared faders and outputs, and the 309's duophonic hi-hat section. For the MD16, routing sounds to the same individual output makes them cut each other off. Everywhere else, open/closed hat choking is a reasonable assumption but is not documented.

### Cited Findings
- **RZ-1:** There are 10 voice faders for the 16 voices, and "some of the logical instrument combinations" double up, with open/closed hi-hat given as the example. — [IM review](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164)
- **RZ-1 output pairs:** There are ten individual outputs shared in pairs: Rim+Snare, Sample1+Sample2, Sample3+Sample4, Cowbell+Crash, Clap+Ride, Open+Closed HH. — [VSE RZ-1](https://www.vintagesynth.com/casio/rz-1)
- **RZ-1 output count conflict:** The IM review says 10 individual outputs plus L/R. Polynominal says "12 separate outputs". — [IM review](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164); [Polynominal](https://www.polynominal.com/sample-packs/casio-rz1/)
- **Quasimidi 309:** The hi-hat section is duophonic for open and closed hi-hat (one section, two voices). Kick, Snare and Bass/Lead are monophonic. The Percussion Set is 12-voice polyphonic. — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf); [SOS](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)
- **Cheetah MD16:** "Each out is monophonic, and the unit has 8-note polyphony." — [SOS](https://www.soundonsound.com/reviews/cheetah-md16)
- **Cheetah MD16 voice settings:** Each voice has an output setting (1-8) and a number-of-voices setting (1-8). — [Music Technology](https://www.muzines.co.uk/articles/cheetah-md16/792)
- **DrumStation:** Each drum can be set to accept or ignore note-off messages. This decides whether a drum cuts off when it's retriggered before its decay ends. — [SOS DrumStation](https://www.soundonsound.com/reviews/novation-drumstation)
- **DrumStation 'A Bit Off' kit:** The factory kit "'A Bit Off' TR909" uses note-off recognition. This comes from a search-result snippet of the manual's factory list; the page itself was blocked. — [manualshive snippet](https://manualshive.com/en/manual/novation/drumstation/1711554?page=46)

### Inferences
- **RZ-1 hats:** Open and closed HH almost certainly behave as one choking pair, since they share a fader and output. The other RZ-1 pairs (Rim/Snare, Clap/Ride, Cowbell/Crash, Sample 1/2, Sample 3/4) share only a fader and output. There's no evidence they choke each other.
- **MD16 hats:** To recreate hi-hat choking, put the four hats ('Closed', 'Mid', 'Open', 'Pedal Closed') on one output or in one choke group.
- **DrumStation hats:** Ableton choke groups for 808 CH/OH and 909 CH/OH copy the original TR-808/909 behaviour. This is not documented for the DrumStation itself.
- **VL-1, SK-1, R-50, R-50e, XD-5:** Nothing is documented. Treat open/closed hats as one choke pair by convention.

### Gaps
- No primary source documents hi-hat choke on the RZ-1, SK-1, VL-1, R-50, R-50e, XD-5 or DrumStation.

## 3. What controls does each voice have? How does accent work? Flam, shuffle, per-voice tuning?

### Takeaway
- **RZ-1:** Only level faders and accent/mute; no tuning.
- **309:** Each drum section is a full synth voice (filter and envelopes), with 4-level velocity accent and a Groove (shuffle) setting.
- **DrumStation:** TR-style knobs (Tune, Level, Decay, Tone/Snappy/Attack), with velocity assignable to any parameter.
- **MD16:** Deep per-voice editing, swing ±8 and an echo function.
- **VL-1, SK-1:** No per-drum controls are documented.

No machine here has a documented flam function.

### Cited Findings
- **Casio RZ-1:**
  - "No onboard control for pitch, envelope, or stereo position." — [Music Technology 'Beauty and the Beat'](https://www.muzines.co.uk/articles/beauty-and-the-beat/9279)
  - Each sound has three dynamic levels: Accent, Normal and Mute. — [Polynominal](https://www.polynominal.com/sample-packs/casio-rz1/)
  - There are purple Accent and Mute buttons. Quantise ("Auto-compensate") runs from 1/2 to 1/96 notes, triplets are possible, and tempo runs from 40 to 250 BPM. — [IM review](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164)
  - Two rear mini-pots adjust the tone of the samples. — [IM review](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164)
  - Swing, flam and how accent works are "not covered" in the IM review.
- **Casio SK-1:** The SK-1 has 4-voice polyphony, 13 envelope shapes, no filter, no VCA, no MIDI and no effects. — [VSE SK-1](https://www.vintagesynth.com/casio/sk-1)
- **Casio VL-1:** No per-voice drum controls are described in the sources found. — [Wikipedia VL-1](https://en.wikipedia.org/wiki/Casio_VL-1); [German Wikipedia](https://de.wikipedia.org/wiki/Casio_VL-1)
- **Kawai R-50:** Per-sound parameters are panorama, volume, tuning ("Stimmung") and dynamics. — [sequencer.de](https://www.sequencer.de/syns/kawai/R100_R50.html)
- **Kawai XD-5:** Each voice combines 1-4 waveforms and has a "digital resonant lowpass" filter (DCF) and a "digital envelope" amplifier (DCA). There is no LFO. — [VSE XD-5](https://www.vintagesynth.com/kawai/xd-5)
- **Cheetah MD16 per-voice settings:** — [Music Technology](https://www.muzines.co.uk/articles/cheetah-md16/792)
  - Sample number, tuning (chromatic or fine) and reverse.
  - Pan 0-15, volume envelope 1-8, volume level 1-31, velocity curve 1-8, output 1-8, number of voices 1-8 and MIDI note 0-127.
  - Humanise (random start, random pitch).
  - Opposite, Roll and Auto Pan, Auto Pitch and Auto Reverse.
  - Swing ±8, timing randomisation and cyclic randomisation.
  - Shift + Accent/Level cycles the pad levels.
- **Cheetah MD16 tuning and velocity:** Tuning runs from +1 to -6 octaves, or chromatically ±1 octave. Velocity can affect tuning, sample length, attack and start point. — [SOS](https://www.soundonsound.com/reviews/cheetah-md16)
- **Cheetah MD16R/RP:** These add negative swing and quantise to 1/192. — [Music Technology MD16R/RP](https://www.muzines.co.uk/articles/cheetah-md16r-and-md16rp/1004)
- **Quasimidi 309 front-panel knobs:** — [SOS](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)
  - Kick: Instrument, Tune, Attack, Decay, Level, Sound
  - Snare: Instrument, Tune, Tone, Decay, Level, Sound
  - Hi-hat: Instrument, Tune, Decay, Level, Sound
  - Percussion Set: Perc Set, Tone, Decay, Level, Sound
- **Quasimidi 309 sound parameters (every section):** Level, VCF-Drive, Cutoff, Resonance, Envelope-Modulation, Dynamic-Modulation, Accent and EG Attack/Decay/Sustain/Release. All drums have "24 dB steile Filter mit Resonanz" (resonant 24 dB/octave filters) and ADSR envelopes. — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- **Quasimidi 309 percussion instruments:** Each of the 12 instruments in a set has Wave, Tune, Level, Panorama, FX1-Send and FX2-Send. — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- **Quasimidi 309 accent:** — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
  - The drumgrid offers "4 Lautstärke-Stufen" (4 velocity levels) on buttons 9-12, from quietest (9) to loudest (12). The pad values are set on Edit Pads pages 41-44.
  - Each section's ACCENT parameter controls how strongly a note's assigned velocity changes its level and tone. It has its strongest effect at the middle setting (64).
  - It's on MIDI CC25, "(Accent) Velocity Response".
- **Quasimidi 309 timing:** — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
  - GROOVE "shuffeln" (shuffle) is set as a percentage on pattern-edit page 2.
  - Drumgrid resolutions are 8th, 12th (triplet), 16th (default), 24th and 32nd notes.
  - Tempo runs from 50 to 250 BPM, with tap tempo.
- **Novation DrumStation knobs:** — [SOS](https://www.soundonsound.com/reviews/novation-drumstation)
  - Snare: Tune, Level, Tone, Snappy
  - Bass drum: Tune, Level, Decay, plus Attack (909) or Tone (808)
  - Toms, hi-hats, cymbals: Tune, Level, Decay
  - Other instruments: Tune, Level
- **DrumStation velocity:** Velocity or controller response can be set per parameter. For example, snare tone and tuning can follow velocity while Snappy follows a MIDI controller. — [SOS](https://www.soundonsound.com/reviews/novation-drumstation)
- **DrumStation accent:** With the 808 sounds on MIDI, notes can be swung and given independent accents. Accent is handled through velocity. — [Zoë Blade](https://notebook.zoeblade.com/DrumStation.html)
- **DrumStation knob list:** Kick: level, pitch, decay, attack. Cymbal (808 mode): level, decay, tune. — [Polynominal](https://www.polynominal.com/novation-drum-station/index.html)

### Inferences
- **RZ-1 accent:** Accent probably works per step and per instrument (Accent/Normal/Mute). It's applied with the Accent button while programming. The exact gain step is unknown.
- **309:** For Ableton, map the 4 drumgrid velocity levels to 4 MIDI velocity values. The defaults are not in the manual excerpt read.

### Gaps
- No source describes swing or shuffle on the RZ-1, R-50, R-50e, SK-1 or VL-1. No flam function is documented on any of these machines.
- The R-50's accent behaviour is unknown.
- How the MD16's dedicated "Accent" works is not described in the reviews found.

## 4. Any built-in effects? What do they apply to?

### Takeaway
- **309:** Three effects units (reverb/delay, modulation, a 2-band EQ on the sum) plus Overblast.
- **DrumStation:** Per-voice distortion and Front Cut.
- **MD16:** A pad echo (repeats), no reverb.
- **XD-5:** A delay-type effect and a ring modulator.
- **SX-240:** Ensemble chorus and ring mod.
- **None:** RZ-1 (apart from a tone pot on the user samples) and SK-1. The VL-1, R-50 and R-50e have no documented effects.

### Cited Findings
- **Casio RZ-1:** There are no built-in effects. Samples have a rear low-pass tone trimmer. — [Polynominal](https://www.polynominal.com/sample-packs/casio-rz1/)
- **Casio RZ-1 sample tone (circuit-bent unit):** On a circuit-bent RZ-1, each tone knob controls a pair of samples. Casio placed these as tiny rear-panel pots. — [Circuitbenders](https://www.circuitbenders.co.uk/newsarchive/RZ1.html)
- **Casio SK-1:** "no effects". — [VSE SK-1](https://www.vintagesynth.com/casio/sk-1)
- **Kawai XD-5:** A delay-type effect and a ring modulator. — [VSE XD-5](https://www.vintagesynth.com/kawai/xd-5)
- **Kawai K3:** No effects are mentioned. — [VSE K3](https://www.vintagesynth.com/kawai/k3)
- **Kawai SX-240:** The "Ensemble" effect is a chorus. The "Brass" function is a ring-modulation effect. — [VSE SX-240](https://www.vintagesynth.com/kawai/sx-240)
- **Kawai SX-240 chorus chip:** The SX-240 uses an NM3009 chorus chip. — [sequencer.de SX240](https://www.sequencer.de/syns/kawai/SX240.html)
- **Cheetah MD16:** Echo on pad levels 3 and 4: pad count, repeat rate (1-120 MIDI clocks, straight and triplet), 1-16 repeats and fade from -8 to +8. The MD16 "has no reverb capability". — [Music Technology](https://www.muzines.co.uk/articles/cheetah-md16/792)
- **Cheetah MD16 echo banks:** Programmable echo banks can be assigned to any pad. They are MIDI-style repeats, not FX units. — [SOS](https://www.soundonsound.com/reviews/cheetah-md16)
- **Quasimidi 309 effects units:** — [309 manual p. 28](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf); [SOS](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)
  - FX-1: Room1, Room2, Room3, Hall1, Hall2, Plate, Delay, Pan-Delay
  - FX-2: Chorus1-4, Feedback-Chorus, Flanger, Short-Delay, Feedback-Delay
  - FX-3: a 2-band parametric EQ
  - Plus the "Overblast"
- **Quasimidi 309 routing:** — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
  - Each section has FX1 and FX2 sends in the MIX menu.
  - Within the Percussion Set, each of the 12 instruments has its own FX sends, and these must be open for the section sends to work.
  - The EQ works on the stereo sum only.
  - Overblast is a "Bass-Boost" on the overall sound.
  - Every section, drums included, has VCF Drive into a resonant 24 dB/octave low-pass filter.
- **Novation DrumStation:** — [SOS](https://www.soundonsound.com/reviews/novation-drumstation)
  - Distortion adds soft-knee distortion to the currently selected drum voice.
  - Front Cut removes up to 99 ms from the start of a drum sound.
- **DrumStation distortion use:** The distortion/fuzz section is described as useful for 909 gabber-style kicks. — [Polynominal](https://www.polynominal.com/novation-drum-station/index.html)

### Inferences
- **VL-1, R-50, R-50e:** I found no evidence of effects. Treat them as having none until a manual says otherwise.

### Gaps
- XD-5 effect routing (per voice or global) is not documented in the sources found.

## 5. For ROM machines: total sounds, categories with counts and number ranges, official ordered sound list, factory kit layout and default MIDI note map (and do the numbered packs line up?)

### Takeaway
- **309:** The manual gives the official ordered list: 28 bass waves, 26 kicks, 25 snares, 7 hi-hats and "128" drumset samples, of which only 126 names are printed. The pack's QuasiA/B/C numbering (50/135/39) does not line up with these categories.
- **MD16:** Exactly 41 ROM sounds are documented by name and category, but no ROM order was found. The pack's 48 numbered files therefore can't be matched with certainty.
- **DrumStation:** The pack's Kit00-Kit22 folders line up with factory programs 1-23, offset by one. Programs 24-25, the individual-output duplicates, are left out. The MIDI note map is published.
- **RZ-1, R-50, XD-5:** Only totals are known.

### Cited Findings
**Quasimidi Rave-O-Lution 309: official lists (manual p. 25, printed order)** — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- **Bass-Waves (28):** MoogWav1, MoogWav2, DistSin1, DistSin2, D_Trian1, D_Trian2, MixWavA2, Form_A_1, Form_A_2, Form_B_1, Form_B_2, Form_C_1, Form_C_2, RolSaw_1, RolSaw_2, Sawtoth1, Sawtoth2, Sine_1, Sine_2, SineSaw2, SineSqu2, SineTri2, Square_1, Square_2, SqarSaw2, TriaSaw2, TriaSqu2, MixWav_4.
- **Kicks (26):** D_Kick1, D_Kick2, D_Kick3, D_Kick4, D_Kick5, 808Kick1, 808Kick2, 808Kick3, 909Kick1, 909Kick2, 909Kick3, 909Kick4, 909Kick5, HipKick, DistorBD, KickShrt, KicRev, KlickKic, KxiuKick, LongBD, ShrtBD, MS_Kick, AnaKick1, AnaKick2, AnaKick3, AnaKick4.
- **Snares (25):** 606Snare, 808Snar1, 808Snar2, 808Snar3, 909Snar1, 909Snar2, HipSnar, EfSnare1, EfSnare2, EfSnare3, EfSnare4, EfSnare5, FlSnare, IndSnare, HiSnare, DrySnar1, DrySnar2, MS20_Snr, Snare1, Snare2, Snare3, Snare4, Noise1, Noise2, Noise3.
- **HiHats (7):** MS_HiHat, NatHiHat, 808HiHat, 909HiHat, 606HiHat, Fx_HiHat, MS_20_HH.
- **Drumset-Instr. ("128 Samples"; 126 names printed), for the Percussion Set:**
  - 606/808 group: 606ClHH, 606Cymb, 606_hTom, 606_lTom, 606_opHH, 606SnarF, 808_clHH, 808_Clap, 808Clave, 808_Cow, 808_Cymb, 808hCong, 808_hTom, 808Kic1F, 808Kic2F, 808_lTom, 808_mTom, 808_Rim, 808Sna2F, 808Sna3F, 808SnarF.
  - 909 group: 909_Clap, 909_clHH, 909Crash, 909hiTom, 909Kic1F, 909Kic2F, 909Kic3F, 909Kic4F, 909loTom, 909_mTom, 909_opHH, 909_Ride, 909_Rim, 909Sna1F, 909Sna2F.
  - Brickn and conga group: Brickn, Cng1Mute, Cng1Palm, Cng1Slap, Cng2Mute, Cng2Palm, Cng3_OT, Cng3Palm, Cng2Slap, CngMuffl, CngMute, CngOpen, CngOTOF, CngOTOF2, CngOTOFF, CngPalm, CngSlap, CngSlOf, CngSlpHd, CngTips.
  - D to F group: DeepShak, DirtClap, DirtClp2, DirtHH, DistorBF, DrySna1F, DrySna2F, D_Kick1F, D_Kick2F, D_Kick3F, D_Kick4F, D_Kick5F, EfSnar1F, EfSnar2F, EfSnar3F, EfSnar4F, EfSnar5F, FingSnip, FipSnap, FlngClp, FlSnareF, F_Drum_1, F_Drum_2, F_Drum_3, F_Drum_4, F_Drum_5, F_Drum_6, F_Drum_7, F_Revs1.
  - H to M group: HighStck, HipKick, HipSnaF, HiSnarF, Ito_HDMT, Ito_HDOT, Ito_HDS, Ito_LDM, Ito_LDOT, Ito_LDS, Iya_AHDO, Iya_AHDS, Iya_HDM, Iya_HDOT, Iya_HDS, Iya_LDM, Iya_LDO, Iya_LDS, KickShrF, KicRevF, KlickKiF, LongBF, MS_20HHF, MS_20SF, MS_KicF.
  - N to U group, then Metronom: NcHHFoot, NclHH, NormClap, Revers1, Ride, ShrtBF, Snare1F, Snare2F, Snare3F, Snare4F, Ticker, Udus1, Udus2, Udus3, Udus4, Metronom.

**Quasimidi 309: other official facts**
- There are 10 percussion sets (0-9) of 12 instruments each, and 64 sound memories per drum section. — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- Default MIDI channels: Kick on 1, Snare on 2, Hihat on 3, Percussion on 4. If the system channel is changed, they shift up together. — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- The MIDI implementation chart gives the default basic channel as "1-5" and the note range as "36-96". — [309 manual p. 27](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- SOS counts "26 kicks, 25 snares, seven hi-hats" and "a pool of 128 raw waveforms" for the percussion sets. — [SOS](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)
- VSE's "64 kicks, 64 snares, 64 hi-hats" are the user sound memories, not the raw samples. VSE also says 17 voices. — [VSE 309](https://www.vintagesynth.com/quasimidi/rave-o-lution-309)
- Wikipedia says "32-voice polyphony", which conflicts with the manual's 16 drum voices plus a mono bass. — [Wikipedia 309](https://en.wikipedia.org/wiki/Quasimidi_Rave-O-Lution_309)
- The pack Readme says: "Unfortunately I no longer own this machine or its manuals and don't have a list of the sound names." — local inspection of `Quasimidi 309/readme.txt`

**Cheetah MD16**
- There are 41 sounds: 5 kicks, 6 snares, 5 toms, 4 hi-hats, 3 cymbals, 17 percussion and 1 slap bass. Optional cartridges added TR-808/909, electro drums, extra kicks and snares, and African and Latin percussion. — [SOS](https://www.soundonsound.com/reviews/cheetah-md16)
- The voice setting assigns the sample number as "off or 1-41". The ROM cartridge port takes up to 192 extra samples. — [Music Technology](https://www.muzines.co.uk/articles/cheetah-md16/792)
- The R and RP models use the same 41 samples. Cartridges each hold over 200 samples. — [Music Technology MD16R/RP](https://www.muzines.co.uk/articles/cheetah-md16r-and-md16rp/1004)
- A scanned 109-page MD16R manual exists, but only as a zip download, so it wasn't read. — [cykong.com](https://cykong.com/Synths/Cheetah%20MD16RP/Cheetah-MD16RP.htm)
- MIDI notes are assignable per pad and per voice (0-127), and 2-8 pads can share a note. No default map was found. — [Music Technology](https://www.muzines.co.uk/articles/cheetah-md16/792)
- The pack Readme carries the same "no list of the sound names" note as the 309 pack. — local inspection of `Cheetah MD16/readme.txt`

**Novation DrumStation**
- The pack Readme lists 23 preset kits and notes: "Kits 023 and 024 are duplicate kits using individual outputs so have not been included." It also says "The Kits contain both 808 and 909 sounds." — local inspection of `Novation Drumstation/Readme.txt`
- Kit names from the pack Readme, by pack folder: 00 Classic TR909 V1, 01 FX TR909/TR808, 02 Garage 909/808, 03 Classic TR909 V2, 04 Hardcore TR909, 05 Rave / Jungle TR808, 06 Classic TR808 V1, 07 Tune Me Up, 08 Cut TR909, 09 Dynamic TR909, 10 Cut TR808, 11 Grunge TR909, 12 Dynamic TR808, 13 Grunge TR808, 14 Classic TR909 V3, 15 Power TR909, 16 Power TR808, 17 A Bit Off TR909, 18 A Bit off TR808, 19 Velo TR909, 20 Velo Dis TR909, 21 Velo Tom TR909, 22 Velo Tom TR808. — local inspection
- A search-result snippet of the manual's factory list (p. 44) gave these entries. Treat them as medium confidence, because some snippets came from a mislabelled "Roland D-Station" page. — [manualshive snippet](https://manualshive.com/en/manual/novation/drumstation/1711554?page=46)
  - Program 1 "Classic TR909 V1" ("Another setup of this timeless classic")
  - Program 16 "'Power' TR909" (distortion on bass, snare and hi-hats)
  - Program 18 "'A Bit Off' TR909" (note-off recognition)
  - Program 24 "Classic TR909 Ind." (individual outputs: 1 = bass, 2 = snare, 3 = hi-hats)
  - "'Hardcore' TR909: Distortion effect on 808/909 Bass drums"
  - "'Tune Me Up': Key velocity Mod - Tuning on all 808/909 drums"
- There are 25 preset kits and 15 user kits, with SysEx dumps. — [SOS](https://www.soundonsound.com/reviews/novation-drumstation); [Polynominal](https://www.polynominal.com/novation-drum-station/index.html)
- **MIDI note map** (C1 = note 24). Format: note, 808 mode / 909 mode. — [Zoë Blade, citing the 1996 manual pp. 18, 23 and its addendum](https://notebook.zoeblade.com/DrumStation_MIDI_map.html)
  - Low octave: 24 909 BD / 808 BD; 25 909 RS / 808 RS; 26 909 SD / 808 SD; 27 909 CP / 808 CP; 28 909 LT / 808 LT; 29 909 MT / 808 MT; 30 909 CH / 808 CH; 31 909 HT / 808 HT; 32 909 crash / 808 crash (cymbal); 33 909 ride / none; 34 909 OH / 808 OH.
  - Main octave: 36 808 BD / 909 BD; 37 RS; 38 SD; 39 CP; 40 SD; 41 LT; 42 CH; 43 LT; 44 CH; 45 MT; 46 OH; 47 MT; 48 HT; 49 crash; 50 HT; 51 none / 909 ride.
  - Fixed 808 notes: 56 808 cowbell; 62 808 high conga; 63 808 mid conga; 64 808 low conga; 70 808 maracas; 75 808 claves.
  - Mode is switched in the GM utility menu ("-" for 808 mode, "+" for 909 mode).
- An "Assign Bank" maps a single drum across an octave of keys. A General MIDI remap facility is included. — [SOS](https://www.soundonsound.com/reviews/novation-drumstation)

**RZ-1, R-50, R-50e, XD-5, K3**
- **RZ-1:** 12 preset PCM sounds plus 4 RAM sample pads. — [VSE](https://www.vintagesynth.com/casio/rz-1)
  - Outgoing note numbers follow "the standard found on... Yamaha drum machines" and are "fixed, not programmable". The actual numbers are not given. — [IM review](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164)
  - The documentation includes sound ROMs "A/B" as EPROM dumps. — [Polynominal](https://www.polynominal.com/sample-packs/casio-rz1/)
  - On the modded unit, one pitch knob controls the first eight preset sounds, and the other controls the remaining four plus the samples. — [Circuitbenders](https://www.circuitbenders.co.uk/newsarchive/RZ1.html)
- **Kawai R-50:** 24 sounds, 12-bit, 32 kHz. — [sequencer.de](https://www.sequencer.de/syns/kawai/R100_R50.html)
- **Kawai XD-5:** 256 waveforms, 64 patches and 16 DrumKits. — [VSE XD-5](https://www.vintagesynth.com/kawai/xd-5)
- **Kawai K3:** 32 digital waveforms. Some are samples of acoustic instruments, including percussion and piano according to VSE. — [VSE K3](https://www.vintagesynth.com/kawai/k3)

### Inferences
- **Do the Quasimidi files line up?** The numbering does not match the manual.
  - A = 50, B = 135 and C = 39 files (224 in total). The manual's categories are 26/25/7/128/28 (214 by the headings, 212 names printed).
  - B's count (135) equals 128 drumset + 7 hi-hats. But B001 is a low, tonal sound, while the first printed drumset entry is "606ClHH", a bright closed hat. So B is not in manual order.
  - Content profile from WAV headers (length, and zero crossings per second as a brightness proxy):
    - A001-A029: 0.7-17.3 s, mostly noisy or bright. A007 is a 4.3 s low tone.
    - A030-A050: short, very bright.
    - B: mostly 0.5-1.0 s, with clicks at B010, B022, B034-037, B053, B063 and B079. B124-B135 are 12 files of about 30-150 ms at full scale with almost no zero crossings, which looks like clicks or pulses.
    - C: mixed. C001, C022, C031, C033-035 and C039 are low.
  - Treat the 309 pack as unlabelled. A listening pass would be needed to name the files.
- **Do the Cheetah files line up?** 48 files against 41 documented ROM sounds means 7 are unexplained. They could be cartridge sounds, edited variants or a different ROM; this is unknown. Header-based grouping, low confidence:
  - CHTMD01-05: low and short, likely the 5 bass drums.
  - 06-12: noisy mid, snare-like. That's 7 files against 6 documented snares.
  - 13-16: very bright, likely the 4 hi-hats. 13 is 0.12 s, 14 is 0.30 s, 15 is 0.60 s and 16 is 0.18 s, which fits Closed / Mid / Open / Pedal.
  - 17-20: low, 0.37-0.60 s, toms.
  - 21-28: low-mid, 0.18-0.39 s, toms or tonal percussion.
  - 29-32: bright and long (0.45-1.05 s), cymbals. That's 4 against 3 documented.
  - 33-47: short mixed sounds, percussion.
  - 48: low, 0.26 s, possibly the bass guitar.
- **Does the DrumStation pack line up?** Yes, offset by one.
  - Pack Kit00 = program 1 ("Classic TR909 V1").
  - Pack 15 "Power TR909" = program 16.
  - Pack 17 "A Bit Off TR909" = program 18.
  - The Readme's omitted "023/024" = programs 24-25, the individual-output kits.
- **What the DrumStation kit names suggest:** The names describe parameter and velocity tweaks rather than different samples:
  - Distortion: Power, Hardcore.
  - Velocity routing: Velo, Tune Me Up.
  - Note-off recognition: A Bit Off.
  - Likely shorter decays or cut-off: Cut.
  - Likely dynamics settings: Dynamic.

  That's why every kit folder holds the full 16 + 11 voice set.

### Gaps
- No official ROM order was found for the MD16 (it's in the zipped scanned manual), the RZ-1, the R-50/R-50e or the XD-5.
- The RZ-1's default note numbers and the XD-5's default kit and note map were not found.
- The contents of the 309's 10 factory percussion sets were not found.
- The name of DrumStation program 25 was not found.

## 6. What does each pack folder contain?

### Takeaway
- **Named by sound:** The Casio, Kawai R-50, R-50e, XD-5 and SX-240 packs are small one-shot sets with descriptive names.
- **Empty:** All 32 Kawai K3 files contain no audio.
- **Numbered only:** Cheetah MD16 (48) and Quasimidi 309 (224) use numbers with no names.
- **DrumStation:** Full 27-voice renders of 23 factory kits.
- **Loops:** Possibly one, the VL-Tone "DaDaDa" phrase.

### Cited Findings (all local inspection of `~/Splice/sounds/packs`, read-only)
- **Casio RZ-1:** 12 stereo 16-bit/44.1 kHz files: Bassdrum, Clap, Cowbell, Crash, Hat Closed, Hat Open, Ride, Rim Shot, Snaredrum, Tom H, Tom L, Tom M. This is the full 12-voice factory set, with no sample-pad content.
- **Casio RZ1:** The same 12 voices as mono 16-bit/44.1 kHz files: RZ1Clap, RZ1Cowbell, RZ1Crash, RZ1Hat_C, RZ1Hat_O, RZ1Kick, RZ1Ride, RZ1Rimshot, RZ1Snare, RZ1TomHi, RZ1TomLo, RZ1TomMid.
- **Casio SK-1:** 6 stereo files: Bassdrum, Hat Closed, Hat Open, Snaredrum, Tom H, Tom L.
- **Casio SK1:** The same 6 sounds as mono files: SK1Kick, SK1Snare, SK1Hat_C, SK1Hat_O, SK1Tom_Hi, SK1Tom_Lo.
- **Casio VL-1:** 3 stereo files: Bassdrum.wav (0.050 s), Hi Hat.wav (0.028 s), Snaredrum-01.wav (0.194 s).
- **Casio VL-Tone:** 6 mono files: the five preset tones as single notes (Piano, Fantasy, Violin, Flute, Guitar, 0.47-0.58 s each) plus "Casio VL1 DaDaDa.wav" (3.4 s, probably a phrase or loop; not played).
- **Kawai R50:** 24 mono files: Kick01-03, Snare01-03, TomH, TomM, TomL, HatC, HatO, Crash01, Crash02, China, Ride01, Ride02, Claps, Cowbell, Claves, Agogo, Conga, Timbale, Shaker, Tamborine (spelled that way).
- **Kawai R50e:** 24 mono files: R50eKick01-03, R50eSnare01-04, R50eRimshot, R50eTomA_Hi, R50eTomA_Lo, R50eTomE_Hi, R50eTomE_Mid, R50eTomE_Lo, R50eHat_C, R50eHat_O, R50eCrash, R50eClap, R50eSnap, R50eHiQ, R50eOrch01, R50eOrch02, R50eGuitar1, R50eGuitar2, and "R50Timp.wav" (missing the "e" in its prefix).
- **Kawai XD5:** 17 mono files: XD5Kick01-05, XD5Snare01-07, XD5TomHi, XD5TomLo, XD5TomE, XD5HatC, XD5HatO.
- **Kawai K3:** 32 files, K3M_00 to K3M_31. Each is 44 bytes: a RIFF/WAVE header with a data chunk of size 0. All are empty.
- **Kawai SX240:** 14 mono files:
  - Toms: hightom, medtom, lowtom, floortom (0.6-0.7 s)
  - Snares: snare1, snare2 (0.44-0.50 s)
  - Effects: zap (0.04 s), ringmod (0.58 s), bigrez1 and bigrez2 (3.2-3.3 s)
  - Bass notes: fatbass-c2, fatbass-g2, fatbass-c3, fatbass-c4 (2.2-2.7 s)
- **Cheetah MD16:** 48 mono 16-bit/44.1 kHz files, CHTMD01-CHTMD48, named only by number, plus readme.txt saying there is no name list.
- **Quasimidi 309:** 224 mono 16-bit/44.1 kHz files, named only by number: "QuasiA 001-050", "QuasiB 001-135" and "QuasiC 001-039". Plus readme.txt saying there is no name list.
- **Novation Drumstation:** 23 folders, Kit00-Kit22, with 27 files each (621 WAVs), plus Readme.txt.
  - Naming is `DS<kit><808|909><Sound>.wav`.
  - The 808 files are Kick, Snare, TomLo, TomMid, TomHi, CongaLo, CongaMid, CongaHi, Rimshot, Clave, Clap, Maracas, Cowbell, Cymbal, Hat_C, Hat_O.
  - The 909 files are Kick, Snare, TomLo, TomMid, TomHi, Rimshot, Clap, Hat_C, Hat_O, Crash, Ride.
  - Two names are inconsistent: "DS09909TomHI.wav" has a capital I, and "DS21808Claves.wav" is used instead of "Clave".

### Inferences
- The two RZ-1 folders are two different captures of the same 12 ROM voices, one stereo and one mono, with different lengths. For example, the hat-open file is 0.68 s in one folder and 0.60 s in the other. The same applies to the two SK-1 folders.
- Because the K3 pack has exactly 32 files, it was probably meant to hold the K3/K3m's 32 ROM waveforms, one per file.

### Gaps
- None for listing. The contents of the numbered files are unknown; see section 5.

## 7. Factory preset patterns (names, and step grids where a source shows them)

### Takeaway
- **Names found:** The VL-1 (10 rhythms) and the SK-1 (11 rhythms).
- **Presets that exist but are unnamed:** The 309 has 100 ROM patterns and 99 preset motifs. The MD16 has demo programs.
- **No step grids** were found for any machine.
- **No patterns:** The DrumStation and XD-5 have no sequencer. No preset patterns are documented for the RZ-1, R-50 or R-50e.

### Cited Findings
- **Casio VL-1:** The rhythms are March, Waltz, 4-Beat, Swing, Rock-1, Rock-2, Bossanova, Samba, Rhumba and Beguine. — [German Wikipedia VL-1](https://de.wikipedia.org/wiki/Casio_VL-1)
- **Casio VL-1 rhythm count:** English Wikipedia says there are 10 built-in rhythms and names only Rock-1 and Rock-2. — [Wikipedia VL-1](https://en.wikipedia.org/wiki/Casio_VL-1)
- **Casio CK-200:** This keyboard reportedly has the "Same 10 rhythms (and drum sounds), including the 'Rock 1' rhythm (aka: Trio's Da Da Da drum pattern)". The page shows no step pattern. — [matrixsynth](https://www.matrixsynth.com/2018/03/casio-ck-200-casio-vl-1-rock-1-rhythm.html)
- **Casio SK-1:** 11 drum patterns: "Disco, rock, pops, march, samba, bossa nova, rhumba, 4 beat, swing, slow rock, and waltz". — [VSE SK-1](https://www.vintagesynth.com/casio/sk-1)
- **Quasimidi 309:** 100 unerasable ROM patterns plus 99 preset motifs, which SOS describes as "extremely fine replications of typical rave and dance styles", including "a wry nod in Kraftwerk's direction". — [SOS](https://www.soundonsound.com/reviews/quasimidi-rave-o-lution-309)
- **Quasimidi 309 numbering:** The patterns are numbered 00-99. Pressing play starts with P01. — [309 manual](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)
- **Cheetah MD16:** Preset demo programs (dance, techno and hip-hop beats) are included, but none are named. — [SOS](https://www.soundonsound.com/reviews/cheetah-md16)
- **Casio RZ-1:** No preset patterns are mentioned. The supplied cassette holds sounds, not patterns. — [IM review](https://www.muzines.co.uk/articles/casio-digital-sampling-rhythm-composer-rz-1/5164)
- **Novation DrumStation:** It has no internal step sequencer. — [Wikipedia DrumStation](https://en.wikipedia.org/wiki/Novation_DrumStation)
- **Quasimidi 309 licence note:** The manual's "Warnung" (warning) says using the preset motifs and patterns in your own music production is allowed. Commercially distributing samples of the sounds and preset patterns (on sampling CD, Internet, floppy disk or other media) is forbidden without QUASIMIDI's permission. Copyright 1997. — [309 manual, early pages](https://www.vintagesynth.com/sites/default/files/2017-05/309Man.pdf)

### Inferences
- If someone later finds and transcribes the 309's ROM patterns, using them in your own tracks is permitted by the manual. Redistributing them as a pattern pack would need permission.

### Gaps
- No published step grid was found for any VL-1 or SK-1 rhythm, any 309 ROM pattern or any MD16 demo. Search ran out before dedicated searches for step charts could be done.
- Under the constraints, no grid has been reconstructed.

## 8. Famous recordings that used each machine, with step charts of their grooves

### Takeaway
- **VL-1:** The one strongly attributed drum use is Trio's "Da Da Da" (1982), on the Rock-1 preset. I found no published step chart of it.
- **Other machines:** Mostly named users rather than specific tracks. The DrumStation has one titled recording, Underworld's *Everything, Everything*, but only via a secondary pointer.
- **No grids** were found.

### Cited Findings
**Casio VL-1**
- Trio, "Da Da Da" (1982), used the Rock-1 rhythm preset and the Piano voice. Wikipedia cites Paphides, *The Times* (2009), but flags that link as dead. — [Wikipedia VL-1](https://en.wikipedia.org/wiki/Casio_VL-1)
- German Wikipedia also says the song's rhythm is reproduced by Rock-1, with no citation. — [German Wikipedia](https://de.wikipedia.org/wiki/Casio_VL-1)
- The song's own Wikipedia article does not mention the VL-1 or its drum pattern. — [Wikipedia Da Da Da](https://en.wikipedia.org/wiki/Da_Da_Da)
- Other credits, all from [Wikipedia VL-1](https://en.wikipedia.org/wiki/Casio_VL-1):
  - Hazel O'Connor, "Hanging Around" (*Cover Plus*), used the "Rock-2" drum sound. No citation is given.
  - The Human League, "Get Carter" (*Dare*). Wikipedia cites Adams, *Herald Sun* (2009); no specific feature is named.
  - Fergie, "Clumsy" (2007), used a default electronic beep for the melody, not the rhythm. Wikipedia cites *Happy Mag* (2017).
- The Fall, *The Man Whose Head Expanded*, is credited without a citation. — [German Wikipedia](https://de.wikipedia.org/wiki/Casio_VL-1)

**Casio SK-1** — all from [Wikipedia SK-1](https://en.wikipedia.org/wiki/Casio_SK-1)
- Blur (Damon Albarn), "Advert" (*Modern Life Is Rubbish*). No citation is given.
- Turnstyle, "Happier Than Metallica" and "Sad Rambo", used the sample function.
- Mount Eerie, *Eleven Old Songs of Mount Eerie*.
- DJ Hype used it in his jungle productions, citing Belle-Fortune's *All Crews*.
- Autechre had it among their first equipment, citing *Fact* (2017).
- VSE also lists Fatboy Slim, Beck, Portishead, NIN, Blur and others, without tracks. — [VSE SK-1](https://www.vintagesynth.com/casio/sk-1)

**Casio RZ-1**
- Users with no tracks named: Prince Paul, Autechre, Steve Poindexter, DJ Mike Smooth, Raw Dope Posse, Christian Vogel. — [VSE RZ-1](https://www.vintagesynth.com/casio/rz-1)
- The RZ-1's samples are "cropping up on a number of Dance Mania tracks", and it is popular with ghetto house producers. — [Attack Magazine](https://attackmagazine.com/features/ten-of-the-best-hardware-drum-machines/3)
- A Reverb article reportedly says RZA got his start crafting beats on the RZ-1. I saw this only in a search snippet; the page returned 403. — [Reverb](https://reverb.com/news/the-casio-rz-1-an-entry-level-sampler-behind-top-tier-beats)

**Kawai XD-5 and K3**
- XD-5: VSE says only that Mouse On Mars "might use it". — [VSE XD-5](https://www.vintagesynth.com/kawai/xd-5)
- K3: users are Jan Hammer and Patrick O'Hearn, with no tracks named. — [VSE K3](https://www.vintagesynth.com/kawai/k3)

**Quasimidi 309**
- Users: Apollo 440, Nine Inch Nails and KMFDM, with no tracks named. — [VSE 309](https://www.vintagesynth.com/quasimidi/rave-o-lution-309)
- Wikipedia adds Beastie Boys. — [Wikipedia 309](https://en.wikipedia.org/wiki/Quasimidi_Rave-O-Lution_309)

**Novation DrumStation**
- Users: Mike Banks, Laurent Garnier and Massive Attack, cited to Detroit Techno Militia and Sound On Sound. — [Wikipedia DrumStation](https://en.wikipedia.org/wiki/Novation_DrumStation)
- Massive Attack and Underworld are listed as users, citing Paul Tingen, "Underworld: The Making of 'Everything, Everything'", SOS, December 2000. — [Zoë Blade](https://notebook.zoeblade.com/DrumStation.html)

**No users found**
- No users or recordings were found for the Kawai R-50, R-50e or SX-240, or the Cheetah MD16. — [Sonic State R-50](https://sonicstate.com/synth/kawai_r50/); [VSE SX-240](https://www.vintagesynth.com/kawai/sx-240); [SOS MD16](https://www.soundonsound.com/reviews/cheetah-md16)

### Inferences
- **Trio "Da Da Da":** The track's drum part is reportedly the stock VL-1 Rock-1 preset. So a faithful clip would be the Rock-1 preset itself, but no published grid of Rock-1 was found. The pack's "Casio VL1 DaDaDa.wav" may be a recording of it, which could be checked by listening.

### Gaps
- No step charts or transcriptions were found for any recording listed here.
- The Underworld credit is second-hand. I didn't open the SOS article itself.
- No specific track was verified for the RZ-1, 309, MD16, R-50/R-50e, XD-5, K3 or SX-240.

## 9. Free, clearly licensed MIDI pattern files for these machines

### Takeaway
None found. Web search was exhausted before dedicated MIDI-file searches could be run, so this is untested rather than confirmed absent.

### Cited Findings
- No source consulted offered downloadable MIDI pattern files for these machines.

### Inferences
- None.

### Gaps
- MIDI-file sources were not searched (session search limit reached).

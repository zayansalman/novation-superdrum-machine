# Early rhythm boxes and synths: hardware setup, factory rhythms and famous uses (Ace Tone Rhythm Ace, Univox Micro Rhythmer 12, Sound Master SR-88, MFB-512, Doepfer MS-404, Moog/Realistic MG-1, Rhodes Polaris, Serge Modular)

Scope note for the report writer: the shared WebSearch budget (200 searches per turn, shared by all agents) ran out part-way through this assignment. After that point only known URLs could be fetched, so some gaps below (Univox rhythm names, MIDI files, published step charts, Serge drum-patching docs) are "not searched further", not "proven absent". Pack facts come from a read-only listing and header/waveform analysis of the local files (nothing was played, moved or changed).

## 1. What voices does each machine have, in front-panel order, with the exact labels? (For synths: how drum sounds are made)

### Takeaway
Only the MFB-512 has a primary-source voice list (a 1984 magazine review), and even that gives no panel order or panel labels. The Ace Tone FR-1, Univox MR-12 and Sound Master SR-88 have partial or second-hand lists, and no source fetched gives their exact panel labels or order. The four synths have no drum section at all. Drums on them are patches built from a noise source, a resonant (often self-oscillating) low-pass filter and short envelopes. Their relevant controls are well documented for the MS-404, MG-1 and Polaris, and only loosely for the Serge.

### Cited Findings

**Ace Tone Rhythm Ace FR-1 (preset rhythm box)**
- The FR-1 has four push buttons for four instruments: cymbal, claves, cowbell and bass drum. The Swiss museum SMEM says they play each voice manually — [SMEM](https://www.smemmusic.ch/fr/node/1391); djjondent describes four round white buttons that mute those same four sounds — [djjondent](https://djjondent.blogspot.com/2014/11/ace-tone-fr-1-rolands-first-drum-machine.html).
- A demo write-up calls them "cancel" buttons: FR-1 = bass drum, cowbell, claves, cymbal; FR-2L = snare, claves, cymbal; FR-1 and FR-2 are "basically the same unit" (same PCB, same presets) — [MatrixSynth / ohm_studi_ohm, 2023](https://www.matrixsynth.com/2023/11/the-ace-tone-rhythm-ace-family-fr-1.html).
- Total voice count: Tubbutec's FR-1 MIDI retrofit guide says all 10 drum voices can be played over MIDI, and that the "Brush" sound can be made velocity-sensitive — [Tubbutec FR-1](https://tubbutec.de/?p=4719).
- On the FR-2 voice boards, Tubbutec names Cymbal and Maracas triggers and a Brush (B) point — [Tubbutec FR-2](https://tubbutec.de/?p=4693).
- Conflicting count: polynominal lists "Polyphony of 4" and 4 pad buttons — [polynominal](https://www.polynominal.com/ace-tone-fr1). This likely counts the buttons, not the voices (inferred).
- Construction: fully transistorized analog; presets only; internal clock only (no external sync); mono 1/4" output — [polynominal](https://www.polynominal.com/ace-tone-fr1).
- Ace Electronic's 1970 rhythm-generator patent (Kakehashi) describes sound generators for bongo, maracas, cymbal and snare drum. It is a later design and not specific to the FR-1 — [US3651241](https://patents.google.com/patent/US3651241A/en).
- Year conflict: 1967 per Wikipedia (citing Gordon Reid, Sound On Sound 2004) — [Wikipedia: Drum machine](https://en.wikipedia.org/wiki/Drum_machine), [Wikipedia: Ace Tone](https://en.wikipedia.org/wiki/Ace_Tone); 1965 per [SMEM](https://www.smemmusic.ch/fr/node/1391), [polynominal](https://www.polynominal.com/ace-tone-fr1) and [sequencer.de](https://www.sequencer.de/syns/acetone/RhythmAceFR1.html).
- Brands: Hammond put it in its organs; in the US it was sold as Multivox (Sorkin); in the UK as the Bentley Rhythm Ace — [Wikipedia: Drum machine](https://en.wikipedia.org/wiki/Drum_machine), [djjondent](https://djjondent.blogspot.com/2014/11/ace-tone-fr-1-rolands-first-drum-machine.html).
- Related models with different voice sets: the FR-6's sounds are listed as Kick, Snare, Tom 1/2, Claves, Hit (seen only in a search-result summary of SMEM's FR-6 page; the page itself redirected); the Bentley FR-8L has faders for Cymbal/High-Hat/Maracas, Guiro, Snare Drum, Bass Drum (search summary of [SMEM FR-8L](https://smemmusic.ch/fr/node/336)); the Roland TR-77 is an updated FR-8L — [Wikipedia: Ace Tone](https://en.wikipedia.org/wiki/Ace_Tone).

**Univox Micro Rhythmer 12 (MR-12)**
- Effects Database lists the MR-12 with 12 rhythms. It says the Sound Master SD-3 "Disco Beat" is functionally equivalent and has 5 voices: kick, snare, hi-hat, cymbal, rimshot. This was seen only in search-result summaries; the pages returned HTTP 403 when fetched, so it is unverified — [Effects Database MR-12](https://www.effectsdatabase.com/model/univox/microrhythmer12), [Effects Database SD-3](https://www.effectsdatabase.com/model/soundmaster/discobeat).
- A 2011 commenter is looking for "a Univox Micro Rhythmer 12 or a Soundmaster Disco Beat SD3", which supports the pairing — [MatrixSynth 2005 post](https://www.matrixsynth.com/2005/10/univox-mr-12x-new-flickr-shot.html).
- Sibling MR-8 (8 rhythms), for context: pedal-format box with a Tempo knob and claves and snare sounds. It has internal trimmers for claves length (up to self-oscillation), sound balance ("more or less snare and highs") and tempo, and a single output jack — [Pedal of the Day](https://www.pedal-of-the-day.com/?p=23559).
- Univox was Unicord's US brand. Korg Mini Pops models were sold under it — [Wikipedia: Drum machine](https://en.wikipedia.org/wiki/Drum_machine). No source fetched names the MR-12's actual maker.

**Sound Master Memory Rhythm SR-88 (programmable)**
- VSE lists 4 analog voices: Kick, Snare, Closed Hi-Hat, Cymbal. There is no rim shot, and the hi-hat is fully programmable. Dated 1981 — [Vintage Synth Explorer](https://www.vintagesynth.com/soundmaster/memory-rhythm-sr-88).
- Rhythmic Robot lists four sounds: kick, snare, crash and hats — [Rhythmic Robot](https://www.rhythmicrobot.com/?p=811). Kit Monsters lists kick, snare, hi-hat and cymbal — [Kit Monsters](https://kitmonsters.com/kit/sound-master/sound-master-memory-rhythm-sr-88).
- The AudioThing emulation names 5 sounds: Kick, Snare, Hi Hat 1, Hi Hat 2, Cymbal — [AudioThing](https://www.audiothing.net/instruments/sr-88/). A MusicRadar review counts five channels (Kick, Snare, Cymbal and two hi-hats); this was seen only in a search summary — [MusicRadar review](https://musicradar.com/reviews/tech/audiothing-sr-88-641008).
- A seller calls it basically identical to the Boss DR-55, except that the hi-hat can be programmed without mods — [MatrixSynth 2025 listing](https://www.matrixsynth.com/2025/02/sound-master-sr-88-analog-drum-machine.html). A Sonic State user review says the same — [Sonic State](https://www.sonicstate.com/synth/soundmaster_sr88/).
- Dating conflict: 1981 per VSE; "1980?" per [Sonic State](https://www.sonicstate.com/synth/soundmaster_sr88/).

**MFB-512 (Fricke, Berlin; sample-based)**
- Paul White's review in Electronics & Music Maker (June 1984) lists the voices as bass drum, snare, three toms, handclaps, cymbal, and open and closed hi-hats. The nine sampled sounds sit on one EPROM, so they can't be swapped — [E&MM via muzines](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888).
- Hollow Sun also says nine sampled drum sounds — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/fricke/index.html). sequencer.de instead says 8 voices / "8 rom samples" and dates it 1980 — [sequencer.de](https://www.sequencer.de/syns/mfb/MFB512.html). The 1980 date conflicts with the 1984 review and with the 501 (its non-programmable predecessor) being from 1980.
- Context: its analog predecessor, the MFB-501 (1980), has ten voices labeled BD, SD, TT, LB, HB, H1, H2, HH, LC, SC. Its two cymbals share one switch — [Bonedo](https://www.bonedo.de/artikel/vintage-drum-machine-mfb-501).

**Doepfer MS-404 (synth, 1994)**
- Architecture:
  - One true analog VCO with a waveform switch (sawtooth / off / rectangle). Pulse width is adjustable and LFO1 can modulate it.
  - White noise can be selected in place of the VCO.
  - 24 dB low-pass filter with resonance up to self-oscillation. Keyboard tracking switches off / half / full.
  - Full ADSR envelope.
  - Two triangle LFOs, from very slow up to 5 kHz: LFO1 goes to VCO pitch or pulse width, LFO2 to the filter.
  - Adjustable glide.
  - External audio input that replaces the VCO or noise.
  - 15 knobs and 6 switches; 1U rack.
  - [Doepfer](https://www.doepfer.de/ms404e.htm).
- VSE calls it basically a TB-303 emulator and dates it 1994 — [VSE](https://www.vintagesynth.com/doepfer/ms-404).
- How drums are made, as a general analog method: a kick is a low tone (triangle or filtered saw) with a fast AR envelope on both volume and a slight pitch drop, plus a short click — [SOS Synth Secrets, Jan 2002](https://www.soundonsound.com/techniques/synthesizing-drums-bass-drum). A snare is tone partials plus a noise layer, each with its own decay, through a low-pass filter — [SOS Synth Secrets, Mar 2002](https://www.soundonsound.com/techniques/synthesizing-drums-snare-drum).

**Moog/Realistic Concertmate MG-1 (synth, 1981)**
- Architecture:
  - Two tone sources with sync and detune: one square or sawtooth, the other pulse or sawtooth.
  - Digital pseudo-random noise.
  - "Bell Tone" (amplitude/ring modulation of VCO1 and VCO2).
  - 24 dB/oct low-pass filter with 3-position keyboard tracking that can self-oscillate.
  - Envelope with "Rise Time" (attack) and "Fall Time" (decay/release), sustain on/off, triggered by the keyboard or the LFO.
  - LFO with triangle, square and sample-and-hold.
  - VCA with keyed / hold / envelope modes; the switch is labeled "Tone Sources".
  - "Glide"; CV/Gate inputs; 32 keys; a divide-down polyphonic organ section feeding the same filter and VCA.
  - [Wikipedia](https://en.wikipedia.org/wiki/Moog_Concertmate_MG-1).
- VSE: the filter has cutoff, emphasis and envelope amount, and the "Contour" envelope (ASR) can go to both amp and filter — [VSE](https://www.vintagesynth.com/realistic/concertmate-mg-1).

**Rhodes Polaris (synth, 1984)**
- From the 1984 sales primer:
  - 6 voices, each with 2 oscillators (sawtooth and pulse with pulse-width modulation).
  - 61-note velocity-sensitive keyboard.
  - Digital envelopes, pitched as fast enough for very percussive sounds.
  - 132 programs; keyboard split and voice linking.
  - Polyphonic sequencer (12 sequences, about 650 notes, real-time only); drum-machine sync interface; tempo tap; MIDI; $1995.
  - [Polaris Sales Primer, Steve Grom, Sept 1984](http://www.rhodeschroma.com/content/polaris/salesprimer.pdf).
- From the service manual:
  - Dual oscillator chip giving triangle and sawtooth; pulses come from comparators.
  - Digital ring modulation (an exclusive-OR of the two pulse waves); hard sync.
  - A digital noise generator (about 100 kHz bit stream, filtered toward pink) that can be switched into each voice.
  - Four-pole low-pass filter. Resonance is set in 8 steps; step 7 is self-oscillation.
  - Main and alt outputs.
  - [Polaris service manual, circuit descriptions](http://www.rhodeschroma.com/?id=polarisservicecircuitdescriptions).

**Serge Modular (synth, first systems 1973)**
- Modules include:
  - Dual Universal Slope Generator / Dual Transient Generator.
  - Variable Q VCF (2-pole state-variable, 12 dB/oct).
  - Resonant Equalizer.
  - Wave Multiplier.
  - Noise generator (later with sample-and-hold).
  - Programmer sequencer and 16-stage TKB.
  - Ring modulator, frequency shifter and quadrature oscillator.
  - [Wikipedia](https://en.wikipedia.org/wiki/Serge_synthesizer), [VSE](https://www.vintagesynth.com/serge/modular).
- The current Random*Source VCFQ has simultaneous low-pass, high-pass, band-pass and notch outputs, self-oscillation, a "trigger in" and a "LOW mode" — [Random*Source VCFQ](https://serge-modular.com/serge_4x4?mod=RS_VCFQSM4X4). The Resonant EQ is a ten-band filter with bands spaced a major seventh apart — [Random*Source Res EQ](https://serge-modular.com/serge_4x4?mod=RS_RESEQ-VCM4X4).

### Inferences
- **FR-1 voice list (inferred):** at least 7 of its 10 voices can be named from sources: bass drum, snare (via the same-PCB FR-2L), brush, cymbal, maracas, claves, cowbell. Only four are panel-accessible (the instrument buttons). Their left-to-right order is unknown; sources list them as cymbal, claves, cowbell, bass drum.
- **The pack is probably not an FR-1 (inferred, low confidence).** The FR-1 sources never mention a hi-hat, rim shot, conga, guiro or bongo. Yet the pack's "Acetone Rhythm Ace" sub-folder has Cl Hat, Rim, Hi/Lo Bongo, Lo Conga and Guiro, and the top-level set has open and closed hats. Both points to a later, larger Rhythm Ace model (FR-3/6/7L/8L class), or to names chosen by the sampler's maker. The exact model can't be identified from the files: there is no metadata, and nothing was played. Hollow Sun, which sells a "Rhythm Ace" set in the same collection as its MFB-512 set, dates its unit "around 1970" — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/rhythmace/index.html). The "smpl"-chunk export style shared by the pack's Rhythm Ace and Fricke folders hints at that source, but this is unproven.
- **SR-88 kit:** the hardware probably has 4 voices plus "held" variants (see Q2), so a faithful kit is BD, SD, HH, CY with the long snare and long hat as alternates.
- **Synth kits are patches, not voices.** Panel order doesn't apply; the per-sound controls listed in the JSON are the synth parameters that would shape such a sound (inferred). Nothing documents how these specific pack samples were programmed.
- **MS-404 snare limit (inferred):** noise is selectable instead of the VCO, not mixed with it. So an MS-404 snare is noise-only or noise through a resonant filter, rather than tone plus noise. With a low-pass filter only, its hats are low-passed noise.

### Gaps
- No FR-1 owner's or service manual was found. Three of its ten voices are unidentified, and the exact panel labels and order are unknown.
- No MR-12 manual or panel photo text was found. Its voices, rhythm names, maker and year are unknown. The Effects Database data could not be fetched (403).
- No SR-88 manual was found, so exact panel labels and order are unknown.
- MFB-512 panel labels and order are unknown. The review lists voices but not panel layout, and no German manual was found.
- Serge: no Serge-authored text describing percussion patches ("pinging" a filter or Resonant EQ with a trigger) was fetched. The technique is described here only as inferred.

## 2. Which sounds share one voice or cut each other off?

### Takeaway
There are documented hard cut-offs only on the MFB-512: the three toms are one sample, so one tom at a time, and the cymbal shares with the hi-hats, so a hat cuts the cymbal's tail. On the SR-88 the "long" snare and hat are the same circuits held on, so each should choke with its short partner. The monophonic synths (MS-404, MG-1) cut every sound with the next. The Polaris is 6-voice polyphonic, and the Serge depends on the patch.

### Cited Findings
- **MFB-512, toms:** all tom sounds come from one sample, so two toms cannot play at once — [E&MM 1984](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888).
- **MFB-512, cymbal and hats:** the review says the hi-hats and cymbal work "in much the same manner", so a hi-hat on the next beat cuts the cymbal's decay short — [E&MM 1984](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888). Whether open and closed hats cut each other is not stated explicitly.
- **SR-88, held sounds:** holding the step-time buttons makes sounds sustain. The short hat becomes an extended hiss, and the crash and snare sustain while held — [Rhythmic Robot](https://www.rhythmicrobot.com/?p=811).
- **SR-88, hat and cymbal are separate:** putting hi-hat and cymbal on the same step gives some dynamic variation, so they can sound together — [VSE](https://www.vintagesynth.com/soundmaster/memory-rhythm-sr-88).
- **SR-88, trigger and SQ jack:** the trigger output is taken from the cymbal, and plugging into the "SQ" jack removes the cymbal from the main output — [MatrixSynth 2025 listing](https://www.matrixsynth.com/2025/02/sound-master-sr-88-analog-drum-machine.html).
- **MFB-501 (context):** its long and short cymbal share one switch — [Bonedo](https://www.bonedo.de/artikel/vintage-drum-machine-mfb-501).
- **MS-404 and MG-1 are monophonic:** MS-404 per [VSE](https://www.vintagesynth.com/doepfer/ms-404); MG-1 per [Wikipedia](https://en.wikipedia.org/wiki/Moog_Concertmate_MG-1). The MG-1's poly organ section runs through the same single filter and VCA.
- **Polaris:** 6 analog channels with dynamic voice allocation — [Sales Primer](http://www.rhodeschroma.com/content/polaris/salesprimer.pdf).

### Inferences
- **MFB-512 choke groups (inferred):** Tom H / Tom M / Tom L in one group, and cymbal / open hat / closed hat in another. The review's "same manner as the toms" implies one shared channel.
- **SR-88 choke groups (inferred):** Snare short with Snare long (pack SHORTSN / LONGSN), and Hat short with Hat long (SHORTHI / LONGHI). The pack's "Open Hat" is the held hat, not a separate voice.
- **MS-404 and MG-1:** a strict emulation would put every sound in one choke group, since one voice plays at a time. This is optional for a Drum Rack.
- **Polaris and Serge:** no inherent choke.

### Gaps
- FR-1: no source describes shared circuits or cut-offs. A "polyphony 4" claim conflicts with the 10-voice count.
- MR-12: unknown.
- MFB-512: the open-versus-closed hat choke is not confirmed. Hollow Sun says there are eight individual outputs, but the voice-to-output mapping isn't documented, so it's unclear how outputs relate to the shared channels.

## 3. What controls does each voice have? How does accent work? Any built-in effects?

### Takeaway
None of the four drum boxes has per-voice level, tune or decay knobs.
- **FR-1:** tempo and volume, plus four instrument buttons; no accent.
- **SR-88:** a global tone (low-pass) control; no accent.
- **MFB-512:** a master tune and programmable accent steps.
- **MR-12:** unknown; its sibling has internal trimmers only.

On the synths:
- **MS-404:** has a true accent, from velocity or CC7 with an accent knob.
- **Polaris:** velocity can control volume and/or timbre.
- **MG-1:** no accent.
- **Serge:** whatever you patch.

No machine has built-in reverb, delay or compression.

### Cited Findings
- **FR-1 controls:** "Tempo, Volume" plus four buttons — [SMEM](https://www.smemmusic.ch/fr/node/1391). Start/stop pedal; select a rhythm, then set the volume and tempo pots; no programming — [polynominal](https://www.polynominal.com/ace-tone-fr1). All FR units can start and stop from a foot pedal, and they are easy to mod with extra mute buttons, individual levels and outputs — [MatrixSynth 2023](https://www.matrixsynth.com/2023/11/the-ace-tone-rhythm-ace-family-fr-1.html). Effects: none are mentioned — [polynominal](https://www.polynominal.com/ace-tone-fr1).
- **SR-88 controls:** Rhythmic Robot describes a "tone" control that is basically a low-pass filter across the outputs, and notes there were no decay settings — [Rhythmic Robot](https://www.rhythmicrobot.com/?p=811). Programming is step-by-step: select a sound, then press start for a hit or stop for a rest — [VSE](https://www.vintagesynth.com/soundmaster/memory-rhythm-sr-88), [Sonic State](https://www.sonicstate.com/synth/soundmaster_sr88/).
- **SR-88 accent and effects:** there is no accent feature, and VSE lists effects as "None" — [VSE](https://www.vintagesynth.com/soundmaster/memory-rhythm-sr-88). The plugin's per-sound pitch, pan and level, plus its filter, overdrive, compressor and reverb, are emulation add-ons — [AudioThing](https://www.audiothing.net/instruments/sr-88/).
- **MFB-512 controls:** front panel has tempo, start, a 3-position record toggle, and a multifunction switch with five positions (Play, Chain Select, Instrument Select, Accent, Reset/Erase). It also has a measure switch and binary bank switches F–A. Rear panel: master tune for all voices, trigger in/out, footswitch jacks for start/stop and fills, mono or stereo outs, and DIN individual outputs. The voices can't be triggered from external pads — [E&MM 1984](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888).
- **MFB-512 accent:** accents are entered in record mode with the red (instrument) and black (rest) buttons. Their sonic effect isn't described — [E&MM 1984](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888).
- **MR-12:** no control list was found. Its sibling MR-8 has a Tempo knob plus internal trimmers for claves length, balance and tempo — [Pedal of the Day](https://www.pedal-of-the-day.com/?p=23559).
- **MS-404 accent:** the VCA envelope amount ("accent") follows MIDI volume (CC7) and/or velocity, and an accent knob sets the depth. Filter cutoff can follow any MIDI controller and/or velocity. Glide switches on and off via CC65, and retrigger can be switched on or off — [Doepfer](https://www.doepfer.de/ms404e.htm). VSE adds that all parameters are MIDI-controllable and velocity gives the accent — [VSE](https://www.vintagesynth.com/doepfer/ms-404).
- **MG-1 controls:** Tone Source settings, "Contour" with Rise Time and Fall Time and sustain on/off, filter cutoff, emphasis and contour amount, keyboard tracking, "Bell Tone", noise, LFO (triangle, square, S&H), VCA mode switch ("Tone Sources"), and "Glide". It has no pitch or mod wheels — [Wikipedia](https://en.wikipedia.org/wiki/Moog_Concertmate_MG-1), [VSE](https://www.vintagesynth.com/realistic/concertmate-mg-1).
- **Polaris:** velocity can be assigned to volume and/or timbre; the envelopes are digital and give the fast attacks needed for percussive sounds — [Sales Primer](http://www.rhodeschroma.com/content/polaris/salesprimer.pdf). Resonance has 8 steps, the top one self-oscillating; there is a noise switch per voice, plus ring mod and hard sync — [service manual](http://www.rhodeschroma.com/?id=polarisservicecircuitdescriptions).
- **Serge:** the VCFQ has a trigger input, a LOW mode and self-oscillation — [Random*Source VCFQ](https://serge-modular.com/serge_4x4?mod=RS_VCFQSM4X4). Slope generators and envelopes come from the DUSG and transient generators — [Wikipedia](https://en.wikipedia.org/wiki/Serge_synthesizer), [VSE](https://www.vintagesynth.com/serge/modular).
- **General drum-synthesis controls:**
  - A kick needs a VCA with an attack-release envelope, a small pitch drop from the same envelope, and a short click from a fast filter sweep or noise burst — [SOS, Jan 2002](https://www.soundonsound.com/techniques/synthesizing-drums-bass-drum).
  - A snare needs a noise generator with its own VCA and envelope, a low-pass filter whose cutoff tracks hit strength, and a tone layer with a separate, shorter decay — [SOS, Mar 2002](https://www.soundonsound.com/techniques/synthesizing-drums-snare-drum).

### Inferences
- **Drum Rack mapping:**
  - FR-1, SR-88 and MFB-512: per-pad volume and tuning are modern conveniences; the hardware had none, apart from the MFB's global master tune.
  - MFB-512: accent should map to a velocity layer.
  - FR-1 and SR-88: keep velocity fixed.
- **SR-88 tone control:** put one global low-pass (Auto Filter) on the kit to mimic it.
- **Serge percussion (inferred, unsourced):** the classic method is "pinging". A short trigger or pulse hits a high-Q VCFQ, or the Resonant EQ, which rings at its tuned frequency. The pack's "Clink" and "Click" sounds look like that kind of patch. This was not verified from a Serge document.

### Gaps
- **FR-1:** no documentation of accent or any per-voice trimmers.
- **MR-12:** controls are entirely undocumented.
- **MFB-512:** what accent does to the sound (louder? brighter?) is unknown.
- **Polaris:** the exact envelope stages (ADSR or other) and the LFO controls were not confirmed. The parameter appendix wasn't retrieved, and the owner's manual is a scanned PDF that wasn't read.
- **MS-404:** the exact names of its 15 knobs and 6 switches were not retrieved.

## 4. What does each pack folder contain?

### Takeaway
Three folder pairs are duplicates. "Rhythm-Ace", "Sound Master, Memory Rhythm SR-88" and "MFB-512" are renamed, stereo, peak-normalized copies of "Ace Tone Rhythm Ace" (top level), "Sound Master" and "Fricke MFB512", with 10 ms of silence added at the end. So use one of each pair, not both. Only the Ace Tone folder and the MFB-512 folder contain loops. There are no MIDI files anywhere.

### Cited Findings
(Source for this whole section: read-only `ls -R`, `afinfo` durations, WAV-header chunks and waveform correlation of the files under [~/Splice/sounds/packs](file://~/Splice/sounds/packs). Nothing was played or modified.)

**Ace Tone Rhythm Ace**
- **Top level:** 16 mono 16-bit/44.1 kHz one-shots with no metadata:
  - CLAVE (0.09 s), HHCL (0.05 s), HHOP (0.32 s)
  - KICK1, KICK2, KICK3 (about 0.63–0.66 s)
  - SNARE1 (0.11 s), SNARE2 (0.12 s), SNARE3 (0.32 s)
  - PERC1–PERC7 (0.05–0.45 s)
  - Names are generic, and PERC1–7 aren't identified.
- **Sub-folder "Acetone Rhythm Ace":** 12 named mono one-shots, prefix "RA", each with a sampler "smpl" chunk:
  - Cl Hat, Clave, Cowbell, Cymbal, Guiro, Hi Bongo, Kick, Lo Bongo, Lo Conga, Maracas, Rim, Snare
  - "RA Rim" is only 9 ms long.
- **Sub-folder "Rhythm_Ace_loops":** 12 mono loops, "Rhythm Ace LP1"–"LP12", from 1.83 to 7.31 s, with smpl chunks. No rhythm names or tempos are given.

**Rhythm-Ace**
- 16 stereo one-shots that duplicate the 16 top-level Ace Tone files. Waveform correlation is at least 0.999, some after a 5–9-sample shift; each file is exactly 441 samples longer and peak-normalized.
- Renaming map:
  - KICK1–3 → Bassdrum-01 to 03; CLAVE → Clave; HHCL → Hat Closed; HHOP → Hat Open; SNARE1–3 → Snaredrum-01 to 03
  - PERC1 → Tom H; PERC2 → Tom L; PERC3–6 → Percussion-01 to 04; PERC7 → Click
- The "Tom H / Tom L / Click" names are the renamer's labels, not hardware names.

**Univox Microrhythmer-12**
- 4 stereo one-shots: Bassdrum (0.23 s), Closed Hat (0.10 s), Open Hat (0.94 s), Snaredrum (0.98 s, long tail).

**Sound Master**
- 6 mono one-shots: KICK (0.19 s), SHORTSN (0.15 s), LONGSN (1.42 s), SHORTHI (0.08 s), LONGHI (1.26 s), CRASH (0.81 s).

**Sound Master, Memory Rhythm SR-88**
- 6 stereo duplicates of "Sound Master" (correlation at least 0.999; plus 10 ms each):
  - KICK → Bassdrum; SHORTSN → Snare-1; LONGSN → Snare-2
  - SHORTHI → Closed Hat; LONGHI → Open Hat; CRASH → Crash

**Fricke MFB512**
- 9 mono one-shots with smpl chunks:
  - mfb_kick (0.07 s), mfb_snare (0.14 s), mfb_clap (0.18 s)
  - mfb_hitom (0.36 s), mfb_mid_tom (0.31 s), mfb_lo_tom (0.27 s)
  - mfb_cl_hat (0.16 s), mfb_op_hat (1.72 s), mfb_cymbal (0.78 s)
- A rough pitch estimate (autocorrelation, not listening) puts the toms at about 148, 128 and 107 Hz, so the hi/mid/lo labels match pitch order.

**MFB-512**
- 9 stereo duplicates of "Fricke MFB512" (correlation at least 0.999; plus 10 ms each):
  - Bassdrum, Snaredrum, Clap, Tom H, Tom M, Tom L, Hat Closed, Hat Open, Crash (= mfb_cymbal)
- Plus one extra: "512 loop.wav" (stereo, 1.71 s).

**Doepfer MS-404**
- 6 stereo one-shots: Bassdrum (1.02 s), Bassdrum Reverse (0.21 s), Snaredrum (0.50 s), Tom (0.37 s), Hat Closed (0.14 s), Hat Open (0.15 s).

**Moog Concertmate MG-1**
- 5 stereo one-shots: Bassdrum-01 (0.30 s), Bassdrum-02 (0.58 s), Bassdrum-03 (1.10 s), Snaredrum-1 (0.80 s), Snaredrum-2 (0.49 s).

**Rhodes Polaris**
- 12 stereo one-shots: Bassdrum-01 to 04 (0.96–1.83 s), Noise-1 to 4 (0.13–0.16 s), Snaredrum-01 to 04 (0.82–1.08 s).

**Serge Modular**
- 7 stereo one-shots: Bassdrum (0.42 s), Claves (0.10 s), Click-01 to 04 (0.01–0.09 s), Clink (0.15 s).

### Inferences
- **Which copy to use:** the 10 ms pads are at the end, not the start, since onsets fall on the same sample index. So either copy times correctly. Prefer the named stereo copies for readability, or the mono originals to save space.
- **"512 loop.wav":** at 1.71 s, this is plausibly one 4/4 bar at about 140 BPM (inferred from duration only; not listened to).
- **Ace Tone loops:** the "Rhythm_Ace_loops" are probably recordings of preset rhythms, but which rhythms is unknown without listening.
- **Unusually short files:** "RA Rim" (9 ms) and "Click-04" (13 ms) may be truncated captures (inferred).

### Gaps
- Which hardware model and which voice each unnamed file (PERC1–7, Noise-1–4, Click-01–04) represents cannot be confirmed without listening, which was out of scope.

## 5. Factory preset rhythms: names, plus step grids where a source shows them

### Takeaway
- **FR-1:** the 16 rhythm names are firmly established. Two sources agree, apart from one apparent typo.
- **MR-12:** has 12 rhythms whose names were not found.
- **SR-88:** a programmable box (6×16-step and 2×12-step patterns) with no documented factory rhythms.
- **MFB-512:** ships with an unnamed factory set.
- **Step grids:** no source found shows a step grid for any of these machines, so every grid is null.

### Cited Findings
- **FR-1, 16 presets in SMEM order:** Waltz, Dixieland, Western, Rock'n Roll, Slow Rock, Bosa Nova [sic], Fox Trot, Swing, Tango, Beguine, Rhumba, Samba, Mambo, Cha-Cha, Sniffle [sic], March — [SMEM](https://www.smemmusic.ch/fr/node/1391).
- **FR-1 demo timeline:** a demo video runs through the same 16 in the same order, but with "SHUFFLE" in slot 15. It then plays the combinations ROCK N ROLL + BOSSANOVA, FOXTROT + SWING, SAMBA + CHA CHA, SHUFFLE + MARCH and BOSSA NOVA + BEGUINE — [MatrixSynth 2024](https://www.matrixsynth.com/2024/10/ace-tone-rhythm-ace-fr-1-demo.html). So "Sniffle" is a typo for Shuffle.
- **FR-1 combinations:** pressing two rhythm buttons together cascades and mixes the patterns, and 16 presets give more than a hundred variations — [djjondent](https://djjondent.blogspot.com/2014/11/ace-tone-fr-1-rolands-first-drum-machine.html).
- **FR-1 pattern circuit:** patterns come from a diode matrix driven by a pulse generator and a frequency-dividing counter — [djjondent](https://djjondent.blogspot.com/2014/11/ace-tone-fr-1-rolands-first-drum-machine.html), [Wikipedia: Drum machine](https://en.wikipedia.org/wiki/Drum_machine).
- **FR-2L:** has the same 16 rhythms (Synthmania lists them in reverse: March … Waltz), but fewer combination options — [Synthmania](https://synthmania.com/rhythm_ace_fr-2l.htm).
- **FR-3, for contrast:** a different set: 2 Beat, 4 Beat, Waltz, Slow Rock, Rock'n'Roll, Bossa Nova, Samba, Mambo, Rhumba, Beguine. A rotary switch adds Fox Trot 1/2, Swing 1/2/3, March, Haba-Nera and Tango — [SMEM FR-3](https://www.smemmusic.ch/de/node/335).
- **No timing data in the patent:** the 1970 Ace patent's text gives counter structures but no instrument-by-step timing table — [US3651241](https://patents.google.com/patent/US3651241A/en).
- **MR-12:** 12 rhythms; Effects Database lists the SD-3's categories as disco, rock, pop and march variations. Seen only in a search summary — [Effects Database SD-3](https://www.effectsdatabase.com/model/soundmaster/discobeat).
- **SR-88 pattern memory:** six 16-step patterns and two 12-step patterns. Playback is bar A, bar B, A+B, or fill-in; there is no song mode, and patterns switch on the fly — [VSE](https://www.vintagesynth.com/soundmaster/memory-rhythm-sr-88). There are programmable fill-ins, and four AA batteries keep the memory — [MatrixSynth 2025](https://www.matrixsynth.com/2025/02/sound-master-sr-88-analog-drum-machine.html).
- **MFB-512:** supplied with a "useful set of rhythm patterns", which are not named. Memory is 64 rhythms plus 64 fill-ins, up to 8 chains and 2048 measures, with up to 16 steps per measure and measures that can be doubled. The measure switch plays rhythm only, rhythm and fill alternating, or three rhythms then a fill — [E&MM 1984](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888).
- **MFB-501 presets, context only (not the 512):** 64 presets selected by a 6-bit binary code, including Walzer, Cha-Cha-Cha, Marsch, Rock, Punk Rock, Boogie, Disco, Latin and Funk Rock; Jazz Rock 3 is in 11/8 and Funk Rock 8 in 15/8 — [Bonedo](https://www.bonedo.de/artikel/vintage-drum-machine-mfb-501).
- **Polaris:** 132 factory voice programs and a user sequencer with 12 sequences, but no factory rhythm patterns — [Sales Primer](http://www.rhodeschroma.com/content/polaris/salesprimer.pdf).

### Inferences
- **SR-88 grid size:** the pattern structure mirrors the Boss DR-55 (see Q1), so MIDI clips should be 16-step bars, or 12-step bars for triplet patterns.
- **FR-1 timing (inferred):** the FR-1 runs on an internal clock with no swing control. Shuffle and Slow Rock feel would have to come from the matrix itself, probably at a triplet-capable resolution, but this is not documented.

### Gaps
- No published step chart or transcription of any FR-1 preset was found. The FR-1 service manual (which might show the diode matrix) was not found, and searches ran out before step-chart searches could be completed.
- No rhythm names were found for the MR-12, no factory patterns for the SR-88, and no factory pattern names for the MFB-512.

## 6. Famous recordings that verifiably used each machine (with step charts if published)

### Takeaway
- **FR-1 family:** two well-sourced uses. Kingdom Come's *Journey* (1973; Bentley Rhythm Ace, the UK-badged FR-1, per CD liner notes) and J.J. Cale's *Naturally* (1971; a drum machine on "Crazy Mama" and "Call Me the Breeze", attributed to the FR-1 by a dealer).
- **Serge:** Plastikman's *Consumed* (1998) used Serge filters on percussion.
- **Everything else:** only artist-level claims with no track named, or nothing at all.
- **Step charts:** none found for any of these recordings.

### Cited Findings
- **Kingdom Come, *Journey*:**
  - Recorded Nov–Dec 1972 and released 1973; a drum machine supplies the percussion.
  - The page names the machine as the Bentley Rhythm Ace, the British version of the FR-1, citing the Castle Music 2003 CD liner notes.
  - Tracks: "Time Captives", "Triangles", "Gypsy", "Superficial Roadblocks", "Conception", "Spirit of Joy", "Come Alive".
  - [Wikipedia](https://en.wikipedia.org/wiki/Journey_(Kingdom_Come_album)).
- **J.J. Cale, *Naturally* (1971):**
  - The album says "Call Me the Breeze" was recorded with a primitive drum machine.
  - In a 2004 Vintage Guitar interview, Cale says most people didn't realize the first album used an electric drum machine, and that he cut "Crazy Mama" and "Call Me the Breeze" with Carl Radle on bass.
  - The personnel list credits Karl Himmel on drums for "Call Me the Breeze", an unreconciled conflict.
  - [Wikipedia](https://en.wikipedia.org/wiki/Naturally_(J._J._Cale_album)).
  - Model: a dealer says the FR-1 is the model Cale used on *Naturally* — [Soundgas](https://soundgas.com/products/ace-tone-rhythm-ace-fr-1-drum-machine).
- **Serge, Plastikman, *Consumed* (1998):**
  - On the title track, a tom/conga sound from a Kawai drum machine was opened and closed through a Serge filter.
  - About ten minutes in, a Serge riff distorts from too much filter resonance.
  - On the earlier Concept 1 releases (1996), kicks and percussion went through Serge filters.
  - [SOS Classic Tracks](https://www.soundonsound.com/techniques/classic-tracks-plastikman-consumed).
- **Serge, TONTO:** Serge custom modules for TONTO were used on several Stevie Wonder albums (no titles given) — [Wikipedia](https://en.wikipedia.org/wiki/Serge_synthesizer).
- **SR-88, artist-level only and conflicting:**
  - VSE lists the Cocteau Twins as users — [VSE](https://www.vintagesynth.com/soundmaster/memory-rhythm-sr-88).
  - Kit Monsters adds Blancmange and The Woodentops, saying all the early Woodentops material was written on it — [Kit Monsters](https://kitmonsters.com/kit/sound-master/sound-master-memory-rhythm-sr-88).
  - Against this, Wikipedia's *Garlands* (1982) page cites "stark TR808 drums" and credits Robin Guthrie with "drum machine" without naming a model — [Wikipedia Garlands](https://en.wikipedia.org/wiki/Garlands_(album)).
  - The band's own history mentions a drum machine on the demos ("Speak No Evil", "Perhaps Some Other Aeon", "Objects D'Art") and on *Garlands*, but never names it — [cocteautwins.com](https://cocteautwins.com/chapter-one.html).
- **MS-404, artist-level only:** used by Hardfloor and Josh Wink, with no tracks named — [VSE](https://www.vintagesynth.com/doepfer/ms-404).
- **MG-1, artist-level only:** Peter Gabriel, 808 State, Remy Shand and KMFDM, with no tracks named — [VSE](https://www.vintagesynth.com/realistic/concertmate-mg-1). Wikipedia adds names from Equipboard and others, with no recordings and with reliability warnings — [Wikipedia](https://en.wikipedia.org/wiki/Moog_Concertmate_MG-1).
- **MFB-512, MR-12 and Polaris:** no users or recordings were named in any source fetched — [E&MM](https://www.muzines.co.uk/articles/mfb-digital-drum-machine/7888), [Hollow Sun](https://hollowsun.com/nostalgia/vintage/fricke/index.html), [Polaris resources](http://www.rhodeschroma.com/?id=polaris).

### Inferences
- **What to model:** for MIDI-clip work, *Journey* and *Naturally* are the realistic FR-family targets. Their grooves would be FR-1 presets, or combinations of presets, not programmed patterns. Which preset each track uses is not documented.
- **SR-88:** treat the Cocteau Twins link as a claim only. Better primary evidence (Guthrie's archived "Equipment Notes", which Wikipedia cites) couldn't be fetched (web.archive.org is blocked for this tool, and the live page returned 404).

### Gaps
- No published step chart or transcription exists in the sources found for any of these tracks.
- Which preset or preset combination was used on *Journey*, "Crazy Mama" or "Call Me the Breeze" is unknown.
- The exact Rhythm Ace model on *Naturally* rests on a dealer's claim. The Wax Poetics article the dealer cites was not retrieved.

## 7. Free, clearly licensed MIDI pattern files

### Takeaway
None found for any of the eight machines. The search budget ran out before a thorough MIDI search was possible, so treat this as "not found", not "doesn't exist".

### Cited Findings
- No source fetched offered MIDI files for these machines. The only "MIDI" items seen were retrofit kits, not pattern files: Tubbutec's uniPulse can play the FR-1's 10 voices from MIDI with velocity — [Tubbutec FR-1](https://tubbutec.de/?p=4719). AudioThing's SR-88 plugin lets you drag its patterns into a DAW as MIDI (commercial, not free) — [AudioThing](https://www.audiothing.net/instruments/sr-88/).

### Inferences
- For these preset-era and obscure machines, clips will have to come from the published rhythm names plus careful listening to demo recordings. That would be a reconstruction and must be labeled as one; this note doesn't attempt it.

### Gaps
- No search was done of GitHub, Freesound or Pocket Operations-style libraries for these machine names; the search budget was exhausted.

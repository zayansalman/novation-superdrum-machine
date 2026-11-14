# Alesis HR-16, HR-16:B, SR-16, the "SR15" pack, and the DM5: hardware setup, sound banks, patterns, famous uses

Scope note: covers the machines behind the pack folders "Alesis HR-16", "Alesis HR16" (HR-16), "Alesis HR16B" (HR-16:B), "Alesis SR-16", "Alesis SR16" and "Alesis SR15" (SR-16), and "Alesis DM5" (DM5). The SR-16 and DM5 owner's manuals were read in full text. The HR-16 owner's manual was only readable as scattered OCR pages. The web-search budget for this session ran out before every lead could be followed. Those leads are listed under Gaps.

## 1. How are the pads laid out and what is the default kit?

### Takeaway
The HR-16 and HR-16:B have 16 pads, one voice each, labelled Tom 1–4, Ride, Crash, Perc 1–2, Kick, Snare, Closed/Mid/Open Hat, Claps and Perc 3–4. The SR-16 has 12 velocity pads, labelled Kick, Snare, Cls Hat, Open Hat, Claps, Perc 2, Tom 1–3, Ride, Crash and Perc 1. The DM5 has no pads: it has 12 trigger inputs and a 61-note MIDI map per kit.

### Cited Findings
#### HR-16
- The 16 pads default, in order 1–16, to: Tom 1, Tom 2, Tom 3, Tom 4, Ride, Crash, Perc 1, Perc 2, Kick, Snare, Closed Hat, Mid Hat, Open Hat, Claps, Perc 3, Perc 4. Each pad can take any of the 49 samples, and the defaults can be restored with the reset procedure. — [Sound On Sound, Jan 1988, David Mellor (via muzines)](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449)
- The service manual's pattern-data format stores per-pad parameters in this order: KICK, SNARE, CLS HAT, MID HAT, OPN HAT, CLAPS, PERC 3, PERC 4, TOM 1, TOM 2 (page truncated after this). These are the panel labels. — [HR-16 service manual p.26 (manualsdir p.32)](https://www.manualsdir.com/manuals/46570/alesis-hr-16.html?page=32)
- The manual's VOICE page example shows "KICK PAD" assigned to "24' POWER KICK" (OCR). It also says "An empty pattern defaults to a standard voice assignment with no pitch shift, and nominal mix levels." — [HR-16(:B) manual p.18 (manualsdir)](https://www.manualsdir.com/manuals/724207/alesis-hr-16b-mmt-8.html?page=18)
- Each pattern stores its own VOICE, TUNE and MIX setup, so a kit is a per-pattern setting, not a global one. — [SOS Jan 1988](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449); also "Pan assignments for all 16 pads" per Pattern — [SOS Nov 1988, Craig Anderton](https://www.muzines.co.uk/articles/using-the-alesis-hr16-as-an-expander/4005)
- Spec summary: "Keyboard - 16 pads", "Polyphony - 16 voices". — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/hr-16)
#### HR-16:B
- "The operating systems of the Alesis HR-16 and the HR-16:B are identical with a few exceptions." — [HR-16:B manual p.2 (manualsdir)](https://www.manualsdir.com/manuals/724207/alesis-hr-16b-mmt-8.html?page=2)
- The HR-16:B is black and the HR-16 grey. The HR-16:B "had lots of new sounds cool for enough techno and electronic music". — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/hr-16)
#### SR-16
- "Each of the 12 large pads triggers a voice". "The default drum sound assignments are printed in white on the pads." — [SR-16 Reference Manual §1.2D–E](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- The default pad-to-note table, in the manual's order: Kick 036 (C1), Snare 038 (D1), Cls Hat 042 (F#1), Open Hat 046 (A#1), Claps 039 (D#1), Perc 2 067 (G3), Tom 1 048 (C2), Tom 2 045 (A1), Tom 3 041 (F1), Ride 051 (D#2), Crash 049 (C#2), Perc 1 065 (F3). Note assignments are global, not per pattern. — [SR-16 Reference Manual §6.4](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- There are 50 preset and 50 user drum sets. A drum set holds each pad's sound, level, tuning, panning, triggering mode and output. Preset patterns have fixed drum-set assignments. — [SR-16 Reference Manual ch.4](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- "12 rubber pads across the lower front panel" with eight velocity levels. — [Music Technology, Feb 1991, Simon Trask (via muzines)](https://www.muzines.co.uk/articles/alesis-sr16/776)
#### DM5
- The DM5 holds 21 drum sets (00–20), all restorable from ROM. A drum set contains 61 notes, MIDI 36–96 by default. The root-note setting can shift that window anywhere from 0–60 up to 67–127. — [DM5 Reference Manual ch.2 and ch.4](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)
- Default trigger notes: 1 = Bb1/46 Hi-Hat; 2 = C1/36 Bass Drum; 3 = D1/38 Snare; 4 = C2/48 Tom 1; 5 = A1/45 Tom 2; 6 = F1/41 Tom 3; 7 = Eb2/51 Ride Cymbal; 8 = C#2/49 Crash Cymbal 1; 9 = A2/57 Crash Cymbal 2; 10 = D3/62 Conga; 11 = F3/65 Hi Timbale; 12 = G3/67 Hi Agogo. Note 46 "is always the Open Hi-Hat sound (except in Drum Set 18)". A footswitch can make the hi-hat trigger send another note, e.g. F#1/42, "the Closed Hi-Hat sound". Drum Set 18 uses its own default note numbers. — [DM5 Reference Manual, External Triggers Hookup](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)
- The factory kits cover "heavy metal, pop, rock, jazz, Latin, and general percussion", plus techno, rap and world music. No kit names are given. — [Sound On Sound, Sep 2006](https://www.soundonsound.com/reviews/alesis-dm5)

### Inferences
- SR-16 pad numbers 1–12 probably follow the order of the default note table (Kick, Snare, Cls Hat, Open Hat, Claps, Perc 2, Tom 1, Tom 2, Tom 3, Ride, Crash, Perc 1). This is inferred: the manual does not number the pads in text.
- Alesis manuals call MIDI note 36 "C1", the same naming Ableton Live uses. The SR-16 and DM5 default notes (36 kick, 38 snare, 42/46 hats, 41/45/48 toms, 49 crash, 51 ride) can therefore go straight onto a Live Drum Rack's default note layout.
- The HR-16:B probably keeps the same 16 pad labels as the HR-16. This is inferred from the shared operating system and shared manual.

### Gaps
- The HR-16's physical pad rows (e.g. 2×8) and the default sound on every pad except the kick (24" Power Kick) were not found.
- Which ROM sound sits on each SR-16 pad in Drum Set 00 / the "printed in white" defaults: the sound chart shipped with the unit was not found online.
- The DM5 Factory Drum Set Reference Chart (kit names 00–20 and full default note maps) could not be retrieved. ManualsLib returned 403.

## 2. Total sounds, categories (counts and number ranges), and the official ordered sound list

### Takeaway
The HR-16 has 49 sounds. A numbered 1–49 list exists, but only from a secondary source (an EPROM vendor's list), and a 1988 press list uses slightly different names. The HR-16:B's official list was not found; the pack numbers 47 sounds (001–047). The SR-16 has 233 sounds (49 kicks, 59 snares, 51–52 toms, 19 hats, 12 cymbals, 42 percussion), but its official numbered chart was not found. The DM5 has "over 550" sounds in 8 families (Kik, Snr, Tom, Hat, Cym, Prc, Efx, Rnd). Only the Random family's count (15) is published in the sources found.

### Cited Findings
#### HR-16
- There are 49 sounds: "There are a total of 49 sounds to choose from". — [HR-16(:B) manual p.18](https://www.manualsdir.com/manuals/724207/alesis-hr-16b-mmt-8.html?page=18). The pattern data stores sound numbers 0–30H (0–48). — [service manual](https://www.manualsdir.com/manuals/46570/alesis-hr-16.html?page=32)
- Numbered list from a custom-EPROM vendor, quoted on MatrixSynth. Each custom sound replaces the factory sound at the same number, and the factory names are listed: 1 24" Power Kick, 2 22" Deep Kick, 3 22" Power Kick, 4 20" Swift Kick, 5 22" Dbl Hd Kick A, 6 22" Dbl Hd Kick B, 7 22" 60's Kick, 8 22" Gated Kick, 9 Electronic Kick 1, 10 Electronic Kick 2, 11 8x14" Wood Snare, 12 Ambient Snare, 13 13" Brass Piccolo, 14 Gated Snare, 15 Electronic Snare, 16 Rimshot Snare, 17 Sidestick, 18 Brush Hit Snare, 19 10" Power Tom, 20 16" Power Tom, 21 10" Dbl Head Tom, 22 14" Dbl Head Tom, 23 Electronic Tom, 24 Closed HiHat A, 25 Closed HiHat B, 26 Half Open HiHat, 27 Open HiHat, 28 Foot Closed HiHat, 29 Ride Cymbal, 30 Ride Cymbal Bell, 31 Crash Cymbal, 32 Timbale, 33 High Conga Slap, 34 Low Conga Slap, 35 Small Wood Block, 36 Large Wood Block, 37 Rosewood Claves, 38 Cabasa, 39 Maracas A, 40 Maracas B, 41 Shaker, 42 Agogo Bell, 43 Medium Cowbell, 44 Large Cowbell, 45 Triangle, 46 Tambourine, 47 Hand Claps, 48 Finger Snap, 49 Drum Sticks. By name this groups as kicks 1–10, snares/rim/sidestick/brush 11–18, toms 19–23, hats 24–28, cymbals 29–31 and percussion 32–49. — [MatrixSynth (Apr 2011)](https://www.matrixsynth.com/2011/04/alesis-hr-16-custom-sounds-eproms-linn.html)
- The 1988 press list is unnumbered and identical in both SOS articles. It has the same membership but a different order and some different names: 20" kick A, 20" kick B, 22" power kick, 22" 60's kick, 22" double-head kick A/B, 22" ballad kick, 24" power kick, electronic kick 1/2, 8x14" wood snare, 13" brass piccolo (listed twice), snare sidestick, wood ambient snare, snare rimshot, electronic snare, brush hit snare, timbale, 10" power tom, 16" power floor tom, 14"/10" double-head tom, electronic tom, low/high conga slap, closed hi-hat A/B, half open hi-hat, open hi-hat foot, closed hi-hat, ride cymbal, ride cymbal bell, crash cymbal, shaker, small/large wood block, cabasa, agogo, finger snap, drum sticks, medium/large cow bell, claves, maracas A/B, tambourine, triangle, hand claps. — [SOS Jan 1988](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449); [SOS Nov 1988](https://www.muzines.co.uk/articles/using-the-alesis-hr16-as-an-expander/4005)
- Short form: "49 drum sounds, including 10 kicks and 7 snares". — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/hr-16)
#### HR-16:B
- Mixdown says there is "a slightly different set on the later HR-16B model". — [Mixdown](https://mixdownmag.com.au/features/mixdowns-greatest-drum-machines-of-all-time-part-one/). Vintage Synth Explorer gives 1989 and "lots of new sounds". — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/hr-16)
- The count is unresolved. The HR-16:B manual's voice page says 49, but that is probably text carried over from the HR-16 manual. — [manual p.18](https://www.manualsdir.com/manuals/724207/alesis-hr-16b-mmt-8.html?page=18). One search-engine summary of the manual text gave "47 in the HR-16:B", but this was not verified on a page.
#### SR-16
- "over 230 high-fidelity drum/percussion sounds". "The chart included with the SR-16 describes each of the over 230 drum sounds" (the chart is not in the Reference Manual). — [SR-16 Reference Manual §1.1B, §4.2](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- Counts: 49 kicks, 59 snares, 51 toms ("hi, mid and lo versions"), 19 hi-hats, 12 cymbals (ride and crash), 42 percussion (sum 232). 94 of the 233 sounds are stereo. Named sounds include an "808 kick and snare", three pitches of "808 cowbell", "Impact" and "Sample & Hold". Sample & Hold randomly plays one of four sounds: two tunings of the 808 cowbell, a woodblock and an agogo. — [Music Technology Feb 1991](https://www.muzines.co.uk/articles/alesis-sr16/776)
- A search-engine summary (source page not identified) gives toms as 52, which makes the total 233. This conflicts with Music Technology's 51.
- The modern SR-16 Quickstart Guide (Rev C, 52 pages, multilingual) contains no sound list or pattern list. I checked its full text. — [SR16 Quickstart Guide Rev C](https://www.alesis.com/rscdn/920/documents/SR16_Quickstart_Guide_RevC.pdf)
#### DM5
- There are 4 MB of samples. "The Voices have been organized into 8 Voice Families": Kik, Snr, Tom, Hat, Cym ("Cymbals and hi hats"), Prc, Efx and Rnd (Random). Each Random voice "includes a sampling of various other Voices", and a different sample plays on each hit. — [DM5 Reference Manual ch.2, ch.4](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)
- The SOS review counts "over 550 sounds divided into eight categories". The Random group holds 15, "mainly special effects" apart from hi-hats and a few snares. — [SOS Feb 1996, Paul White](https://www.soundonsound.com/reviews/alesis-dm5-0). A later SOS review says "over 500". — [SOS Sep 2006](https://www.soundonsound.com/reviews/alesis-dm5)
- The sound chart is a separate supplementary sheet. Its Kick family begins "Arena", "Producer", "Pwr Rock" (seen only in a search snippet; the page returned 403). — [ManualsLib DM5 Supplementary Manual](https://www.manualslib.com/manual/207485/Alesis-Dm5.html)

### Inferences
- The MatrixSynth numbering (24" Power Kick = 1) matches the manual's example of 24" Power Kick on the kick pad, and the 0–48 sound-number range. That makes it the most likely factory ROM/display order. The SOS 1988 list probably reproduces pre-release literature, which would explain the name differences ("ballad kick", "20" kick A/B" against "Deep/Swift/Gated Kick"). This is an inference: the owner's manual list itself was not seen.
- SR-16 Sample & Hold is a random-switching sound, so it cannot exist as one WAV in any pack.

### Gaps
- The official HR-16 owner's-manual sound table (ManualsLib/ManualMachine/Scribd copies were blocked or OCR-garbled).
- The official HR-16:B sound list and count.
- The official numbered SR-16 sound chart and the ROM number ranges per category.
- DM5 per-family counts (except Random = 15), number ranges, the full sound chart, and the exact total ("over 500" and "over 550" are both quoted).

## 3. Which sounds cut each other off (hi-hat groups, voice assignments)?

### Takeaway
The SR-16 and DM5 have per-pad/per-note trigger modes: Multi, Single, and two cut-off groups (Group 1, Group 2). The manuals give closed and open hi-hat as the "classic use". For the HR-16/HR-16:B, no source found states how the three hi-hat pads interact.

### Cited Findings
- SR-16 ASN MODE per pad: "Multi" lets each hit ring through its full decay. "Single" means a new hit terminates the still-decaying sound. "Group 1 and 2: Pads assigned to a particular group (1 or 2) will cut each other off ... a closed high-hat will cut off an open hi-hat, and hitting an open hi-hat sound will cut off a closed hi-hat." There are 16 voices total, and the voice closest to finishing its decay is stolen. The manual suggests putting all the toms in a group so they use one voice at a time. — [SR-16 Reference Manual §4.6](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- The DM5 GROUP function has the same four options (Multi, Single, Group 1, Group 2) per note, with the same hi-hat example and the same 16-voice stealing rule. — [DM5 Reference Manual, Group](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf). "Sounds can be assigned to groups so that a closed hi-hat cuts off an open one". — [SOS Feb 1996](https://www.soundonsound.com/reviews/alesis-dm5-0)
- DM5 hi-hat pedal mode: the footswitch changes the hi-hat trigger's note (e.g. Bb1/46 open to F#1/42 closed). — [DM5 Reference Manual](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf). The SOS 2006 kit review says the hi-hat pad "switches from open to closed and also generates a closing sound when the pedal is operated". — [SOS Sep 2006](https://www.soundonsound.com/reviews/alesis-dm5)
- The HR-16 has 16 voices, which one review describes as one sound per pad at once. The SOS Jan 1988 review does not describe hat groups. — [SOS Jan 1988](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449)

### Inferences
- For an Ableton rack: SR-16 and DM5 should put closed and open hat in one choke group. The hardware groups are user-assigned, and which factory drum sets put hats in a group is not documented in what I found. Optionally, toms can go in a second group to mimic the "one voice" tip. For the HR-16/HR-16:B, a Cls/Mid/Opn hat choke group is the conventional choice, but this is not confirmed hardware behaviour.

### Gaps
- HR-16/HR-16:B hi-hat cut-off behaviour. A search snippet of the manual mentions "12 of the pads (all pads except Closed Hat, Mid Hat, Open Hat, and Crash)", which hints that those four pads are treated specially, but the full sentence was not retrieved.
- The factory default ASN/Group setting for SR-16 preset drum sets and DM5 preset kits.

## 4. Per-sound parameters (level, tuning, pan, output) and how dynamics/accent work

### Takeaway
All three machines have per-pad/per-note volume 00–99, 7 pan positions, and a choice of two stereo output pairs. Tuning differs: HR-16 –16…+15 steps; SR-16 +3…–4; DM5 +3.00…–4.00 semitones in cent steps. None has an accent control. Dynamics come from velocity: 8 pad levels on the HR-16/SR-16, full MIDI velocity when triggered over MIDI, and "Dynamic Articulation" timbre changes on the SR-16 and DM5.

### Cited Findings
#### HR-16 / HR-16:B
- TUNE: "The range is from -16 to +15". Volume: "adjusted with the slider (00 to 99)", and "The Volume slider on the front controls output 1 only". Pan is "seven position" (<3, <2, <1, <>, 1>, 2>, 3>). Output: stereo output 1 or 2. — [HR-16(:B) manual p.19](https://www.manualsdir.com/manuals/724207/alesis-hr-16b-mmt-8.html?page=19). The service manual matches: pitch 0=–16 to 1FH=+15, volume 0–63H (0–99), pan bits 0=L…6=R, output-assign bit. — [service manual](https://www.manualsdir.com/manuals/46570/alesis-hr-16.html?page=32)
- Craig Anderton describes the tuning as "from 12 semitones flat to almost seven semitones sharp". — [SOS Nov 1988](https://www.muzines.co.uk/articles/using-the-alesis-hr16-as-an-expander/4005)
- Dynamics: pads are velocity-sensitive with "eight distinct levels of resolution", and there are three response curves (Soft, Medium, Loud) or sensitivity off. Quantise runs from 1/4 to 1/64 or off. There is a SWING function (values not given). OFFSET moves events in 1/384-note steps up to 99/384 (not working on the review unit). — [SOS Jan 1988](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449)
#### SR-16
- A voice has these parameters: "Drum sound, tuning, volume, output assignment ... and MIDI note number". Volume runs 00–99. Pan has seven positions: hard left (1), soft left (2), left of center (3), center (4), right of center (5), soft right (6), hard right (7). Tuning runs from "+3 (most sharp) to 0 (normal pitch) to -4 (most flat)". Output is Main or Aux stereo pair. ASN mode is Multi/Single/Group 1/Group 2. — [SR-16 Reference Manual §1.2D, ch.4](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- "There are eight levels of pad volume resolution ... when ... triggering sounds via MIDI, they respond to all 127 MIDI volume levels". The VELOCITY page has 11 responses: Soft, Medium, Loud and Fixed 1–8. "Many sounds use advanced 'dynamic articulation' techniques so that these sounds, when hit loudly, have a different timbre than when they're hit softly." Step mode can change "a Drum Sound's Volume in a Given Step". — [SR-16 Reference Manual §1.2, §2.5, §2.9C](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- Dynamic articulation is clearly audible only on "a few kicks, snares, congas and toms". — [Music Technology Feb 1991](https://www.muzines.co.uk/articles/alesis-sr16/776)
#### DM5
- Per note: Voice (Family/Number). Tune runs "+3.00 (most sharp) to 0 (normal pitch) to -4.00 (most flat)", adjustable by semitone or by cent. MIX gives volume 00–99 and pan in seven positions (<3 … 3>). OUTPUT is Main or Aux. GROUP is Multi/Single/Group 1/Group 2. — [DM5 Reference Manual ch.4](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)
- "Using Dynamic Articulation™ techniques, the timbre (tonal content) and pitch will often change as well". The trigger section has gain, velocity curve, crosstalk, decay and noise parameters. — [DM5 Reference Manual](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)

### Inferences
- In Ableton: map Volume 00–99 to Simpler/Sampler volume, the 7 pan steps to about ±100% in thirds, tuning to Transpose (SR-16/DM5 most likely semitones, –4…+3), Output Main/Aux to rack chains/return routing. A velocity-to-volume curve stands in for the 8 velocity levels. No accent lane is needed.
- The SR-16's "+3…–4" has no stated unit. The DM5 manual uses the same range in semitones and cents, which suggests semitones on the SR-16 too (inferred).

### Gaps
- The HR-16 tuning step size: –16…+15 steps against Anderton's "12 semitones flat to almost seven semitones sharp" implies non-uniform steps. Not resolved.
- The HR-16 swing values.

## 5. Built-in effects or reverb baked into samples; default MIDI note map

### Takeaway
None of these machines has an effects processor. The SR-16 (and its full-ROM "SR15" pack) and the DM5 carry reverb/ambience baked into many samples. The HR-16 and HR-16:B have a few ambient/gated sounds, going by their names. Default notes: SR-16 and DM5 follow a GM-like map (36/38/42/46/48/45/41/49/51). The HR-16's map was readable only from OCR, with gaps.

### Cited Findings
- HR-16: "Effects - None". — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/hr-16). The sound list includes "wood ambient snare" — [SOS Jan 1988](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449) — and "Ambient Snare", "22" Gated Kick", "Gated Snare" — [MatrixSynth list](https://www.matrixsynth.com/2011/04/alesis-hr-16-custom-sounds-eproms-linn.html).
- SR-16: "a mixture of dry and reverbed sounds", and many of the stereo sounds are the reverbed ones. Toms include "deep, booming, reverberant acoustic sounds". — [Music Technology Feb 1991](https://www.muzines.co.uk/articles/alesis-sr16/776). "Some samples have reverb & ambience in them". Its "Effects" line reads "Panning & Dynamic Articulation (modulates tone)". — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/sr-16)
- DM5: many sounds are recorded with ambience or reverb, so "external processing isn't always necessary". No onboard effects are mentioned. — [SOS Feb 1996](https://www.soundonsound.com/reviews/alesis-dm5-0). The reference manual's function list (Voice, Tune, Mix, Output, Drum Set, Ext Trig, Group, MIDI) has no effects section. — [DM5 Reference Manual](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)
- SR-16 default notes: Kick 36, Snare 38, Cls Hat 42, Open Hat 46, Claps 39, Perc 2 67, Tom 1 48, Tom 2 45, Tom 3 41, Ride 51, Crash 49, Perc 1 65. MULTI-DRUMSET mode maps user drum sets 00–09 (and the groups 10–19, …, 40–49) across notes 000–119, 12 pads per octave starting on C. — [SR-16 Reference Manual §6.4, §6.9](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- HR-16/HR-16:B default notes (manual OCR, partly garbled): KICK 035, SNARE 038, CLS HAT 042, MID HAT 044, OPN HAT 046, CLAPS 039, TOM1 048, TOM2 045, TOM3 041, TOM4 reads "063" (doubtful), RIDE 051, CRASH 049, PERC3 067, PERC4 068. PERC1 and PERC2 are unreadable. MIDI drum receive/transmit are off by default. — [HR-16:B manual p.25 (manualsdir OCR)](https://www.manualsdir.com/manuals/724207/alesis-hr-16b-mmt-8.html?page=25)
- DM5 default notes: see Q1 (trigger table). The playable window is 36–96. — [DM5 Reference Manual](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)
- Local check (read-only header/sample analysis of the pack WAVs). In the "Alesis SR15" folder, 91 of 224 files are stereo, and 46 of those have L/R correlation below 0.9, i.e. genuinely wide stereo. These are the Hall/Room/Ambient/Gated/Wet kicks, snares and toms. The cymbals are all mono. — local analysis of `~/Splice/sounds/packs/Alesis SR15` (no web source)

### Inferences
- Do not add reverb to the Room/Hall/Ambient/Gated/Wet SR-16 and DM5 samples in Ableton: it is already in the audio. The dry SR-16 sounds and most HR-16 sounds are dry.
- The SR-16's 94 stereo ROM sounds are mostly the reverbed ones. The SR15 pack's 91 stereo files line up with this almost exactly (see Q6).

### Gaps
- The HR-16 TOM4, PERC1 and PERC2 default notes (OCR unreadable). Whether Perc 1/2 default to 65/67 as on the SR-16 is unknown.

## 6. What does each pack folder contain?

### Takeaway
"Alesis HR-16" (19) and "Alesis HR16" (44) are partial HR-16 sets with descriptive names. "Alesis HR16B" (47) is a complete-looking, contiguously numbered HR-16:B set. "Alesis SR-16" and "Alesis SR16" (52 each) are the same small SR-16 subset in stereo and mono containers. "Alesis SR15" (224) is almost certainly a near-complete SR-16 ROM set that was mislabelled. "Alesis DM5" (470) is a large partial DM5 set with no cymbals and no Random family. There are no loops or MIDI files in any folder.

### Cited Findings (from `ls -R` and read-only `afinfo`/channel analysis on 2026-11-13. Local observation, no web source)
- **Alesis HR-16** (19 files; 16-bit/44.1 kHz, 2-channel but effectively centred mono: L/R correlation ≥0.998, 0 dB balance). Named without numbers: Agogo Bell, Bassdrum, Cabasa, Clap, Claves, Closed Hat, Conga H, Conga L, Maracas, Open Hat, Rim, Shaker, Snaredrum, Timbale, Tom-1, Tom-2, Triangle, Wood Block H, Wood Block L. It has no ride, crash, mid hat, toms 3–4, cowbells, tambourine, snap or sticks, and only one kick and one snare.
- **Alesis HR16** (44 mono 16-bit/44.1 kHz). Prefix "HR16": Kick01–06, Snare01–07, Rimshot, Sidestick, Tom01–04, Hat_C1, Hat_C2, Hat_M, Hat_O, Hat_P, Ride01–02, Crash, Timbale, HiConga, LoConga, Shaker, Block1–2, Clave, Cabasa, Maracas01–02, Agogo, Cowbell01–02, Triangle, Tamborine (sic), Clap, Snap. Compared with the 49-sound ROM: 6 of 10 kicks, 4 of 5 toms, all 5 hats (C1/C2 = closed A/B, M = half-open, O = open, P = foot/pedal, inferred), all 3 cymbals, 17 of 18 percussion (Drum Sticks missing). There are 7 snares against 6 in the ROM, unexplained. Pack numbers do not follow ROM numbers.
- **Alesis HR16B** (47 mono 16-bit/44.1 kHz, numbered 001–047 with no gaps): 001 Monster Kick, 002 Tiled Room Kick, 003 Big Foot, 004 Rap Kick, 005 Techno Kick, 006 Deep Wood Kick, 007 Tight Kick, 008 Combination Snare, 009 Techno Snare, 010 Hi Picolo Rim, 011 HI Picolo Snare, 012 Rap Snare, 013 90s Gated Snare, 014 Reverb Snare, 015 Mid Punch Snare, 016 Fat Snare, 017 Aggressive Snare, 018 Sidestick, 019 Gated Sidestick, 020 Closed Hihat, 021 Mid Hihat, 022 Open Hihat, 023 R&B Closed Hat, 024 Rock Hihat, 025 Hi Power Tom, 026 Mid Power Tom, 027 Aggressive Tom, 028 Crash Cymbal, 029 Ride Cymbal, 030 Open Conga, 031 Conga Slap, 032 Ambient Bongo, 033 Cabasa, 034 Fast Cabasa, 035 Tambourine, 036 Gated Claps, 037 Hi Agogo Bell, 038 Bottles, 039 Pipe, 040 Lip Pop, 041 Ambient Puh, 042 Scratch, 043 Synth Block, 044 Torque Wrench, 045 Trash Can, 046 Glass Break, 047 Jam Block. By number range: kicks 001–007 (7), snares 008–017 (10, including a rim), sidesticks 018–019 (2), hats 020–024 (5), toms 025–027 (3), cymbals 028–029 (2), percussion 030–037 (8), FX/found sounds 038–047 (10).
- **Alesis SR-16** (52 files, 2-channel but effectively mono except "Guiro", corr 0.01, and "Hit", corr 0.97), in sub-folders: Bassdrums (Bassdrum-01–13), Snaredrums (Rim, Snaredrum-01–12), Cymbals (Crash-01–02, Hat Closed-01–03, Hat Open-01–03, Hat Reverse, Ride-01–03), Percussion (Block, Bongo, Clap, Congo, Cowbell, Finger, Guiro, Shaker, Tamb, Timbale, Triangle), Misc (Hit, Metal, Synth Cymbal).
- **Alesis SR16** (52 mono, prefix "SR16"): Kick01–13, Snare01–12, Rimshot, Hat_C1–C3, Hat_O1–O4, Ride01–03, Crash01–02, Block, Bongo, Clap, Conga, Cowbell01–02, FSnap, Guiro, Shaker, Spark, Tamborine, Tank, Timbale, Triangle. It has the same category structure as "Alesis SR-16" (13 kicks, 12 snares + rim, 3 rides, 2 crashes, 7 hats, 14 percussion/misc). Durations differ (e.g. Snare01 0.18 s against Snaredrum-01 0.31 s).
- The free Polynominal SR-16 pack has 53 sounds: "13 kicks", "3 rides", "2 crashes", "8 hats", "13 snares", "14 percussions". It is 24-bit/44 kHz, "© … All Rights Reserved", with no licence stated. — [Polynominal](https://www.polynominal.com/sample-packs/Alesis-SR16-sample-pack/)
- **Alesis SR15** (224 files; 91 stereo/133 mono, 16-bit/44.1 kHz). All files are prefixed "SR16". Sub-folders sr16_kik22 (48: Dry01–12, Dry Wood 1–2, Dry Flabby/Loose, Dbl Head, Room 1–6, Room Flab/Lo1/Lo2/Punch, Hall 1–6, Ambient 1–3, Amb Elect/Low, Elect Boom/Hi/Long/Low/Mid, Flange 1–2, Gated 1–2, Garage), sr16_snares (57: Dry01–08, Room01–12, Hall Lo/Long/Mid, Gated1–2, Gated stick, Elect Hi/Mid/Lo, Ring Hi/Mid/Lo, Ring Tone 1–2, ClapSnare1–3, Piccollo, Sidestick, Flange, Flutter, Crack/Crack2, Coaw 1–2, Smacky01–02, etc.), sr16_toms (50: sets of 3–5 such as Dry 1–5, Room 1–5, Amb 1–5, Hall 1–4, Big Hall 1–4, Cannon 1–4, Hall Can 1–4, Gated 1–4, Flat/Flat Hall/Flat Room 1–3, Elect 1–3, Flange 1–3), sr16_hats22 (17: Closed, Tight, Thin, Small, Sweet, Hard, Edge, Half, Vari, Open1–2, Wet1–2, Reverse1–4), sr16_cym22 (12: Crash, Crash Hi/Mid/Lo/Trash/Flange, Ride Soft/Hard/Bell/Flange/Live1/Live2), sr16_perc22 (40: Agogo Hi/Lo, Bamboo, Block Hi/Mid/Lo, Coldblok, Cabasa, Claps Hi/Lo, Clave Hi/Lo/Wet, Conga Hi/Lo/HiSlap/LoSlap/DynHi/DynLo, Cowbell Hi/Mid/Lo, RapCow Hi/Mid/Lo, Fingersnap, Finger Wide, Firecrack, Fish Lo, Fishstick, Frogfish, Impact, Shaker, Sticks Hi/Lo, Tambourine, Timbale Hi/Mid/Lo, Triangle). The file names have typos ("Prc_ Bamboo" with a leading space, "Timable", "Piccollo").
- **Alesis DM5** (470 mono 16-bit/44.1 kHz, one flat folder). FX01–64 (64); Kick01–95 (95); Snare001–109 (108, **028 missing**); Rim01–09 (9); Hat_C01–10 (9, **C08 missing**); Hat_O01–10 (9, **O07 missing**); Perc001–114 (114); Tom01–25 as Hi/M/Lo variants (62 files; incomplete sets: Tom03/04/05/16/18/19 Hi+Lo only, Tom07 and Tom09 Hi only, Tom08 Lo+M, Tom10 Lo only; Tom25 uses "_Mid" instead of "_M"). There are **no cymbals (Cym family) and no Random family**. "Rim" is not a DM5 family name.

### Inferences
- **"Alesis SR15" = Alesis SR-16 ROM set, mislabelled.** No "SR-15" exists in the sources consulted, and every file is prefixed "SR16". The category counts (48/57/50/17/12/40 = 224) sit within 1–2 of the SR-16's published 49 kicks / 59 snares / 51 toms / 19 hats / 12 cymbals / 42 percussion (Music Technology 1991). The stereo count (91) is close to the published 94 stereo sounds. "Impact" and three-pitch "RapCow" (likely the "three pitches of the 808 cowbell") match sounds named in the review. Sample & Hold is necessarily absent. This makes it by far the most complete SR-16 source of the three SR-16 folders.
- "Alesis SR-16" and "Alesis SR16" look like two renderings of the same ~52-sound subset, structurally close to the free Polynominal 53-sound pack (one hat fewer). That provenance is a guess, not verified.
- "Alesis HR-16" stores mono hardware samples in stereo containers. Use it as mono, and set panning in Ableton, not from the file.
- The DM5 pack's numbering is the sampler's own and probably not the DM5 chart numbering (e.g. separate Rim and Hat_C/Hat_O series). The 44.1 kHz rate differs from the DM5's 48 kHz, so these are recordings/conversions.

### Gaps
- How the pack file numbers map to ROM numbers (SR-16, DM5, HR16) cannot be checked without the official charts.
- Whether the 7th HR16 snare is a duplicate or a re-pitched copy was not checked (no listening, by instruction).

## 7. Factory preset patterns (names and step grids)

### Takeaway
The SR-16 ships with 50 preset patterns (00–49), each with Main A, Main B, Fill A and Fill B, played in by professional drummers across rock to Latin styles. Only one preset name ("Rap 3") was found, and no published step grids. No source found says the HR-16, HR-16:B or DM5 ship with preset rhythm patterns. The DM5 has no sequencer, only a demo sequence.

### Cited Findings
- SR-16: "50 Preset (i.e., can't be edited) Patterns and 50 user-programmable Patterns, each of which can be from 1 to 128 beats long". Each numbered pattern has Main A, Main B, Fill A and Fill B, giving 400 patterns in all with presets. Presets are "a variety of rock, jazz, pop, and other rhythms programmed by professional drummers" with fixed drum-set assignments. To edit one, copy it to a User pattern. — [SR-16 Reference Manual §1.1B, §1.2A–B, §4.1](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)
- Preset styles: rock, hard rock, R&B, funk, blues, rap, techno, reggae, jazz rock, fusion, new age, country, jazz, Latin and ballad. The reviewer is unconvinced by the funk, rap and techno presets except "Rap 3" ("a lively swingbeat rhythm"). — [Music Technology Feb 1991](https://www.muzines.co.uk/articles/alesis-sr16/776)
- The presets were reportedly performed by session drummers rather than programmed and quantised. — [Polynominal](https://www.polynominal.com/sample-packs/Alesis-SR16-sample-pack/). A search summary attributed to a muzines/Music Technology article says the preset list is printed on the unit's bottom panel (not verified on the page itself).
- HR-16: 100 patterns (up to 682 beats) and 100 songs (up to 255 steps). The review mentions no factory demo patterns. — [SOS Jan 1988](https://www.muzines.co.uk/articles/alesis-hr-16-drum-machine/3449)
- DM5: "Playing the Demo Sequence" ([DRUM SET] + [PREVIEW]). There is no pattern sequencer. — [DM5 Reference Manual ch.2](https://www.alesis.com/rscdn/1580/documents/alesis_dm5_refmanual.pdf)

### Inferences
- Because the SR-16 presets were played in rather than quantised (Polynominal), any SR-16 groove MIDI should keep human micro-timing. Its 96 ppqn record resolution ([Music Technology](https://www.muzines.co.uk/articles/alesis-sr16/776)) and swing settings of 54/58/62% ([manual §2.2](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf)) are the hardware's limits.

### Gaps
- The names of the 50 SR-16 presets (bottom-panel list) and any step charts of them. No grids were found, so none are given.
- Whether the HR-16 or HR-16:B shipped with factory demo patterns.

## 8. Famous recordings made with these machines (with groove transcriptions)

### Takeaway
There are credible HR-16 credits: Godflesh "Streetcleaner" (1989), They Might Be Giants "Lincoln" (1988), Prince Paul productions including Big Daddy Kane's "It's a Big Daddy Thing" (1989), and the HR16 was in Orbital's setup for "Chime" (1989). Stereo MC's "Connected" (1992) is claimed but only weakly sourced. No verified tracks were found for the HR-16:B, SR-16 or DM5. No published step charts of any of these grooves were found.

### Cited Findings
- Godflesh, *Streetcleaner* (1989): Broadrick and G.C. Green used an Alesis HR-16 for nearly all the album's percussion. Seen via a search-result summary of Wikipedia; secondary. — [Wikipedia: Streetcleaner](https://en.wikipedia.org/wiki/Streetcleaner)
- They Might Be Giants: the HR-16 was bought partway through recording *Lincoln* (1988) on Chris Butler's recommendation. "It was heavily used on Lincoln, and to a lesser extent on Flood" (1990). This cites John Flansburgh's Tumblr. They also owned an HR-16:B, but its "use in recordings has not been mentioned or identified". — [TMBW wiki: Drum Machine](https://tmbw.net/wiki/Drum_Machine)
- Prince Paul: a Smithsonian NMAAHC object, "Alesis HR-16 drum machine used by Prince Paul". The description says its sounds were used "on almost every record I worked on after 3 Feet High and Rising – Big Daddy Kane, 3rd Bass, Prince Among Thieves, and Stetsasonic". It "can clearly be heard on 'It's a Big Daddy Thing'". The page returned 403, so this was seen only in search snippets. — [visualartsdb mirror of SI object](https://www.visualartsdb.com/artwork/si-nmaahc-ld1-1658220228681-1658220241664-0-alesis-hr-16-drum-machine-used-by-prince-paul)
- Orbital, "Chime" (first recorded summer 1989): Paul Hartnoll says "after that I added 909 and [Alesis] HR16 drum machines" and "The HR16 was Phil's … I was borrowing it". The article does not say which drum parts the HR16 played, and it shows no drum chart. — [SOS Classic Tracks, Dec 2006, Richard Buskin](https://www.soundonsound.com/techniques/classic-tracks-orbital-chime)
- Stereo MC's, "Connected" (1992): Mixdown says the HR-16 is "Famed for being the drum machine used on Stereo MC's track 'Connected' as well as '90s heavyweights Orbital" (no citation). — [Mixdown](https://mixdownmag.com.au/features/mixdowns-greatest-drum-machines-of-all-time-part-one/). The band's own interview says only "We use an Alesis drum machine, just the MIDI notes from that to loop things" (model not named; seen in search snippet). — [Music Technology interview (muzines)](https://www.muzines.co.uk/articles/stereo-speakers/5489)
- User lists without track credits: HR-16(:B), "Orbital, The Grid, Autechre, Sub Dub and the Stereo MC's" — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/hr-16); SR-16, "Autechre and Vangelis" — [Vintage Synth Explorer](https://www.vintagesynth.com/alesis/sr-16).

### Inferences
- Confidence is highest for Godflesh and TMBG (album-level), medium for Prince Paul/Big Daddy Kane (museum object, but seen only via snippet), low to medium for Orbital (the HR16 is in the setup, its role is unspecified), and low for Stereo MC's.

### Gaps
- No published step charts or transcriptions were found for any of these tracks. Grids are left null rather than reconstructed.
- No verified recordings for the HR-16:B, SR-16 or DM5. The search budget ran out before SR-16 and DM5 users (e.g. Autechre, Vangelis, triggered metal kick sounds) could be checked.

## 9. Free, clearly licensed MIDI pattern files

### Takeaway
None found for any of the five machines.

### Cited Findings
- Searches for SR-16 preset-pattern MIDI found none. Synthmania's SR-16 page reportedly links a "Ballroom Rhythms" set of SR-16 pattern programs. This was seen only in a search summary, the format may be sysex/tape rather than MIDI, and no licence was seen. — [Synthmania SR-16](https://synthmania.com/sr-16.htm)
- Polynominal offers SR-16 manuals, OS ROM binaries and a free 53-sample pack, not MIDI. The page is "All Rights Reserved". — [Polynominal](https://www.polynominal.com/sample-packs/Alesis-SR16-sample-pack/)

### Inferences
- The SR-16 can dump patterns as MIDI sysex or tape. — [SR-16 Reference Manual ch.7](https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf). Pattern banks from users may therefore exist as .syx files, which would need the hardware to render to MIDI notes.

### Gaps
- No clearly licensed MIDI files for the HR-16, HR-16:B, SR-16 or DM5 were found. The web-search budget was exhausted before forum archives (Gearspace, KVR) could be checked.

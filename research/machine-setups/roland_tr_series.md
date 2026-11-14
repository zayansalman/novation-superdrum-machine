# Roland TR series (TR-808, TR-909, TR-606, TR-707, TR-727, TR-505, TR-626, Rhythm 33, Rhythm 77): hardware setup, presets and famous grooves

Companion data file: `roland_tr_series.json` (same folder). Research limits: the original owner's manuals are only online as scans on ManualsLib (behind a bot-verification wall, not bypassed) and Roland's support pages returned HTTP 403; the web-search budget ran out part-way, so the remaining facts come from pages already found. All step grids are therefore `null`; see the Gaps sections.

## 1. Voices in front-panel order, with panel labels

### Takeaway
Panel order and labels are solid for the TR-808, TR-909 and TR-606. For the TR-707, 727, 505 and 626 the sound lists are certain, but the exact panel abbreviations and left-to-right order could not be checked, so the JSON uses descriptive labels. The Rhythm 77 voice list comes from one repair blog; no Rhythm 33 voice list was found.

### Cited Findings
- **TR-808 (1980).** Roland's TR-08 recreation lists the voices in this order: BD (Bass Drum), SD (Snare Drum), LC (Low Conga), LT (Low Tom), MC (Mid Conga), MT (Mid Tom), HC (Hi Conga), HT (Hi Tom), CL (Claves), RS (Rim Shot), MA (Maracas), CP (Hand Clap), CB (Cow Bell), CY (Cymbal), OH (Open Hi-Hat), CH (Closed Hi-Hat), plus an ACCENT LEVEL knob — [Roland TR-08 specs](https://www.roland.com/au/products/tr-08/specifications/). The original's voices are analog, not samples — [Wikipedia TR-808](https://en.wikipedia.org/wiki/Roland_TR-808). Launch year: Wikipedia says 1980 (built 1980–83). Roland's support page title says "TR-808 RHYTHM COMPOSER (1981-1983)" (seen as a search-result title; the page returned 403) — [Roland support](https://support.roland.com/hc/en-us/articles/201963539-TR-808-Technical-Specifications). Music Technology says it was "first shown in 1981" — [Music Technology, Nov 1986](https://www.muzines.co.uk/articles/beat-box-chic/983).
- **TR-909 (1983).** Roland's TR-09 recreation lists the instruments in this order: BASS DRUM, SNARE DRUM, LOW TOM, MID TOM, HI TOM, RIM SHOT, HAND CLAP, CLOSED/OPEN HI HAT, CRASH CYMBAL, RIDE CYMBAL — [Roland TR-09 specs](https://www.roland.com/global/products/tr-09/specifications/). There are 11 voices. Crash, ride and the hi-hats are samples; the rest are analog — [Wikipedia TR-909](https://en.wikipedia.org/wiki/Roland_TR-909). Hollow Sun says everything except the snare was sampled, which contradicts Wikipedia — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/909/index.html).
- **TR-606 Drumatix (1981).** Track/instrument selector order: BD, SD, LT, HT, CY, OH, CH, with AC (accent) in the last position. That is seven drum voices — [E&MM, Feb 1982 (Tony Bacon)](https://www.muzines.co.uk/articles/roland-tr606/3696). Analog voices: bass drum, snare, toms, cymbal, open and closed hi-hat — [Wikipedia TR-606](https://en.wikipedia.org/wiki/Roland_TR-606).
- **TR-707.** 15 voices: Bass Drum 1 and 2, Snare Drum 1 and 2, Low/Mid/High Tom, Rimshot, Cowbell, Handclap, Tambourine, Closed Hi-Hat, Open Hi-Hat, Crash, Ride — [IM&RW, Jan 1985 (Bob Henrit)](https://www.muzines.co.uk/articles/roland-tr-707/12363). The machine was reviewed in Dec 1984 — [E&MM, Dec 1984](https://www.muzines.co.uk/articles/roland-tr707/8027). Wikipedia gives a 1985 release — [Wikipedia TR-707](https://en.wikipedia.org/wiki/Roland_TR-707). Roland support titles it "(1984-1989)" (search-result title only) — [Roland support](https://support.roland.com/hc/en-us/articles/201925909-TR-707-Technical-Specifications).
- **TR-727.** 15 sounds: Bongo Hi, Bongo Lo, Conga Mute, Conga Hi, Conga Lo, Timbale Hi, Timbale Lo, Agogo Hi, Agogo Lo, Cabasa, Maracas, Whistle Short, Whistle Long, Quijada, Starchime — [In Tune, Dec 1985 (Nick Graham)](https://www.muzines.co.uk/articles/roland-tr727-rhythm-composer/5584). It is the TR-707 with Latin percussion samples and the same programming system — [E&MM, Aug 1985 (Dan Goldstein)](https://www.muzines.co.uk/articles/latin-lessons/9115); [Wikipedia TR-707](https://en.wikipedia.org/wiki/Roland_TR-707).
- **TR-505 (1986).** 16 sounds, in the spec-list order: low conga, high conga, timbale, low cowbell, high cowbell, handclap, crash, ride, bass drum, snare, low tom, mid tom, high tom, rim shot, closed hi-hat, open hi-hat. There are 16 drum pads — [Making Music, Apr 1986](https://www.muzines.co.uk/articles/roland-tr505/4806). Wikipedia gives the same order, citing manual p. 9 — [Wikipedia TR-505](https://en.wikipedia.org/wiki/Roland_TR-505).
- **TR-626 (1987).** 30 sounds: BD 1/2, SD 1/2/3, Rimshot, Low/Mid/High Tom 1 and 2, Closed and Open Hi-Hat, Tambourine, Cowbell, Low/High Agogo, Low/High Timbale, Low/Open High/Mute High Conga, Handclap, Shaker, Claves, China, Crash, Cup, Ride. Pads 1–14 each hold two sounds, switched with INST CHANGE. Pad 15 is the open hi-hat and pad 16 the closed hi-hat — [Sound On Sound (Derek Johnson)](https://www.soundonsound.com/reviews/roland-tr626). The kit is 12-bit PCM (30 voices) — [Music Technology, Nov 1987](https://www.muzines.co.uk/articles/roland-tr626/2125).
- **Rhythm 77 / TR-77 (1972), Roland's first product.** A repair blog lists 13 voices: bass drum, low conga, low bongo, high bongo, rim shot, cowbell, claves, tambourine, cymbal, hi-hat, maracas, snare drum, guiro — [Mezzoauto TR-77](https://mezzoauto.blogspot.com/2017/05/roland-rhythm-tr-77-how-it-works.html). Audiofanzine describes noise-based voices (snare, maracas, hi-hat, guiro), sine-based low/mid voices including the bass drum, plus bongos and claves — [Audiofanzine TR-77](https://en.audiofanzine.com/drum-machine/roland/TR-77/editorial/articles/the-roland-tr-77-history-and-features-of-monophonic-and-analog-drum-machines.html). Roland's first product was the TR-77, followed the same year by the TR-33 and TR-55 — [Wikipedia (Roland article; the TR-77 title redirects there)](https://en.wikipedia.org/wiki/Roland_TR-77).
- **Rhythm 33 / TR-33 (1972).** Analog preset machine — [SoundProgramming TR-33](https://soundprogramming.net/drum-machines/roland/roland-tr-33/). Neither a voice list nor a panel order was found.

### Inferences
- The TR-08 page puts the conga, claves and maracas label before the tom, rim and clap label in each pair. That suggests the 808 panel prints the alternate on top of each switched pair. The JSON follows the TR-08 order (inferred).
- The 505's 16-sound list is identical in two independent sources, so it is likely the pad 1–16 order (inferred, not confirmed).

### Gaps
- Exact panel abbreviations and left-to-right order for the 707, 727, 505 and 626, and the 626's full pad pairing. These are in the owner's manuals, but the scans are blocked.
- TR-33 voice list. TR-77 panel order and panel labels.

## 2. Shared voices (switches) and sounds that cut each other off

### Takeaway
The 808 has five hardware switch pairs; the 909 and 606 only pair their hi-hats. The 707/727 play 10 of 15 sounds at once and the 505/626 eight voices, so several sounds cut each other off; this is fully documented for the 505 and only partly for the 707, 727 and 626.

### Cited Findings
- **TR-808.** Low/Mid/Hi each switch between conga and tom, sharing one Level and Tuning knob per pair. CL/RS and MA/CP each have a voice selector — [Roland TR-08 specs](https://www.roland.com/au/products/tr-08/specifications/). The three toms switch to congas, "mostly a pitch shift" — [Music Technology, Nov 1986](https://www.muzines.co.uk/articles/beat-box-chic/983).
- **TR-909.** CLOSED/OPEN HI HAT is one section with a shared LEVEL knob — [Roland TR-09 specs](https://www.roland.com/global/products/tr-09/specifications/). The snare and clap share a noise source, so they "phase" when hit together. That is an interaction, not a cut-off — [Wikipedia TR-909](https://en.wikipedia.org/wiki/Roland_TR-909).
- **TR-707.** Two sliders are shared: rimshot with cowbell, and handclap with tambourine. A rimshot and a snare can sit on the same beat — [E&MM, Dec 1984](https://www.muzines.co.uk/articles/roland-tr707/8027). There are 15 samples, but only 10 can play at once. Analog envelopes let one sample serve two sounds, for example the open and closed hi-hats — [Roland "Mod Squad"](https://articles.roland.com/mod-squad-a-history-of-tr-707-and-tr-727-modifications/). Some volume sliders "double-up" (no list given) — [In Tune, Jan 1985](https://www.muzines.co.uk/articles/roland-tr707/8864).
- **TR-727.** Ten individual voice outputs, and one trigger output taken from the "agogo channel" — [E&MM, Aug 1985](https://www.muzines.co.uk/articles/latin-lessons/9115). Like the 707, it plays 15 samples, 10 at once — [Roland "Mod Squad"](https://articles.roland.com/mod-squad-a-history-of-tr-707-and-tr-727-modifications/).
- **TR-505.** 8-voice polyphony, with accent counted as a voice. Sounds in the same group cannot play at once, and programming one erases the other. Groups: open/closed hi-hat; hi/mid/low tom with timbale; hi/low conga; clap/rim shot; crash/ride — [Bonedo](https://www.bonedo.de/?p=530195). Wikipedia adds the cowbell pair, citing manual p. 9 — [Wikipedia TR-505](https://en.wikipedia.org/wiki/Roland_TR-505). Toms, cymbals and hi-hats each share one playback channel — [Making Music, Apr 1986](https://www.muzines.co.uk/articles/roland-tr505/4806).
- **TR-626.** Eight voices. Group 1 is Snare 1, Snare 2, Low Timbale and High Timbale. Group 6 is Bass Drum 1 and 2. The handclap cannot sound with claves, shaker or mute high conga — [Sound On Sound](https://www.soundonsound.com/reviews/roland-tr626). Ride with cup, and crash with china, share a button; at high tempos the second hit cuts off the first — [Music Technology, Nov 1987](https://www.muzines.co.uk/articles/roland-tr626/2125).
- **TR-77.** One slider is shared by maracas, hi-hat and cymbal — [Mezzoauto TR-77](https://mezzoauto.blogspot.com/2017/05/roland-rhythm-tr-77-how-it-works.html). No cut-off behaviour is documented.

### Inferences
- **808 and 606:** closed hat cuts open hat. This is the standard behaviour, but no fetched source states it (inferred). It is in the JSON choke groups.
- **TR-707:** 15 sounds on 10 channels means five pairs. RS/CB and HCP/TAMB are confirmed by the shared sliders. CH/OH is supported by Roland's one-sample-two-envelopes remark. BD1/BD2 and SD1/SD2 are inferred as the remaining two pairs. Crash and ride are probably separate (inferred).
- **TR-727:** the "agogo channel" wording implies Hi/Lo Agogo share one channel (inferred). The other four pairs are unknown. Short/long whistle is a plausible one-sample-two-envelopes pair, by analogy with the 707's hats (speculative; not in the JSON).
- **TR-626:** the eight individual outputs (BD, SD, LT, MT, HT, HH, Crash, Ride) probably correspond to the eight voice groups (inferred). The JSON lists only the groups stated by a source, plus OH/CH.

### Gaps
- Complete voice-group tables for the 707, 727 and 626. They are in the owner's manuals and service notes, which were not readable.

## 3. Per-voice controls, accent, flam, shuffle, tuning

### Takeaway
Only the 808 and 909 have real per-voice sound controls; the 606, 707, 727 and 505 have level only, and the 626 adds global ±7-semitone pitch. Accent is a global per-step track on the 808, 606, 707 and 727; it is per-instrument on the 626 and probably the 909.

### Cited Findings
- **TR-808 controls.** BD: Level, Tone, Decay. SD: Level, Tone, Snappy. Each conga/tom pair: Level, Tuning, voice selector. CL/RS and MA/CP: Level plus selector. CB: Level. CY: Level, Tone, Decay. OH: Level, Decay. CH: Level. ACCENT LEVEL. Pre-scale selector. Features the TR-08 adds (compressor, gain, tune, pan, sub-steps, MIDI) are not on the original — [Roland TR-08 specs](https://www.roland.com/au/products/tr-08/specifications/). The snare knob is labelled "snappy". Some tuning is variable but not programmable. One accent affects every voice on the beat. There is no swing or humanise. Each voice has its own audio output. No MIDI — [Music Technology, Nov 1986](https://www.muzines.co.uk/articles/beat-box-chic/983). Accent is a sequenced "instrument" that makes no sound and raises the other voices — [iO-808 tutorial](https://io808.com/tutorial).
- **TR-909 controls.** BD: Tune, Level, Attack, Decay. SD: Tune, Level, Tone, Snappy. Each tom: Tune, Level, Decay. RS and HC: Level (the TR-09 shares one RIM/CLAP knob). Hi-hats: Level, CH Decay, OH Decay. Crash: Level, Tune. Ride: Level, Tune. TOTAL ACCENT knob. SHUFFLE/FLAM button — [Roland TR-09 specs](https://www.roland.com/global/products/tr-09/specifications/). The sequencer has shuffle and flam. It was the first Roland drum machine with MIDI and has DIN sync in — [Wikipedia TR-909](https://en.wikipedia.org/wiki/Roland_TR-909).
- **TR-606.** Five level knobs cover seven sounds ("four of the sounds are squeezed into two"), plus Accent, Tempo and Volume. AC is written as its own step layer. Four Scale settings, including 3- and 6-step (triplet-type) scales; pattern length is settable (e.g. 12 steps). 32 patterns, 8 tracks. Sync socket and two trigger outputs — [E&MM, Feb 1982](https://www.muzines.co.uk/articles/roland-tr606/3696). "The sounds cannot be edited" — [Wikipedia TR-606](https://en.wikipedia.org/wiki/Roland_TR-606).
- **TR-707.** Eleven faders cover voice levels, accent and overall volume. Flam applies to Snare 2 and the three toms, with adjustable spacing; the shuffle "gap" is adjustable — [IM&RW, Jan 1985](https://www.muzines.co.uk/articles/roland-tr-707/12363). Two accent levels; flam has four intervals; shuffle has four levels; rimshot trigger out at 5 V, 20 ms — [In Tune, Jan 1985](https://www.muzines.co.uk/articles/roland-tr707/8864). Four global shuffle levels. Flam can go on any step (this conflicts with IM&RW). No tuning — [Wikipedia TR-707](https://en.wikipedia.org/wiki/Roland_TR-707). Samples are 25 kHz 8-bit, some 6-bit — [Roland "Mod Squad"](https://articles.roland.com/mod-squad-a-history-of-tr-707-and-tr-727-modifications/).
- **TR-727.** A variable accent applies to the whole beat, never to single voices. No pitch tuning — [E&MM, Aug 1985](https://www.muzines.co.uk/articles/latin-lessons/9115). Accents and flams can be added to any drum — [In Tune, Dec 1985](https://www.muzines.co.uk/articles/roland-tr727-rhythm-composer/5584).
- **TR-505.** Six level steps (0–5) per sound, set globally and not saved with patterns. Accent strength is set the same way. Velocity in, and higher velocity out on accented notes — [Bonedo](https://www.bonedo.de/?p=530195). Accent is set per beat, 0–5 — [Making Music, Apr 1986](https://www.muzines.co.uk/articles/roland-tr505/4806).
- **TR-626.** Each sound tunes ±7 semitones, with one tuning stored per voice. Accent is ±3 per beat per voice. Shuffle and flam are programmable — [Music Technology, Nov 1987](https://www.muzines.co.uk/articles/roland-tr626/2125). Three accent levels per instrument per step. Tuning and level are global, so they also affect the presets — [Sound On Sound](https://www.soundonsound.com/reviews/roland-tr626).
- **TR-77.** Four voice sliders (bass, snare, guiro, maracas/hi-hat/cymbal), a tempo slider, a fade button, a touch-plate start and a restart footswitch — [Mezzoauto TR-77](https://mezzoauto.blogspot.com/2017/05/roland-rhythm-tr-77-how-it-works.html). Also: 2 BEAT and 4 BEAT, BASS & SNARE mode, SHUFFLE mode, a lever that splits the rhythm, a first-beat LED, and a 32-step (2 × 16) diode-matrix sequence — [Audiofanzine TR-77](https://en.audiofanzine.com/drum-machine/roland/TR-77/editorial/articles/the-roland-tr-77-history-and-features-of-monophonic-and-analog-drum-machines.html).
- **TR-33.** A balance knob can mute some drum sounds — [Roland Indonesia chronicle](https://rolandindonesia.com/roland-drum-machine-chronicle-1964-2016/). A Wikipedia-mirror snippet (search result only, page not fetched) says one control balances the bass drum against cymbal, hi-hat and maracas — [Wikipedia mirror](https://ipfs.aleph.im/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Roland_Rhythm_33.html).

### Inferences
- **TR-606 levels:** the five knobs are probably BD, SD, Tom (LT+HT), Cymbal and Hi-hat (OH+CH) (inferred from "four sounds squeezed into two").
- **TR-909 accent:** the original very likely also has per-instrument accent next to Total Accent (my recollection, not confirmed by a fetched source; marked unconfirmed in the JSON).
- **Ableton mapping:** 808 tone/decay/snappy/tuning have no MIDI control on the hardware. Use sample variants (Section 5) or Simpler/Sampler parameters. 909 tune/decay can map to Drum Rack macros.

### Gaps
- Exact ranges for the 909's shuffle and flam, and the number of positions on the 808's pre-scale switch.
- 505 shuffle and flam (not mentioned in any fetched review).
- 707 flam scope: whether it applies to all voices or only Snare 2 and the toms (sources conflict).

## 4. Built-in effects and default MIDI note maps

### Takeaway
None of the nine machines has built-in effects. The 909, 707/727, 505 and 626 respond to fixed default MIDI notes close to the later General MIDI drum map; the 808, 606, TR-33 and TR-77 have no MIDI.

### Cited Findings
- **Effects.** None are listed in any fetched spec or review. The compressor appears only on Roland's modern Boutique recreations — [Roland TR-08 specs](https://www.roland.com/au/products/tr-08/specifications/); [Roland TR-09 specs](https://www.roland.com/global/products/tr-09/specifications/). One reviewer suggests adding a little short reverb to 727 sounds, which implies it has none — [In Tune, Dec 1985](https://www.muzines.co.uk/articles/roland-tr727-rhythm-composer/5584).
- **TR-909**, citing the TR-909 service notes (Jun 1984, p. 14): BD 35 and 36; RS 37; SD 38 and 40; HC 39; LT 41 and 43; CH 42 and 44; MT 45 and 47; OH 46; HT 48 and 50; Crash 49; Ride 51 — [Zoeblade Roland TR MIDI map](https://notebook.zoeblade.com/Roland_TR_MIDI_map.html). Same list at [JonDent 909](https://djjondent.blogspot.com/2020/04/roland-tr-909-drum-mapping.html).
- **TR-707**, citing the TR-707 manual p. 55 and the service notes: BD1 35; BD2 36; RS 37; SD1 38; HCP 39; SD2 40; LT 41 and 43; CH 42; MT 45 and 47; OH 46; HT 48 and 50; Crash 49; Ride 51; Tamb 54; Cowbell 56 — [Zoeblade](https://notebook.zoeblade.com/Roland_TR_MIDI_map.html). One blog also lists CH on 44, which Zoeblade does not — [JonDent 707](https://djjondent.blogspot.com/2020/05/roland-tr-707-drum-mapping-midi.html).
- **TR-727**, citing the TR-727 manual (Sep 1985, p. 48): 60 Hi Bongo; 61 Low Bongo; 62 Mute Hi Conga; 63 Open Hi Conga; 64 Low Conga; 65 Hi Timbale; 66 Low Timbale; 67 Hi Agogo; 68 Low Agogo; 69 Cabasa; 70 Maracas; 71 Short Whistle; 72 Long Whistle; 73 Quijada; 74 Star Chime — [Zoeblade](https://notebook.zoeblade.com/Roland_TR_MIDI_map.html). A search summary of the manual scan put Star Chime near 76 on p. 46. That scan was garbled, so 73/74 are not fully settled.
- **TR-505**, citing the TR-505 manual (Feb 1986, p. 40): BD 35; RS 37; SD 38; HCP 39; LT 41; CH 42; MT 45; OH 46; HT 48; Crash 49; Ride 51; Hi Conga 62; Low Conga 63; Timbale 65; Hi Cowbell 67; Low Cowbell 68 — [Zoeblade](https://notebook.zoeblade.com/Roland_TR_MIDI_map.html). It transmits and receives on channels 1–16, notes 25–99 — [Wikipedia TR-505](https://en.wikipedia.org/wiki/Roland_TR-505).
- **TR-626**, citing the TR-626 manual (Oct 1987, p. 80): BD1 35; BD2 36; RS 37; SD1 38; HCP 39; SD2 40; LT1 41; CH 42; LT2 43; MT1 45; OH 46; MT2 47; HT1 48; Crash 49; HT2 50; Ride 51; China 52; Cup 53; Tamb 54; Cowbell 56; SD3 58; Mute Hi Conga 62; Open Hi Conga 63; Low Conga 64; Hi Timbale 65; Low Timbale 66; Hi Agogo 67; Low Agogo 68; Shaker 69; Claves 75 — [Zoeblade](https://notebook.zoeblade.com/Roland_TR_MIDI_map.html). Note numbers are user-assignable per voice — [Music Technology, Nov 1987](https://www.muzines.co.uk/articles/roland-tr626/2125).
- **No MIDI:** the 808 — [Music Technology, Nov 1986](https://www.muzines.co.uk/articles/beat-box-chic/983). The 606 has DIN sync instead — [Wikipedia TR-606](https://en.wikipedia.org/wiki/Roland_TR-606).

### Inferences
- **Shared Drum Rack layout:** the four MIDI-era kits line up on GM-style notes (35–51 kit, 54/56 tambourine/cowbell, 60–75 Latin). One Ableton Drum Rack layout can therefore cover the 707, 727, 505 and 626 with almost no collisions.

### Gaps
- No original MIDI implementation chart was read directly; all note maps are second-hand citations of the manuals.

## 5. What each pack folder contains

### Takeaway
Seven of the nine folders hold two parallel one-shot sets: plain-named stereo files and "TR-xxx"-prefixed mono files, the prefixed set being the complete one. The Rhythm 33/77 folders hold one lowercase mono set each. There are no loops and no MIDI anywhere, and only the TR-606 set encodes a setting (accent level) in its file names.

### Cited Findings
Source for this whole section: read-only `ls -R` and `afinfo` on `~/Splice/sounds/packs/<folder>`.
- **Roland TR-808:** 82 WAVs plus 82 Ableton `.asd` files (the only folder with them, so it has been opened in Live before). The plain set is stereo: Bassdrum-01..05, Snaredrum, Clap, Claves, Cowbell, Cabasa, Crash-01/02, Hat Closed/Open, Rimshot, Tom L/M/H (18 files). The "TR-808" set is mono: Kick01-16, Snare01-16, Tom01-07, Conga01-05, Hat_C01-05, Hat_O01-03, Ride01-04, Clap01-02, Rim01-02, Shaker01-02, Clave, Cow (64 files). Kick lengths run from 0.04 s to 2.05 s. No knob values appear in the names.
- **Roland TR-909:** 78 WAVs. The plain set is stereo (14 files) and includes two misspelled files, `Rimhot.wav` and `naredrum.wav`. The "TR-909" set is mono: Kick 01-17, Snare 01-32, Tom Low/Mid/Hi 01-02, Hat C 01-02, Hat O 01-03, Clap, Rim, Crash, Ride (64 files).
- **Roland TR-606:** 55 WAVs plus `Readme.txt`. The plain set is stereo (7 files). The "TR606" set is mono: Kick, Snare, TomLo, TomHi, Cymb, Hat_C, Hat_O and Hat_P, each in versions 01–05 plus `_OD` (48 files). The Readme says the 606's accent adds a subtle overdrive; 01–05 are accent levels from 1 (low) to 5 (high), and `_OD` files are overdriven high-accent hits. "Hat_P" is not a 606 panel voice. Its length (0.33–1.07 s) falls between closed (0.11–0.19 s) and open (1.27–1.86 s).
- **Roland TR-707:** 29 WAVs. The plain set has 14 files and no Ride. The "TR-707" set has all 15 sounds, with "Tamborine" misspelled.
- **Roland TR-727:** 27 WAVs. The plain set has 12 files and lacks Mute Hi Conga, Open Hi Conga and one whistle. The "TR-727" set has all 15: Conga_HiMut, Conga_HiOp, Whistle_S, Whistle_L and so on.
- **Roland TR-505:** 32 WAVs, two complete 16-sound sets.
- **Roland TR-626:** 60 WAVs, two 30-sound sets. The plain set uses Ride-01/02 and Conga H/M/L; the "TR-626" set names Cup, Conga_HiOp and Conga_MutHi explicitly.
- **Rhythm 33:** 7 mono WAVs at 44.1 kHz/16-bit: rhythm33_bd, sn, rim, tom, cow, ch, oh.
- **Rhythm 77:** 9 mono WAVs: rhythm77_bd, sn, rim, conga, high_tom, low_tom, maracas, ch, oh.
- No WAV in either Rhythm folder carries embedded metadata (no INFO chunk names a source).

### Inferences
- **TR-808 file names that don't match the panel:** the 808 has one cymbal voice (CY), so Crash/Ride files are probably CY at different Tone/Decay settings. "Cabasa"/"Shaker" are probably the MA (maracas) voice. Kick01-16 and Snare01-16 are probably Tone/Decay/Snappy sweeps (all inferred).
- **TR-626 plain set:** "Ride-02" is probably the Cup, and "Conga H"/"Conga M" are the open and mute high congas (inferred).
- **TR-606 "Hat_P":** possibly a part-open or "pedal" hat made by the sample creator (unknown).
- **Rhythm 33 = Roland TR-33, Rhythm 77 = Roland TR-77.** Only the names support this: "Rhythm 33" and "Rhythm 77" are Roland's product names — [SoundProgramming TR-33](https://soundprogramming.net/drum-machines/roland/roland-tr-33/); [SoundProgramming TR-77](https://soundprogramming.net/drum-machines/roland/roland-tr-77/). The Rhythm 77 files (bd, sn, rim, conga, maracas, hats) fit the documented TR-77 voice list. The TR-77 has no toms, so "high_tom"/"low_tom" are probably its bongos (inferred). The TR-33 cannot be checked against a voice list.

### Gaps
- No pack documentation exists beyond the 606 Readme, so the knob settings behind the numbered variants are unknown.

## 6. Factory preset patterns

### Takeaway
Real preset patterns exist on the TR-77 (18 named), TR-33 (8 or ~20), TR-505 (48, 9 named) and TR-626 (48, styles only), while the 808 and 606 manuals contain factory or sample patterns; the 909, 707 and 727 have none documented. No step grid could be retrieved for any of them.

### Cited Findings
- **TR-808.** The operation manual has sections titled "The Factory-Programmed Rhythm Patterns" and "Sample Rhythm" (ManualsLib table of contents, seen only in search snippets; the site is bot-gated) — [ManualsLib TR-808 manual](https://www.manualslib.com/manual/695754/Roland-Tr-808.html). Wikipedia names no factory presets — [Wikipedia TR-808](https://en.wikipedia.org/wiki/Roland_TR-808).
- **TR-606.** The manual's contents list "Sample Rhythms" on p. 34 — [all-guidesbox TR-606 manual](https://all-guidesbox.com/manual/1001808/roland-tr-606-owner-s-manual-48.html). Roland's chronicle says the 606 has no presets — [Roland Indonesia chronicle](https://rolandindonesia.com/roland-drum-machine-chronicle-1964-2016/). E&MM mentions no factory patterns — [E&MM, Feb 1982](https://www.muzines.co.uk/articles/roland-tr606/3696).
- **TR-909, TR-707, TR-727.** No presets are mentioned. Wikipedia lists capacity only — [Wikipedia TR-909](https://en.wikipedia.org/wiki/Roland_TR-909); [Wikipedia TR-707](https://en.wikipedia.org/wiki/Roland_TR-707). Reviews mention no demo or preset patterns — [E&MM, Dec 1984](https://www.muzines.co.uk/articles/roland-tr707/8027); [E&MM, Aug 1985](https://www.muzines.co.uk/articles/latin-lessons/9115).
- **TR-505.** 48 ROM presets in groups A–C, plus 48 user patterns in D–F — [Wikipedia TR-505](https://en.wikipedia.org/wiki/Roland_TR-505). The presets cannot be edited — [One Two Testing, May 1986](https://www.muzines.co.uk/articles/roland-tr505/13420). Named presets: A6 "Electric Pop", A8 "16 Beat Rock", C1/C2 "Rock Bossa 1/2", C3/C4 "Samba 1/2", C9/C10 "Bossanova 1/2", C11 "Samba 3". The banks hold 8-beat, 16-beat, disco and samba patterns with matching fills — [Bonedo](https://www.bonedo.de/?p=530195). Roland's spec reads "48 kinds (16 x Pattern Group A to C)" (search snippet). One search summary said 49, which is unverified.
- **TR-626.** 48 presets in three banks of 16: rock, disco, latin and swing, each with fill-ins, plus some funk and reggae — [Music Technology, Nov 1987](https://www.muzines.co.uk/articles/roland-tr626/2125). Sound On Sound confirms 48 presets — [Sound On Sound](https://www.soundonsound.com/reviews/roland-tr626).
- **TR-77.** 18 presets. Basic: Rock'n Roll 1, Rock'n Roll 2, Slow Rock, Ballad, Western, 6/8 March, Jazz Waltz, Waltz. Latin: Rhumba, Beguine, Cha-Cha, Mambo, Samba 1, Samba 2, Bossa Nova, Baion, Bolero, Tango — [Audiofanzine TR-77](https://en.audiofanzine.com/drum-machine/roland/TR-77/editorial/articles/the-roland-tr-77-history-and-features-of-monophonic-and-analog-drum-machines.html). The patterns are hard-wired in a diode matrix. The service manual's timing chart (p. 11) shows the pulses — [Mezzoauto TR-77](https://mezzoauto.blogspot.com/2017/05/roland-rhythm-tr-77-how-it-works.html).
- **TR-33.** 8 preset patterns, unnamed — [SoundProgramming TR-33](https://soundprogramming.net/drum-machines/roland/roland-tr-33/). Another source says "about 20" — [Roland Indonesia chronicle](https://rolandindonesia.com/roland-drum-machine-chronicle-1964-2016/). The two conflict.

### Inferences
- The most reliable route to real preset grids is the original documents: the TR-808 "Sample Rhythm" pages, TR-606 manual pp. 34–42, the TR-77 service-manual timing chart, and the TR-505/626 manual pattern tables. They should be read by a person from a properly obtained copy.

### Gaps
- No preset grid was obtained for any machine. ManualsLib is bot-gated. all-guidesbox serves only 82×123-pixel page thumbnails, and its text layer covers only the first pages. Roland's support pages returned 403.
- Preset names for the remaining 39 TR-505 presets and all 48 TR-626 presets. Names for the TR-33 presets.

## 7. Famous recordings and published step charts

### Takeaway
Verified uses are well documented for the 808 and 909, decent for the 707 and TR-77, artist-level only for the 606, and absent for the 727, 505, 626 and TR-33. No published, text-readable step chart of any of these tracks was found.

### Cited Findings
- **TR-808** (all from [Wikipedia TR-808](https://en.wikipedia.org/wiki/Roland_TR-808), each with a press citation):
  - Ryuichi Sakamoto, *B-2 Unit* / "Riot in Lagos" (1980): introduced the 808 to clubs.
  - Yellow Magic Orchestra, *BGM* (1981).
  - Marvin Gaye, "Sexual Healing" (1982): the first US hit with the 808 (CBC 2008).
  - Afrika Bambaataa & Soulsonic Force, "Planet Rock" (1982; Guardian 2014).
  - Beastie Boys, "Paul Revere" (1986): a reversed 808 recording.
  - Whitney Houston, "I Wanna Dance With Somebody" (1987; BBC 2014).
  - Kanye West, *808s & Heartbreak* (2008): the 808 on every track.
- **TR-909** (all from [Wikipedia TR-909](https://en.wikipedia.org/wiki/Roland_TR-909)):
  - Skinny Puppy, *Remission* (1984).
  - Just-Ice, *Back to the Old School* (1986; Kurtis Mantronik).
  - Adamski, "Killer" (1990).
  - Daft Punk, "Revolution 909" (1997).
  - Björk, "Hunter" (1997; Mark Bell).
  - Radiohead, "Videotape" (2007).
- **TR-707:** INXS "Need You Tonight", Marshall Jefferson "Move Your Body", Mr. Fingers "Washing Machine". The page gives no years; 1987/1986/1986 are from general knowledge — [Wikipedia TR-707](https://en.wikipedia.org/wiki/Roland_TR-707). Roland names INXS, The Jesus and Mary Chain and Stock Aitken Waterman as users, but no tracks — [Roland "Mod Squad"](https://articles.roland.com/mod-squad-a-history-of-tr-707-and-tr-727-modifications/).
- **TR-606:** named users are Sisters of Mercy, OMD, Skinny Puppy, Big Black, Autechre, Aphex Twin, Luke Vibert, Massive Attack and Nine Inch Nails. No specific recordings are named — [Wikipedia TR-606](https://en.wikipedia.org/wiki/Roland_TR-606).
- **TR-77:** George McCrae "Rock Your Baby" (1974), David Bowie "Art Decade" (*Low*, "reportedly" his own TR-77), Ultravox "Hiroshima Mon Amour" (*Ha! Ha! Ha!*), Gary Numan "I Nearly Married a Human" (*Replicas*) — [Audiofanzine TR-77](https://en.audiofanzine.com/drum-machine/roland/TR-77/editorial/articles/the-roland-tr-77-history-and-features-of-monophonic-and-analog-drum-machines.html). Wikipedia confirms only that "Rock Your Baby" used "a drum machine", without naming the model — [Wikipedia, Rock Your Baby](https://en.wikipedia.org/wiki/Rock_Your_Baby).
- **Step charts:** Attack Magazine's "Beat Dissected" index has no entry tied to a Roland TR model — [Attack Beat Dissected index](https://www.attackmagazine.com/technique/beat-dissected/). Its Cybotron "Clear" piece rebuilds the beat with Ableton's 808 Core Kit at 125 BPM and 50% swing. It shows the steps only as screenshots and does not say which machine the original used — [Attack Magazine, Cybotron 'Clear'](https://www.attackmagazine.com/technique/beat-dissected/how-to-make-an-electro-beat-inspired-by-cybotrons-clear/).

### Inferences
- Several of the TR-77 attributions rest on one secondary article; treat them as medium-low confidence.

### Gaps
- No step chart was found for "Sexual Healing", "Planet Rock", "Revolution 909", "Move Your Body" or any other listed track. The web-search budget ran out before MusicRadar, Sound On Sound and Attack track-specific pieces could be searched.
- No TR-727, TR-505, TR-626 or TR-33 recording was verified.

## 8. Free, clearly licensed MIDI pattern files

### Takeaway
None found.

### Cited Findings
- No source found in this session offered machine-specific MIDI pattern files with a stated licence. Searching for them was planned but not possible after the web-search budget was exhausted.

### Inferences
- None.

### Gaps
- The whole question remains open: free MIDI packs for the 808, 909, 707 and others with explicit licences.

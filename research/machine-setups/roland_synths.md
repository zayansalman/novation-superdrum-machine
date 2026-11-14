# Roland synths, sound modules and samplers: drum layouts, effects, pack contents and famous uses (D-110, D-70, JD-990, JD-800, MT-32, S-50, SH-09, System-100)

Conventions used in these notes:
- Roland numbers octaves so that middle C = C4 = MIDI note 60. The D-110 manual prints both forms (for example "C2 (36)", "B1 (35)"), which confirms it ([D-110 Owner's Manual p.102](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)). So C2 = 36 and C7 = 96. The same rule is applied (inferred) to the JD-800, JD-990 and D-70 key ranges.
- "Pack" = the local folder at ~/Splice/sounds/packs/<folder>. Folders were only listed and readme files were read. Nothing was played, moved or changed.
- The web-search budget for this session ran out partway through. Later facts come from fetching known URLs, mostly scanned owner's manuals read page by page. Gaps that more searching might close are marked.

## Q1. What drum sounds does each machine have, and how are they mapped to keys / MIDI notes in the factory rhythm part or drum kit?

### Takeaway
Full factory key maps from primary manuals were found for the **D-110** (63 sounds on notes 35–97) and the **MT-32** (30 sounds on notes 35–75). For the **D-70** the 28 drum samples are known in ROM order, but its factory key map was not found. For the **JD-800** and **JD-990** only the frame is documented: one tone per key from C2 to C7 (notes 36–96). The only known factory key names are C2 = "BassDrum 1" (JD-800) and C2 = "Kick 1" (JD-990, shown in a manual screen example). The **S-50** has no fixed kit; the layout depends on the disk loaded. The **SH-09** and **System-100** make drums by synthesis, and published recipes exist for both.

### Cited Findings

**Roland D-110 (rhythm part). Factory "Initial Rhythm Setting", primary source.** Keys 24–34 and 98–108 are OFF. The sound numbers r01–r63 are the D-110's preset rhythm tones ([D-110 Owner's Manual p.101–102](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).

| Key (MIDI) | Tone | Sound | Key (MIDI) | Tone | Sound |
|---|---|---|---|---|---|
| B1 (35) | r15 | Bass Drum-1 | C5 (72) | r54 | Long Whistle |
| C2 (36) | r16 | Bass Drum-2 | C#5 (73) | r55 | Quijada |
| C#2 (37) | r25 | Rim Shot | D5 (74) | r12 | Cup (Mute) |
| D2 (38) | r19 | Snare Drum-1 | D#5 (75) | r56 | Claves |
| D#2 (39) | r39 | Hand Clap | E5 (76) | r26 | Brush-1 |
| E2 (40) | r20 | Snare Drum-2 | F5 (77) | r27 | Brush-2 |
| F2 (41) | r30 | Low Tom Tom-1 | F#5 (78) | r57 | Castanets |
| F#2 (42) | r01 | Closed High Hat-1 | G5 (79) | r38 | High Pitch Tom Tom-2 |
| G2 (43) | r33 | Low Tom Tom-2 | G#5 (80) | r58 | Triangle |
| G#2 (44) | r04 | Open High Hat-2 | A5 (81) | r37 | High Pitch Tom Tom-1 |
| A2 (45) | r29 | Middle Tom Tom-1 | A#5 (82) | r59 | Wood Block |
| A#2 (46) | r03 | Open High Hat-1 | B5 (83) | r60 | Bell |
| B2 (47) | r32 | Middle Tom Tom-2 | C6 (84) | r17 | Bass Drum-3 |
| C3 (48) | r28 | High Tom Tom-1 | C#6 (85) | r18 | Bass Drum-4 |
| C#3 (49) | r05 | Crash Cymbal | D6 (86) | r22 | Snare Drum-4 |
| D3 (50) | r31 | High Tom Tom-2 | D#6 (87) | r23 | Snare Drum-5 |
| D#3 (51) | r08 | Ride Cymbal | E6 (88) | r24 | Snare Drum-6 |
| E3 (52) | r13 | China Cymbal | F6 (89) | r36 | Low Tom Tom-3 |
| F3 (53) | r11 | Cup | F#6 (90) | r02 | Closed High Hat-2 |
| F#3 (54) | r40 | Tambourine | G6 (91) | r35 | Middle Tom Tom-3 |
| G3 (55) | r14 | Splash Cymbal | G#6 (92) | r06 | Crash Cymbal (Short) |
| G#3 (56) | r41 | Cowbell | A6 (93) | r34 | High Tom Tom-3 |
| A3 (57) | r07 | Crash Cymbal (Mute) | A#6 (94) | r09 | Ride Cymbal (Short) |
| A#3 (58) | r21 | Snare Drum-3 | B6 (95) | r61 | Native Drum-1 |
| B3 (59) | r10 | Ride Cymbal (Mute) | C7 (96) | r62 | Native Drum-2 |
| C4 (60) | r42 | High Bongo | C#7 (97) | r63 | Native Drum-3 |
| C#4 (61) | r43 | Low Bongo | | | |
| D4 (62) | r44 | High Conga (Mute) | | | |
| D#4 (63) | r45 | High Conga | | | |
| E4 (64) | r46 | Low Conga | | | |
| F4 (65) | r47 | High Timbale | | | |
| F#4 (66) | r48 | Low Timbale | | | |
| G4 (67) | r49 | High Agogo | | | |
| G#4 (68) | r50 | Low Agogo | | | |
| A4 (69) | r51 | Cabasa | | | |
| A#4 (70) | r52 | Maracas | | | |
| B4 (71) | r53 | Short Whistle | | | |

- Each of the 63 preset rhythm tones appears exactly once, on contiguous notes 35–97 (checked against the table above). The low keys 35–75 follow the same pattern as the MT-32 / later GM drum map. Keys 76–97 hold the extra sounds: brushes, castanets, alternative kicks/snares/toms, short and muted cymbals, and "Native Drum" 1–3 ([D-110 Owner's Manual p.102](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).
- The rhythm setup covers keys 24–108. Each key can use any of the 63 preset rhythm tones or the 64 user-programmable tones ([D-110 Owner's Manual p.39](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).
- Music Technology's 1988 review describes the rhythm part as "63 percussion sounds" with "four bass drums, six snares, four tom sets", cymbals and Latin percussion. This was seen only as a search excerpt ([Music Technology, Sept 1988, via mu:zines](https://muzines.co.uk/articles/roland-d110/2282)). The manual's r-list matches: r15–r18 kicks, r19–r24 snares, three tom sets plus "High Pitch" toms.

**Roland MT-32 (rhythm part). Factory key list, primary source** ([MT-32 Owner's Manual p.13](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)). Names are as printed:
35 Acou BD · 36 Acou BD · 37 Rim Shot · 38 Acou SD · 39 Hand Clap · 40 Elec SD · 41 Acou Low Tom · 42 Clsd Hi Hat · 43 Acou Low Tom · 44 Open Hi Hat 2 · 45 Acou Mid Tom · 46 Open Hi Hat 1 · 47 Acou Mid Tom · 48 Acou Hi Tom · 49 Crash Cym · 50 Acou Hi Tom · 51 Ride Cym · 52 — · 53 — · 54 Tambourine · 55 — · 56 Cowbell · 57–59 — · 60 High Bongo · 61 Low Bongo · 62 Mt High Conga · 63 High Conga · 64 Low Conga · 65 High Timbale · 66 Low Timbale · 67 High Agogo · 68 Low Agogo · 69 Cabasa · 70 Maracas · 71 Smba Whis S · 72 Smba Whis L · 73 Quijada · 74 — · 75 Claves · 76 —.
- Note that key 44 is a **second open hi-hat** ("Open Hi Hat 2"), not a pedal hat, and 73 is "Quijada", not "Vibraslap" ([MT-32 Owner's Manual p.13](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)). A secondary GM/MT-32 comparison table uses GM-style names for these keys (Pedal Hi-hat, Vibraslap) ([Battle of the Bits Lyceum](https://battleofthebits.com/lyceum/View/Specification+of+General+MIDI+and+Roland+MT-32+patches)). The manual wins.
- The rhythm setup address map covers keys 24–87. Each key's TIMBRE value is 0–93, meaning memory timbres i01–i64 or PCM rhythm sounds r01–r30. So there are **30 PCM rhythm sounds** ([MT-32 Owner's Manual p.12 of MIDI section, "*5-3-1 Rhythm setup"](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)).
- The factory stereo placement is shown as a chart, not numbers ([MT-32 Owner's Manual p.14](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)). Approximate reading (±1 step on a 7>…><…<7 scale):
  - Centre: kick, acoustic snare, cowbell, high timbale.
  - One step right: rim shot, elec SD, all hi-hats, crash.
  - Toms: low tom about 4–5 steps left, mid tom 1 left, high tom about 4 right.
  - Left side: ride about 1 left; tambourine, cabasa and both whistles about 2 left; low conga and quijada about 3 left; claves far left (about 6).
  - Right side: low bongo and maracas about 3 right; high bongo and both agogos about 5 right; low timbale about 2 right.

**Roland D-70 (rhythm part).**
- The rhythm section has 28 percussive samples from the internal "Original Tone" library, which "can be mapped to any note of the keyboard" ([Sound On Sound, July 1990, Richard Lamont, via mu:zines](https://www.muzines.co.uk/articles/roland-d70/7249)).
- The official ROM list is Media I3 "Percussion" ([D-70 Owner's Manual p.186](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)): 1 SNAREDRUM1, 2 SNAREDRUM2, 3 SNAREDRUM3, 4 SNAREDRUM4, 5 SNAREDRUM5, 6 KICK 1, 7 KICK 2, 8 KICK 3, 9 KICK 4, 10 TOM 1, 11 TOM 2, 12 HI-HAT, 13 CHINA CYM, 14 CRASH CYM, 15 RIDE BELL, 16 SIDE STICK, 17 STICKS, 18 CABASA, 19 CLAPS, 20 COWBELL, 21 808 SNARE, 22 808 HI-HAT, 23 808 TOM, 24 ELEC TOM, 25 808 CLAVES, 26 CLICK, 27 AGOGO, 28 ORCH HIT.
- The rhythm setup spans keys **E1–G7** (the D-70's 76 keys). Each key picks an Original Tone by media (I1–3 internal, D1–32, U1–32) and number ([D-70 Owner's Manual p.181](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)).
- Synthmania describes preset patch "78 Drum Kit" as "Solid drum sounds, straight from Roland's own R-8 drum machine of that era" ([Synthmania D-70](https://www.synthmania.com/d-70.htm)). This is a secondary source; the R-8 link is its claim.

**Roland JD-800 (Special Setup).**
- A Special Setup is a Multi-mode function that "a different tone can be assigned to each key of the keyboard (C2—C7)". One setup is stored internally and one on a DATA card ([JD-800 Owner's Manual II p.10](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)). That is 61 keys, notes 36–96 (inferred from Roland numbering).
- The manual's screen examples show the factory internal setup's **C2 key named "BassDrum 1"** ([JD-800 Owner's Manual II p.II-15 to II-23](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- The JD-800's 108 internal waveforms contain **no dedicated kick, snare or hi-hat samples** ([JD-800 Owner's Manual II p.V-34 to V-36](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)). The percussion-relevant waves are:
  - 046 Kalimba, 047 Xylo, 048 Marim Wave, 049 Log Drum, 050 AgogoBells, 051 Bottle Hit, 052–054 Gamelan 1–3, 055 Tabla, 056 Pole lp.
  - One-shots 075–091: 077 Wood Crak, 078 Kimba Atk, 079 Block, 082 Cowbell, 083 Sm Metal, 084 StrikePole, 086 Switch, 087 Tuba Slap, 088 Plink, 089 Plunk, 091 "TVF_Trig" ("an impulse-type sound usable as a trigger").
  - Noises 098 WhiteNoise, 099 Pink Noise, 100–106 wind/noise loops, plus 107 Anklungs and 108 Wind Chime.
- **Dance card (SL-JD80-02, "Drums & Percussion DANCE").** It is a pair: an SO-JD80-02 waveform card and a PN-JD80-02 data card. It holds 56 one-shot drum waves and 64 patches (A11–A88) ([Polynominal SL-JD80-02](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/SL-JD80-02.htm); [soundprogramming.net SL-JD80 list](https://soundprogramming.net/synthesizers/roland/roland-sl-jd80-expansion-cards)). The wave list, in card order:
  - 01–11 kicks: 808 K Shrt, 808 K Long, 909 Kick, Smash Kick, Bryt Kick, Tekno Kick, Industry K, Mach Kick, Butt Kick, Gate Kick, Mondo Kick.
  - 12 808 Rim.
  - 13–27 snares: 808 SN, 909 SN, CR78 SN, Attack SN, Splat SN, 90's SN, Dance Sn1, Dance SN 2, Hip Hop SN, Video SN, Rap SN, House SN, Swing SN, Combo SN, Disco SN.
  - 28–36 toms: 606 Tom 1, 606 Tom 2, Boosh Tom, Blast Tom, E Tom, Rim Tom 1–4.
  - 37–38 808 CHH 1, 808 CHH 2.
  - 39–56 percussion: Whistle, Cowbell 2, Block 2, Maraca, Cabasa Up, CabasaDown, Tambourin, Slap Cga, Mute Cga 1, Mute Cga 2, Hi Conga, Lo Conga, Hi Bongo, Lo Bongo, Timabale [sic], then 54–56 printed run-together as "Chekere 55- snapes 56tamburi" ([Polynominal SL-JD80-02](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/SL-JD80-02.htm)).
- The full SL-JD80 series is: 01 Drums & Percussion STANDARD, 02 Drums & Percussion DANCE, 03 Rock Drums, 04 Strings Ensemble, 05 Brass Section, 06 Grand Piano, 07 Guitar Collection, 08 Accordion ([Polynominal JD-800 page](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/index.html)).

**Roland JD-990 (Rhythm Set).**
- "Each note on the keyboard corresponds to a different percussion sound… composed of one Tone (Tone A) only". The diagram runs Note C2 to Note C7 ([JD-990 Owner's Manual p.Base-8](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).
- Memory holds one rhythm set each in Preset A, Preset B, Internal and Card ([JD-990 Owner's Manual p.Base-9](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).
- The manual's screen examples show **C2 named "Kick 1"** ([JD-990 Owner's Manual p.Ryth-11, Ryth-14](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).
- The internal waveform list has 195 waves; waves 1–108 match the JD-800 list. Dedicated drum waves ([Roland JD-990 Waveform List, via Polynominal](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/PCM-list.jpg)):
  - 157 Solid Kick, 158 Room Kick, 159 808 K Long.
  - 160 Hard SN, 161 808 SN, 162 90's SN, 163 Bigshot SN, 164 Power SN.
  - 165 Power Tom.
  - 166 Closed HH1, 167 Closed HH2, 168 Open HH, 169 Crash Cym, 170 Ride Cym.
  - 171 808 Claps, 172 Maraca, 173 Cabasa Up, 174 CabasaDown, 175 Slap Cga, 176 Mute Cga 1, 177 Mute Cga 2, 178 Hi Conga, 179 Lo Conga, 180 Snaps, 181 Tambourine, 182 Cowbell 2.
  - Also 149 Vibes, 150 Steel Drums, 154 Rattles.
- The JD-990 can also play SO-JD80 waveform cards. Roland notes that "Some Waveforms on certain PCM Cards may already be contained in the JD-990's memory" ([JD-990 Owner's Manual p.Base-10](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).

**Roland S-50 (sampler).**
- There is no fixed kit. "Samples can be placed anywhere across the full MIDI range (0–127)", so a drum machine or sequencer can trigger them ([Music Technology, Dec 1986, Paul Wiffen, via mu:zines](https://www.muzines.co.uk/articles/roland-s50/203)).
- Five disks shipped with the machine: piano, strings/choir, brass/bass/tuned percussion, **a drum disk** ("a wide variety of acoustic, electronic and gated drums" in "various useful combinations") and an effects disk. The reviewer's main complaint was a crash cymbal "starved of memory and bandwidth" ([Music Technology, Dec 1986](https://www.muzines.co.uk/articles/roland-s50/203)).
- A 1986 Sound On Sound review says a disk offers 18 drum and percussion sounds arranged in kits that mix acoustic and electronic sounds. This was seen as a search excerpt only ([Sound On Sound 1986, via mu:zines](https://www.muzines.co.uk/articles/roland-s-50-sampling-keyboard/1443)).

**Roland SH-09 (analog monosynth; drums by synthesis).** The owner's manual includes three factory sound charts for drums ([SH-09 Owner's Manual p.29–30](https://static.roland.com/assets/media/pdf/SH-09_OM.pdf)):
- **"Synth Drum"**: different keys give different pitches. Play rhythms and short rolls; Gate+Trigger envelope mode allows fast playing.
- **"Inverted Synth Drum"**: same idea with the inverted filter envelope. Raising VCF MOD to "7" gives a delayed special effect.
- **"Bass Drum"**: strike a key in the middle of the keyboard; different keys change the sound. The manual suggests triggering it from a Roland CR rhythm unit or a Boss DR-55 trigger output plugged into the SH-09's Gate input, to add "a custom drum".
- The slider positions are printed as small panel pictures. They are not legible at the resolution read here.

**Roland System-100 (semi-modular; drums by synthesis).** Bonedo's patch walkthrough ([Bonedo, 09.02.2023](https://www.bonedo.de/artikel/vintage-synth-roland-system-100)):
- **Kick and snare**: pink noise through a strongly resonant filter. Sequence row B sets the filter pitch and a very short filter envelope adds a click at note start; row A gates the hits. Reverb comes in from bar 3.
- **Hi-hat**: two VCOs through the ring modulator plus some noise. VCO2 is driven by random S&H values, and the S&H clock sets the kick/snare tempo.
- **Tom**: an envelope-modulated triangle-wave VCO, played by hand.
- **"Whistling" percussion**: the snare patch with a different envelope.

### Inferences
- On the D-110, MT-32 and D-70, kit slots are separate sound choices per key. On the JD-800/JD-990, every key is a full synth tone (WG/TVF/TVA with envelopes and LFOs). A faithful Drum Rack for the JD machines should treat each pad as a lightly processed one-shot, not a static sample.
- The JD-800's factory drum kit must be built from the non-drum waves listed above (TVF_Trig, noises, Block, Wood Crak, Cowbell, Sm Metal, StrikePole and so on). That is why the factory C2 is a programmed "BassDrum 1" rather than a sampled kick. This is inferred from the waveform list.
- For an Ableton layout, the D-110 and MT-32 maps can be used verbatim. Pads at notes 35–51 line up with GM (with the MT-32's key 44 being an open hat, not a pedal hat).

### Gaps
- **D-70 factory rhythm key map**: not found. The manual's "Initialize Data" section covers Performance, Patch and Tone, but no factory rhythm map was located in the pages read.
- **JD-800 factory internal Special Setup (61 key names)** and the **Dance card's PN-JD80-02 Special Setup key map**: not found online, apart from C2 = BassDrum 1. The Owner's Manual I (User's Guide) and the card leaflet were not available.
- **JD-990 Preset A/B rhythm set key lists**: not found, apart from the C2 "Kick 1" screen example.
- **S-50 factory drum-disk key layout and sample names**: not found.
- SH-09 slider values for the three drum charts could not be read reliably from the scan.

## Q2. Which sounds cut each other off (exclusive / mute groups such as closed/pedal/open hi-hat)?

### Takeaway
Only the JD-800, JD-990 and D-70 have a choke mechanism, and their factory assignments are unknown. The D-110 and MT-32 rhythm setups have no mute or exclusive parameter. The SH-09 is monophonic, so every note cuts the last. On the System-100, the published kick/snare recipe uses one voice, so those two cut each other.

### Cited Findings
- **JD-800**: per-key "Mute group" with values OFF or A–H. Keys in a group play with last-note priority, so a new note mutes any sounding note in the same group. The manual's example puts open and closed hi-hats in one group, and also Latin pairs such as open/mute low conga, cowbells and cuica ([JD-800 Owner's Manual II p.II-17](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- **JD-990**: per-key "Mute Group" OFF or A–Z (26 groups). The manual's hint is to put all hi-hats in one group; it is also handy for some Latin percussion ([JD-990 Owner's Manual p.Ryth-12](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).
- **D-70**: each rhythm key has a "Mute" parameter whose value is another key (E1–G7) or Off ([D-70 Owner's Manual p.181](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)).
- **D-110**: rhythm setup parameters per key are only Tone, Level, Pan and Output Assign ([D-110 Owner's Manual p.39](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).
- **MT-32**: rhythm setup parameters per key are only Timbre, Output Level, Panpot and Reverb Switch ([MT-32 Owner's Manual, MIDI section "*5-3-1"](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)).
- **System-100**: in Bonedo's recipe, kick and snare come from the same noise-plus-resonant-filter voice, pitched by sequencer row B ([Bonedo 2023](https://www.bonedo.de/artikel/vintage-synth-roland-system-100)).
- **SH-09**: it is a single-VCO lead synthesizer with one envelope and one VCA ([SH-09 Owner's Manual p.1–6](https://static.roland.com/assets/media/pdf/SH-09_OM.pdf)).

### Inferences
- D-70: the "Mute" value names the key that gets cut. This is how the parameter list reads, but the exact direction of the mute was not confirmed in the prose.
- D-110 and MT-32: no hi-hat choke on the hardware, inferred from the absence of any such parameter. For authenticity, leave the Drum Rack hats unchoked. A choke group is still a sensible option for usability.
- JD-800/JD-990: the factory kits very likely put hats in a mute group, given the manuals' own advice. Not verified.
- System-100: put the kick and snare pads in one choke group to mimic the single shared voice.

### Gaps
- Factory mute-group assignments for the JD-800, JD-990 and D-70 kits are unknown.
- The S-50 has no documented exclusive or mute-group feature. The Wiffen review lists per-sample tuning, vibrato and envelope but no grouping, so this is unknown rather than confirmed absent.

## Q3. What per-sound parameters exist, what built-in effects exist, and do the drums go through them?

### Takeaway
All five ROM/PCM machines (D-110, MT-32, D-70, JD-800, JD-990) have built-in reverb, and the drums can go through it. The routing is per key on the MT-32 (reverb on/off), D-70 (Reverb/Chorus/Dry/Direct), JD-800 (DRY/REV/CHO+REV/DLY+REV plus level) and JD-990 (EQ:MIX/EQ+R/EQ+C+R/EQ+D+R or DIR1–3 plus send level). On the D-110 it depends on which output the key uses. The S-50 and SH-09 have no effects. The System-100's Model 103 mixer has a spring reverb.

### Cited Findings
**D-110**
- Per key: Tone (preset rhythm r01–r63 or programmable i01–i64), Level, Pan, Output Assign. Keys 24–108 ([D-110 Owner's Manual p.39](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).
- Pan runs 7> to <7. In the rhythm part pan is set per key, so there is no part-wide pan ([p.69](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)). The part has an output level of 0–100, and key range cannot be set for the rhythm part ([p.69–70](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).
- Reverb is set per patch: Small Room, Medium Room, Medium Hall, Large Hall, Plate, Delay 1, Delay 2, Delay 3, or OFF. Reverb Time 1–8, Level 0–7 ([p.41](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).
- Output Assign is MIX or one of six multi outs. "The Timbres sent through the Direct Output Sockets do not take on reverb effects", and with reverb on, Multi Outputs 5 and 6 cannot be used ([p.44](https://static.roland.com/assets/media/pdf/D-110_OM.pdf); outputs on [p.5](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)).

**MT-32**
- Per rhythm key: Timbre (i01–i64 or r01–r30), Output Level 0–100, Panpot 0–14 (printed "R – L"), Reverb Switch OFF/ON.
- System reverb: mode Room, Hall, Plate or Tap delay; time 1–8; level 0–7 ([MT-32 Owner's Manual, MIDI implementation "*5-3-1" and "*5-5"](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)).

**D-70**
- Rhythm Common: Rhythm Shift −28 to +24 semitones.
- Per key (E1–G7):
  - Source: Original Tone media and number, Source Key, Mute (key or Off), Output Assign (Reverb, Chorus, Dry, Direct), Pan (7>–<7), ENV mode (Sus / No Sus).
  - Pitch: coarse ±12 semitones, fine −64 to +63, pitch-envelope attack time and depth.
  - TVF: LPF, HPF, BPF or Bypass, with cutoff, resonance, velocity curve, envelope depth, envelope-depth velocity and a 7-stage envelope.
  - TVA: level, velocity curve, velocity sensitivity and a 7-stage envelope ([D-70 Owner's Manual p.181](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)).
- Effects: default Reverb type "Hall 2" (time, level, feedback) and Chorus "Chorus 1" with out mode "Pre Reverb" ([p.183](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)).
- Reviews: "13 24-bit digital reverb, chorus and delay effects" with "both dry and effected stereo outs" ([Music Technology, June 1990, Simon Trask](https://www.muzines.co.uk/articles/roland-d70/383)). Each drum sound can be panned and given its own output destination ([Sound On Sound, July 1990](https://www.muzines.co.uk/articles/roland-d70/7249)).

**JD-800 Special Setup**
- Per key, eight parameter areas: Key name (10 characters), Mute group, Envelope mode (SUSTAIN / NO SUSTAIN), Pan (L30–00–30R), Effect mode (DRY, REV, CHO+REV, DLY+REV), Effect level (0–100), and a full Tone edit (WG, pitch envelope, TVF, TVF envelope, TVA, TVA envelope, LFO 1/2) ([JD-800 Owner's Manual II p.II-15 to II-23](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- Common setup: bender range, aftertouch bend sensitivity, plus an EQ setup ([p.II-14](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- The Special Part ignores MIDI pan. Effect mode and level can only be set per key, not for the whole part ([p.II-12, II-13, II-20 to II-22](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- The part's Output Assign is MIX or DIR. With DIR, "the internal effects will not be applied" ([p.II-11](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- Multi-mode effects are chorus, delay and reverb ([TOC, p.II-31 to II-34](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).
- For rhythm sounds the manual advises NO SUSTAIN, so notes play a fixed length whatever the gate time ([p.II-19](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)).

**JD-990 Rhythm Set**
- Common: Rhythm Set Level 0–100, Pan L50–50R, Analog Feel 0–100, Bend Range down 0–48 and up 0–12, Tone Ctrl Src 1/2, and EQ ([JD-990 Owner's Manual p.Ryth-8, Ryth-9](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).
- Per key: Key WG, TVF and TVA as in a patch, but with no sync slave switch ([p.Ryth-10](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)). Key CTRL: name, velocity curve 1–7, Mute Group, Envelope Mode (SUSTAIN / NO-SUS), Hold Control switch, LFO1/LFO2, Control 1 & 2 ([p.Ryth-11 to Ryth-13](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).
- Out & FX send per key: EQ:MIX, EQ+R:MIX, EQ+C+R:MIX, EQ+D+R:MIX, DIR1, DIR2 or DIR3, with FX Send Level 0–100. The rhythm set's effects are chorus, delay and reverb ([p.Ryth-14, Ryth-15](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)).

**S-50**
- 16 voices (8 when two sounds share a note), 12-bit at 30 or 15 kHz.
- Per sample: tuning, vibrato and an eight-stage envelope. Filtering is static, with no filter envelope.
- The audio input can trigger up to eight keys.
- No reverb or delay is mentioned ([Music Technology, Dec 1986](https://www.muzines.co.uk/articles/roland-s50/203)).

**SH-09** ([SH-09 Owner's Manual p.1–6](https://static.roland.com/assets/media/pdf/SH-09_OM.pdf))
- VCO: Noise, Sawtooth, Square or Pulse (with PWM), range 32'–2'.
- Sub-oscillator and a three-way audio mixer.
- 24 dB/oct low-pass VCF with cutoff and resonance. Resonance self-oscillates near the top so the VCF "becomes a separate sine wave audio oscillator". Envelope mode is positive, inverted or envelope follower, with ENV depth 0–10 and MOD.
- VCA mode: HOLD, ENV or GATE.
- ADSR envelope triggered by Gate+Trigger, Gate, or LFO.
- LFO 0.2–25 Hz: sine (with delay), square, or S&H.
- The manual's design pyramid lists reverb as an *external* effect.

**System-100**
- 101/102 VCO waves: triangle, saw, square and variable pulse. The 101 adds noise and "Autoglide"; the 102 adds ring mod and S&H.
- VCF: 24 dB/oct LPF plus a fixed 6 dB/oct HPF. ADSR envelope, LFO.
- 103 mixer: spring reverb via a per-channel send.
- 104 sequencer: 2×12 knobs, 1–24 steps, tempo and gate length ([Bonedo 2023](https://www.bonedo.de/artikel/vintage-synth-roland-system-100); [Wikipedia: Roland System 100](https://en.wikipedia.org/wiki/Roland_System_100)).

### Inferences
- Ableton mapping:
  - D-110: one Reverb return; Drum Rack pads on "MIX" are sent and pads on multi outs are dry.
  - MT-32: a per-pad on/off send.
  - D-70: per-pad routing to Reverb, Chorus→Reverb or Dry.
  - JD-800/990: per-pad send amount into Reverb / Chorus+Reverb / Delay+Reverb returns.
  - System-100: a spring-reverb return.
- Per-pad Simpler/Drum Sampler controls that match the hardware:
  - D-110: level and pan.
  - MT-32: level, pan and reverb send.
  - D-70 and JD: level, pan, pitch, filter type/cutoff/resonance, amp and filter envelopes, and velocity curve.

### Gaps
- Default factory reverb/chorus settings for the D-110 and MT-32 rhythm parts, and the per-key reverb-switch defaults, were not checked.
- The D-70's full list of reverb/chorus types was not captured (only the defaults).

## Q4. Total drum sounds and categories, with the official ordered list

### Takeaway
D-110: 63 rhythm tones r01–r63, built from about 30 raw rhythm PCM samples. MT-32: 30 PCM rhythm sounds r01–r30. D-70: 28 percussion Original Tones. JD-990: 26 dedicated drum/percussion waves (157–182) among 195. JD-800: 0 dedicated drum samples internally (percussive and one-shot waves only); the Dance card adds 56. S-50: depends on disk. SH-09 and System-100: none (synthesis).

### Cited Findings
- **D-110 preset rhythm tones in official order** ([D-110 Owner's Manual p.101](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)):
  - r01 Closed High Hat-1, r02 Closed High Hat-2, r03 Open High Hat-1, r04 Open High Hat-2.
  - r05 Crash Cymbal, r06 Crash Cymbal (Short), r07 Crash Cymbal (Mute), r08 Ride Cymbal, r09 Ride Cymbal (Short), r10 Ride Cymbal (Mute), r11 Cup, r12 Cup (Mute), r13 China Cymbal, r14 Splash Cymbal.
  - r15–r18 Bass Drum-1 to -4.
  - r19–r24 Snare Drum-1 to -6, r25 Rim Shot, r26–r27 Brush-1/-2.
  - r28 High Tom Tom-1, r29 Middle Tom Tom-1, r30 Low Tom Tom-1, r31–r33 High/Middle/Low Tom Tom-2, r34–r36 High/Middle/Low Tom Tom-3, r37–r38 High Pitch Tom Tom-1/-2.
  - r39 Hand Clap, r40 Tambourine, r41 Cowbell, r42–r43 High/Low Bongo, r44 High Conga (Mute), r45 High Conga, r46 Low Conga, r47–r48 High/Low Timbale, r49–r50 High/Low Agogo, r51 Cabasa, r52 Maracas, r53 Short Whistle, r54 Long Whistle, r55 Quijada, r56 Claves, r57 Castanets, r58 Triangle, r59 Wood Block, r60 Bell.
  - r61–r63 Native Drum-1 to -3.
  - The table also gives partials per tone (1–3).
- **D-110 raw rhythm PCM** (Bank 1, 001–030, "Rhythm Sound"): Bass Drum-1 to -3, Snare Drum-1 to -4, Tom Tom-1/-2, High-Hat, High-Hat (Loop), Crash Cymbal-1, Crash Cymbal-2 (Loop), Ride Cymbal-1, Ride Cymbal-2 (Loop), Cup, China Cymbal-1, China Cymbal-2 (Loop), Rim Shot, Hand Clap, Mute High Conga, Conga, Bongo, Cowbell, Tambourine, Agogo, Claves, Timbale High, Timbale Low, Cabasa ([D-110 Owner's Manual p.103](https://static.roland.com/assets/media/pdf/D-110_OM.pdf)). So the 63 tones are re-pitched and re-enveloped versions of these samples.
- **MT-32**: 30 rhythm PCM sounds, r01–r30 ([MT-32 Owner's Manual MIDI section](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf)). The full r01–r30 ROM order was not printed in the pages read. The key list in Q1 holds the 30 distinct names.
- **D-70**: Media I3 "Percussion", 28 entries, listed in Q1 ([D-70 Owner's Manual p.186](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)). By category:
  - Snares 5 (1–5), kicks 4 (6–9), toms 2 (10–11).
  - Hi-hat 1 (12), cymbals 3 (13–15), side stick/sticks 2 (16–17).
  - Percussion 3 (18–20).
  - "808" and electronic 5 (21–25), click 1, agogo 1, orchestra hit 1.
- **JD-990**: 195 waves in total ([JD-990 Owner's Manual p.Intr-6](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/roland-jd990-manual.pdf)); the dedicated drum waves are 157–182 ([JD-990 Waveform List](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/PCM-list.jpg)).
- **JD-800**: 108 waves, grouped as ([Polynominal JD-800](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/index.html)):
  - Analog synth 1–13, digital synth 14–35, realistic sustain 36–45.
  - Percussive 46–61, enhanced overtones 62–70, piano 71–74.
  - Fast attack/one-shot 75–91, wind 92–97, noise 98–106, special FX 107–108.

### Inferences
- The D-110 has three hi-hat "articulations" built from one hi-hat sample: closed via envelope, open, and open-2. That is why the D-110's hats in the pack may sound related.
- The D-70 has only one HI-HAT Original Tone. The pack's separate "Hat Closed" and "Hat Open" were most likely made from that one sample with different TVA envelopes.

### Gaps
- MT-32 r01–r30 ROM order not captured.
- S-50 factory drum disk sound list not found.

## Q5. What does each pack folder contain? (read-only `ls -R`)

### Takeaway
Packs that use names map cleanly onto the manuals: the D-110 (18 files), D-70 (20), MT-32 (30 = every MT-32 rhythm sound), S-50 (43, in four subfolders) and JD-990 (62 truncated wave names). The two JD-800 packs are number-only (46 and 61 files) and come with a readme admitting the sound names are unknown. The SH-09 packs are kick-only, and the second has a 1997 "free of copyright" readme. The System-100 pack (62) is synthesized drums and is missing Snaredrum-13.

### Cited Findings (from the local listing; file names quoted)

**Roland D-110 (18 files)**
- Files: Bassdrum, Bongo, Cabasa, Conga, Cowbell H, Cowbell L, Crash, Hat Closed, Hat Open, Hat Pedal, Ride, Rimshot, Snaredrum-01..03, Tambourine, Tom, Woodblock.
- Inferred matches to the [D-110 tone list](https://static.roland.com/assets/media/pdf/D-110_OM.pdf):
  - Hat Closed = r01 (42); Hat Open = r03 (46); Crash = r05 (49); Ride = r08 (51); Rimshot = r25 (37); Tambourine = r40 (54); Cabasa = r51 (69); Woodblock = r59 (82).
  - **Hat Pedal**: the D-110 has no pedal hat, so this is probably key 44 = r04 "Open High Hat-2", the GM pedal-hat slot.
  - **Cowbell H/L**: the D-110 has a single Cowbell (r41), so these are probably High/Low Agogo (r49/r50, keys 67/68). Low confidence.
  - Bassdrum, Tom, Bongo, Conga and the three snares cannot be pinned to specific r-numbers.
- Only about 18 of the 63 tones are present.

**Roland D-70 (20 files)**
- Files: Bassdrum-01..04, Cabasa, Clap, Cowbell, Crash, Hat Closed, Hat Open, Ride, Rim Shot, Snaredrum-01..05, Sticks, Tom-02, "Tom.-01" (stray dot in the name).
- Inferred matches to the [D-70 I3 list](https://static.roland.com/assets/media/pdf/D-70_OM.pdf):
  - KICK 1–4, SNAREDRUM1–5, TOM 1–2, CRASH CYM, RIDE BELL (= "Ride"), SIDE STICK (= "Rim Shot"), STICKS, CABASA, CLAPS, COWBELL.
  - HI-HAT appears as two envelopes (closed and open).
- Absent: CHINA CYM, 808 SNARE, 808 HI-HAT, 808 TOM, ELEC TOM, 808 CLAVES, CLICK, AGOGO, ORCH HIT.

**Roland MT-32 (30 files)**
- Files: Agogo H/L, Bassdrum, Bongo H/L, Cabasa, Clap, Claves, Conga H/L, Conga Muted H, Cowbell, Crash, Hat Closed, Hat Open-01/-02, Maracas, Quijada, Ride, RimShot, Snaredrum-01/-02, Tambourine, Timbale H/L, Tom H/M/L, Whistle Short, Whistle.
- That is exactly the 30 distinct rhythm sounds on the [MT-32 key list](https://www.polynominal.com/roland-mt-32/roland-mt32-manual.pdf).
- Inferred matches: Snaredrum-01 = Acou SD (38), Snaredrum-02 = Elec SD (40), Hat Open-01 = Open Hi Hat 1 (46), Hat Open-02 = Open Hi Hat 2 (44), Whistle = Smba Whis L (72).

**Roland JD-990 (62 files)**: 8-character truncated names. Matched against the [JD-990 internal list](https://www.polynominal.com/site/studio/gear/synth/roland_jd990/PCM-list.jpg) and the [SL-JD80-02 Dance card list](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/SL-JD80-02.htm):

| Group | Files → wave name (source) |
|---|---|
| JD-990 internal drums | Solid-k → Solid Kick (157); Room-kck → Room Kick (158); Hard-sd → Hard SN (160); Bigshots → Bigshot SN (163); Power_sd → Power SN (164); Power_tm → Power Tom (165); Ohh → Open HH (168); Crsh-cym → Crash Cym (169); Ride_cym → Ride Cym (170); Vibes (149); Rattles (154) |
| JD-800/990 shared percussive waves | Kalimba (46), Xylo (47), Marimwav → Marim Wave (48), Agogo_bl → AgogoBells (50), Bottlhit → Bottle Hit (51), Gamelan (52–54, which one unknown), Crystal (62), Digibels → Digi Bell (63), Fingbell → FingerBell (64), Digichim → Digi Chime (65), Org_bell → Org Bell (67), Woodcrak → Wood Crak (77), Cowbell (82, or Cowbell 2), Sm_metal → Sm Metal (83), Plink (88), Plunk (89) |
| Dance card (SO-JD80-02) only | Smash-k (04), Bryt-kck (05), Tekno-k (06), Indstr-k → Industry K (07), Mach-kck (08), Butt-kck (09), Gate-kck (10), Mondo-k (11), Attack_s → Attack SN (16), Splat-sd (17), Dance-s1 (19), Dance-s2 (20), Hiphop-s (21), Video-sd (22), Rap-sd (23), House-sd (24), Swing-sd (25), Combo-sd (26), Disco-sd (27), Boosh-tm (30), Blast-tm (31), E-tom (32), Rim-tom1..4 (33–36) |
| In both lists (ambiguous source) | 90's-sd (int. 162 / card 18), Snaps (int. 180 / card 55), Tambourn (int. 181 / card 45), Chh_1, Chh_2 (Closed HH1/2 166/167 or 808 CHH 1/2 card 37/38) |
| No matching wave name | Dance-cl, Lite-ch1, Lite-ch2, Lite-ohh |

- Every wave whose name contains a machine model is absent (808/909/606/CR78), as are the card's and the internal Latin percussion.

**Roland JD800 (47 files)**: "JD800 Internal Drums 001.wav" to "046.wav", plus a readme.txt that says the uploader no longer owns the machine or its manuals "and don't have a list of the sound names".

**Roland JD800 Dance Card (62 files)**: "JD800 Dance Card Drums 001.wav" to "061.wav", plus the same readme text.

**Roland S50 (43 files in four subfolders)**
- Bassdrums: Bassdrum-01..04.
- Cymbals: China, Crash, Gong, Hihat, Ride.
- "Percusson" (sic, 31 files): Agogo-01/02, Bongo, Cabasa-01/02, Clap, Claves-01/02, Conga-01..03, Cowbell, Cuica-01/02, "Cuical-01/02", Maracas-01/02, "Qijada" (sic), Tambourine-01/02, Timbale H/L, Tom-01..04, Tria-1/2, Wblk, Whstl.
- Snaredrums: Snaredrum-01..03.
- Possible source disks: Roland's S-50/S-550 library includes L-503 #11 "Latin Percussion #1", L-509 #44/#45 "Latin Percussion #2/#3", L-552 #10 "Classic Percussions", USB-503 #6 "Timbales & Toms", #7 "Assorted Kicks #1", #8 "Assorted Snares #1", USB-503 #3 "Assorted Cymbals #1" and #9 "Ethnic & Gongs #1", and S-50 System #4 "Effect Drum Parts" ([Llama Music L-CD1 list](https://llamamusic.com/s50s550/Roland_L-CD1_List.html)). Roland later posted these library disk images online ([Roland Sound Bank notice](https://www.sgroup.ca/archive/samples/Roland/ReadMes/soundbnk.txt)).

**Roland SH-09 (43 files)**: Bassdrum-01..43, kicks only, no readme.

**SH09 Drum sounds (37 files)**
- 909bass1–12 (12), lowbass1–13 (13), lowbass_long, lowbass_long2–4 (4), stompbass1–7 (7), plus readme.txt.
- The readme says the samples are a "Bass drum pack" made on an SH-09, recorded 16-bit 44.1 kHz mono "directly from the synth without any modifications or effects". It also says "All samples are free of copyright. You may use them as you like." Signed Björn Fogelberg, Ängelholm, Sweden, 19 Dec 1997.

**Roland System-100 (62 files)**
- Bassdrum-01..15, Bell, Click-01..06, Hat Closed-01/02, Hat Open-01..03, Pling-01..03, Plopp-01..09, Tock, Triangle.
- Snaredrum-01..22 **with Snaredrum-13 missing** (21 snares).

### Inferences
- The D-110, D-70, MT-32, S-50, SH-09 and System-100 packs share a naming style ("Bassdrum-01", "Hat Closed", "Snaredrum-01"). This suggests one curator. Not verified, because web search ran out before the source could be traced.
- **JD-800 Dance Card**: 61 files = the 61 keys C2–C7 of a Special Setup. The numbered files are most likely the Dance card data card's Special Setup sampled key by key from C2 (001) to C7 (061). Only 56 waves exist on the card, so 5 or more keys reuse waves or use internal waves. Inferred, not verified.
- **JD-800 Internal**: 46 files from a 61-key Special Setup suggests some keys were skipped or duplicates dropped. Their mapping cannot be recovered without the factory key list.
- The JD-990 pack mixes JD-990 internal waves with Dance-card waves. That implies it was sampled from a JD-990 with an SO-JD80-02 card fitted. "Lite-ch1/2", "Lite-ohh" and "Dance-cl" are probably rhythm-set key names (programmed tones) rather than raw waves.
- The S-50 percussion set (cuica, quijada, whistle, agogo, timbales, congas) fits Roland's "Latin Percussion" library disks better than the general factory drum disk. Low confidence.

### Gaps
- No provenance or licence is documented for the D-110, D-70, JD-990, JD-800, MT-32, S-50, SH-09 (43) and System-100 packs. Only the SH09 Drum sounds readme states terms.
- Which JD-800 numbered file is which sound remains unknown.

## Q6. Factory rhythm patterns, and famous recordings that verifiably used each machine's drum sounds (with published step charts)

### Takeaway
None of these eight machines has factory rhythm patterns. The JD-800 and D-70 have demo songs (ROM Play), not drum patterns, and the System-100's Model 104 is an empty step sequencer. The only drum use that is reasonably well documented is the Human League's "Being Boiled", with its beat programmed on a System-100 sequencer. For the MT-32, its game soundtracks are the famous use. **No published step chart was found for any of these recordings.** Every grid is therefore null; none was reconstructed.

### Cited Findings
- **Demo songs, not patterns**: the JD-800's appendix lists "ROM PLAY" ([JD-800 Owner's Manual II TOC, p.V-28](https://www.polynominal.com/site/studio/gear/synth/roland_jd800/roland-jd800-manual.pdf)). The D-70 has a "ROM Play mode" that "allows you to hear the demo song built into the D-70" ([D-70 Owner's Manual p.4](https://static.roland.com/assets/media/pdf/D-70_OM.pdf)). The D-70 "had no sequencer" ([Wolf Architects retro review](https://review.wolfarchitects.design/roland-d-70-synthesizer-1990/), search excerpt).
- **System-100 sequencer**: the Model 104 is "two-channel, 12-step" ([Wikipedia](https://en.wikipedia.org/wiki/Roland_System_100)), with step count adjustable 1–24 and no stored patterns ([Bonedo 2023](https://www.bonedo.de/artikel/vintage-synth-roland-system-100)).
- **Human League, "Being Boiled"** (original recording c.1978, per photo captions and video title cited in [Bonedo 2009](https://www.bonedo.de/artikel/human-league-being-boiled-und-das-roland-system-100)):
  - Martyn Ware used the 104 sequencer's speed control, via one knob row, to set different note lengths "for the beat programming of 'Being Boiled'" ([Bonedo 2023](https://www.bonedo.de/artikel/vintage-synth-roland-system-100)).
  - The 2009 Bonedo piece stresses there was no drum machine. The rig was a fully expanded System-100 (101, 102, sequencer, mixer) plus a Korg 700S for the bass ([Bonedo 2009](https://www.bonedo.de/artikel/human-league-being-boiled-und-das-roland-system-100)).
- **Human League, albums *Reproduction* and *Travelogue***: a large System 100 (1×101, 2×102, 2×104, 1×103) was multitracked "to provide nearly all the arrangements, including drums and percussion". This claim is **uncited** in a "needs more citations" article ([Wikipedia](https://en.wikipedia.org/wiki/Roland_System_100)). Attack Magazine also says Ware used an expanded System 100 extensively on those two albums (search excerpt, [Attack Magazine](https://attackmagazine.com/?p=89579)).
- **MT-32 game soundtracks**: Polynominal lists Ultima VI, Ultima VII, Ultima Underworld, Space Quest 3, Castle Dr. Brain, Monkey Island, Day of the Tentacle and Dune as MT-32 titles, and compares original MT-32 Dune with the MUNT emulator ([Polynominal MT-32](https://www.polynominal.com/roland-mt-32)).
- **D-110, D-70, JD-800, JD-990, S-50, SH-09**: no source was found that ties a named commercial recording to these machines' *drum sounds*. Synthmania's famous D-70 patch is a non-drum pad ("Shaku Zulu") ([Synthmania D-70](https://www.synthmania.com/d-70.htm)).

### Inferences
- Any MT-32 game whose music uses MIDI channel 10 plays the MT-32 rhythm part. So the drums in those soundtracks are the 30 MT-32 rhythm sounds. Inferred from the architecture.
- The SH-09 manual's advice to trigger its "Bass Drum" chart from a CR-78/DR-55 trigger output is the documented way the SH-09 was used as a drum voice. It is not a specific recording.

### Gaps
- No published step chart or transcription was found for "Being Boiled", any Human League *Reproduction*/*Travelogue* track, or any MT-32 game tune. More searching was blocked by the exhausted search budget.
- Release years for the MT-32 games and the Human League albums were not verified in the fetched sources, so they are left null in the JSON.

## Q7. Free, clearly licensed MIDI pattern files

### Takeaway
None found. No MIDI pattern source with a clear licence was identified for any of these machines. Free sample sources with stated terms exist (the SH09 readme), but they are audio, not MIDI.

### Cited Findings
- No source found. The search budget was exhausted before a dedicated search for MIDI pattern files could be run.

### Inferences
- MT-32 game music MIDI rips exist widely, but their licence status is typically unclear or copyrighted. They should not be listed as "clearly licensed".

### Gaps
- A follow-up search could look for permissively licensed (CC0 / CC-BY) MIDI drum grooves in GM/MT-32 layout. Those would play directly on the D-110/MT-32 maps above.

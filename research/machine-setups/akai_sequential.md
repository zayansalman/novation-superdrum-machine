# Akai MPC60, XE8, XR10 and Sequential Circuits Drumtraks, TOM: hardware setup, sound banks, patterns and famous recordings

## 1. What voices does each machine have, in front-panel or pad order, with the exact labels?

### Takeaway
The Drumtraks has 13 instrument keys in six channel groups: BASS | SNARE RIM | TOM 1 TOM 2 | CRASH RIDE | CLOSED OPEN | CLAPS TAMB COWBELL CABASA. The TOM has 8 buttons. The XR10 has 15 key pads, and the sounds on them come from 10 pad banks (bank 1 at power-on). The XE8 has no pads: it plays 16 numbered sound slots per program. The MPC60 has 16 pads; in v3 software there are 4 banks, and in the old software the hi-hat pad was HIHT at A01.

### Cited Findings
- **Primary documents used:**
  - Drumtraks Operation Manual CM400A, issued Nov 1983 — [Drumtraks manual](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - XR10 Owner's Manual — [XR10 manual](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
  - XE8 Operator's Manual — [XE8 manual](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
  - MPC60 Software v3.1 Operator's Manual — [MPC60 manual](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - The TOM owner's manual on manualmachine.com returned HTTP 403, so TOM facts below come from 1985 magazine reviews.

**Sequential Circuits Drumtraks (Model 400)**
- The manual's official drum-number order is: 0 BASS, 1 SNARE, 2 RIM, 3 TOM 1, 4 TOM 2, 5 CRASH CYMBAL, 6 RIDE CYMBAL, 7 CLOSED HI-HAT, 8 OPEN HI-HAT, 9 CLAPS, 10 TAMB, 11 COWBELL, 12 CABASA — [Drumtraks manual, "400 MIDI" p.7, Table 7](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- The spec sheet groups the 13 instruments into channels:
  - Channel 1: Bass
  - Channel 2: Snare, Rim
  - Channel 3: Tom 1, Tom 2
  - Channel 4: Crash Cymbal, Ride Cymbal
  - Channel 5: Closed Hi-Hat, Open Hi-Hat
  - Channel 6: Claps, Tambourine, Cowbell, Cabasa
  - The manual says "Each instrument has its own performance key" — [manual p.15-1](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- The front-panel photo in the pack (`Sequential Drumtacks/DrumTraks/drumtracks.jpg`, a local file) shows the bottom row of keys under the headers CH 1 to CH 6 in that same order. "CYMBAL" is printed under CRASH/RIDE and "HI HAT" under CLOSED/OPEN. To the left of the keys are the PER INSTRUMENT VOLUME and TUNING knobs and the RUN/STOP and ACCENT buttons. The panel controls are also drawn in [manual p.1-3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf).
- Key names printed in the manual's MIDI keyboard figure: BASS, SNARE, RIM, CLAPS, TOM 1, TOM 2, CLOSED HI HAT, OPEN HI HAT, CRASH, RIDE, TAMB, COW-BELL, CABASA — [manual, "400 MIDI" p.4](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- The 13 trigger pads are not touch-sensitive — [Wikipedia: Drumtraks](https://en.wikipedia.org/wiki/Drumtraks); [Hollow Sun](https://hollowsun.com/nostalgia/vintage/drumtraks/index.html)

**Sequential Circuits TOM (Model 420)**
- The eight voices, read left to right: "Bass drum, snare drum, tom 1, tom 2, hi hat open, hi hat closed, crash cymbal and claps". Each has its own square button that plays the voice — [International Musician 1985 review (muzines)](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
- Other reviews give the same 8 sounds:
  - Each sound has its own triggering pad — [E&MM, July 1985](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - "No ride — bit of a shame" — [muzines review 11797](https://www.muzines.co.uk/articles/sequential-tom/11797)

**Akai XR10**
- The XR10 has 24 rubber pads, of which 15 are non-dynamic instrument pads — [Music Technology, June 1990](https://www.muzines.co.uk/articles/akai-xr10/387). The manual calls them "Key pads #1-#15" — [XR10 manual p.14](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- There are 10 internal Pad Banks. Banks 1-5 are fixed and banks 6-10 can be edited. The PAD BANK key steps through 01-10, and the display shows "BANK01" — [manual p.15](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **Factory Pad Bank 1** (Chart A), pad #1 to #15: KICK 7, SNARE 2, CRASH 1, TOM1 L, TOM1 M, TOM1 H, HAT CL, HAT MD, HAT OP, CRASH 2, CHOKE, RIDE, RIM 1, CLAPS, FINGER — [manual p.16, Chart A](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **Other fixed banks** (Chart A), pads #1 to #15 — [same chart](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf):
  - Bank 2: KICK 3, SNARE 5, SNARE 9, TOM2 L, TOM2 M, TOM2 H, HAT CL, HAT MD, HAT OP, CRASH 2, CHOKE, CRASH 1, RIM 2, COWBELL, TAMB.
  - Bank 3: KICK 6, SNARE 3, SNARE 8, TOM3 L/M/H, SQK L, SQK H, CLAVES, SNARE 1, SNARE 10, CABASA, HITS, TRI L, TRI H.
  - Bank 4: KICK 1, SNARE 6, RIM 1, TOM4 L/M/H, AGOGO L, AGOGO H, WHISTLE, TIMB H, CONGA 1, CONGA 2, TIMB L, CONGA 3, CONGA 4.
  - Bank 5: CONGA 1, CONGA 2, TAMB, CONGA 3, CONGA 4, COWBELL, TIMB L, TIMB H, CABASA, GUIRO 2, GUIRO 1, VIBRA, AGOGO L, AGOGO H, WHISTLE.
  - Bank 10 (factory, editable) puts user sounds 83-97 on all 15 pads. These are all copies of 65-CHOP.
- When a preset rhythm is playing, only pads #1-#9 play sounds. Pads #10-#15 select Variation A-C and Fill-in A-C — [manual p.14, p.19](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- The panel legend pairs each rhythm number with a sound name, for example "1 ROCK1 /KICK1" through "64 /AGOGO H" — [polynominal: legend image](https://www.polynominal.com/akai-xr10/assets/images/preset.jpg)

**Akai XE8**
- The XE8 is a 1U rack module with two 2-digit displays and no sound names: "No names... just numbers!" — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/xe8/index.html)
- You audition sounds with the SHOT key, turning the SOUND NO knob to step through the 16 sounds of Program 1 — [XE8 manual p.7](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- **Factory Program 1**, sounds 1-16: KICK 0, KICK 1, KICK 2, KICK 3, HIHT 0, HIHT 1, HIHT 2, SNARE 0, SNARE 1, SANRE 2 [sic], TOM 0, TOM 1, CRASH, JAZZ RIDE, CLAP, PERC — [manual p.23, "Program Data (Program No1)"](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- The official ROM names for internal sounds 1-16: KICK-0, KICK-1, KICK-2, KICK-3, HIHAT-0, HIHAT-1, HIHAT-2, SNARE-0, SNARE-1, SNARE-2, TOM-0, TOM-1, CRASH, JAZZ RID, CLAP, PERC — [manual p.26](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)

**Akai MPC60**
- **Pads and banks**
  - 16 pads, sensitive to velocity and pressure, with 4 pad banks — [MPC60 manual p.218 specifications](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - In v3 the 64 pad/bank combinations are named A01-D16, and the BANK 2 key cycles through banks A-D — [manual p.14-15, p.18](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - Version 3 raised the number of pad banks "from two to four" — [manual p.4](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **Old software (v1/v2)**
  - In v1/v2, drum notes were assigned "to one of 32 pad names (HIHT-DR16)". The manual names HIHT (shown as pad A01), SNR1 and SNR2, plus a pad called BASS — [manual p.168](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - RBMA describes "32 different drums in the machine's memory" — [Red Bull Music Academy](https://daily.redbullmusicacademy.com/2017/11/mpc-instrumental-instruments)
- **Panel legend**
  - The 4x4 pad grid carried suggested drum allocations on the panel legend. Hi-hat, snares and bass drum sat on the bottom row, with toms, cymbals and percussion on the top three rows. Any sound could still be assigned to any pad — [Sound On Sound, "Akai MPC60 Revisited"](https://www.soundonsound.com/music-business/akai-mpc60-revisited)

### Inferences
- **Drumtraks panel order.** The physical left-to-right order of the Drumtraks keys matches the manual's drum-number order. The pack photo and Table 7 agree, so this order is safe for Drum Rack pads 1-13.
- **XR10 pad arrangement.** The XR10 pads are probably arranged as a 3x3 block (#1-#9) plus two columns of three (#10-#12 and #13-#15). Numbering likely runs bottom-to-top, because the manual's figure shows C = pad #10 at the bottom and A = pad #12 at the top. The physical grid is not stated in what I read.
- **MPC60 pad positions.** I place SNR1 on A02, SNR2 on A03 and BASS on A04 because of two things: the manual lists "HIHT, SNR1, SNR2, etc." in that order, and SOS describes the bottom row as hat, snares and kick. The exact positions are not confirmed.

### Gaps
- **TOM labels.** The exact silkscreen legends of the TOM buttons were not verified (manual not accessible).
- **MPC60 pad names.** The 32 v1/v2 pad names from A05 to the second bank (ending "DR16") were not found. The MPC60 v2 manual on ManualsLib returned HTTP 403.

## 2. Which sounds share one voice or cut each other off (open/closed hat, mute groups)?

### Takeaway
Only the Drumtraks has fixed groups: six one-at-a-time channels, which work as five choke groups (bass sits alone on channel 1). The MPC60 has programmable "Cutoff" mute targets. The XE8 makes two sounds cut each other only when they share an output in fixed-assign mode. No hi-hat choke is documented for the TOM or XR10.

### Cited Findings
- **Drumtraks**
  - "Only one instrument in each channel can be played simultaneously. Each channel has a separate output jack." The channels are: 2 = Snare/Rim, 3 = Tom 1/Tom 2, 4 = Crash/Ride, 5 = Closed/Open Hi-Hat, 6 = Claps/Tambourine/Cowbell/Cabasa, with Bass alone on channel 1 — [Drumtraks manual p.15-1](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - The E&MM review gives the same channel grouping — [E&MM, March 1984](https://www.muzines.co.uk/articles/sequential-circuits-drumtraks/1581)
  - Vintage Synth Explorer lists "Polyphony - 12 voices", which conflicts with the manual's six one-at-a-time channels — [vintagesynth](https://vintagesynth.com/sequential-circuits/drumtraks)
- **MPC60**
  - Each note number has two Cutoff fields. When the note plays, "any currently playing sounds assigned to either of the note numbers in these two fields are immediately terminated". The manual's example is "a closed hi-hat stopping an open hi-hat, or a muted triangle stopping an open triangle" — [MPC60 manual p.118](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - The Poly field per note offers POLY (overlapping), MONO ("terminating and restarting playback") and NOTE OFF (stops on pad release) — [manual p.117-118](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **MPC60 hi-hat history**
  - With the old software, the hi-hat pad played "one of three different sounds (closed, loose or open hi-hat) ... depending on the slider position", and the slider also varied decay — [manual p.115](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - Version 3 emulates this with the DCY SW assignment mode, where up to 3 sounds share one note and the decay value picks which one plays. The other v3 modes are simultaneous playback or a velocity switch — [manual p.3, p.113-115](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **XE8**
  - In fixed-assign mode, "as 16 sounds are assigned to 8 outputs, there will be cases where 2 sounds are assigned to 1 output channel. Since 2 sounds cannot be outputted simultaneously, the new sound will replace the previous sound." Free-assign mode instead puts a new sound on the quietest output — [XE8 manual p.19](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
  - The manual warns that the voice assigner judges by decay level, so overly long decays can steal channels — [manual p.18](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
  - The individual outs are monophonic, and sounds cannot be removed from the mix out — [Music Technology, April 1989](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58)
- **XE8 hat trick**
  - With velocity modulating decay, "playing the open hi hat sound hard will give you open hi-hat, while playing it soft will give you closed hi hat sound" — [XE8 manual p.18](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- **TOM**
  - The sound circuitry can play only four sounds at once. When all four channels are busy, a new event takes the channel with the least sound remaining. Retriggering a sounding voice restarts it, while Stack mode moves it to another channel so hits can overlap — [E&MM, July 1985](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - "Only four voices can sound at one time" — [International Musician 1985](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
  - None of the four reviews says whether the open and closed hats cut each other off.
- **XR10**
  - Polyphony is 8 notes. "A ninth note on a beat simply erases the earliest note you played on that beat" — [Music Technology, June 1990](https://www.muzines.co.uk/articles/akai-xr10/387)
  - No open/closed hat cut-off is described. CHOKE is a sample (a choked cymbal), not a function — [XR10 manual p.37, Chart C](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)

### Inferences
- **Drumtraks in Ableton.** A faithful Drum Rack would use five choke groups mirroring channels 2-6. Each Simpler should also be set to one voice, because each hardware channel restarts rather than overlapping.
- **MPC60 in Ableton.** A closed-to-open hat choke is the manual's own recommended setting, so it is a reasonable default, but it was not fixed on the hardware.
- **XR10 and TOM in Ableton.** A hat choke group would be a modern convenience, not documented hardware behaviour.

### Gaps
- **TOM channel behaviour.** Whether the TOM's four channels give closed-cuts-open hat behaviour is unknown.
- **XE8 factory routing.** The XE8 factory Program 1 output assignments (which sounds share an output) could not be read reliably from the low-resolution data sheet.

## 3. What controls does each voice have, how do accent and dynamics work, and is there flam, swing, per-voice tuning or reverse?

### Takeaway
- **Drumtraks:** 16-step level and 16-step tuning per instrument, an ACCENT key, and eighth-note swing at 50-70%.
- **TOM:** 32-step tuning, 8 levels and pan per note, a global Reverse button, and no documented swing.
- **XR10:** 12 parameters per sound, including tune ±2 octaves, pan, decay/hold, pitch sweep, reverse and effect send. It has an ACCENT key and no documented swing.
- **XE8:** per-sound tuning, pitch sweep, envelope, reverse, and key/velocity modulation. It has no accent.
- **MPC60:** per-note tune, attack/decay, velocity modulation, poly mode, pan, outputs, Note Variation, 16 Levels, and swing at 50-75%.

### Cited Findings
**Drumtraks**
- **Volume and tuning**
  - PER INSTRUMENT VOLUME has "one of sixteen levels" (00-15), and PER INSTRUMENT TUNING has "one of sixteen pitches" (00-15). Each is set by holding the instrument key and turning the knob — [manual p.1-3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - Volume and pitch can also be stored per note: a "dynamic" event holds V = 0-15 and P = 0-15 — [manual, "400 MIDI" p.6](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - Recorded per note: time, accented or not, instrument, volume and pitch — [manual p.14-2](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **Accent**
  - "If ACCENT is held, playing any instrument key will accent that instrument" — [manual p.1-3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - Final volume runs 0-255. PER INSTRUMENT VOLUME covers 0-175, with each displayed step worth 11 units. "The ACCENT key adds 80 final volume units". MIDI velocity covers the same 0-175 range in 16 levels and "allows MIDI-input notes to be accented" — [manual p.14-4](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **Swing**
  - Swing defaults to 50% and can be set to 54, 58, 62, 66 or 70% only while stopped. It applies only when the beat value is 4 — [manual p.2-3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - It changes "the syncopation of the eighth notes" for patterns with a quarter-note beat — [manual p.14-3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
  - The spec sheet calls these "Six 'feels': 50, 54, 58, 62, 66, 70 %" — [manual p.15-1](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **Error correct**
  - Values are 1/2, 1/4, 1/6, 1/8, 1/12, 1/16, 1/24, 1/32, 1/48 and 1/96 — [manual, "400 MIDI" p.7](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **Tom tuning**
  - The tom tuning gives "effectively 32 different tom sounds" — [E&MM, March 1984](https://www.muzines.co.uk/articles/sequential-circuits-drumtraks/1581)
- **Not covered**
  - The manual has no section on flam, roll, reverse or pan; its contents and specifications list none — [manual pp. iii-iv, 15-1 to 15-3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)

**TOM**
- **Per-note settings**
  - Tuning has 32 levels, and tuning, volume and pan are note-specific and can change in real time while recording. Pan is left/centre/right, set via MIDI keys — [E&MM, July 1985](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - "Each sound sample has a 32-step scale of tunings" and "eight volume levels for programming dynamics" — [muzines review 11797](https://www.muzines.co.uk/articles/sequential-tom/11797)
  - Control-section volume runs 0-7 — [International Musician 1985](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
- **Reverse** (the reviews differ on whether it is stored or real-time only)
  - Reverse is a button press, stored with the pattern, and has no LED to show it is on — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - IM says it works "only in real time, not on already-recorded sound" — [IM](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
  - Forward and backward versions of a sound can play together — ["Tasty TOM" review](https://www.muzines.co.uk/articles/tasty-tom/3918)
  - Hollow Sun calls it the first reverse function on a drum machine — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/tom/index.html)
- **Dynamics and accent**
  - No accent key is described. Dynamics come from a velocity-sensitive MIDI keyboard — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - Error-correct rolls can be made "progressively louder or quieter", and Human Factor "changes slightly the pitches and volumes as the machine plays" — [IM](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
- **Timing**
  - Error correct runs "from 2 up to 96", and auto repeat makes rolls. Tempo is 40-240 BPM — [IM](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
  - Improv drops in fills a set percentage of the time — [muzines 11797](https://www.muzines.co.uk/articles/sequential-tom/11797)
  - No review mentions swing/shuffle or flam — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078); [IM](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602); ["Tasty TOM"](https://www.muzines.co.uk/articles/tasty-tom/3918); [11797](https://www.muzines.co.uk/articles/sequential-tom/11797)

**XR10**
- **Per-sound parameters** (stored per sound, not per pad) — [XR10 manual p.5](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf):
  - Sound Volume 0-31
  - Sound Tune -26 to +25 (100 cents per step)
  - Fine Tune -8 to +7 (6.25 cents per step)
  - Pan L15-Center-R15
  - Effect Send Volume 0-31
  - DCA Decay 0-31 and DCA Hold 0-31
  - Sweep Decay 0-63, Sweep Depth 0-31, Sweep Polarity DU/UD
  - Reverse FW/RV
  - Velocity Feel ON/OFF
  - Sound Select 1-65 (user sounds only)
- **Factory settings**
  - Factory parameter values for every sound are tabulated in Charts B-D. As far as I could read the low-resolution scan, the hats are panned around R10 and each tom set runs L15 / centre / R15 — [manual p.36-38](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **Accent**
  - Hitting a pad "while pressing the ACCENT, a louder sound will be reproduced" — [manual p.14](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
  - Accents are recorded per note. In step time each of the 15 pads plays the selected sound at a different velocity, and Octopad dynamics are "quantised to one of 15 levels" — [Music Technology, June 1990](https://www.muzines.co.uk/articles/akai-xr10/387)
- **Timing**
  - Resolution is 1/384 (96 per quarter note), and tempo is 40-296 BPM — [manual p.5](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
  - The manual's contents list Note Repeat and Timing Correct but no swing entry — [manual p.1-2](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)

**XE8**
- **Parameter Guide** — [XE8 manual p.25](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf):
  - NOTE: source number (INT 1-16 or EXT 1/2 card), plus low and high MIDI note.
  - TUNE: master tuning -8 to +7 and fine tuning -8 to +7.
  - TUN-MOD: key offset or velocity, depth 0-15, sweep polarity.
  - SW-RANGE and SW-TIME: pitch sweep depth and time, each with key/velocity modulation.
  - OUTPUT: level 0-127, and REPLAY forward/back, which is reverse.
  - VCA-MOD: key or velocity, depth 0-15, hold time.
  - VCA-ENV: decay with key/velocity modulation.
  - PLAY: free or fixed assign, output 1-8.
- **Envelope and volume**
  - Hold time is 0-127 in 4 ms steps. Volume can follow velocity or key position — [manual p.17-18](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- **Modulation**
  - "A depth of 15 gives equal temperament". The XE8 can also add random pitch and duration fluctuation — [Music Technology, April 1989](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58)
- **No sequencer**
  - There is no sequencer, so there is no swing or flam — [Music Technology](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58)

**MPC60**
- **Per note (35-98) in each program** — [MPC60 manual p.116-118](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf):
  - Attack and Decay, each 101 values over 0-5000 ms.
  - Decay mode START or END.
  - Velocity modulation of attack, soft start and volume (0-100%).
  - Tune "-120 (-12 semitones) to 60 (+6 semitones) in increments of 0.1 semitone".
  - Poly POLY/MONO/NOTE OFF and two Cutoff notes.
- **Mixer**
  - Stereo pan runs "50L to C to 50R" — [manual p.128-129](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - Each sound can go to individual out 1-8 or to the pairs 1&2, 3&4, 5&6, 7&8, with an echo send level — [manual p.126-127](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **Note Variation slider** (formerly the Hihat Decay Slider)
  - It can be assigned to any pad to vary TUNING, DECAY or ATTACK, and the values are recorded into sequences — [manual p.19-21](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **16 LEVELS**
  - One sound plays from all 16 pads at 16 evenly spaced levels of velocity, tuning, attack or decay — [manual p.21-22](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **Pad dynamics**
  - The pads are dynamic, and FULL LEVEL forces maximum level — [manual p.18](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **Swing**
  - Swing works on 1/16 or 1/8 notes from 50% to 75%. 66% is "technically perfect" triplet swing. The manual suggests 54% (removes stiffness) and 62% (relaxed 1/16 swing), both at 100 BPM — [manual p.43-44](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - Producers mainly swung the hi-hats — [RBMA](https://daily.redbullmusicacademy.com/2017/11/mpc-instrumental-instruments)
- **Reverse**
  - Reverse exists only as a sample edit: in v3 "any portion can be silenced or reversed" — [manual p.3](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)

### Inferences
- **Drumtraks in Ableton.** The ACCENT math (+80 of 255) means an accented note at full instrument volume reaches 255 "final volume units" against 175 unaccented, about 1.46x. The manual doesn't say whether these units are linear amplitude. In MIDI clips, a plain hit and an accented hit can map to two velocity tiers.
- **Drumtraks swing.** The swing acts on eighth notes, not sixteenths. An Ableton groove should shift the off-beat 8ths, which is different from the MPC60's 1/16 swing.
- **XE8 key tracking.** Because the XE8's Program 1 tracks key position in equal temperament, its kit spreads pitched copies of each sound over several keys. See section 5.

### Gaps
- **TOM numbers.** The TOM's exact tuning range in semitones, and whether its pan has more than three positions, are unknown.
- **XE8 tuning units.** The units of the XE8 "master tuning" (-8 to +7) are not stated in what I read.

## 4. Any built-in effects?

### Takeaway
None of the five has built-in effects. The MPC60 and XR10 have effect-send outputs for external units.

### Cited Findings
- **Drumtraks:** "Effects - None" — [vintagesynth](https://vintagesynth.com/sequential-circuits/drumtraks). Its internal mixer "does not have pan facilities", and the manual suggests external delay or chorus on the channel outputs — [manual p.9-1](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **TOM:** stereo outputs only, with no effects described in any review — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078); [IM](https://www.muzines.co.uk/articles/sequential-circuits-tom/12602)
- **XR10:**
  - A per-sound Effect Send plus an Effect Send output jack — [XR10 manual p.5](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
  - The send is "intended for an external reverb or multi-FX unit" — [Music Technology](https://www.muzines.co.uk/articles/akai-xr10/387)
- **XE8:** no effects mentioned. The outputs are eight mono individual outs plus a mono mix out — [Music Technology](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58); [XE8 manual p.19](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- **MPC60:**
  - The rear panel has an echo send mixer output and an echo return input — [MPC60 manual p.218](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
  - "No filter" — [vintagesynth](https://vintagesynth.com/akai/mpc60)

### Inferences
- In an Ableton rebuild, any reverb or delay is a later addition, not part of the original machine.

### Gaps
- None.

## 5. ROM machines (XE8, XR10): total sounds, categories, official ordered list, factory kit layout and default MIDI note map

### Takeaway
- **XR10:** 65 ROM sounds in an official numbered list, plus 32 user copies.
- **XE8:** 16 internal sounds, plus 16-sound ROM cards. SL801R and SL802R came in the box; SL803R and SL804R (14 sounds each) were optional.
- **Default MIDI maps:** both manuals publish one (XR10 Chart E; XE8 Program 1 key ranges). The Drumtraks publishes its own MIDI key map too.

### Cited Findings
**XR10**
- **Totals**
  - "Internal Sound Sources 65 patterns, Copy Sound Sources 32 patterns" — [XR10 manual p.5](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
  - Music Technology also counts 65 16-bit PCM samples — [Music Technology](https://www.muzines.co.uk/articles/akai-xr10/387)
  - Polynominal says 64 and vintagesynth says "64 to choose from", which conflicts with the manual — [polynominal](https://www.polynominal.com/akai-xr10/index.html); [vintagesynth](https://vintagesynth.com/akai/XR10)
- **Official ordered list** (Charts B and C) — [XR10 manual p.36-37](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf):
  - 1-10: KICK 1-10
  - 11-20: SNARE 1-10
  - 21-22: RIMSHOT 1-2
  - 23-25: HAT CL, HAT MD, HAT OP
  - 26-37: TOM1 L/M/H, TOM2 L/M/H, TOM3 L/M/H, TOM4 L/M/H
  - 38-41: CRASH 1, CRASH 2, RIDE, CHOKE
  - 42-43: CLAPS, FINGER
  - 44-52: CONGA 1-4, VIBRASLAP, GUIRO 1-2, CABASA, TAMBOURINE
  - 53: HITS
  - 54-55: TRIANGLE L/H
  - 56-58: COWBELL, CLAVES, WHISTLE
  - 59-60: SQUEAK L/H
  - 61-62: TIMBALES L/H
  - 63-64: AGOGO L/H
  - 65: CHOP
  - 66-97: USER sounds (copies of presets with edited parameters)
- **What some names mean:** CHOP = slapped bass, HITS = orchestral hit, FINGER = finger click, and the review lists a "choke cymbal" — [Music Technology](https://www.muzines.co.uk/articles/akai-xr10/387)
- **User sounds**
  - "User sounds 71 to 97 are used for the Demonstration songs". As far as I could read the scan, user sounds 83-97 are copies of 65-CHOP tuned from -1 to +13 semitones, making a chromatic slap-bass scale — [manual p.38, Chart D](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **Factory MIDI receive note map (Chart E)** — [XR10 manual p.65](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf):

  | Notes | Sound |
  |---|---|
  | 0-14 | USER 83-97 (the CHOP scale) |
  | 15-34 | not assigned |
  | 35, 36 | KICK 1 |
  | 37 | CHOKE |
  | 38 | KICK 2 |
  | 39 | RIDE |
  | 40 | KICK 3 |
  | 41 | KICK 4 |
  | 42 | HAT CL |
  | 43 | KICK 5 |
  | 44 | HAT MD |
  | 45 | KICK 6 |
  | 46 | HAT OP |
  | 47 | KICK 7 |
  | 48 | KICK 8 |
  | 49 | CRASH 1 |
  | 50 | KICK 9 |
  | 51 | CRASH 2 |
  | 52 | KICK 10 |
  | 53 | SNARE 1 |
  | 54 | TOM1 L |
  | 55 | SNARE 2 |
  | 56 | TOM1 M |
  | 57 | SNARE 3 |
  | 58 | TOM1 H |
  | 59 | SNARE 4 |
  | 60 | SNARE 5 |
  | 61 | SQUEAK L |
  | 62 | SNARE 6 |
  | 63 | SQUEAK H |
  | 64 | SNARE 7 |
  | 65 | SNARE 8 |
  | 66 | TOM2 L |
  | 67 | SNARE 9 |
  | 68 | TOM2 M |
  | 69 | SNARE 10 |
  | 70 | TOM2 H |
  | 71 | RIMSHOT 1 |
  | 72 | RIMSHOT 2 |
  | 73 | TIMBALES L |
  | 74 | CLAPS |
  | 75 | TIMBALES H |
  | 76 | FINGER |
  | 77 | CONGA 1 |
  | 78 | TOM3 L |
  | 79 | CONGA 2 |
  | 80 | TOM3 M |
  | 81 | CONGA 3 |
  | 82 | TOM3 H |
  | 83 | CONGA 4 |
  | 84 | VIBRASLAP |
  | 85 | AGOGO L |
  | 86 | GUIRO 1 |
  | 87 | AGOGO H |
  | 88 | GUIRO 2 |
  | 89 | CABASA |
  | 90 | HITS |
  | 91 | TAMBOURINE |
  | 92 | TRIANGLE L |
  | 93 | TRIANGLE H |
  | 94 | COWBELL |
  | 95 | CLAVES |
  | 96 | WHISTLE |
  | 97 | TOM4 L |
  | 98 | TOM4 M |
  | 99 | TOM4 H |
  | 100 | CHOP |
  | 101-117 | USER 66-82 |
  | 118-127 | not assigned |
- **Note maps and MIDI**
  - Receive notes can be reassigned from 00-127. Transmit notes "are not set when the XR10 is shipped" — [manual p.66-67](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
  - The MIDI chart (Version 2.0, dated 1990.1.10) shows transmit channel 1 by default, receive 1-16, velocity 1-127, SysEx IDs 47H/4DH, and clock — [manual, MIDI chart](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **Factory kit:** Pad Bank 1, listed in section 1 — [manual p.16](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)

**XE8**
- **Sampled Sound List** — [XE8 manual p.26](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf):
  - INTERNAL 1-16: KICK-0, KICK-1, KICK-2, KICK-3, HIHAT-0, HIHAT-1, HIHAT-2, SNARE-0, SNARE-1, SNARE-2, TOM-0, TOM-1, CRASH, JAZZ RID, CLAP, PERC.
  - SL801R (Standard Accessory): KICK-4, SNARE-3, RIM SHOT-0, HIHAT CLOSE-0, HIHAT OPEN-0, TOM-2, TOM-3, TOM-4, TOM-5, CYMBAL-0, CYMBAL-1, PERCUSSION-0, PERCUSSION-1, PERCUSSION-2, PERCUSSION-3, ORCHESTRA HIT-0.
  - SL802R (Standard Accessory): KICK-5, SNARE-4, RIM SHOT-1, HIHAT CLOSE-1, HIHAT OPEN-1, TOM-6, TOM-7, TOM-8, TOM-9, CYMBAL-2, CYMBAL-3, CYMBAL-4, PERCUSSION-4, PERCUSSION-5, PERCUSSION-6, PERCUSSION-7.
  - SL803R (Option): KICK-8, SNARE-7, RIM SHOT-3, TOM-13, TOM-14, TOM-15, CYMBAL-9, CYMBAL-10, CYMBAL-11, HIHAT OPEN-3, HIHAT CLOSE-3, GATE SNARE, GATE KICK, CYMBAL-12.
  - SL804R (Option): KICK-6, SNARE-5, RIM SHOT-2, TOM-10, TOM-11, TOM-12, HIHAT CLOSE-2, HIHAT OPEN-2, CYMBAL-5, CYMBAL-6, CYMBAL-7, CYMBAL-8, KICK-7, SNARE-6.
- **Internal ROM contents**
  - 16 onboard sounds in 1 MB of ROM: four bass drums (one recorded with ambience), three snares, three hi-hats, two toms, crash, ride, handclaps and "percussion" — [Music Technology](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58)
- **Cards**
  - Each card holds up to 16 samples, and the first two cards came free (48 samples in total) — [Music Technology](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58)
  - A card may hold fewer than 16 sounds "due to the length of sounds" — [manual p.11](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- **Programs and key ranges**
  - There are 32 programs of 16 sounds — [MT](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58); [polynominal](https://polynominal.com/sample-packs/akai-xe8)
  - "As the note number of XE8's program is set to keyboards with 61 keys, sound will come out by pressing the keys". Up to 16 keys can be assigned to one sound, and up to eight sounds can play from one key — [manual p.8-10](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)
- **Factory Program 1 key ranges** (NOTE row: source / low key / high key) — [manual p.23](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf):

  | Sound | Name | Keys |
  |---|---|---|
  | 1 | KICK 0 | 36-38 |
  | 2 | KICK 1 | 39-41 |
  | 3 | KICK 2 | 42-44 |
  | 4 | KICK 3 | 45-47 |
  | 8 | SNARE 0 | 48-49 |
  | 9 | SNARE 1 | 50-51 |
  | 10 | SNARE 2 | 52-53 |
  | 5 | HIHT 0 | 54-55 |
  | 6 | HIHT 1 | 56-57 |
  | 7 | HIHT 2 | 58-59 |
  | 11 | TOM 0 | 60-66 |
  | 12 | TOM 1 | 67-76 |
  | 13 | CRASH | 77-86 |
  | 14 | JAZZ RIDE | 87-94 |
  | 15 | CLAP | 95 |
  | 16 | PERC | 96 |

  The TUNE-MOD row appears to read "A 15" (key offset at depth 15, which is equal temperament), so each sound plays chromatically across its range.
- **MIDI chart**
  - Receive only; Omni default; note 0-127; velocity 1-127; program change 1-32 recognized; SysEx IDs 47H/4AH; no clock — [manual p.27](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf)

**Drumtraks (fixed ROM, for reference)**
- **MIDI key assignments** (Table 1): 35, 36 BASS; 37 RIM; 38, 40 SNARE; 39 CLAPS; 41, 43 TOM 1; 42, 44 CLOSED HI-HAT; 45, 47 TOM 2; 46 OPEN HI-HAT; 49 CRASH CYMBAL; 51 RIDE CYMBAL; 54 TAMB; 56 COWBELL; 58 CABASA. "Transmit: Keys 36, 40, 43, 44, and 47 are sent for the duplicated sounds" — [manual, "400 MIDI" p.4](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **Power-up mode:** Omni on, and the basic channel is set to 15 at the factory — [manual, "400 MIDI" p.3](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **Swappable ROMs:** sounds sit on ROM chips swappable through the front panel, and the unit accepts LinnDrum ROM chips — [Wikipedia: Drumtraks](https://en.wikipedia.org/wiki/Drumtraks)

**TOM (fixed ROM)**
- **Cartridges**
  - A cartridge adds 7 more sounds, for 15 voices in all, still limited to four channels. Four cartridge sets are listed, with these example sounds:
    - Standard Drumkit: ride cymbal, cymbal bell, cowbell, rimshot
    - Latin Percussion: conga slap, timbale, timbale rim, agogo bell, guiro
    - Electronic: kick drum, tom, laser, record scratch
    - Effects: dog bark, car horn, orchestra "tutt", crowd
    - Source — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - Another review says a cartridge holds "eight more drum samples", with Latin Percussion first — [muzines 11797](https://www.muzines.co.uk/articles/sequential-tom/11797); this conflicts with E&MM's seven.
- **MIDI**
  - The 32 adjacent keys map to the 32 tuning levels, and pan and trigger-out sit on selected keys — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078)
  - "The bottom octave of keys on the synth select the sound played on the TOM", and the upper octaves play the pitches — ["Tasty TOM"](https://www.muzines.co.uk/articles/tasty-tom/3918)

**MPC60 (sampler, no ROM sounds)**
- **Sound engine**
  - Up to 128 sounds (34 before v3), 8 programs × 64 note assignments (35-98), 12-bit non-linear at 40 kHz, 16 voices, and 13.1 s of memory (26.2 s expanded) — [MPC60 manual p.3, p.14, p.218](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)
- **Factory disks**
  - Four factory floppies: "Studio set", "Rock set", "Dry set", "Synth set". The add-on library ran SL601-SL630 (for example SL601 Samba set, SL622 Mix-2 Gate, SL630 Brushes) — [R-Massive](https://zine.r-massive.com/?p=5980)
- **Default note conversion**
  - By default, v1/v2 pad names convert to the General MIDI note with the same instrument name. For example, pad BASS becomes note 36 — [manual p.168](https://www.polynominal.com/akai-mpc60/akai-mpc60-manual.pdf)

### Inferences
- **XE8 key ranges are internally consistent.** The Program 1 ranges cover exactly the 61 keys 36-96 with no overlaps, which matches the manual's "61 keys" statement. This supports the reading of the low-resolution scan.
- **XR10 kick/snare layout.** In Chart E, kicks 1-10 are interleaved on white keys and snares from note 53 upward. Hats sit on the General MIDI notes 42, 44 and 46, and the crashes sit on 49/51.

### Gaps
- **XE8 Program 1 values.** The note ranges and output routing were read from a small rotated table; check against a sharper scan before relying on them. The root pitch within each range is not stated.
- **XE8 card contents.** I could not confirm whether SL803R/SL804R hold fewer sounds because of sample length (the manual allows this). The polynominal card descriptions do not match these two lists exactly — [polynominal](https://polynominal.com/sample-packs/akai-xe8)

## 6. What does each pack folder contain?

### Takeaway
All 10 folders hold 16-bit/44.1 kHz WAV one-shots named by instrument, with no loops or MIDI. Coverage is:
- XE8: internal ROM plus the SL801R card, complete.
- XR10: two partial-to-near-complete sets.
- Drumtraks: three sets, two of them complete.
- TOM: four complete 8-sound sets.
- MPC60: a 21-sound kit plus two tonal extras.

### Cited Findings (from read-only `ls -R` and file headers, 2026-11-13; local files)
**Akai MPC60** — "Akai MPC-60" (21 stereo WAVs)
- Bassdrum, Bassdrum Gated, Snare 1, Snare 2, Snare 3, Rim Gated, Clap, Closed Hat, Open Hat, Crash, Ride, Tom H, Tom M, Tom L, Conga H, Conga L, Bongo, Timbale, Click.
- Two tonal extras: Bass (1.0 s) and Electric Piano (0.6 s).
- No numbers and no loose (medium) hat.

**Akai XE8** — "Akai XE8" (32 mono WAVs)
- "XE8 <name> int_1…16" is the full internal ROM in official order.
- "XE8 <name> ext_1…16" is SL801R in official order.
- The pack's names differ from Akai's:

  | Pack file | Official name |
  |---|---|
  | int_4 "ElectroTom" | KICK-3 |
  | int_5/6/7 Hat Closed / Medium / Open | HIHAT-0/1/2 |
  | int_14 "Ride" | JAZZ RID |
  | int_16 "Crack" | PERC |
  | ext_3 "Sidestick" | RIM SHOT-0 |
  | ext_10 "Ride", ext_11 "Crash" | CYMBAL-0, CYMBAL-1 |
  | ext_12-13 "Cowbell 1/2" | PERCUSSION-0/1 |
  | ext_14-15 "Block 1/2" | PERCUSSION-2/3 |
  | ext_16 "Orch" | ORCHESTRA HIT-0 |

  The official names come from [XE8 manual p.26](https://polynominal.com/sample-packs/akai-xe8/Akai%20XE8%20user%20manual.pdf). The pack has no SL802R, SL803R or SL804R sounds.

**Akai XR10** — "Akai XR-10" (57 stereo WAVs in 5 subfolders)
- Bassdrums: Bassdrum-01…10.
- Snaredrums: Snaredrum-01…10.
- Cymbals: Crash-01…03, Hat Closed, Hat Middle, Hat Open, Ride.
- Percussion (26 files): Agogo, Cabasa, Clap, Claves, Conga-01…04, Cowbell, "Fingersanp", Guiro-01, "Guirro-02", Rim Shot-01/02, Tambourine, Timbale H/L, Tom L-01/02, Tom M-01/02, "Toma H-01", Tom H-02, Triangle, "Vibrator", Whistle.
- Misc: Hit, Slap Bass, "Square Kick-01/02".
- Compared with the 65-sound ROM: only 6 of 12 toms, 1 of 2 agogos, 1 of 2 triangles.
- Crash-03 is 0.45 s long, against 1.36 s for Crash-01.

**Akai XR10** — "Akai XR10" (62 mono WAVs, flat)
- XR10Kick01-10, XR10Snare01-10, XR10Rimshot01-02, XR10Hat_C/_Mid/_O.
- XR10LoTom01-04, XR10MidTom01-04, XR10HiTom01-04: 12 toms grouped by pitch rather than by set.
- XR10Crash01-02, XR10RideCymbal, XR10Choke, XR10Clap, XRFinSnap.
- XRConga01-04, XR10Vibra, XRGuira01-02, XRCabasa, XR10Tamborine, XRTambroll, XR10Triangle, XRCow, XRClave, XR10Whistle, XR10HiQ01-02, XR10Timb_Hi/_Lo, XRAgogo.
- Missing compared with the ROM: HITS, CHOP, one triangle, one agogo. "XRTambroll" has no ROM counterpart.

**Sequential Drumtraks** — three folders
- "Sequential Circuits Drumtraks": 12 stereo WAVs (Bassdrum, Snaredrum, Rim Shot, Tom, Crash, Ride, Hat Closed, Hat Open, Clap, Tambourine, Cowbell, Cabasa). There is only one tom, so this is 12 of 13.
- "Sequential Drumtacks" [sic] / "DrumTraks": 26 mono WAVs. These are two complete 13-sound sets, named "DT <Name>" and "DT_<Name>", plus drumtracks.jpg, a front-panel photo.
- "Sequential Drumtrax": 13 mono WAVs, complete.

**Sequential TOM** — three folders, each with the 8 internal sounds
- "Sequential Circuits TOM": 8 stereo WAVs (Bassdrum, Snaredrum, Tom-01, Tom-02, Hat Open, Hat Closed, Crash, Clap).
- "Sequential TOM1": 8 mono WAVs (TOMKick, TOMSnare, TOMTom_Hi, TOMTom_Lo, TOMHat_O, TOMHat_C, TOMCymbal, TOMClap).
- "Sequential Tom": 16 mono WAVs, two 8-sound sets ("Tom <Name>" and lowercase).
- No cartridge sounds and no reversed versions.

### Inferences
- **XR10 name mismatches.**
  - "Square Kick-01/02" and "XR10HiQ01/02" are very likely the ROM's SQUEAK L/H, since there is no "square kick" in the official list.
  - Crash-03 (0.45 s) is likely CHOKE.
  - "Vibrator" is VIBRASLAP, "Hit" is HITS and "Slap Bass" is CHOP.
  - The numbered files are assumed to follow ROM order (Bassdrum-07 = KICK 7, and so on).
- **XR10 toms.** The XR10 folder's Lo/Mid/HiTom 01-04 probably correspond to TOMn L/M/H for sets 1-4. The XR-10 folder's six toms cannot be mapped to sets without listening.
- **Combined coverage.** Combining the two XR10 folders covers every ROM sound except possibly the second triangle and second agogo. It is unknown whether the two "Triangle"/"Agogo" files are the same pitch.
- **Unknown mappings.** The Drumtraks folder's single "Tom.wav" may be Tom 1 or Tom 2. The TOM1 folder's Hi/Lo toms cannot be matched to Tom 1/Tom 2 without listening.

### Gaps
- **No listening.** Files were not played (by instruction), so pitch-based identification (which tom, which agogo) was not possible.

## 7. Factory preset patterns: names and step grids

### Takeaway
- **XR10:** 50 named preset rhythm styles, each with 9 parts. Names are below; no grids were found.
- **Drumtraks and TOM:** both shipped with factory or demo patterns, but no source names them.
- **XE8 and MPC60:** the XE8 has no sequencer, and the MPC60's demo sequences were disk-based and not documented.

### Cited Findings
- **XR10 parts:** each preset has three Variations (2 measures each), three Fill-ins (1 measure), and one Intro, one Break and one Ending (1 measure each) — [XR10 manual p.18](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf). The total is "450 varieties (50 varieties x 3 Variations, 3 Fill-ins, 1 Intro, 1 Break, 1 Ending)" — [manual p.5](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **XR10 tempos:** the display examples show "140:01:ROCK 1" and "135:02:ROCK 2", so the initial tempos are 140 and 135 BPM — [manual p.18](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **XR10 preset names** from the panel legend — [polynominal legend image](https://www.polynominal.com/akai-xr10/assets/images/preset.jpg):

  | No. | Name | No. | Name |
  |---|---|---|---|
  | 1 | ROCK1 | 26 | BEATBOX1 |
  | 2 | ROCK2 | 27 | BEATBOX2 |
  | 3 | ROCK3 | 28 | SHUFFLE1 |
  | 4 | ROCK4 | 29 | SHUFFLE2 |
  | 5 | ROCK5 | 30 | SHUFFLE3 |
  | 6 | DANCE1 | 31 | SAMBA1 |
  | 7 | DANCE2 | 32 | SAMBA2 |
  | 8 | DANCE3 | 33 | MAMBO |
  | 9 | DANCE4 | 34 | SALSA |
  | 10 | DANCE5 | 35 | CHACHA1 |
  | 11 | FUNK1 | 36 | CHACHA2 |
  | 12 | FUNK2 | 37 | RHUMBA |
  | 13 | FUNK3 | 38 | BEGUINE |
  | 14 | FUNK4 | 39 | BOSSA1 |
  | 15 | FUNK5 | 40 | BOSSA2 |
  | 16 | ELECTRO1 | 41 | WALTZ |
  | 17 | ELECTRO2 | 42 | COUNTRY |
  | 18 | ELECTRO3 | 43 | MARCH |
  | 19 | ELECTRO4 | 44 | TWIST |
  | 20 | ELECTRO5 | 45 | SWING |
  | 21 | DISCO1 | 46 | SLOWROCK |
  | 22 | DISCO2 | 47 | BALLAD |
  | 23 | DISCO3 | 48 | REGGAE |
  | 24 | DISCO4 | 49 | JAZZ |
  | 25 | DISCO5 | 50 | TRIBAL |

  Music Technology lists matching styles (samba, mambo, cha cha, beguine, bossa nova, rhumba, salsa, waltz, country, march, twist, reggae, jazz, five rock styles, dance, funk, electro, disco, beatbox) — [Music Technology](https://www.muzines.co.uk/articles/akai-xr10/387)
- **XR10 demo songs:** these use user sounds 71-97 — [manual p.38](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf)
- **Drumtraks:** "The Drumtraks comes pre-programmed with a few patterns (and songs)"; the manual gives no names or contents — [Drumtraks manual p.2-1](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)
- **TOM:** "The TOM's demo patterns show these off rather well"; no count or names are given — [E&MM](https://www.muzines.co.uk/articles/sequential-tom/9078)
- **XE8:** the XE8 dropped onboard sequencing — [Music Technology](https://www.muzines.co.uk/articles/akai-xe8-midi-drum-expander/58)

### Inferences
- XR10 pads #10-#15 control the variation and fill selection when presets play, so a MIDI-clip recreation would need separate clips per variation and fill.

### Gaps
- **No grids.** No source shows step grids for any XR10, Drumtraks or TOM factory pattern, so no grids are given.
- **MPC60 demos.** MPC60 factory-disk demo sequence names were not found. R-Massive lists the disks but not their sequences — [R-Massive](https://zine.r-massive.com/?p=5980)

## 8. Famous recordings that verifiably used each machine, with published step charts

### Takeaway
I found specific-record evidence for the MPC60 (DJ Shadow's *Endtroducing.....*) and the Drumtraks (Daft Punk's "Short Circuit"; Tame Impala's *Currents* album). I found no published step charts for any of them. I found no recordings with named-track evidence for the TOM, XE8 or XR10.

### Cited Findings
- **MPC60 — DJ Shadow, *Endtroducing.....* (1996)**
  - "The producer used an MPC60 MKII to create his influential 1996 album *Endtroducing*." The source cited is Greg Rule, "DJ Shadow + Akai MPC = History", *Keyboard*, Oct 1997 — [Wikipedia: MPC60](https://en.wikipedia.org/wiki/MPC60)
  - RBMA says it "was produced entirely on the MPC60" — [RBMA](https://daily.redbullmusicacademy.com/2017/11/mpc-instrumental-instruments)
  - SOS says "with little more than an MPC60 II" — [Sound On Sound](https://www.soundonsound.com/music-business/akai-mpc60-revisited)
  - Its drums are sampled breaks, so the MPC60 is the sampler and sequencer here, not a fixed drum kit.
- **MPC60 — artist-level users, no specific records cited**
  - Sound On Sound: Level 42, Erasure, Hall & Oates, Prince (pop); Dr Dre, J Dilla, MF Doom, DJ Premier, De La Soul, Warren G, Ice Cube, Public Enemy, DJ Mike Magic (hip-hop) — [SOS](https://www.soundonsound.com/music-business/akai-mpc60-revisited)
  - Vintage Synth Explorer: Apollo 440, BT, Jean-Michel Jarre, Jimmy Edgar, Jermaine Dupri, A Guy Called Gerald — [vintagesynth](https://vintagesynth.com/akai/mpc60)
  - RBMA: Prince Paul, MC Dalek — [RBMA](https://daily.redbullmusicacademy.com/2017/11/mpc-instrumental-instruments)
- **Drumtraks — Daft Punk, "Short Circuit" (from *Discovery*, 2001)**
  - Wikipedia cites a 2006 *Remix* magazine article ("ROBOPOP") — [Wikipedia: Drumtraks](https://en.wikipedia.org/wiki/Drumtraks)
- **Drumtraks — Tame Impala, *Currents* (2015)**
  - The album only, citing a 2016 Hypebeast interview; no track is named — [Wikipedia: Drumtraks](https://en.wikipedia.org/wiki/Drumtraks)
- **Drumtraks — artist-level users:** Orbital, Freddy Fresh and Prince, with no tracks named — [vintagesynth](https://vintagesynth.com/sequential-circuits/drumtraks)
- **TOM:** no musicians or recordings are named on Vintage Synth Explorer or in the reviews read — [vintagesynth](https://www.vintagesynth.com/sequential-circuits/tom); [muzines 11797](https://www.muzines.co.uk/articles/sequential-tom/11797)
- **XR10:**
  - The only named people on Vintage Synth Explorer are forum posters and video creators — [vintagesynth](https://vintagesynth.com/akai/XR10)
  - Hollow Sun names only the styles that inspired the sounds (Peter Gabriel-style gated toms, Robert Palmer-style kicks and snares, Jam and Lewis-style sounds, Simmons kit). These are not users — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/xr10/index.html)
- **XE8:** no users named — [Hollow Sun](https://hollowsun.com/nostalgia/vintage/xe8/index.html)

### Inferences
- The Wikipedia claims for the Drumtraks rest on magazine citations I could not open, so they count as medium-confidence secondary evidence.

### Gaps
- **Search cut short.** The shared web-search quota for this session ran out midway, so I could not run planned searches on:
  - Jam & Lewis / Janet Jackson and the MPC60
  - DJ Premier or Gang Starr tracks
  - Drumtraks hit records
  - any step charts or transcriptions of these grooves
- **No grids.** No step chart for any listed recording was found, so every grid is null. None was reconstructed.

## 9. Free, clearly licensed MIDI pattern files for these machines

### Takeaway
None found. This topic was not searched thoroughly, because the search quota ran out.

### Cited Findings
- No source I read offered machine-specific MIDI pattern files with a clear licence. The XR10 preset patterns exist only as on-board ROM data, and the Drumtraks factory patterns exist only as SysEx/cassette memory dumps — [XR10 manual p.5](https://www.polynominal.com/akai-xr10/assets/files/akai-xr10-manual.pdf); [Drumtraks manual, "400 MIDI" p.2-6](https://vintagesynth.com/sites/default/files/2017-05/DrumtraksOperationsManual.pdf)

### Inferences
- The Drumtraks SysEx dump format is fully documented (Tables 2-7: song/pattern pointers, 2-3 byte note events with accent, volume and pitch). A real factory-memory dump, if one turns up, could in principle be decoded into MIDI. The XR10's "Bulk Dump" SysEx format is not documented in its manual.

### Gaps
- **Not searched.** Free MIDI libraries (for example on GitHub or Archive.org, or under CC licences) were not searched, because of the quota.

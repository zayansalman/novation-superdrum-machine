# Pattern files for `beat_clips.py`

Put your own step-grid patterns here as JSON files, and `python3 superdrum/beat_clips.py` turns them into
MIDI clips for every kit of the machine. Pattern files are git-ignored by default. Only commit patterns you
have the right to share.

## Format

A file holds a list of machines:

```json
[
  {
    "machine": "Roland TR-808 Rhythm Composer",
    "pack_folders": ["Roland TR-808"],
    "tracks": [
      {
        "artist": "Example Artist",
        "title": "Example Track",
        "bpm": 120,
        "pattern_confidence": "chart",
        "patterns": [
          {
            "section": "main groove",
            "time_signature": "4/4",
            "steps_per_bar": 16,
            "bars": 1,
            "swing_percent": 50,
            "lanes": {
              "Kick":       "X...x...X...x...",
              "Snare":      "....X.......X...",
              "Closed Hat": "x.x.x.x.x.x.x.x."
            }
          }
        ]
      }
    ]
  }
]
```

- `machine` must match an entry in `research/machine-setups/`.
- Each lane is a string with one character per step: `X` for an accented hit, `x` for a normal hit, `.` for
  a rest. The length must equal `bars × steps_per_bar`.
- Lane names: Kick, Kick 2, Snare, Snare 2, Rim, Clap, Snap, Closed Hat, Pedal Hat, Open Hat, Low Tom,
  Mid Tom, High Tom, Low Conga, Mid Conga, High Conga, Low Bongo, High Bongo, Timbale, Cowbell, Agogo,
  Clave, Wood Block, Shaker, Cabasa, Tambourine, Triangle, Guiro, Crash, Ride, Cymbal, Accent.
- `pattern_confidence` is `"chart"`, `"tab_or_notation"` or `"description"`. A `"description"` pattern
  gets "(approx)" in its clip name.
- Use 12 steps per bar for triplet or shuffle feels. Set `swing_percent` (50 means straight) to swing the
  even 16ths.

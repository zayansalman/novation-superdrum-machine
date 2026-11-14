# Contributing

Thanks for helping make these kits more faithful to the real machines.

## Reporting a wrong kit

Open an issue that includes:

- the kit name, as it appears in Live;
- what is wrong: pad order, a pad name, a missing choke group, or a sample on the wrong pad;
- a source, if you have one: a manual page, service notes, a review, or a recording of the hardware.

## Fixing a machine's layout

Each machine is one entry in `research/machine-setups/<maker>.json`. The fields that drive the build are:

| Field | Meaning |
|---|---|
| `machine` | The machine's full name |
| `pack_folders` | The sample-pack folder names this machine's kits are built from |
| `voices` | Voices in panel order: `label` (as printed), `name`, `type` (Kick, Snare, Tom, Closed Hat, ...) |
| `choke_groups` | Lists of voice labels that cut each other off |
| `built_in_effects` | The machine's effects, if any |
| `sources` | Where the information comes from |

After editing, rebuild the affected kit and run the audit:

```bash
python3 superdrum/build_kits.py "Pack Folder Name"
python3 superdrum/audit.py
```

## Fixing a sample's label

Sample labels live in `data/sample_labels.json`, keyed by path relative to the packs folder. Set `type`,
and set `source` to say how you know (`"official list"`, `"file name"` or `"by ear"`).

## Code

- Keep functions small, and keep changes focused: one fix per pull request.
- Every writer reads its output back and checks it. Keep those checks passing, and add one for anything new.
- Never commit samples, Ableton factory content, or transcribed patterns from third-party sources.

## Pull requests

1. Fork the repository and create a branch.
2. Make the change, then rebuild and run the audit.
3. Open a pull request that describes what changed and links your source.

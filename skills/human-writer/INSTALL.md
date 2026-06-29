# Installation — Human Writer (ChatGPT / Codex) skill

This is the ChatGPT/Codex edition of the `human-writer` skill. It ships in the
Codex skill format: a `SKILL.md` manifest, an `agents/openai.yaml` agent
descriptor, a `references/` doctrine set, and a `scripts/` analyzer. It covers
**English and French** in one skill.

## Prerequisites

- A Codex / ChatGPT agent runtime that loads skills from a skills directory
- Python 3.10+ on your system (required for the analyzer script)
- `pip` for installing one mandatory dependency
- A terminal with `unzip` (macOS, Linux) or PowerShell with `Expand-Archive` (Windows)

## Installation

Place the `human-writer/` directory inside your agent's skills directory. For a
Codex setup that reads from `~/.codex/skills/`:

### macOS / Linux

```bash
# 1. Create the skills directory if it doesn't exist
mkdir -p ~/.codex/skills

# 2. Unzip (or copy) the skill into that directory
unzip human-writer.zip -d ~/.codex/skills/

# 3. Install Python dependencies
pip install --user -r ~/.codex/skills/human-writer/requirements.txt
# pyyaml is required; httpx is optional (only for --external mode)

# 4. Verify the structure
ls ~/.codex/skills/human-writer/
# Expected: SKILL.md  README.md  INSTALL.md  requirements.txt  agents/  references/  scripts/

# 5. Make the analyzer script executable (optional, for convenience)
chmod +x ~/.codex/skills/human-writer/scripts/analyze.py
```

### Windows (PowerShell)

```powershell
# 1. Create the skills directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills"

# 2. Unzip the skill into that directory
Expand-Archive -Path .\human-writer.zip -DestinationPath "$env:USERPROFILE\.codex\skills\"

# 3. Install Python dependencies
pip install --user -r "$env:USERPROFILE\.codex\skills\human-writer\requirements.txt"

# 4. Verify the structure
Get-ChildItem "$env:USERPROFILE\.codex\skills\human-writer\"
```

If your runtime reads skills from a different path, copy the `human-writer/`
directory there instead. The skill itself is path-agnostic; only the install
location changes.

## First test

### Test the analyzer directly

The analyzer is a standalone CLI. It accepts input from `--input <file>` or
stdin, requires `--lang` (`en` / `fr`) and `--type`, and emits either JSON
(default) or a human-readable report (`--format human`).

```bash
cd ~/.codex/skills/human-writer

python3 scripts/analyze.py \
  --input path/to/your-draft.md \
  --lang en \
  --type marketing \
  --format human
```

Expected output: a header showing the score, top tells, and recommendations. An
AI-flavored draft (clichés, tricolons, spaced em-dashes) should land at
HIGH_RISK or CRITICAL (≥ 50); clean human prose should land at LOW_RISK (≤ 25).

### Quick smoke test (no draft needed)

Point the analyzer at one of the shipped doctrine files to confirm it runs
offline:

```bash
cd ~/.codex/skills/human-writer
python3 scripts/analyze.py \
  --input references/tells-stylistic-en.md \
  --lang en \
  --type marketing \
  --format human
```

Expected: a report prints with no error and no network call. (Catalog files
cite many tells by design, so the score itself is not meaningful here — this
only confirms the analyzer works.)

## Optional: external detector setup

The `--external` flag dispatches to one of Copyleaks, GPTZero, or
Originality.ai. To use it:

1. Install `httpx` (already in `requirements.txt`).
2. Obtain an API key from the provider and export it as an environment variable:

```bash
export COPYLEAKS_EMAIL="..."        # Copyleaks needs email + key (two-step auth)
export COPYLEAKS_API_KEY="..."      # for --external copyleaks
export GPTZERO_API_KEY="..."        # for --external gptzero
export ORIGINALITY_AI_API_KEY="..." # for --external originality
```

3. Invoke:

```bash
python3 scripts/analyze.py \
  --input draft.md \
  --lang en \
  --type marketing \
  --external copyleaks \
  --format human
```

**Provider notes:**
- **Copyleaks:** two-step auth (login with email + key → access token → Bearer on
  the detector call), response parsed at `summary.ai`. Requires BOTH
  `COPYLEAKS_EMAIL` and `COPYLEAKS_API_KEY`. Minimum input is ~255 characters
  (shorter text returns a 400, surfaced as an error, not a crash).
- **GPTZero / Originality.ai:** paid-only APIs. Their endpoints and
  response-parsing JSON paths in `call_gptzero` / `call_originality` are
  best-effort reconstructions from public docs, each with an inline `# (verify)`
  comment.

If `httpx` is not installed, `--external` dispatch raises `ImportError` cleanly
without breaking the analyzer's local scoring.

## Updating the skill

Replace the directory:

```bash
# macOS / Linux
rm -rf ~/.codex/skills/human-writer
unzip human-writer.zip -d ~/.codex/skills/
pip install --user -r ~/.codex/skills/human-writer/requirements.txt
```

Your customizations to `scripts/rules.yaml` (vocab lists, thresholds) will be
lost. If you want to preserve them, fork the skill locally before updating.

## Troubleshooting

**Analyzer fails with `ModuleNotFoundError: No module named 'yaml'`.**
`pyyaml` is mandatory. Install with `pip install --user pyyaml`.

**Analyzer fails with `ModuleNotFoundError: No module named 'httpx'` when using `--external`.**
`httpx` is optional and only needed for external detector dispatch. Install with
`pip install --user httpx`. Without `--external`, the analyzer runs fully offline.

**Analyzer flags legitimate human prose as AI (false positive).**
Run `--format human` to see which detector flagged it, then either loosen the
threshold in `scripts/rules.yaml` for that detector or add the flagged construct
to a project-specific allowlist.

**Python 3.10+ syntax errors.**
`analyze.py` uses `from __future__ import annotations` and PEP 604 union syntax
(`int | None`). On Python 3.8 or 3.9 this will fail. Upgrade Python.

## Skill content overview

For the full skill layout, see [`README.md`](README.md).

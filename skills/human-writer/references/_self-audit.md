# Self-audit of `references/*.md` against `scripts/analyze.py`

> Why a doctrine file flags itself, and which findings are actionable.

Last run: 2026-06-02. Non-catalog files scored with their own `--type`; catalog files with `--type technical`.

| File | Score | Verdict | Class |
|---|---|---|---|
| `adapter-technical.md` | 11 | LOW | adapter (fixed) |
| `adapter-marketing.md` | 23 | LOW | adapter (fixed) |
| `adapter-editorial-seo.md` | 20 | LOW | adapter (fixed) |
| `adapter-short-comms.md` | 10 | LOW | adapter (fixed) |
| `checklists.md` | 3 | LOW | adapter (fixed) |
| `external-detectors.md` | 12 | LOW | adapter (fixed) |
| `humanization-techniques.md` | 22 | LOW | mixed (fixed) |
| `tells-statistical.md` | 28 | MEDIUM | catalog (accepted) |
| `tells-structural.md` | 37 | MEDIUM | catalog (accepted) |
| `tells-stylistic-en.md` | 42 | MEDIUM | catalog (accepted) |
| `tells-stylistic-fr.md` | 42 | MEDIUM | catalog (accepted) |

## The two classes

**1. Catalog files (accepted at MEDIUM).** `tells-stylistic-en.md` / `tells-stylistic-fr.md` / `tells-structural.md` / `tells-statistical.md` ARE the canonical lists of suspect vocabulary, AI constructions, em-dash conventions, and structural markers. By design they cite every detected pattern many times. `tells-stylistic-en.md` contains 170 em-dashes and `journey` x9, `embark` x7, etc. The analyzer cannot tell a citation ("here is a pattern AI overuses") from a usage ("look at this seamless integration"). The whole file is effectively one big citation, so wrapping it in ignore markers would wrap ~90% of the content for no benefit.

**Disposition: accept as-is. Do NOT rewrite.** Their score is a structural artifact, not a quality signal.

**2. Explanatory files (fixed, now LOW_RISK).** The 7 adapter / checklist / technique / external-detector files explain *when and how to apply* the doctrine. Their MEDIUM scores were a mix of two things: genuine em-dash drift in the explanatory prose, and intentional citations of bad examples. Both were resolved (commits `95e7b75`, `2ccc7ae`):

- **Genuine drift fixed by rewording.** The prose itself overused em-dashes (`adapter-technical` had 43) while teaching against them. Replaced with commas / colons / semicolons / periods. Unironic suspect vocab in the doctrine's own voice reworded to plain English.
- **Intentional citations wrapped in ignore markers** (see below). Bad-example blockquotes, anti-pattern bullet lists, suspect-vocab tables, and deliberately-AI "Before" worked examples are teaching material; they SHOULD contain tells. They are now exempt from scoring.

## The ignore-marker mechanism

`analyze.py` (`strip_non_prose`, commit `1e9979f`) removes two kinds of non-prose before any detector runs:

1. **Fenced code blocks** (```` ``` ````): honors the prose-only contract documented in `adapter-technical.md` § "Code blocks and non-prose are exempt".
2. **Opt-in ignore regions**, for citing bad examples without self-flagging:

```
<!-- human-writer:ignore-start (short reason for the exemption) -->
...intentionally AI-flavored example, or a quoted list of tells...
<!-- human-writer:ignore-end -->
```

The start marker tolerates a trailing annotation between the marker name and `-->`. Use this in any doctrine file (or any user draft that quotes AI examples, e.g. a "how to spot AI writing" article). Markers must balance: one `ignore-end` per `ignore-start`.

## Self-audit discipline

- **User-facing artifacts** (README.md, INSTALL.md, public docs) MUST score ≤ 25. Enforced in commit `39f452d`.
- **Explanatory references** MUST score ≤ 25. Use ignore markers for citations, reword genuine drift. Re-check on any edit.
- **Catalog files** score ≥ 25 by design; accepted, do not rewrite.

## How to verify

```bash
for f in references/*.md; do
  base=$(basename "$f")
  if [[ "$base" == *"-fr"* ]]; then lang=fr; else lang=en; fi
  score=$(python3 scripts/analyze.py --input "$f" --lang "$lang" --type technical \
    | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{d[\"ai_probability_score\"]:3d}/100  {d[\"verdict\"]:13s}')")
  printf "%-40s %s\n" "$base" "$score"
done
```

(Use each non-catalog file's own `--type` for an exact read; `technical` is a quick uniform sweep.)

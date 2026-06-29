# Human Writer — a ChatGPT / Codex skill (EN + FR)

A skill for ChatGPT / Codex agents that produces prose reading as human-authored, sanitizes AI drafts to remove detector tells, and scores any draft for AI-detection risk before publication. It covers **English and French** in a single skill.

This is the ChatGPT/Codex edition. It ships in the Codex skill format (`SKILL.md` + `agents/openai.yaml` + `references/` + `scripts/`) and auto-activates on humanization, cleanup, and audit requests.

## Why this skill exists

Modern GPT-class output is fluent enough to ship, but it carries fingerprints that commercial detectors (Copyleaks, GPTZero, Originality.ai) latch onto. A draft goes out, someone runs it through a detector, the score comes back at 70%+, and it's rejected. The fix is a disciplined sweep of the specific tells detectors weight. This skill encodes that doctrine plus a deterministic analyzer so any agent session can produce, clean, or audit prose to a target score before delivery.

The tells cluster in three families:

- **Statistical:** low burstiness (flat sentence-length variance), narrow type-token ratio (language-agnostic).
- **Stylistic:** the same few dozen inflated phrases repeated across drafts ("delve", "leverage", "seamless", "robust" / "tirer parti de", "robuste", "incontournable"), formulaic frames ("It's not just X, it's Y" / "Il ne s'agit pas seulement de X").
- **Structural / typographic:** header pyramids, syndetic tricolons ("X, Y, and Z"), the em-dash "—" overused as the single strongest English tell, and — on the French side — the tiret cadratin "—" where native French uses commas or parentheses, plus de-accented prose.

## What it can do

**Three modes:**
- **Write:** produce new content already engineered to score LOW_RISK.
- **Clean:** rewrite an existing AI draft to strip tells, preserving meaning.
- **Audit:** score a draft, surface the top offending tells, recommend fixes without rewriting it.

**Two languages, fully specialized:** English (`en`) and French (`fr`), each with its own suspect-vocabulary list, AI-construction regex bank, and tricolon detector. French adds a dedicated **accent-stripping** typography detector calibrated NOT to false-fire on clean native prose.

**Four content-types** (each with its own adapter): marketing long-form, short-form comms, technical docs, editorial-SEO.

**Optional external integration:** live scoring via Copyleaks, GPTZero, or Originality.ai (`--external <provider>`). Lazy `httpx` import, so the analyzer works fully offline.

## What's inside

```
human-writer/
├── SKILL.md                          # Orchestration hub: routing + master checklist + anti-patterns
├── README.md                         # This file
├── INSTALL.md                        # Installation instructions
├── requirements.txt                  # pyyaml (required) + httpx (optional)
├── agents/
│   └── openai.yaml                   # Codex agent manifest (display name, default prompt, invocation policy)
├── references/
│   ├── tells-stylistic-en.md         # ⭐ EN suspect vocab + AI constructions + typography
│   ├── tells-stylistic-fr.md         # ⭐ FR suspect vocab + AI constructions + accent doctrine
│   ├── tells-statistical.md          # burstiness / TTR (language-agnostic)
│   ├── tells-structural.md           # bullets / headers / tricolons / emoji
│   ├── humanization-techniques.md    # the ten humanization moves (EN + FR worked examples)
│   ├── adapter-marketing.md          # marketing long-form adapter
│   ├── adapter-short-comms.md        # short-form comms adapter
│   ├── adapter-technical.md          # technical-docs adapter (prose-only contract)
│   ├── adapter-editorial-seo.md      # editorial-SEO adapter
│   ├── external-detectors.md         # Copyleaks / GPTZero / Originality.ai integration notes
│   ├── checklists.md                 # pre-publish checklists
│   └── _self-audit.md                # why doctrine files flag themselves; ignore-marker mechanism
└── scripts/
    ├── rules.yaml                    # ⭐ vocab + constructions + thresholds (en + fr)
    └── analyze.py                    # ⭐ deterministic scorer (tricolon + accent-stripping)
```

## The analyzer

`scripts/analyze.py` is a deterministic scorer that runs offline. It loads `scripts/rules.yaml` (vocab lists, regex patterns, thresholds) and emits a 0-100 score plus a list of flagged tells.

```bash
# Audit mode (default, JSON output for tooling)
python3 scripts/analyze.py --input draft.md --lang en --type marketing

# Human-readable report
python3 scripts/analyze.py --input draft.md --lang fr --type editorial-seo --format human

# Pipe via stdin
cat draft.md | python3 scripts/analyze.py --lang en --type technical --format human
```

Required flags: `--lang` (`en` / `fr`), `--type` (`marketing` / `short-comms` / `technical` / `editorial-seo`). `--input` is optional; stdin otherwise.

**Score bands** (4-band, canonical):
- `0-25` **LOW_RISK:** ship it.
- `26-49` **MEDIUM_RISK:** apply the top 3 recommendations, re-score.
- `50-74` **HIGH_RISK:** in WRITE mode restart; in CLEAN mode apply a stronger rewrite.
- `75-100` **CRITICAL:** major rewrite.

**Detectors implemented:** em-dash density, sentence-length stdev (burstiness), TTR (lexical diversity), suspect-vocabulary, AI-construction regex bank, tricolon, bullet parallelism, header pyramid, and the French-only **accent-stripping** detector (low-weight, word-count guard, calibrated below the native-prose accent floor).

**Prose-only scoring.** The analyzer strips fenced code blocks, markdown data tables, and opt-in ignore regions before scoring. Wrap any intentionally AI-flavored citation so it doesn't count against you:

```
<!-- human-writer:ignore-start (citation of a bad example) -->
In today's fast-paced world, leverage our robust and seamless solution.
<!-- human-writer:ignore-end -->
```

## How to invoke

Once installed, the skill auto-activates on prose requests. Example prompts:

- "Write a 600-word blog post that reads human, not AI"
- "Clean this AI draft so its Copyleaks score drops under 25"
- "Audit this email for AI tells before I send it"
- "Humanize this, it sounds too much like ChatGPT"
- "Réécris cet article en français pour qu'il ne fasse pas IA"

If auto-activation misses, force it: "Use the `human-writer` skill to..."

## What's NOT inside

- **Document structure** (which sections, which schemas, which headings): use a dedicated structure/content tool. This skill is the stylistic filter applied on top of whatever produces the structure.
- **Technical SEO audit of a web project:** use a dedicated SEO tool. This skill handles content style only.

This skill is a stylistic filter invoked on top of structure-producing tools, never as a replacement.

## Part of the mr-bridge.com toolkit

This skill is part of the [mr-bridge.com](https://mr-bridge.com) toolkit for scraping, data, and content automation. Related resources:

- [mr-bridge.com](https://mr-bridge.com) — home
- [Scrapers](https://mr-bridge.com/scrapers) — the Apify Actor portfolio
- [MCP servers](https://mr-bridge.com/mcp-servers) — Model Context Protocol servers
- [AI workflows](https://mr-bridge.com/ai-workflows) — agents and automation
- [Studies](https://mr-bridge.com/studies) — data studies and one-pagers
- [Articles](https://mr-bridge.com/articles) — write-ups and guides
- [Solutions](https://mr-bridge.com/solutions) — end-to-end solutions

## License

Personal use. Customize freely. No warranty. The external-detector endpoints in `analyze.py` carry `# (verify)` markers where they were reconstructed from public docs rather than live-verified.

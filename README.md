# Human Writer - English and French (ChatGPT / Codex)

Make English or French AI text read as human-authored, and audit any draft with a **deterministic 0-100 AI-detection score** before you publish. A ChatGPT / Codex Agent Skill.

This is the bilingual English + French master (the original `human-writer` skill), packaged for ChatGPT / Codex. Per-language Claude editions live in the `human-writer-en`, `human-writer-fr`, and sibling repositories.

## Three modes

- **Write:** produce new English or French content already engineered to score low-risk.
- **Clean:** rewrite an existing AI draft to strip detector tells, preserving meaning.
- **Audit:** score a draft, surface the worst tells, and recommend fixes without rewriting it.

Four content types are supported (marketing long-form, short-form comms, technical docs, editorial-SEO), each with its own tolerances.

## Why it exists

Modern LLM output is fluent enough to ship but carries fingerprints that commercial detectors (Copyleaks, GPTZero, Originality.ai) latch onto: low burstiness, repeated vocabulary, formulaic frames, and typographic tells. A draft rejected at 70 percent or more does not need a rewrite from scratch; it needs a disciplined sweep of the specific tells the detectors weight. This skill encodes that doctrine for English and French and ships a scorer, targeting sub-25 percent AI-probability on Copyleaks and GPTZero.

## Language doctrine

- **English:** a suspect-vocabulary and AI-construction regex bank, tricolon detection ("X, Y, and Z"), and the em-dash (U+2014) as the single English typographic tell.
- **French:** an accent-stripping hard-check (missing accents are a strong French AI tell), the tiret cadratin (em-dash, U+2014) as a foreign tell, and EN-to-FR calques (tirer parti de, sans couture, robuste, actionnable).

## The analyzer

`scripts/analyze.py` is a deterministic 0-100 scorer that runs offline (it loads `rules.yaml`; optional live scoring via Copyleaks, GPTZero, or Originality.ai with `--external`). Pass `--lang en` or `--lang fr`.

```bash
python3 skills/human-writer/scripts/analyze.py --input draft.md --lang en --type marketing --format human
```

Score bands: 0-24 low-risk (ship it), 25-49 medium (apply the top fixes and re-score), 50-74 high, 75-100 critical.

## Installation

```bash
cp -r skills/human-writer ~/.codex/skills/
pip install -r skills/human-writer/requirements.txt   # pyyaml required, httpx optional
```

Or copy `skills/human-writer` into a project's `.codex/skills/` directory.

## Use it

Once installed, the skill auto-activates on English or French prose requests. Example prompts:

- "Humanize this draft (English or French) and audit it for AI tells"
- "Clean this AI text and bring its Copyleaks score under 25"
- "Score this article for AI-detection risk and tell me what to fix first"

Force activation: "Use the `human-writer` skill to ...".

## What is inside

The skill lives in [`skills/human-writer/`](skills/human-writer/): a `SKILL.md` (routing, master checklist, anti-patterns), a `references/` library (stylistic, statistical, and structural tells, humanization techniques, and per-content-type adapters), and `scripts/` (`rules.yaml` plus the `analyze.py` 0-100 scorer and its tests).

## License

See `LICENSE`.

---

Part of the **[mr-bridge.com](https://mr-bridge.com)** toolkit for scraping, data, and content automation:
[Scrapers](https://mr-bridge.com/scrapers) · [MCP servers](https://mr-bridge.com/mcp-servers) · [AI workflows](https://mr-bridge.com/ai-workflows) · [Studies](https://mr-bridge.com/studies) · [Articles](https://mr-bridge.com/articles) · [Solutions](https://mr-bridge.com/solutions)

---

*Part of the [MrBridge Agent Skills catalog](https://github.com/MrBridgeHQ/skills). Browse them all at [mr-bridge.com/skills](https://mr-bridge.com/skills).*

# External AI detectors: doctrine and integration

> Cross-checking the analyzer's heuristic score against a third-party AI
> detector (Copyleaks, GPTZero, Originality.ai) before publication.
> The analyzer is fast, deterministic, and free. External detectors are
> slower, opaque, and metered, but they're what the world will use to
> judge the text. Use both.

---

## 1. When to call an external detector

Use when:

- **High-stakes publication**: Google-indexed blog post, paying client
  deliverable, public newsletter, landing page meant to rank for SEO.
  The cost of a "this reads as AI" complaint is greater than the API spend.
- **Cross-check after refactor**: the analyzer score dropped to LOW_RISK
  (< 25/100) and you want one more independent signal before publishing.
- **Adversarial calibration**: you suspect the analyzer is missing
  something. For example, text scores low but feels off. An external detector
  trained on different signals may catch it.

Do NOT use when:

- **Every iteration of the REFACTOR loop.** Burns budget for no signal.
  External detectors are noisy; the analyzer is what you tune against
  during iteration.
- **Short-form content** (< 300 words). Most detectors give unreliable
  scores below ~250 words; the variance dominates the signal.
- **Exploration / brainstorm phase.** You haven't committed to the text
  yet. Wait until the draft is near-final.
- **You don't have a budget for it.** The skill works without any
  external detector. The analyzer + doctrine is the load-bearing part.

---

## 2. Provider comparison (as of 2026-05)

| Provider | URL | Pricing model | Strength | Weakness |
|---|---|---|---|---|
| **Copyleaks** | copyleaks.com/ai-content-detector | Pay-per-scan (credit packs) | Most mainstream in B2B / enterprise; what clients run against your deliverables | High false-positive rate on technical / translated / non-native English |
| **GPTZero** | gptzero.me | Subscription tiers (free + paid) | Educator-focused, transparent metrics (burstiness + perplexity), gives sentence-level breakdown | Lower accuracy on commercial / marketing content; weaker on FR |
| **Originality.ai** | originality.ai | Pay-per-scan (credit packs) | SEO / publisher focus, includes plagiarism + fact-check; what Google-adjacent agencies use | More aggressive flagging; false positives common on edited content |

**Triangulation rule of thumb**: if two of the three flag a draft as AI,
treat the draft as AI-flagged. If one flags and two don't, look at which
two agree with the analyzer's score and trust the majority.

---

## 3. API setup

### Getting keys

- **Copyleaks**: API Dashboard at `api.copyleaks.com/dashboard` (sign up free at `api.copyleaks.com/signup`). The credential is under **API Access Credentials**. You need **two values**: your account email AND the API key (a GUID).
  Free tier: ~250 credits/month. Paid: ~$10 / 1000 credits.
- **GPTZero**: register at `gptzero.me/api`, subscribe to a paid tier
  ($10/month "Essential" or $25/month "Premium"). API key on dashboard.
- **Originality.ai**: register at `originality.ai`, top up credits.
  Pay-per-scan, ~$0.01 per credit, 1 credit = 100 words.

Pricing changes; verify current rates at the time you sign up.

### Copyleaks auth model (verified 2026-06-02)

Copyleaks is NOT a static-key API. It uses a two-step flow, which is why `call_copyleaks` needs both `COPYLEAKS_EMAIL` and `COPYLEAKS_API_KEY`:

1. `POST https://id.copyleaks.com/v3/account/login/api` with `{email, key}` returns `{access_token}` (valid 48h).
2. `POST https://api.copyleaks.com/v2/writer-detector/{scanId}/check` with `Authorization: Bearer <access_token>` and `{text, sandbox}`. Synchronous; the response carries `summary.ai` (0..1) as the AI probability.

Facts confirmed by live-fire (2026-06-02, real non-sandbox scan):
- **`summary.ai` is the right field** (0.0 human .. 1.0 AI). A real scan of an AI-flavored sample returned `summary = {"human": 0.0, "ai": 1.0}`; `call_copyleaks` parses `summary.ai` correctly.
- **Minimum input ~255 characters.** Shorter text returns `400 Bad Request` — the server validates length before billing, so 139- and 26-character inputs both 400 even with no credits left. The dispatcher degrades this to `{"status": "error"}` rather than crashing, but audit longer drafts.
- `sandbox: true` returns the same response shape with simulated scores (`ai: 1.0`) and **consumes no credits** — use it to smoke-test the flow. `call_copyleaks(text, sandbox=True)`.
- **Free-tier credits are minimal.** A single real ~400-word scan exhausted the trial allowance; the next real call returned `402 Payment Required` (also degraded to `{"status": "error"}`). Budget paid credits before relying on `--external copyleaks` in a loop, and prefer `sandbox` for plumbing tests.

### GPTZero / Originality.ai — paused (paid-only)

Live-verification of `call_gptzero` and `call_originality` is **on hold**: neither has a usable free tier (GPTZero ~$10/month, Originality pay-per-scan), so the spend is not justified without a concrete need. Their endpoints and JSON paths stay best-effort reconstructions with inline `# (verify)` markers in `analyze.py`. Resume only if a subscription is taken: run one real `--format human` call, confirm the response shape, fix the JSON path if needed, remove the marker.

### Storing keys

Export the keys as environment variables (for example in your shell profile,
or a `.env` file your shell loads on startup):

```bash
# AI detector APIs (human-writer skill)
export COPYLEAKS_EMAIL=you@example.com   # Copyleaks needs email + key (two-step auth)
export COPYLEAKS_API_KEY=00000000-0000-0000-0000-000000000000
export GPTZERO_API_KEY=gz_...
export ORIGINALITY_AI_API_KEY=oai_...
```

Then reload your shell (or open a new one) and verify:

```bash
echo "${COPYLEAKS_API_KEY:0:6}..."   # should print first 6 chars
```

If a key is unset, the analyzer returns `{"status": "skipped_no_key"}` in
the `external_detector` block; it never crashes.

---

## 4. CLI usage

### Single provider cross-check

```bash
# Run the analyzer on a draft, attach Copyleaks score
python3 scripts/analyze.py \
  --input draft.md \
  --lang en \
  --type marketing \
  --external copyleaks \
  --format human
```

Output includes the analyzer block (score, tells, recommendations) AND a
final `External detector` block:

```
-- External detector --------------------------------------
provider: copyleaks  →  AI probability: 18.4%
```

### Triangulation across all three (manual loop)

```bash
# Run all three providers and dump just the external_detector block
for provider in copyleaks gptzero originality; do
  echo "=== $provider ==="
  python3 scripts/analyze.py \
    --input draft.md \
    --lang en \
    --type marketing \
    --external "$provider" \
    --format json \
  | jq '.external_detector'
done
```

### Quick "is it ready to publish?" check

```bash
SCORE=$(python3 scripts/analyze.py --input draft.md --lang en --type marketing \
        --external copyleaks --format json \
        | jq '.external_detector.ai_probability')
echo "Copyleaks AI probability: $SCORE"
# Manual judgement call — but typically < 0.25 = green, > 0.50 = revise
```

---

## 5. Interpreting scores

### Normalized output

Every provider's `ai_probability` is normalized to a single float in
**`[0.0, 1.0]`** where `1.0 = certainly AI`. The analyzer's own
`ai_probability_score` is on a **0–100 integer scale** — they are NOT the
same scale. Multiply the external probability by 100 to compare visually.

### Convention thresholds (rule of thumb)

| Range | Interpretation |
|---|---|
| `0.00 – 0.25` | Reads as human. Safe to publish. |
| `0.25 – 0.50` | Ambiguous. Acceptable if content type is "AI-shaped" (technical docs, structured reference); risky for editorial / marketing. |
| `0.50 – 0.80` | AI-leaning. Likely flagged by most clients. Revise. |
| `0.80 – 0.95` | High confidence AI. Refactor before publication. |
| `0.95 – 1.00` | Certain AI. Major rewrite needed. |

These are **rough conventions**. Real-world calibration varies by
provider and content type. Copyleaks's 0.5 ≠ GPTZero's 0.5. The
analyzer's deterministic 0–100 score is more stable across content types
than any external detector's "probability".

### Agreement vs disagreement (the load-bearing pattern)

| Analyzer score | External score | Interpretation | Action |
|---|---|---|---|
| High (≥ 50) | High (≥ 0.50) | Confirmed AI tells | Refactor (priority tells in `recommendations[]`) |
| High (≥ 50) | Low (< 0.25) | Analyzer false positive (likely); check for technical jargon flagged as suspect vocab | Investigate which detector to trust; usually external wins for publication decisions |
| Low (< 25) | High (≥ 0.50) | Adversarial / detector-fooled; external sees something analyzer doesn't | Re-read the text; rephrase suspicious paragraphs |
| Low (< 25) | Low (< 0.25) | Reads as human to both | Ship it |

**Disagreement is the signal**, not the score. When the two diverge, look
closer.

---

## 6. Cost considerations

| Provider | Per-scan cost (~2026-05) | Notes |
|---|---|---|
| Copyleaks | ~$0.0014 per 250 words | Cheapest per word for short content |
| GPTZero | ~$10/month for N scans | Flat-rate; cheaper at high volume |
| Originality.ai | ~$0.01 per 100 words | Includes plagiarism scan |

**Budget guidance for a typical publishing workflow:**

- 1 blog post (1500 words) cross-checked with Copyleaks = ~$0.008.
- 30 blog posts/month with Copyleaks = ~$0.25.
- Triangulating all 3 detectors per post triples that = ~$0.75, still
  trivial.

The real cost isn't the API; it's the **time spent acting on conflicting
scores**. Pick one primary detector (Copyleaks recommended for B2B
content) and only invoke the others when the primary disagrees with the
analyzer.

### Pre-publish only, not per iteration

The analyzer runs in milliseconds. External detectors take 2–10 seconds
per call. If the REFACTOR loop runs N times to get the analyzer below 25,
that's potentially N × 10s × 3 providers wasted on a draft still
changing. Run external detectors **once**, after the analyzer has
converged, as the final gate before publishing.

---

## 7. URL fetch workflow

**The skill NEVER fetches URLs from `analyze.py`.**
(no scraping from local IP), `httpx` in `analyze.py` is permitted ONLY
for outbound POSTs to the three detector endpoints. The script reads
input from `--input <file>` or stdin, nothing else.

If the user provides a URL to audit, the orchestrator (Claude itself,
not `analyze.py`) does the fetch via MCP:

```bash
# Step 1: Claude fetches the URL via Firecrawl / Tavily / Exa MCP
#   (in conversation, not in the script)
# → saves the cleaned markdown to /tmp/audit_input.md

# Step 2: pipe through the analyzer + external detector
python3 scripts/analyze.py \
  --input /tmp/audit_input.md \
  --lang en \
  --type editorial-seo \
  --external copyleaks \
  --format human
```

The split is intentional: scraping policy and detector policy are
orthogonal concerns. The analyzer's `httpx` whitelist is narrow on
purpose.

---

## 8. Limitations of external detectors

All three (Copyleaks, GPTZero, Originality.ai) have well-documented
failure modes.

### False positives (flagging human text as AI)

- **Technical writing with formulaic structure.** RFCs, postmortems,
  Apify Actor READMEs all trigger "AI-shaped" features regardless of
  authorship.
- **Non-native English / non-native French.** Translated and ESL writing
  carries hallmarks (regularized sentence length, restricted vocabulary,
  formal register) that overlap with AI signatures.
- **Highly structured docs.** Markdown with deep heading hierarchies and
  uniform bullet lists scores AI even when human-written.
- **Short text.** Under ~250 words the detectors are basically
  guessing.

### False negatives (missing actual AI text)

- **Heavily edited AI output.** Once a human rewrites 30%+ of the
  sentences, all 3 detectors lose signal fast.
- **Hybrid human + AI.** Paragraphs alternated between human and AI
  source confuse statistical detectors (burstiness becomes noisy).
- **AI text post-processed by another AI.** Paraphrase, "humanize"
  tools, or just round-tripping through a different model often defeats
  these detectors.
- **Older / niche models.** Detectors train on GPT/Claude outputs; text
  from less common models slips through.

### Why the analyzer + 1 external > either alone

The analyzer catches **lexical / structural / pattern** tells deterministically.
External detectors catch **statistical / perplexity** signals via ML
models trained on millions of samples. The two are complementary;
they fail in different directions. Use both, and trust the agreement
between them more than either score alone.

### Don't make publication decisions on a single tool

No detector is ground truth. If the analyzer says LOW_RISK, Copyleaks
says 0.18, and the text reads well to a human eye → publish. If two of
the three agree it's AI-flagged → revise. If you only have one signal,
treat it as **advisory**, not gating.

---

## See also

- `SKILL.md`: the routing table that decides when to invoke external
  detectors per content-type and mode (write / clean / audit).
- `scripts/analyze.py`: the `call_copyleaks`, `call_gptzero`,
  `call_originality`, and `call_external` dispatch functions.
- your environment variables: where the three API keys live.
- `references/checklists.md`: pre-publish checklist that references
  this doctrine for the "external cross-check" step.

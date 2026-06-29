# Adapter: Marketing Long-Form

> Doctrine for the `human-writer` skill, applied to marketing long-form: blog posts, README prose, landing pages, long-form newsletters. Loaded in addition to language-specific stylistic tells (`tells-stylistic-en.md` / `tells-stylistic-fr.md`).

Long-form marketing is the highest-risk content type for AI detection. It's also where AI tells matter most for brand: a single "transformative seamless solution" can torpedo a piece's credibility. Detectors and human readers both have more surface to work with; every paragraph is another sample.

---

## 1. What "marketing long-form" means here

| Attribute | Value |
|---|---|
| Word count | 500–2500 words (sometimes longer for white papers) |
| Purpose | Educate + persuade + qualify the reader |
| Channels | Blog posts, Apify README prose, landing page sections, white paper excerpts, long newsletters |
| Tone | Confident, helpful, opinionated, never neutral |
| Reader posture | Skimming first, then committing if hooked |
| Detection risk | High (Copyleaks/GPTZero are trained on a lot of marketing) |

This content-type is distinct from:

- **`editorial-seo`**: optimized for search rankings, structured for crawlers; marketing is structured for humans
- **`short-comms`**: emails, social posts, replies (≤ 300 words); marketing is sustained argument
- **`technical`**: API docs, runbooks, schemas; marketing is persuasive, not prescriptive

If the brief sits between two types (e.g. an SEO-optimized blog post), load both adapters and prefer the stricter rule when they conflict.

---

## 2. Tell priority ranking (marketing-specific)

Long-form gives every tell more room to land. Prioritize in this order when cleaning or auditing:

<!-- human-writer:ignore-start (quoted AI tells, cited not used) -->
1. **AI constructions (HIGHEST)** — "In today's fast-paced world", "It's not just X, it's Y", "Imagine if", "In an era where". Long form gives these constructions a stage. Readers also have more time to notice the pattern repeat.
2. **Suspect vocabulary** — every Tier-1 word that lands is a hit on detectors. Cap at **1 Tier-1 word per 300 words MAXIMUM**, and never in the first 100 words.
3. **Conclusion templates** — long content invites templated closes ("In conclusion", "Ultimately", "All things considered"). The conclusion is the second-most-scanned region of a marketing page.
<!-- human-writer:ignore-end -->
4. **Em-dash overuse**: cap at 4 per 1000 words (EN) / 2 per 1000 words (FR). Acceptable for rhetorical emphasis within cap.
5. **Bullet parallelism**: marketing uses bullet lists for feature comparisons; force asymmetry in verb choice and item length.
6. **Burstiness floor**: long form makes flat sentence lengths obvious. Variance must stay ≥ 8.

---

## 3. What's tolerated here (and why)

Marketing long-form is more permissive than `short-comms` or `technical` on these axes:

<!-- human-writer:ignore-start (quoted tells/anchors cited as examples, not used) -->
- **A few em-dashes for emphasis**: within the 4/1000 cap. A single emphatic dash in a 600-word piece reads as voice, not AI.
- **Section headers (H2/H3)**: long content NEEDS them for skimmability. Just break the pyramid: never `H2 → 3× H3 → 3× H3` symmetry. Mix counts: 0, 1, 2, 4 H3s under different H2s.
- **Some lexical repetition for thematic emphasis**: saying a product name 4× is fine; saying "innovative" 4× is not. Tier-1 vocabulary stays capped regardless of intent.
- **Anchor sentences sparingly**: "Here's why this matters" / "The catch?" / "One more thing" once or twice in 1500 words reads as a writer guiding the reader. Three times reads as a template.
- **Listicles with unusual counts**: 4, 6, 7. Avoid 3 (AI default) and 10 (SEO bait).
<!-- human-writer:ignore-end -->

---

## 4. Marketing-specific anti-patterns

Reject on sight. These are not optimizations; they are disqualifications.

<!-- human-writer:ignore-start (quoted AI tells, cited not used) -->
- **"In a world where..."** opener
- **"Imagine if..."** opener (variants: "Picture this", "Think about the last time you...")
- **Statistics with no source** — "80% of companies struggle with X" with no citation, no date, no link
- **Promise / proof / call-to-action template structure** — three identical-shape paragraphs followed by a CTA
- **Bullet-list-as-paragraph** — 4+ bullet lists per 1000 words signals AI scaffolding
- **"What you'll learn"** preview at the top of the post
- **"Key takeaways" box** at the end (or worse: floating in the middle as a TL;DR card)
- **Emoji-led section headers** — `🚀 Getting Started`, `✨ Features`, `💡 Pro Tip`
- **Quote callouts with no attribution** — pull-quotes are fine; anonymous pull-quotes are not
- **"This is just the beginning"** closing (variants: "The journey is only beginning", "We're excited to see what's next")
- **"Game-changer"**, **"unlock the power"**, **"take it to the next level"** — flag and rewrite
- **Three-paragraph rhythm** where every paragraph is 3–4 sentences
<!-- human-writer:ignore-end -->

---

## 5. Apify README prose, specific guidance

A common use case for marketplace listings. The `human-writer` skill owns the STYLE of the prose blocks; a structure-producing step owns the STRUCTURE (which sections, which schemas, which order).

What this means concretely:

- **Target the prose paragraphs** between schemas, code blocks, and tables. Those are where AI tells live.
- **First 2–3 paragraphs are scanned hardest** by both Apify Quality Score reviewers and prospective users. Keep AI constructions out of the intro completely.
- **Apify Quality Score** includes content quality as a factor; humanized prose improves the score, which improves Store ranking.
- **Sections that need prose attention:**
  - The hook / "Why use this Actor?" paragraph
  - The "How it works" narrative
  - The pricing section explainer (above the pricing table)
  - FAQ answers (1–3 sentences each, but they accumulate)
  - The Changelog entries (yes, even those; they're scanned)

Cross-reference: a structure-producing step produces the README shell; `human-writer` polishes the prose inside it. Run the analyzer with `--type marketing` on the rendered README before publishing.

**Apify-specific tells to watch:**

<!-- human-writer:ignore-start (quoted AI tells, cited not used) -->
- README intros that open with "In today's data-driven world..." — extremely common in the Apify Store, instantly recognizable
- "Whether you're a developer, a marketer, or a data scientist..." — generic audience hedging that signals AI
- "Unlock the power of [X]" — banned in any pricing or hook paragraph
- Pricing prose that explains the model with "Our innovative pay-per-event model empowers..." — say what events you charge and why, drop the framing
- "Seamless integration with Apify's robust platform" — never use "seamless" or "robust" in Apify README prose; both are heavily flagged
<!-- human-writer:ignore-end -->

Practical workflow for a README pass:

1. Extract every prose paragraph (skip code, tables, schemas) into a single working buffer
2. Run `analyze.py --type marketing` on the buffer
3. Fix the prose, paste it back into the README
4. Re-render and run `analyze.py` once more on the full README to catch context drift

---

## 6. Landing page tone calibration

Landing pages compress marketing into the smallest possible space, which amplifies every tell. One templated subhead can sink the whole page in detector eyes; there is no surrounding prose to dilute the signal.

<!-- human-writer:ignore-start (bullets quote forbidden/bad/better templates as examples) -->
- **Hero headline** — short, sharp, specific. Forbidden templates: "Transform your X", "The future of Y", "Reimagine Z", "The smarter way to Z", "Z, simplified".
- **Subhead** — concrete benefit, not abstract promise. Bad: "Streamline your workflow". Better: "Cut invoice processing from 4 hours to 20 minutes."
- **Feature blocks** — lead with the user outcome, not the tech. Bad: "Powered by AI". Better: "Catches duplicate entries before they hit your accounting system."
- **Social proof** — real names, real numbers, real companies. If you don't have permission, drop the section entirely. Faux-anonymized testimonials ("CTO at a Fortune 500") are worse than no testimonials.
- **CTA** — specific verb, not "Get Started" / "Learn More". Better: "See the pricing", "Try it on one URL", "Book a 15-min walkthrough".
- **FAQ block** — write answers as if speaking to one customer who just asked. Avoid "Great question!" openers and avoid restating the question in the answer.
- **Footer microcopy** — even legal-adjacent text ("Trusted by teams at...") counts as marketing prose and gets scanned. Keep it specific or remove it.
<!-- human-writer:ignore-end -->

---

## 7. Long-form blog post structure

The default AI shape is: introduction → 3 H2 sections → conclusion. Break it.

<!-- human-writer:ignore-start (bullets quote AI openers/closers as examples to avoid) -->
- **Open with a specific story, statistic, or question** — NOT with "In today's world". An opening anchored in a real moment (a date, a customer name, a number you observed) is the strongest single signal of human authorship.
- **Bury the thesis until paragraph 2 or 3** — let the reader earn the argument. AI defaults to thesis-in-paragraph-1.
- **Mix paragraph lengths aggressively** — alternate 1-sentence paragraphs with 5+ sentence paragraphs. Uniform 3-sentence paragraphs are an AI tell. The analyzer's burstiness score catches this; readers feel it before they can name it.
- **Asymmetric section counts** — three H2s of unequal depth, not three H2s of equal depth. One H2 with 600 words, one with 200, one with 50 — that's a human structure.
- **Include at least one tangent** — a 2–3 sentence digression that doesn't advance the argument but adds texture. AI almost never produces tangents; everything it writes serves the outline.
- **Hedge unevenly** — mix confident claims with explicit uncertainty. AI hedges everything at the same intensity ("could potentially", "may sometimes"). Humans say "I'm sure of X" and "I have no idea about Y" in the same paragraph.
- **End without a summary** — leave the reader with a question, a punchline, a concrete next step. No recap. No "key takeaways". No "in conclusion".
<!-- human-writer:ignore-end -->

---

## 8. Pre-publish checklist (10 items)

Paste this into the workspace and tick before delivery:

```markdown
- [ ] Ran `scripts/analyze.py --type marketing --lang <en|fr>` — score ≤ 25
- [ ] First 100 words contain zero AI constructions and zero Tier-1 suspect vocabulary
- [ ] No "In conclusion / Ultimately / All in all" close
- [ ] No bullet list longer than 8 items, and not more than 3 bullet lists per 1000 words
- [ ] At least 1 specific opinion or take in the piece (not a hedged "some argue that")
- [ ] At least 1 concrete number, named entity, or date in the piece
- [ ] Sentence length variance (stdev) ≥ 8 (analyzer green)
- [ ] Em-dash count ≤ 4 per 1000 words (EN) / ≤ 2 per 1000 (FR)
- [ ] No emoji used as section header
- [ ] No "Key takeaways" / "What you'll learn" block, no thesis-in-paragraph-1
```

If any item fails, fix before delivery. If the analyzer score is 26–49 after fixes, apply the top 3 recommendations and re-score. If 50+, restart the draft from a different angle; do not try to salvage.

---

## 9. Calibration with `analyze.py`

Marketing weights from `scripts/rules.yaml`:

```yaml
content_type_weights:
  marketing:     {statistical: 1.0, stylistic: 1.0, structural: 1.0}
```

All three axes weighted at **1.0**: full enforcement, no latitude. This is the strictest content-type calibration in the skill (compare with `technical` at 0.5/0.7/0.3, or `short-comms` at 0.6/1.2/0.5).

What this means in practice:

- Statistical signals (burstiness, sentence variance, lexical diversity, comma density) all count at full weight, no quarter for "but it's a blog, of course it's rhythmic"
- Stylistic signals (suspect vocabulary, AI constructions, em-dash density) count at full weight; every tier-1 word lands
- Structural signals (header pyramids, bullet parallelism, listicle counts) count at full weight; symmetric structure is penalized hard

Run order:

```bash
python3 scripts/analyze.py --input draft.md --lang en --type marketing --format human
```

Read the `recommendations[]` array in the JSON output and apply top-3 highest-severity items first. Re-run after each pass; fixing one tell often surfaces another that was masked by it. A typical clean pass drops a score from ~60 to ~15 in 2–3 iterations; if iteration 3 still scores above 30, restart from a different angle rather than continuing to patch.

---

## 10. Before / after worked examples

### Example 1: Apify Actor README intro (EN)

**Before (AI-flavored, ~80 words):**

<!-- human-writer:ignore-start (deliberately AI-flavored sample for teaching; must not self-flag) -->
> In today's fast-paced e-commerce landscape, businesses need to leverage robust data extraction tools to stay ahead. Our innovative scraper empowers you to seamlessly navigate the complex world of competitor pricing intelligence. Whether you're a small startup or an established enterprise, this Actor unlocks the full potential of automated price monitoring. Dive deep into actionable insights and transform your pricing strategy with our cutting-edge solution.

*Analyzer score: ~78 (CRITICAL). Hits: 5 Tier-1 words (leverage, robust, empowers, seamlessly, unlocks), 3 AI constructions ("In today's fast-paced", "Whether you're", "Dive deep into"), no concrete number, generic close.*
<!-- human-writer:ignore-end -->

**After (humanized, ~80 words):**

<!-- human-writer:ignore-start (quoted model output sample for teaching) -->
> Competitor pricing changes hourly on Amazon and Shopify. Most teams find out about a price war 48 hours late, when their conversion rate has already tanked. This Actor pulls competitor prices on a schedule you set — 15 minutes, 1 hour, daily — and pushes them to a dataset or webhook. It works on 90+ marketplaces tested in production, and it costs $0.40 per 1000 products scraped. The README below covers setup, schemas, and the three pricing modes available.

*Analyzer score: ~12 (LOW_RISK). Delta: −66. Specific numbers (48h, 15min, 90+, $0.40), one take ("Most teams find out... too late"), zero AI constructions, zero Tier-1 vocabulary.*
<!-- human-writer:ignore-end -->

---

### Example 2: Blog post opener (FR)

**Before (AI-flavored, ~70 mots) :**

<!-- human-writer:ignore-start (deliberately AI-flavored FR sample for teaching; must not self-flag) -->
> Dans un monde où la donnée est reine, il convient de tirer parti des outils de scraping pour libérer le potentiel de votre stratégie commerciale. Que vous soyez une PME ou un grand groupe, naviguer dans l'écosystème des données web peut sembler complexe. En effet, il s'agit de comprendre les enjeux pour embrasser pleinement cette transformation. Plongeons au cœur de cette révolution silencieuse.

*Analyzer score: ~82 (CRITICAL). Hits: 6 Tier-1 FR (dans un monde où, il convient de, tirer parti, libérer le potentiel, en effet, plongeons au cœur), 1 AI construction ("Que vous soyez ... ou"), pas de chiffre, ouverture cliché.*
<!-- human-writer:ignore-end -->

**After (humanisée, ~70 mots) :**

<!-- human-writer:ignore-start (quoted FR model output sample for teaching) -->
> Lundi dernier, un client m'envoie un CSV de 12 000 lignes. Le scraper qu'on avait monté en mars tournait toujours, mais 30 % des prix étaient faux : Shopify avait changé son markup HTML un mercredi soir, sans rien annoncer. Ce billet raconte comment on a détecté la dérive en quatre heures au lieu de quatre semaines, et pourquoi les "scrapers qui marchent" sont une fiction si vous ne surveillez pas leur sortie.

*Analyzer score: ~14 (LOW_RISK). Delta: −68. Ancrage temporel précis (lundi dernier, mars, mercredi soir), chiffres (12 000, 30 %, 4 heures vs 4 semaines), opinion ("une fiction"), zéro vocabulaire suspect.*
<!-- human-writer:ignore-end -->

---

### Example 3: Landing page subhead + feature blurb (EN)

**Before (AI-flavored, ~45 words):**

<!-- human-writer:ignore-start (deliberately AI-flavored sample for teaching; must not self-flag) -->
> Transform your data pipeline with our innovative, AI-powered platform. Seamlessly integrate with your existing stack and unlock the full potential of your analytics workflow. Whether you're a data scientist or a business analyst, our robust solution empowers you to navigate complex datasets with ease.

*Analyzer score: ~88 (CRITICAL). Hits: 5 Tier-1 (transform, seamlessly, unlock, robust, empowers, navigate — 6 actually), 1 AI construction (Whether you're), zero concrete claim.*
<!-- human-writer:ignore-end -->

**After (humanized, ~45 words):**

<!-- human-writer:ignore-start (quoted model output sample for teaching) -->
> Ship a working ETL job by Friday. We connect to Snowflake, BigQuery, and Postgres in under 4 minutes — measured, not promised. The free tier covers up to 5 million rows per month. If you need more, the Pro tier is $49/month with no per-row markup. Pricing page below.

*Analyzer score: ~9 (LOW_RISK). Delta: −79. Specific verb (Ship), real deadline (Friday), measured claim (4 minutes), real numbers (5M rows, $49), no Tier-1 vocabulary, no AI construction, opinionated CTA framing.*
<!-- human-writer:ignore-end -->

---

## See also

- `tells-stylistic-en.md`: full EN suspect vocabulary list and AI construction patterns
- `tells-stylistic-fr.md`: full FR suspect vocabulary list and AI construction patterns
- `tells-statistical.md`: burstiness, sentence variance, lexical diversity thresholds
- `tells-structural.md`: header pyramids, bullet parallelism, listicle counts
- `humanization-techniques.md`: rewrite strategies for CLEAN mode
- `checklists.md`: generic pre-publish self-review (this adapter's checklist is the marketing-specific overlay)
- a structure-producing step: owns README STRUCTURE (schemas, sections, pricing format); this skill owns the prose STYLE inside each section
- your CMS / SEO workflow: for pieces also optimized for search rankings; load `adapter-editorial-seo.md` in addition when both apply

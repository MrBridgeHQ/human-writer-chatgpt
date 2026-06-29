# Statistical AI Tells — Doctrine Reference

Internal doctrine. Loaded by the `human-writer` router in WRITE / CLEAN / AUDIT
mode regardless of target language. Complements the stylistic and structural
references; this one focuses on **measurable distributional properties** of
text rather than vocabulary or layout.

---

## 1. Why statistical tells matter

Large language models generate text by sampling from learned distributions.
That sampling is biased toward the mean of the training corpus on almost every
dimension that can be counted: sentence length, lexical reuse, punctuation
density, opener variety, paragraph shape. The result is text that is
*locally fluent* but *globally too regular*.

Human writing, in contrast, is irregular at every scale. People interrupt
themselves, drop fragments, recycle one specific word for emphasis while
varying others, write a 4-word sentence next to a 38-word one, and use
commas inconsistently.

Modern AI detectors (Copyleaks, GPTZero, Originality.ai, Turnitin, Winston AI,
ZeroGPT) lean heavily on these distributional metrics because they survive
paraphrase. You can rewrite every sentence and still trip a detector if the
underlying distribution of sentence lengths or function-word ratios remains
machine-like. That is why this file matters: stylistic cleanup alone is not
enough.

The companion script `scripts/analyze.py` measures the subset of these
properties that can be computed cheaply and deterministically. This file is
the **doctrine layer** — it explains the metrics, the thresholds, and the
concrete moves a writer makes to bring a draft into the human zone.

Rule of thumb: a draft that fails on two or more statistical metrics is
almost guaranteed to be flagged by at least one external detector, even if
every visible stylistic tell has been removed.

---

## 2. Burstiness — sentence-length variance

### Definition

Burstiness is the standard deviation of sentence lengths (counted in words)
across a passage. Some authors call it sentence-length variance or
sigma-sentence. The formula:

```
mean       = sum(sentence_lengths) / n
variance   = sum((length - mean) ** 2 for length in lengths) / n
stdev      = sqrt(variance)
```

`analyze.py` implements exactly this in `detect_sentence_stdev` (population
stdev, not sample stdev — the difference is negligible past 10 sentences).

### Why it matters

Humans alternate. They write a long meandering sentence that explains a
nuance, then drop a three-word punch, then go medium, then fragment. AI text
clusters around a comfortable middle — 15 to 22 words per sentence — because
that is where training data lives and where decoding heuristics feel safe.

Burstiness is the single most cited statistical feature in academic AI
detection literature (the "perplexity / burstiness" pair from GPTZero's
original paper). It is also the easiest to fix.

### Empirical thresholds

Calibrated for marketing-style English and French, 300 to 1500 words:

| stdev (words) | reading | action |
|---|---|---|
| `>= 8.0` | human-like | ok |
| `4.0 - 7.9` | AI-leaning | rewrite a few sentences for variance |
| `< 4.0` | strong AI signal | restructure paragraphs |

`analyze.py` uses `sentence_stdev_min = 8.0` for both EN and FR (see
`rules.yaml`). Severity escalates to `high` below `threshold / 2` (i.e. 4.0).

### How to write more burst-y

Concrete moves, in priority order:

1. **The 3-5 word drop.** After every 2 to 3 medium sentences, insert a 3-5
   word sentence. It can be a fragment, an aside, a verdict. "It works." /
   "Mais pas pour tout."
2. **The 25+ word stretch.** Every 3 to 4 medium sentences, give yourself
   permission to write one long sentence — 25 words or more — that piles
   subordinate clauses, parentheticals, or an actual list inside the prose.
3. **Intentional fragments.** Humans use sentence fragments freely. "Not
   ideal." "Three weeks later, nothing." "Ce qui change tout." A draft with
   zero fragments reads as machine output regardless of vocabulary.
4. **Unpredictable joining.** Resist the urge to glue every related pair with
   a semicolon or "and". Sometimes use the period; sometimes use the
   semicolon; sometimes split into three sentences where one would do.
5. **Resist the 18-22 word default.** When every sentence you write lands in
   that band, you are producing AI prose without realizing it. Watch your
   word counts as you draft.

### Examples

EN — bad (stdev ~1.0, three sentences of 5-6 words each):
> Wine pricing has changed. The market is volatile. Producers must adapt.

EN — good (stdev ~12, mix of 28 / 2 / 6 words):
> Wine pricing has shifted dramatically — Bordeaux 2016 sheds 8% in a week,
> while Burgundy 2020 holds firm against a softening en primeur campaign.
> Producers adapt. Or they lose distribution.

FR — bad (stdev ~1.5):
> Le marché du vin évolue. Les prix bougent. Il faut s'adapter.

FR — good (stdev ~11):
> Le marché du vin s'est durci en quelques semaines — Bordeaux 2016 perd 8%
> sur sept jours pendant que la Bourgogne 2020 tient bon malgré une campagne
> en primeur poussive. Les producteurs s'adaptent. Sinon, ils perdent leurs
> distributeurs.

---

## 3. Lexical diversity — Type-Token Ratio

### Definition

Type-Token Ratio (TTR) is the count of unique words divided by the total
word count:

```
TTR = unique_words / total_words
```

`analyze.py` implements this in `detect_ttr`, lowercasing tokens before
deduplication so "Wine" and "wine" count as one type.

### Why it matters

AI tends to recycle a small set of abstract nouns and connective phrases
across a piece: *experience, solution, platform, approach, however, moreover,
additionally, ultimately*. The repetition is not stylistic — it is
distributional. The model literally has higher probabilities for those tokens
once the topic is set.

Humans either use a wider vocabulary, OR repeat *specific concrete* terms
intentionally for rhythm or emphasis. The pattern differs: AI repeats
abstract glue; humans repeat concrete keystones.

### Thresholds

`analyze.py` uses `lexical_diversity_min = 0.45` for both EN and FR,
calibrated for 300-1500 word marketing copy:

| TTR | reading | action |
|---|---|---|
| `>= 0.45` | acceptable | ok |
| `0.27 - 0.44` | low diversity | rewrite repeated abstract nouns |
| `< 0.27` | severe | manual rewrite, likely template output |

Severity escalates to `high` below `threshold * 0.6` (i.e. 0.27).

### Caveat — TTR is length-dependent

Raw TTR is biased toward short texts. A 50-word passage almost mechanically
scores 0.7+; a 5000-word passage rarely passes 0.4 even when written by
gifted humans. This is a known limitation in the corpus linguistics
literature. Two better metrics exist:

- **MATTR** (Moving-Average Type-Token Ratio) — computes TTR over a sliding
  window of N tokens (typically 50) and averages. Length-invariant.
- **MTLD** (Measure of Textual Lexical Diversity) — walks the text and
  measures how far it takes for TTR to fall below 0.72; longer = more
  diverse. Also length-invariant.

`analyze.py` deliberately stays with raw TTR for now. The threshold 0.45 is
calibrated specifically for the 300-1500 word marketing band, which is the
skill's primary use case. If the writer's draft falls outside that band
significantly, treat the TTR reading as advisory rather than a hard flag.
A future iteration may add MATTR.

### How to increase lexical diversity

- **Stop reusing the same abstract noun in the same paragraph.** Track these
  five offenders: *experience, solution, platform, approach, journey* (and
  their FR equivalents: *expérience, solution, plateforme, approche,
  parcours*). One instance per paragraph, maximum.
- **Vary connectives.** Replace the *however / moreover / additionally /
  furthermore* cycle with *but / and / also*, or restructure to drop the
  connective entirely. In French: *cependant / par ailleurs / de plus* →
  *mais / et / aussi* or no connective.
- **Prefer concrete to generic.** "Bordeaux 2016" beats "the wines". "Tuesday
  morning" beats "recently". "12% margin compression" beats "significant
  pressure". Specificity bumps TTR and reads as human.
- **Re-read for echo.** When you spot the same word twice in three sentences,
  one of them is almost always replaceable.

---

## 4. Sentence-opening diversity

### Definition

Ratio of unique first-words across the sentences in a passage. If 10
sentences open with 10 different words, the diversity is 1.0; if 7 of them
open with "The", diversity is 0.4.

### Why it matters

AI defaults to a small set of openers: *The, This, While, Although, In, As,
For, By, With*. In French: *Le, La, Les, Cette, Bien que, Dans, Pour, En,
Avec*. A 12-sentence passage where 7 openers come from that list reads as
machine output even when the rest of the prose is clean.

### Implementation note

Not in `analyze.py` yet. May be added in a future iteration alongside
paragraph-stdev. For now, the doctrine layer asks the writer to enforce
this by eye.

### Manual guidance

- Cap reuse of the same opener at **2 sentences within any 10-sentence
  window**.
- Mix opener types: subject ("The X"), conjunction ("Because"), preposition
  ("In", "After"), adverb ("Quickly", "Honestly"), fragment ("Not always."),
  question ("Why does this matter?").
- When auditing a draft, scan the leftmost word of each sentence in
  isolation. If a column of "The" appears three times in a row, rewrite at
  least one.

---

## 5. Comma density

### Definition

Average number of commas per sentence across the passage. Computed as
`total_commas / sentence_count`.

### Why it matters

AI tends to over-comma. It piles clauses inside a single sentence —
"Bordeaux, which has historically led en primeur, faces pressure from
buyers, who increasingly turn to Burgundy, which offers tighter allocations,
and Champagne, which holds firm." That five-clause monster is high-comma
output. Humans break the same content into two or three shorter sentences.

### Thresholds

`rules.yaml` sets `comma_density_max = 2.0` for both EN and FR:

| commas / sentence | reading |
|---|---|
| `< 2.0` | human-like |
| `2.0 - 3.0` | watch — clausal piling starting |
| `> 3.0` | AI-clausal pattern, rewrite |

Note: comma density is not yet wired into `analyze.py`'s composite score.
It lives in `rules.yaml` for reference and may be promoted in a future
iteration. Use it as a manual audit step.

### How to reduce

- **The three-comma rule.** When a sentence carries 3 or more commas, split
  it into two sentences. The clause boundaries are usually obvious.
- **Replace comma-and-conjunction with a period.** "X is true, and Y also
  holds" → "X is true. Y also holds." This single move drops average comma
  count noticeably.
- **Parenthesize true asides.** Comma-bracketed asides ("Bordeaux, which is
  a region, ...") often read more naturally as parentheses or em-dashes (be
  careful with the em-dash budget — see section 8).
- **Drop the Oxford comma occasionally.** In English, optional. Mixing
  Oxford and non-Oxford within the same piece is, ironically, more human.

---

## 6. Paragraph-length distribution

### Definition

Standard deviation of paragraph lengths in words. A passage where every
paragraph is 70 to 100 words has very low paragraph-stdev. A passage where
one paragraph is 12 words, another is 240 words, and a third is 60 words
has high paragraph-stdev.

### Why it matters

AI produces shapely, uniform paragraphs. The default output is 3 to 5
sentences per paragraph, 60 to 100 words each, repeated for as many
paragraphs as needed. The visual rhythm on the page is the giveaway: every
block looks like every other block.

Humans vary paragraph shape constantly. A one-sentence paragraph for
emphasis. A 250-word paragraph when the argument needs space. A six-word
paragraph as a transition.

### Implementation note

Not in `analyze.py` yet. Planned for a future iteration alongside opener
diversity.

### Manual guidance

- Use **one-sentence paragraphs** for emphasis: a key claim, a transition,
  a punchline.
- Allow long paragraphs (6+ sentences, 150+ words) when the argument needs
  the breathing room — but never write three of them back to back.
- **Don't write five paragraphs of similar shape in a row.** This is the
  number one visual tell for editors who skim before they read.
- Aim for at least one paragraph in any 1000-word draft that is under 30
  words and at least one that is over 150.

---

## 7. Function-word frequency

### Definition

Function words are the closed-class glue tokens: *the, a, of, and, to, in,
is, that*. In French: *le, la, de, et, à, en, est, que*. Authorship-attribution
research from the 1960s onward has shown that function-word distributions
are remarkably stable per author and remarkably different between humans
and machine-generated text.

### Why it matters

AI has more uniform function-word frequencies across sentences than humans
do. Detectors like Originality.ai and ZeroGPT use function-word
distributions as one input to their classifiers.

### Implementation note

Not in `analyze.py`. Implementing it reliably requires a per-author baseline
or a large reference corpus; without that, the signal is noisy and easy to
trigger false positives on technical writing (which legitimately uses fewer
function words).

Mentioned here so the writer is aware that high-end detectors do look at
this dimension — which is one more reason to vary sentence structure
deliberately rather than templating from a single mental pattern.

---

## 8. Em-dash density (statistical view)

The vocabulary references already flag em-dashes as a stylistic tell. The
statistical angle is sharper.

Reference baseline from sampled corpora:

- Human published prose (literary essays, journalism): **~1 em-dash per
  1000 words**, often zero in a given piece.
- GPT-4-class output, default settings: **4 to 7 em-dashes per 1000 words**
  systematically.
- Claude output, default settings: similar range, often higher in long-form.

This is one of the strongest single-feature signals available. A 600-word
piece with 5 em-dashes is almost certainly machine-generated, regardless of
vocabulary.

`analyze.py` enforces this via `detect_em_dashes`:

- EN: `em_dash_per_1000_words = 4.0` (threshold above which the flag fires)
- FR: `em_dash_per_1000_words = 2.0` (stricter — em-dashes are rarer in
  native French and the marker is even more diagnostic)

Severity escalates to `high` above `threshold * 2`.

When in doubt, replace em-dashes with: commas, parentheses, full periods, or
restructure the sentence. Two em-dashes in a 600-word piece is the soft
ceiling.

---

## 9. Punctuation as fingerprint

Other punctuation-level signals worth tracking by eye, even though they are
not all wired into `analyze.py`:

- **Semicolon density.** AI uses semicolons at roughly 3 to 5 times the
  human rate in marketing prose. Audit any draft with more than 2 semicolons
  per 500 words.
- **Bold/italic markup density (markdown).** AI tends to bold or italicize
  3 to 5+ phrases per 500 words to signal "key concept". Humans mark up
  sparingly or not at all in flowing prose. Cap markup at 1-2 emphases per
  500 words in marketing copy.
- **Header density (markdown).** AI inserts H2/H3 every 100 to 150 words.
  Humans vary widely; some pieces have no headers at all, others use them
  as section dividers every 400+ words. The header-pyramid detector in
  `analyze.py` (see `detect_header_pyramid`) catches the most extreme case:
  multiple H2 blocks each containing exactly 3 H3s.
- **Bullet density.** Same logic. AI loves bullets. A 1000-word piece with
  4 bullet lists is suspicious; 1 or 2 is normal; 0 is fine.

---

## 10. How `analyze.py` operationalises these tells

Reference the actual code paths so a writer can trace from doctrine to
implementation:

| Doctrine section | Code path in `analyze.py` | Threshold key in `rules.yaml` |
|---|---|---|
| Burstiness (§2) | `detect_sentence_stdev` | `sentence_stdev_min` |
| Lexical diversity (§3) | `detect_ttr` | `lexical_diversity_min` |
| Em-dash density (§8) | `detect_em_dashes` | `em_dash_per_1000_words` |
| Bullet parallelism (§9) | `detect_bullet_parallelism` | `bullet_parallelism_max` |
| Header pyramid (§9) | `detect_header_pyramid` | (boolean, no threshold) |
| Sentence-opener diversity (§4) | not yet implemented | planned |
| Paragraph-length stdev (§6) | not yet implemented | planned |
| Comma density (§5) | not in score, advisory only | `comma_density_max` |
| Function-word frequency (§7) | not implemented | n/a |

The analyzer is deterministic, fast (sub-second on any normal draft), and
cheap to run. Always score your draft before delivering. The composite
score lives in `compute_score` and is bucketed by `verdict_bands`:

| score | verdict |
|---|---|
| 0 - 24 | `LOW_RISK` |
| 25 - 49 | `MEDIUM_RISK` |
| 50 - 74 | `HIGH_RISK` |
| 75 - 100 | `CRITICAL` |

Target `LOW_RISK` before delivering any piece to a client.

---

## 11. Calibration vs content type

Different content types tolerate different statistical profiles. The
content-type weights live in `rules.yaml` under `content_type_weights`:

| content type | statistical | stylistic | structural | notes |
|---|---|---|---|---|
| `marketing` | 1.0 | 1.0 | 1.0 | full enforcement, the default |
| `short-comms` | 0.6 | 1.2 | 0.5 | under 100 words, stdev naturally lower; weight statistical down, weight stylistic up |
| `technical` | 0.5 | 0.7 | 0.3 | technical vocabulary repetition is OK, headers and bullets are expected; relax everything |
| `editorial-seo` | 0.9 | 1.0 | 1.0 | full enforcement plus manual keyword density check |

What this means in practice for the writer:

- **Marketing long-form (default).** Hit stdev >= 8, TTR >= 0.45, em-dashes
  under 4/1000 EN or under 2/1000 FR, no header pyramids, no bullet
  parallelism above 0.80.
- **Short-form comms** (LinkedIn post, tweet thread, push notification).
  The stdev requirement relaxes because you cannot get high variance from
  3 sentences. Focus instead on vocabulary cleanliness and a punchy mix of
  short and very short sentences.
- **Technical docs** (README, API doc, runbook). TTR is allowed to drop
  because technical vocabulary is necessarily repetitive — you cannot
  rotate "endpoint" to a synonym every paragraph. Structural patterns
  (bullets, headers) are expected and not penalized.
- **Editorial-SEO** (long-form blog post, comparison article). Full
  enforcement, plus a manual pass for keyword density — search-targeted
  posts often inflate one keyword unnaturally; if it appears more than
  ~1.5% of total words, dilute.

---

## 12. Workflow — using this file in practice

1. Draft the piece using doctrine from sections 2 through 6 as you write.
2. Save as markdown or plain text.
3. Run `python scripts/analyze.py --input draft.md --lang en --type marketing --format human`.
4. For each flagged metric, locate the corresponding section above and apply
   the concrete moves.
5. Re-run until the verdict is `LOW_RISK` AND every individual flag is `ok`.
6. For high-stakes deliveries, run an external detector via
   `--external copyleaks` or `--external gptzero` and confirm the result.

---

## See also

- `tells-stylistic-en.md` / `tells-stylistic-fr.md` — vocabulary and
  constructions
- `tells-structural.md` — bullets, headers, tricolons, emoji
- `humanization-techniques.md` — how to write with intentional asymmetry
- `scripts/analyze.py` — the deterministic implementation of these checks
- `scripts/rules.yaml` — thresholds, suspect vocabulary, content-type
  weights

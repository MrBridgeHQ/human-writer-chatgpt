# Structural Tells

> Doctrine for the `human-writer` skill. Covers shape-level patterns the analyzer detects via `scripts/analyze.py` (bullet parallelism, header pyramids, tricolon density, decorative emoji) plus nine further structural tells the analyzer doesn't catch yet but reviewers should flag manually. Language-agnostic; bilingual examples where vocabulary matters.

The throughline: detectors don't read meaning, they read *shape*. Shape uniformity is the cheapest signal of template-driven generation. A page that varies its shape — bullet lengths, header depths, paragraph rhythm — already looks 30% more human before a single word is rewritten.

---

## 1. Bullet parallelism

### What it is

AI bullet lists default to one of three parallel forms:

1. **Verb-first** — every item starts with the same opening verb. *"Build the system / Build the dashboard / Build the alerts."*
2. **Noun-last** — every item ends on the same trailing noun. *"Build the system / Maintain the system / Deploy the system."*
3. **Structure-parallel** — every item shares the same grammatical scaffolding. *"X is good because Y / A is useful because B / C is critical because D."*

The analyzer (`detect_bullet_parallelism` in `scripts/analyze.py`) measures the max of *first-word-ratio* and *last-word-ratio* across bullets in a list. Above 0.60 → flag.

### Why AI defaults to this

It's the cleanest pattern in training data. Tutorials, slide decks, and "10 tips" listicles overwhelmingly use parallel bullets because they read fast. The model has internalized "well-formed list ⇒ parallel form" and reproduces this without explicit anti-prompting. It also looks "tidy" — asymmetry feels sloppy to a model optimizing for surface coherence. But to a reader who's seen 200 AI posts this month, that tidiness *is* the tell.

### When parallelism IS OK

- **Feature matrices** where each row genuinely compares the same attribute. *"Supports OAuth / Supports SAML / Supports OIDC"* — the parallelism encodes real information.
- **Procedural steps** in numbered lists where each step is a command.
- **API reference tables** where each entry has the same shape by spec.

Outside those, parallelism is a tell.

### How to break it

- **Mix sentences and fragments.** One bullet a full sentence, the next a noun phrase, the third a parenthetical clarification.
- **Vary length 3:1 minimum.** If your shortest bullet is 4 words, at least one should run 12+.
- **Mix opener types.** Verb, noun, preposition, conjunction. Never all imperatives.
- **Demote a bullet to inline prose** if it doesn't earn its own line.

### Examples (EN)

Bad — verb-first parallelism, uniform length:

```
- Build the integration with Stripe
- Build the dashboard for monitoring
- Build the alerts for failure modes
- Build the export to CSV
```

Good — opener variety, length variance, one fragment:

```
- Stripe first: integration takes about half a day if you skip Connect.
- Dashboard reads from the same events table — no new schema.
- Alerts: Slack on hard failures, email digest on retries.
- CSV export comes for free (Stripe gives it to you).
```

Bad — noun-last parallelism, every item ends on "the system":

```
- Build the system
- Maintain the system
- Deploy the system
- Document the system
```

Good — asymmetric phrasing:

```
- Build it (3 weeks if Stripe behaves)
- Keep it running (one engineer, half-time)
- Deploy on tag pushes — no manual step
- Docs live in /docs, regenerated from the OpenAPI spec
```

### Exemples (FR)

Mauvais — parallélisme verbal, quatre impératifs :

```
- Construire l'intégration Stripe
- Construire le dashboard
- Construire les alertes
- Construire l'export CSV
```

Bon — ouvertures variées, longueurs hétérogènes :

```
- Stripe d'abord — une demi-journée si on évite Connect.
- Le dashboard lit la même table d'événements (pas de schéma nouveau).
- Alertes : Slack sur erreur dure, mail digest sur retries.
- L'export CSV, Stripe le donne déjà.
```

---

## 2. Header pyramid

### What it is

The "H2 → 3× H3" template. Every H2 section contains exactly three H3 subsections. The analyzer (`detect_header_pyramid`) flags when 2+ H2s each have exactly 3 H3 children.

### Why it triggers detectors

Structural uniformity correlates strongly with template-driven generation. The model has learned "a well-structured article has three subpoints per section" because that's what slide decks and SEO templates look like. The pattern is consistent enough across AI output that detectors can fingerprint it from the table of contents alone. The pyramid also flattens narrative — real writing has sections where one point dominates and others where five interlocking ideas need separate treatment.

### How to break it

- **Vary H3 counts.** Use 0, 1, 2, 4, 5 — anything but uniform 3. One H2 with no H3s, the next with four.
- **Mix flat and deep sections.** Sometimes H2 → straight prose. Sometimes H2 → H3 → H4 for one branch only.
- **Use inline bold leads** instead of H3 when a sub-idea doesn't deserve its own anchor.
- **Drop H3 entirely** from short pieces (under 1500 words).

### When pyramid IS OK

Rigorous technical reference docs (API specs, SDK references, schema documentation) where every "method" or "endpoint" genuinely has the same three subsections (parameters / returns / example). The parallelism encodes the structure of the domain itself. Outside reference docs, kill the pyramid.

### Example

Bad — pure pyramid:

```
## Setup
### Install
### Configure
### Verify

## Usage
### Basic
### Advanced
### Troubleshooting
```

Good — asymmetric depth, one section flat, one with an H4:

```
## Setup

One command: `npm i && npm run init`. Edit `.env` if you need a custom port.

## Usage

### Basic

Run `start`. Read `localhost:3000`.

### When it breaks

Two failure modes that actually happen: stale token (500 on `/api/auth`) and clock skew (401 on every endpoint). Both fixed by `npm run reset`.

#### Note on clock skew

On macOS the system clock drifts after sleep. `sudo sntp -sS time.apple.com` to force a resync.
```

H2 with no H3, H2 with two H3s (one with an H4). No pyramid.

---

## 3. Tricolon rationing

### What it is

The "X, Y, and Z" pattern. *Fast, reliable, and scalable. Build, test, and deploy.* In French: *rapide, fiable et évolutif.* The analyzer (`detect_tricolons`) counts the comma-comma-and pattern and flags above 1 per 200 words.

### Why it's a tell

Tricolons are rhetorically powerful — classical, used by Cicero, Lincoln, every modern speechwriter. *That's the problem.* AI has learned "good prose has tricolons" and uses them in every paragraph. Average AI marketing page: 3-5 tricolons. Average human marketing page: 0-1. The rhythm itself becomes recognizable: a sentence ending in three parallel nouns, followed within two sentences by another. Detectors don't need to parse meaning — they pattern-match the rhythm.

### Budget

**1 tricolon per 200 words.** If your piece is 800 words, allow 4 tricolons total. Spend them on section openers or peroration where rhetoric earns its keep.

### Alternatives

- **List of 2** (asymmetric pair) — *"It's faster and cheaper."* Less rhetorical, more honest.
- **List of 4** (asyndeton) — *"Faster, cheaper, simpler, smaller."* The missing conjunction adds urgency.
- **List of 5** (loose enumeration) — *"Faster, cheaper, more reliable, easier to debug, and shipped a month earlier."* Real benefits come in messy bundles.
- **No list** (single concept) — *"It's faster."* Often the single claim hits harder.

### Examples (EN)

Bad — two tricolons in one paragraph:

```
Our platform is fast, reliable, and scalable. We help teams build, ship, 
and monitor production systems with confidence, speed, and clarity.
```

Good — one tricolon, two pairs, one solo:

```
The platform is fast. Teams use it to ship production systems without 
the usual three-week debugging tax. Build, deploy, monitor — that's the 
loop, and it stays tight even at scale.
```

Bad — every other sentence has a tricolon:

```
We believe in shipping fast, learning fast, and iterating fast. Our 
customers are startups, scale-ups, and enterprises. We provide tools, 
templates, and training.
```

Good — varied enumeration:

```
We ship fast and learn from production. Customers range from 
two-person startups to enterprise teams running 400 services. What we 
provide: a CLI, a dashboard, and the on-call when things break at 3am.
```

### Exemples (FR)

Mauvais — trois tricolons consécutifs :

```
Notre plateforme est rapide, fiable et évolutive. Elle aide les équipes 
à construire, déployer et maintenir leurs systèmes avec confiance, 
rigueur et clarté.
```

Bon :

```
La plateforme est rapide. Les équipes l'utilisent pour pousser en 
production sans la taxe habituelle de trois semaines de debug. 
Construire, déployer, maintenir — la boucle reste serrée même à l'échelle.
```

---

## 4. Emoji as section decoration

### The starter pack

🚀 ✨ 💡 📊 🎯 🔥 💎 ⚡ 📈 🌟 — these account for the majority of AI-decorated headers. Identifiable from across the room:

```
## 🚀 Performance
## ✨ Features  
## 💡 Tips
## 🎯 Goals
## 🔥 What's new
```

### Why it's a tell

AI uses emoji as **decoration**, not information. The rocket doesn't tell you anything new about "Performance". Humans use emoji either **informatively** (country flags in a pricing table, status indicators 🟢 stable / 🟡 beta / 🔴 deprecated, file-type icons) or **voicefully** (sparingly, idiosyncratically, as part of an established style — one emoji that appears 3× in 2000 words and isn't from the starter pack reads as voice). Starter-pack-as-section-marker reads as template.

### Where appropriate

- **Almost never** in technical docs, editorial-SEO long-form, or marketing long-form.
- **Sparingly** in short-comms (Slack, LinkedIn, Twitter). Even there: one per post, not five. And not from the starter pack.

The current analyzer doesn't flag emoji density — manual discipline. A future `detect_decorative_emoji` could flag any emoji in headers, or more than 1 per 500 words in body.

### Defensible use

```
| Region | Currency | Card support |
|--------|----------|--------------|
| 🇺🇸 US  | USD      | Stripe       |
| 🇪🇺 EU  | EUR      | Stripe + SEPA|
| 🇬🇧 UK  | GBP      | Stripe       |
```

The flags encode region. They're not repeated decoratively in headers.

---

## 5. List density

AI converts everything into bullets. A 1000-word piece with 5 bullet-lists screams AI. Humans use prose where flow matters and reserve bullets for genuinely enumerable content.

**Rule: at most 1-2 bullet-lists per ~500 words. Rest as prose.**

A reasonable distribution for a 1500-word post: 3 lists total, of which at most 1 exceeds 5 items; body otherwise prose with bold inline phrases doing the work of "items" without imposing list structure.

### Why it's a tell

Bullets fragment ideas. They prevent the connective tissue of argument — "because", "but", "and yet", "the consequence is" — from doing its work. AI defaults to bullets because they look organized and skim well. Organization-by-fragmentation is itself the signal.

### Example

Bad:

```
The new architecture has three advantages:

- It's faster
- It's simpler
- It's easier to debug

The migration takes a week.
```

Good — prose, same content, varied rhythm:

```
The new architecture wins on three counts that matter: it's roughly 4× 
faster on the hot path, it removes the Kafka layer entirely, and when 
something breaks you can read the failure in one log file. Migration 
takes a week.
```

The bullets carry 18 words of payload in 3 fragments. The prose carries 50 words and tells you *why*.

---

## 6. Conclusion templates

AI adds a "Conclusion" section at the end of nearly every piece, sometimes with that literal H2 header. Three recurring shapes:

1. *"In conclusion, [restate]. [Vague action]. [Vague call to act]."*
2. *"Ultimately, the choice depends on your needs. [Generic CTA]."*
3. *"Whether you're X or Y, [feature] is the solution. Get started today."*

Cross-reference `tells-stylistic-en.md` for the vocabulary side. This file flags it as a *structural* tell because the section itself — its presence, placement, and H2 — is the signal.

### Why it's a tell

Humans end mid-thought, with a question, with a punchline, with a specific call to action. They rarely end with a labeled "Conclusion" that restates the introduction. The instinct to summarize is school-essay instinct — fine for a 3000-word academic paper, wrong for a 1200-word blog post where the reader still has the introduction in working memory.

### Rule

**Don't end with summary unless the piece is genuinely long enough to need it (3000+ words).** Otherwise end on:

- A concrete number (*"We tested 47 actors. 12 survived. Here are the four worth knowing."*)
- A sharp opinion (*"Skip the Postgres extension — it's still alpha."*)
- A specific next action (*"Run `apify push`. If it errors on memory, bump to 2GB."*)
- A question that earns a follow-up (*"What about Apify's standby mode? Different post."*)
- A returning callback to the opening without explicitly restating it.

Never end on "let me know if you have any questions" or "feel free to reach out". That's email signoff, not prose.

---

## 7. Intro-body-conclusion rigidity

AI defaults to the five-paragraph essay structure regardless of topic: intro (hook + thesis), three body paragraphs (each one supporting claim with example), conclusion (restate thesis, broad implication, CTA). This works in five-paragraph essays because that's what they are. It does not work in a blog post, a technical document, a case study, a teardown, an editorial, or a memo.

### How humans differ

They skip the intro. They bury the thesis in paragraph 3. They mix evidence and argument in the same paragraph. They end abruptly. They start mid-thought. Structure follows what the content needs.

### How to break it

- **Start with the punchline.** First sentence is the conclusion you'd normally save for the end.
- **Withhold the thesis until paragraph 3.** Start with a scene, an anecdote, a quote, a number.
- **Open in media res.** Drop the reader mid-debate, mid-problem. *"The Stripe webhook had been failing for four days before anyone noticed."*
- **End without summary.** When you've said what you came to say, stop.
- **Mix evidence and argument** in the same paragraph. AI separates "here's a claim" from "here's the example"; humans braid them.

### Example

Bad — five-paragraph essay on a topic that doesn't need it:

```
## Introduction
Choosing the right database is one of the most important decisions in 
building a modern application. We'll explore three options: Postgres, 
MongoDB, and Redis.

## Postgres
Postgres is a powerful relational database. [generic paragraph]

## MongoDB  
MongoDB is a popular NoSQL option. [generic paragraph]

## Redis
Redis is fast and good for caching. [generic paragraph]

## Conclusion
Each database has its strengths. The right choice depends on your needs.
```

Good — punchline-first, no intro, abrupt end:

```
Use Postgres. Use it for the relational data, use it for the JSON, use 
it for the queue (Skytools, river, whatever — Postgres can be your 
queue). The reason you've been told to add MongoDB or Redis is usually 
"we hit a wall at scale", and the wall they hit was almost always one 
missing index or one missing connection pool. Postgres until 100k DAU, 
then re-evaluate. That's the rule.
```

Same topic, 25% the length, no intro, no conclusion, opinion clearly held.

---

## 8. Header text patterns

### What AI does

- **Noun-phrase titles** in Title Case Every Word — *"Performance Optimization", "Database Selection"*.
- **"Compelling Subheaders"** (literal AI tell) — headers reaching for vague positives ("powerful", "seamless", "comprehensive").
- **Consistent grammar** across all headers — every H2 a noun phrase, no variation.

### What humans do

- **Sentence case** — *"Performance optimization"*. Capital on first word only.
- **Questions** — *"What actually changes?", "Why this matters?", "Where does it break?"*
- **Fragments** — *"The quiet part", "What we got wrong", "One weird thing"*.
- **Mixed grammar** — H2 in one section a question, the next a noun phrase, the third an imperative.

### Example

Bad — uniform noun-phrase Title Case:

```
## Performance Optimization Techniques
## Database Selection Criteria
## Monitoring And Observability Best Practices
## User Onboarding Strategies
```

Good — mixed forms, sentence case, question, fragment:

```
## Where the latency actually came from
## Postgres or DynamoDB?
## Monitoring: stop pretending Datadog is enough
## The onboarding problem
```

---

## 9. Bold and italic markup density

### What AI does

Bolds key phrases aggressively — 3-5 bolded phrases per section. Pattern reads like over-eager textbook annotation: every important word emphasized, which means none of them are. Also italicizes for emphasis on every other claim, mixing emphasis-italic with the correct typographic uses.

### What humans do

- **Bold sparingly** — often only for true definitional terms ("an **idempotent** operation is..."). Sometimes for the key claim of a section, once.
- **Italic for typography**: book and publication titles (*Le Monde*, *The New Yorker*), foreign-language phrases not yet absorbed (*ad hoc*, *de facto*), technical terms on first introduction.
- **Don't double up.** Never **_bold-italic_** — that's print design from 1995.

### Budget

- **Bold**: 1-2 phrases per 500 words. Less is fine. More is suspicious.
- **Italic**: only the typographic uses above. If italicizing for emphasis, use bold instead — and sparingly.

### Example

Bad — bold-spray:

```
This **revolutionary** approach to **database design** offers 
**unprecedented performance** and **scalability**. By leveraging 
**modern architectures**, teams can achieve **significant improvements** 
in their **operational efficiency**.
```

Good — one italic for a defined term, one bold for the load-bearing claim:

```
The trick is *event sourcing*: instead of storing the current state, 
you store the sequence of events that produced it. State becomes a 
**derived view**, not a source of truth. Replay the events, get the 
state. Cheap, durable, debuggable.
```

---

## 10. Block-quote and callout overuse

AI templates pull a "key sentence" into a blockquote or callout once per section. Often the callout just restates the surrounding paragraph in a slightly punchier form.

Use blockquotes for **actual quotes** (citing someone else's words). Use callouts (`> Note:`, `> Warning:`) sparingly, when the information genuinely sits outside the main argument — a caveat, a side-note, a pointer to related reading.

### Budget

- **One callout per piece** is comfortable.
- **One callout per section** is a tell.
- **Zero callouts** is fine for most pieces under 2000 words.

### Example

Bad — callout that just restates the paragraph:

```
The Stripe webhook had been failing silently for four days. Nobody 
noticed because the dashboard showed "OK" — it was reading from a 
cached health check.

> Silent failures are the worst failures because nobody knows to 
> look for them.

The fix was to make the health check actually call the webhook endpoint.
```

Good — same content as prose, punch lives in the sentence:

```
The Stripe webhook had been failing silently for four days. Nobody 
noticed because the dashboard showed "OK" — it was reading from a 
cached health check. Silent failures: nobody knows to look for them. 
The fix: make the health check actually call the webhook endpoint.
```

Defensible callout — genuine side-note:

```
> Note: this only works if your health check has the same auth context 
> as the production webhook. If it doesn't, you're testing a different 
> code path and you'll miss class-of-error #3 (token expiry).
```

---

## 11. Numbered list overuse

AI defaults to numbered when sequence doesn't matter. Three items become 1/2/3 even when order is interchangeable.

**Rule: numbered ONLY when order is meaningful** — sequential steps in a procedure, ranked items, or items the prose later refers to by number ("see point 2 above"). Otherwise use bullets, or — better — prose.

### Why it's a tell

A numbered list of unordered items is structural noise. The numbers imply sequence or ranking that doesn't exist. Detectors don't pattern-match the numbers specifically, but a human reader notices: *"why is this numbered?"* The answer is usually: "because the model defaulted to numbered."

### Examples

Bad — numbered list of unordered features:

```
Our platform offers:

1. Real-time analytics
2. Custom dashboards
3. API access
4. Multi-tenant support
```

Good — bullets:

```
The platform gives you:

- Real-time analytics (sub-second on the hot path)
- Custom dashboards built on the same data layer
- API access (REST and GraphQL, same auth)
- Multi-tenant from day one
```

Better — prose if it'll flow:

```
You get analytics in real time, dashboards you can rearrange, REST 
and GraphQL APIs, and multi-tenancy as a primitive rather than an 
afterthought.
```

Truly numbered — order matters:

```
Migration steps:

1. Run `db:freeze` to pause writes (about 30 seconds).
2. Snapshot the database with `pg_dump`.
3. Restore into the new cluster.
4. Repoint the connection string.
5. Run `db:unfreeze`.
```

Step 3 cannot precede step 2. The numbers carry information.

---

## 12. Table of contents at the top

AI loves to scaffold a TOC at the top of any piece longer than 800 words. The TOC is auto-generated from the headers and provides zero new information — it's the table of contents of a document the reader is about to read in the next 30 seconds.

### When TOC is appropriate

- Reference documentation (API specs, SDK guides, multi-page manuals).
- Long-form essays (5000+ words) where the reader genuinely needs a map.
- Documentation portals where the TOC is auto-rendered by the doc engine, not written into the markdown.

### When TOC is a tell

- Blog posts under 3000 words.
- Marketing pages of any length.
- Editorial pieces of any length (the TOC kills the reading experience).
- Anything with a sidebar nav that already serves the TOC purpose.

**Rule: drop the TOC unless the piece is genuinely a reference doc or 5000+ words and intended for non-linear reading.** Trust the headers to do the navigation work.

---

## 13. Section dividers (`---`)

AI uses `---` between every section. Sometimes between every H2. Sometimes between every paragraph. The dividers add visual chunking that the headers should already be doing.

Humans use dividers sparingly, often only for major shifts — between body and postscript, between parts of a series (rare), between an essay and a "further reading" appendix.

**Budget: 1 divider per 600 words of body content, maximum.** A typical 1500-word piece should have 0-2 dividers, not 6.

### Why it's a tell

Like emoji decoration and TOC scaffolding, divider overuse is a *visual* signal that hits before the reader parses a word. A page broken every 200 words by `---` looks like template output.

### Defensible use

```
## Final section
...the body concludes here, naturally...

---

**Update (2026-05-15):** since publication, the API changed. The 
endpoint mentioned above is now `/v2/events` rather than `/v1/events`. 
The rest of the analysis still holds.
```

The divider marks a genuine shift in voice and time.

---

## Summary heuristics

Quick structural pass over a draft:

- **Bullet lists**: vary opener types and lengths; cap parallelism at 50%; demote short lists to prose.
- **Headers**: vary H3 counts (never uniform 3); mix grammar (statement / question / fragment); use sentence case.
- **Tricolons**: 1 per 200 words max; alternate with pairs, fours, fives, solos.
- **Emoji**: zero in technical/long-form/editorial; one informative per 500 words elsewhere.
- **Bullets vs prose**: 1-2 lists per 500 words; rest as prose.
- **Endings**: no labeled "Conclusion" under 3000 words; end on number, opinion, or specific action.
- **Bold**: 1-2 phrases per 500 words.
- **Italic**: only for true typographic use (titles, foreign phrases, terms on first intro).
- **Callouts**: 1 per piece, not 1 per section.
- **Numbered lists**: only when order is meaningful.
- **TOC**: drop unless reference doc or 5000+ words.
- **Dividers**: max 1 per 600 words; usually 0.

A draft that passes all twelve checks is already in the top quartile of pre-publication AI-resistance. Vocabulary work (`tells-stylistic-*.md`) and statistical work (`tells-statistical.md`) are then the remaining layers.

---

## See also

- `tells-stylistic-en.md` / `tells-stylistic-fr.md` — vocabulary side (lexical tells, banned-word lists)
- `tells-statistical.md` — distributional metrics (burstiness, perplexity, sentence-length variance)
- `humanization-techniques.md` — how to write asymmetrically from the first draft
- `scripts/analyze.py` — `detect_bullet_parallelism`, `detect_header_pyramid`, `detect_tricolons` (current automated coverage); structural tells 4-13 above are manual-review for now

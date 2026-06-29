# Humanization Techniques

> Doctrine for the `human-writer` skill. The ten moves that turn AI-shaped prose into human-shaped prose. Apply in WRITE mode while drafting; apply in CLEAN mode as a targeted checklist.

The techniques are ordered by impact-per-edit. If you can only apply one, apply #1. If you can apply two, add #5. If you have time for everything, the full ten will cut analyzer score by 30–50 points on a typical AI draft.

Each technique below answers the same four questions:

1. **Definition.** What is it?
2. **Why it works.** Which statistical / stylistic signal does it disrupt?
3. **Worked examples.** Before and after, in EN plus FR where applicable.
4. **How to apply.** Proactive in WRITE mode, targeted in CLEAN mode.

---

## 1. Vary sentence length deliberately

**Definition.** Alternate short (≤ 6 words) and long (≥ 25 words) sentences. Aim for a standard deviation of sentence lengths ≥ 8.

**Why it works.** AI prose averages 18–22 words per sentence with a low standard deviation (typically 3–5). The analyzer measures this via `sentence_length_stdev` and flags anything under ~6. Variance is the cheapest, highest-signal humanization edit available.

### Rhythm patterns to build in

| Pattern | Shape | Use case |
|---|---|---|
| **Short-short-long** | 5w + 4w + 28w | Set up a claim, then expand |
| **Long-short** | 30w + 4w | Build then punch (very human) |
| **Fragment-long** | 2w + 25w | Topic + dump |
| **Short-medium-fragment** | 6w + 15w + 3w | Cadence variation |
| **Run-on with semicolon** | 35w with `;` | One thought, two beats |

Use semicolons to extend without resetting rhythm. Use periods to reset hard. Use commas to slow without breaking. Explicit fragments ("So.", "Right.", "And there it is.") are the strongest rhythm breakers.

### Worked example (EN)

Bad (uniform; lengths 13, 13, 11, 12; stdev ~1):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> The pricing tool exports a CSV file with margin tiers per SKU. It updates daily based on competitor data scraped from major marketplaces. Users can filter by category, region, or supplier. The dashboard shows historical price evolution over the past 90 days.
<!-- human-writer:ignore-end -->

Good (varied; lengths 2, 8, 25, 18, 5, 8; stdev ~9):

> CSV out. One row per SKU, one column per marker. The pricing tool updates the file every night, pulling competitor data from Amazon, eBay, and three regional marketplaces I won't name in public. Filter it in Excel — category, region, supplier — and you get the same view our procurement team uses. Ninety days of history. That's usually enough to spot a competitor stockout.

### Worked example (EN) (second pattern)

Bad (uniform, all 12–16 words):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Our analytics platform tracks user behavior across multiple touchpoints. It provides actionable insights for marketing teams. It integrates with the most common ad networks. It exports reports as PDF or CSV.
<!-- human-writer:ignore-end -->

Good (long + short + fragment + long):

> The analytics platform follows a user from the first ad click through to the seventh return visit, then stops because GDPR makes anything beyond that a lawyer's problem. Five tables. PDF or CSV — your call. We added the Meta connector last year after a client got tired of switching tabs every Monday morning.

### Worked example (FR)

Bad (uniform; longueurs 14, 13, 15, 12; écart-type ~1.2) :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Notre outil d'analyse exporte un fichier CSV pour chaque référence du catalogue. Il se met à jour chaque nuit selon les données concurrentielles. Les utilisateurs peuvent filtrer par catégorie, région ou fournisseur. Le tableau de bord affiche l'évolution des prix sur 90 jours.
<!-- human-writer:ignore-end -->

Good (longueurs 3, 12, 28, 5, 18 ; écart-type ~10) :

> Export CSV. Une ligne par référence, une colonne par marqueur de prix. L'outil tourne chaque nuit et récupère les prix Amazon, eBay et trois marketplaces régionales que je préfère ne pas nommer ici. Filtrage Excel direct. Quatre-vingt-dix jours d'historique, ce qui couvre la quasi-totalité des ruptures de stock concurrentes qu'on a observées en 2025.

### Worked example (FR) (second pattern)

Bad :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Le scraper récupère les données depuis le site source. Il les nettoie selon les règles configurées. Il les stocke dans une base PostgreSQL. Il les rend disponibles via une API REST.
<!-- human-writer:ignore-end -->

Good :

> Le scraper avale la page, la nettoie selon nos règles maison (qui ne survivent jamais à un redesign de la cible) et la pousse dans Postgres. Trois colonnes. C'est tout. L'API REST sort le reste — et on garde la sortie au format JSON parce que c'est ce que veut le front, point.

### How to apply

**WRITE mode (proactive).** As you draft, force yourself to drop a one- or two-word sentence after every long one. If you've written three sentences of similar length, the next one *must* be a fragment or a 30+ word run-on.

**CLEAN mode (targeted edit).** Run `analyze.py` and look at `sentence_length_stdev`. If under 6, identify the three longest paragraphs and rewrite them by:
1. Splitting one mid-length sentence into a fragment + a sentence.
2. Joining two short sentences into one long, comma-spliced or semicolon-linked sentence.
3. Adding one explicit fragment ("Right.", "So.", "Or not.").

---

## 2. Inject one opinion or specific anecdote per ~300 words

**Definition.** Every 300 words or so, insert one of: a first-person take, a named entity, a specific number, or a small concrete story.

**Why it works.** AI prose is information-dense but opinion-empty and entity-light. LLMs default to generic claims because generic claims minimize the chance of being wrong. Specific entities ("Bordeaux 2018", "47 req/s", "Marie from procurement") are statistically rare in AI output; they're high-signal markers of authored prose because they couldn't be generated without first-hand context.

### What counts as an "opinion"

A take that someone could disagree with. Not "X is good for Y"; that's a fact-claim. But "I'd skip X for anything under 100 SKUs because the ROI doesn't break even" is an opinion: opinionated, specific, defensible.

| Not an opinion | Opinion |
|---|---|
| "Performance matters" | "Performance is the only thing that matters below 1k QPS — everything else is bikeshedding." |
| "Choose the right tool" | "Don't use Playwright for static pages. Cheerio is faster and the maintenance bill is smaller." |
| "Pricing is important" | "Most pricing strategies fail because the team that sets them never talks to the team that quotes them." |

### What counts as "specific"

A named entity (person, place, product, version), a date, a number with units, or a concrete event. Not "a major marketplace"; say Amazon. Not "recently"; say "March 2024". Not "users"; say "the on-call engineer who got paged at 3am".

### How to inject without breaking flow

Three placements work:

1. **Mid-paragraph aside.** "The actor (we benched at 47 req/s on a 2GB instance) handles bundles..."
2. **End-of-paragraph kicker.** "...and so on. Honestly, that's where most teams stop — and where ours started."
3. **New sentence between two claims.** "API clients need rate limits. The Stripe API caps you at 100 req/s, by the way. So you architect around that."

### Bad vs good

Bad (vague platitude):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Web scraping at scale requires careful tooling. Choosing the right framework can make a significant difference in performance and reliability.
<!-- human-writer:ignore-end -->

Good (specific take):

> Caching at scale comes down to one decision: do you cache full responses, or just the expensive query results? Full-response caching is simple (~5 lines in nginx) but your hit rate caps around 40% once query params vary. Result caching in Redis is more code but holds 85% hit rate on our traffic. We pick result-caching for read-heavy endpoints; full-response for static marketing pages.

### Worked example (FR)

Bad :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Le pricing dynamique nécessite des outils adaptés. Le choix du bon framework peut faire une vraie différence.
<!-- human-writer:ignore-end -->

Good :

> Le rafraîchissement des données se joue sur une décision unique : est-ce qu'on rappelle l'API toutes les 4 heures, ou est-ce qu'on tient la fenêtre 15 minutes ? L'API REST officielle tolère le 15 minutes sous plan payant ; le endpoint gratuit te coupe à 60 req/min. On a perdu deux semaines en 2025 à le découvrir par accident, et on a fini par caler le rythme service par service.

### How to apply

**WRITE mode.** Before writing, list 3 specific facts/anecdotes/opinions you can drop into the piece. Place one every ~300 words.

**CLEAN mode.** Search the draft for paragraphs that contain zero proper nouns, zero numbers, and zero first-person markers. Each such paragraph needs one injection. If the draft has *none* across the whole text, that's an emergency — the piece reads as generic and no amount of sentence-length variance will save it.

---

## 3. Use asymmetric bullets

**Definition.** In any bulleted list, deliberately vary the length, structure, opening word, and grammatical shape of each item.

**Why it works.** AI bullets are parallel by default: same verb (`Build / Build / Build`), same length (8–12 words each), same shape (verb + object). The analyzer (`scripts/analyze.py`) flags this when > 60% of bullets share the same first or last word, or when bullet-length variance is below threshold. Asymmetry breaks the fingerprint.

### Three asymmetry axes

| Axis | Bad (symmetric) | Good (asymmetric) |
|---|---|---|
| **Length** | All 6–8 words | Mix of 2-word fragments and 25-word callouts |
| **Opener** | All start with a verb | Mix verbs, nouns, questions, fragments |
| **Shape** | All `verb + object` | Mix commands, observations, questions, mini-paragraphs |

### Worked example (EN)

Bad (length-symmetric, verb-symmetric):

```
- Scrape product pages
- Extract pricing data
- Store results in dataset
- Export to CSV
```

Good (asymmetric):

```
- Parse input files (JSON direct for the simple case, custom parser for the legacy format — see `parsers.ts`)
- Amounts: we capture list, discount, and "total" separately because the source format rounds inconsistently
- Data → CSV is one `make export` away
- And then? Most teams stop here. We pipe it into Metabase for the trend view.
```

What changed: bullet 1 has a parenthetical with code path; bullet 2 opens with a noun and uses a colon callout; bullet 3 is one short clause with an arrow; bullet 4 is a rhetorical question + two sentences.

### Worked example (FR)

Bad :

```
- Scraper les pages produits
- Extraire les données de prix
- Stocker les résultats dans le dataset
- Exporter en CSV
```

Good :

```
- Parser les fichiers d'entrée (JSON direct pour le simple, parseur custom pour le legacy — cf. `parsers.ts`)
- Côté montants : on stocke brut, remise et "total" séparément parce que le format source arrondit n'importe comment
- Données → CSV : `make export`, point final
- Et après ? La plupart des équipes s'arrêtent là. Nous, on branche Metabase derrière.
```

### Sub-bullets for asymmetry

Adding a single sub-bullet under one item (and only one) breaks the visual rhythm hard:

```
- Parse input files
  - Custom parser only for the legacy format — adds ~200ms/file
- Amount extraction
- CSV export
```

The lone sub-bullet kills the AI shape. It signals "a human chose to elaborate exactly here."

### When symmetric bullets ARE appropriate

Parallel lists where the reader is supposed to compare like-with-like deserve symmetric formatting. Examples:

- Step-by-step procedures where order is critical ("Step 1: ... Step 2: ... Step 3: ...")
- API reference tables (every endpoint described the same way)
- Comparison matrices (same column headers, same row shapes)
- Pricing tiers in a structured table (every tier has price / features / limits)

In those cases, parallelism is *informational*: the reader uses the structure to compare. Don't break it just for style. The rule is: **prose-embedded lists should be asymmetric; reference/comparison structures can stay symmetric**.

### How to apply

**WRITE mode.** When you reach for a bullet list, draft it normally, then deliberately rewrite at least 2 of the 4 bullets to use a different shape (a colon callout, a parenthetical, a question, a fragment).

**CLEAN mode.** Check `bullet_first_word_repetition` from `analyze.py`. If > 60%, the bullets need rewriting. Easiest fix: rewrite half the bullets to NOT start with the dominant verb.

---

## 4. Break tricolons: vary list sizes

**Definition.** Resist the "rule of three" reflex. Use lists of 2, 4, or 5 items. Cap the explicit three-item `and`-joined tricolon at 1 per 200 words.

**Why it works.** AI prose is saturated with tricolons. A few typical specimens:

<!-- human-writer:ignore-start (citation: tricolon tells quoted, not used) -->
"fast, reliable, and scalable", "build, test, and deploy", "small, medium, and large".
<!-- human-writer:ignore-end -->

The cadence is comforting and grammatically tidy, which is exactly why LLMs default to it. The analyzer flags density above 1 per 200 words.

### When tricolons ARE OK

Tricolons aren't banned; they're capped. A well-placed tricolon at a rhetorical climax (end of paragraph, end of section) earns its place. The problem is repetition: when *every* paragraph closes with one, the rhythm becomes a fingerprint.

Acceptable uses:

- **Rhetorical climax.** One per piece, ideally the closing line of an argument.
- **Set-up + payoff.** A tricolon in a setup sentence followed by a sharp pivot ("Fast, cheap, reliable. Pick two.").
- **Quoting an existing tricolon.** "Liberté, égalité, fraternité" is fine; "speed, scale, simplicity" probably isn't.

When tricolons are tells: when they appear in every paragraph, or worse, twice in the same paragraph. A "tricolon budget" of 1 per 200 words holds the line.

### Specific alternatives

| Reflex | Alternative | Example |
|---|---|---|
| Tricolon (3 items, "and") | **List of 2** | "Fast and cheap." |
| Tricolon (3 items, "and") | **List of 4** | "Fast, cheap, cached, and audited." |
| Tricolon (3 items, "and") | **List of 5 with asyndeton** | "Fast, cheap, cached, audited, deployable in one command." |
| Tricolon (3 items, "and") | **List of 3 with asyndeton (no "and")** | "Fast, reliable, scalable." (drops the final "and") |
| Tricolon (3 items, "and") | **Pair + parenthetical** | "Fast and reliable (also cheap, but that's a side effect)." |

Asyndeton, dropping the final "and", is the cheapest variation. It keeps the three-beat rhythm but loses the AI-signature `, and` connector.

### Worked example (EN)

Bad (three tricolons in two sentences):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> The actor is fast, reliable, and scalable. It handles bundles, variants, and locales. It runs daily, weekly, and on demand.
<!-- human-writer:ignore-end -->

Good (one tricolon budget spent; varied list sizes):

> The actor handles bundles and variants across 12 locales. It runs daily — or on demand for ad-hoc audits. Fast, reliable, scalable: that's the order we optimized in.

### Worked example (FR)

Bad (calque français du tricolon) :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> L'outil est rapide, fiable et précis. Il gère les bundles, les variantes et les locales. Il tourne tous les jours, toutes les semaines et à la demande.
<!-- human-writer:ignore-end -->

Good :

> L'outil gère bundles et variantes sur 12 locales. Tournée quotidienne ou à la demande, selon le besoin. Rapide, fiable, précis : c'est l'ordre dans lequel on a optimisé.

### How to apply

**WRITE mode.** Keep a mental "tricolon budget" of 1 per 200 words. If you've already used one in the current ~200-word stretch, force the next list into 2 or 4 items, or use asyndeton.

**CLEAN mode.** Search the draft for `, and ` followed by a noun ending the sentence. Count instances. If > 1 per 200 words, rewrite the lowest-impact occurrences first (the ones that aren't at rhetorical climaxes).

---

## 5. Cut all hedging openers

**Definition.** Delete the AI-templated qualifier phrases that front-load sentences (the openers catalogued below). State the claim directly.

**Why it works.** Hedging openers are the most distinctive AI signature in long-form prose. They're space-filler with zero information value. Humans hedge inline when needed; LLMs hedge by template at the start of sentences. Removing them is the highest words-saved-per-edit move available.

### Full forbidden list (EN)

<!-- human-writer:ignore-start (citation table: tells quoted, not used) -->
| Forbidden opener | Why it's a tell |
|---|---|
| "It's important to note that" | Templated AI hedging |
| "It's worth noting that" | Templated AI hedging |
| "Worth mentioning that" | Templated AI hedging |
| "Keep in mind that" | Templated AI hedging |
| "It should be noted that" | Templated AI hedging |
| "It's worth mentioning that" | Templated AI hedging |
| "One thing to remember is that" | Templated AI hedging |
| "It's crucial to understand that" | Templated AI hedging + "crucial" tell |
| "It is essential to recognize that" | Templated AI hedging + "essential" tell |
| "Bear in mind that" | Templated AI hedging |
| "That said," (as paragraph opener) | Mid-sentence OK; paragraph-opener is templated |
| "All in all," | Conclusion template |
| "In conclusion," | Conclusion template |
| "Ultimately," (as opener) | Conclusion template |
<!-- human-writer:ignore-end -->

### Full forbidden list (FR)

<!-- human-writer:ignore-start (citation table: tells quoted, not used) -->
| Forbidden opener | Why it's a tell |
|---|---|
| "Il est important de noter que" | Calque + AI template |
| "Il convient de noter que" | Templated, formal AI register |
| "Il convient de souligner que" | Templated, formal AI register |
| "Il faut garder à l'esprit que" | Calque of "keep in mind" |
| "Il est essentiel de comprendre que" | Templated AI hedging |
| "On notera que" | Formal AI register |
| "Précisons que" | Sometimes OK inline; opener is template |
| "Notez que" | Templated |
| "En conclusion," | Conclusion template |
| "Au final," | Conclusion template |
| "Finalement," (as opener) | Conclusion template |
<!-- human-writer:ignore-end -->

### Why they're tells

These phrases signal AI hedging behavior: the model's tendency to soften every claim with a meta-comment about its importance. A human writer either states the qualifier inline ("The actor needs 1GB minimum, by the way") or doesn't bother ("The actor needs 1GB minimum.").

### What to do instead

Two options:

1. **State the claim directly.** Drop the opener; keep the rest.
2. **Qualify inline.** If the qualifier carries information, work it into the sentence as a parenthetical or as a dependent clause.

### Worked example (EN)

Bad:

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> It's important to note that the actor requires at least 1GB of memory. It's worth mentioning that performance degrades on bundles. Keep in mind that the schema may change.
<!-- human-writer:ignore-end -->

Good (option 1, direct):

> The actor needs 1GB minimum. Performance degrades on bundles (we'll fix that in v2). The schema may change.

Good (option 2, inline qualifier):

> The actor needs 1GB minimum — non-negotiable on Apify's free tier. Performance on bundle SKUs is roughly 40% slower; this is a known issue we'll address in v2. Schema changes are likely in the next two quarters.

Same content. Half the words. Sounds like someone actually wrote it.

### Worked example (FR)

Bad :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Il est important de noter que l'Actor nécessite au minimum 1 Go de mémoire. Il convient de souligner que les performances se dégradent sur les bundles. Il faut garder à l'esprit que le schéma peut évoluer.
<!-- human-writer:ignore-end -->

Good :

> L'Actor a besoin d'1 Go minimum. Les performances décrochent sur les bundles (correction prévue en v2). Le schéma peut évoluer.

### How to apply

**WRITE mode.** Never start a sentence with a hedging opener. Period. If you catch yourself typing "It's important to note", delete and rewrite.

**CLEAN mode.** Grep the draft for every entry in the forbidden lists. Delete each occurrence and rewrite the remaining sentence. This is the single highest-ROI CLEAN-mode operation.

---

## 6. Use idiosyncratic markers (NEW)

**Definition.** Deliberately build 1–2 recurring tics per piece (a favored conjunction, a pet phrase, a quirky structural pattern) that the analyzer cannot fingerprint but that human readers attribute to authorial personality.

**Why it works.** Human writers have tics. Hemingway abuses "and." Pratchett abuses footnotes. McPhee abuses parentheticals. AI prose is *too clean*. It avoids signature moves because LLMs are trained to produce average-of-corpus output. A deliberate tic registers as personality.

The trick is calibration. One tic per ~500 words is invisible to the analyzer (which thresholds on density) but registers to readers. Two tics per 200 words is noise.

### Tic catalog (pick one or two; not all)

| Tic | Cadence | Use case |
|---|---|---|
| Sentences starting with "Look," | 1 per ~1000 words | Pivot to a strong claim |
| Sentences starting with "And" / "But" / "Yet" | 1 per ~200 words (cap) | Continuation that defies "no conjunction at start" rule |
| Em-dash interrupt mid-sentence | 1 per ~250 words (capped — see EN tells doc) | Genuine thought interruption |
| Trailing "anyway." | 1 per ~800 words | Casual sign-off |
| Trailing "honestly." | 1 per ~600 words | Confidential register |
| Self-correction ("actually, closer to X") | 1 per ~500 words | Human imperfection signal |
| Bracketed aside `[like this]` | 1 per ~400 words | Visual rhythm break |
| "The thing is," opener | 1 per ~800 words | Setup before a key claim |

### FR-specific tics

| Tic | Cadence | Use case |
|---|---|---|
| "voilà" as sentence pivot | 1 per ~600 words | Genuine French rhythm marker |
| "bref," as paragraph closer | 1 per ~800 words | Casual register |
| "du coup," as connector | 1 per ~400 words | Spoken register |
| "franchement," as opener | 1 per ~600 words | First-person take |
| Sentences ending with ", quoi." | 1 per ~1000 words | Very casual register; use only in informal contexts |

### Worked example (EN)

Without a tic (clean, AI-flavored):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> The pricing tool runs every 15 minutes. It tracks 50 SKUs by default. The results land in a Postgres view that the team queries from Metabase.
<!-- human-writer:ignore-end -->

With a "Look," tic and a trailing "anyway":

> The pricing tool runs every 15 minutes. Look, we tried 5 and the rate limits killed us — 15 is the floor. It tracks 50 SKUs by default. The results land in a Postgres view, which the team queries from Metabase anyway.

The two tics ("Look," and "anyway") are invisible to bot detection but read as a person with a voice.

### Worked example (FR)

Sans tic :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> L'outil de pricing tourne toutes les 15 minutes. Il surveille 50 références par défaut. Les résultats arrivent dans une vue Postgres que l'équipe interroge depuis Metabase.
<!-- human-writer:ignore-end -->

Avec "voilà" et "du coup" :

> L'outil tourne toutes les 15 minutes — voilà, on a essayé 5 minutes, on s'est mangé les rate limits. Cinquante références par défaut. Du coup les résultats arrivent dans une vue Postgres que l'équipe interroge depuis Metabase.

### How to apply

**WRITE mode.** Before drafting, pick one or two tics from the catalog. Use them at the cadence listed. Resist the urge to add more.

**CLEAN mode.** Carefully, because adding tics during cleanup risks over-doing it. If the piece is otherwise good but reads as bot-clean, inject *one* tic at *one* natural insertion point. Re-run the analyzer.

---

## 7. Inject digressions and parentheticals (NEW)

**Definition.** Humans wander. AI stays on-track relentlessly. Insert one short digression per ~500 words. Use parentheses for genuine asides.

**Why it works.** LLMs are trained to follow the prompt without drift. The result is unnaturally focused prose: every paragraph stays inside its topical lane. Human writers tangent constantly: a price discussion triggers a memory of a specific 2018 vintage, which triggers a comment about that summer's heatwave, which loops back to the price. The drift is the signal of authentic thought.

### What counts as a digression

- A bracketed aside about a related but minor fact
- A sentence that exits the topic for one beat then returns
- A footnote-style interjection ("which is itself a long story")
- A parenthetical with a specific number, name, or moment

The key constraint: the digression must *return* to the main thread. A digression that doesn't return is just a tangent; AI doesn't do digressions because it never tangents.

### Worked example (EN)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
Without digression:

> Wine pricing is volatile. Producers adapt by monitoring market signals.
<!-- human-writer:ignore-end -->

With digression:

> Wine pricing is volatile (Burgundy 2020 just dropped 11% in three weeks). Producers adapt — those who track market signals weekly, anyway.

### Worked example (EN) (longer)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
Without digression:

> A database migration requires good preparation. The schema matters, the indexes matter, and the constraints matter. Get any one wrong and the deploy breaks in prod.
<!-- human-writer:ignore-end -->

With digression:

> A database migration requires good preparation. Schema, indexes, constraints — get one wrong and the deploy breaks in prod. (We learned this the hard way on a migration in March 2024: schema clean, indexes clean, but we'd forgotten a NOT NULL constraint on a column full of NULLs. Rolled back in 47 minutes.) The lesson is just: belt-and-braces on every layer.

### Worked example (FR)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
Sans digression :

> Le pricing du vin est volatil. Les producteurs s'adaptent en surveillant les signaux marché.
<!-- human-writer:ignore-end -->

Avec digression :

> Le pricing du vin est volatil (Bourgogne 2020 a chuté de 11% en trois semaines). Les producteurs s'adaptent — du moins ceux qui regardent les signaux marché chaque semaine.

### Worked example (FR) (longer)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
Sans digression :

> Une migration de base de données demande une bonne préparation. Le schéma, les index, les contraintes — tout doit être réglé sinon le déploiement casse en prod.
<!-- human-writer:ignore-end -->

Avec digression :

> Une migration de base de données demande une bonne préparation. Schéma, index, contraintes — un seul oubli et le déploiement casse en prod. (On a appris ça sur une migration en mars 2024 : schéma nickel, index nickel, mais on avait oublié une contrainte NOT NULL sur une colonne pleine de NULL. Rollback en 47 minutes.) Bref, ceinture-bretelles sur chaque couche.

### How to apply

**WRITE mode.** Plan one digression per major section (every ~500 words). Mark insertion points in your outline.

**CLEAN mode.** Read each paragraph and ask: "Did the writer think of anything specific while writing this?" If every paragraph is locked to its topic, inject one parenthetical with a real specific fact.

---

## 8. Choose concrete over abstract (NEW)

**Definition.** When given the choice between a generic noun and a specific one, always pick the specific. AI defaults to abstractions ("solutions", "businesses", "workflows"); humans default to concrete examples ("the 14-tab Google Sheet", "the finance team's Monday reconciliation", "Monday morning prep").

**Why it works.** AI prose lives in the abstraction layer because abstractions are safer: you can't be wrong about "solutions" because the word doesn't commit to anything. Concrete nouns ("Postgres", "the nightly cron", "12 minutes") commit to facts that must be true. Their presence is a strong signal of first-hand writing.

This technique compounds with #2 (specific anecdotes); but where #2 is about *inserting* a specific moment, #8 is about *replacing* abstract nouns with concrete ones throughout.

### Abstract → concrete substitution table

<!-- human-writer:ignore-start (citation table: abstract AI nouns quoted, not used) -->
| Abstract (AI default) | Concrete (human alternative) |
|---|---|
| "businesses" | "a 12-person finance team" / "the on-call rotation" |
| "solutions" | the specific tool: "the dashboard", "the cron job", "the CSV export" |
| "workflows" | the specific step: "the Monday-morning prep", "the import script" |
| "users" | "the support agent triaging tickets" / "the analyst on the trading desk" |
| "data" | "47 columns of id + amount + status + timestamp" |
| "performance" | "47 req/s on a 2GB instance" |
| "scalability" | "we ran this against 2.3M records in 9 hours" |
| "insights" | "the specific number you couldn't get before" |
| "stakeholders" | name them: "the CFO", "the finance team", "the dev team" |
| "ecosystem" | name it: "the npm registry", "the Postgres extension set" |
<!-- human-writer:ignore-end -->

### Worked example (EN)

Bad (abstract):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Our solution helps businesses optimize their workflow.
<!-- human-writer:ignore-end -->

Good (concrete):

> We replaced a team's 14-tab Google Sheet reporting tracker with a single dashboard. They cut their Monday morning prep from 2 hours to 12 minutes.

### Worked example (EN) (longer)

Bad:

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> The platform empowers organizations to leverage real-time data for better decision-making across the enterprise.
<!-- human-writer:ignore-end -->

Good:

> The platform pushes live price moves from 8 marketplaces into Slack — channel by channel, region by region. When Bordeaux 2018 drops more than 5%, the trading desk knows within 90 seconds. They closed three buy orders last quarter on signals the tool surfaced before the broker emails.

### Worked example (FR)

Bad :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> Notre solution aide les entreprises à optimiser leurs processus.
<!-- human-writer:ignore-end -->

Good :

> On a remplacé le fichier Excel à 14 onglets que l'équipe utilisait pour son reporting par un seul tableau de bord. Résultat : la prep du lundi matin est passée de 2 heures à 12 minutes.

### Worked example (FR) (longer)

Bad :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> La plateforme permet aux organisations d'exploiter les données en temps réel pour une meilleure prise de décision.
<!-- human-writer:ignore-end -->

Good :

> La plateforme pousse les variations de prix de 8 marketplaces dans Slack, canal par canal et région par région. Quand Bordeaux 2018 baisse de plus de 5%, la salle de trading le sait en 90 secondes. Trois ordres d'achat clôturés ce trimestre sur des signaux que l'outil avait sortis avant les emails du courtier.

### How to apply

**WRITE mode.** Each time you reach for an abstract noun ("solution", "users", "data"), pause and ask: "What's the concrete version?" Write that instead.

**CLEAN mode.** Grep the draft for the abstract nouns in the table above. For each occurrence, either replace with a concrete equivalent or rewrite the sentence around the concrete version.

---

## 9. Vary transitions, drop the formal connectors (NEW)

**Definition.** AI-generated transitions are predictable and connector-heavy. Humans transition with simple conjunctions, restructure sentences, or skip transitions entirely.

**Why it works.** The connector-class AI tells are the formal-register conjunctions listed below. They appear when an LLM tries to make logical structure visible at the surface, which humans rarely do. We just write the next sentence.

### Forbidden transitions (EN)

<!-- human-writer:ignore-start (citation list: tells quoted, not used) -->
- Moreover
- Furthermore
- Additionally
- In addition
- Similarly
- Likewise
- In the same vein
- Conversely (when overused)
- On the other hand (when overused — fine sparingly)
- Thus
- Hence
- Therefore (when used as paragraph opener)
<!-- human-writer:ignore-end -->

### Forbidden transitions (FR)

<!-- human-writer:ignore-start (citation list: tells quoted, not used) -->
- En outre
- De plus
- Par ailleurs (as paragraph opener)
- D'ailleurs (as paragraph opener)
- En effet (as paragraph opener)
- Ainsi (as paragraph opener)
- De même
- À l'inverse (when overused)
- D'autre part
<!-- human-writer:ignore-end -->

### Human alternatives

- **"And"**: start a sentence with "And". Humans do this all the time; AI rarely does because LLMs were trained on edited prose.
- **"But" / "Yet" / "Still"**: sharper contrast than "however" or "conversely".
- **"The thing is,"**: pivot to the key point.
- **"That said,"**: mid-sentence is fine; opener is templated (don't use as paragraph opener if it's your only transition).
- **"One catch:"**: signals a complication.
- **"Or:"**: branching alternative.
- **Restructure**: sometimes the cleanest transition is no transition at all. Rewrite the next sentence to flow without a connector.

### FR alternatives

- **"Et"** : yes, start a sentence with "et". French allows it, even if school grammar disapproves.
- **"Mais"** : sharp pivot.
- **"Sauf que"** : informal contrast, very human.
- **"Le truc, c'est que"** : register varies but this is human.
- **"Bon,"** / **"Bref,"** : French rhythm markers.
- **"Sinon,"** : branching alternative.
- **Restructurer** : souvent, supprimer le connecteur et reformuler la phrase suivante est plus propre.

### Worked example (EN)

Bad (connector-heavy):

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> The actor scrapes prices from Amazon. Moreover, it tracks stock levels. Furthermore, it integrates with Slack. Additionally, it supports daily exports.
<!-- human-writer:ignore-end -->

Good (varied):

> The actor scrapes prices from Amazon. It also tracks stock levels. Slack integration ships in v2. Exports run daily — or hourly if you ask nicely.

### Worked example (FR)

Bad :

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> L'Actor récupère les prix depuis Amazon. En outre, il suit les niveaux de stock. De plus, il s'intègre à Slack. Par ailleurs, il supporte les exports quotidiens.
<!-- human-writer:ignore-end -->

Good :

> L'Actor récupère les prix depuis Amazon. Il suit aussi les stocks. L'intégration Slack arrive en v2. Exports quotidiens — ou horaires sur demande.

### How to apply

**WRITE mode.** Never use the forbidden list. When you reach a transition point, pick from the human alternatives or just restructure.

**CLEAN mode.** Grep for every forbidden transition. Delete and rewrite. This is one of the fastest, highest-impact CLEAN-mode operations.

---

## 10. Build in productive imperfection (NEW)

**Definition.** Humans pause, repeat for emphasis, change midstream, use casual contractions. AI hyper-corrects. A light imperfection ratio (1–2 instances per 500 words) registers as human without seeming sloppy.

**Why it works.** LLMs are trained to produce "good" text, which means trained-out of the small imperfections that real writing carries. Contractions, mid-sentence self-corrections, repetitions for emphasis, and casual interjections are statistically scarce in AI output and statistically common in human prose. Adding a small dose flips the signal.

### Imperfection categories (EN)

| Category | Example | Cadence |
|---|---|---|
| **Contractions** | "it's", "they're", "don't", "won't", "can't" | Use throughout — AI often expands these to "it is", "they are" |
| **Repetition for emphasis** | "It's good. Really good." | 1 per ~500 words |
| **Self-correction** | "The price moved 11% — actually closer to 12% if you include the fees." | 1 per ~700 words |
| **Casual interjections** | "Honestly,", "Look,", "Right,", "Yeah," | 1 per ~400 words (overlaps with #6 idiosyncratic markers) |
| **Mid-sentence pivot** | "We tried the cheaper proxy provider, but — well, you can guess." | 1 per ~800 words |
| **Trailing "or whatever"** | "...or whatever the equivalent is in your stack." | 1 per ~1000 words (informal only) |

### Imperfection categories (FR)

| Category | Example | Cadence |
|---|---|---|
| **Contractions orales** | "y'a" pour "il y a", "j'sais pas" (très informel uniquement) | Cas extrêmes — informel marketing OK, technique non |
| **Élisions courantes** | "c'est", "j'ai", "t'as" | "c'est" / "j'ai" partout ; "t'as" en informel |
| **Répétition** | "C'est bien. Vraiment bien." | 1 par ~500 mots |
| **Auto-correction** | "Le prix a bougé de 11% — plutôt 12% si on compte les frais." | 1 par ~700 mots |
| **Interjections** | "Franchement,", "Bon,", "Bref,", "Honnêtement," | 1 par ~400 mots |
| **Pivot en cours de phrase** | "On a essayé le proxy le moins cher, mais bon — vous voyez." | 1 par ~800 mots |
| **Trailing "quoi"** | "...enfin, ce genre de truc, quoi." | 1 par ~1000 mots (informel uniquement) |

### Worked example (EN)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
Without imperfection (hyper-correct AI):

> The price moved 11% in three weeks. This is significant. It is worth investigating the underlying cause.
<!-- human-writer:ignore-end -->

With imperfection (contractions + self-correction + interjection):

> The price moved 11% in three weeks — actually closer to 12% if you count the fees. That's significant. Honestly, worth digging into the cause.

### Worked example (FR)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
Sans imperfection :

> Le prix a bougé de 11% en trois semaines. C'est significatif. Il est utile d'investiguer la cause.
<!-- human-writer:ignore-end -->

Avec imperfection :

> Le prix a bougé de 11% en trois semaines — plutôt 12% si on compte les frais. C'est significatif. Franchement, ça mérite qu'on creuse.

### Calibration warning

Imperfection is dosed. Too much and you cross from "human writer" to "sloppy draft". The cadences in the tables above are upper bounds, not minimums. In a technical doc, lean toward the lower end. In casual marketing copy, the upper end works.

### How to apply

**WRITE mode.** Use contractions throughout (free). Add one self-correction or one casual interjection per ~500 words.

**CLEAN mode.** Search for expanded forms ("it is", "they are", "do not") and replace with contractions where the register allows. Identify one paragraph that reads as too-polished and inject a single self-correction.

---

## Bonus: how to combine techniques

The techniques compound. Applying #1 alone drops `sentence_length_stdev` flags. Applying #1 + #5 + #9 drops the three most common AI signatures simultaneously. Below is a worked example showing the cumulative effect.

### Starting paragraph (vanilla AI output, ~95 words)

<!-- human-writer:ignore-start (before-example, deliberately AI) -->
> In today's fast-paced e-commerce landscape, monitoring competitor prices is paramount. Our pricing intelligence tool offers a seamless, robust, and intuitive solution. It's not just about tracking prices — it's about empowering your team with actionable insights. Whether you're a startup or an enterprise, our platform helps you navigate the complexities of dynamic pricing. Moreover, it integrates seamlessly with your existing workflows. Ultimately, you'll be able to make data-driven decisions and stay ahead of the competition.

**Analyzer baseline:** suspect vocabulary count ~7 (`fast-paced`, `landscape`, `paramount`, `seamless` ×2, `robust`, `empowering`, `navigate`), tricolons 2, hedging openers 1 ("Ultimately"), em-dashes 1, forbidden constructions 2 ("It's not just X, it's Y", "Whether you're X or Y"), sentence-length stdev ~5. Estimated AI-probability: 85–95%.
<!-- human-writer:ignore-end -->

### Apply technique #5 first (cut hedging openers + forbidden constructions)

<!-- human-writer:ignore-start (intermediate state, still partly AI by design) -->
> In today's fast-paced e-commerce landscape, monitoring competitor prices is paramount. Our pricing intelligence tool offers a seamless, robust, and intuitive solution. The tool tracks prices and gives your team actionable insights. Our platform helps you navigate the complexities of dynamic pricing. It integrates seamlessly with your existing workflows. You'll be able to make data-driven decisions and stay ahead of the competition.
<!-- human-writer:ignore-end -->

<!-- human-writer:ignore-start (annotation quotes the removed tells) -->
→ Removed "It's not just X, it's Y", "Whether you're X or Y", "Moreover", "Ultimately". Score drops ~10–15 pts.
<!-- human-writer:ignore-end -->

### Apply technique #1 (vary sentence length)

<!-- human-writer:ignore-start (intermediate state, still partly AI by design) -->
> In today's fast-paced e-commerce landscape, monitoring competitor prices is paramount. Pricing changes hourly. Our tool tracks them, gives your team actionable insights, and integrates with your existing workflows. Make data-driven decisions. Stay ahead.
<!-- human-writer:ignore-end -->

→ Sentence-length stdev climbs from ~5 to ~10. Score drops another ~10 pts.

### Apply technique #4 (break tricolons) + technique #9 (vary transitions)

> Pricing changes hourly on Amazon. Our tool runs every 15 minutes against 50 SKUs. It surfaces the deltas. The dashboard is a Postgres view — no fancy UI.

→ Removed the "fast, reliable, scalable" tricolon energy, dropped the leftover connector, reframed around concrete actions. Score drops another ~5–10 pts.

### Apply technique #8 (concrete over abstract) + technique #2 (inject anecdote)

> Pricing changes hourly on Amazon during Q4. Our tool runs every 15 minutes against your 50 priciest SKUs and flags any move greater than 3%. The dashboard is a Postgres view — no fancy UI — because the team that needs it lives in Metabase anyway. We built this for one client in 2024 after they got undercut for six weeks straight before noticing. If you want the same setup, the whole thing is about 200 lines of Python on a cron.

→ Replaced "businesses", "your existing workflows", "actionable insights" with concrete nouns (Amazon, Q4, 50 SKUs, 3%, Postgres, Metabase). Added a real anecdote (2024 client, six weeks). Score drops another ~10–15 pts.

### Apply technique #6 (idiosyncratic markers) + technique #10 (imperfection)

> Pricing changes hourly on Amazon during Q4. Look — our tool runs every 15 minutes against your 50 priciest SKUs and flags any move greater than 3%. That's it. The dashboard is a Postgres view (no fancy UI) because the team that needs it lives in Metabase anyway. We built this for a mid-size retailer in 2024 after they got undercut for six weeks straight before noticing — well, before their CFO noticed. If you want the same setup, the whole thing is about 200 lines of Python on a cron. Bring your own categories.

→ Added "Look —" tic, added "That's it." fragment, added a parenthetical self-correction ("well, before their CFO noticed"), added a closing imperative ("Bring your own categories"). Score drops another ~5 pts.

**Final estimated AI-probability: 15–25%** versus 85–95% starting baseline. Same word count, same content, dramatically different signal.

### Order of operations summary

| Order | Technique | Reason |
|---|---|---|
| 1 | #5 Cut hedging openers | Highest words-saved, fastest fix |
| 2 | #9 Vary transitions | Cuts the connector class in one pass |
| 3 | #1 Vary sentence length | Statistical signal most analyzers test |
| 4 | #4 Break tricolons | Density signal — easy to target |
| 5 | #3 Asymmetric bullets | Only if the piece has lists |
| 6 | #8 Concrete over abstract | Compounds with #2 |
| 7 | #2 Inject opinion/anecdote | Highest authorial-signal move |
| 8 | #7 Digressions | Adds drift |
| 9 | #6 Idiosyncratic markers | Final personality layer |
| 10 | #10 Imperfection | Final humanity layer |

The first five fix the statistical signature. The last five inject the authorial signal.

---

## See also

- `tells-stylistic-en.md` / `tells-stylistic-fr.md` — vocabulary and construction lists that techniques #5, #8, #9 reference directly.
- `tells-statistical.md` — the metrics (sentence-length stdev, bullet parallelism, tricolon density, em-dash density) these techniques target.
- `tells-structural.md` — bullet, header, conclusion anti-patterns that techniques #3 and #4 disrupt.
- `adapter-marketing.md` / `adapter-short-comms.md` / `adapter-technical.md` / `adapter-editorial-seo.md` — content-type-specific calibration of these ten techniques.

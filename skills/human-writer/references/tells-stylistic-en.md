# Stylistic Tells — English

> Doctrine for the `human-writer` skill. Covers vocabulary, constructions, punctuation, voice, and surface tells specific to AI-generated English prose. Internal doctrine in English; examples target real AI patterns harvested in Phase 2 and cross-referenced against Wikipedia "Signs of AI writing", Hunting the Muse, The Augmented Educator, and ETBI Library.

## How to use this file

- **Tier 1 vocabulary** — treat as almost-always banned. Cap at 0–1 per 500 words even in domain-legitimate cases.
- **Tier 2 vocabulary** — contextual. Allowed in its native domain, banned when used as filler or as a synonym for a plain word.
- **Tier 3 vocabulary** — frequency-only. Any one word is fine; 5+ in a single paragraph is a tell.
- **AI constructions** — sentence-level patterns. Each instance is a stronger signal than any single word; 2+ in a 500-word piece almost always means LLM.
- **Punctuation tells** — surface-level signatures (em-dash, smart quotes, semicolons). Density alone is the signal.
- **Voice and POV tells** — first-person absence and royal "we" are the most overlooked detectors.

This file is the master reference for English. The deterministic analyzer (`scripts/analyze.py`) loads Tier 1 + Tier 2 from `scripts/rules.yaml`. Tier 3 is frequency-only and not yet wired into the analyzer.

---

## Suspect vocabulary — Tier 1 (High signal — almost always avoid)

Each entry: the word, why it's a tell, and the replacement.

### Metaphorical movement and discovery

- **delve / delving / dive deep into** — ChatGPT's signature verb. Real writers say "look at", "get into", or just skip the verb.
  → Replace with: *look at, get into, dig into, work through, study*
- **embark (metaphorical)** — "embark on this journey" is the canonical LLM opener. Real embarkations involve ships.
  → Replace with: *start, begin, set out*
- **navigate (metaphorical)** — "navigate the landscape" is template prose. Reserve for ships, planes, and websites.
  → Replace with: *work through, get around, deal with, handle*
- **journey (metaphorical)** — "your journey to success" is marketing-AI boilerplate.
  → Replace with: *path, process, what you go through, work*
- **unleash (metaphorical)** — "unleash the power of X" — AI loves the violence-as-metaphor.
  → Replace with: *release, let loose, set free, turn on*
- **harness (metaphorical)** — "harness the potential of AI" — same pattern as unleash.
  → Replace with: *use, put to work, channel, draw on*
- **unlock (metaphorical)** — "unlock new possibilities" is a Gemini favorite.
  → Replace with: *open up, give access to, find, discover (used sparingly)*
- **explore (metaphorical, in headers)** — "Let's explore..." as a section opener.
  → Replace with: *look at, here's, the X is*

### Inflated qualifiers

- **seamless / seamlessly** — flagged in 4/4 Phase 2 fixtures. The single most overused adjective in 2024–2026 LLM output.
  → Replace with: *smooth, easy, no friction, with no glue code*
- **robust** — outside statistics and engineering, this is filler.
  → Replace with: *solid, reliable, tough, sturdy, well-built*
- **transformative** — marketing-AI's favorite empty modifier.
  → Replace with: *big, important, that changes how X works (concrete)*
- **vibrant** — "vibrant community", "vibrant ecosystem" — empty visual praise.
  → Replace with: *active, busy, lively (with a concrete example)*
- **intricate** — used to inflate "complex" or "detailed".
  → Replace with: *complex, detailed, tangled, fiddly*
- **multifaceted** — almost always means "complicated and I won't be specific".
  → Replace with: *complex, with several parts, layered*
- **nuanced** — overused to signal sophistication without naming the nuance.
  → Replace with: *subtle, detailed, careful (name the detail)*
- **paramount** — when "most important" would do.
  → Replace with: *the most important, the key thing*
- **pivotal** — outside mechanical engineering and historical writing, filler.
  → Replace with: *key, important, decisive*
- **meticulous / meticulously** — "meticulously crafted" is template-tier.
  → Replace with: *careful, careful about details, with attention to (specific)*
- **comprehensive** — when "complete" or "full" works.
  → Replace with: *complete, full, covers everything, covers X, Y, and Z (be specific)*
- **holistic** — corporate-LLM filler.
  → Replace with: *full, all-around, end-to-end*
- **dynamic (used vaguely)** — "dynamic environment", "dynamic team" — empty.
  → Replace with: *fast-changing, active, busy (name what changes)*

### Marketing inflation

- **innovative** — empty self-praise.
  → Replace with: *new, fresh, different — and SHOW why*
- **cutting-edge / state-of-the-art** — late-2010s template.
  → Replace with: *new, current, the latest (with a date)*
- **revolutionary / game-changing / game-changer** — buyer-side eye-roll triggers.
  → Replace with: *changes how X works because Y (be specific)*
- **world-class / best-in-class / unparalleled** — unfalsifiable claims.
  → Replace with: *cite a benchmark, a number, or a comparison*
- **unprecedented** — almost never literally true.
  → Replace with: *new for this domain, the first time we've seen X*
- **optimal** — almost never measured.
  → Replace with: *the best for X, the one we picked, fastest/cheapest*

### Corporate jargon (calque from LLM training data)

- **leverage (as a verb meaning "use")** — financial jargon escaped into prose.
  → Replace with: *use, rely on, build on*
- **foster (metaphorical)** — "foster collaboration" — bureaucrat-LLM speak.
  → Replace with: *help, build, encourage, support*
- **empower** — outside HR and training contexts, empty.
  → Replace with: *help, let, give the means to, give X the power to*
- **tapestry (metaphorical)** — "rich tapestry of cultures" — purple-prose LLM.
  → Replace with: *mix, range, collection*
- **realm (metaphorical)** — "in the realm of" — fantasy-novel filler.
  → Replace with: *field, area, world, in X*
- **synergy** — universally despised business jargon, but LLMs still produce it.
  → Replace with: *fit, work together, X helps Y*
- **ecosystem (metaphorical)** — when no organism is involved.
  → Replace with: *system, network, set of tools, market*
- **paradigm** — academic filler outside Kuhnian discussions.
  → Replace with: *approach, way, model*
- **framework (vague)** — when no actual framework exists.
  → Replace with: *approach, plan, way of thinking about X*
- **bandwidth (metaphorical)** — "I don't have the bandwidth" — Slack-LLM speak.
  → Replace with: *time, capacity, room*
- **wheelhouse** — over-used metaphor for skill area.
  → Replace with: *area, specialty, what I'm good at*
- **deep dive** — meeting-LLM speak.
  → Replace with: *close look, full breakdown*
- **double-click on (metaphorical)** — UX metaphor outside software.
  → Replace with: *focus on, dig into, look closer at*
- **unpack (metaphorical)** — overused.
  → Replace with: *break down, explain, look at the parts of*
- **ladder up to / north star / table stakes / low-hanging fruit / move the needle / boil the ocean / drink from the firehose / level the playing field / raise the bar / hit the ground running / think outside the box / swim lane / bake in / dial in / lean into / table the discussion / circle back / take this offline / ping (verb) / action item / deliverable / learnings (for "lessons")** — corporate-meeting jargon family. Each one alone is suspicious; two in one paragraph is a confession.
  → Replace with: plain English appropriate to context. "Action item" → "task". "Circle back" → "come back to". "Ping" → "message". "Learnings" → "lessons" or "what we learned".

### Verbing of nouns (LLM tic)

- **ideate** — say "come up with ideas" or "brainstorm".
- **operationalize** — say "put into practice" or "turn into a process".
- **incentivize** — say "give X a reason to" or "reward".
- **prioritize (when overused)** — fine sparingly; say "put X first" in plain prose.
- **strategize** — say "plan" or "think through".
- **conceptualize** — say "think of X as" or "model".
- **contextualize** — say "put X in context of Y".
- **gamify** — narrow term, fine in product design; tell in general prose.
- **monetize (when vague)** — say "make money from X" and be specific.

---

## Suspect vocabulary — Tier 2 (Medium signal — contextual)

These words have legitimate uses but become tells when used as fillers or piled up. Each entry lists the legitimate use case and the tell pattern.

### Connectors and transitions

- **moreover / furthermore / additionally** — *OK*: rare formal essay. *Tell*: paragraph-opening connector in marketing or blog prose. → Use *also*, *and*, *plus*, or just start a new sentence.
- **however** — *OK*: contrast in formal writing. *Tell*: every other paragraph. → Use *but* at the start of a sentence (yes, it's fine).
- **consequently / thus / hence / therefore** — *OK*: logical argument. *Tell*: padding in casual prose. → Use *so*.
- **notably / particularly / specifically** — *OK*: introducing a real example. *Tell*: standalone qualifier with no example following.

### Vague qualifiers

- **crucial / vital / essential** — *OK*: when something is genuinely required. *Tell*: every adjective in a marketing page. → Drop or replace with *the most important*, *the one that matters*.
- **key (as a vague qualifier)** — *OK*: "the key insight is X" with the actual insight. *Tell*: "key feature", "key benefit" without specifics. → Drop or name the specific thing.
- **important** — *OK*: when followed by why. *Tell*: standalone. → Drop or say why.
- **significant / considerable / substantial / notable / prominent** — *OK*: with a number. *Tell*: empty modifier. → Use the number.

### Action verbs (motivational LLM tics)

- **elevate** — *OK*: physical lifting, music. *Tell*: "elevate your strategy". → *Raise, lift, improve, push up*.
- **streamline** — *OK*: process redesign with detail. *Tell*: vague optimization promise. → *Simplify, cut steps, speed up*.
- **optimize** — *OK*: technical (compiler, query). *Tell*: marketing filler. → *Improve, tune, make better at X*.
- **enable** — *OK*: technical (feature flag). *Tell*: filler. → *Let, allow, make X possible*.
- **facilitate** — *OK*: bureaucratic procedure. *Tell*: filler. → *Help, make easier, smooth*.
- **leverage (as noun)** — *OK*: finance. *Tell*: anywhere else. → *Use, advantage*.

### Discovery verbs (template openers)

- **explore / discover / uncover / reveal / unveil / showcase** — *OK*: genuine novelty. *Tell*: section-opener filler. → *Look at, show, here is*.
- **highlight / emphasize / illustrate / demonstrate / exemplify / embody** — *OK*: when introducing a concrete example. *Tell*: every paragraph. → *Show, mean, prove*.
- **encapsulate / encompass / comprise / constitute / signify / denote / indicate / suggest / imply / convey** — *OK*: precise definitional writing. *Tell*: filler. → *Mean, include, cover, show*.
- **articulate / elucidate / expound / posit / propose / advocate / champion** — *OK*: academic argument. *Tell*: blog prose. → *Say, explain, suggest, argue, support*.

### Caretaking verbs

- **foster / nurture / cultivate / hone / refine / polish / perfect** — *OK*: gardening, craft. *Tell*: stacked in business prose. → *Build, grow, work on, get better at*.

### Beauty and superlative adjectives

- **exquisite / elegant / intuitive / immersive / engaging / captivating / compelling / riveting / gripping / breathtaking / awe-inspiring / mind-blowing / stunning** — *OK*: a single one in genuine review prose. *Tell*: two or more per paragraph. → Pick the most concrete one or use a specific descriptor (smooth, fast, clear, surprising).
- **remarkable / extraordinary / exceptional / outstanding / phenomenal / spectacular / magnificent / splendid / marvelous / fabulous / fantastic / terrific / superb / excellent / brilliant** — *OK*: one in a personal recommendation. *Tell*: any LLM marketing page. → Pick one or remove.
- **masterful / masterpiece / hallmark / paragon / epitome / quintessence / archetype** — *OK*: art criticism. *Tell*: anywhere else. → *The best example, the standard, a classic*.

### Foundation metaphors

- **cornerstone / bedrock / foundation / pillar / backbone / lifeblood / heart and soul / essence / core / kernel / nucleus / hub / nexus** — *OK*: one per piece. *Tell*: two or more in a paragraph or as section openers ("The cornerstone of our approach..."). → *The main, the central, the key part of*.
- **crossroads / intersection / convergence / confluence / synthesis / amalgamation / fusion / integration** — *OK*: genuine joining of two things. *Tell*: jazz-up filler. → *Joining, mix, blend, where X meets Y*.

---

## Suspect vocabulary — Tier 3 (Low signal — frequency only)

Individually harmless. Flag when 5+ appear in a single paragraph. (The current analyzer does not yet measure paragraph-level Tier 3 density; treat this as authorial discipline.)

**Quantifiers:** numerous, various, several, multiple, many, significant, considerable, substantial, notable.

**Importance markers:** important, prominent, leading, foremost, premier, top, primary, principal, chief, major, central, fundamental, basic, essential, necessary, requisite, indispensable, integral, instrumental, vital, critical, pivotal, decisive, definitive, conclusive.

**Completeness markers:** comprehensive, exhaustive, thorough, complete, total, full, entire, whole, holistic, integrated, unified, cohesive.

**Smoothness markers:** seamless, smooth, fluid, effortless, frictionless, painless, hassle-free, straightforward, easy, intuitive, user-friendly, accessible, approachable.

**Warmth markers:** inclusive, welcoming, friendly, warm, inviting, embracing, encompassing.

**Scale markers:** far-reaching, wide-ranging, broad, expansive, vast, immense, enormous, gigantic, massive, mammoth, colossal, monumental, herculean, titanic, towering.

**Growth markers:** soaring, skyrocketing, exploding, surging, booming, thriving, flourishing, prospering, succeeding, excelling, dominating.

**Pioneer markers:** leading, pioneering, trailblazing, groundbreaking, revolutionary.

When you see 5+ of these in one paragraph, it's almost certainly an LLM — even if no Tier 1 word appears.

---

## AI constructions

Sentence-level patterns. Stronger signals than any individual word because they shape paragraph rhythm. Each pattern: severity, why it's a tell, rewrite suggestion.

### Antithesis amplifiers (high severity)

- **"It's not just X, it's Y"** / **"Not just X — Y"** / **"More than just X, this is Y"** / **"X is more than just a Y"** — the single most overused construction in 2024–2026 ChatGPT output. The frame promises depth without delivering it.
  → Rewrite as: a concrete claim. "It's not just a pricing tool, it's a strategic asset." → "The pricing tool exposes margin tiers per SKU — same data the buyers use."

### Vague scene-setters (high severity)

- **"In today's fast-paced world"** / **"In an era where"** / **"In a digital landscape where"** / **"In the modern age of"** / **"Gone are the days when..."** / **"Imagine a world where..."** / **"Picture this:"** / **"What if I told you..."** — present-tense scene-setters with no specific date, event, or place.
  → Rewrite as: a date, a specific event, or jump straight in. "In today's fast-paced world of e-commerce..." → "Since Amazon's 2024 algorithm update..."

### Dual-audience hedges (medium severity)

- **"Whether you're X or Y"** / **"Whether you're a [persona] looking to [verb] or a [persona] hoping to [verb]"** — default move when the writer hasn't chosen an audience.
  → Rewrite as: pick one audience and write for them. Or use the construction only when the answer genuinely branches by audience.

### Dramatic openers (medium severity)

- **"Buckle up, because..."** / **"Hold on to your hats..."** / **"Get ready for..."** — false urgency.
  → Rewrite as: just say what's coming.
- **"Let's break it down."** / **"Let's dive in."** / **"Let's get into it."** — empty section opener.
  → Rewrite as: state the topic. "Pricing strategy — start with margin floors."
- **"Here's the thing:"** / **"Here's the deal:"** / **"Here's why:"** — pseudo-conversational filler.
  → Rewrite as: drop the opener and state the thing.
- **"Spoiler:"** / **"Spoiler alert:"** / **"Plot twist:"** — TikTok-LLM speak.
  → Rewrite as: drop the marker and make the claim.

### Pseudo-summaries (medium severity)

- **"Long story short,"** / **"To be clear,"** / **"To put it simply,"** / **"In a nutshell,"** / **"In short,"** — used when the long version was never given.
  → Rewrite as: just give the simple version with no preamble.
- **"At the end of the day,"** / **"When all is said and done,"** / **"All things considered,"** — cliché summaries.
  → Rewrite as: drop entirely or state the conclusion directly.

### Catalog frames (medium severity)

- **"From X to Y to Z, A has it all"** / **"From X to Y, A covers everything"** — exhaustiveness claim that's almost never true.
  → Rewrite as: name the two or three things that actually matter.
- **"Look no further than..."** — infomercial phrasing.
  → Rewrite as: drop the frame, name the thing.

### Stage-direction openers (medium severity)

- **"Enter X"** / **"Enter, stage left, X"** — theatrical metaphor.
  → Rewrite as: "X solves this." / "X does Y."
- **"Say goodbye to X, hello to Y"** — infomercial.
  → Rewrite as: "X is gone. Y replaces it."

### Pseudo-Socratic Q&A (medium severity)

- **"The result? X."** / **"The takeaway? X."** / **"The catch? X."** — single-word-question-then-answer.
  → Rewrite as: just state X. "The result is faster runs." → "Runs are faster."
- **"Why does this matter? Because..."** / **"What does this mean? It means..."** — fake-dialogue framing.
  → Rewrite as: state the consequence directly.
- **"You might be wondering..."** / **"You might be asking..."** / **"You might be thinking..."** — mind-reading filler.
  → Rewrite as: just answer the implied question.

### Hedging openers (low to medium severity)

Cut entirely. If the qualifier matters, state it inline. If not, drop it.

- **"It's important to note that"** / **"It's worth noting that"** / **"It bears mentioning that"** / **"It cannot be overstated that"** — every one of these is droppable.
- **"Suffice it to say that"** / **"Needless to say,"** — academic-LLM speak.
- **"Of course,"** / **"Indeed,"** / **"In fact,"** / **"As a matter of fact,"** — filler emphasis.
- **"To be sure,"** / **"Granted,"** / **"Admittedly,"** — hedge openers; fine occasionally, never twice in 500 words.
- **"Arguably,"** / **"Some might argue that"** / **"One could say that"** — passive-voice opinion-laundering.
  → Rewrite as: just state the claim, or state who actually argues it.
- **"Keep in mind that"** / **"Bear in mind that"** / **"Worth mentioning that"** — paragraph-opener droppables.
- **"That said,"** as a paragraph opener — fine mid-sentence, banned as opener.

### Conclusion templates (medium severity)

Never start a paragraph (especially a closing one) with these. They mark the conclusion as AI-templated.

- **"In conclusion,"** / **"To conclude,"** / **"To summarize,"** / **"To wrap up,"** / **"In closing,"** / **"Finally,"** / **"Lastly,"** — never use as paragraph openers.
- **"Ultimately,"** / **"All in all,"** / **"At the end of the day,"** — same problem.
- **"As we've seen,"** / **"As discussed,"** / **"As mentioned earlier,"** — recap filler.
- **"Going forward,"** / **"Moving forward,"** / **"Looking ahead,"** — false-progress markers.
- **"The future is bright,"** / **"Stay tuned for..."** / **"The journey doesn't end here"** / **"This is just the beginning"** / **"The possibilities are endless"** — empty inspirational closers.
  → Rewrite as: end with a concrete next action, a specific recommendation, or a number. Or just stop writing.

### Stacked formulas

- **"Not only X, but also Y"** — replace with "X and Y" or two sentences.
  → Bad: "The actor not only scrapes prices but also tracks stock." Good: "The actor scrapes prices and tracks stock."
- **"By doing X, you can Y" + "moreover, Z"** — the connector chain (X → moreover → furthermore → ultimately) is structural. Break with periods, paragraph breaks, and direct claims.

### Direct topic markers

- **"Dive deep into"** / **"In the realm of"** / **"At the heart of"** / **"At its core,"** — never use. State the topic directly.

---

## Em-dash discipline

**Ban the literal em-dash "—" (U+2014). Target 0 in body prose; hard cap ≤ 1 per 1000 words.** This is the single most recognisable AI surface signature in 2024–2026 output: readers and detectors alike now treat a stray "—" as a tell on sight, regardless of grammar. Every em-dash must be converted to a comma, colon, period, or parentheses (see the replacement table below). En-dash "–" (U+2013) in numeric ranges (10–15, 2014–2023) and the minus sign "−" are fine and are NOT this tell — only the wide "—" is. When cleaning or writing, sweep the text for the "—" character explicitly and remove every one; do not leave "a few" as acceptable.

### Why so strict

Published 2024–2025 studies on ChatGPT output measure em-dash density at 3–5× typical human writing rates. Even when the *individual* em-dash is grammatically perfect, the *aggregate frequency* is the signature. Density alone identifies the source.

### Replacement table by context

| Em-dash context | Replacements |
|---|---|
| **Apposition** ("The CEO — a former trader — said...") | commas: "The CEO, a former trader, said..." / parentheses: "The CEO (a former trader) said..." / restructure: "The CEO said... She's a former trader." |
| **Contrast** ("Cheap — but powerful.") | period: "Cheap. But powerful." / comma + but: "Cheap, but powerful." / colon: "Cheap: powerful." |
| **Range** ("pages 12 — 18") | en-dash: "pages 12–18" / "to": "pages 12 to 18" |
| **Parenthetical aside** ("The tool — released yesterday — runs...") | parentheses: "The tool (released yesterday) runs..." / comma pair: "The tool, released yesterday, runs..." |
| **Dramatic pause / setup** ("She knew — finally — the answer.") | period: "She knew. Finally. The answer." / comma: "She knew, finally, the answer." / restructure: "Finally, she knew the answer." |

### Quick rewrites

- "Quick — fast — easy." → "Quick. Fast. Easy."
- "The tool — built for traders — runs daily." → "The tool, built for traders, runs daily."
- "It works — most of the time." → "It works (most of the time)."

A handful of em-dashes is fine for emphasis. A surplus reads as LLM regardless of vocabulary.

---

## Tricolon rationing

"X, Y, and Z" three-item lists are the prose equivalent of em-dashes: fine in moderation, deadly in series. **Cap: 1 tricolon per 200 words.**

Vary list sizes — use lists of 2, 4, or 5 items. Use commas, em-dashes (sparingly), or asyndeton ("X, Y, Z" with no "and"). Don't let every list close with ", and Z".

- Bad: "The actor is fast, reliable, and scalable. It handles bundles, variants, and locales. It runs daily, weekly, and on demand."
- Good: "The actor handles bundles and variants across 12 locales. It runs daily — or on demand for ad-hoc audits."

---

## Punctuation tells

Surface-level signatures. Each one alone may not damn a draft, but density is diagnostic.

### Em-dash overuse

See above. Universal tell.

### Smart-quotes inconsistency

LLMs paste content with curly quotes ("/" /'/') mixed with straight quotes ("/'). Humans either use one consistently (most platforms auto-convert) or the other. Mixed quotes within a single paragraph is a strong signal that the text was pasted from multiple LLM sessions.

- **Fix:** pick one (straight ASCII is safest for technical writing; curly for editorial) and normalize the entire piece.

### Oxford comma uniformity

AI almost always uses the Oxford comma ("X, Y, and Z"). Humans are variable — many drop it ("X, Y and Z"), especially in British English or journalistic style.

- **Tell:** every list of 3+ items has a comma before "and", with zero exceptions across 1000+ words.
- **Fix:** intentionally drop the Oxford comma on 20–30% of lists, especially in shorter or less-formal sentences.

### Semicolon overuse

AI loves semicolons; especially in lists; even when periods or commas would be cleaner. Humans use semicolons rarely.

- **Cap:** ≤ 2 semicolons per 1000 words.
- **Fix:** replace with periods or commas. Reserve semicolons for genuinely linked independent clauses or list items containing internal commas.

### Ellipsis style

AI uses the typographic ellipsis "…" (U+2026). Humans (outside academic copy-editing) almost always type three periods "..." manually.

- **Tell:** every ellipsis in the draft is "…" rather than "...".
- **Fix:** normalize to three ASCII periods. Or, better, replace ellipses with periods entirely — LLMs use them as "thinking pauses" where humans would just stop the sentence.

### Bold-as-emphasis density

AI bolds 3–5+ phrases per section, often the same kind of phrase (definitions, key takeaways, button names).

- **Cap:** ≤ 2 bold spans per 200 words.
- **Fix:** remove all but the most necessary bold. If everything is emphasized, nothing is.

### Italics as concept marker

AI italicizes any abstract noun on first mention (*scalability*, *resilience*, *quality*) as if introducing a technical term. Humans only italicize for actual emphasis, foreign words, or genuine first-use definitions.

- **Tell:** italicized abstract nouns that aren't being defined.
- **Fix:** strip the italics. Define the term inline if needed.

### Colon-driven structure

AI uses colons to introduce every claim: like this. Humans use colons sparingly.

- **Cap:** ≤ 4 mid-sentence colons per 1000 words (excluding URLs, ratios, times).
- **Fix:** replace with periods or recast as a single sentence.

---

## Voice and POV tells

Often missed by vocabulary scanners. These are the most reliable detectors at long-form scale.

### Royal "we" without referent

AI defaults to "we" — "we believe", "we think", "we recommend" — without ever identifying who "we" is. Real publications either say "I" or attribute claims to a named team / company / institution.

- **Tell:** "we" appears 10+ times in 1000 words but the piece is signed by one person and "we" is never defined.
- **Fix:** switch to "I" (single author) or name the team ("the platform team", "our data group") on first use.

### Vague second-person

AI defaults to "you might want to consider", "you may find that", "you could potentially" — hedged second-person without commitment.

- **Tell:** second-person verbs nested in modal hedges ("might", "could", "may", "would") more than 4× per 500 words.
- **Fix:** use plain imperative ("do X") or assertive declarative ("X works"). Drop the hedges.

### Hedged first-person

AI says "I would argue that...", "I might suggest...", "I would venture to say...".

- **Tell:** first-person verbs always wrapped in modals.
- **Fix:** "I argue", "I think", "I say". Or drop the first-person frame and state the claim.

### Absent first-person entirely

A 1000-word personal essay or opinion piece with zero "I" is almost certainly LLM. Humans writing in their own voice slip into first-person within the first few paragraphs.

- **Tell:** 0 occurrences of "I" in a piece that should have a personal voice (essay, opinion, anecdote-driven blog).
- **Fix:** add one first-person anecdote, opinion, or aside per ~300 words. Even just "I noticed..." breaks the pattern.

### Passive voice for opinion-laundering

AI passes opinions through passive constructions: "it is generally believed that...", "it has been said that...", "it is widely understood that...". This hides the source.

- **Tell:** passive-voice claim-frames with no source named.
- **Fix:** name the source ("the FT reported...", "in 2024 Anthropic published...") or own the claim ("I think...").

### Apologetic openers

AI starts paragraphs with "While X is true, Y..." — a hedge that pre-empts disagreement.

- **Tell:** 3+ paragraphs start with "While..." in a 1000-word piece.
- **Fix:** state Y and let the reader handle X. Or move X to a separate sentence.

---

## Worked rewrites (LLM → human)

Each example below is a real fragment harvested in Phase 2 from ChatGPT-4 or Gemini output. The rewrite removes the tells while keeping the meaning.

### Example 1 — marketing opener

> **LLM:** In today's fast-paced digital landscape, businesses are constantly seeking innovative solutions to navigate the intricate challenges of modern e-commerce. Our cutting-edge platform empowers teams to unlock new possibilities and embark on a transformative journey.

Tells: "In today's fast-paced", "digital landscape", "constantly", "innovative", "navigate", "intricate", "cutting-edge", "empowers", "unlock new possibilities", "embark", "transformative", "journey".

> **Human:** Most e-commerce platforms break on bundles or multi-currency pricing. Ours doesn't. Here's how the pricing engine handles both — with two examples below.

### Example 2 — feature list closer

> **LLM:** Whether you're a startup founder navigating the complexities of growth, or an enterprise CTO seeking to streamline operations, our solution offers a seamless, robust, and intuitive experience that empowers your team to thrive in today's competitive landscape.

Tells: "Whether you're", "navigating", "complexities", "streamline", "seamless", "robust", "intuitive", "empowers", "thrive", "competitive landscape", tricolon ("seamless, robust, and intuitive").

> **Human:** Pricing engineers at series-B startups use this to ship per-tier rules in a day. CTOs at larger firms use it to consolidate three legacy pricers. The setup time is the same: forty minutes.

### Example 3 — conclusion

> **LLM:** In conclusion, the transformative power of AI is reshaping the realm of business operations. Ultimately, by leveraging these cutting-edge tools, organizations can unlock unprecedented value and embark on a journey toward unparalleled success.

Tells: "In conclusion", "transformative", "realm", "Ultimately", "leveraging", "cutting-edge", "unlock", "unprecedented", "embark", "journey", "unparalleled".

> **Human:** The pricing team cut markup-error rates from 7% to 0.4% in six weeks using this stack. Three of the changes were one-liners. The full diff is in the appendix.

### Example 4 — listicle item

> **LLM:** Moreover, it's important to note that fostering a culture of innovation is paramount. Companies that fail to leverage this pivotal opportunity will find themselves navigating an increasingly intricate competitive landscape.

Tells: "Moreover", "it's important to note", "fostering", "paramount", "leverage", "pivotal", "navigating", "intricate", "competitive landscape".

> **Human:** Companies that don't run experiments fall behind. The ones that do — even badly — beat the ones that argue about the experiment framework for six months.

### Example 5 — antithesis trap

> **LLM:** It's not just a scraper, it's a strategic intelligence asset. Not just data — insights. Not just insights — actionable transformation.

Tells: the antithesis chain ("not just X, it's Y" × 3), "strategic", "actionable", "transformation".

> **Human:** The scraper pulls 14 fields per SKU, twice a day, for 38 retailers. Margin analysts in three teams use the output to set Friday's price ladder.

---

## Frequency caps (consolidated reference)

| Tell | Cap | Source |
|---|---|---|
| Em-dash "—" (U+2014) | **0 (target); hard cap ≤ 1 per 1000 words** | Phase 2 fixtures + 2024–2025 ChatGPT studies; the top surface signature |
| Tricolon ("X, Y, and Z") | ≤ 1 per 200 words | Wikipedia "Signs of AI writing" |
| Semicolon | ≤ 2 per 1000 words | The Augmented Educator |
| Mid-sentence colon | ≤ 4 per 1000 words | Phase 2 marketing fixtures |
| Bold span | ≤ 2 per 200 words | Hunting the Muse |
| Tier 1 word | ≤ 1 per 500 words | This doctrine |
| Tier 2 word | ≤ 2 per 500 words | This doctrine |
| Tier 3 word | ≤ 4 per paragraph | This doctrine |
| AI construction | 0 per piece (target) | This doctrine |
| "While X..." paragraph opener | ≤ 2 per 1000 words | Voice tells, this doctrine |
| Modal-hedged second person | ≤ 4 per 500 words | Voice tells, this doctrine |
| "We" without referent | ≤ 4 per 1000 words (if unsigned) | Voice tells, this doctrine |

---

## Doctrinal sources

- **Wikipedia, "Signs of AI writing"** (Editor essay, en.wikipedia.org) — the canonical community-curated taxonomy. Source for: antithesis amplifiers, scene-setters, dual-audience hedges, conclusion templates, em-dash overuse, tricolon overuse, Oxford comma uniformity.
- **Hunting the Muse, "How to tell if writing is AI"** — source for: bold-as-emphasis density, italics-as-concept marker, beauty adjective stacking, foundation metaphor frequency.
- **The Augmented Educator, "Ten telltale signs of AI-generated content"** — source for: semicolon overuse, ellipsis style ("…" vs "..."), Tier 3 quantifier stacking, growth-marker piling.
- **ETBI Library, "AI signs"** — source for: corporate-jargon family (synergy, ecosystem, paradigm, bandwidth), verbing of nouns, royal "we" pattern.
- **Phase 2 fixtures** (this skill, 2026-05) — empirical: 4/4 ChatGPT/Gemini/Sonnet outputs exceeded em-dash cap; 4/4 used at least one antithesis amplifier; 3/4 used "in today's fast-paced" or close variant.

---

## Quick reference — top 20 tells (for fast triage)

If a draft hits any of these, rewrite before publishing:

1. `delve` or `dive deep into`
2. `seamless` / `seamlessly`
3. `leverage` (as verb)
4. `robust` outside engineering/stats
5. `transformative`
6. `journey` (metaphorical)
7. `embark on`
8. `unlock new possibilities`
9. `harness the power of`
10. `it's not just X, it's Y`
11. `in today's fast-paced world`
12. `whether you're X or Y` (default audience-hedge)
13. `dive deep into the realm of`
14. `it's important to note that`
15. `in conclusion,` / `ultimately,` as paragraph opener
16. ANY literal em-dash "—" (U+2014) in body prose, convert every one to comma/colon/period/parentheses (en-dash "–" in ranges is fine)
17. Every 3-item list closes with `, and Z` (no asyndeton, no variation)
18. Every paragraph starts with a transition word (`moreover`, `furthermore`, `additionally`, `however`)
19. Zero `I` in a 1000-word opinion piece
20. Bolded phrase every 3–4 sentences

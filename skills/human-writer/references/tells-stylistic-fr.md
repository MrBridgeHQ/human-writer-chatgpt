# Stylistic Tells — French

> Doctrine for the `human-writer` skill, French side. Same axes as `tells-stylistic-en.md` but covers FR-specific patterns. Internal doctrine is in English; examples are in French because that is the surface the analyzer matches against.

French ChatGPT output is *louder* than English ChatGPT output for two structural reasons:

1. The model leans on the literary register it learned from journalistic French (`Le Monde`, `Les Échos`, encyclopedic prose). This register is naturally bombastic — "véritable", "incontournable", "indéniablement" — and it reads as marketing copy when applied to anything else.
2. English-language formulas leak through as calques: `leverage` → "tirer parti de", `navigate` → "naviguer dans", `address an issue` → "adresser un enjeu". A native ear catches these immediately; the model never does.

This file's job: codify which words, phrases, openers, closers, and typographic choices are tells in French, with severity and rewrite.

---

## Suspect vocabulary (FR)

The Phase 2 FR baseline (a short relance email) flagged em-dash density above all else. Suspect vocabulary did not trigger because the email was short — but it would in a 600-word marketing piece. The list below is calibrated against typical ChatGPT FR output.

**Hard rule.** Never use 2+ tier-1 items in the same paragraph. Cap any single tier-1 item at 1 per 500 words. Treat tier-1 items the way you would treat the words "delve" or "tapestry" in English: even one is suspicious; two is a giveaway.

**Soft rule.** Tier-2 items are legitimate in their domain. Track frequency: 3+ tier-2 items in a 300-word paragraph = the paragraph reads as AI-generated. Cap any single tier-2 item at 2 per 500 words.

**Pure-frequency rule.** Tier-3 items are individually invisible but flag the prose when 5+ co-occur in a single paragraph. The detector treats tier-3 differently: it counts cluster density, not absolute occurrence.

### Tier 1 — High signal (always avoid)

These are the equivalents of English `delve`, `tapestry`, `realm`. Each line: the phrase, why it's a tell, a human alternative.

#### Connectors and meta-comments

- **"en effet"** (paragraph opener) — Why: AI uses it as a generic "moreover" connector. Native FR uses "en effet" tightly, to justify a *just-stated* claim. Alternative: drop it, or "en fait" / "d'ailleurs" / Ø.
- **"il convient de noter"** / "il est important de noter" — Why: meta-textual hedge; reads as report-writing. Alternative: "à noter", or just state the fact.
- **"il convient de souligner"** / "il convient de rappeler" / "il convient de préciser" — Same family. Alternative: drop the prefix, state the claim.
- **"rappelons que"** / "soulignons que" / "précisons que" / "notons que" — Pedantic, schoolbook. Alternative: state the fact without the meta-frame.
- **"force est de constater"** / "force est d'admettre" — Why: literary cliché, AI uses it for any factual observation. Alternative: "on constate" / "il est clair que" / "manifestement".
- **"il s'agit là de"** — Why: heavy demonstrative, AI uses it to *name* what was just said. Alternative: name it directly, no "il s'agit".
- **"c'est dans ce contexte que"** — Why: chronological filler. Alternative: time-stamp the event ("en mars 2026...") or omit.
- **"dans cette perspective"** / **"dans cette optique"** — Why: meta-textual signpost. Alternative: drop it, the next sentence carries the logic.
- **"à cet égard"** — Same. Drop or use "là-dessus" / "sur ce point".
- **"il n'est pas anodin de"** / **"il n'est pas exagéré de dire"** / **"il ne fait aucun doute que"** — Why: triple-hedge openers; AI uses them to inflate a banal claim. Alternative: state the claim flat.
- **"nul ne saurait contester"** / **"comme chacun sait"** / **"comme nul ne l'ignore"** — Why: rhetorical appeal-to-authority that no native writer uses unless ironically. Alternative: drop.

#### Adverbs of certainty

- **"résolument"** / **"pleinement"** / **"fondamentalement"** — Why: intensifiers AI sprinkles on adjectives. Alternative: drop them; if the adjective needs a boost, change the adjective.
- **"indéniablement"** / **"assurément"** / **"manifestement"** / **"incontestablement"** / **"indubitablement"** — Why: heavy "of course" adverbs. AI uses them to assert authority. Alternative: drop or use "clairement" / "visiblement".
- **"à n'en pas douter"** — Same. Drop.

#### Spatial-temporal abstractions

- **"dans un monde où"** / **"dans un univers où"** — Why: meta-frame opener. Alternative: name the year, the event, the actor.
- **"à l'ère du numérique"** / **"à l'ère de l'IA"** / **"à l'heure où"** — Same family. Alternative: a date, a fact.
- **"aux quatre coins du"** (metaphorical, e.g., "monde", "globe") — Why: lyrical cliché. Alternative: name the regions, or "partout".
- **"au cœur de"** (when not literal anatomy/geography) — Why: AI inflates "in" or "inside" with "au cœur de". Alternative: "au centre de" / "dans" / "au milieu de" / Ø.
- **"au sein de"** — Same. AI uses it for any "in" inside a noun phrase. Alternative: "dans", "à l'intérieur de", or restructure.
- **"au-delà de"** / **"par-delà"** — Why: overused metaphorical scope-broadener. Alternative: "plus que", "au lieu de", "en plus de".
- **"à mille lieues de"** / **"à des années-lumière"** — Why: poetic cliché. Alternative: state the distance concretely or drop.

#### Comparators

- **"à l'instar de"** / **"à l'image de"** — Why: literary "like X" that AI defaults to instead of "comme". Alternative: "comme", "à la manière de".
- **"à l'aune de"** (calque, partly) — Why: AI uses it as a heavy "in light of". Alternative: "par rapport à" / "au regard de" (sparingly) / "à la mesure de".
- **"à la lumière de"** — Calque of "in the light of". Alternative: "à partir de" / "compte tenu de" / "vu".
- **"au regard de"** / **"compte tenu de"** / **"eu égard à"** — Administrative French. AI overuses for "given that". Alternative: "vu" / "puisque" / "étant donné".

#### Metaphorical inflators

- **"véritable"** (as intensifier, e.g., "véritable révolution") — Why: AI's go-to amplifier for nouns. Alternative: drop or use a concrete number/fact.
- **"incontournable"** — Why: marketing cliché now associated with AI prose. Alternative: "indispensable" (sparingly), "central", "incontournable" only if literally unavoidable.
- **"phare"** (as adjective: "produit phare", "marque phare") — Same. Alternative: "principal", "le plus vendu", name a specific reason.
- **"emblématique"** / **"iconique"** — Why: marketing inflators. Alternative: name what makes it notable.
- **"révolutionnaire"** (outside literal politics) — Calque of "revolutionary". Alternative: "qui change la donne", "neuf", "inédit" — sparingly.
- **"transformatif"** — Calque of "transformative", barely exists in literary French. Alternative: "décisif" / "déterminant".
- **"robuste"** (non-technical) — Calque of "robust". Alternative: "solide", "fiable", "qui tient la route".
- **"à la croisée des chemins"** — Why: AI's go-to for "at a turning point". Alternative: name the choice.

#### Structural metaphors

- **"le maillon essentiel"** / **"la pierre angulaire"** / **"le fil conducteur"** / **"l'épine dorsale"** / **"le socle"** / **"la clé de voûte"** — Why: AI scatters these as if every concept needs a heroic noun. Alternative: name the function ("X dépend de Y", "Y soutient X").
- **"le moteur"** (metaphorical) / **"le levier"** (calque of "leverage") — Same. Alternative: name what X actually does to Y.

#### Verbs and verbal phrases

- **"tirer parti de"** — Calque of "leverage". Alternative: "utiliser", "se servir de", "exploiter" (sparingly).
- **"mettre à profit"** — Same family. Alternative: "utiliser".
- **"exploiter pleinement"** — Tier-1 because of the adverb. Alternative: "utiliser".
- **"déployer"** (metaphorical: "déployer une stratégie") — Why: militaristic AI cliché. Alternative: "lancer" / "mettre en place".
- **"ériger"** / **"instaurer"** / **"consacrer"** — Why: AI uses these heavy verbs where "créer", "mettre en place", "dédier" would do. Alternative: the simple verbs.
- **"imprégner"** / **"irriguer"** / **"insuffler"** — Why: lyrical verbs that AI uses metaphorically. Alternative: name the concrete action.
- **"incarner"** — Why: AI's "embodies" reflex. Alternative: "représente", "est".
- **"cristalliser"** — Same. Alternative: "résume", "concentre".
- **"catalyser"** — Same. Alternative: "déclenche", "accélère".
- **"fédérer"** — Why: corporate AI cliché. Alternative: "rassembler", "réunir".
- **"transcender"** — Why: pompous. Alternative: "dépasser", "aller au-delà de".
- **"embrasser"** (metaphorical, e.g., "embrasser le changement") — Calque of "embrace". Alternative: "accepter", "adopter".

### Tier 2 — Medium signal (contextual)

Legitimate in domain (e.g., "optimiser" in an SRE post is fine). Flag when 3+ co-occur in 300 words.

#### Verbs

- **"naviguer dans"** (metaphorical) — Calque of "navigate". Alt: "s'y retrouver" / "gérer".
- **"explorer"** (metaphorical: "explorons ensemble") — Alt: "regarder", "examiner".
- **"découvrir"** (metaphorical) — Alt: "trouver", "lire", "lisez".
- **"dévoiler"** — Why: marketing reveal verb. Alt: "présenter", "montrer".
- **"révolutionner"** — Cf. tier-1 "révolutionnaire". Alt: "changer".
- **"transformer"** (overused, e.g., "transformer votre business") — Alt: "changer", "améliorer".
- **"optimiser"** / **"rationaliser"** / **"fluidifier"** — Domain-fine, but AI uses them as filler. Alt: name the concrete change.
- **"favoriser"** / **"encourager"** / **"stimuler"** — Hedge-y "helps to" verbs. Alt: "pousse à" / "facilite" / verb of the actual mechanism.
- **"valoriser"** — Alt: "mettre en avant", "rentabiliser".
- **"magnifier"** / **"sublimer"** — Marketing-poetic. Alt: "améliorer", "mettre en valeur".
- **"accompagner"** (overused in B2B copy) — Alt: "aider à" + verb, or just the verb.
- **"délivrer"** (in the sense of "to deliver a service / a feature") — Calque. Alt: "fournir", "livrer", "proposer".
- **"adresser"** (in the sense of "to address an issue") — Calque. Alt: "régler", "traiter", "s'occuper de".
- **"supporter"** (in the sense of "to support a feature") — Calque. Alt: "prendre en charge", "gérer".
- **"impacter"** — Alt: "affecter", "toucher", "modifier".
- **"initier"** (in the sense of "to initiate a project") — Calque. Alt: "lancer", "entreprendre", "démarrer".
- **"investiguer"** — Calque of "to investigate". Alt: "enquêter sur", "examiner".
- **"monitorer"** — Calque. Alt: "surveiller", "suivre".
- **"implémenter"** — Calque of "implement". Alt: "mettre en œuvre", "mettre en place", "coder".
- **"challenger"** (verb, calque of "to challenge") — Alt: "remettre en question", "contester".
- **"pivoter"** (figurative) — Alt: "changer de direction", "réorienter".

#### Adjectives of importance

- **"essentiel"** / **"fondamental"** / **"primordial"** / **"crucial"** / **"déterminant"** / **"décisif"** / **"capital"** — All inflators. AI sprays them. Alt: drop, or quantify.

#### Adjectives of intensity

- **"remarquable"** / **"exceptionnel"** / **"extraordinaire"** / **"spectaculaire"** / **"saisissant"** — AI's intensifier toolkit. Alt: name the specific quality.
- **"majestueux"** / **"somptueux"** / **"impressionnant"** — Tourism/wine-copy cliché. Alt: a concrete detail.
- **"raffinement"** / **"élégance"** / **"sophistication"** — Same family for product copy. Alt: name the design choice.

#### Abstract nouns

- **"harmonie"** / **"équilibre"** / **"symbiose"** / **"synergie"** — Buzzwords. Alt: name the relationship.
- **"écosystème"** (metaphorical, outside biology) — Calque of "ecosystem". Alt: "marché", "communauté", "réseau".
- **"univers"** (metaphorical, e.g., "l'univers du vin") — Alt: "le monde du vin", "la filière vin", or drop.
- **"monde de"** (metaphorical: "le monde du numérique") — Alt: "le secteur numérique", "la tech".

#### Vague abstractions

- **"expérience"** (vague usage: "une expérience unique") — Alt: name what the user actually does.
- **"immersion"** / **"voyage"** / **"parcours"** (metaphorical) — Tourism/UX cliché. Alt: name the steps.
- **"découverte"** / **"aventure"** / **"épopée"** — Same family. Alt: a fact.
- **"panorama"** / **"paysage"** / **"horizon"** — Meta-narrative scene-setters. Alt: enumerate.
- **"une multitude de"** — Alt: "beaucoup de", "plusieurs", a number.
- **"un large éventail de"** — Alt: a number, "plusieurs", "varié".
- **"offrir une expérience"** (anything) — Marketing tell. Alt: name what the user does.

#### Connectors (overuse)

- **"d'ailleurs"** / **"par ailleurs"** (as paragraph connectors) — Alt: drop, or restructure.
- **"en outre"** / **"de plus"** — Schoolbook. Alt: "et", "aussi", "plus".
- **"par conséquent"** / **"de ce fait"** / **"de sorte que"** — Heavy connectors. Alt: "donc", "alors", restructure.

### Tier 3 — Low signal (frequency-only)

Individually fine. Flag a paragraph if 5+ co-occur. Examples (non-exhaustive — the analyzer doesn't list these, the human reviewer does):

solution, approche, démarche, stratégie, enjeu, défi, opportunité, perspective, vision, ambition, performance, efficience, rentabilité, croissance, accompagnement, valeur ajoutée, plus-value, gain, bénéfice, atout, force, ressource, potentiel, dynamique, momentum, levier, axe, pilier, dimension, facette, aspect, élément, composante, brique, module, périmètre, posture, posture, écoute, agilité, résilience, excellence, expertise, savoir-faire, qualité, exigence, rigueur, méthodologie, processus, cadre, gouvernance, alignement, cohérence, transversalité, transparence, fluidité, simplicité, efficacité, robustesse, scalabilité, modularité, interopérabilité, durabilité, RSE, impact, traçabilité, monitoring, observabilité, automatisation, industrialisation, sécurisation, fiabilisation.

**Why these are low signal**: each appears naturally in honest French B2B prose. **Why they still matter**: a paragraph with 5+ of them is corporate AI Esperanto.

### Replacements (consolidated)

| Tell | Human alternative |
|---|---|
| en effet (connector) | en fait / d'ailleurs / Ø (often deletable) |
| il convient de noter | à noter / précisons / notons |
| il convient de souligner | drop and state the claim |
| force est de constater | on constate / il est clair que / manifestement |
| dans un monde où | aujourd'hui / depuis [date] / chez nous |
| à l'ère du numérique | aujourd'hui / depuis [date concrète] |
| plonger au cœur de | regarder / examiner / décortiquer |
| libérer le potentiel de | utiliser / exploiter (sparingly) |
| robuste (non-technique) | solide / fiable / qui tient la route |
| transformatif | important / décisif / qui change la donne |
| au cœur de | au centre de / au milieu de / dans |
| au sein de | dans / à l'intérieur de |
| incontournable | indispensable / essentiel (with restraint) |
| une multitude de | beaucoup de / plusieurs / des dizaines de (concrete) |
| un large éventail de | un (large) choix de / une dizaine de / Ø |
| naviguer dans (métaphorique) | s'y retrouver / s'orienter / gérer |
| en outre / de plus | et / aussi / plus |
| à l'instar de | comme / à la manière de |
| à la lumière de | à partir de / compte tenu de / vu |
| à l'aune de | par rapport à / à la mesure de |
| tirer parti de | utiliser / se servir de / exploiter (sparingly) |
| mettre à profit | utiliser |
| déployer (stratégie) | lancer / mettre en place |
| ériger / instaurer | créer / mettre en place |
| incarner | représente / est |
| catalyser | déclenche / accélère |
| fédérer | rassembler / réunir |
| transcender | dépasser / aller au-delà de |
| véritable (intensifier) | drop |
| phare (adjectif) | principal / le plus vendu |
| emblématique / iconique | drop or name what makes it notable |
| résolument / pleinement | drop |
| indéniablement / assurément | drop or "clairement" |
| délivrer (un service) | fournir / livrer / proposer |
| adresser (un problème) | régler / traiter / s'occuper de |
| supporter (une feature) | prendre en charge / gérer |
| impacter | affecter / toucher / modifier |
| initier (un projet) | lancer / entreprendre / démarrer |
| implémenter | mettre en œuvre / mettre en place / coder |
| pierre angulaire / clé de voûte / socle | name the function literally |
| écosystème (métaphorique) | marché / réseau / communauté |
| univers du X | secteur X / filière X / le X |
| à mille lieues de | très loin de / aux antipodes de |

---

## AI constructions (FR)

Patterns the analyzer matches via regex. Severity drives scoring.

### High severity

#### "Il ne s'agit pas seulement de X, il s'agit de Y"

Calque of "It's not just X, it's Y". Never use. Replace with a concrete claim.

- À éviter: "Il ne s'agit pas seulement d'un outil de pricing, il s'agit d'un atout stratégique."
- À préférer: "L'outil expose les marges par référence — les mêmes chiffres que regardent les acheteurs."

#### "Plongeons au cœur de" / "Explorons ensemble"

Never use as an introduction. State the subject directly.

- À éviter: "Plongeons au cœur du sujet du pricing dynamique."
- À préférer: "Le pricing dynamique — commençons par les seuils de marge."

#### "Dans un monde où..." / "À l'ère de l'IA..." / "À l'heure où..."

Never open with a temporal abstraction. Use a date, an event, or jump straight in.

- À éviter: "Dans un monde où la donnée est reine..."
- À préférer: "Depuis le RGPD, exporter sa base clients coûte plus cher."

#### "Imaginez un monde où..." / "Et si je vous disais que..."

Conference-bro openers. Banned.

- À éviter: "Imaginez un monde où vos clients paient avant d'acheter."
- À préférer: "Le prépaiement existe déjà — Wine.com le fait depuis 2003."

#### "Force est de constater"

Cf. suspect vocab. Pattern-matched separately because it acts as a topic-sentence opener.

- À éviter: "Force est de constater que les marges baissent."
- À préférer: "Les marges baissent. Quatre points en deux ans."

### Medium severity

#### "Que vous soyez X ou Y"

Avoid unless the branching is real. By default, pick one reader and write for them.

- Banni par défaut: "Que vous soyez startup ou grand groupe..."
- Acceptable si réel: "Que vous facturiez en EUR ou en USD, l'export reste identique."

#### "Accrochez-vous, car..." / "Voici pourquoi :" / "Voilà :"

AI signal-flares to the reader. Cut them; the sentence after is the actual content.

- À éviter: "Accrochez-vous, car les chiffres vont vous surprendre."
- À préférer: "Les chiffres : +47 % en 2025."

#### "Décortiquons cela." / "Voici ce qu'il en est :" / "Disons-le clairement :"

Same family — meta-sentences that perform thinking instead of doing it.

- À éviter: "Décortiquons cela ensemble."
- À préférer: skip to the decomposition.

#### "Pour faire court," / "Pour résumer," / "En somme,"

Closers that announce a summary. Either summarize, or don't — don't announce.

- À éviter: "Pour faire court, le pricing est cassé."
- À préférer: "Le pricing est cassé."

#### "Vous vous demandez peut-être..."

AI's "you might be wondering" reflex. Bad.

- À éviter: "Vous vous demandez peut-être pourquoi."
- À préférer: "Pourquoi ? Trois raisons."

#### "Le résultat ? X." / "L'enseignement ? X." / "Pourquoi cela importe ? Parce que..."

Question-then-answer pattern AI overuses. Native French does it occasionally; AI does it every paragraph. Cap at 1 per 800 words.

#### "Le constat est sans appel :"

AI's "the verdict is clear" reflex. Drop.

- À éviter: "Le constat est sans appel : il faut migrer."
- À préférer: "Il faut migrer. Voici pourquoi en trois lignes."

### Low severity

#### "Au final," / "À l'arrivée," / "Au bout du compte," / "Tout compte fait,"

Conclusion templates. **"Au final" is the strongest single-phrase FR tell of 2025-2026** — register-wrong (originally fight-sport slang now AI-overused). Cap all four at 0.

#### "Cela étant," / "Cela dit," / "Au demeurant,"

Pseudo-hedges. Each acceptable rarely; AI overuses. Cap at 1 per 800 words.

#### "Que les choses soient claires :" / "Disons les choses ainsi :"

Tone-resetter clichés. Drop.

### Hedging openers (drop entirely)

- "Il est important de noter que"
- "Il convient de souligner que"
- "Il faut garder à l'esprit que"
- "On notera que"
- "Mentionnons que"

If the qualifier matters, state it inline. Example: "Le pricing dépend du volume (important: hors taxes)."

---

## Em-dash and tiret cadratin discipline

**Ban the em-dash "—" (U+2014). Target 0; hard cap ≤ 1 per 1000 words.** In French it is an even louder AI signature than in English: native French prose almost never uses the wide em-dash outside dialogue, so a single "—" in an article reads as machine output on sight. Convert every one to a comma, colon, period, or parentheses. (En-dash "–" in ranges and the minus sign are fine; only the wide "—" is the tell.) When cleaning or writing FR, sweep for the "—" character explicitly and remove every occurrence.

French typography uses em-dashes far less natively than English. They belong to dialogue (tiret cadratin) and to a small set of structural roles. ChatGPT FR output sprays them everywhere, which is why the cap is stricter.

### Why FR is stricter than EN

- Native French prose prefers parentheses for parenthetical material, virgules for short asides, deux-points for setups, points for emphatic separations.
- The "incise" (X, conçu pour Y, tourne tous les jours) uses commas, not em-dashes, by default.
- The em-dash (— with non-breaking space, technically `—`) is a *typographic* mark, not a *rhetorical* one. AI conflates the two.
- "Tiret moyen" (en-dash, –) is even rarer in FR and almost always wrong outside ranges.
- Even reputable houses (Gallimard, Seuil) reserve "—" for dialogue tags ("— Bonjour, dit-il.") or for very strong incise.

### When em-dash IS appropriate in FR

1. **Dialogue.** "— J'arrive, dit-il." — opens a speaker line.
2. **Very strong incise** where commas would dilute or be ambiguous because the inserted clause already contains commas. Rare. One per 800 words at most.
3. **Bullet-style mid-sentence break** for typographic emphasis in a tight piece. Rare. The whole piece allows one or two.

### Replacement table

| AI overuse | Human FR |
|---|---|
| "Rapide — efficace — simple." | "Rapide, efficace, simple." or "Rapide. Efficace. Simple." |
| "L'outil — conçu pour les négociants — tourne chaque jour." | "L'outil, conçu pour les négociants, tourne chaque jour." |
| "Ça marche — la plupart du temps." | "Ça marche (la plupart du temps)." |
| "C'est simple — et ça marche." | "C'est simple. Et ça marche." |
| "Trois options — A, B et C — toutes valides." | "Trois options : A, B et C. Toutes valides." |
| "Le coût — non négligeable — reste compétitif." | "Le coût, non négligeable, reste compétitif." |
| "Pricing flexible — pay-per-event." | "Pricing flexible : pay-per-event." |

---

## Calques anglais à éviter (anglicismes IA)

These English-origin patterns leak into FR ChatGPT output. They're stronger tells in French than in English because they read as unnatural to a native ear.

### Lexical calques

- **"tirer parti de"** (leverage) → "utiliser", "se servir de", "exploiter"
- **"naviguer dans"** (navigate) → "s'y retrouver", "gérer"
- **"robuste"** (non-technical, robust) → "solide", "fiable"
- **"transformatif"** (transformative) → "déterminant", "décisif"
- **"délivrer"** (to deliver a service) → "fournir", "livrer", "proposer"
- **"adresser"** (to address an issue) → "régler", "traiter", "s'occuper de"
- **"supporter"** (to support a feature) → "prendre en charge", "gérer"
- **"challenger"** (to challenge) → "remettre en question", "contester"
- **"impacter"** (to impact) → "affecter", "toucher", "modifier"
- **"initier"** (to initiate) → "lancer", "entreprendre", "démarrer"
- **"investiguer"** (to investigate) → "enquêter sur", "examiner"
- **"monitorer"** (to monitor) → "surveiller", "suivre"
- **"implémenter"** (to implement) → "mettre en œuvre", "mettre en place"
- **"adresser X"** (address X, without preposition) → in FR you address X *to* someone; for "address an issue" use "régler"
- **"discuter X"** (discuss X, without preposition) → in FR you "discuss *de* X" (discuter d'un problème); AI drops the "de"
- **"focaliser X"** (focus X) → "se concentrer sur X"
- **"basé sur"** (based on, before main verb) → "fondé sur", "à partir de", "en fonction de"
- **"en train de + infinitif"** as default progressive → FR uses simple present
- **"finaliser"** (to finalize) → "terminer", "achever", "boucler"
- **"prioriser"** (to prioritize) — accepted now in FR but AI-overused → "donner la priorité à"
- **"juste"** as English "just" (jamais → "uniquement", "simplement")

### Calques de traduction métier (EN→FR)

When **translating** EN source into FR (not writing fresh), a second class of calque appears: domain terms rendered word-for-word into FR strings that either don't exist or mean something else. They pass every "fluency" check yet read as machine output to a native professional. Found in real audits of mr-bridge.com (2026-06):

| EN source | Calque (avoid) | Idiomatic FR | Note |
|---|---|---|---|
| open data | "données ouvertes" | **"open data"** / "données publiques" | the term French data circles actually use |
| routing (GPS / navigation) | "routage" | **"itinéraire" / "calcul d'itinéraire" / "itinéraires conseillés"** | "routage" = mail/packet routing in FR, never GPS |
| actionable | "actionnable" | **"exploitable" / "applicable"** | "actionnable" in FR = *justiciable* (legal); contresens |
| default (value) | "un défaut" | **"une valeur par défaut"** | "défaut" = flaw/defect; *default* = "valeur par défaut" |
| grower Champagne | "grower-Champagne" | **"champagne de vigneron"** / "récoltant-manipulant (RM)" | standard FR wine vocabulary |
| turnover (of businesses) | "turnover" | **"rotation" / "renouvellement"** | keep "turnover" only for accounting CA if truly meant |
| business register | "registres d'entreprises" | **"répertoire des entreprises"** (SIRENE) | the official French name |
| radar grid | "grille radar" | **"maille radar"** | |
| à la Ke / Ozer (author's method) | "à la Ke" | **"méthode Ke" / "selon Ke"** | and "(street scale)" → "(à l'échelle de la rue entière)", not "(échelle de la rue)" |
| world-class | "d'envergure mondiale" | **"de classe mondiale"** | "envergure" = scale/size, not quality |
| smart money / sweet spot | "smart money" / "sweet spot" | **"zone d'achat avisé" / "créneau optimal"** | franciser; don't leave the English in body copy |
| X correlates with Y | "X corrèle avec Y" | **"X est corrélé à Y"** | "corréler" is not intransitive in soigné FR |
| donut period / window | "période beignet" | name the real thing: **"on exclut une fenêtre temporelle autour de…"** | never transliterate an English jargon image |

**Doctrine.** These are *context-dependent* (a few, like "données ouvertes", are tolerable in official register), so they need a native judgment call, not a blind find-replace. But in translated marketing/editorial copy aimed at a French professional audience, prefer the idiomatic column. The tell is strongest when the calque is the **central concept** of the piece (e.g. "grower-Champagne" used 14× across one study).

**Whole-file accent stripping (hard check).** A distinct, severe failure mode: an entire translated file emitted with **no accents at all** ("donnees", "developpe", "systemes", "asymetrie de couts", and "deplorons" where "déployons" was meant). It reads as broken French on sight, yet is invisible to a fluency spot-check that never looks at the raw bytes. **Detection:** measure the ratio of accented characters to total letters; a real FR file sits around 0.12–0.17, a stripped file at ~0.00. Any FR file far below the corpus median is mangled — re-accentuate it fully before publishing. Run this on *every* translated file, not a sample:

```bash
for f in <fr-files>; do
  acc=$(grep -oP '[éèêëàâäîïôöùûüçÉÈÊËÀÂÎÏÔÖÙÛÜÇ]' "$f" | wc -l); w=$(wc -w <"$f")
  awk "BEGIN{printf \"%.3f  %s\n\", $acc/$w, \"$f\"}"
done | sort -n   # anything ≈0.000 is accent-stripped
```

### Syntactic calques

- **"the more X, the more Y"** → "plus X, plus Y" (legitimate FR — keep)
- **"X-friendly"** → "favorable à X", "adapté à X" (NEVER "X-friendly" as a hyphenated FR adjective)
- **"X-driven"** → "fondé sur X", "guidé par X"
- **"X-ready"** → "prêt pour X", "compatible X"
- **"as X as Y"** → "aussi X que Y" (legitimate) but AI overuses "tout aussi X que Y"
- **"in order to"** → "afin de" is fine, but AI uses it where "pour" would do
- **"such as X"** → "tel que X" (legitimate) but AI uses it where "comme X" would do
- **Comparatives with "than that of"** → AI writes "supérieur à celui de" reflexively when a simple "plus haut que" works

### Punctuation calques

- **Title case in FR titles** (capitalizing every word, e.g., "Comment Choisir Son Vin") — wrong in FR. FR title case capitalizes only the first word and proper nouns: "Comment choisir son vin".
- **Oxford comma** before "et" (e.g., "A, B, et C") — Anglo-Saxon. FR convention: "A, B et C".
- **Period inside closing quote** — English convention. FR puts the period *outside* (or inside only if the quoted material is a full sentence).
- **No space before `:` `;` `!` `?` `»`** — Anglo convention. FR uses a non-breaking space before each. AI often forgets.
- **Straight quotes `"X"`** instead of French guillemets `« X »` — typographic AI tell.

---

## Pedantic / scolaire turns

Schoolbook French. The model's training corpus is heavy with academic writing, so it defaults to phrases your *prof de français* would have written in red pen on your dissertation.

Banned by default:

- **"Avant tout, il convient de poser le décor"** — meta-textual scene-setting.
- **"Force est de constater"** — cf. supra.
- **"Il ne fait aucun doute"** / **"Nul ne saurait contester"** — appeal to phantom consensus.
- **"Comme chacun sait"** / **"Comme nul ne l'ignore"** — same.
- **"À ce stade de notre réflexion"** — fake academic transition.
- **"Au terme de cette analyse"** / **"À l'issue de cette réflexion"** — fake academic closer.
- **"De prime abord"** / **"Au premier abord"** — AI's "at first glance" reflex.
- **"En définitive,"** — heavy closer.
- **"Aux yeux de l'auteur"** — third-person self-reference. AI does this when asked to write a "neutral" piece.
- **"Le présent article"** / **"Le présent document"** — bureaucratic self-reference. Drop.
- **"Nous nous proposons de"** — academic intent statement. Drop.
- **"Il sera question de"** — same. Drop.

Rewrite by **stating** instead of **announcing**.

- À éviter: "À ce stade de notre réflexion, il convient d'examiner les marges."
- À préférer: "Maintenant, les marges."

---

## Conclusion templates (FR)

Never start a closing paragraph with any of:

- "En conclusion,"
- "Finalement,"
- "Pour conclure,"
- "Pour terminer,"
- "En définitive,"
- **"Au final,"** (the single strongest closing tell)
- "À l'arrivée,"
- "Au bout du compte,"
- "Tout compte fait,"
- "Tout bien considéré,"
- "À l'issue de cette réflexion,"
- "Pour clore ce propos,"
- "Comme nous avons pu le voir,"
- "Comme évoqué précédemment,"
- "Allons de l'avant,"
- "L'avenir s'annonce radieux,"
- "Ce n'est qu'un début."

End on a concrete action, a number, or a sharp opinion. Examples:

- "Le choix dépend du volume. Moins de 100 références: prenez A. Au-dessus: B."
- "Trois étapes — testez, mesurez, décidez. Le reste suit."
- "Pas convaincu ? Lancez un dry-run sur 100 lignes. Vous verrez."

---

## Voice and POV tells (FR)

### Absence de "je" sur 800+ mots

AI defaults to detached third-person or impersonal "on". A native author of an opinion piece **uses "je" at least once per 500 words**. Cleanup rule: insert one "je" sentence per 500 words to break the impersonal register.

- À éviter (entire piece): "On peut observer que les marges baissent. Il est probable que..."
- À préférer: "Je vois les marges baisser chez trois clients sur dix. Probablement..."

### Surutilisation de "nous" pédagogique

The "we" of a textbook ("nous allons voir que..."). AI defaults to this when asked to explain. Replace with "vous" (direct address) or "je + on" alternation.

- À éviter: "Nous allons voir comment migrer."
- À préférer: "Voici comment migrer." / "Vous migrez en trois étapes."

### "Vous" surutilisé comme adresse marketing

The other extreme. "Vous", repeated every sentence, becomes salesy.

- À éviter: "Vous gagnez du temps. Vous gagnez de l'argent. Vous gagnez en sérénité."
- À préférer: "Trois heures par jour économisées. 2 000 € par mois sauvés. Et le client appelle moins."

### Verbes au futur de prescription

"Vous découvrirez", "vous comprendrez", "vous serez en mesure de" — AI's prescriptive future. Replace with present or imperative.

- À éviter: "Vous découvrirez nos trois piliers."
- À préférer: "Trois piliers. On les regarde."

### Conditionnel de prudence à dose excessive

"Il pourrait être intéressant de", "il serait souhaitable que" — AI's politesse-conditional. Replace with direct present.

- À éviter: "Il pourrait être intéressant de tester."
- À préférer: "Testez."

---

## Typographic FR-specific tells

### Espaces insécables

French uses a non-breaking thin space (`U+202F` or `U+00A0`) before `:`, `;`, `!`, `?`, and inside guillemets `« X »`. AI output often omits these.

- AI output: "Trois options: A, B et C."
- Native FR: "Trois options : A, B et C." (note the space before `:`)

This is a *typographic* tell but it ladders into detection because human writers in pro CMS tools auto-insert it, AI in plain text doesn't.

**Cleanup rule.** When cleaning AI text for publication, run a global insert of non-breaking space before `:`, `;`, `!`, `?` (and inside guillemets). When writing fresh, type the space yourself.

### Guillemets

French uses `« »` with a non-breaking space inside. AI defaults to straight `"X"`.

- AI: `"un projet rentable"`
- Native: `« un projet rentable »`

### Majuscules accentuées

`À`, `É`, `È`, `Ç`, `Ê` at the start of words. AI often drops the accent on uppercase letters ("Etat" instead of "État", "A la croisée" instead of "À la croisée"). Native FR keeps them. This is the single fastest visual check for "did this come out of a French press CMS or a US-trained LLM".

### Tirets

Three lengths, three uses:

- **Trait d'union `-`** — composed words ("c'est-à-dire", "porte-monnaie").
- **Tiret moyen `–`** — number ranges ("pages 12–14"). Almost never elsewhere.
- **Tiret cadratin `—`** — dialogue and very strong incise. Capped at 2 per 1000 words.

AI conflates the three. Cleanup includes replacing inappropriate `—` with `,` or `(`.

### Apostrophes

French typography prefers the curly apostrophe `’` (U+2019) over the straight one `'` (U+0027). Most code-rendered text uses straight; most published FR text uses curly. For the analyzer: both are matched (regex normalization), but for *human writing*, use whichever your CMS expects and be consistent.

---

## Tricolon rationing (FR)

Same rule as EN: **cap at 1 tricolon per 200 words.** French already has rhetorical pull toward triadic structures ("liberté, égalité, fraternité") so a high count reads as borrowed-rhythm rather than authored prose.

Vary list sizes (2, 4, 5 items). Use asyndeton ("rapide, fiable, propre" without "et"). Don't close every list with ", et Z".

- À éviter: "L'outil est rapide, fiable, et précis. Il gère les bundles, variantes, et locales. Il tourne tous les jours, toutes les semaines, et à la demande."
- À préférer: "L'outil gère les bundles et les variantes sur 12 locales. Tournée quotidienne — ou à la demande pour un audit ponctuel."

### Sub-rule: tricolons in titles and bullets

AI title format: "Rapide, fiable, et performant". AI bullet last item: "et scalable". Both are tricolon tells.

- Title rewrite: "Rapide. Et fiable." / "Rapide et fiable" (deux items) / "Rapide" (un item).
- Bullet rewrite: drop the "et", or replace the last bullet with a different rhythm.

---

## Quick triage (for the human reviewer)

When auditing a 500-word FR piece, scan in this order:

1. Em-dashes — count them. If >1, replace.
2. Opening sentence — if it starts with a temporal abstraction or a meta-frame, rewrite.
3. Closing sentence — if it starts with any conclusion template (cf. supra), rewrite.
4. Tier-1 vocab — scan; cap at 1 per paragraph.
5. AI constructions — pattern-match by eye.
6. Tricolons — count; cap at 2 per piece.
7. POV — at least one "je" in the piece if it's opinion.
8. Calques — find and replace the lexical ones; for **translated** copy also scan the EN→FR translation-calque table (open data, routage, actionnable, grower-Champagne, défaut…).
9. Typography — non-breaking spaces, guillemets, accentuated capitals; on translated files, run the **accent-ratio check** (a file at ~0.000 is fully accent-stripped — re-accentuate before anything else).

A passing FR piece, by this skill's bar:

- 0–1 em-dash per 500 words.
- 0 tier-1 vocab items, ≤ 2 tier-2.
- 0 AI constructions.
- ≤ 1 tricolon per 200 words.
- At least one "je" if opinion.
- Non-breaking spaces in place.
- Title in sentence case.

That piece will score LOW_RISK (≤ 24) on the deterministic analyzer and survive Copyleaks / GPTZero at sub-25 % AI probability in most domains.

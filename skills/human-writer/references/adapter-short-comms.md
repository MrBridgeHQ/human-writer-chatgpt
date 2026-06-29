# Adapter: Short-Form Communications

> Doctrine for the `human-writer` skill, applied to short-form comms: emails, LinkedIn posts and DMs, Slack/Teams messages to clients, X/Twitter replies, GitHub issue comments, customer replies. Loaded in addition to language-specific stylistic tells (`tells-stylistic-en.md` / `tells-stylistic-fr.md`).

Short texts amplify density. A single em-dash in a 50-word email is louder than four em-dashes in a 1500-word blog post. The thresholds tighten accordingly, the surface area for "redemption" shrinks to nothing, and the reader is paying full attention. This is the hardest content-type in which to sound human, and the cheapest one for AI detectors to flag.

## 1. Scope: what counts as `short-comms`

| Channel | Typical length | Notes |
|---|---|---|
| Business email (Brevo, IMAP, Gmail) | 40-300 words | Both cold and warm |
| LinkedIn post | 80-300 words | Hook in line 1 (preview) |
| LinkedIn DM | 30-120 words | Often the cold ask |
| Slack/Teams to client | 20-200 words | Tone informal, content business |
| X/Twitter reply | < 280 chars | Tiny surface, one tell kills it |
| GitHub issue comment | 50-300 words | Technical, may include code |
| Internal update / status | 100-300 words | Some structure tolerated |
| Newsletter intro | 100-300 words | Body switches to `marketing` |

Distinct from:
- `marketing`: no persuasion structure, no funnel, no hero claim
- `technical`: less precision focus, more relational/conversational tone
- `editorial-seo`: no SEO intent, no keyword targeting

Word count typically 30-500 words. Below 30 words, this adapter still applies but most checks become moot (the only thing left is "does the signoff smell of AI").

## 2. Why short-comms is the trickiest content-type for AI detection

Five reasons the bar is higher here than anywhere else:

1. **Density amplification.** One em-dash in a 100-word email is 10/1000 words, already 2.5× the EN threshold and 5× the FR threshold from `rules.yaml`. One AI-flavored idiom in 80 words is one in eighty. There's nowhere to hide.
2. **Signoffs are templates.** AI email tooling has trained millions of readers to spot "I look forward to hearing from you" at a glance. The closing 8-12 words of an email carry disproportionate weight in the reader's "is this a person?" judgment.
3. **No surface to redeem.** A 1500-word blog post can afford one weak section if the rest is strong. A 60-word reply cannot.
4. **Detector attention.** Copyleaks, GPTZero, Originality, and outreach-platform-side detectors are increasingly tuned for sales/cold-email formats. The training set is dense.
5. **Reader attention.** Recipients of a personal email or DM read every word. A blog post reader skims. Tells stand out more under close reading.

## 3. Priority ranking: which tells matter MOST here

Different from long-form. Order matters.

1. **Em-dash discipline (TIGHTER cap).** Hard cap: 1-2 em-dashes max in the whole message, regardless of length. Effective rates: EN ≤ 2/1000 words, FR ≤ 1/1000 words. For a 100-word email, that means: prefer zero, accept one, never two.
2. **Idiosyncrasy (HIGHEST POSITIVE SIGNAL).** One unusual word, fragment, or structure puts the reader firmly in "this is a person" territory. See section 6.
3. **AI-flavored signoffs (HIGH).** Section 4 below: zero tolerance for the listed phrases.
4. **AI-flavored openers (HIGH).** Section 5: same logic, mirror image at the top.
<!-- human-writer:ignore-start (these two items quote forbidden vocab and constructions as anti-patterns) -->
5. **Tier-1 vocabulary (HIGH).** 1 tier-1 word in 200 words is a tell. Still zero `delve`, `leverage`, `transformative`, `seamless`, `robuste`, `transformatif`.
6. **Conclusion templates (HIGH).** "In conclusion,", "Ultimately,", "En conclusion,": never in a short message.
<!-- human-writer:ignore-end -->
7. **Sentence variance (LOWER).** Short messages naturally have low variance (few sentences total). Relax the `burstiness_min` / `sentence_stdev_min` checks.
8. **Structural tells (LOWER).** Short messages rarely have headers or bullet lists. The `structural: 0.5` weight reflects this.

## 4. AI-flavored signoffs: zero tolerance

The single most expensive 8 words in any email. Detectors and readers both lock onto these.

<!-- human-writer:ignore-start (forbidden signoff phrases, quoted as anti-patterns not used as prose) -->
### EN — never use

- "I look forward to hearing from you."
- "Looking forward to your response."
- "I would love to hear your thoughts."
- "Please don't hesitate to reach out."
- "Feel free to reach out with any questions."
- "If you have any questions, feel free to ask."
- "Thank you for your understanding."
- "Thank you for your time and consideration."
- "Best regards," (overused — fine 1 email in 5, never every email)
- "Warm regards,"
- "Kind regards,"
- "Sincerely yours,"

### FR — never use

- "Au plaisir de vous lire,"
- "Dans l'attente de votre retour,"
- "Restant à votre disposition,"
- "N'hésitez pas à me solliciter pour toute question."
- "Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées." (formal — OK in legal/administrative contexts, but AI defaults to it always)
- "Bien cordialement," (overused, same logic as "Best regards,")
- "Cordialement," (acceptable 1 in 5, never every email)
- "Au plaisir,"
<!-- human-writer:ignore-end -->

## 5. AI-flavored openers: zero tolerance

The first 10-15 words set the read. Same logic, opposite end.

<!-- human-writer:ignore-start (forbidden opener phrases, quoted as anti-patterns not used as prose) -->
### EN — never use

- "I hope this email finds you well,"
- "I hope this message finds you well,"
- "I trust this email finds you well,"
- "I hope you're doing well,"
- "I trust you're well,"
- "I wanted to reach out to..."
- "I'm reaching out because..."
- "I am writing to inquire about..."
- "I would like to take this opportunity to..."
- "Just wanted to follow up on..."
- "Per our last conversation,"
- "Following up on my previous email,"
- "As discussed,"

### FR — never use

- "J'espère que ce message vous trouve en bonne santé," (full calque, ouch)
- "J'espère que vous allez bien,"
- "Comme convenu," (when stale)
- "Pour faire suite à mon précédent email,"
- "Je me permets de revenir vers vous au sujet de..."
- "Je vous écris afin de..."
- "Suite à notre échange,"
<!-- human-writer:ignore-end -->

## 6. Human-sounding alternatives

<!-- human-writer:ignore-start (quoted signoff/opener literals, cited as examples not used as prose) -->
### EN — signoffs that pass

- Just a first name on its own line
- "Talk soon,"
- "Cheers,"
- "Thanks,"
- "Best," (yes — better than "Best regards,")
- "—Léa"
- Nothing at all (a 2-sentence reply doesn't need a signoff; the email client signature handles attribution)

### FR — signoffs that pass

- Just a first name
- "À bientôt,"
- "Merci,"
- "Bonne journée,"
- "Bonne soirée,"
- "À+,"
- Nothing at all

### EN — openers that pass

- Open with the actual point: "Quick question about the Q3 pricing."
- Open with a fact: "Saw your post on the Apify PPE change. One thing surprised me:"
- Open with a question: "How's the rollout going?"
- Skip the opener entirely: drop straight into the content. "The contract version you sent has an issue on clause 4.2..."

### FR — openers that pass

- Sur le sujet : "Question rapide sur le tarif Q3."
- Sur un fait : "Vu votre post sur le PPE Apify. Un point m'a marqué :"
- Sur une question : "Le déploiement avance comment ?"
- Pas d'ouverture : entrer directement. "La version du contrat que tu m'as envoyée a un souci sur l'article 4.2..."
<!-- human-writer:ignore-end -->

## 7. Idiosyncrasy: the #1 humanization technique here

In long-form, you can vary rhythm and use specific data. In short-form, your single best tool is **one** idiosyncratic phrase or structure that no AI template would generate. One is enough. Two starts to look like you're trying.

Concrete moves:

<!-- human-writer:ignore-start (quoted sample phrases demonstrating the moves, cited not used as prose) -->
- Open with a specific observation only you would make ("Your Friday post on Postgres connection pooling — that footnote about PgBouncer in transaction mode was exactly what I'm hitting.")
- Use a sentence fragment for emphasis ("Worth it.")
- Drop a side joke (one line, never two)
- Mention a specific shared context: a person, a date, a previous conversation, a place
- Use casual contractions ("won't", "we're", "it's") — AI defaults to expanded forms in business email
- End mid-thought, with no closing summary
- Reference a number that's clearly from your own measurement, not a benchmark ("4.2 ms p50 with the cache warm, vs 0.8 s cold")
- Drop one word of slang, jargon, or in-group vocabulary
- Use one French/English borrowing if you naturally code-switch (if you do)
<!-- human-writer:ignore-end -->

See also `humanization-techniques.md`, technique #6 (idiosyncratic markers).

## 8. Length calibration by use case

| Use case | Word count | Notes |
|---|---|---|
| Cold intro email | 80-150 words | One specific opener, one clear ask |
| Warm follow-up | 60-120 words | Reference the previous, ask one thing |
| Internal status update | 100-300 words | Light structure OK, no headers |
| Reply to client | 40-150 words | Direct, no preamble, no signoff filler |
| Newsletter intro | 100-200 words | Body switches to `marketing` adapter |
| LinkedIn post | 80-300 words | Section 9 |
| LinkedIn DM (cold) | 30-80 words | Section 9 |
| X/Twitter reply | < 280 chars | One thought, no emoji |
| Slack message to client | 20-150 words | Most informal; contractions everywhere |

Below 30 words, only the signoff/opener checks apply.

## 9. LinkedIn post specifics

- **First line is the hook.** Under 100 characters so it fits in the feed preview before the "...see more" cut.
- **No emoji in the first line.** Heavy AI tell: AI templating defaults to opener emojis.
- **Max 5 emojis total** across the whole post. Zero is fine. Six is a tell.
- **No bullet lists for content.** LinkedIn algorithm doesn't favor them, and they look templated. If you need parallel items, write them as short standalone lines separated by blank lines.
- **No "Agree? Disagree? Comment below" CTA.** Heaviest AI tell on the platform. Same for "What do you think?" closers and "Drop a 🔥 if you agree."
- **No "Thoughts?" closer.** Also templated.
- **Hashtags max 3, at the very bottom.** Avoid #innovation #leadership #ai stacks.

LinkedIn DMs follow the cold-email rules. Skip the "Hope you're well" entirely.

## 10. Tells that are tolerated more here

### Tier-1 vocabulary (slightly relaxed in narrow technical context)

<!-- human-writer:ignore-start (calibration paragraph quotes the suspect word `robust` as its worked example) -->
In a 50-word Slack message to a developer ("the deploy is robust enough for smoke tests"), `robust` reads as a technical adjective, not AI gloss. The analyzer's `stylistic: 1.2` weight still flags it, but a single instance in a strictly technical context is defensible.
<!-- human-writer:ignore-end -->

<!-- human-writer:ignore-start (forbidden tier-1 vocab list, quoted as anti-patterns not used as prose) -->
Still zero: `delve`, `leverage`, `transformative`, `seamless`, `unlock`, `harness`, `unleash`, `tapestry`, `realm`, `synergy`, `paradigm`. These never pass regardless of context.
<!-- human-writer:ignore-end -->

### Headers (irrelevant)

Short comms rarely have headers. Skip structural checks. If a message has H2s, it's not short-comms: switch adapter.

### Tricolons (relaxed if asyndeton)

"Fast, cheap, done." in a Slack message reads as human punch. "Fast, cheap, and done." in the same message reads as AI. Same content, different punctuation. The "and" is the tell. Asyndetic tricolons (no "and") pass; syndetic tricolons trip.

### Sentence variance (relaxed)

A 5-sentence email naturally has low burstiness; there's no statistical room to vary. The `statistical: 0.6` weight reflects this. Don't force long-short alternation in a 50-word reply.

## 11. Calibration with `analyze.py`

Short-comms weights from `scripts/rules.yaml`:

```yaml
short-comms:   {statistical: 0.6, stylistic: 1.2, structural: 0.5}
```

Stylistic enforced HIGHER (1.2×: most important axis here). Statistical and structural relaxed (0.6× and 0.5×). Run:

```bash
python3 scripts/analyze.py --type short-comms --lang en draft.txt
python3 scripts/analyze.py --type short-comms --lang fr brouillon.txt
```

Target: score ≤ 25 (LOW_RISK band from `rules.yaml verdict_bands`). For very short messages (< 80 words), interpret the score loosely; a single em-dash can spike density above the threshold without the message actually reading as AI. Cross-check with the checklist in section 12.

## 12. Pre-publish checklist: short-comms

```markdown
- [ ] Ran `analyze.py --type short-comms` — score ≤ 25
- [ ] No "I hope this finds you well" / "J'espère que vous allez bien"
- [ ] No "Looking forward to hearing from you" / "Au plaisir de vous lire"
- [ ] No "Best regards," / "Bien cordialement," (unless rotated, not every email)
- [ ] Em-dashes: ≤ 1 in the whole message (zero preferred)
- [ ] At least one idiosyncratic phrase, fragment, contraction, or specific reference
- [ ] No tier-1 AI vocab (see `tells-stylistic-en.md` / `tells-stylistic-fr.md`)
- [ ] No "In conclusion," / "Ultimately," / "En conclusion," / "Finalement,"
- [ ] Signoff is a first name or short phrase, not corporate boilerplate
- [ ] For LinkedIn posts: first line < 100 chars, no opener emoji, no "Thoughts?" closer
```

If any item fails, fix before sending. The bar for "sounds human" is higher here than in any other content type.

## 13. Worked examples

### Example 1: EN cold follow-up email (~120 words)

<!-- human-writer:ignore-start (deliberately AI-flavored sample + tells citation; must not self-flag) -->
**AI-flavored draft (analyzer score: 58/100, HIGH_RISK)**

> Subject: Following up on our previous conversation
>
> Hi Sarah,
>
> I hope this email finds you well. I wanted to reach out to follow up on our previous conversation regarding the Apify integration. I trust you've had a chance to review the proposal I sent over last week.
>
> I believe our solution would be a transformative addition to your workflow, enabling you to seamlessly leverage scraping capabilities at scale. I'd love to hear your thoughts and would be happy to schedule a call to delve deeper into the specifics.
>
> Please don't hesitate to reach out if you have any questions.
>
> Looking forward to hearing from you.
>
> Best regards,
> Léa

Tells: opener cliché, "transformative", "seamlessly leverage", "delve deeper", "Please don't hesitate", "Looking forward to hearing from you", "Best regards," — every closing template box checked.
<!-- human-writer:ignore-end -->

**Humanized version (analyzer score: 12/100, LOW_RISK)**

<!-- human-writer:ignore-start (quoted clean-example email body; cited as a sample not used as prose) -->
> Subject: Apify integration — still on?
>
> Hi Sarah,
>
> Quick check — did the proposal land OK? No rush, just don't want it to drift if there's a question I can answer.
>
> The piece I'd most like your read on is the PPE pricing in §3. We've had two clients push back on the per-event rate; I have a fallback if it's a blocker.
>
> Happy to jump on a call this week or next.
>
> Léa
<!-- human-writer:ignore-end -->

Changes: subject line is concrete and direct. No "hope this finds you well." Specific reference (§3, "two clients push back"). One sentence fragment ("No rush, just..."). Contraction ("don't"). Signoff is just the name. Em-dashes: 2 in 70 words, at the cap, but one is in the subject (not body) and the body has only one. Acceptable.

### Example 2: FR client reply (~80 words)

<!-- human-writer:ignore-start (deliberately AI-flavored FR sample + tells citation; must not self-flag) -->
**AI-flavored draft (analyzer score: 51/100, HIGH_RISK)**

> Bonjour Marc,
>
> J'espère que ce message vous trouve en bonne santé. Je vous remercie pour votre retour concernant l'intégration API. Il convient de noter que notre solution offre une approche robuste et transformative qui permettra de tirer parti de l'ensemble des données disponibles.
>
> N'hésitez pas à me solliciter pour toute question complémentaire.
>
> Bien cordialement,
> Léa

Tells: calque opener "J'espère que ce message vous trouve en bonne santé", "Il convient de noter", "robuste", "transformative", "tirer parti", "N'hésitez pas à me solliciter", "Bien cordialement". Six high-severity tells in 60 words of body.
<!-- human-writer:ignore-end -->

**Humanized version (analyzer score: 14/100, LOW_RISK)**

<!-- human-writer:ignore-start (quoted clean-example FR email body; cited as a sample not used as prose) -->
> Bonjour Marc,
>
> Merci pour le retour sur l'intégration. Sur les 47 références que vous m'avez listées, 43 passent ; les 4 qui plantent ont tous le même symptôme (timeout sur le endpoint détails). Je regarde ça demain matin et je vous renvoie un patch dans la journée.
>
> À bientôt,
> Léa
<!-- human-writer:ignore-end -->

Changes: no opener cliché, straight into thanks + content. Specific numbers (47, 43, 4). Technical detail (timeout, details endpoint). Concrete commitment with a time ("demain matin", "dans la journée"). Signoff is "À bientôt," warm but not templated. Zero em-dashes. Zero tier-1 vocab.

### Example 3: LinkedIn DM ask (~50 words)

<!-- human-writer:ignore-start (deliberately AI-flavored sample + tells citation; must not self-flag) -->
**AI-flavored draft (analyzer score: 47/100, MEDIUM_RISK)**

> Hi Alex,
>
> I hope you're doing well. I wanted to reach out because I noticed your impressive work in the scraping space. I would love to connect and explore potential synergies between our innovative solutions.
>
> Looking forward to your response.
>
> Best,
> Léa

Tells: "I hope you're doing well", "I wanted to reach out", "impressive work", "synergies", "innovative solutions", "Looking forward to your response". Generic and templated end to end.
<!-- human-writer:ignore-end -->

**Humanized version (analyzer score: 8/100, LOW_RISK)**

<!-- human-writer:ignore-start (quoted clean-example DM body; cited as a sample not used as prose) -->
> Hi Alex,
>
> Your write-up on the connection-pool exhaustion issue last week — that's the exact failure mode I hit in March on a high-throughput API client. Did you ever figure out whether it was the TLS handshake cost or the session pool churn?
>
> No agenda, just curious.
>
> Léa
<!-- human-writer:ignore-end -->

Changes: opens on specific shared context (the write-up, a date). Specific technical question (TLS vs session churn). Explicit "no agenda" disarms the cold-DM frame. Fragment ("No agenda, just curious."). No signoff filler. One em-dash, justified by the parenthetical break. The "ask" is implicit, a real question, not a templated meeting request.

## See also

- `tells-stylistic-en.md` / `tells-stylistic-fr.md`: full vocabulary and construction lists to avoid
- `humanization-techniques.md`: technique #6 (idiosyncratic markers) is the critical one here
- `checklists.md`: master checklist; section 12 above is the short-comms specialization
- `adapter-marketing.md`: for newsletter bodies and persuasion-structured content
- `adapter-technical.md`: when the message is a GitHub comment with heavy code/diagnostics

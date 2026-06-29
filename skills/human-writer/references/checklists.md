# Pre-Publish Checklists (human-writer)

> Ready-to-paste self-review checklists, one per content-type. Run `analyze.py` first, then walk through the relevant checklist before delivery. Each checklist is short, actionable, and covers the tells most likely to trigger AI detectors for that specific format.

---

## Marketing Long-Form

Before publishing blogs, READMEs, landing pages, or long-form newsletters, confirm:

- [ ] Analyzer score ≤ 25 with `--type marketing`
- [ ] First 100 words contain zero Tier-1 suspect vocabulary
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] First paragraph does not open with "In today's", "In an era", "In the realm of", or "Whether you're"
- [ ] Closing paragraph does not start with "In conclusion", "Ultimately", "All in all", or "To sum up"
<!-- human-writer:ignore-end -->
- [ ] Em-dash count ≤ 4 per 1000 words (run `analyze.py` to check)
- [ ] At least one specific number, named entity, or first-person opinion per ~300 words
- [ ] Bulleted lists vary opening verbs (≤ 50% share the same first word)
- [ ] No H2 has exactly 3 H3 children (if 2+ H2s exist, vary H3 counts)
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] No "Key takeaways" / "What you'll learn" / "Top X things" standalone block
<!-- human-writer:ignore-end -->
- [ ] No emoji as section header

If any item fails: fix before delivery. If analyzer score is 26–49 after fixes, apply the top 3 recommendations and re-score. If 50+, reconsider your angle.

---

## Short-Form Communications

Before sending emails, LinkedIn posts, Slack messages, or customer replies, confirm:

- [ ] Analyzer score ≤ 25 with `--type short-comms`
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] No "I hope this finds you well" / "J'espère que ce message vous trouve en bonne santé" opening
- [ ] No "Looking forward to hearing from you" / "Au plaisir de vous lire" closing
- [ ] No "I look forward to", "Feel free to reach out", "Don't hesitate to", "If you have any questions"
<!-- human-writer:ignore-end -->
- [ ] Em-dashes: 0 preferred, 1 acceptable, never 2+ in messages under 200 words
- [ ] At least one contraction, sentence fragment, or first-person verb in replies over 30 words
- [ ] Signoff is first name, short phrase, or nothing, not corporate boilerplate
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] First line is not "I wanted to reach out" / "I'm reaching out" / "I wanted to follow up"
<!-- human-writer:ignore-end -->

If any item fails: revise before sending. Short comms are where human voice shows up clearest; a single misstep reads louder than in longer formats.

---

## Technical Documentation

Before publishing internal READMEs, RFCs, architecture docs, or technical journals, confirm:

- [ ] Analyzer score ≤ 25 with `--type technical`
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] First sentence states the WHY (problem this doc solves), not "In this document, we will..."
- [ ] No "Let's dive in!" / "Let's get started!" / "Here we go!" filler
- [ ] No "Conclusion" section (unless >500 words and earns a summary)
- [ ] Every instance of "robust", "scalable", "leverage", "elegant", "powerful" passes the "replace with 'good'" test
<!-- human-writer:ignore-end -->
- [ ] Code blocks are not surrounded by paragraphs that re-explain them line-by-line
- [ ] One sentence per concept: no restating or hedging the same idea twice
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] Zero hedging openers ("It's worth noting", "Keep in mind", "Please be aware", "Important:", "Note that")
<!-- human-writer:ignore-end -->

If any item fails: revise. Technical docs should be direct and economical; every sentence must earn its space.

---

## Editorial-SEO Articles

Before publishing ranking-optimized articles, blog posts, or news pieces, confirm:

- [ ] Analyzer score ≤ 25 with `--type editorial-seo`
- [ ] Target keyword appears in: title, first 100 words, and ≥1 H2
- [ ] First 100 words contain a specific data point or opinion (not just the keyword)
- [ ] H2 hierarchy is varied, not pyramid (not 3 H3s per H2 uniformly)
- [ ] At least 1 internal link with natural anchor text (not "click here")
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] No "In today's fast-paced X world," / "As the world becomes increasingly digital," opener
- [ ] No "Conclusion" that just restates the intro / tl;dr
<!-- human-writer:ignore-end -->
- [ ] At least one opinion that someone could reasonably disagree with
<!-- human-writer:ignore-start (checklist quotes the tells to look for) -->
- [ ] No "Ultimate guide", "Everything you need to know", "Complete walkthrough" UNLESS your keyword data demands it
<!-- human-writer:ignore-end -->
- [ ] Sentence-length standard deviation ≥ 8 (mix short and long)

If any item fails: fix before publishing. SEO articles work best when they have a clear stake and a mixed voice, not a survey-tone.

---

## Universal Baseline

Apply to **all** content types before delivery:

- [ ] Final `analyze.py` run; score ≤ 25
- [ ] No Tier-1 suspect vocabulary in the first 100 words (check `rules.yaml` for the list)
- [ ] At least one specific element: number, name, date, fact, quote, not generic claims
- [ ] At least one stylistic asymmetry: e.g. a short sentence after long ones, a varied list length, unexpected punctuation or structure
- [ ] Doesn't end with a summary or call-to-action that merely restates the opening

---

## How to Use These Checklists

1. Write or clean your draft.
2. Run `python3 scripts/analyze.py --input <draft> --lang <lang> --type <type> --format human` from the skill root.
3. If score > 25, apply the analyzer's top recommendations until ≤ 25.
4. Walk through the relevant checklist above (marketing, short-form, technical, or editorial-SEO).
5. Check off each item; revise any failures.
6. Re-run the analyzer if you made major changes.
7. Deliver only when both gates pass (analyzer ≤ 25 AND checklist complete).

---

## See Also

- `tells-stylistic-en.md` / `tells-stylistic-fr.md`: vocabulary, constructions, punctuation tells
- `adapter-marketing.md`: doctrine specific to long-form marketing
- `adapter-short-comms.md`: doctrine specific to short communications
- `humanization-techniques.md`: positive techniques for adding human voice
- `scripts/analyze.py`: deterministic analyzer (run before checklist)
- `external-detectors.md`: optional integration with Copyleaks, GPTZero, etc.

# Daily News Card Summary Prompt

Use this prompt after the day's news cards have been created in the vault.

```text
Process the news cards created today in this Obsidian vault.

1. Identify cards with `type: news-card` and included in [Today](app://obsidian.md/Today). Search only the vault's `Cards` folders. 
2. Determine whether each card already has a dateline summary. A citation line beginning `(U)` is not a summary; it contains an accessed date and source URL. Do not duplicate or rewrite a valid existing summary.
3. For each card that lacks a summary, read the card and its source URL. Fetch the source; if direct access fails, search the headline and outlet on the web. Do not invent details. If a source remains inaccessible, summarize only what can be verified from reliable search excerpts and state the limitation.
4. Add a concise, objective, past-tense summary of 2–4 sentences in this form:

   `(U) <CITY, REGION, or COUNTRY> — <summary>`

   Use the real em dash (—). Insert the paragraph immediately after `[Source](URL)` and before `**Query:**`.
5. Attribute claims to their source, especially allegations, official statements, state media, partisan or opinion pieces, aggregators, vendor research, and press releases. Keep reported claims distinct from independently established facts.
6. If a card has a clearly broken/bare-domain headline, junk outlet suffix, or URL used as its outlet, clean the `title:` property, `# Heading`, citation title, or outlet consistently. Do not change card IDs or filenames.
7. Normalize a missing `[Source]` line or misplaced summary only as needed to restore the required order. Leave unrelated body text untouched.
8. Verify every card processed today: each must have exactly one non-citation `(U) ... — ...` summary after `[Source]` and before `**Query:**`; check that the separator is an actual em dash. Report the count completed and any unresolved cards.
```

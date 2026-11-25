---
epoch: 1795098984136
mode: agent
backendId: opencode
sessionId: "ses_e0bca4735ffeCwik0lm0Chendc"
tags:
  - copilot-conversation
---

**user**: Task
Write today’s Priority Headlines brief from the article cards in the note [[Today]]  and including the information from [[All Hazards Brief 2026-11-19]], [[CI Sector Brief 2026-11-19]], and [[USBR Brief 2026-11-19]]   .
Title it exactly: Priority Headlines for DDMMMYYYY
(Use the briefing date, e.g. Priority Headlines for 18NON2026. Write the finished brief into [[Summary for 19NOV2026]].)

Source of truth
- Use only article cards in [[Today]] whose created/imported timestamp is on or after the cutoff (default: three calendar days before the briefing date at 08:00 local, or the cutoff given in the request).
- State the card count in the scope line. If the count is materially different from what the user expected, say so at the top and continue with what is present. A 2–3 card delta is not material.
- Do not invent outlets, titles, facts, or incidents. If a card is thin, summarize only what is on the card.
- Match the structure, heading style, bullet style, and density of the previous brief [[Summary for 19NOV2026]]   (or the most recent Priority Headlines note if that filename differs). Copy the format; do not copy that brief’s content.

What “tactical” means here
Lead with operational, place-and-time, asset-specific items. Prefer:
- Named facilities, utilities, plants, substations, ports, airports, rail, pipelines, water systems, telecom/data centers, emergency services
- Attacks, intrusions, disruptions, arrests, devices, drones/UAS, vandalism, sabotage, cyber incidents with a concrete target
- Sector, location, actor, or TTPs if the card has them
 - Organize First alert incidents by state and avoid a mass paragraph with all incidents jumbled together. Please bulletize the Energy/Electric section and organize by country and state.
For the Strategic Section focus on:
- High-level geopolitics, market commentary, and “what it means for the world” unless they name a CI asset or an imminent operational effect
- Diplomacy, pacts, travel, legislation, and opinion essays with no incident                                               
Demote or omit:
- False positives (movies, gadgets, exam leaks, academic SVR/forecast papers, CI/CD marketing)
- Repeat analysis already briefed in an earlier batch unless there is a new operational fact
- Duplicate coverage of the same incident: keep one bullet; name the strongest outlet and, if useful, the other outlets in the same bullet

Consolidation
- One incident = one bullet even if 3–6 cards cover it (e.g. Houthi strike on Riyadh; mass drone attack on Moscow; synagogue arson sequence).

Output format
1. One-line scope: date range, card count used, and (if needed) a short note that the count differs slightly from expected.
2. Same section headings as the previous brief if they still fit. If they do not, use:
   - Energy / Electric
   - Water / Wastewater
   - Transportation
   - Communications / Cyber
   - Government / Emergency Services
   - Other CI / Soft targets
   Omit empty headings. Do not invent a heading to save a weak card.
3. Under each heading, bullets only. Each bullet:
   - Article title as it appears on the card (or a tight factual rewrite if the title is clickbait)
   - Outlet in parentheses; if several cards are the same story, one title plus outlets
   - Optional: one short clause with location + CI relevance if that is not already in the title
4. After the section bullets, “Tactical takeaways”: 3–6 bullets of patterns visible in this batch only (who/what/where repeating). No strategy essays.
5. Do not add recommendations, policy advice, or a narrative intro beyond the one-line scope.
6.  Organize First alert incidents by state and avoid a mass paragraph with all incidents jumbled together.
Constraints
- English, tight, no filler.
- No article that is only strategic “big picture.”
- If you are unsure an item is CI-relevant, put it under Other CI / Soft targets rather than stretching a sector heading.
- When finished, leave the brief in [[Summary for 19NOV2026]]    and give a short process note: cards in / cards omitted (categories only, not a second brief) / headings used / takeaway count.

Then include a strategic level summary like that seen in notes Summary for 11SEP2026-Summary for 18NOV2026 for the notes set specified above. See the combined [[Summary for 18NOV2026]]  .
[Timestamp: 2026/11/19 07:36:24]

**ai**: **Error:** Internal error: UNKNOWN_CERTIFICATE_VERIFICATION_ERROR: unknown certificate verification error
[Timestamp: 2026/11/19 07:36:24]

**user**: Task
Write today’s Priority Headlines brief from the article cards in the note [[Today]]  and including the information from [[All Hazards Brief 2026-11-19]], [[CI Sector Brief 2026-11-19]], and [[USBR Brief 2026-11-19]]   .
Title it exactly: Priority Headlines for DDMMMYYYY
(Use the briefing date, e.g. Priority Headlines for 18NON2026. Write the finished brief into [[Summary for 19NOV2026]].)

Source of truth
- Use only article cards in [[Today]] whose created/imported timestamp is on or after the cutoff (default: three calendar days before the briefing date at 08:00 local, or the cutoff given in the request).
- State the card count in the scope line. If the count is materially different from what the user expected, say so at the top and continue with what is present. A 2–3 card delta is not material.
- Do not invent outlets, titles, facts, or incidents. If a card is thin, summarize only what is on the card.
- Match the structure, heading style, bullet style, and density of the previous brief [[Summary for 19NOV2026]]   (or the most recent Priority Headlines note if that filename differs). Copy the format; do not copy that brief’s content.

What “tactical” means here
Lead with operational, place-and-time, asset-specific items. Prefer:
- Named facilities, utilities, plants, substations, ports, airports, rail, pipelines, water systems, telecom/data centers, emergency services
- Attacks, intrusions, disruptions, arrests, devices, drones/UAS, vandalism, sabotage, cyber incidents with a concrete target
- Sector, location, actor, or TTPs if the card has them
 - Organize First alert incidents by state and avoid a mass paragraph with all incidents jumbled together. Please bulletize the Energy/Electric section and organize by country and state.
For the Strategic Section focus on:
- High-level geopolitics, market commentary, and “what it means for the world” unless they name a CI asset or an imminent operational effect
- Diplomacy, pacts, travel, legislation, and opinion essays with no incident                                               
Demote or omit:
- False positives (movies, gadgets, exam leaks, academic SVR/forecast papers, CI/CD marketing)
- Repeat analysis already briefed in an earlier batch unless there is a new operational fact
- Duplicate coverage of the same incident: keep one bullet; name the strongest outlet and, if useful, the other outlets in the same bullet

Consolidation
- One incident = one bullet even if 3–6 cards cover it (e.g. Houthi strike on Riyadh; mass drone attack on Moscow; synagogue arson sequence).

Output format
1. One-line scope: date range, card count used, and (if needed) a short note that the count differs slightly from expected.
2. Same section headings as the previous brief if they still fit. If they do not, use:
   - Energy / Electric
   - Water / Wastewater
   - Transportation
   - Communications / Cyber
   - Government / Emergency Services
   - Other CI / Soft targets
   Omit empty headings. Do not invent a heading to save a weak card.
3. Under each heading, bullets only. Each bullet:
   - Article title as it appears on the card (or a tight factual rewrite if the title is clickbait)
   - Outlet in parentheses; if several cards are the same story, one title plus outlets
   - Optional: one short clause with location + CI relevance if that is not already in the title
4. After the section bullets, “Tactical takeaways”: 3–6 bullets of patterns visible in this batch only (who/what/where repeating). No strategy essays.
5. Do not add recommendations, policy advice, or a narrative intro beyond the one-line scope.
6.  Organize First alert incidents by state and avoid a mass paragraph with all incidents jumbled together.
Constraints
- English, tight, no filler.
- No article that is only strategic “big picture.”
- If you are unsure an item is CI-relevant, put it under Other CI / Soft targets rather than stretching a sector heading.
- When finished, leave the brief in [[Summary for 19NOV2026]]    and give a short process note: cards in / cards omitted (categories only, not a second brief) / headings used / takeaway count.

Then include a strategic level summary like that seen in notes Summary for 11SEP2026-Summary for 18NOV2026 for the notes set specified above. See the combined [[Summary for 18NOV2026]]  .
[Timestamp: 2026/11/19 07:38:11]

**ai**: **Error:** Internal error: UNKNOWN_CERTIFICATE_VERIFICATION_ERROR: unknown certificate verification error
[Timestamp: 2026/11/19 07:38:11]

**user**: Task
Write today’s Priority Headlines brief from the article cards in the note [[Today]]  and including the information from [[All Hazards Brief 2026-11-19]], [[CI Sector Brief 2026-11-19]], and [[USBR Brief 2026-11-19]]   .
Title it exactly: Priority Headlines for DDMMMYYYY
(Use the briefing date, e.g. Priority Headlines for 18NON2026. Write the finished brief into [[Summary for 19NOV2026]].)

Source of truth
- Use only article cards in [[Today]] whose created/imported timestamp is on or after the cutoff (default: three calendar days before the briefing date at 08:00 local, or the cutoff given in the request).
- State the card count in the scope line. If the count is materially different from what the user expected, say so at the top and continue with what is present. A 2–3 card delta is not material.
- Do not invent outlets, titles, facts, or incidents. If a card is thin, summarize only what is on the card.
- Match the structure, heading style, bullet style, and density of the previous brief [[Summary for 19NOV2026]]   (or the most recent Priority Headlines note if that filename differs). Copy the format; do not copy that brief’s content.

What “tactical” means here
Lead with operational, place-and-time, asset-specific items. Prefer:
- Named facilities, utilities, plants, substations, ports, airports, rail, pipelines, water systems, telecom/data centers, emergency services
- Attacks, intrusions, disruptions, arrests, devices, drones/UAS, vandalism, sabotage, cyber incidents with a concrete target
- Sector, location, actor, or TTPs if the card has them
 - Organize First alert incidents by state and avoid a mass paragraph with all incidents jumbled together. Please bulletize the Energy/Electric section and organize by country and state.
For the Strategic Section focus on:
- High-level geopolitics, market commentary, and “what it means for the world” unless they name a CI asset or an imminent operational effect
- Diplomacy, pacts, travel, legislation, and opinion essays with no incident                                               
Demote or omit:
- False positives (movies, gadgets, exam leaks, academic SVR/forecast papers, CI/CD marketing)
- Repeat analysis already briefed in an earlier batch unless there is a new operational fact
- Duplicate coverage of the same incident: keep one bullet; name the strongest outlet and, if useful, the other outlets in the same bullet

Consolidation
- One incident = one bullet even if 3–6 cards cover it (e.g. Houthi strike on Riyadh; mass drone attack on Moscow; synagogue arson sequence).

Output format
1. One-line scope: date range, card count used, and (if needed) a short note that the count differs slightly from expected.
2. Same section headings as the previous brief if they still fit. If they do not, use:
   - Energy / Electric
   - Water / Wastewater
   - Transportation
   - Communications / Cyber
   - Government / Emergency Services
   - Other CI / Soft targets
   Omit empty headings. Do not invent a heading to save a weak card.
3. Under each heading, bullets only. Each bullet:
   - Article title as it appears on the card (or a tight factual rewrite if the title is clickbait)
   - Outlet in parentheses; if several cards are the same story, one title plus outlets
   - Optional: one short clause with location + CI relevance if that is not already in the title
4. After the section bullets, “Tactical takeaways”: 3–6 bullets of patterns visible in this batch only (who/what/where repeating). No strategy essays.
5. Do not add recommendations, policy advice, or a narrative intro beyond the one-line scope.
6.  Organize First alert incidents by state and avoid a mass paragraph with all incidents jumbled together.
Constraints
- English, tight, no filler.
- No article that is only strategic “big picture.”
- If you are unsure an item is CI-relevant, put it under Other CI / Soft targets rather than stretching a sector heading.
- When finished, leave the brief in [[Summary for 19NOV2026]]    and give a short process note: cards in / cards omitted (categories only, not a second brief) / headings used / takeaway count.

Then include a strategic level summary like that seen in notes Summary for 11SEP2026-Summary for 18NOV2026 for the notes set specified above. See the combined [[Summary for 18NOV2026]]  .
[Timestamp: 2026/11/19 07:42:18]

**ai**: **Error:** Internal error: UNKNOWN_CERTIFICATE_VERIFICATION_ERROR: unknown certificate verification error
[Timestamp: 2026/11/19 07:42:18]
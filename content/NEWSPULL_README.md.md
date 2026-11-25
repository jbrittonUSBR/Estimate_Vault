# News pull, sources page, and Obsidian cards

Two tracks share the same scripts. GitHub Pages publishes the daily bibliography. The Obsidian vault stays on this PC.

|   |   |   |
|---|---|---|
|Track|Where|What it produces|
|GitHub Actions|jbrittonUSBR.github.io|sources/YYYY/MM/YYYY-MM-DD.md and data/YYYY/MM/YYYY-MM-DD-ci.json|
|Desktop Agent|C:\Users\JBritton\OneDrive - DOI\Desktop\Agent|newspull.json → newspull_ci.json → Obsidian cards|

Python: C:\Users\JBritton\AppData\Local\anaconda3\python.exe

Agent folder: C:\Users\JBritton\OneDrive - DOI\Desktop\Agent

Vault: C:\Users\JBritton\Threat_Estimate_2027

Pages repo (local clone): C:\Users\JBritton\jbrittonUSBR.github.io

Live site: https://jbrittonusbr.github.io

---

## 1. Scripts

|   |   |
|---|---|
|File|Role|
|newspull_to_json.py|NewsAPI /v2/everything. Asks for a key unless NEWSAPI_KEY is set. Writes newspull.json + .txt.|
|filter_ci_json.py|Title/citation CI + terrorism screen. Drops Biztoc, contracts, guidance, sports. Writes newspull_ci.json.|
|map_unmapped_to_topics.py|Maps query/title → vault topic. Dedupes URL/title. Writes newspull_ci_mapped.json.|
|newspull_to_obsidian.py|Creates Card No. PREFIX-YEAR-N; Title.md under each topic Cards folder.|
|add_url_card.py|One URL → one card (for stories NewsAPI missed).|
|chicago_citations.py|Jekyll sources page (layout: page, permalink /YYYY/MM/DD/sources/).|
|.github/workflows/newspull.yml|Weekdays 12:00 UTC (06:00 MDT) plus manual **Run workflow**.|

Do not commit API keys. Actions uses repo secret NEWSAPI_KEY.

---

## 2. Weekday automation (GitHub)

Repo secret: **Settings → Secrets and variables → Actions →** NEWSAPI_KEY

Workflow file: .github/workflows/newspull.yml

Each run:

1. scripts/newspull_to_json.py → newspull.json
    
2. scripts/filter_ci_json.py → newspull_ci.json
    
3. scripts/chicago_citations.py → sources/YYYY/MM/YYYY-MM-DD.md
    
4. Copy JSON to data/YYYY/MM/YYYY-MM-DD-ci.json
    
5. Delete raw newspull.json
    
6. Commit and push
    

Manual test: **Actions → Weekday news pull → Run workflow**

After Pages rebuilds:

- Bibliography: https://jbrittonusbr.github.io/YYYY/MM/DD/sources/
    
- Saved JSON: data/YYYY/MM/YYYY-MM-DD-ci.json on main
    

The home-page **calendar** reads sources/. The **Bibliography — date** box on index.md must use site.pages filtered to /sources/ (not site.posts.first). Daily Brief still comes from _posts/.

---

## 3. Desktop pull (when you want cards the same day)

```powershell
cd "C:\Users\JBritton\OneDrive - DOI\Desktop\Agent"

$py = "C:\Users\JBritton\AppData\Local\anaconda3\python.exe"
$vault = "C:\Users\JBritton\Threat_Estimate_2027"

& $py .\newspull_to_json.py --insecure --out .\newspull.json
& $py .\filter_ci_json.py --in .\newspull.json --out .\newspull_ci.json
& $py .\map_unmapped_to_topics.py --in .\newspull_ci.json --out .\newspull_ci_mapped.json
& $py .\newspull_to_obsidian.py --json .\newspull_ci_mapped.json --vault $vault --dry-run
& $py .\newspull_to_obsidian.py --json .\newspull_ci_mapped.json --vault $vault
```

--insecure is the DOI SSL workaround. Drop it off-network if the cert chain is fine.

--dry-run prints paths only. Remove it to write cards.

Obsidian Dataview (today’s cards):

```dataview
TABLE card, outlet, published, imported
WHERE type = "news-card" AND imported = date(today)
SORT file.name asc
```

After importing today's cards, run the workflow in [[Prompts/Daily News Card Summary Prompt]] to identify and summarize cards that lack a dateline paragraph.

---

## 4. One-off URL (missed by NewsAPI)

```powershell
cd "C:\Users\JBritton\OneDrive - DOI\Desktop\Agent"
& "C:\Users\JBritton\AppData\Local\anaconda3\python.exe" .\add_url_card.py `
    --url "https://www.justice.gov/opa/pr/..." `
    --topic Insider `
    --vault "C:\Users\JBritton\Threat_Estimate_2027"
```

--topic is a prefix (UAS, IED, FTO, Insider, HS, SVT, Cyber, …) or a folder name. --dry-run first. --force if the URL already exists.

---

## 5. Daily Brief post (home page “Priority Headlines”)

Actions does **not** write _posts. Add the brief by hand in the Pages repo:

_posts/2026/09/2026-09-17-priority_headlines.md

```markdown
---
layout: post
title: "Priority Headlines for 17SEP2026"
date: 2026-09-17 09:00:00 -0600
categories: news
---

## 1. Theme (UAS/SVT/FTO)
- bullet
- bullet

## Sources
[Open the 17 September 2026 bibliography]({{ '/2026/09/17/sources/' | relative_url }})
```

```powershell
cd C:\Users\JBritton\jbrittonUSBR.github.io
git add _posts/2026/09/2026-09-17-priority_headlines.md
git commit -m "Brief 17 Sep 2026"
git push origin main
```

Until that file exists, Daily Brief on the home page stays on the previous post date. The bibliography box follows the latest sources page if index.md uses the site.pages /sources/ assign.

---

## 6. Search terms and filter

Edit SEARCH_TERMS only in newspull_to_json.py (Agent **and** scripts/ in the repo). Each string is one NewsAPI request (100/day on the developer plan).

Each list item must be **one** Python string. This is invalid:

```python
'Espionage AND ...' OR '(Espionage OR "murder for hire" ...)'
```

filter_ci_json.py KEEP is title-only. Bare drone, airport, plot were removed so market copy drops. Add paired patterns for cases like “US charges five people over alleged Russian plots”.

Biztoc, contract/award/guidance, and empty titles are dropped even if a KEEP word appears.

---

## 7. Topic map (Obsidian folders)

|   |   |   |
|---|---|---|
|Needle / query|Folder|Prefix|
|drone / UAS / UAV|1 - UAS|UAS|
|bombing / IED|2 - IED|IED|
|ballistic / substation shooting|3 - Ballistic|Ballistic|
|active shooter|4 - Armed Hostile Event (AHE)|AHE|
|vehicle ramming|5 - Vehicle Ramming Incident (VRI)|VRI|
|arson|6 - Arson|ARN|
|CBRN|7 - CBRN|CBRN|
|cyber / SCADA|8 - Cyber|Cyber|
|sabotage / vandalism / theft|9 - Sabotage, Vandalism, Theft|SVT|
|surveillance|10 - Hostile Surveillance (HS)|HS|
|emerging threats|11 - Emerging Trends|ET|
|DVE|12 - DVE|DVE|
|terrorism / FTO|13 - FTO|FTO|
|geopolitical|14 - NST|NST|
|insider / espionage / intel services|15 - Insider Threat|Insider|
|neoluddite|16 - Grievance Triggers|GT|

Title overrides beat the query (blast at a station → IED, not Cyber). Duplicate URL or near-duplicate title is skipped.

---

## 8. Sources page format

chicago_citations.py must emit blank lines and <!-- --> around --- so kramdown does not merge numbered lists across topics.

Copy the script into **both** Agent and jbrittonUSBR.github.io\scripts\ after any edit.

---

## 9. Pushing workflow files

A classic PAT needs repo **+** workflow to change .github/workflows/newspull.yml. Without workflow, edit that file on github.com. Scripts under scripts/ push with repo alone.

---

## 10. If something is missing

|   |   |
|---|---|
|Symptom|Cause|
|Bibliography box still shows yesterday|index.md still uses site.posts.first, or Pages has not rebuilt|
|Calendar has today, brief does not|No _posts file for today|
|No newspull_ci.json on GitHub|File lives at data/YYYY/MM/YYYY-MM-DD-ci.json after the updated workflow; older runs deleted it|
|Actions YAML error line 25|Broken indent or smart quotes — paste the whole workflow in the GitHub editor|
|Node 20 annotation|Bump actions/checkout@v5 and actions/setup-python@v6|
|Card not created|Unmapped query, duplicate URL/title, or dry-run|
|Story never in JSON|NewsAPI query/title miss — add_url_card.py|

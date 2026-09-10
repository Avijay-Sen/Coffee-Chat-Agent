# Coffee Chat Agent

A small CLI that helps you run a healthcare-focused coffee-chat networking
campaign: browse target companies across the healthcare value chain --
**consulting**, **digital health/product**, **big pharma**, **biotech**,
**medtech/devices**, **payers/insurance**, **CROs**, and **healthcare-focused
investing** (spanning startups to giants) -- generate LinkedIn/Google search
strings to find real people in **Operations**, **R&D**, **Strategy**,
**Commercial**, **Regulatory**, **Manufacturing**, **Clinical Development**,
or **Data/Analytics** roles there, draft personalized outreach messages for
email or LinkedIn, and track who you've reached out to.

## Why it works this way

There's no LinkedIn API/scraping access here, so this tool never invents
names -- either it gives you a ready-to-paste search string to find the
actual human yourself on LinkedIn, or (for the daily targets, below) it
names a real person only when their role is genuinely public (an official
company leadership page, a press release, a conference speaker list) with
a source link included so you can verify it yourself.

## Daily targets

`daily_targets/` holds one file per day (`YYYY-MM-DD.md`), each with ~5 real
people to reach out to, sourced from public leadership pages/press releases
(never LinkedIn scraping), plus ready-to-send email and LinkedIn drafts for
each. `coffee_chat_agent/daily.py` deterministically rotates through
`data.py`'s companies (spread across segments) so the same company isn't
suggested twice until every company has been covered once; its state lives
in `daily_targets/.state.json`.

```bash
# Get today's 5 target companies (doesn't touch state)
python3 -m coffee_chat_agent.cli daily-next --count 5

# After writing today's daily_targets/<date>.md, mark those companies used
python3 -m coffee_chat_agent.cli daily-mark-covered "Pfizer" "Medtronic" ...
```

Note: sourcing from public bios tends to surface senior leaders (VP/C-suite)
since they're the ones with public profiles -- great for learning about the
role, but reply odds from a cold student outreach are realistically low at
that level. Pair this with `search-string` to also find more reachable
Director/Manager-level people at the same companies.

## Setup

No dependencies beyond Python 3 (stdlib only).

```bash
cd coffee_chat_agent  # or run as a module from the repo root, see below
```

## Usage

Run everything as a module from the repo root:

```bash
# 1. Browse target companies (segments: Consulting, Product, Pharma, Biotech,
#    MedTech, Payer, CRO, Investing)
python3 -m coffee_chat_agent.cli list --segment Pharma --function "R&D"
python3 -m coffee_chat_agent.cli list --segment Consulting --size Mid-size
python3 -m coffee_chat_agent.cli list --segment Biotech
python3 -m coffee_chat_agent.cli list --segment MedTech --function Regulatory
python3 -m coffee_chat_agent.cli list --segment Payer
python3 -m coffee_chat_agent.cli list --segment CRO --function "Clinical Development"
python3 -m coffee_chat_agent.cli list --segment Investing

# 2. Get a search string to find real people at a target company
python3 -m coffee_chat_agent.cli search-string --company "Pfizer" --function "R&D"
python3 -m coffee_chat_agent.cli search-string --company "McKinsey & Company (Healthcare Systems & Services)" \
    --function Operations --seniority "Manager"

# 3. Draft an outreach message once you have a name
python3 -m coffee_chat_agent.cli draft --channel email \
    --my-name "Avijay" \
    --my-background "an undergrad BioE student exploring healthcare/pharma operations" \
    --recipient-name "Jane Doe" \
    --recipient-company "Pfizer" \
    --recipient-role "Director, R&D Operations" \
    --hook "I saw your talk on pharma supply chain resilience"

python3 -m coffee_chat_agent.cli draft --channel linkedin \
    --my-name "Avijay" --my-background "an MBA student exploring healthcare ops" \
    --recipient-name "Jane Doe" --recipient-company "Pfizer" \
    --hook "we're both alumni of the same school"

# 4. Log outreach so you can follow up
python3 -m coffee_chat_agent.cli log --name "Jane Doe" --company Pfizer \
    --segment Pharma --role "Director, R&D Operations" --channel email
python3 -m coffee_chat_agent.cli log-list

# 5. Networking tips
python3 -m coffee_chat_agent.cli tips
```

`log` appends to `outreach_log.csv` at the repo root (git-ignored, since it
will contain real names/contacts once you use it).

## Data

- `coffee_chat_agent/data.py` -- curated (not scraped) starting list of
  companies across the three segments and three functions. Update this file
  freely as you research more targets; it's a plain Python tuple of
  `Company` records.
- `coffee_chat_agent/search.py` -- builds Google X-ray (`site:linkedin.com/in ...`)
  and native LinkedIn search guidance per company/function.
- `coffee_chat_agent/templates.py` -- message templates for LinkedIn
  connection notes, LinkedIn messages, cold emails, follow-ups, and
  thank-you notes.
- `coffee_chat_agent/tracker.py` -- CSV-backed outreach log.
- `coffee_chat_agent/cli.py` -- ties it all together.

## Extending it

- Add companies/segments/functions in `data.py` as you find more targets
  (alumni database, employer's internal directory, industry newsletters,
  conference speaker lists, etc. are all better sources of *real names*
  than anything scraped).
- If you get LinkedIn API or a people-data provider (e.g. via your school's
  career services tools) hooked up later, `search.py` is the natural place
  to wire in an actual lookup instead of just generating a search string.

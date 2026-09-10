# Coffee Chat Agent

A small CLI that helps you run a healthcare-focused coffee-chat networking
campaign: browse target companies across **healthcare consulting**,
**healthcare product/health tech**, and **big pharma/biotech** (spanning
startups to giants), generate LinkedIn/Google search strings to find real
people in **Operations**, **R&D**, or **Strategy** roles there, draft
personalized outreach messages for email or LinkedIn, and track who you've
reached out to.

## Why it works this way

This tool intentionally does **not** produce a list of named individuals to
message. There's no LinkedIn API/scraping access here, and generating
specific private people's names or contact details without a live directory
would mean making them up -- not useful and not okay to send. Instead, the
agent gets you 90% of the way: real target companies, a ready-to-paste
search string to find the actual humans yourself on LinkedIn, and a
strong message draft the moment you have a name.

## Setup

No dependencies beyond Python 3 (stdlib only).

```bash
cd coffee_chat_agent  # or run as a module from the repo root, see below
```

## Usage

Run everything as a module from the repo root:

```bash
# 1. Browse target companies
python3 -m coffee_chat_agent.cli list --segment Pharma --function "R&D"
python3 -m coffee_chat_agent.cli list --segment Consulting --size Mid-size
python3 -m coffee_chat_agent.cli list --segment Product

# 2. Get a search string to find real people at a target company
python3 -m coffee_chat_agent.cli search-string --company "Pfizer" --function "R&D"
python3 -m coffee_chat_agent.cli search-string --company "McKinsey & Company (Healthcare Systems & Services)" \
    --function Operations --seniority "Manager"

# 3. Draft an outreach message once you have a name
python3 -m coffee_chat_agent.cli draft --channel email \
    --my-name "Avijay" \
    --my-background "an MBA student exploring healthcare/pharma operations" \
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

"""Command-line entry point for the Coffee Chat Agent.

Examples:
    python -m coffee_chat_agent.cli list --segment Pharma --function "R&D"
    python -m coffee_chat_agent.cli search-string --company "Pfizer" --function "R&D"
    python -m coffee_chat_agent.cli draft --channel email --my-name "Avijay" \\
        --recipient-name "Jane Doe" --recipient-company "Pfizer" \\
        --recipient-role "Director, R&D Operations" \\
        --my-background "an MBA student interested in healthcare/pharma ops" \\
        --hook "I saw your talk on pharma supply chain resilience"
    python -m coffee_chat_agent.cli log --name "Jane Doe" --company Pfizer \\
        --segment Pharma --role "Director, R&D Operations" --channel email
    python -m coffee_chat_agent.cli tips
"""

import argparse
import sys

from . import alumni as alumni_mod
from . import data as data_mod
from . import daily as daily_mod
from . import search as search_mod
from . import templates as templates_mod
from . import tracker as tracker_mod

ALUMNI_HOOK = "We're both part of the UC Berkeley community"

TIPS = """\
Coffee chat networking tips (healthcare consulting / product / pharma):

1. Lead with a specific, low-effort ask. "15-20 minutes" reads as easy to
   say yes to; "pick your brain" or open-ended asks get ignored.
2. Personalize one sentence minimum -- shared school, a post they wrote, a
   project, a mutual connection. This is the single biggest reply-rate lever.
3. Warm paths beat cold ones. Check alumni networks, past coworkers, and
   mutual LinkedIn connections before cold-emailing/DMing.
4. Segment your ask by function, not just company: "Operations" people can
   speak to supply chain, launch execution, manufacturing; "R&D" people to
   clinical development, discovery, regulatory strategy. Ask what matches
   their actual role, not a generic "tell me about the industry."
5. Follow up once, politely, after ~7-10 days if you hear nothing. Don't
   follow up more than twice.
6. Come with 3-4 real questions (their path into the role/industry, a
   day-in-the-life, what they'd do differently, advice for someone like you)
   -- don't make them improvise the whole conversation.
7. Always send a thank-you within 24 hours, and close the loop later if
   their advice led anywhere (interview, decision, etc.) -- people remember
   who followed up.
8. Startups vs. big pharma vs. consulting giants have very different
   cultures/paces -- tailor your questions (e.g. ask a startup person about
   scope/ambiguity, ask a big-pharma person about how decisions get made
   cross-functionally, ask a consultant about client variety/travel).
9. Track everything (see the `log` command) -- volume + follow-through beats
   sending one polished message and waiting.
10. Respect a "not right now" -- a graceful decline reply keeps the door
    open for later.
"""


def cmd_list(args):
    companies = data_mod.filter_companies(segment=args.segment, function=args.function, size=args.size)
    if not companies:
        print("No companies matched those filters.")
        return
    for c in companies:
        funcs = ", ".join(c.functions)
        note = f" -- {c.notes}" if c.notes else ""
        print(f"[{c.segment} | {c.size}] {c.name} ({funcs}){note}")


def cmd_search_string(args):
    keywords = args.keywords.split(",") if args.keywords else None
    query = search_mod.linkedin_site_search(
        args.company, function=args.function, keywords=keywords, seniority=args.seniority
    )
    print("Google X-ray search (paste into Google):")
    print(f"  {query}")
    print()
    print("Native LinkedIn search:")
    print(f"  {search_mod.linkedin_native_search_url_hint(args.company, args.function)}")


def cmd_draft(args):
    recipient_company = args.recipient_company
    recipient_role = args.recipient_role
    hook = args.hook

    if args.alumni:
        hook = hook or ALUMNI_HOOK
        known = alumni_mod.find(args.recipient_name)
        if known:
            recipient_company = recipient_company or known.get("company", "")
            recipient_role = recipient_role or known.get("role", "")

    if not recipient_company:
        raise SystemExit(
            "--recipient-company is required (not found in alumni.csv either -- "
            "add it with `alumni-add` first, or pass --recipient-company directly)."
        )

    ctx = templates_mod.OutreachContext(
        my_name=args.my_name,
        recipient_name=args.recipient_name,
        recipient_company=recipient_company,
        recipient_role=recipient_role,
        hook=hook,
        mutual_connection=args.mutual_connection,
        my_background=args.my_background,
        channel=args.channel,
    )
    if args.channel == "email":
        result = templates_mod.cold_email(ctx)
        print(f"Subject: {result['subject']}\n")
        print(result["body"])
    else:
        print("--- Connection note (<=300 chars) ---")
        print(templates_mod.linkedin_connection_note(ctx))
        print("\n--- Full LinkedIn message (send after they accept) ---")
        print(templates_mod.linkedin_message(ctx))


def cmd_log(args):
    tracker_mod.add_entry(
        name=args.name, company=args.company, segment=args.segment,
        role=args.role, channel=args.channel, status=args.status,
        followup_date=args.followup_date, notes=args.notes,
    )
    print(f"Logged {args.name} @ {args.company} to {tracker_mod.DEFAULT_PATH}")


def cmd_log_list(args):
    entries = tracker_mod.list_entries()
    if not entries:
        print("No outreach logged yet.")
        return
    for e in entries:
        print(f"{e['date_contacted']} | {e['name']} @ {e['company']} ({e['role']}) "
              f"[{e['channel']}] -- {e['status']}")


def cmd_tips(args):
    print(TIPS)


def cmd_daily_next(args):
    for c in daily_mod.next_targets(n=args.count):
        funcs = ", ".join(c.functions)
        print(f"{c.name} | {c.segment} | {c.size} | ({funcs})")


def cmd_daily_mark_covered(args):
    daily_mod.mark_covered(args.companies)
    print(f"Marked {len(args.companies)} companies as covered.")


def cmd_alumni_add(args):
    alumni_mod.add(
        name=args.name, company=args.company, role=args.role,
        segment=args.segment or "", function=args.function or "",
        source=args.source, notes=args.notes,
    )
    print(f"Added {args.name} @ {args.company} to {alumni_mod.DEFAULT_PATH}")


def cmd_alumni_list(args):
    rows = alumni_mod.list_all()
    if not rows:
        print("No alumni logged yet. Use `alumni-add` to start building the list.")
        return
    for r in rows:
        print(f"[{r['contacted']}] {r['name']} @ {r['company']} ({r['role']}) -- source: {r['source']}")


def cmd_alumni_next(args):
    rows = alumni_mod.next_uncontacted(n=args.count)
    if not rows:
        print("No uncontacted alumni left -- add more with `alumni-add`.")
        return
    for r in rows:
        print(f"{r['name']} @ {r['company']} ({r['role']}) -- source: {r['source']}")


def cmd_alumni_mark_contacted(args):
    alumni_mod.mark_contacted(args.names)
    print(f"Marked {len(args.names)} alumni as contacted.")


def build_parser():
    parser = argparse.ArgumentParser(prog="coffee-chat-agent")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List target companies")
    p_list.add_argument("--segment", choices=data_mod.SEGMENTS)
    p_list.add_argument("--function", choices=data_mod.FUNCTIONS)
    p_list.add_argument("--size", choices=data_mod.SIZES)
    p_list.set_defaults(func=cmd_list)

    p_search = sub.add_parser("search-string", help="Generate a LinkedIn/Google X-ray search string")
    p_search.add_argument("--company", required=True)
    p_search.add_argument("--function", choices=data_mod.FUNCTIONS)
    p_search.add_argument("--keywords", help="Comma-separated role keywords, overrides --function defaults")
    p_search.add_argument("--seniority", help='e.g. "Director", "VP", "Manager"')
    p_search.set_defaults(func=cmd_search_string)

    p_draft = sub.add_parser("draft", help="Draft a coffee-chat outreach message")
    p_draft.add_argument("--channel", choices=["email", "linkedin"], default="linkedin")
    p_draft.add_argument("--my-name", required=True)
    p_draft.add_argument("--my-background", required=True,
                          help='e.g. "an MBA student interested in healthcare ops"')
    p_draft.add_argument("--recipient-name", required=True)
    p_draft.add_argument("--recipient-company", default="",
                          help="Required unless --alumni finds it from alumni.csv")
    p_draft.add_argument("--recipient-role", default="")
    p_draft.add_argument("--hook", default="", help="One specific personalization line")
    p_draft.add_argument("--mutual-connection", default="")
    p_draft.add_argument("--alumni", action="store_true",
                          help="Default the hook to a shared-school note and look up "
                               "company/role from alumni.csv if not given")
    p_draft.set_defaults(func=cmd_draft)

    p_log = sub.add_parser("log", help="Log an outreach attempt")
    p_log.add_argument("--name", required=True)
    p_log.add_argument("--company", required=True)
    p_log.add_argument("--segment", choices=data_mod.SEGMENTS, required=True)
    p_log.add_argument("--role", default="")
    p_log.add_argument("--channel", choices=["email", "linkedin"], required=True)
    p_log.add_argument("--status", default="sent")
    p_log.add_argument("--followup-date", default="")
    p_log.add_argument("--notes", default="")
    p_log.set_defaults(func=cmd_log)

    p_log_list = sub.add_parser("log-list", help="Show logged outreach")
    p_log_list.set_defaults(func=cmd_log_list)

    p_tips = sub.add_parser("tips", help="Print networking tips")
    p_tips.set_defaults(func=cmd_tips)

    p_daily_next = sub.add_parser("daily-next", help="Get the next N companies for today's outreach targets")
    p_daily_next.add_argument("--count", type=int, default=5)
    p_daily_next.set_defaults(func=cmd_daily_next)

    p_daily_mark = sub.add_parser("daily-mark-covered", help="Mark companies as covered so they aren't repeated")
    p_daily_mark.add_argument("companies", nargs="+", help="Exact company name(s) as printed by daily-next")
    p_daily_mark.set_defaults(func=cmd_daily_mark_covered)

    p_alumni_add = sub.add_parser("alumni-add", help="Log an alumni contact found via LinkedIn's Alumni page, CalConnect, etc.")
    p_alumni_add.add_argument("--name", required=True)
    p_alumni_add.add_argument("--company", required=True)
    p_alumni_add.add_argument("--role", default="")
    p_alumni_add.add_argument("--segment", choices=data_mod.SEGMENTS)
    p_alumni_add.add_argument("--function", choices=data_mod.FUNCTIONS)
    p_alumni_add.add_argument("--source", default="",
                               help='e.g. "LinkedIn Alumni page", "CalConnect", "BioE alumni directory"')
    p_alumni_add.add_argument("--notes", default="")
    p_alumni_add.set_defaults(func=cmd_alumni_add)

    p_alumni_list = sub.add_parser("alumni-list", help="Show all logged alumni contacts")
    p_alumni_list.set_defaults(func=cmd_alumni_list)

    p_alumni_next = sub.add_parser("alumni-next", help="Show uncontacted alumni to reach out to next")
    p_alumni_next.add_argument("--count", type=int, default=5)
    p_alumni_next.set_defaults(func=cmd_alumni_next)

    p_alumni_mark = sub.add_parser("alumni-mark-contacted", help="Mark alumni as contacted")
    p_alumni_mark.add_argument("names", nargs="+", help="Exact name(s) as logged via alumni-add")
    p_alumni_mark.set_defaults(func=cmd_alumni_mark_contacted)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())

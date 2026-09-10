"""Coffee-chat outreach message templates for email and LinkedIn.

Keep messages short, specific, and low-pressure -- a 15-20 minute chat ask,
not a favor ask. Fill in `hook` with something real and specific (a shared
school, a post they wrote, a mutual connection, a project of theirs) --
generic messages get ignored.
"""

from dataclasses import dataclass


def _sentence(text: str) -> str:
    """Return text as a standalone sentence (trailing period + space), or ''."""
    text = text.strip()
    if not text:
        return ""
    if text[-1] not in ".!?":
        text += "."
    return text + " "


@dataclass
class OutreachContext:
    my_name: str
    recipient_name: str
    recipient_company: str
    recipient_role: str = ""
    hook: str = ""  # e.g. "we both went to X" or "I saw your post on Y"
    mutual_connection: str = ""
    my_background: str = ""  # one-line: e.g. "a BA/MS student exploring healthcare consulting"
    channel: str = "linkedin"  # "linkedin" | "email"


def linkedin_connection_note(ctx: OutreachContext) -> str:
    """LinkedIn connection request notes are capped at 300 characters."""
    hook = f" {_sentence(ctx.hook)}".rstrip() if ctx.hook else ""
    msg = (
        f"Hi {ctx.recipient_name}, I'm {ctx.my_name}, {ctx.my_background}."
        + hook
        + f" Would love to connect and hear about your work at {ctx.recipient_company}."
    )
    return msg[:300]


def linkedin_message(ctx: OutreachContext) -> str:
    hook_line = _sentence(ctx.hook)
    mutual_line = _sentence(f"{ctx.mutual_connection} suggested I reach out" if ctx.mutual_connection else "")
    role_clause = f" as a {ctx.recipient_role}" if ctx.recipient_role else ""
    return (
        f"Hi {ctx.recipient_name},\n\n"
        f"{mutual_line}I'm {ctx.my_name}, {ctx.my_background}. {hook_line}"
        f"I've been really interested in {ctx.recipient_company}'s work"
        f"{role_clause} and would love to hear how you got into it and what "
        f"a typical day looks like.\n\n"
        f"Would you have 15-20 minutes in the next couple weeks for a quick "
        f"virtual coffee chat? Happy to work around your schedule.\n\n"
        f"Thanks so much for considering it,\n{ctx.my_name}"
    )


def cold_email(ctx: OutreachContext) -> dict:
    hook_line = _sentence(ctx.hook)
    mutual_line = _sentence(f"{ctx.mutual_connection} suggested I reach out" if ctx.mutual_connection else "")
    role_clause = f" as {ctx.recipient_role}" if ctx.recipient_role else ""
    subject = f"Quick coffee chat re: {ctx.recipient_company}"
    body = (
        f"Hi {ctx.recipient_name},\n\n"
        f"{mutual_line}My name is {ctx.my_name} -- {ctx.my_background}. {hook_line}"
        f"I came across your work at {ctx.recipient_company}{role_clause} and "
        f"would love to learn more about your path and what the healthcare "
        f"side of the business looks like day to day.\n\n"
        f"Would you be open to a brief 15-20 minute call in the next few weeks? "
        f"I'm glad to work around whatever time is easiest for you.\n\n"
        f"Thank you for considering it -- I know your time is valuable.\n\n"
        f"Best,\n{ctx.my_name}"
    )
    return {"subject": subject, "body": body}


def followup_message(ctx: OutreachContext, days_since: int = 7) -> str:
    return (
        f"Hi {ctx.recipient_name}, just floating this back up in case it got "
        f"buried -- still would love a quick 15-20 minute chat about your "
        f"experience at {ctx.recipient_company} if you have time in the coming "
        f"weeks. No worries at all if now isn't a good time.\n\nBest,\n{ctx.my_name}"
    )


def thank_you_message(ctx: OutreachContext) -> str:
    return (
        f"Hi {ctx.recipient_name}, thank you so much for taking the time to "
        f"chat -- I really appreciated hearing about your experience at "
        f"{ctx.recipient_company} and your advice. I'll keep you posted on "
        f"where things go, and please don't hesitate to reach out if there's "
        f"ever anything I can help with on my end.\n\nBest,\n{ctx.my_name}"
    )

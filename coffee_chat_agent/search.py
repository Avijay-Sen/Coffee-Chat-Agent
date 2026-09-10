"""Generate LinkedIn/Google X-ray search strings to find real people at a
target company. This tool does not query LinkedIn itself (no scraping/API
access) -- it produces search strings you paste into Google or LinkedIn's
own search bar.
"""

DEFAULT_ROLE_KEYWORDS = {
    "Operations": ["Operations", "Ops", "Program Manager", "Supply Chain"],
    "R&D": ["R&D", "Research", "Clinical Development", "Discovery"],
    "Strategy": ["Strategy", "Corporate Strategy", "Consultant"],
}


def linkedin_site_search(company: str, function: str = None, keywords: list = None, seniority: str = None) -> str:
    """Build a Google X-ray query targeting LinkedIn profiles."""
    terms = [f'site:linkedin.com/in "{company}"']
    role_terms = list(keywords) if keywords else DEFAULT_ROLE_KEYWORDS.get(function, [])
    if role_terms:
        role_clause = " OR ".join(f'"{t}"' for t in role_terms)
        terms.append(f"({role_clause})")
    if seniority:
        terms.append(f'"{seniority}"')
    return " ".join(terms)


def linkedin_native_search_url_hint(company: str, function: str = None) -> str:
    """Describe how to run the equivalent search directly in LinkedIn."""
    role_terms = DEFAULT_ROLE_KEYWORDS.get(function, [])
    keyword_str = " / ".join(role_terms) if role_terms else "(role keyword)"
    return (
        f"In LinkedIn search: People > Current company = \"{company}\" "
        f"+ Title contains {keyword_str}. Then filter by 2nd-degree connections "
        "or School (shared alma mater) to raise reply odds."
    )

"""Curated target list of organizations in healthcare consulting, healthcare
product/health tech, and big pharma/biotech, spanning startups to giants.

This is a starting point, not a scraped or verified real-time list -- company
names, sizes, and focus areas change. Treat `notes` as a prompt for your own
quick research, not a substitute for it.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Company:
    name: str
    segment: str  # "Consulting" | "Product" | "Pharma"
    functions: tuple  # e.g. ("Operations", "R&D", "Strategy")
    size: str  # "Startup" | "Mid-size" | "Large/Enterprise"
    notes: str = ""


COMPANIES: tuple = (
    # --- Healthcare Consulting ---
    Company("McKinsey & Company (Healthcare Systems & Services)", "Consulting",
            ("Strategy", "Operations"), "Large/Enterprise",
            "Broad healthcare + pharma practice; look for 'Life Sciences' or 'Healthcare Systems & Services' practice tags."),
    Company("Boston Consulting Group (Health Care practice)", "Consulting",
            ("Strategy", "Operations", "R&D"), "Large/Enterprise",
            "Strong biopharma R&D and market access work."),
    Company("Bain & Company (Healthcare & Life Sciences)", "Consulting",
            ("Strategy", "Operations"), "Large/Enterprise", ""),
    Company("Deloitte (Life Sciences & Health Care)", "Consulting",
            ("Operations", "Strategy"), "Large/Enterprise",
            "Large ops/implementation arm alongside strategy."),
    Company("Accenture (Health & Life Sciences)", "Consulting",
            ("Operations", "R&D"), "Large/Enterprise",
            "Heavy focus on digital/tech-enabled ops and R&D transformation."),
    Company("Oliver Wyman Health", "Consulting", ("Strategy", "Operations"), "Mid-size", ""),
    Company("L.E.K. Consulting (Life Sciences)", "Consulting", ("Strategy",), "Mid-size", ""),
    Company("ZS Associates", "Consulting", ("R&D", "Operations"), "Mid-size",
            "Pharma-commercial and R&D analytics specialist."),
    Company("IQVIA Consulting", "Consulting", ("R&D", "Operations"), "Large/Enterprise",
            "Also a major CRO/data company -- good ops+R&D crossover."),
    Company("Trinity Life Sciences", "Consulting", ("Strategy", "R&D"), "Mid-size", ""),
    Company("Putnam Associates", "Consulting", ("Strategy",), "Mid-size", ""),
    Company("Health Advances", "Consulting", ("Strategy",), "Mid-size", ""),
    Company("Charles River Associates (Life Sciences)", "Consulting", ("Strategy", "R&D"), "Mid-size", ""),
    Company("Avalere Health", "Consulting", ("Strategy", "Operations"), "Mid-size",
            "Policy/market access heavy."),
    Company("Genesis Research", "Consulting", ("R&D",), "Startup", "HEOR/RWE boutique."),

    # --- Healthcare Product / Health Tech ---
    Company("Included Health", "Product", ("Operations",), "Mid-size", ""),
    Company("Oscar Health", "Product", ("Operations", "R&D"), "Mid-size", ""),
    Company("Cityblock Health", "Product", ("Operations",), "Startup", ""),
    Company("Devoted Health", "Product", ("Operations",), "Mid-size", ""),
    Company("Hinge Health", "Product", ("Operations", "R&D"), "Mid-size", ""),
    Company("Cedar", "Product", ("Operations",), "Startup", "Patient billing/fintech-for-health."),
    Company("Commure", "Product", ("Operations", "R&D"), "Mid-size", ""),
    Company("Abridge", "Product", ("R&D",), "Startup", "Clinical AI/ambient documentation."),
    Company("Doximity", "Product", ("Operations",), "Mid-size", ""),
    Company("Flatiron Health", "Product", ("R&D",), "Mid-size", "Oncology RWE, part of Roche."),
    Company("Cohere Health", "Product", ("Operations",), "Startup", ""),
    Company("Verily", "Product", ("R&D", "Operations"), "Mid-size", "Alphabet life sciences arm."),
    Company("Tempus", "Product", ("R&D",), "Mid-size", "Precision medicine / genomic data."),
    Company("Ro", "Product", ("Operations",), "Mid-size", ""),
    Company("athenahealth", "Product", ("Operations",), "Large/Enterprise", ""),
    Company("Truveta", "Product", ("R&D",), "Startup", "Health data network."),

    # --- Big Pharma / Biotech ---
    Company("Pfizer", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Merck & Co.", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Johnson & Johnson (Innovative Medicine)", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Novartis", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Roche / Genentech", "Pharma", ("R&D",), "Large/Enterprise", ""),
    Company("AbbVie", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Amgen", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("GSK", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("AstraZeneca", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Sanofi", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Eli Lilly", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Bristol Myers Squibb", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Takeda", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Bayer (Pharmaceuticals)", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Moderna", "Pharma", ("R&D", "Operations"), "Mid-size", ""),
    Company("Regeneron", "Pharma", ("R&D",), "Mid-size", ""),
    Company("Vertex Pharmaceuticals", "Pharma", ("R&D",), "Mid-size", ""),
    Company("Novo Nordisk", "Pharma", ("R&D", "Operations"), "Large/Enterprise", ""),
    Company("Gilead Sciences", "Pharma", ("R&D",), "Mid-size", ""),
    Company("Biogen", "Pharma", ("R&D",), "Mid-size", ""),
)

SEGMENTS = ("Consulting", "Product", "Pharma")
FUNCTIONS = ("Operations", "R&D", "Strategy")
SIZES = ("Startup", "Mid-size", "Large/Enterprise")


def filter_companies(segment: str = None, function: str = None, size: str = None):
    results = COMPANIES
    if segment:
        results = tuple(c for c in results if c.segment.lower() == segment.lower())
    if function:
        results = tuple(c for c in results if function.lower() in (f.lower() for f in c.functions))
    if size:
        results = tuple(c for c in results if c.size.lower() == size.lower())
    return results

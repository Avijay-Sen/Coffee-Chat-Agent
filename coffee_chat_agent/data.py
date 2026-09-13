"""Curated target list of organizations across the healthcare value chain --
consulting, digital health/product, big pharma, biotech, medtech/devices,
payers, CROs, and healthcare-focused investing -- spanning startups to
giants.

This is a starting point, not a scraped or verified real-time list -- company
names, sizes, and focus areas change. Treat `notes` as a prompt for your own
quick research, not a substitute for it.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Company:
    name: str
    segment: str  # one of SEGMENTS
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
    Company("ZS Associates", "Consulting", ("R&D", "Operations", "Commercial"), "Mid-size",
            "Pharma-commercial and R&D analytics specialist."),
    Company("IQVIA Consulting", "Consulting", ("R&D", "Operations", "Commercial"), "Large/Enterprise",
            "Also a major CRO/data company -- good ops+R&D crossover."),
    Company("Trinity Life Sciences", "Consulting", ("Strategy", "R&D", "Commercial"), "Mid-size", ""),
    Company("Putnam Associates", "Consulting", ("Strategy", "Commercial"), "Mid-size", ""),
    Company("Health Advances", "Consulting", ("Strategy",), "Mid-size", ""),
    Company("Charles River Associates (Life Sciences)", "Consulting", ("Strategy", "R&D"), "Mid-size", ""),
    Company("Avalere Health", "Consulting", ("Strategy", "Operations"), "Mid-size",
            "Policy/market access heavy."),
    Company("Genesis Research", "Consulting", ("R&D",), "Startup", "HEOR/RWE boutique."),
    Company("Clearview Healthcare Partners", "Consulting", ("Strategy", "Commercial"), "Mid-size", ""),
    Company("Defined Health", "Consulting", ("Strategy",), "Startup", "Life sciences strategy boutique."),

    # --- Healthcare Product / Digital Health / Health Tech ---
    Company("Included Health", "Product", ("Operations",), "Mid-size", ""),
    Company("Oscar Health", "Product", ("Operations", "R&D"), "Mid-size", ""),
    Company("Cityblock Health", "Product", ("Operations",), "Startup", ""),
    Company("Devoted Health", "Product", ("Operations",), "Mid-size", ""),
    Company("Hinge Health", "Product", ("Operations", "R&D"), "Mid-size", ""),
    Company("Cedar", "Product", ("Operations",), "Startup", "Patient billing/fintech-for-health."),
    Company("Commure", "Product", ("Operations", "R&D"), "Mid-size", ""),
    Company("Abridge", "Product", ("R&D",), "Startup", "Clinical AI/ambient documentation."),
    Company("Doximity", "Product", ("Operations",), "Mid-size", ""),
    Company("Flatiron Health", "Product", ("R&D", "Data/Analytics"), "Mid-size", "Oncology RWE, part of Roche."),
    Company("Cohere Health", "Product", ("Operations",), "Startup", ""),
    Company("Verily", "Product", ("R&D", "Operations"), "Mid-size", "Alphabet life sciences arm."),
    Company("Tempus", "Product", ("R&D", "Data/Analytics"), "Mid-size", "Precision medicine / genomic data."),
    Company("Ro", "Product", ("Operations",), "Mid-size", ""),
    Company("athenahealth", "Product", ("Operations",), "Large/Enterprise", ""),
    Company("Truveta", "Product", ("R&D", "Data/Analytics"), "Startup", "Health data network."),
    Company("Epic Systems", "Product", ("Operations", "R&D"), "Large/Enterprise", "Dominant EHR vendor, privately held."),
    Company("Sword Health", "Product", ("Operations", "R&D"), "Startup", ""),
    Company("Suki AI", "Product", ("R&D",), "Startup", "Ambient clinical voice AI."),
    Company("Waymark", "Product", ("Operations",), "Startup", "Medicaid-focused care delivery."),

    # --- Big Pharma ---
    Company("Pfizer", "Pharma", ("R&D", "Operations", "Manufacturing", "Commercial"), "Large/Enterprise", ""),
    Company("Merck & Co.", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Johnson & Johnson (Innovative Medicine)", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Novartis", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Roche / Genentech", "Pharma", ("R&D", "Manufacturing"), "Large/Enterprise", ""),
    Company("AbbVie", "Pharma", ("R&D", "Operations", "Commercial"), "Large/Enterprise", ""),
    Company("Amgen", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("GSK", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("AstraZeneca", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Sanofi", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Eli Lilly", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Bristol Myers Squibb", "Pharma", ("R&D", "Operations", "Commercial"), "Large/Enterprise", ""),
    Company("Takeda", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Bayer (Pharmaceuticals)", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Novo Nordisk", "Pharma", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Gilead Sciences", "Pharma", ("R&D", "Commercial"), "Mid-size", ""),
    Company("Biogen", "Pharma", ("R&D", "Regulatory"), "Mid-size", ""),
    Company("Moderna", "Pharma", ("R&D", "Operations", "Manufacturing"), "Mid-size", ""),
    Company("Regeneron", "Pharma", ("R&D", "Manufacturing"), "Mid-size", ""),
    Company("Vertex Pharmaceuticals", "Pharma", ("R&D", "Clinical Development"), "Mid-size", ""),

    # --- Biotech (venture/earlier-stage & focused platforms) ---
    Company("Alnylam Pharmaceuticals", "Biotech", ("R&D", "Clinical Development"), "Mid-size", "RNAi therapeutics."),
    Company("BioNTech", "Biotech", ("R&D", "Manufacturing"), "Mid-size", ""),
    Company("Intellia Therapeutics", "Biotech", ("R&D", "Clinical Development"), "Startup", "CRISPR gene editing."),
    Company("Beam Therapeutics", "Biotech", ("R&D", "Clinical Development"), "Startup", "Base editing."),
    Company("Sarepta Therapeutics", "Biotech", ("R&D", "Regulatory"), "Mid-size", "Gene therapy, rare disease."),
    Company("Neurocrine Biosciences", "Biotech", ("R&D", "Commercial"), "Mid-size", ""),
    Company("Ionis Pharmaceuticals", "Biotech", ("R&D", "Clinical Development"), "Mid-size", ""),
    Company("Blueprint Medicines", "Biotech", ("R&D", "Commercial"), "Mid-size", ""),
    Company("Recursion Pharmaceuticals", "Biotech", ("R&D", "Data/Analytics"), "Startup", "AI-driven drug discovery."),
    Company("argenx", "Biotech", ("R&D", "Clinical Development"), "Mid-size", ""),
    Company("Arcus Biosciences", "Biotech", ("R&D", "Clinical Development"), "Startup", ""),
    Company("Insitro", "Biotech", ("R&D", "Data/Analytics"), "Startup", "Machine-learning drug discovery."),
    Company("Xaira Therapeutics", "Biotech", ("R&D",), "Startup", "AI drug design, well-funded startup."),

    # --- MedTech / Devices ---
    Company("Medtronic", "MedTech", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Stryker", "MedTech", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Boston Scientific", "MedTech", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Abbott (Medical Devices)", "MedTech", ("R&D", "Manufacturing"), "Large/Enterprise", ""),
    Company("Becton Dickinson (BD)", "MedTech", ("Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Edwards Lifesciences", "MedTech", ("R&D", "Clinical Development"), "Large/Enterprise", ""),
    Company("Intuitive Surgical", "MedTech", ("R&D", "Operations"), "Large/Enterprise", "Surgical robotics (da Vinci)."),
    Company("Dexcom", "MedTech", ("R&D", "Operations"), "Mid-size", "Continuous glucose monitoring."),
    Company("Insulet", "MedTech", ("R&D", "Manufacturing"), "Mid-size", ""),
    Company("GE HealthCare", "MedTech", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),
    Company("Siemens Healthineers", "MedTech", ("R&D", "Operations", "Manufacturing"), "Large/Enterprise", ""),

    # --- Payers / Health Insurance ---
    Company("UnitedHealth Group / Optum", "Payer", ("Operations", "Data/Analytics", "Strategy"), "Large/Enterprise", ""),
    Company("CVS Health / Aetna", "Payer", ("Operations", "Strategy"), "Large/Enterprise", ""),
    Company("Cigna", "Payer", ("Operations", "Strategy"), "Large/Enterprise", ""),
    Company("Elevance Health", "Payer", ("Operations", "Strategy"), "Large/Enterprise", "Formerly Anthem."),
    Company("Humana", "Payer", ("Operations", "Strategy"), "Large/Enterprise", ""),
    Company("Centene", "Payer", ("Operations",), "Large/Enterprise", "Medicaid-focused managed care."),
    Company("Molina Healthcare", "Payer", ("Operations",), "Mid-size", ""),

    # --- CRO / Clinical Research ---
    Company("ICON plc", "CRO", ("Clinical Development", "Operations"), "Large/Enterprise", ""),
    Company("Parexel", "CRO", ("Clinical Development", "Regulatory"), "Large/Enterprise", ""),
    Company("Fortrea (formerly Labcorp Drug Development)", "CRO", ("Clinical Development", "Operations"), "Large/Enterprise", ""),
    Company("Medpace", "CRO", ("Clinical Development", "Regulatory"), "Mid-size", ""),
    Company("Syneos Health", "CRO", ("Clinical Development", "Commercial"), "Large/Enterprise", ""),

    # --- Healthcare-focused Investing (VC / PE) ---
    Company("General Catalyst (Health)", "Investing", ("Strategy",), "Mid-size", ""),
    Company("a16z Bio + Health", "Investing", ("Strategy", "R&D"), "Mid-size", "Andreessen Horowitz life sciences arm."),
    Company("Flare Capital Partners", "Investing", ("Strategy",), "Startup", "Digital health-focused VC."),
    Company("Deerfield Management", "Investing", ("Strategy", "R&D"), "Mid-size", ""),
    Company("Bain Capital Life Sciences", "Investing", ("Strategy",), "Mid-size", ""),
    Company("Oak HC/FT", "Investing", ("Strategy",), "Mid-size", "Healthcare + fintech VC/growth."),
)

SEGMENTS = ("Consulting", "Product", "Pharma", "Biotech", "MedTech", "Payer", "CRO", "Investing")
FUNCTIONS = (
    "Operations", "R&D", "Strategy", "Commercial", "Regulatory",
    "Manufacturing", "Clinical Development", "Data/Analytics",
)
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

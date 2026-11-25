#!/usr/bin/env python3
"""Generate 4 structurally-identical, visually-distinct BAUVIZ workshop pages.
Shared real content; four different CSS/compositions."""

LOGO = "BAUVIZ-logo.svg"

# ----------------------------------------------------------------------------
# SHARED REAL CONTENT (from BAUVIZ 2027 CFP + summary)
# ----------------------------------------------------------------------------
NAV = [
    ("About", "#about"),
    ("Program", "#program"),
    ("Topics", "#topics"),
    ("Submit", "#submit"),
    ("Dates", "#dates"),
    ("Organization", "#org"),
    ("Contact", "#contact"),
]

ABOUT = (
    "BAUVIZ (Visualization in Architecture, Engineering &amp; Construction) brings together "
    "researchers and practitioners from visualization and the AEC disciplines to explore "
    "how visual analytics, immersive interfaces, and human-AI collaboration can support "
    "the digital transformation and circularity of the built environment. The workshop spans "
    "the full building lifecycle, from early design and simulation through construction, "
    "operation, and reuse, and extends to the scale of districts and urban systems. "
    "Within the EuroVis community, it provides a forum for sharing new techniques, "
    "identifying emerging challenges, and building interdisciplinary collaborations."
)

FORMAT = (
    "BAUVIZ is a half-day workshop. We plan for a format that fosters individual paper "
    "presentations as thought-provoking seeds, followed by an interactive discussion with all "
    "workshop participants."
)
AUDIENCE = [
    "Visualization &amp; Visual Analytics Researchers",
    "Computer Graphics &amp; HCI Researchers",
    "Architects &amp; Computational Designers",
    "AEC Practitioners",
    "Civil &amp; Structural Engineers",
    "Construction Engineers &amp; Managers",
    "BIM &amp; Digital Twin Experts",
    "Urban Informatics Researchers",
]

PROGRAM = [
    ("09:00 &ndash; 09:10", "Welcome &amp; introduction (Kuno Kurzhals)"),
    ("09:10 &ndash; 10:30", "Session 1 &mdash; paper presentations (short talks + questions)"),
    ("10:30 &ndash; 10:45", "Coffee break"),
    ("10:45 &ndash; 11:45", "Session 2 + interactive panel discussion"),
    ("11:45 &ndash; 12:00", "Closing &amp; next steps"),
]
PROGRAM_TBA = "TBA"  # schedule removed for now (2026-11-25, kuno); keep PROGRAM list above to restore later
PROGRAM_NOTE = ""

TOPICS = [
    ("Architecture &amp; Computational Design", [
        "Generative and computational design visualization",
        "Design space exploration",
        "Architectural performance visualization",
        "Explainable AI for design workflows",
        "AI copilots for architectural design",
        "Urban visualization and GIS",
    ]),
    ("Engineering &amp; Simulation", [
        "Engineering simulation visualization",
        "Uncertainty visualization",
        "Optimization and sensitivity analysis",
        "Comparative design evaluation",
        "Human-in-the-loop engineering workflows",
        "Life-cycle assessment &amp; embodied carbon",
    ]),
    ("Digital Fabrication &amp; Construction", [
        "Construction planning and monitoring",
        "Reality capture and point-cloud visualization",
        "Robotic fabrication and construction",
        "Circular construction",
        "Construction site safety &amp; workforce analytics",
        "Renovation and retrofitting workflows",
    ]),
    ("BIM &amp; Digital Twins", [
        "BIM visualization and interaction",
        "Semantic and interoperable data",
        "Digital twin analytics",
        "Sensor and IoT data",
        "Scalable rendering of large BIM models",
    ]),
    ("Human&ndash;Building Interaction &amp; Facility Mgmt.", [
        "Indoor environmental quality &amp; occupant comfort",
        "Building performance monitoring &amp; fault detection",
        "Energy consumption and smart-meter analytics",
        "Facility management and dashboards",
        "Structural health monitoring &amp; asset condition",
    ]),
    ("Immersive &amp; Collaborative Visualization", [
        "Virtual and augmented reality for AEC",
        "Immersive analytics for building and site data",
        "On-site AR guidance for construction &amp; maintenance",
        "Collaborative visualization environments",
        "Embodied interaction and collaboration",
        "Stakeholder communication and education",
    ]),
]

SUBMIT_TYPES = [
    ("Short research papers", "Original work in the EuroVis short paper format (up to 4 pages, two-column Eurographics style; abstract max. 150 words)."),
    ("Position / vision papers", "Foster discussion and envision future directions in built-environment visualization."),
    ("Industrial experience reports", "Lessons learned from deploying visualization in real AEC workflows."),
    ("Demonstrations", "Working systems, tools, or interactive artifacts."),
    ("Work-in-progress", "Early-stage results open to critique."),
]
SUBMIT_PROC = (
    "All contributions are handled through the Precision Conference System (PCS) via EuroVis 2027 "
    "under the BAUVIZ workshop track. Please read and follow the EuroVis 2027 and Eurographics author "
    "guidelines, as well as the Eurographics policy on the use of Generative AI tools. Submissions are "
    "peer-reviewed by at least two IPC members and one paper chair. Accepted short papers are published "
    "in the Eurographics Digital Library (archival) under a CC&nbsp;BY license; at least one author must "
    "register for and attend EuroVis 2027 in person."
)

# Dates not yet public (2026-11-25, kuno): to be announced around the beginning of
# March 2027. Keep this list to restore once announced:
DATES_ANNOUNCED = [
    ("Paper submission due", "Mar 05, 2027"),
    ("Notification", "Apr 16, 2027"),
    ("Camera-ready", "May 03, 2027"),
]
DATES = [
    ("Paper submission due", "TBA"),
    ("Notification", "TBA"),
    ("Camera-ready", "TBA"),
    ("EuroVis 2027", "May 31 &ndash; Jun 4, 2027, Stuttgart"),
]
DATES_TZ = "Workshop day: TBA &mdash; dates will be announced in early March 2027."

ORG = [
    ("Kuno Kurzhals", "University of Stuttgart, Germany"),
    ("Xiliu Yang", "University of Stuttgart / Max Planck Institute for Intelligent Systems, Germany"),
    ("Andrew Vande Moere", "Katholieke Universiteit Leuven, Belgium"),
]
STEERING = [
    ("Daniel Weiskopf", "University of Stuttgart, Germany"),
    ("Achim Menges", "University of Stuttgart, Germany"),
]
PC_NOTE = ("An international committee representing visualization, architecture, engineering, "
           "digital twins, HCI, and AI will be announced shortly.")
# Support section removed from pages for now (2026-11-25, kuno) - keep text to restore:
SUPPORT = (
    "The workshop is supported by the Cluster of Excellence &ldquo;Integrative Computational Design "
    "and Construction for Architecture&rdquo; (IntCDC) at the University of Stuttgart &mdash; one of the "
    "world&rsquo;s leading interdisciplinary initiatives in computational design and construction, "
    "bringing together architecture, engineering, robotics, computer science, and visualization."
)
CONTACT = "bauviz@visus.uni-stuttgart.de"
TITLE = "BAUVIZ 2027"
SUBTITLE = "Visualization in Architecture, Engineering &amp; Construction"
META = "Stuttgart, Germany &middot; TBA &middot; in conjunction with EuroVis 2027"
FOOT = "BAUVIZ 2027 &mdash; a EuroVis workshop. Built with the Eurographics community."

# ----------------------------------------------------------------------------
# tiny HTML helpers (content is identical across all four designs)
# ----------------------------------------------------------------------------
def nav_items():
    return "\n".join(f'<li><a href="{h}">{t}</a></li>' for t, h in NAV)

def topics_html():
    out = []
    for i, (head, items) in enumerate(TOPICS, 1):
        lis = "".join(f"<li>{it}</li>" for it in items)
        out.append(f'<div class="topic" data-i="{i}"><div class="topic-h">{head}</div>'
                   f'<ul>{lis}</ul></div>')
    return "\n".join(out)

def dates_html():
    return "\n".join(f'<div class="dt-row"><span class="dt-k">{k}</span><span class="dt-v">{v}</span></div>'
                     for k, v in DATES)

def org_html():
    return "\n".join(f'<div class="person"><div class="p-name">{n}</div><div class="p-aff">{a}</div></div>'
                     for n, a in ORG)

def steering_html():
    return "\n".join(f'<div class="person"><div class="p-name">{n}</div><div class="p-aff">{a}</div></div>'
                     for n, a in STEERING)

def submit_types_html():
    return "\n".join(f'<div class="stype"><div class="s-name">{n}</div><div class="s-desc">{d}</div></div>'
                     for n, d in SUBMIT_TYPES)

def audience_html():
    return "\n".join(f"<li>{a}</li>" for a in AUDIENCE)

def program_html():
    if PROGRAM_TBA:
        return f'<p class="tba">{PROGRAM_TBA}</p>'
    return "\n".join(f'<div class="pg-row"><span class="pg-t">{t}</span><span class="pg-d">{d}</span></div>'
                     for t, d in PROGRAM)

def page_wrap(css, body):
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{TITLE} &mdash; {SUBTITLE}</title>\n<style>{css}</style></head>\n'
        f'<body>{body}</body></html>'
    )

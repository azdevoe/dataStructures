from pathlib import Path
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

doc = docx.Document()

# Page Margins (0.5 in for tight, clean 1-page fit)
for section in doc.sections:
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.55)
    section.right_margin = Inches(0.55)

# Color constants
PRIMARY_COLOR = RGBColor(17, 24, 39)  # Deep slate / near black
MUTED_COLOR = RGBColor(75, 85, 99)  # Subtle charcoal gray
ACCENT_COLOR = RGBColor(30, 41, 59)  # Header accent
LINK_COLOR = RGBColor(37, 99, 235)  # Professional blue


def add_hyperlink(paragraph, text, url):
    """Inserts a real, clickable hyperlink into a python-docx paragraph."""
    part = paragraph.part
    r_id = part.relate_to(
        url,
        docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK,
        is_external=True
    )

    # Added "r" namespace declaration alongside "w"
    hyperlink = parse_xml(f'<w:hyperlink {nsdecls("w", "r")} r:id="{r_id}"/>')
    new_run = parse_xml(f'<w:r {nsdecls("w")}/>')
    rPr = parse_xml(
        f'<w:rPr {nsdecls("w")}>\n'
        f'  <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>\n'
        f'  <w:color w:val="2563EB"/>\n'
        f'  <w:u w:val="single"/>\n'
        f'  <w:sz w:val="19"/>\n'
        f'</w:rPr>'
    )
    new_run.append(rPr)
    text_elem = parse_xml(f'<w:t {nsdecls("w")} xml:space="preserve">{text}</w:t>')
    new_run.append(text_elem)
    hyperlink.append(new_run)
    paragraph._element.append(hyperlink)


def add_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True

    run = p.add_run(text.upper())
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = ACCENT_COLOR

    pPr = p._element.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="2" w:color="D1D5DB"/>\n'
        f"</w:pBdr>"
    )
    pPr.append(pBdr)


def add_bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.color.rgb = PRIMARY_COLOR


# ----------------- HEADER -----------------
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(1)
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

name_run = title_p.add_run("Aro Abdulazeez Goodluck")
name_run.font.name = "Calibri"
name_run.font.size = Pt(19)
name_run.font.bold = True
name_run.font.color.rgb = PRIMARY_COLOR

contact_p = doc.add_paragraph()
contact_p.paragraph_format.space_before = Pt(0)
contact_p.paragraph_format.space_after = Pt(4)
contact_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add phone
r = contact_p.add_run("+234 906 382 6057  |  ")
r.font.name, r.font.size, r.font.color.rgb = "Calibri", Pt(9.5), MUTED_COLOR

# Add LinkedIn Link
add_hyperlink(contact_p, "LinkedIn", "https://linkedin.com/in/aro-abdulazeez")

r = contact_p.add_run("  |  aroabdulazeez@gmail.com  |  ")
r.font.name, r.font.size, r.font.color.rgb = "Calibri", Pt(9.5), MUTED_COLOR

# Add GitHub Link
add_hyperlink(contact_p, "GitHub", "https://github.com/GoodluckAro")

r = contact_p.add_run("  |  Lagos, Nigeria")
r.font.name, r.font.size, r.font.color.rgb = "Calibri", Pt(9.5), MUTED_COLOR

# ----------------- EDUCATION -----------------
add_heading(doc, "Education")

p_edu1 = doc.add_paragraph()
p_edu1.paragraph_format.space_before = Pt(2)
p_edu1.paragraph_format.space_after = Pt(0)
r = p_edu1.add_run("University of Lagos")
r.bold = True
r.font.name, r.font.size = "Calibri", Pt(10)
r = p_edu1.add_run(" — Lagos, Nigeria")
r.font.name, r.font.size = "Calibri", Pt(10)

p_edu2 = doc.add_paragraph()
p_edu2.paragraph_format.space_before = Pt(0)
p_edu2.paragraph_format.space_after = Pt(1)
r = p_edu2.add_run("Bachelor of Science in Computer Science")
r.italic = True
r.font.name, r.font.size = "Calibri", Pt(9.5)
r = p_edu2.add_run(" | Expected 2028")
r.font.name, r.font.size = "Calibri", Pt(9.5)

p_edu3 = doc.add_paragraph()
p_edu3.paragraph_format.space_before = Pt(0)
p_edu3.paragraph_format.space_after = Pt(2)
r = p_edu3.add_run("Relevant Coursework: ")
r.bold = True
r.font.name, r.font.size = "Calibri", Pt(9.5)
r = p_edu3.add_run(
    "Data Structures & Algorithms, Operating Systems, Concurrent Programming,"
    " Formal Methods, Automata Theory"
)
r.font.name, r.font.size = "Calibri", Pt(9.5)

# ----------------- EXPERIENCE & LEADERSHIP -----------------
add_heading(doc, "Experience & Leadership")

# Role 1
p_l1 = doc.add_paragraph()
p_l1.paragraph_format.space_before = Pt(2)
p_l1.paragraph_format.space_after = Pt(0)
r = p_l1.add_run("Department of Computer Science Upskilling")
r.bold = True
r.font.name, r.font.size = "Calibri", Pt(10)
r = p_l1.add_run(" — Lagos, Nigeria")
r.font.name, r.font.size = "Calibri", Pt(10)

p_l2 = doc.add_paragraph()
p_l2.paragraph_format.space_before = Pt(0)
p_l2.paragraph_format.space_after = Pt(1)
r = p_l2.add_run("Student Lead / DSA Facilitator")
r.italic = True
r.font.name, r.font.size = "Calibri", Pt(9.5)
r = p_l2.add_run(" | 2025 – Present")
r.font.name, r.font.size = "Calibri", Pt(9.5)

add_bullet(
    doc,
    "Facilitated hands-on Data Structures & Algorithms tutorials for an"
    " undergraduate cohort, breaking down memory layout, pointer mechanics,"
    " and asymptotic complexity analysis.",
)
add_bullet(
    doc,
    "Designed interactive physical-simulation walkthroughs for linear data"
    " structures (linked lists, queues, stacks), boosting cohort retention of"
    " pointer traversal concepts.",
)
add_bullet(
    doc,
    "Mentored peers across 100+ algorithmic patterns, including two-pointer,"
    " sliding window, graph traversals, and dynamic programming to prepare"
    " candidates for technical assessments.",
)

# Role 2
p_f1 = doc.add_paragraph()
p_f1.paragraph_format.space_before = Pt(2.5)
p_f1.paragraph_format.space_after = Pt(0)
r = p_f1.add_run("Freelance Backend Developer")
r.bold = True
r.font.name, r.font.size = "Calibri", Pt(10)
r = p_f1.add_run(" — Remote")
r.font.name, r.font.size = "Calibri", Pt(10)

p_f2 = doc.add_paragraph()
p_f2.paragraph_format.space_before = Pt(0)
p_f2.paragraph_format.space_after = Pt(1)
r = p_f2.add_run("Software Engineer")
r.italic = True
r.font.name, r.font.size = "Calibri", Pt(9.5)
r = p_f2.add_run(" | 2025")
r.font.name, r.font.size = "Calibri", Pt(9.5)

add_bullet(
    doc,
    "Engineered a secure backend communication pipeline for a client web"
    " platform, handling contact routing, payload sanitization, and automated"
    " transactional email delivery via SMTP.",
)
add_bullet(
    doc,
    "Designed centralized error-handling middleware and schema validation,"
    " achieving resilient API endpoints and zero unhandled request exceptions.",
)
add_bullet(
    doc,
    "Collaborated with client stakeholders to optimize frontend integration"
    " contracts and streamline asset delivery.",
)

# ----------------- PROJECTS -----------------
add_heading(doc, "Projects")

# Project 1
p_p1 = doc.add_paragraph()
p_p1.paragraph_format.space_before = Pt(2.5)
p_p1.paragraph_format.space_after = Pt(1)
r = p_p1.add_run("realFin")
r.bold = True
r.font.name, r.font.size = "Calibri", Pt(10)
r = p_p1.add_run(
    " | TypeScript, Node.js, Express, PostgreSQL, Sequelize, Docker, Jest"
)
r.italic = True
r.font.name, r.font.size = "Calibri", Pt(9.5)
r = p_p1.add_run(" | 2026 – Present")
r.font.name, r.font.size = "Calibri", Pt(9.5)

add_bullet(
    doc,
    "Architected a modular REST API adhering to layered domain design (Routes"
    " → Zod Validation → Controllers → Services) with centralized error"
    " handling and atomic database transactions.",
)
add_bullet(
    doc,
    "Implemented stateless JWT authentication and role-based access control"
    " (RBAC) middleware with custom error hierarchies (401 Unauthorized / 403"
    " Forbidden), backed by 30+ passing automated tests.",
)
add_bullet(
    doc,
    "Designed a normalized relational PostgreSQL schema featuring UUID primary"
    " keys, composite unique indexes, and ENUM state management via versioned"
    " Sequelize migrations.",
)
add_bullet(
    doc,
    "Containerized local development environments using Docker and Docker"
    " Compose, enforcing strict Test-Driven Development (TDD) with"
    " Jest/Supertest integration test suites.",
)

# Project 2
p_p2 = doc.add_paragraph()
p_p2.paragraph_format.space_before = Pt(2.5)
p_p2.paragraph_format.space_after = Pt(1)
r = p_p2.add_run("CalcEngine")
r.bold = True
r.font.name, r.font.size = "Calibri", Pt(10)
r = p_p2.add_run(" | C#, ANTLR, xUnit, BenchmarkDotNet")
r.italic = True
r.font.name, r.font.size = "Calibri", Pt(9.5)
r = p_p2.add_run(" | 2026")
r.font.name, r.font.size = "Calibri", Pt(9.5)

add_bullet(
    doc,
    "Architected the core calculation engine for an extensible spreadsheet"
    " system, building an ANTLR-based formula grammar and AST visitor"
    " evaluation pipeline.",
)
add_bullet(
    doc,
    "Implemented a reactive dependency graph with topological cycle detection"
    " to resolve cell-reference DAGs and eliminate recursive calculation"
    " stalls.",
)
add_bullet(
    doc,
    "Applied Observer, Command (undo/redo), and Strategy patterns across the"
    " recalculation engine, maintaining strict Test-Driven Development with"
    " 375 passing automated tests.",
)
add_bullet(
    doc,
    "Collaborated with team members to integrate interactive UI controls and"
    " conduct performance benchmarking under high computational workloads.",
)

# ----------------- TECHNICAL SKILLS -----------------
add_heading(doc, "Technical Skills")

skills = [
    (
        "Languages: ",
        "Python, TypeScript, JavaScript, C#, SQL (PostgreSQL), C/C++",
    ),
    (
        "Frameworks & Libraries: ",
        "Node.js, Express, Sequelize, Jest, Supertest, Zod, ANTLR, xUnit",
    ),
    (
        "Developer Tools: ",
        "Git, Docker, Docker Compose, Postman, Linux/Bash, VS Code",
    ),
    (
        "Core Competencies: ",
        "Test-Driven Development (TDD), RESTful API Design, Relational Database"
        " Modeling, Role-Based Access Control (RBAC), Data Structures &"
        " Algorithms, Design Patterns, Concurrent Systems",
    ),
]

for label, values in skills:
  sp = doc.add_paragraph()
  sp.paragraph_format.space_before = Pt(0)
  sp.paragraph_format.space_after = Pt(1)
  sp.paragraph_format.line_spacing = 1.05

  r1 = sp.add_run(label)
  r1.bold = True
  r1.font.name, r1.font.size = "Calibri", Pt(9.5)

  r2 = sp.add_run(values)
  r2.font.name, r2.font.size = "Calibri", Pt(9.5)

# Save directly to current workspace
output_path = Path("Aro_Abdulazeez_Resume.docx")
doc.save(str(output_path))
print(f"File saved successfully to {output_path.resolve()}")
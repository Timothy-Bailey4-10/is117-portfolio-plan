"""Build Timothy Bailey's one-page résumé PDF.

Public version (no phone, safe to publish on the portfolio):
    python build_resume.py Timothy-Bailey-Resume.pdf
Application version (adds phone; keep it out of git):
    python build_resume.py private/Timothy-Bailey-Resume-apply.pdf --phone "XXX-XXX-XXXX"

Needs: pip install reportlab
"""
import argparse

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (HRFlowable, ListFlowable, ListItem, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

INK = HexColor("#1b1b1f")
W = 7.5 * inch - 12  # frame width minus default 6pt padding each side
ACCENT = HexColor("#4a2bd1")  # darker brand violet, high contrast for print
LINK = "#4a2bd1"

EMAIL = "tsb32@njit.edu"
PORTFOLIO = "https://timothy-bailey4-10.github.io/is117-portfolio-plan/"
GITHUB = "https://github.com/Timothy-Bailey4-10"
LINKEDIN = "https://www.linkedin.com/in/timothy-bailey-20250a281/"

name_s = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, leading=26,
                        alignment=TA_CENTER, textColor=INK)
contact_s = ParagraphStyle("contact", fontName="Helvetica", fontSize=9.8, leading=13,
                           alignment=TA_CENTER, textColor=INK)
head_s = ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=11.5, leading=14,
                        textColor=ACCENT, spaceBefore=8, spaceAfter=1)
left_s = ParagraphStyle("left", fontName="Helvetica", fontSize=10.2, leading=12.8, textColor=INK)
right_s = ParagraphStyle("right", parent=left_s, alignment=2)
bullet_s = ParagraphStyle("bullet", parent=left_s, fontSize=10, leading=12.6)


def a(url, text=None):
    return f'<link href="{url}" color="{LINK}"><u>{text or url.replace("https://", "")}</u></link>'


def row(left, right=""):
    t = Table([[Paragraph(left, left_s), Paragraph(right, right_s)]],
              colWidths=[W - 2.0 * inch, 2.0 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t


def bullets(items):
    return ListFlowable([ListItem(Paragraph(i, bullet_s), leftIndent=11, value="•")
                         for i in items], bulletType="bullet", start="•",
                        leftIndent=11, bulletFontSize=8, spaceBefore=0.5)


def section(title):
    return [Paragraph(title.upper(), head_s),
            HRFlowable(width="100%", thickness=0.7, color=ACCENT, spaceAfter=2)]


def build(out, phone=None):
    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=0.5 * inch, rightMargin=0.5 * inch,
                            topMargin=0.45 * inch, bottomMargin=0.4 * inch,
                            title="Timothy Bailey — Résumé", author="Timothy Bailey",
                            subject="Résumé: NJIT Business & Information Systems student")
    contact = [p for p in [phone, a(f"mailto:{EMAIL}", EMAIL), f"LinkedIn: {a(LINKEDIN)}"] if p]
    s = [Paragraph("Timothy Bailey", name_s),
         Paragraph(" | ".join(contact), contact_s),
         Paragraph(f"Portfolio: {a(PORTFOLIO)} | GitHub: {a(GITHUB)}", contact_s),
         Spacer(1, 2)]

    s += section("Education")
    s += [row("<b>New Jersey Institute of Technology</b> | Newark, NJ", "Expected May 2028"),
          row("<i>Bachelor of Science in Business &amp; Information Systems</i>"),
          row("<b>Burlington County Institute of Technology</b> | Westampton, NJ — "
              "Diploma and Certificate in Information Technology", "Sept. 2019 – June 2023")]

    s += section("Projects")
    s += [row(f"<b>Jersey Givers T-shirt Storefront</b> | Course project, IS117 | "
              f"HTML, CSS, JavaScript | {a('https://timothy-bailey4-10.github.io/is117-t-shirt-assignment/', 'Live&nbsp;site')}",
              "Fall 2026"),
          bullets(["Built a branded storefront and live style guide for New Jersey student volunteers: "
                   "original SVG logo, shared color and type tokens, size selector and demo bag.",
                   "Checked it with automated tests (7 server tests, 10 browser tests including "
                   "accessibility scans on 3 pages) plus keyboard and phone-width review."]),
          row(f"<b>AI Career Research Site</b> | Course project, IS117 | VitePress, GitHub Actions | "
              f"{a('https://timothy-bailey4-10.github.io/is117-ai-career-research/', 'Live&nbsp;site')}",
              "Nov. 2026"),
          bullets(["Researched the Forward Deployed Engineer role and related AI jobs; published a "
                   "6-section guide that deploys automatically to GitHub Pages.",
                   "Linked every figure on the main role pages to the exact source sentence it came from."]),
          row(f"<b>Solo Software Research</b> | Group course project, IS117 (2 members) | HTML, CSS | "
              f"{a('https://github.com/Timothy-Bailey4-10/is-117-business-research', 'Repository')}",
              "Nov. 2026 – Present"),
          bullets(["Built the team's 11-page research site; selected and documented competitors "
                   "(Starter Story, MicroConf) and opened the team's first peer-review issue. "
                   "<i>In progress.</i>"]),
          row("<b>Python Projects</b> | Quiz Game; Compound Interest Calculator",
              "June 2024 – Aug. 2026"),
          bullets(["Wrote a trivia quiz program and a calculator script that prompts for principal, "
                   "rate and time."]),
          row("<b>Early Web Projects</b> | HTML, CSS | Music review, cybersecurity info and "
              "portfolio websites", "Jan. 2023 – May 2023")]

    s += section("Leadership &amp; Involvement")
    s += [row("<b>Student Senate, First-Year Representative</b> | NJIT", "Sept. 2024 – May 2025"),
          bullets(["Earned the “Most Ambitious Senator” award, voted on by fellow senators; "
                   "served on 3 student-interest committees and oversaw 6 first-year "
                   "representatives, taking notes at every first-year meeting."]),
          row("<b>Association for Computing Machinery (ACM), Member</b> | NJIT — special interest "
              "groups in full-stack development and AI tools", "Sept. 2024 – Present"),
          row("<b>Bank of America Global Technology Early Insights Forum</b> | Selected participant",
              "Jan. 2025"),
          row("<b>NJIT Esports, Super Smash Bros. Ultimate Team</b> | Competes against other "
              "colleges and at local tournaments", "Jan. 2025 – Present"),
          row("<b>Abundant Life Fellowship Church</b> | NJ — Social Media Manager (posted and "
              "monetized long-form YouTube videos); food bank volunteer (50+ hours); usher (50+ hours)",
              "2019 – Present"),
          row("<b>Private Tutor, Precalculus</b> | Burlington County Institute of Technology",
              "Sept. 2022 – May 2023")]

    s += section("Skills")
    s += [Paragraph("<b>Languages:</b> HTML, CSS, JavaScript, Python  |  <b>Tools:</b> Git, GitHub, "
              "GitHub Pages and Actions, VitePress, VS Code  |  <b>Practices:</b> directing and "
              "verifying AI coding assistants, peer review through GitHub issues, browser and "
              "accessibility checks", left_s)]
    doc.build(s)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("out")
    p.add_argument("--phone")
    args = p.parse_args()
    build(args.out, args.phone)

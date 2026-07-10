from __future__ import annotations

from pathlib import Path
import subprocess

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs" / "sales-marketing" / "generated" / "leaflets"
LOGO = ROOT / "docs" / "brand" / "logos" / "final" / "bright-roof-final-logo-dark-transparent.png"

PDF = OUT / "bright-roof-bulk-apartment-leaflet-a5.pdf"
PNG_PREFIX = OUT / "bright-roof-bulk-apartment-leaflet-a5"
PNG = OUT / "bright-roof-bulk-apartment-leaflet-a5.png"
JPG = OUT / "bright-roof-bulk-apartment-leaflet-a5.jpg"

NAVY = HexColor("#0E1E4D")
AMBER = HexColor("#F5A524")
TERRACOTTA = HexColor("#C75B3C")
CREAM = HexColor("#FAF6EE")
SLATE = HexColor("#2C3444")
MUTED = HexColor("#6B7280")
LIGHT = HexColor("#E8EBEF")
WHITE = HexColor("#FFFFFF")


def wrap_text(c: canvas.Canvas, text: str, max_width: float, font: str, size: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if c.stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    max_width: float,
    font: str,
    size: float,
    leading: float,
    color,
) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_text(c, text, max_width, font, size):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_panel_icon(c: canvas.Canvas, x: float, y: float) -> None:
    c.saveState()
    c.setFillColor(AMBER)
    c.circle(x + 22 * mm, y + 22 * mm, 13 * mm, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    # apartment block
    c.roundRect(x + 4 * mm, y, 40 * mm, 28 * mm, 2 * mm, stroke=0, fill=1)
    c.setFillColor(CREAM)
    for col in range(4):
        for row in range(3):
            c.roundRect(x + (9 + col * 7) * mm, y + (6 + row * 6) * mm, 3.4 * mm, 2.8 * mm, 0.6 * mm, stroke=0, fill=1)
    # roof solar panel
    c.setFillColor(TERRACOTTA)
    points = [
        x + 2 * mm,
        y + 28 * mm,
        x + 46 * mm,
        y + 28 * mm,
        x + 39 * mm,
        y + 38 * mm,
        x + 9 * mm,
        y + 38 * mm,
    ]
    c.setStrokeColor(CREAM)
    c.setLineWidth(0.7)
    c.setFillColor(TERRACOTTA)
    c.line(points[0], points[1], points[2], points[3])
    c.line(points[2], points[3], points[4], points[5])
    c.line(points[4], points[5], points[6], points[7])
    c.line(points[6], points[7], points[0], points[1])
    c.setFillColor(TERRACOTTA)
    p = c.beginPath()
    p.moveTo(points[0], points[1])
    p.lineTo(points[2], points[3])
    p.lineTo(points[4], points[5])
    p.lineTo(points[6], points[7])
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.setStrokeColor(CREAM)
    for i in range(1, 4):
        xx = x + (2 + i * 11) * mm
        c.line(xx, y + 28.2 * mm, xx + 5 * mm, y + 37.6 * mm)
    c.line(x + 6 * mm, y + 33 * mm, x + 42 * mm, y + 33 * mm)
    c.restoreState()


def generate() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    w, h = A5
    c = canvas.Canvas(str(PDF), pagesize=A5)
    c.setTitle("Bright Roof Bulk Apartment Leaflet A5")

    # Background and edge bands
    c.setFillColor(CREAM)
    c.rect(0, 0, w, h, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.rect(0, h - 31 * mm, w, 31 * mm, stroke=0, fill=1)
    c.setFillColor(AMBER)
    c.rect(0, h - 33 * mm, w, 2.2 * mm, stroke=0, fill=1)

    margin = 13 * mm
    top = h - 10 * mm

    if LOGO.exists():
        c.drawImage(str(LOGO), margin, h - 26 * mm, width=31 * mm, height=16 * mm, mask="auto", preserveAspectRatio=True)

    c.setFillColor(CREAM)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawRightString(w - margin, h - 17 * mm, "BRIGHT ROOF POWER SYSTEMS")
    c.setFont("Helvetica", 8.3)
    c.drawRightString(w - margin, h - 22 * mm, "Solar that stays.")

    # Hero
    y = h - 46 * mm
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 23)
    c.drawString(margin, y, "Is your apartment's")
    y -= 8.8 * mm
    c.drawString(margin, y, "electricity bill too high?")
    c.setFillColor(AMBER)
    c.rect(margin, y - 5.5 * mm, 30 * mm, 1.4 * mm, stroke=0, fill=1)

    draw_panel_icon(c, w - 57 * mm, h - 94 * mm)

    y -= 16 * mm
    y = draw_wrapped(
        c,
        "Rooftop solar with no upfront installation cost to the society.",
        margin,
        y,
        92 * mm,
        "Helvetica-Bold",
        13.8,
        6.2 * mm,
        TERRACOTTA,
    )
    y -= 3 * mm
    y = draw_wrapped(
        c,
        "Bright Roof installs, owns, operates, and maintains rooftop solar systems for apartment societies in Hyderabad.",
        margin,
        y,
        76 * mm,
        "Helvetica",
        9.4,
        4.3 * mm,
        SLATE,
    )
    y -= 2.2 * mm
    y = draw_wrapped(
        c,
        "Your society pays only for solar electricity under the agreement, with a starting proposal of 10% saving against the agreed electricity-tariff benchmark.",
        margin,
        y,
        76 * mm,
        "Helvetica",
        9.4,
        4.3 * mm,
        SLATE,
    )

    # Fit box
    box_y = 59 * mm
    c.setFillColor(WHITE)
    c.roundRect(margin, box_y, w - 2 * margin, 34 * mm, 3 * mm, stroke=0, fill=1)
    c.setStrokeColor(LIGHT)
    c.setLineWidth(0.7)
    c.roundRect(margin, box_y, w - 2 * margin, 34 * mm, 3 * mm, stroke=1, fill=0)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 10.4)
    c.drawString(margin + 6 * mm, box_y + 25 * mm, "Good fit for apartments with")
    c.setFont("Helvetica", 8.7)
    c.setFillColor(SLATE)
    bullets = ["Lifts", "Water pumps", "Common lighting", "Clubhouse", "STP", "Security loads"]
    positions = [(0, 0), (39, 0), (78, 0), (0, -9), (39, -9), (78, -9)]
    for text, (dx, dy) in zip(bullets, positions):
        c.setFillColor(AMBER)
        c.circle(margin + (7 + dx) * mm, box_y + (17 + dy) * mm, 1.2 * mm, fill=1, stroke=0)
        c.setFillColor(SLATE)
        c.drawString(margin + (10 + dx) * mm, box_y + (15.8 + dy) * mm, text)

    # First step
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin, 47 * mm, "Simple first step")
    draw_wrapped(
        c,
        "Share 12 months of common-area electricity bills and allow a rooftop/electrical-room survey. Bright Roof will check whether solar makes sense for your society.",
        margin,
        41 * mm,
        w - 2 * margin,
        "Helvetica",
        8.9,
        4.1 * mm,
        SLATE,
    )

    # CTA band
    c.setFillColor(NAVY)
    c.roundRect(margin, 13 * mm, w - 2 * margin, 22 * mm, 3 * mm, stroke=0, fill=1)
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 10.8)
    c.drawString(margin + 6 * mm, 26 * mm, "Call / WhatsApp: +91 93902 10407")
    c.setFillColor(CREAM)
    c.setFont("Helvetica", 8.9)
    c.drawString(margin + 6 * mm, 20.3 * mm, "support@brightroofpower.com  |  www.brightroofpower.com")

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 5.8)
    c.drawCentredString(w / 2, 6.5 * mm, "Commercial overview only. Final terms are governed by the signed Power Purchase Agreement.")
    c.showPage()
    c.save()

    subprocess.run(["/opt/homebrew/bin/pdftoppm", "-singlefile", "-r", "300", "-png", str(PDF), str(PNG_PREFIX)], check=True)
    generated = OUT / f"{PNG_PREFIX.name}.png"
    if generated.exists() and generated != PNG:
        generated.rename(PNG)
    img = Image.open(PNG).convert("RGB")
    img.save(JPG, quality=95, dpi=(300, 300))
    print(PDF)
    print(PNG)
    print(JPG)


if __name__ == "__main__":
    generate()

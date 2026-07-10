import pathlib
from textwrap import wrap

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


REPO = pathlib.Path(__file__).resolve().parents[3]
REPORT_ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = REPORT_ROOT / "assets"
OUT = REPO / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
MARGIN = 42
INK = colors.HexColor("#191714")
MUTED = colors.HexColor("#6b645b")
LINE = colors.HexColor("#d8d0c3")
PANEL = colors.HexColor("#fffdf8")
PANEL_2 = colors.HexColor("#f0ebe1")
GREEN = colors.HexColor("#2c6651")
AMBER = colors.HexColor("#a95d1c")


AREAS = {
    "nacharam-east": {
        "title": "Nacharam East - <10 Floor Solar Prospects",
        "subtitle": "Low-rise apartment prospects with no obvious rooftop PV arrays in the satellite scan.",
        "file": OUT / "nacharam-east-less-than-10-floors-solar-prospects.pdf",
        "route": "Concrete Opus -> Sri Tirumala Millennium Phase 2 -> Shanti Gardens Block E -> Navya Global -> NS Platinum",
        "prospects": [
            {
                "name": "Concrete Opus Apartments",
                "image": "nacharam-east-concrete-opus.png",
                "coords": "17.4301484, 78.5538058",
                "floors": "~5-7 floors",
                "units": "~100-160 units, visual estimate",
                "confidence": "Medium",
                "note": "Main blocks appear low/mid-rise with open concrete roof areas. No obvious PV grid on the target roof; verify boundary because nearby roofs show panel-like structures.",
                "maps": "https://www.google.com/maps?q=17.4301484,78.5538058",
            },
            {
                "name": "Sri Tirumala Millennium Phase 2",
                "image": "nacharam-east-sri-tirumala-millennium-phase-2.png",
                "coords": "17.4370167, 78.5699369",
                "floors": "~5-7 floors",
                "units": "Large phase, unit count needs confirmation",
                "confidence": "Medium",
                "note": "Large low-rise campus. Rooftop water tanks are visible, but no obvious PV panel grid was seen in the crop.",
                "maps": "https://www.google.com/maps?q=17.4370167,78.5699369",
            },
            {
                "name": "Shanti Gardens Block E",
                "image": "nacharam-east-shanti-gardens-block-e.png",
                "coords": "17.4251239, 78.5519081",
                "floors": "~5-6 floors",
                "units": "~80-150 units, visual estimate",
                "confidence": "Medium",
                "note": "Low-rise blocks with simple roof surfaces and no clear PV arrays in the target mosaic.",
                "maps": "https://www.google.com/maps?q=17.4251239,78.5519081",
            },
            {
                "name": "Navya Global Apartments",
                "image": "nacharam-east-navya-global-apartments.png",
                "coords": "17.4283708, 78.5542484",
                "floors": "~5-7 floors",
                "units": "~40-80 units, visual estimate",
                "confidence": "Low-medium",
                "note": "Smaller low-rise target. Use as a nearby add-on rather than first meeting unless contact details are easy to obtain.",
                "maps": "https://www.google.com/maps?q=17.4283708,78.5542484",
            },
            {
                "name": "NS Platinum Apartments",
                "image": "nacharam-east-ns-platinum.png",
                "coords": "17.4283602, 78.5537998",
                "floors": "~5-7 floors",
                "units": "~60-100 units, visual estimate",
                "confidence": "Low-medium",
                "note": "Target roof looks low-rise and mostly open, but adjacent roofs show panel-like grids. Confirm exact society boundary before outreach.",
                "maps": "https://www.google.com/maps?q=17.4283602,78.5537998",
            },
        ],
    },
    "mallapur": {
        "title": "Mallapur - <10 Floor Solar Prospects",
        "subtitle": "Low-rise apartment prospects with no obvious rooftop PV arrays in the satellite scan.",
        "file": OUT / "mallapur-less-than-10-floors-solar-prospects.pdf",
        "route": "Gulmohar Gardens -> Sri Tirumala Millennium -> Mayflower Platinum -> Mayflower Park -> Gulmohar Residency",
        "prospects": [
            {
                "name": "Gulmohar Gardens",
                "image": "mallapur-gulmohar-gardens.png",
                "coords": "17.4443797, 78.5805605",
                "floors": "~5-7 floors",
                "units": "Large multi-block society, unit count needs verification",
                "confidence": "Medium",
                "note": "One of the strongest Mallapur prospects: repeated low-rise blocks, broad roof surfaces, and no obvious rooftop PV field.",
                "maps": "https://www.google.com/maps?q=17.4443797,78.5805605",
            },
            {
                "name": "Sri Tirumala Millennium",
                "image": "mallapur-sri-tirumala-millennium.png",
                "coords": "17.4370167, 78.5699369",
                "floors": "~5-7 floors",
                "units": "Large multi-phase society, unit count needs phase confirmation",
                "confidence": "Medium",
                "note": "Low-rise blocks and no obvious PV panels in the current rooftop crop. Verify phase boundaries before proposal sizing.",
                "maps": "https://www.google.com/maps?q=17.4370167,78.5699369",
            },
            {
                "name": "Mayflower Platinum",
                "image": "mallapur-mayflower-platinum.png",
                "coords": "17.4469699, 78.5740716",
                "floors": "~6-8 floors",
                "units": "Medium-large society, visual estimate",
                "confidence": "Medium",
                "note": "Long low/mid-rise apartment block with open roof strips. No clear PV-grid signature visible in the scan.",
                "maps": "https://www.google.com/maps?q=17.4469699,78.5740716",
            },
            {
                "name": "Mayflower Park Apartments",
                "image": "mallapur-mayflower-park.png",
                "coords": "17.4432638, 78.5686462",
                "floors": "~5-7 floors",
                "units": "Multi-block society, visual estimate",
                "confidence": "Medium",
                "note": "Good low-rise target with multiple apartment blocks and mostly open rooftops in the inspected frame.",
                "maps": "https://www.google.com/maps?q=17.4432638,78.5686462",
            },
            {
                "name": "Gulmohar Residency",
                "image": "mallapur-gulmohar-residency.png",
                "coords": "17.4507720, 78.5727710",
                "floors": "~5-7 floors",
                "units": "Medium-large cluster, visual estimate",
                "confidence": "Medium",
                "note": "Large low-rise pattern with repeated roofs and no obvious PV panel grid. Good Mallapur field target.",
                "maps": "https://www.google.com/maps?q=17.450772,78.572771",
            },
            {
                "name": "Janapriya Township",
                "image": "mallapur-janapriya-township.png",
                "coords": "17.4417770, 78.5683431",
                "floors": "~5-7 floors",
                "units": "Large older township, unit count needs confirmation",
                "confidence": "Low-medium",
                "note": "Potentially useful because of low-rise format and multiple blocks, but tree cover and campus boundaries require a manual route pass.",
                "maps": "https://www.google.com/maps?q=17.441777,78.5683431",
            },
            {
                "name": "Aditya Pearl Apartment",
                "image": "mallapur-aditya-pearl.png",
                "coords": "17.4410599, 78.5756127",
                "floors": "~5-7 floors",
                "units": "~40-80 units, visual estimate",
                "confidence": "Low-medium",
                "note": "Looks technically feasible but lower volume. Add to route only if nearby contacts are easy.",
                "maps": "https://www.google.com/maps?q=17.4410599,78.5756127",
            },
        ],
    },
}


def draw_wrapped(c, text, x, y, max_width, font="Helvetica", size=9, leading=12, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    lines = []
    line = ""
    for word in words:
        trial = f"{line} {word}".strip()
        if stringWidth(trial, font, size) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def pill(c, x, y, text, color):
    c.setFillColor(colors.white)
    c.setStrokeColor(color)
    c.roundRect(x, y - 2, stringWidth(text, "Helvetica-Bold", 8) + 14, 16, 8, stroke=1, fill=1)
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x + 7, y + 2, text)


def draw_header(c, area, page_num):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN, PAGE_H - 24, area["title"])
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 24, f"Page {page_num}")
    c.setStrokeColor(LINE)
    c.line(MARGIN, PAGE_H - 34, PAGE_W - MARGIN, PAGE_H - 34)


def draw_card(c, prospect, x, y, w, h):
    c.setFillColor(PANEL)
    c.setStrokeColor(LINE)
    c.roundRect(x, y - h, w, h, 8, stroke=1, fill=1)

    img_size = 126
    img_x = x + 14
    img_y = y - 14 - img_size
    image = ImageReader(str(ASSETS / prospect["image"]))
    c.drawImage(image, img_x, img_y, img_size, img_size, preserveAspectRatio=True, anchor="c")

    text_x = img_x + img_size + 16
    text_w = w - img_size - 44
    text_y = y - 20

    pill(c, text_x, text_y, "<10 floors", GREEN)
    pill(c, text_x + 74, text_y, prospect["confidence"], AMBER if "Low" in prospect["confidence"] else GREEN)
    text_y -= 22

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(INK)
    c.drawString(text_x, text_y, prospect["name"])
    text_y -= 15

    c.setFont("Helvetica", 8.5)
    c.setFillColor(MUTED)
    c.drawString(text_x, text_y, prospect["coords"])
    text_y -= 17

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(INK)
    c.drawString(text_x, text_y, prospect["floors"])
    text_y -= 12

    c.setFont("Helvetica", 9)
    c.setFillColor(MUTED)
    text_y = draw_wrapped(c, prospect["units"], text_x, text_y, text_w, "Helvetica", 9, 11, MUTED)
    text_y -= 3

    text_y = draw_wrapped(c, prospect["note"], text_x, text_y, text_w, "Helvetica", 9, 11, INK)

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GREEN)
    link_y = y - h + 16
    c.drawString(text_x, link_y, "Open in Google Maps")
    c.linkURL(prospect["maps"], (text_x, link_y - 2, text_x + 98, link_y + 9), relative=0)


def create_pdf(area):
    c = canvas.Canvas(str(area["file"]), pagesize=A4)
    page_num = 1
    draw_header(c, area, page_num)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 26)
    title_y = PAGE_H - 78
    for line in wrap(area["title"], 34):
        c.drawString(MARGIN, title_y, line)
        title_y -= 30

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 11)
    draw_wrapped(c, area["subtitle"], MARGIN, title_y - 6, PAGE_W - 2 * MARGIN, "Helvetica", 11, 15, MUTED)

    c.setFillColor(PANEL_2)
    c.setStrokeColor(LINE)
    box_y = title_y - 68
    c.roundRect(MARGIN, box_y - 64, PAGE_W - 2 * MARGIN, 64, 8, stroke=1, fill=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(MARGIN + 14, box_y - 20, "Recommended field route")
    draw_wrapped(c, area["route"], MARGIN + 14, box_y - 38, PAGE_W - 2 * MARGIN - 28, "Helvetica", 9, 11, MUTED)

    y = box_y - 92
    card_h = 174
    for idx, prospect in enumerate(area["prospects"]):
        if y - card_h < 54:
            c.showPage()
            page_num += 1
            draw_header(c, area, page_num)
            y = PAGE_H - 58
        draw_card(c, prospect, MARGIN, y, PAGE_W - 2 * MARGIN, card_h)
        y -= card_h + 16

    c.setFont("Helvetica", 8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, 30, "Generated from Google Maps candidate coordinates and satellite-tile rooftop review. Field verification required before proposal sizing.")
    c.save()


def main():
    for area in AREAS.values():
        create_pdf(area)
        print(area["file"])


if __name__ == "__main__":
    main()

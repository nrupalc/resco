from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs" / "sales-marketing" / "generated" / "leaflets"
PHOTO = OUT / "assets" / "rooftop-solar-apartment-photo.png"
LOGO_DARK = ROOT / "docs" / "brand" / "logos" / "final" / "bright-roof-final-logo-dark-transparent.png"
LOGO_LIGHT = ROOT / "docs" / "brand" / "logos" / "final" / "bright-roof-final-logo-transparent.png"

DPI = 300
A4 = (2480, 3508)
A5 = (1748, 2480)

NAVY = "#0E1E4D"
AMBER = "#F5A524"
TERRACOTTA = "#C75B3C"
CREAM = "#FAF6EE"
SLATE = "#2C3444"
MUTED = "#6B7280"
LIGHT = "#E8EBEF"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except Exception:
            continue
    return ImageFont.load_default()


def cover_crop(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    src_w, src_h = image.size
    scale = max(target_w / src_w, target_h / src_h)
    resized = image.resize((int(src_w * scale), int(src_h * scale)), Image.Resampling.LANCZOS)
    x = (resized.width - target_w) // 2
    y = (resized.height - target_h) // 2
    return resized.crop((x, y, x + target_w, y + target_h))


def paste_logo(canvas: Image.Image, logo_path: Path, box: tuple[int, int, int, int]) -> None:
    if not logo_path.exists():
        return
    logo = Image.open(logo_path).convert("RGBA")
    max_w, max_h = box[2], box[3]
    logo.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    canvas.paste(logo, (box[0], box[1]), logo)


def text_lines(draw: ImageDraw.ImageDraw, text: str, fnt, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if draw.textbbox((0, 0), candidate, font=fnt)[2] <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_text(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], fnt, fill: str, max_width: int, leading: int) -> int:
    x, y = xy
    for line in text_lines(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rounded_rect(draw: ImageDraw.ImageDraw, box, radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def save_all(img: Image.Image, stem: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    png = OUT / f"{stem}.png"
    jpg = OUT / f"{stem}.jpg"
    pdf = OUT / f"{stem}.pdf"
    img.save(png, dpi=(DPI, DPI))
    img.convert("RGB").save(jpg, quality=95, dpi=(DPI, DPI))
    img.convert("RGB").save(pdf, resolution=DPI)
    print(pdf)
    print(png)
    print(jpg)


def make_a4() -> Image.Image:
    photo = Image.open(PHOTO).convert("RGB")
    img = Image.new("RGB", A4, CREAM)
    draw = ImageDraw.Draw(img)

    hero_h = 1470
    hero = cover_crop(photo, (A4[0], hero_h))
    img.paste(hero, (0, 0))
    overlay = Image.new("RGBA", (A4[0], hero_h), (14, 30, 77, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, A4[0], hero_h), fill=(14, 30, 77, 95))
    od.rectangle((0, hero_h - 380, A4[0], hero_h), fill=(14, 30, 77, 175))
    img.paste(overlay, (0, 0), overlay)

    paste_logo(img, LOGO_DARK, (150, 110, 360, 160))
    draw.text((A4[0] - 920, 145), "BRIGHT ROOF POWER SYSTEMS", font=font(42, True), fill=WHITE)
    draw.text((A4[0] - 570, 205), "Solar that stays.", font=font(34), fill=CREAM)

    x = 150
    y = 705
    draw.rectangle((x, y - 40, x + 150, y - 28), fill=AMBER)
    y = draw_text(
        draw,
        "FREE* rooftop solar installation",
        (x, y),
        font(104, True),
        WHITE,
        1420,
        116,
    )
    y += 16
    y = draw_text(
        draw,
        "for your apartment society",
        (x, y),
        font(70, True),
        WHITE,
        1420,
        82,
    )
    y += 18
    draw_text(
        draw,
        "Rs. 0 upfront installation payment. Start reducing common-area electricity bills.",
        (x, y),
        font(43, True),
        AMBER,
        1540,
        56,
    )

    badge_x, badge_y = A4[0] - 570, 570
    draw.ellipse((badge_x, badge_y, badge_x + 350, badge_y + 350), fill=AMBER)
    draw.ellipse((badge_x + 18, badge_y + 18, badge_x + 332, badge_y + 332), outline=NAVY, width=6)
    draw.text((badge_x + 77, badge_y + 78), "Rs. 0", font=font(78, True), fill=NAVY)
    draw.text((badge_x + 54, badge_y + 168), "UPFRONT", font=font(44, True), fill=NAVY)
    draw.text((badge_x + 79, badge_y + 224), "PAYMENT", font=font(32, True), fill=NAVY)

    content_y = hero_h + 115
    draw.text((150, content_y), "What FREE* means", font=font(50, True), fill=NAVY)
    draw.rectangle((150, content_y + 72, 315, content_y + 84), fill=AMBER)
    body = (
        "Your society does not pay upfront installation cost. Bright Roof installs, owns, operates, and maintains the rooftop solar system. "
        "Your society pays only for solar electricity under the agreement, with a starting proposal of 10% saving against the agreed electricity-tariff benchmark."
    )
    draw_text(draw, body, (150, content_y + 135), font(34), SLATE, 1080, 48)

    card_y = content_y + 430
    card_w = 510
    gap = 42
    cards = [
        ("Free installation*", "No upfront installation payment by the society."),
        ("Owned and maintained by Bright Roof", "We handle operation, cleaning, monitoring, and repairs."),
        ("10% starting saving", "Against the agreed electricity-tariff benchmark."),
        ("Simple first step", "Share bills and allow rooftop/electrical-room survey."),
    ]
    for i, (title, desc) in enumerate(cards):
        cx = 150 + (i % 2) * (card_w + gap)
        cy = card_y + (i // 2) * 310
        rounded_rect(draw, (cx, cy, cx + card_w, cy + 250), 24, WHITE, LIGHT, 3)
        draw.ellipse((cx + 34, cy + 36, cx + 62, cy + 64), fill=AMBER)
        draw_text(draw, title, (cx + 85, cy + 30), font(31, True), NAVY, 360, 38)
        draw_text(draw, desc, (cx + 38, cy + 112), font(25), SLATE, 420, 36)

    side_x = 1360
    rounded_rect(draw, (side_x, content_y, A4[0] - 150, content_y + 820), 32, NAVY)
    draw.text((side_x + 70, content_y + 70), "Best fit for apartments with", font=font(36, True), fill=CREAM)
    fit = ["Lifts", "Water pumps", "Common lighting", "Clubhouse", "STP", "Security loads"]
    fy = content_y + 170
    for item in fit:
        draw.ellipse((side_x + 76, fy + 10, side_x + 100, fy + 34), fill=AMBER)
        draw.text((side_x + 128, fy), item, font=font(31), fill=WHITE)
        fy += 62
    rounded_rect(draw, (side_x + 60, content_y + 650, A4[0] - 210, content_y + 760), 22, AMBER)
    draw.text((side_x + 95, content_y + 680), "Call / WhatsApp", font=font(30, True), fill=NAVY)
    draw.text((side_x + 95, content_y + 718), "+91 93902 10407", font=font(34, True), fill=NAVY)

    footer_y = A4[1] - 230
    draw.line((150, footer_y, A4[0] - 150, footer_y), fill=LIGHT, width=3)
    draw.text((150, footer_y + 44), "support@brightroofpower.com", font=font(29, True), fill=NAVY)
    draw.text((760, footer_y + 44), "www.brightroofpower.com", font=font(29, True), fill=NAVY)
    draw.text((150, footer_y + 100), "*Free installation means the society does not pay upfront installation cost. Solar electricity is billed under the signed agreement.", font=font(20), fill=MUTED)
    return img


def make_a5() -> Image.Image:
    photo = Image.open(PHOTO).convert("RGB")
    img = Image.new("RGB", A5, CREAM)
    draw = ImageDraw.Draw(img)

    hero_h = 1040
    hero = cover_crop(photo, (A5[0], hero_h))
    img.paste(hero, (0, 0))
    overlay = Image.new("RGBA", (A5[0], hero_h), (14, 30, 77, 120))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, A5[0], hero_h), fill=(14, 30, 77, 105))
    od.rectangle((0, hero_h - 360, A5[0], hero_h), fill=(14, 30, 77, 185))
    img.paste(overlay, (0, 0), overlay)

    paste_logo(img, LOGO_DARK, (95, 82, 300, 130))
    draw.text((A5[0] - 730, 110), "BRIGHT ROOF POWER SYSTEMS", font=font(31, True), fill=WHITE)
    draw.text((A5[0] - 375, 154), "Solar that stays.", font=font(25), fill=CREAM)

    x = 95
    y = 555
    draw.rectangle((x, y - 34, x + 120, y - 22), fill=AMBER)
    y = draw_text(draw, "FREE* rooftop solar installation.", (x, y), font(70, True), WHITE, 1260, 80)
    y += 10
    draw_text(
        draw,
        "For apartment societies. Rs. 0 upfront installation payment.",
        (x, y),
        font(33, True),
        AMBER,
        1180,
        46,
    )

    y = hero_h + 95
    rounded_rect(draw, (95, y - 18, 520, y + 135), 24, AMBER)
    draw.text((130, y + 12), "Rs. 0", font=font(58, True), fill=NAVY)
    draw.text((130, y + 76), "UPFRONT PAYMENT", font=font(25, True), fill=NAVY)
    draw_text(draw, "Free installation means your society does not pay upfront installation cost.", (580, y), font(37, True), TERRACOTTA, 900, 48)
    y += 175
    draw_text(
        draw,
        "Bright Roof installs, owns, operates, and maintains the rooftop solar system. The society pays only for solar electricity under the agreement.",
        (95, y),
        font(31),
        SLATE,
        1280,
        43,
    )
    y += 205
    rounded_rect(draw, (95, y, A5[0] - 95, y + 285), 28, WHITE, LIGHT, 3)
    draw.text((140, y + 50), "Good fit for societies with", font=font(34, True), fill=NAVY)
    points = ["Lifts", "Water pumps", "Common lighting", "STP", "Security loads"]
    py = y + 125
    px = 145
    for i, item in enumerate(points):
        bx = px + (i % 2) * 570
        by = py + (i // 2) * 55
        draw.ellipse((bx, by + 8, bx + 22, by + 30), fill=AMBER)
        draw.text((bx + 42, by), item, font=font(28), fill=SLATE)

    cta_y = A5[1] - 360
    rounded_rect(draw, (95, cta_y, A5[0] - 95, cta_y + 205), 28, NAVY)
    draw.text((145, cta_y + 44), "Call / WhatsApp: +91 93902 10407", font=font(36, True), fill=AMBER)
    draw.text((145, cta_y + 108), "support@brightroofpower.com", font=font(28), fill=CREAM)
    draw.text((145, cta_y + 152), "www.brightroofpower.com", font=font(28), fill=CREAM)
    draw.text((95, A5[1] - 82), "*Free installation means no upfront installation cost. Solar electricity is billed under the signed agreement.", font=font(18), fill=MUTED)
    return img


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    save_all(make_a4(), "bright-roof-photo-flyer-a4-color")
    save_all(make_a5(), "bright-roof-photo-flyer-a5-handout")
    save_all(make_a4(), "bright-roof-free-installation-flyer-a4-color")
    save_all(make_a5(), "bright-roof-free-installation-flyer-a5-handout")


if __name__ == "__main__":
    main()

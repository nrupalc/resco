import io
import math
import pathlib
import urllib.request

from PIL import Image, ImageDraw


ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

SITES = [
    {"area": "nacharam-east", "slug": "raheja-vistas-elite", "name": "Raheja Vistas Elite", "lat": 17.4320216, "lng": 78.5645212},
    {"area": "nacharam-east", "slug": "concrete-palazzo", "name": "Concrete Palazzo", "lat": 17.4278449, "lng": 78.5526548},
    {"area": "nacharam-east", "slug": "concrete-opus", "name": "Concrete Opus Apartments", "lat": 17.4301484, "lng": 78.5538058},
    {"area": "nacharam-east", "slug": "royal-garden-nacharam", "name": "Royal Garden Apartments Nacharam", "lat": 17.4300889, "lng": 78.55301},
    {"area": "nacharam-east", "slug": "ratnanidhi-nivas", "name": "Ratnanidhi Nivas Apartments", "lat": 17.4270276, "lng": 78.5544784},
    {"area": "nacharam-east", "slug": "sri-tirumala-millennium-phase-2", "name": "Sri Tirumala Millennium Phase 2", "lat": 17.4370167, "lng": 78.5699369},
    {"area": "nacharam-east", "slug": "shanti-gardens-block-e", "name": "Shanti Gardens Block E", "lat": 17.4251239, "lng": 78.5519081},
    {"area": "nacharam-east", "slug": "navya-global-apartments", "name": "Navya Global Apartments", "lat": 17.4283708, "lng": 78.5542484},
    {"area": "nacharam-east", "slug": "ns-platinum", "name": "NS Platinum Apartments", "lat": 17.4283602, "lng": 78.5537998},
    {"area": "nacharam-east", "slug": "sai-darshan-nacharam", "name": "Sai Darshan Apartments Nacharam", "lat": 17.4278146, "lng": 78.5497251},
    {"area": "mallapur", "slug": "mayflower-grande", "name": "Mayflower Grande", "lat": 17.4469705, "lng": 78.5707892},
    {"area": "mallapur", "slug": "mayflower-platinum", "name": "Mayflower Platinum", "lat": 17.4469699, "lng": 78.5740716},
    {"area": "mallapur", "slug": "mayflower-park", "name": "Mayflower Park Apartments", "lat": 17.4432638, "lng": 78.5686462},
    {"area": "mallapur", "slug": "gulmohar-residency", "name": "Gulmohar Residency", "lat": 17.450772, "lng": 78.572771},
    {"area": "mallapur", "slug": "gulmohar-gardens", "name": "Gulmohar Gardens", "lat": 17.4443797, "lng": 78.5805605},
    {"area": "mallapur", "slug": "srinivasam-mallapur", "name": "Srinivasam Apartments Mallapur", "lat": 17.4455756, "lng": 78.5731789},
    {"area": "mallapur", "slug": "sri-tirumala-millennium", "name": "Sri Tirumala Millennium", "lat": 17.4370167, "lng": 78.5699369},
    {"area": "mallapur", "slug": "janapriya-township", "name": "Janapriya Township", "lat": 17.441777, "lng": 78.5683431},
    {"area": "mallapur", "slug": "aditya-pearl", "name": "Aditya Pearl Apartment", "lat": 17.4410599, "lng": 78.5756127},
    {"area": "mallapur", "slug": "vishnu-gokulam", "name": "Vishnu Gokulam Apartments", "lat": 17.44535, "lng": 78.5866071},
    {"area": "mallapur", "slug": "pournima-apartments", "name": "Pournima Apartments", "lat": 17.4424264, "lng": 78.5844828},
    {"area": "mallapur", "slug": "new-sri-balaji-residency", "name": "New Sri Balaji Residency", "lat": 17.445107, "lng": 78.5650831},
]


def latlng_to_tile(lat, lng, zoom):
    lat_rad = math.radians(lat)
    n = 2**zoom
    x = int((lng + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + 1.0 / math.cos(lat_rad)) / math.pi) / 2.0 * n)
    return x, y


def fetch_tile(x, y, zoom):
    server = (x + y) % 4
    url = f"https://mt{server}.google.com/vt/lyrs=s&x={x}&y={y}&z={zoom}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as response:
        return Image.open(io.BytesIO(response.read())).convert("RGB")


def render_site(site, zoom=20, radius=1):
    center_x, center_y = latlng_to_tile(site["lat"], site["lng"], zoom)
    size = 256 * (radius * 2 + 1)
    canvas = Image.new("RGB", (size, size), "white")

    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            tile = fetch_tile(center_x + dx, center_y + dy, zoom)
            canvas.paste(tile, ((dx + radius) * 256, (dy + radius) * 256))

    draw = ImageDraw.Draw(canvas)
    cx = cy = size // 2
    draw.line((cx - 18, cy, cx + 18, cy), fill=(255, 60, 46), width=4)
    draw.line((cx, cy - 18, cx, cy + 18), fill=(255, 60, 46), width=4)
    draw.ellipse((cx - 7, cy - 7, cx + 7, cy + 7), outline=(255, 255, 255), width=3)

    jpg = ASSETS / f"{site['area']}-{site['slug']}.jpg"
    png = ASSETS / f"{site['area']}-{site['slug']}.png"
    canvas.save(jpg, quality=92)
    canvas.save(png)
    return png


def main():
    for site in SITES:
        out = render_site(site)
        print(f"{site['area']} / {site['name']}: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

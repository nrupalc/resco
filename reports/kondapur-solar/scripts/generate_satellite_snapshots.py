import io
import math
import pathlib
import urllib.request

from PIL import Image, ImageDraw


ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

CANDIDATES = [
    {"slug": "smr-vinay-iconia", "name": "SMR Vinay Iconia", "zone": "West / northwest", "lat": 17.4683048, "lng": 78.3347189},
    {"slug": "aparna-luxor-park", "name": "Aparna Luxor Park", "zone": "West / northwest", "lat": 17.4668133, "lng": 78.3359351},
    {"slug": "sumadhura-horizon", "name": "Sumadhura Horizon", "zone": "West / northwest", "lat": 17.4655873, "lng": 78.3375692},
    {"slug": "luxor-apartments", "name": "Luxor Apartments", "zone": "Northwest", "lat": 17.470148, "lng": 78.3444776},
    {"slug": "my-home-mangala", "name": "My Home Mangala", "zone": "North", "lat": 17.4743634, "lng": 78.3480049},
    {"slug": "prime-legend", "name": "Prime Legend", "zone": "Central west", "lat": 17.4644119, "lng": 78.3463583},
    {"slug": "ruby-n-pearl", "name": "Ruby n Pearl Apartments", "zone": "Central west", "lat": 17.4642864, "lng": 78.3493263},
    {"slug": "galaxy-apartments", "name": "Galaxy Apartments", "zone": "North / east", "lat": 17.4720857, "lng": 78.3588236},
    {"slug": "vajra-sree-nivasam", "name": "Vajra Sree Nivasam", "zone": "North / east", "lat": 17.4679959, "lng": 78.3628272},
    {"slug": "pranavas-lotus-park", "name": "Pranavas Lotus Park", "zone": "Central east", "lat": 17.4611087, "lng": 78.3628345},
    {"slug": "bollineni-bion", "name": "Bollineni Bion", "zone": "South / east", "lat": 17.4582146, "lng": 78.3623961},
    {"slug": "aditya-heights-whitefield", "name": "Aditya Heights Whitefield", "zone": "South / east", "lat": 17.4553091, "lng": 78.3644418},
    {"slug": "trendset-jayabheri-elevate", "name": "Trendset Jayabheri Elevate", "zone": "South / east", "lat": 17.4566105, "lng": 78.3666634},
    {"slug": "aparna-towers", "name": "Aparna Towers", "zone": "East", "lat": 17.4645608, "lng": 78.3690966},
    {"slug": "casa-rouge", "name": "Casa Rouge", "zone": "East", "lat": 17.4624186, "lng": 78.3707567},
]


def latlng_to_tile(lat, lng, zoom):
    lat_rad = math.radians(lat)
    n = 2**zoom
    x = int((lng + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + 1.0 / math.cos(lat_rad)) / math.pi) / 2.0 * n)
    return x, y


def fetch_tile(x, y, zoom, layer="s"):
    server = (x + y) % 4
    url = f"https://mt{server}.google.com/vt/lyrs={layer}&x={x}&y={y}&z={zoom}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as response:
        return Image.open(io.BytesIO(response.read())).convert("RGB")


def render_candidate(candidate, zoom=20, radius=1):
    center_x, center_y = latlng_to_tile(candidate["lat"], candidate["lng"], zoom)
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

    out = ASSETS / f"{candidate['slug']}.jpg"
    canvas.save(out, quality=92)
    return out


def main():
    for candidate in CANDIDATES:
        out = render_candidate(candidate)
        print(f"{candidate['name']}: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

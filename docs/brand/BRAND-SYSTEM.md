# Bright Roof — Brand System

**Version:** 0.1 (working draft)
**Last updated:** 2026-04-22

---

## 1. The one-line opinion

> **Sunrise over the Indian rooftop.** Warm amber sun, deep navy sky, terracotta-and-cream rooftops. Solar, but residential, warm, human, and meant to last.

Every design decision should pass this test: *"Does this feel like the first minute of sunlight hitting a Hyderabad apartment block?"* If not, push it.

## 2. Personality

| Dimension | We are | We are **not** |
|---|---|---|
| Tone | Warm, patient, plain-spoken | Corporate jargon, hype |
| Posture | Confident, long-term, neighbour-like | Salesy, pushy, "disruption" energy |
| Proof | Numbers, generation data, contracts | Trends, buzzwords, stock photos of wind turbines |
| Colour | Amber on navy. Dawn. | Generic solar green-and-blue |
| Typography | Serif display + humanist sans | Geometric sans stacked on Inter |

## 3. Name and tagline

- **Legal name:** M/s. Bright Roof Power Systems
- **Short name:** Bright Roof
- **Tagline (primary):** *Solar that stays.*
- **Tagline (long form, for pitches):** *Long-term solar for long-term homes.*

Never use an exclamation mark in the tagline. Never translate it mechanically; leave it in English across Telugu/Hindi materials — it reads as a signature.

## 4. Colour system

### Primary

| Role | Name | Hex | Notes |
|---|---|---|---|
| Ink / primary | **Dawn Navy** | `#0E1E4D` | All headlines, primary text, logo base. |
| Signature | **Roof Amber** | `#F5A524` | The one colour that carries the brand. Buttons, accents, the sun. |

### Secondary / supporting

| Role | Name | Hex | Notes |
|---|---|---|---|
| Rooftop warm | **Terracotta** | `#C75B3C` | Photography tint, illustrative, warm secondary. |
| Paper | **Cream** | `#FAF6EE` | Default background on print and light surfaces. |
| Slate | **Slate 700** | `#2C3444` | Body text alternative to Dawn Navy on long reads. |
| Slate | **Slate 400** | `#6B7280` | Captions, metadata. |
| Slate | **Slate 100** | `#E8EBEF` | Dividers, card backgrounds. |

### State

| Role | Hex |
|---|---|
| Success | `#1F7A4D` |
| Warning | `#C28A1C` (a shade darker than amber so it's legible) |
| Error | `#B43A2A` |

### Rules

- **60 / 30 / 10.** Cream or Dawn Navy dominates (60%). Slate / white secondary (30%). Roof Amber as accent only (10%). Never flood a screen with amber.
- **Text on amber:** always Dawn Navy, never white.
- **Text on Dawn Navy:** Cream or white.
- **Avoid pure `#000000`** in any graphic. Use Slate 700 or Dawn Navy.
- **Avoid pure `#FFFFFF`** on print — use Cream.

## 5. Typography

### Typefaces

| Use | Typeface | Weights | Fallback |
|---|---|---|---|
| Display (headlines, wordmark) | **Fraunces** | 500, 700, 900 (+ italic) | Cormorant Garamond → Playfair Display → Georgia |
| Body / UI | **General Sans** | 400, 500, 600 | Manrope → Helvetica Neue → Arial |
| Mono (data tables, figures) | **JetBrains Mono** | 400, 500 | Fira Code → IBM Plex Mono → monospace |

> **Rationale.** Fraunces is a warm, slightly bookish serif — it makes a long-term promise look like a long-term promise. General Sans is the humanist-sans counterpoint that stays readable at small sizes on both screens and printed PPAs. We deliberately avoid Inter (overused) and Poppins (too round, too startup).

### Type scale (web)

| Token | Size / leading | Typeface | Example |
|---|---|---|---|
| `display/1` | 72 / 80 | Fraunces 700 | Hero headlines |
| `display/2` | 56 / 64 | Fraunces 700 | Page titles |
| `heading/1` | 36 / 44 | Fraunces 600 | Section heads |
| `heading/2` | 28 / 36 | Fraunces 600 | Sub-sections |
| `heading/3` | 22 / 30 | General Sans 600 | Card titles |
| `body/lg` | 18 / 28 | General Sans 400 | Reading paragraphs |
| `body/md` | 16 / 24 | General Sans 400 | Default body |
| `body/sm` | 14 / 20 | General Sans 500 | Captions, labels |
| `mono/md` | 14 / 22 | JetBrains Mono 400 | Numbers, tariffs |

### Typographic rules

- Display headlines always mix **serif display + one amber punctuation rule** (the short amber line under a phrase). Never underline.
- Italic is reserved for the **tagline only**. Never italicise body.
- Tracking: display tight (`-0.01em`), body neutral, all-caps labels widely spaced (`0.15em`).
- Numerals in tariff tables use tabular lining figures (JetBrains Mono).

## 6. Logo system

| File | Use |
|---|---|
| `logos/01-horizon.svg` | Primary mark. Default on letterheads, PPA covers, signage. |
| `logos/02-ray.svg` | Secondary / digital mark. App icon bases, favicons on dark, loaders. |
| `logos/03-seal.svg` | Badge / stamp form. Social avatars, stickers, WhatsApp profile. |
| `logos/04-wordmark-horizontal.svg` | Horizontal lockup. Email signatures, invoice header. |
| `logos/05-wordmark-stacked.svg` | Stacked lockup. PPA cover page, posters. |

### Logo rules

- **Clear space.** Minimum clear space around any lockup = the height of the "B" in "Bright".
- **Minimum size.** Horizontal wordmark: 120px wide on screen, 30 mm on print. Seal: 24 px minimum.
- **Colour use.** Default = navy + amber on cream. Allowed alternates: all-navy, all-cream-on-navy. Never rainbow, never amber-on-amber.
- **Don't.**
  - Don't rotate the logo.
  - Don't drop shadows, bevels, or outer glows.
  - Don't re-colour the sun to red / green / blue.
  - Don't stretch. Don't typeset "Bright Roof" in another font.

## 7. Voice and messaging

### Tone

Write like you're explaining your business to your neighbour over tea, not like you're pitching at a conference.

- Sentences are short. Claims are specific (units, rupees, years).
- Numbers beat adjectives. "Cuts your bill by Rs. 18,000 a month" beats "massive savings".
- Never say "revolutionary", "game-changing", "next-gen", or "synergies".
- The customer is the *society* or the *homeowner*, never "the consumer segment".
- "We" = Bright Roof. "You" = the society. Drop "the company" and "the client" everywhere.

### Boilerplate paragraphs

**Short (tweet / WhatsApp):**

> Bright Roof installs and owns the solar system on your apartment rooftop. You pay only for what you use, at about Rs. 2/unit below your current grid tariff. We stay with you for the full 20+ years — no handover, no surprise bills.

**Medium (website "About" paragraph):**

> Bright Roof Power Systems is a Hyderabad-based rooftop solar company built for apartment societies. We install the system at our cost, maintain it for 20+ years, and sell you the electricity it generates at a flat rate below your grid tariff. Unlike pay-off-and-handover models, we stay with the system for its full life — so the cost never bounces back to you.

**Long (pitch deck first page):**

> Most rooftop solar deals in India treat an apartment society like a utility-scale project: sign a 25-year contract, install a million rupees of equipment, and hand over the operational risk after payback. That is the wrong shape of deal for a 90-flat building in Hyderabad. Bright Roof keeps the system ours for its full life and keeps the rate fixed. Residents pay per unit, below grid, and we handle everything else — monitoring, cleaning, repair, DISCOM coordination, insurance. That is what we mean by *solar that stays*.

### Words to prefer / avoid

| Prefer | Avoid |
|---|---|
| system | "asset", "installation" when speaking to residents |
| society | "association", "HOA" |
| rooftop | "site", "premises" (keep "premises" only for contracts) |
| rupees | "INR", "₹" in body copy |
| units | "kWh" in consumer-facing copy (use kWh in contracts and spec) |

## 8. Photography and imagery

We will build a photo library over time. Until then, these are the rules for AI-generated or stock images:

- **Scene:** Indian apartment rooftops, mid-density mid-rise (4–8 floor), terracotta-and-white, solar panels installed, golden-hour light.
- **People:** residents interacting — a society secretary with a tablet, an electrician on the roof, a family on a balcony. Real-looking. No stock-suit handshake photos.
- **Angles:** wide rooftop shots, low-angle panel detail, aerial at dawn.
- **Never:** stock wind turbines, polar bears, an earth-in-hands photo, hard-hat-pointing-at-laptop.
- **Treatment:** slight warm grade, shadows lifted, saturation restrained. One amber-lit highlight.

Prompts are in `prompts/marketing-imagery.md`.

## 9. Layout principles

- **Generous margins.** At least 48 px on web, 20 mm on print. Never crowd.
- **A single amber accent per view** — a button, a rule under a heading, or a sun in the illustration. Not all three.
- **Left-align long reads.** Centre-align only for covers, section breaks, and quotes.
- **Use the amber rule.** A 3-px amber horizontal rule, 40–80 px long, is the house device. Use it once per page, between a heading and a tagline, or above a call to action.

## 10. Touchpoints to design (roadmap)

- [x] Colour + type tokens
- [x] Three logo directions
- [x] Horizontal + stacked wordmarks
- [ ] Letterhead (A4)
- [ ] PPA cover page
- [ ] Visiting card (front + back)
- [ ] Email signature
- [ ] WhatsApp/social profile picture (use Seal)
- [ ] 1-page sales leaflet for society committees
- [ ] Pitch deck template
- [ ] Website home page (Stitch design pass)
- [ ] Invoice template
- [ ] Site signage (plate on the rooftop enclosure)
- [ ] Hard-hat / T-shirt for field team

## 11. Open questions

- [ ] **Pick one logo direction** from the three drafts — Horizon / Ray / Seal — before locking the system. Recommend **Horizon** as primary, **Seal** as secondary for avatars.
- [ ] Confirm **tagline** — *Solar that stays.* — with partners.
- [ ] Confirm **colour palette** vs. a safer navy-only option for a first conservative audience (traditional apartment society committees).
- [ ] Do we want a **Telugu/Hindi wordmark** variant? If yes, we commission a Devanagari/Telugu match for Fraunces (look at Ek Mukta or Tiro Devanagari for Hindi).

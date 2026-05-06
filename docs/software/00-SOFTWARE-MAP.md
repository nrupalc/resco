# Bright Roof Power Systems — Complete Software Map

> **Date:** 2026-04-22
> **Purpose:** Enumerate every piece of software Bright Roof Power Systems will need across the full company lifecycle — marketing, sales, operations, field, finance, compliance, customer-facing. Group by function, phase by business stage, and make an opinionated build-vs-buy call for each.
> **Audience:** Partners (Nrupal, Phani, Vijay, Cnu, Kalyan).
> **Scope:** This is the meta-plan. Each module listed here will get its own design spec when its phase arrives.

---

## 1. Model recap (what the software has to support)

- **RESCO / OPEX.** Bright Roof installs, owns, and operates. Society pays per-unit PPA rate (grid tariff minus ~Rs 2/kWh) for solar units consumed against their common-area meter via net metering. Term 25 years. Society has a **buyback option** but default is continued ownership past breakeven (~5 years).
- **Customer = society committee (AOA/RWA)**, not individual residents. Long-duration B2B contract; monthly billing; recovery risk sits with the committee.
- **First year: 5 sites. Three-year target: 100 installs.** Everything built needs to scale from "one pilot run manually" to "100 sites run autonomously" without a rewrite.
- **Bootstrapped.** No large tech spend. Heavy bias toward buying mature SaaS for commodity functions and building only what is differentiating or RESCO-specific.
- **Leverage YENSI stack** where it fits (Keystone infra, Concierge for customer ops, NC Dev to build the custom pieces, Sentinel for monitoring, Keeper for India-specific accounting).

---

## 2. The full software inventory — seven functional layers

Seventy-two pieces, grouped by where they live in the company.

### Layer 1 — External / Marketing & Sales

| # | Piece | What it does | Notes |
|---|---|---|---|
| 1 | **Marketing website** | Landing + story + team + case studies + sustainability thesis + contact | Next.js/Astro. Uses brand kit (Dawn Navy + Roof Amber, Fraunces/General Sans). "Bold Brand Photography" archetype. |
| 2 | **Public savings calculator** | Society enters common-area bill, units/month, roof area → outputs capacity, generation, monthly + lifetime savings, breakeven if they bought vs if we RESCO | Core conversion tool. Exports a teaser PDF. |
| 3 | **Enquiry / lead-capture flow** | Multi-step qualifying form: society name, location, units count, common-area spend, roof availability, committee consent stage | Feeds CRM. |
| 4 | **Committee proposal generator** | Branded PDF proposal per society: their 12-month consumption, projected generation, PPA rate, savings curve, term, buyback scenarios | Internal tool; Cnu/Vijay/Kalyan print this for meetings. |
| 5 | **Content / case-study CMS** | Publish pilot case study (Sri Tirumala Millennium), news, policy explainers | Sanity or Keystone CMS or simple MDX in the site repo. |
| 6 | **Public buyback calculator** | "What would it cost your society to buy this system today?" — live depreciation curve | Differentiator vs Volt: transparent exit economics. |
| 7 | **Lead nurture drip** | Email + WhatsApp sequences for leads not yet ready | Resend + WhatsApp Business API. |
| 8 | **Referral program** | Existing-society committee earns credit for introducing another society | Simple referral codes on society portal. |
| 9 | **Coverage / social proof map** | Public map showing signed + generating sites in Hyderabad | MapmyIndia or Google Maps. Powerful trust signal at 20+ sites. |

### Layer 2 — Society & Resident-Facing

| # | Piece | What it does | Notes |
|---|---|---|---|
| 10 | **Society committee portal** | Login per society. Live generation, exported units, savings YTD, invoices, payment history, PPA document, raise support ticket | Mobile-first. Telugu + English. |
| 11 | **Resident lightweight view (optional)** | Residents can see "your society saved Rs X this month" — social reinforcement | Opt-in per society. Drives advocacy for renewal / more capacity. |
| 12 | **Digital onboarding workflow** | Collect committee resolution, AOA bylaws, KYC of committee members, 12 months of common-area bills, roof photos, structural clearance | e-KYC (Aadhaar-based). Checklist drives the PPA-signing gate. |
| 13 | **PPA e-signing flow** | Digital PPA execution — stamp-paper compliant (India), witness capture, Aadhaar e-sign | Digio or Leegality. |
| 14 | **Society-side buyback request** | Committee can formally request a buyout quote from the portal | Goes to finance for review + approval. |
| 15 | **Support ticketing** | Society raises generation/billing/maintenance issue | Freshdesk or built into the portal; routes into Concierge. |
| 16 | **Committee-member change workflow** | Committees rotate every 1–2 years; new committee = new signatories, portal access change | Often missed by built-for-enterprise CRMs. Native to us. |

### Layer 3 — Internal Ops: Pre-Sale

| # | Piece | What it does | Notes |
|---|---|---|---|
| 17 | **CRM (solar-aware)** | Lead → site visit → structural audit → quote → PPA → install pipeline. Each stage has a RESCO-specific checklist (roof condition, shadow %, consumption proof, sanctioned load, meter type) | Start on Zoho CRM or Airtable; build custom once pipeline is >30 leads. |
| 18 | **Field site-survey mobile app** | Cnu/Vijay/Kalyan on-site: GPS, photo capture (roof, DB, meter), structural audit form, rooftop dimensions, shade observations | Offline-first (Hyderabad rooftop connectivity is spotty). |
| 19 | **Shadow / irradiation analysis** | From field photos + coordinates, estimate effective irradiation vs nameplate over the year | Buy: Solcast / Aurora Solar API. Build: thin layer that stores results per site. |
| 20 | **Capacity sizing + design tool** | Inputs: roof area, shadow %, target generation, consumption profile → outputs: panel layout, inverter sizing, structural load, BOM | Can start manual + Excel (Vijay already has Excel templates); graduate to web tool at ~10 sites. |
| 21 | **Vendor / procurement system** | RFQ to panel vendors (Waaree/Premier/Tata/Adani), inverter vendors (Growatt/Sois/Faston), cables/mounting/labour. Compare quotes, raise POs, track invoices. | Zoho Inventory or Odoo or ERPNext for Year 2+. |
| 22 | **Project management — installation** | Per-site: structural audit → design → approvals (TGREDCO, TGSPDCL NOC) → materials → crew → commissioning | Kanban per site. Linear-style board internally. |
| 23 | **Approvals tracker (DISCOM / TGREDCO)** | Every site needs Net Metering approval + TGSPDCL NOC + sometimes society NOC + Fire NOC for rooftop | Deadline-driven; policy-aware. Ties into the Regulatory Watchdog (#55). |

### Layer 4 — Internal Ops: Post-Install (Generation & Billing)

| # | Piece | What it does | Notes |
|---|---|---|---|
| 24 | **Inverter gateway (multi-OEM aggregator)** | Pulls real-time data from Growatt ShineServer, Sois, Faston, Dyee APIs into one normalized schema | Must-build. Each OEM has its own cloud — no unified API exists. |
| 25 | **Edge collector (optional)** | Small device at site for local data cache + kill-switch fallback if OEM cloud fails | Raspberry Pi or off-the-shelf IoT gateway. Deploy once we have >5 sites. |
| 26 | **Net-meter data ingestion** | DISCOM (TGSPDCL/TGNPDCL) net-meter export/import reading, either via their consumer portal scrape or manual upload until API exists | This is where the PPA invoice starts. |
| 27 | **Billing engine (RESCO-specific)** | For each site, monthly: net units × PPA rate → invoice, with adjustments (weather, outage credits, tariff revisions) | Must-build. Off-the-shelf billing SaaS doesn't know PPAs. |
| 28 | **Invoice generator + GST e-invoicing** | GST-compliant invoice, optional IRN generation via ClearTax/Zoho; PDF + email + WhatsApp delivery | Buy the e-invoicing layer (ClearTax), build the invoice template. |
| 29 | **Payment collection + reconciliation** | NACH auto-debit from society account, UPI / bank transfer fallback, Razorpay/Cashfree | NACH is slow to set up; have UPI as Month-1 primary. |
| 30 | **Collections / chaser workflow** | Tiered dunning: day-3 WhatsApp → day-7 email → day-14 voice reminder → day-21 partner call → day-30 kill-switch notice | Concierge (YENSI) is the right substrate. |
| 31 | **Kill switch with legal safeguards** | Remote disconnect via inverter API / relay, with 30-day notice, audit trail, PPA-mandated justification | Build last. Use sparingly. Document every use for PPA defence. |
| 32 | **Maintenance / field-service scheduler** | Quarterly panel cleaning, annual inverter checks, warranty claims, complaint-driven visits | Start with Google Calendar + checklist; graduate to custom at 20+ sites. |
| 33 | **Warranty tracker** | Every panel + inverter serial + install date + warranty end + vendor RMA contact | Asset register (#44) is the backbone. |
| 34 | **Predictive maintenance / anomaly detection** | ML on generation curves → flag soiling, degradation, string faults, inverter faults before failure | Year 2 feature. Needs >10 sites of history. |

### Layer 5 — Monitoring, Analytics & Forecasting

| # | Piece | What it does | Notes |
|---|---|---|---|
| 35 | **Ops single-pane-of-glass** | All sites at a glance: health, generation vs target, revenue, overdue, alerts | One screen on a partner's phone. |
| 36 | **Partner / investor dashboard** | Capital deployed, cash collected, MRR, overdue %, IRR per project, portfolio IRR, cumulative breakeven vs model | Auto-generates the monthly partner digest. |
| 37 | **Consumption profile analyzer** | Ingest 12 months of society bills → identify peak/off-peak, day/night split, right-size proposal | Feeds the public calculator (#2) and the proposal generator (#4). |
| 38 | **Cashflow forecasting** | 30/90/365-day cashflow from signed PPAs + expected generation + collection probability | Critical for bootstrapped operations. |
| 39 | **Tariff tracker** | Monitor TGSPDCL tariff revisions → auto-recompute savings projections and margin risk | If DISCOM tariff drops, our Rs-2 spread compresses. |
| 40 | **Regulatory watchdog** | Poll MNRE, TGREDCO, TGSPDCL, CERC for policy changes → summarize impact | AI digest to partner WhatsApp group weekly. |
| 41 | **BI / reporting platform** | Metabase or Superset on a central data warehouse | Month-1 nice-to-have, Year-2 must-have. |
| 42 | **Central data warehouse / lake** | Every event: inverter, billing, ticket, CRM, accounting, DISCOM | Postgres + dbt for Year 1; ClickHouse or BigQuery at scale. |

### Layer 6 — Finance, Legal, HR, Compliance

| # | Piece | What it does | Notes |
|---|---|---|---|
| 43 | **Accounting system** | Chart of accounts tuned for RESCO: asset capitalization, depreciation, PPA revenue recognition, project-wise P&L | Zoho Books or Tally. CA already connected (Venketeswarlu garu). |
| 44 | **Asset register** | Every panel/inverter serial, purchase price, install date, depreciation schedule, warranty expiry, insurance policy, current book value | Foundational. Feeds depreciation, insurance, RMA, buyback calc. |
| 45 | **Cap-table + partner capital account ledger** | 35/35/10/10/10 split, sweat-equity vesting (Kalyan/Cnu 3-year buy-in), capital contributions, buy-in reimbursements in 43.75/43.75/12.5 ratio | Must-build (or Notion/Excel for Year 1; real tool at conversion to Pvt Ltd). |
| 46 | **Financial modelling + IRR tracker** | Per-project IRR vs plan, portfolio IRR, sensitivity (tariff, generation, O&M, interest rate) | Excel Year 1 → Python/Streamlit Year 2. |
| 47 | **GST / TDS / e-invoicing compliance** | GSTR-1 and GSTR-3B monthly, TDS filings, annual IT return | Zoho Books + CA integration. |
| 48 | **Statutory compliance calendar** | Firm annual filings, GST monthly, IT annual, ROC if converted, TGREDCO annual reports, DISCOM NOC renewals, rooftop Fire-NOC cycles | One dashboard, auto-reminders. |
| 49 | **PPA lifecycle management** | Template versioning, per-society customization, e-sign, amendment trail, renewal at year 25 | Document vault + workflow. |
| 50 | **Document vault** | Committee resolutions, AOA docs, KYC, site photos, approvals, PPAs, invoices, insurance docs — searchable, audit-trail, access-controlled | Year 1: Google Drive; Year 2: proper DMS (Paperless-ng or similar). |
| 51 | **Insurance management** | Per-asset insurance, public liability, professional indemnity; policy tracking, renewals, claims | Annual renewals + claims workflow. |
| 52 | **HRIS (minimal)** | Team records, contacts, bank details, offer letters, contractor agreements, leave tracker | Year 1: spreadsheet. Year 2: Zoho People or Keka. |
| 53 | **Field-crew management** | Install crews (usually contracted), rates, per-site attendance, payments, safety checks | Ties to Site-survey app (#18). |

### Layer 7 — Integrations (Plumbing Between Everything Above)

| # | Piece | What it does | Notes |
|---|---|---|---|
| 54 | **Payment gateway** | UPI, NACH, bank transfer | Razorpay (best India coverage) + Cashfree backup. |
| 55 | **Banking API** | Auto-reconcile settlements to invoices | ICICI or HDFC corporate API. |
| 56 | **E-sign** | PPA execution, stamp-paper compliant | Digio or Leegality (better India support than DocuSign). |
| 57 | **WhatsApp Business API** | Primary comms channel — society committee, residents, reminders | Gupshup or WhatsGate. |
| 58 | **SMS** | OTP, alerts | MSG91. |
| 59 | **Voice / IVR** | Automated payment reminder calls, hot-transfer to agent | Exotel. |
| 60 | **Email (transactional + marketing)** | Invoices, onboarding, marketing | Keystone Email module (SES under the hood) + Resend for marketing. |
| 61 | **Maps / geocoding** | Coverage map, site-visit routing | MapmyIndia (better India building-level data than Google). |
| 62 | **Weather / irradiance API** | Generation forecasting | Solcast. |
| 63 | **Calendar / scheduling** | Site visits, committee meetings | Cal.com self-hosted. |
| 64 | **Identity / SSO (internal)** | Team logins across all internal tools | Keystone Keycloak. |

### Layer 8 — AI Copilots (YENSI-stack leverage)

| # | Piece | What it does | Notes |
|---|---|---|---|
| 65 | **Bright Roof Concierge** | Society-facing AI: answers billing/generation/maintenance questions, handles reminders, handles disputes across voice + WhatsApp + email | YENSI Concierge spec, domain-customized. |
| 66 | **Sales copilot** | During committee pitch: "society asked X, counter with Y"; mid-meeting proposal regeneration | Phone-based or laptop-based for field sales. |
| 67 | **Ops copilot** | Weekly partner digest, anomaly surfacing, cashflow briefing | Vigil CEO spec, domain-customized. |
| 68 | **Site-survey copilot** | From field photos: estimate roof area, shadow %, structural flags, auto-fill audit form | Reduces Cnu's audit time from 3h to 30min. |
| 69 | **PPA redlining copilot** | When society's lawyer sends markup, auto-suggest defensible counters or flag for human lawyer | Use conservatively; human review mandatory. |
| 70 | **Buyback pricing copilot** | Computes fair-value buyback offer; explains depreciation, opportunity cost, tax implications | Feeds #6 and #14. |
| 71 | **Regulatory watchdog (AI)** | Reads TGSPDCL / TGREDCO / MNRE bulletins, summarizes impact on portfolio | #40 is the feature; this is the engine. |
| 72 | **Society-health scoring** | Predicts default risk per society from payment history, committee stability, sentiment in WhatsApp group (opt-in), bill-review patterns | Year 2. Sensitive — needs governance. |

---

## 3. Build vs buy — opinionated call per item

The bias: **buy commodity, build differentiators.** Everything RESCO-specific has to be built because no SaaS understands our model. Everything else, we rent.

### Buy (SaaS or off-the-shelf)

Accounting (Zoho Books), e-sign (Digio/Leegality), payment gateway (Razorpay), WhatsApp Business API (Gupshup), SMS (MSG91), voice (Exotel), e-invoicing (ClearTax), maps (MapmyIndia), weather (Solcast), calendar (Cal.com), support ticketing (Freshdesk), CMS (Sanity or Keystone), BI (Metabase), HRIS (Zoho People when needed), procurement (Zoho Inventory or ERPNext), vendor shadow analysis (Aurora Solar API as fallback).

### Build (differentiators or RESCO-specific)

Public savings calculator, public buyback calculator, committee proposal generator, society committee portal, digital onboarding workflow, inverter gateway aggregator, net-meter ingestion, billing engine, collections chaser, kill-switch controller, asset register, cap-table + partner ledger, IRR tracker, PPA lifecycle management, ops single-pane-of-glass, partner/investor dashboard, consumption profile analyzer, cashflow forecasting, tariff tracker, regulatory watchdog, site-survey mobile app, shadow analysis integration layer, capacity sizing tool, approvals tracker.

### Leverage from YENSI stack

Keystone (auth, logs, metrics, secrets, email, payments, storage, infra primitives) → skip re-building any of that. Concierge → Bright Roof Concierge, Sales copilot, PPA copilot. Sentinel → production monitoring of everything we build. NC Dev System + Quality Pipeline → autonomous implementation of all the "build" items above. Keeper (multi-country) → Indian accounting & tax layer. Vigil CEO → Ops copilot pattern. Helm (once built) → deployment plane for every service above.

---

## 4. Phasing — match software to business stage

### Phase 0 — Pre-Pilot (now → first PPA signed)

Goal: sign the first PPA with Sri Tirumala Millennium and commission the 18 kW plant.

**In scope (minimum viable):**
1. Marketing website (#1) — single page, "early access" feel
2. Public savings calculator (#2)
3. Enquiry form (#3) → Airtable as CRM
4. Committee proposal generator (#4) — PDF template, manually filled
5. PPA template + e-sign (#13, #49, #56) — Digio account
6. Document vault (#50) — Google Drive with a strict folder convention
7. Field site-survey forms — Google Forms + Drive
8. Capacity sizing — Vijay's existing Excel
9. Accounting (#43) — Zoho Books set up with CA
10. Partner digest (#36 lite) — manual WhatsApp message

**Explicitly not yet:** any society portal, billing engine, monitoring dashboard — we don't have a site generating yet.

### Phase 1 — Pilot Running (first site commissioned)

Goal: invoice Sri Tirumala Millennium correctly every month for 12 months, prove the model works.

**Adds:**
- Inverter gateway (#24) — single-OEM (Growatt), single-site
- Net-meter ingestion (#26) — manual upload of DISCOM bill OK for Month 1
- Billing engine (#27) — minimal, one-site, generates Rs-2-spread invoice
- Invoice + GST e-invoicing (#28)
- Payment collection (#29) — NACH mandate + UPI fallback
- Asset register (#44) — proper DB, every serial entered
- Partner dashboard (#36) — one page, auto-updated weekly

### Phase 2 — Year 1 (5 sites)

Goal: run 5 sites without drowning in spreadsheets.

**Adds:**
- Society committee portal (#10) — view-only first, billing/support later
- CRM proper (#17) — moves off Airtable if pipeline >30
- Digital onboarding workflow (#12)
- Collections chaser (#30) via Concierge
- Maintenance scheduler (#32)
- Ops single-pane (#35)
- Consumption profile analyzer (#37)
- Bright Roof Concierge (#65) — WhatsApp + email channels
- Regulatory watchdog (#40) — weekly digest
- Cap-table + partner ledger (#45)
- Cashflow forecasting (#38)

### Phase 3 — Year 2 (20 sites)

Goal: anomaly detection, predictive maintenance, full BI. No longer feasible to eyeball every site.

**Adds:**
- Inverter gateway expanded to multi-OEM (#24 v2)
- Predictive maintenance (#34)
- BI platform + data warehouse (#41, #42)
- Field site-survey mobile app (#18)
- Site-survey copilot (#68)
- Shadow analysis integration (#19)
- Capacity sizing web tool (#20)
- Approvals tracker (#23)
- PPA redlining copilot (#69)
- Sales copilot (#66)
- Tariff tracker (#39)
- Ops copilot (#67)
- Resident lightweight view (#11)
- Referral program (#8)

### Phase 4 — Year 3+ (50–100 sites)

Goal: operate as a real portfolio with dedicated ops discipline.

**Adds:**
- Edge collector at every site (#25)
- Vendor/procurement system (#21)
- Project management — installation (#22) — proper crew kanban
- Kill switch controller (#31) — with full legal safeguard wrapper
- Buyback request workflow (#14)
- Buyback pricing copilot (#70)
- Committee-change workflow (#16)
- Insurance management (#51)
- Full HRIS + field-crew mgmt (#52, #53)
- Society-health scoring (#72)
- Coverage / social-proof map (#9)

---

## 5. India-specific considerations that change the design

These are not generic SaaS concerns — they're why "buy an off-the-shelf billing platform" won't work.

- **GST on electricity sale vs service.** Electricity is exempt; RESCO service is taxable. Invoice structure must split correctly to avoid GST exposure. CA input mandatory before billing engine go-live.
- **E-invoicing mandate** above ₹5 Cr turnover (currently) — we'll cross it before the 100-site mark. Billing engine must be IRN-ready from Phase 1.
- **Stamp paper for PPAs.** Telangana e-stamping via SHCIL. Digio + Leegality both support this — verify before committing.
- **NACH mandate setup** takes 30–45 days. Start for each society in parallel with PPA signing, not after.
- **TGSPDCL / TGNPDCL net metering approval** is a per-site gate with its own timeline. Approvals tracker (#23) is non-negotiable.
- **Aadhaar e-KYC** for committee office-bearers — Digio supports; bundle into onboarding flow.
- **Telugu language support** in committee portal and all customer-facing docs. Not translation afterthought — needed day one.
- **Data residency:** Indian customer data should stay in Indian data centres. Keystone deployment must be on a Mumbai or Hyderabad region for the Bright Roof tenant when it moves off single-host. (This is where **Helm's** compliance router earns its keep — see `/Users/nrupal/dev/yensi/dev/docs-only/planning/2026-04-22-helm/`.)
- **WhatsApp is the primary channel**, not email. Every workflow that emails should also WhatsApp.
- **Offline-first for field app** (#18). Rooftop connectivity is unreliable.

---

## 6. Unknowns worth deciding now

Decisions that unblock a lot of downstream design — flag and resolve before Phase 1 billing goes live.

1. **PPA tariff mechanism** — flat Rs/kWh for 25 years, or annual escalator (e.g., +3% CPI)? Affects the billing engine and every long-term model.
2. **Buyback formula** — straight-line depreciation vs NPV-based? Fixed table vs formula? Committee-friendly but defensible.
3. **Kill-switch threshold** — how many days late before we can legally disconnect? PPA drafting issue; software enforces.
4. **Society default policy** — reclaim the panels? Re-sell the PPA? Force conversion to CAPEX purchase? Affects the collections engine behaviour.
5. **Committee change default** — PPA signed by Committee A: what approvals are needed when Committee B takes over? Software needs to enforce.
6. **Data ownership** — who owns the generation data: us, society, both? Affects portal access and resident view.
7. **Residents' direct payment (future)** — do we ever bill residents directly (vs society committee)? If yes, scope expands massively.
8. **Commercial / industrial pivot** — does the software stack have to serve C&I clients later, or is residential-society forever our lane? Affects data model choices.
9. **Third-party installers** — do we build install crews in-house or remain an orchestrator of vendor crews? Field-crew tools (#53) scale very differently.
10. **Franchise model (Year 5+)** — if we license the operating platform to other RESCO firms, a lot of the "internal" tools become multi-tenant products. Don't over-engineer for this now, but watch for decisions that would preclude it.

---

## 7. One-sentence summary per phase

- **Phase 0:** a website with a calculator, a PPA template, and a Google Drive.
- **Phase 1:** plus a billing engine that reads one inverter and one net meter and produces one correct GST invoice a month.
- **Phase 2:** plus a society portal, a Concierge, a proper CRM, a cashflow forecast, and a partner dashboard.
- **Phase 3:** plus anomaly detection, a mobile field app, multi-OEM inverter support, and a BI stack.
- **Phase 4:** plus edge devices, procurement, crew management, kill-switch infrastructure, and buyback workflow.

---

## 8. Next step proposals

Three ways to slice this for the next session — pick one:

1. **"Write the Phase 0 spec."** Pick the minimum 10-item Phase-0 list, write a detailed design + build order, and hand it to NC Dev System. Outcome: Bright Roof has a working marketing site + calculator + proposal generator + PPA e-sign in ~4 weeks.
2. **"Answer the 10 open decisions."** Block on § 6 questions with each partner; freeze answers; rewrite this doc v1.0 with decisions baked in so the rest of the build can proceed autonomously.
3. **"Pick one differentiator and go deep."** Write the spec for the single highest-leverage piece (my vote: **the public savings + buyback calculator**, because it is the sales tool that converts cold committees). Build that one module end-to-end to prove the stack before committing to the full roadmap.

Recommendation: **#2 first, then #1.** Decisions before code; code before the next round of decisions.

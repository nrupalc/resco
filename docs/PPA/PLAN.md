# PPA Plan — How We Arrived at the Draft

**Last updated:** 2026-04-22

---

## 1. Business model recap (driving the PPA)

From `docs/project-overview.md`:

- **Entity:** M/s. Bright Roof Power Systems (Partnership Firm, Hyderabad)
- **Model:** RESCO / OPEX — we own, install, operate, and maintain. Customer pays per unit consumed.
- **Customer segment (Year 1):** Residential apartment societies, Hyderabad, 40K+ monthly bill, 800+ units/month
- **First pilot:** Sri Tirumala Millennium, Nacharam, 18 kW on 20 kW sanctioned residential load
- **Pricing stance:** ~20-25% below prevailing grid tariff (roughly Rs 2/unit discount against TSSPDCL slabs)
- **Ownership:** Retained by Bright Roof for the full term (unlike Volt's handover model)
- **Term:** 25-year system life → PPA should be **20-25 years**, with renewal option
- **Core ops features needed:** kill switch, automated billing, NACH mandate, remote monitoring dashboard

## 2. PPA archetype choice

Three standard rooftop PPA models exist in India:

| Model | Who owns | Who pays upfront | Who gets the electricity | Fit for us? |
|---|---|---|---|---|
| **CAPEX** | Customer | Customer (full) | Customer | ❌ — this is just an EPC deal, no PPA |
| **OPEX / RESCO (behind-the-meter)** | RESCO | RESCO | Customer consumes all onsite; RESCO bills per unit | ✅ **Primary** |
| **Open Access / Group Captive** | SPV | Investors | Sold via grid to third parties | ❌ — scale mismatch; different regulatory regime |

We are clearly in **RESCO / behind-the-meter**. This is the MNRE-standard Rooftop Solar PPA archetype (see `references/`).

## 3. Counterparty — this is the tricky part

An apartment building has ~60-200 flats. We cannot sign a PPA with each resident individually — operationally impossible, and default risk is unmanageable. The workable options, in decreasing order of robustness:

1. **Society / AOA / RWA as single counterparty** (single consumer number on the common-area bill, or a dedicated RESCO meter). The society then recovers from residents via maintenance billing. — **Our default.**
2. **Builder / owner (if pre-handover)** — rare at our target maturity of buildings, skip.
3. **Individual residents** with the RWA as billing-and-collection agent — workable as Phase 2 once we have a billing platform, too fragile for v1.

**The PPA is drafted assuming Option 1: one registered AOA/RWA is the customer.**

This has a hard prerequisite we must check *before signing*: the society must be a **registered** body (under the Telangana Societies Registration Act / AP Apartments Act, as applicable) with authority to enter long-term contracts on residents' behalf. If unregistered, we ask them to register first — non-negotiable.

## 4. Source templates we are adapting from

Public, freely-available Indian reference templates:

| Source | What we take | What we change |
|---|---|---|
| **MNRE Model RESCO PPA** (Ministry of New & Renewable Energy) | Overall structure, definitions, standard-form clauses (force majeure, change in law, metering) | Tariff model, term length, handover clause |
| **SECI RESCO tender PPA** | Default / termination / buy-out mechanics, billing & payment security | Scale-down for residential |
| **IREDA template** | Technical performance guarantees, O&M obligations | Adapt for small rooftop |
| **TSSPDCL / Telangana net-metering regulations** | Net-metering mechanics, grid-feed rules, approvals | Jurisdiction-specific — directly cited |
| **Partnership Deed (ours)** | Firm signing authority, registered partner list, address | Embed into execution block |

> **Note on handover clause.** Every standard MNRE/SECI template assumes handover-at-term-end. We **strike this out** and replace with a renewal/continuation clause — that's Bright Roof's core commercial stance. Partners must be aligned that this is the thing we sell against Volt.

## 5. Draft structure (v0.1)

The draft PPA follows this clause order:

1. Parties & recitals
2. Definitions
3. Scope of supply & project description (capacity, location, equipment)
4. Rooftop licence & access
5. Term and extension
6. Design, installation, commissioning, testing
7. Ownership of the System (stays with Bright Roof)
8. Operations, maintenance & monitoring
9. Sale and purchase of solar energy (as-generated, no take-or-pay in v1)
10. Tariff, escalation, billing, payment
11. Metering
12. Payment security (security deposit + NACH mandate + disconnection right)
13. Net-metering, grid coordination, DISCOM approvals
14. Representations & warranties
15. Insurance
16. Force majeure
17. Change in law
18. Default and termination (with buy-out waterfall)
19. End of term — **renewal or removal**, not handover
20. Liability and indemnity
21. Assignment
22. Confidentiality
23. Dispute resolution (mediation → arbitration, seat = Hyderabad)
24. Notices
25. Miscellaneous
26. Schedules (equipment BOQ, tariff schedule, site details, metering plan)

## 6. Open commercial questions (need partner alignment before v1.0)

These are decisions that change commercial terms in the PPA and must be decided by the partners, not by the lawyer:

- [ ] **Term length.** 20y or 25y? (Longer = more lifetime revenue but harder to sell to societies. Recommend **15y with auto-renewal**.)
- [ ] **Tariff escalation.** Flat vs annual escalation (e.g. 3% p.a.)? Grid tariff typically rises ~5% p.a., so flat is the best customer hook but erodes our margin. Recommend **flat for 5y, 3% escalation thereafter** or **fixed discount vs prevailing TSSPDCL slab**.
- [ ] **Take-or-pay?** If society consumption drops (residents install their own solar, AC usage falls), we bear the risk. Standard RESCO practice is **deemed-generation** (they pay for what the system *could have generated*, net of downtime we caused). Recommend **no take-or-pay in v1** — it's hostile to residential buyers. Revisit after 2-3 signings.
- [ ] **Security deposit.** 2 months' estimated bill? 3 months? Refundable at term end.
- [ ] **Buy-out option for society.** Do we allow early buy-out? At what formula? (Standard: NPV of remaining cashflows with a discount, or depreciated capex + margin.) Recommend **yes, after year 7, at 1.3× depreciated book value**.
- [ ] **End-of-term.** Renewal default (rolling 5y) vs. decommissioning at our cost vs. sell-to-society at scrap. Recommend **renewal default with 12-month opt-out notice either way**.
- [ ] **Exclusivity.** Do we lock the society out of adding other solar capacity on the same rooftop for the term? Standard yes — else we lose shading / generation. Recommend **yes, full rooftop exclusivity**.
- [ ] **Responsibility for roof waterproofing / structural issues.** We install non-penetrative ballasted mounts where possible; for penetrative, we pay for any leaks caused for 5 years, then shared.
- [ ] **GST treatment.** 12% on solar equipment, 18% on services — PPA tariff is taxable. Confirm with CA whether RWA can claim input credit (typically no for residential).

## 7. Legal / regulatory checks before v1.0

- [ ] Telangana Societies Registration — confirm AOA can enter 20y+ contracts
- [ ] TSSPDCL net-metering regulations current version — inverter, capacity, metering compliance
- [ ] TGREDCO approvals process — confirm whether PPA needs regulatory filing
- [ ] Stamp duty on PPA in Telangana — typically low for service agreements; confirm
- [ ] Registration requirement? — typically not registrable but needs to be on adequate stamp paper
- [ ] Electricity Act 2003 compliance — we are not a licensee; behind-the-meter RESCO is exempt from distribution licensing as long as we don't use grid wires. Confirm.

## 8. Lawyer brief (what to send to counsel)

When engaging a solar-energy lawyer, give them:

1. This PLAN.md
2. `PPA-Residential-Society-v0.1.md` (this draft)
3. Partnership deed (final PDF in `../Bright Roof Partnership deed final.pdf`)
4. Project overview
5. Specific questions:
   - Is our "retain ownership, no handover" clause enforceable and safe?
   - Stamp duty & registration requirements in Telangana
   - Net-metering consumer-number arrangement (RESCO's meter vs society's meter)
   - Enforceability against a future RWA committee (turnover risk)
   - Kill-switch / disconnection enforceability under Consumer Protection Act
   - Liability caps

## 9. Next actions

1. Partners review `PPA-Residential-Society-v0.1.md` and sign off on the commercial-term questions in §6 above.
2. Nrupal / Vijay to source a Hyderabad solar-energy / commercial-contracts lawyer for a paid review.
3. After lawyer pass, freeze `PPA-Residential-Society-v1.0.md` as the template to pitch with.
4. Build a pre-signing checklist (`PPA-Checklist.md`) covering society registration, rooftop survey, sanctioned load, DISCOM approvals, consumption data.

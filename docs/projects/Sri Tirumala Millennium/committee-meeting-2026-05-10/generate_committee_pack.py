from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[4]
OUT_DIR = Path(__file__).resolve().parent
PDF_PATH = OUT_DIR / "Thirumala-Millennium-Rooftop-Solar-Proposal-and-Consent-Pack.pdf"
LOGO = ROOT / "docs/projects/Sri Tirumala Millennium/03-brand-assets/bright-roof-final-logo-transparent.png"

COMPANY = {
    "name": "M/s. Bright Roof Power Systems",
    "short": "Bright Roof",
    "phone": "+91 93902 10407",
    "email": "support@brightroofpower.com",
    "website": "www.brightroofpower.com",
    "address": "8-3-945/8/18&19 Pancom Business Centre, Ameerpet, Hyderabad, 500073, Telangana",
}

PROJECT = "Sri Tirumala Millennium Association"

NAVY = colors.HexColor("#0E1E4D")
AMBER = colors.HexColor("#F5A524")
TERRACOTTA = colors.HexColor("#C75B3C")
CREAM = colors.HexColor("#FAF6EE")
SLATE = colors.HexColor("#2C3444")
MUTED = colors.HexColor("#6B7280")
LINE = colors.HexColor("#E8EBEF")


def styles():
    base = getSampleStyleSheet()
    base.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=30,
            leading=34,
            textColor=NAVY,
            alignment=TA_LEFT,
            spaceAfter=12,
        )
    )
    base.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=20,
            leading=25,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=8,
        )
    )
    base.add(
        ParagraphStyle(
            name="SubTitle",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            textColor=TERRACOTTA,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    base.add(
        ParagraphStyle(
            name="BodyTextBR",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=SLATE,
            spaceAfter=6,
        )
    )
    base.add(
        ParagraphStyle(
            name="SmallBR",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=MUTED,
            spaceAfter=4,
        )
    )
    base.add(
        ParagraphStyle(
            name="Callout",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            textColor=NAVY,
            backColor=colors.HexColor("#FFF8E7"),
            borderColor=AMBER,
            borderWidth=0.8,
            borderPadding=7,
            spaceBefore=8,
            spaceAfter=10,
        )
    )
    base.add(
        ParagraphStyle(
            name="Centered",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=SLATE,
        )
    )
    base.add(
        ParagraphStyle(
            name="TableHeader",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.white,
            spaceAfter=0,
        )
    )
    return base


S = styles()


def p(text, style="BodyTextBR"):
    return Paragraph(text, S[style])


def hp(text):
    return Paragraph(text, S["TableHeader"])


def bullet(items):
    return ListFlowable(
        [ListItem(p(item), bulletColor=AMBER, leftIndent=8) for item in items],
        bulletType="bullet",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=9,
    )


def table(rows, widths=None, header=True):
    t = Table(rows, colWidths=widths, hAlign="LEFT")
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), SLATE),
    ]
    if header:
        commands += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]
    t.setStyle(TableStyle(commands))
    return t


def page_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 20 * mm, A4[0] - doc.rightMargin, 20 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 8)
    footer = f"{PROJECT} | Rooftop Solar Proposal and Consent Pack | Page {doc.page}"
    canvas.drawRightString(A4[0] - doc.rightMargin, 12 * mm, footer)
    canvas.restoreState()


def logo(width_mm=55):
    img = Image(str(LOGO), width=width_mm * mm, height=(width_mm * 0.668) * mm)
    img.hAlign = "LEFT"
    return img


def signature_table():
    rows = [
        [hp("For the Association"), hp("For Bright Roof Power Systems")],
        [p("Name:"), p("Name:")],
        [p("Designation:"), p("Designation:")],
        [p("Mobile / email:"), p("Mobile / email:")],
        [p("Signature:"), p("Signature:")],
        [p("Date:"), p("Date:")],
    ]
    t = Table(rows, colWidths=[82 * mm, 82 * mm], rowHeights=[12 * mm, 13 * mm, 13 * mm, 13 * mm, 18 * mm, 13 * mm])
    t.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, LINE),
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return t


def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=24 * mm,
    )

    story = []

    story += [
        logo(62),
        Spacer(1, 18 * mm),
        p("Sri Tirumala Millennium Association", "CoverTitle"),
        p("Rooftop Solar Proposal and Consent Pack", "CoverTitle"),
        p("For committee review and preliminary consent to proceed with feasibility assessment.", "BodyTextBR"),
        Spacer(1, 5 * mm),
        p(
            "Customer-facing proposal: Bright Roof installs, owns, operates, and maintains the rooftop solar system at its cost. "
            "The association pays only for solar electricity consumed or offset, with a 10% saving against the agreed electricity-tariff benchmark.",
            "Callout",
        ),
        Spacer(1, 7 * mm),
        table(
            [
                [p("<b>Prepared by</b>"), p(COMPANY["name"])],
                [p("<b>Phone</b>"), p(COMPANY["phone"])],
                [p("<b>Email</b>"), p(COMPANY["email"])],
                [p("<b>Website</b>"), p(COMPANY["website"])],
                [p("<b>Address</b>"), p(COMPANY["address"])],
            ],
            widths=[42 * mm, 122 * mm],
            header=False,
        ),
        Spacer(1, 10 * mm),
        p(
            "This pack is designed for committee review and sign-off to proceed with document sharing, technical survey, "
            "bill review, and final PPA population. It is not a final legally executed PPA until all missing society details, "
            "site schedules, payment details, and legal review are completed.",
            "SmallBR",
        ),
        PageBreak(),
    ]

    story += [
        p("1. Purpose of This Pack", "SectionTitle"),
        p(
            "This pack sets out Bright Roof's rooftop solar proposal and the limited consent requested from the Association at this stage. The requested consent allows Bright Roof to review electricity bills, inspect the site, populate the PPA schedules, and submit a final execution-ready proposal for separate approval.",
        ),
        table(
            [
                [hp("Section"), hp("Purpose")],
                [p("Proposal summary"), p("Explains the no-upfront-cost Bright Roof PPA model.")],
                [p("Site-specific working basis"), p("Records the current assumptions to be verified from bills and site inspection.")],
                [p("Commercial heads"), p("Sets out the draft commercial terms for final PPA population.")],
                [p("Document request checklist"), p("Lists the records required from the Association.")],
                [p("Consent and sign-off"), p("Authorises document sharing, technical survey, and preparation of the final PPA draft.")],
            ],
            widths=[54 * mm, 110 * mm],
        ),
        Spacer(1, 5 * mm),
        p("Current approval requested", "SubTitle"),
        bullet(
            [
                "Permission for Bright Roof to review electricity bills and society records.",
                "Permission for Bright Roof and its technical partners to inspect the rooftop, electrical room, meter location, and cable routes after prior coordination.",
                "Permission for Bright Roof to prepare a populated final PPA draft and technical schedule for further Association review.",
                "Acknowledgement that the proposal is based on no upfront installation cost and a 10% saving against the agreed electricity-tariff benchmark.",
                "Acknowledgement that final PPA execution will require separate approval by the Association.",
            ]
        ),
        PageBreak(),
    ]

    story += [
        p("2. Proposal Summary", "SectionTitle"),
        p(
            "Bright Roof proposes to install a grid-connected rooftop solar photovoltaic system on the Sri Tirumala Millennium rooftop under a Power Purchase Agreement model.",
        ),
        table(
            [
                [hp("Item"), hp("Customer-facing position")],
                [p("Upfront cost to association"), p("Nil. Bright Roof funds the installation.")],
                [p("Ownership"), p("Bright Roof owns the solar system and remains responsible for it.")],
                [p("Billing"), p("The association pays only for solar electricity consumed or offset through the agreed metering arrangement.")],
                [p("Saving"), p("Starting proposal: 10% saving against the agreed electricity-tariff benchmark.")],
                [p("Price protection"), p("If electricity-board tariffs increase later, Bright Roof's solar tariff will follow the agreed PPA formula and review limits, rather than rising in the same way as the board tariff.")],
                [p("Grid connection"), p("Existing TSSPDCL supply continues for balance electricity.")],
                [p("Operations"), p("Bright Roof handles monitoring, cleaning, maintenance, repairs, and system performance review.")],
                [p("Costs not shown"), p("Installer cost, system capex, vendor quote, and Bright Roof internal economics are not presented to the association.")],
            ],
            widths=[52 * mm, 112 * mm],
        ),
        Spacer(1, 5 * mm),
        p(
            "The exact benchmark will be calculated only after reviewing the association's electricity bills and net-metering treatment. "
            "For drafting purposes, the tariff formula should be expressed as: Bright Roof solar tariff = 90% of the agreed benchmark electricity tariff for the solar units consumed or offset.",
            "Callout",
        ),
        PageBreak(),
    ]

    story += [
        p("3. Site-Specific Working Basis", "SectionTitle"),
        p("These are current working assumptions from the Bright Roof project file. They must be verified from bills, site inspection, and DISCOM review before final signature."),
        table(
            [
                [hp("Field"), hp("Working value")],
                [p("Building"), p("Sri Tirumala Millennium, Nacharam, Hyderabad")],
                [p("Proposed system capacity"), p("18 kWp, subject to rooftop survey and DISCOM review")],
                [p("Sanctioned load"), p("20 kW noted in internal project file; verify from latest TSSPDCL bill")],
                [p("Expected generation"), p("1,600-2,000 units per month, subject to final design and site conditions")],
                [p("Proposed modules"), p("30 x 610 Wp bifacial TopCon modules, final make to be confirmed after procurement")],
                [p("Proposed inverter"), p("18 kW on-grid 3-phase inverter, final make to be confirmed after installer quotation")],
                [p("Metering"), p("To be aligned with applicable TSSPDCL net-metering and internal solar metering requirements")],
            ],
            widths=[52 * mm, 112 * mm],
        ),
        Spacer(1, 5 * mm),
        p(
            "Important: the Association is not being asked to approve or pay any final installation cost at this stage. Bright Roof will make its internal investment decision after technical survey and installer quotation.",
            "Callout",
        ),
        PageBreak(),
    ]

    story += [
        p("4. Draft PPA Commercial Heads", "SectionTitle"),
        p("The final PPA should be populated after document collection. The following heads record the current draft position for Association review and legal cleanup."),
        table(
            [
                [hp("Head"), hp("Draft position for final PPA population")],
                [p("Parties"), p("Bright Roof Power Systems and the exact registered association name, to be confirmed from society records.")],
                [p("Premises"), p("Sri Tirumala Millennium rooftop and associated electrical routes, as identified in the technical survey.")],
                [p("Term"), p("Initial term of 10 years, with any extension to be separately reviewed and agreed by the parties.")],
                [p("End of 10-year term"), p("The Association may review continuation, renewal, removal, or purchase of the installation at the then-applicable fair value / market value, as agreed in the final PPA.")],
                [p("Upfront cost"), p("No installation capex payable by the association.")],
                [p("Tariff formula"), p("Solar tariff equal to 90% of the agreed benchmark electricity tariff for the solar units consumed or offset.")],
                [p("Future tariff increases"), p("If the electricity board increases grid tariff in future, the Association should continue to receive solar power under the agreed Bright Roof formula and escalation limits, so the solar tariff does not rise in the same manner as the board tariff.")],
                [p("Benchmark"), p("To be calculated from TSSPDCL bills, tariff slabs, and net-metering treatment.")],
                [p("Maintenance"), p("Bright Roof responsible for routine O&M, cleaning, monitoring, and repairs except for association-caused damage.")],
                [p("Approvals"), p("Association to support required DISCOM, net-metering, access, and internal approvals.")],
                [p("Payment mode"), p("To be finalised after bank details and billing process are confirmed.")],
                [p("Legal review"), p("Final signing version should be reviewed by Telangana counsel before execution.")],
            ],
            widths=[45 * mm, 119 * mm],
        ),
        PageBreak(),
    ]

    story += [
        p("5. Documents Requested From the Association", "SectionTitle"),
        p("The Association is requested to authorise sharing of the following records. These are needed to prepare a populated PPA and technical design."),
        table(
            [
                [hp("Document / information"), hp("Why it is needed"), hp("Status")],
                [p("Exact registered association name"), p("Correct legal counterparty in the PPA"), p("To collect")],
                [p("Registration certificate and number"), p("Confirms legal capacity and registration details"), p("To collect")],
                [p("Bye-laws"), p("Confirms authority and approval process"), p("To collect")],
                [p("Current committee list"), p("Identifies authorised office-bearers"), p("To collect")],
                [p("Last 12 months common-area electricity bills"), p("Consumption, tariff benchmark, and sizing"), p("To collect")],
                [p("Consumer service number(s)"), p("DISCOM and net-metering process"), p("To collect")],
                [p("Sanctioned load record"), p("Confirms system sizing ceiling"), p("To verify")],
                [p("Rooftop and electrical-room access contact"), p("Technical survey coordination"), p("To collect")],
                [p("Waterproofing or leakage history"), p("Mounting design and liability review"), p("To collect")],
            ],
            widths=[58 * mm, 73 * mm, 33 * mm],
        ),
        PageBreak(),
    ]

    story += [
        p("6. Consent Requested From the Association", "SectionTitle"),
        p("The requested sign-off is deliberately narrow. It allows Bright Roof to do the work needed to prepare the final PPA. It does not force the association to proceed with installation until the final PPA is approved and signed."),
        p("Requested approvals", "SubTitle"),
        bullet(
            [
                "Receipt and review of the Bright Roof proposal pack.",
                "Permission to share electricity bills, society records, and committee details with Bright Roof.",
                "Permission for Bright Roof or its technical partners to inspect the rooftop, electrical room, meter location, and cable routes after prior coordination.",
                "Permission for Bright Roof to prepare a populated final PPA draft and technical schedule for further review.",
                "Acknowledgement that the starting commercial proposal is no upfront installation cost and a 10% saving against the agreed electricity-tariff benchmark for solar units consumed or offset.",
                "Acknowledgement that the final PPA should include a 10-year initial term and an end-of-term option for the Association to review continuation or purchase of the installation at then-applicable rates.",
            ]
        ),
        Spacer(1, 4 * mm),
        p("Suggested committee resolution", "SubTitle"),
        p(
            "RESOLVED THAT the Association is open to reviewing a rooftop solar proposal from M/s. Bright Roof Power Systems under a Power Purchase Agreement model where Bright Roof would install, own, operate, and maintain the rooftop solar system at its cost, and the Association would pay only for solar electricity consumed or offset at a tariff designed to provide a 10% saving against the agreed electricity-tariff benchmark, with future tariff movement governed by the agreed PPA formula rather than by automatic electricity-board increases, subject to final bill review, technical survey, legal review, and Association approval.",
        ),
        p(
            "RESOLVED FURTHER THAT the President / Secretary / authorised office-bearer is authorised to share electricity bills, consumer service numbers, sanctioned load records, society registration documents, bye-laws, and other relevant documents with Bright Roof for feasibility assessment and PPA data population.",
        ),
        p(
            "RESOLVED FURTHER THAT Bright Roof and its authorised representatives / technical partners may inspect the rooftop, electrical room, meter location, and related access routes after prior coordination with the Association.",
        ),
        p(
            "RESOLVED FURTHER THAT this resolution is limited to document sharing, technical survey, and preparation of the final PPA draft. Final approval for execution of any PPA shall require separate Association approval as per its bye-laws and applicable law.",
        ),
        PageBreak(),
    ]

    story += [
        p("7. Sign-off Sheet", "SectionTitle"),
        p("Project: Sri Tirumala Millennium rooftop solar PPA review"),
        p("Date: ____________________"),
        p("Association legal name: ________________________________________________"),
        p("Approval forum: Committee / General body / Other: ______________________"),
        p("Resolution number, if any: _____________________________________________"),
        Spacer(1, 3 * mm),
        table(
            [
                [hp("Confirmation"), hp("Initial")],
                [p("The Association has received the Bright Roof proposal pack."), p("")],
                [p("The Association authorises document sharing for bill review and PPA population."), p("")],
                [p("The Association authorises coordinated rooftop and electrical-room survey."), p("")],
                [p("The Association understands this sign-off is not the final PPA execution."), p("")],
                [p("The Association asks Bright Roof to prepare the final populated PPA draft for review."), p("")],
            ],
            widths=[134 * mm, 30 * mm],
        ),
        Spacer(1, 7 * mm),
        signature_table(),
        PageBreak(),
    ]

    story += [
        p("8. Next Steps After Sign-off", "SectionTitle"),
        table(
            [
                [hp("Step"), hp("Owner"), hp("Output")],
                [p("Collect documents and 12 months of electricity bills"), p("Association + Bright Roof representative"), p("Bill and legal data pack")],
                [p("Calculate benchmark tariff and consumption profile"), p("Bright Roof"), p("Commercial worksheet for final PPA")],
                [p("Conduct rooftop and electrical survey"), p("Installer / technical partner"), p("Site survey report and technical feasibility")],
                [p("Get installer quotation and BoM"), p("Bright Roof"), p("Internal capex approval, not for customer presentation")],
                [p("Populate final PPA schedules"), p("Bright Roof + counsel"), p("Final signing draft")],
                [p("Committee / general body approval"), p("Association"), p("Authorised final PPA signature")],
                [p("Start DISCOM / net-metering and implementation"), p("Bright Roof + Association"), p("Commissioning plan")],
            ],
            widths=[58 * mm, 42 * mm, 64 * mm],
        ),
        Spacer(1, 6 * mm),
        p("Company-side fields still needed for a final signable PPA", "SubTitle"),
        bullet(
            [
                "Authorised Bright Roof partner name and designation for signing.",
                "PAN, GST, and partnership registration details, if available and intended to appear in the PPA.",
                "Bank account details for payment schedule / NACH mandate once the bank account is ready.",
                "Final term length, payment due date, security deposit, late-payment wording, and insurance wording after legal review.",
                "Final installer survey report, single-line diagram, metering plan, and technical schedule.",
            ]
        ),
        Spacer(1, 7 * mm),
        KeepTogether(
            [
                p("Bright Roof contact", "SubTitle"),
                table(
                    [
                        [p("<b>Phone</b>"), p(COMPANY["phone"])],
                        [p("<b>Email</b>"), p(COMPANY["email"])],
                        [p("<b>Website</b>"), p(COMPANY["website"])],
                        [p("<b>Address</b>"), p(COMPANY["address"])],
                    ],
                    widths=[35 * mm, 129 * mm],
                    header=False,
                ),
            ]
        ),
    ]

    doc.build(story, onFirstPage=page_header_footer, onLaterPages=page_header_footer)
    print(PDF_PATH)


if __name__ == "__main__":
    build()

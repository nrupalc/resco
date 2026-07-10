import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

type IconName = "rupee" | "wrench" | "tag" | "pin" | "shield" | "monitor" | "people" | "spark";

const phone = "+91 93902 10407";
const email = "support@brightroofpower.com";
const address = "8-3-945/8/18&19 Pancom Business Centre, Ameerpet, Hyderabad, 500073, Telangana";
const legalName = "M/s. Bright Roof Power Systems";
const lastUpdated = "9 May 2026";
const clarityProjectId = "wodqeg8hl6";
const analyticsConsentKey = "bright-roof-analytics-consent";

const proofPoints: Array<{ icon: IconName; title: string; body: string }> = [
  {
    icon: "rupee",
    title: "No upfront system cost",
    body: "Zero capital investment from your society.",
  },
  {
    icon: "wrench",
    title: "Owned and maintained by Bright Roof",
    body: "We install, insure, operate, and maintain. You relax.",
  },
  {
    icon: "tag",
    title: "Minimum 10% bill reduction",
    body: "Your society saves at least 10% against current electricity bills.",
  },
  {
    icon: "pin",
    title: "Local Hyderabad team",
    body: "Local service. Faster response. Always around.",
  },
];

const steps = [
  {
    number: "01",
    title: "Assessment",
    body: "We evaluate your rooftop, current bills, and connected load.",
  },
  {
    number: "02",
    title: "Agreement",
    body: "We sign a simple long-term agreement. Bright Roof handles the system.",
  },
  {
    number: "03",
    title: "Installation",
    body: "We install the system with zero disruption to residents.",
  },
  {
    number: "04",
    title: "Generate & Save",
    body: "You use clean solar power while reducing current bills by at least 10%.",
  },
];

const trustItems: Array<{ icon: IconName; text: string }> = [
  { icon: "shield", text: "High-quality solar modules and inverters" },
  { icon: "spark", text: "Comprehensive insurance and performance guarantee" },
  { icon: "monitor", text: "24/7 system monitoring and proactive maintenance" },
  { icon: "people", text: "Dedicated local support team in Hyderabad" },
];

const faqs = [
  {
    question: "Is installation really free?",
    answer:
      "Yes. Bright Roof pays for the solar system, installation, insurance, monitoring, and maintenance. The society pays only for electricity generated and consumed under the agreement.",
  },
  {
    question: "Who owns the system?",
    answer:
      "Bright Roof owns and operates the system for the agreement period. That is why residents are not left with repair, replacement, or post-payback handover risk.",
  },
  {
    question: "Will the roof be protected?",
    answer:
      "We inspect the rooftop before installation, use appropriate mounting methods, and remain responsible for system upkeep through the operating life.",
  },
  {
    question: "What does the star mean?",
    answer:
      "The star explains the commercial model: the solar panel system has no upfront installation cost for the society, while electricity is billed under the signed agreement.",
  },
];

function Icon({ name }: { name: IconName }) {
  const common = {
    width: 32,
    height: 32,
    viewBox: "0 0 32 32",
    fill: "none",
    xmlns: "http://www.w3.org/2000/svg",
    "aria-hidden": true,
  };

  switch (name) {
    case "rupee":
      return (
        <svg {...common}>
          <path d="M10 8h12M10 13h12M11 8c5.8 0 9 1.7 9 5.1 0 3.2-2.9 5.1-8.7 5.1L21 27" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "wrench":
      return (
        <svg {...common}>
          <path d="M20.5 5.5a7 7 0 0 0-8.2 8.9L5 21.7 10.3 27l7.3-7.3a7 7 0 0 0 8.9-8.2l-4.7 4.7-6-6 4.7-4.7Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "tag":
      return (
        <svg {...common}>
          <path d="M5 17.5 16.5 6H26v9.5L14.5 27 5 17.5Z" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" />
          <path d="M21.5 11.5h.01" stroke="currentColor" strokeWidth="4" strokeLinecap="round" />
        </svg>
      );
    case "pin":
      return (
        <svg {...common}>
          <path d="M24 14c0 6-8 13-8 13S8 20 8 14a8 8 0 1 1 16 0Z" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" />
          <circle cx="16" cy="14" r="3" stroke="currentColor" strokeWidth="2" />
        </svg>
      );
    case "shield":
      return (
        <svg {...common}>
          <path d="M16 4 26 8v7.5C26 22 21.6 26 16 28 10.4 26 6 22 6 15.5V8l10-4Z" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" />
          <path d="m11 16 3.2 3.2L21.5 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "monitor":
      return (
        <svg {...common}>
          <path d="M6 7h20v14H6V7Z" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" />
          <path d="M12 26h8M16 21v5M11 16l3-3 3 3 4-5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "people":
      return (
        <svg {...common}>
          <path d="M12 15a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM20 15a4 4 0 1 0 0-8" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
          <path d="M4 26c.8-4.7 3.5-7 8-7s7.2 2.3 8 7M18 20c3.6.2 5.8 2.2 6.5 6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        </svg>
      );
    case "spark":
      return (
        <svg {...common}>
          <path d="m17 3-2.3 9.2L7 16l7.7 3.8L17 29l2.3-9.2L27 16l-7.7-3.8L17 3Z" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" />
        </svg>
      );
  }
}

function Header() {
  return (
    <header className="site-header">
      <a className="brand" href="/" aria-label="Bright Roof home">
        <img src="/assets/bright-roof-logo-dark.png" alt="" />
        <span className="brand-copy">
          <strong>
            <span className="brand-full">Bright Roof Power Systems</span>
            <span className="brand-short">Bright Roof</span>
          </strong>
          <em>Solar that stays.</em>
        </span>
      </a>
      <nav className="desktop-nav" aria-label="Primary navigation">
        <a href="/#how">How it works</a>
        <a href="/#savings">Savings</a>
        <a href="/#faq">FAQ</a>
      </nav>
      <a className="header-cta" href="/#assessment">Get Assessment</a>
    </header>
  );
}

function Hero() {
  return (
    <section className="hero" id="top">
      <div className="hero-image" aria-hidden="true" />
      <div className="hero-shade" aria-hidden="true" />
      <div className="hero-content">
        <h1>
          Free solar panel installation
          <span className="terms-star" aria-label="terms apply">
            <svg viewBox="0 0 32 32" aria-hidden="true">
              <path d="M16 2.5 19.7 12.3 30 16l-10.3 3.7L16 29.5l-3.7-9.8L2 16l10.3-3.7L16 2.5Z" />
            </svg>
          </span>
        </h1>
        <p>
          Bright Roof installs, owns, and maintains the rooftop solar system.
          Your society gets a minimum 10% reduction from its current electricity bills.
        </p>
        <div className="hero-actions" aria-label="Primary actions">
          <a className="button button-primary" href="#assessment">Schedule rooftop assessment</a>
          <a className="button button-secondary" href={`tel:${phone.replace(/\s/g, "")}`}>Call {phone}</a>
        </div>
      </div>
    </section>
  );
}

function ProofStrip() {
  return (
    <section className="proof-strip" aria-label="Bright Roof promises">
      {proofPoints.map((point) => (
        <article className="proof-item" key={point.title}>
          <div className="icon-circle"><Icon name={point.icon} /></div>
          <div>
            <h2>{point.title}</h2>
            <p>{point.body}</p>
          </div>
        </article>
      ))}
    </section>
  );
}

function HowItWorks() {
  return (
    <section className="section how" id="how">
      <div className="section-heading">
        <div className="amber-rule" />
        <h2>How it works</h2>
        <p>Simple for your society. Seamless from day one.</p>
      </div>
      <div className="steps">
        {steps.map((step, index) => (
          <article className="step" key={step.number}>
            <span>{step.number}</span>
            <h3>{step.title}</h3>
            <p>{step.body}</p>
            {index < steps.length - 1 && <div className="step-arrow" aria-hidden="true">/</div>}
          </article>
        ))}
      </div>
    </section>
  );
}

function Savings() {
  return (
    <section className="savings" id="savings">
      <div className="savings-title">
        <h2>Savings example</h2>
        <p>Typical 100 kW rooftop system</p>
      </div>
      <dl className="savings-grid">
        <div>
          <dt>Current Monthly Bill</dt>
          <dd>Rs. 3,90,000</dd>
          <span>example</span>
        </div>
        <div>
          <dt>Minimum Reduction</dt>
          <dd>10%</dd>
          <span>guaranteed</span>
        </div>
        <div>
          <dt>Minimum Monthly Savings</dt>
          <dd>Rs. 39,000</dd>
          <span>at least</span>
        </div>
        <div>
          <dt>Upfront Installation</dt>
          <dd>Rs. 0</dd>
          <span>society cost</span>
        </div>
      </dl>
      <div className="savings-note">
        <strong>Minimum 10% reduction from what you pay now.</strong>
        <p>Final savings depend on rooftop size, consumption, DISCOM tariff, site assessment, and the signed agreement.</p>
      </div>
    </section>
  );
}

function TrustBand() {
  return (
    <section className="trust-band" aria-label="Built to last">
      <h2>Built to last. Backed by Bright Roof.</h2>
      <div className="trust-items">
        {trustItems.map((item) => (
          <div className="trust-item" key={item.text}>
            <Icon name={item.icon} />
            <span>{item.text}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

function DetailSection() {
  return (
    <section className="detail-section">
      <div>
        <div className="amber-rule" />
        <h2>Solar without a handover cliff.</h2>
      </div>
      <p>
        Many rooftop deals are built around installing equipment and handing
        responsibility back to the society later. Bright Roof keeps the system
        ours, monitors it, maintains it, and stays accountable for the full
        agreement life.
      </p>
      <p>
        That matters for society committees. It keeps solar from becoming
        another maintenance headache, and it gives residents a local team to call
        when something needs attention.
      </p>
    </section>
  );
}

function FAQ() {
  return (
    <section className="faq" id="faq">
      <div className="section-heading">
        <div className="amber-rule" />
        <h2>FAQ</h2>
        <p>Plain answers before your committee meeting.</p>
      </div>
      <div className="faq-list">
        {faqs.map((faq) => (
          <details key={faq.question}>
            <summary>{faq.question}</summary>
            <p>{faq.answer}</p>
          </details>
        ))}
      </div>
    </section>
  );
}

function Assessment() {
  return (
    <section className="assessment" id="assessment">
      <div className="assessment-content">
        <h2>Ready to see what your rooftop can generate?</h2>
        <p>
          Send us a recent electricity bill and rooftop access details. We will
          estimate system size, monthly generation, and likely savings for your
          society.
        </p>
        <div className="assessment-actions">
          <a className="button button-primary" href={`tel:${phone.replace(/\s/g, "")}`}>Call {phone}</a>
          <a className="button button-secondary light" href={`mailto:${email}`}>Email Bright Roof</a>
        </div>
      </div>
      <address>
        <strong>{legalName}</strong>
        <span>{address}</span>
      </address>
    </section>
  );
}

function SiteFooter() {
  return (
    <footer className="site-footer">
      <div className="footer-brand">
        <img src="/assets/bright-roof-logo-dark.png" alt="" />
        <p>Solar that stays.</p>
      </div>
      <div className="footer-details">
        <strong>{legalName}</strong>
        <span>{address}</span>
        <a href={`tel:${phone.replace(/\s/g, "")}`}>{phone}</a>
        <a href={`mailto:${email}`}>{email}</a>
      </div>
      <nav className="footer-links" aria-label="Legal and site links">
        <a href="/privacy">Privacy Policy</a>
        <a href="/data-policy">Data Policy</a>
        <a href="/terms">Terms of Service</a>
        <a href="/sitemap.xml">Sitemap</a>
        <button type="button" onClick={() => window.dispatchEvent(new Event("bright-roof:privacy-choices"))}>
          Privacy choices
        </button>
      </nav>
    </footer>
  );
}

type LegalSection = {
  title: string;
  body: Array<string | string[]>;
};

const legalPages: Record<string, { title: string; intro: string; sections: LegalSection[] }> = {
  "/privacy": {
    title: "Privacy Policy",
    intro:
      "This Privacy Policy explains how Bright Roof handles personal data when you visit this website or contact us about rooftop solar services.",
    sections: [
      {
        title: "Who we are",
        body: [
          `${legalName} is a Hyderabad-based rooftop solar business. You can contact us at ${email}, ${phone}, or ${address}.`,
        ],
      },
      {
        title: "Personal data we may collect",
        body: [
          [
            "Contact details such as name, phone number, email address, society name, and role.",
            "Rooftop and electricity-use details you choose to share, including bills, connected load, approximate monthly units, and site access information.",
            "Website analytics data only if you accept analytics cookies, such as pages visited, browser/device information, approximate location derived from IP address, and interaction data collected through Microsoft Clarity.",
          ],
        ],
      },
      {
        title: "Why we use this data",
        body: [
          [
            "To respond to enquiries and schedule rooftop assessments.",
            "To prepare feasibility estimates, savings examples, proposals, and draft agreements.",
            "To operate, secure, improve, and measure the performance of this website.",
            "To comply with applicable legal, accounting, tax, contractual, and regulatory requirements.",
          ],
        ],
      },
      {
        title: "Analytics and cookies",
        body: [
          `We use Microsoft Clarity only after you accept analytics. Clarity helps us understand page usage and improve the website experience. You can decline analytics or reopen privacy choices from the footer.`,
        ],
      },
      {
        title: "Sharing and processors",
        body: [
          "We may share data with service providers that help us host the website, measure analytics, communicate with you, prepare documents, or operate the business. We do not sell personal data.",
        ],
      },
      {
        title: "Retention",
        body: [
          "Enquiry data is kept only as long as needed for sales follow-up, project evaluation, legal compliance, dispute handling, or legitimate business records. Contract, billing, and statutory records may be retained for longer where required by law.",
        ],
      },
      {
        title: "Your choices and rights",
        body: [
          "You may contact us to request access, correction, deletion, withdrawal of consent, or grievance resolution in relation to personal data we hold about you, subject to applicable law and contractual record requirements.",
        ],
      },
      {
        title: "Grievance contact",
        body: [
          `For privacy requests or grievances, contact Bright Roof at ${email} or ${phone}. We will review requests and respond through the contact details you provide.`,
        ],
      },
    ],
  },
  "/data-policy": {
    title: "Data Policy",
    intro:
      "This Data Policy describes the practical safeguards and operating rules Bright Roof follows for website, enquiry, proposal, and project data.",
    sections: [
      {
        title: "Data minimisation",
        body: [
          "We ask only for information reasonably needed to assess a rooftop, estimate solar generation, contact a society or homeowner, prepare a proposal, or support an agreement.",
        ],
      },
      {
        title: "Data categories",
        body: [
          [
            "Website data: consent status, analytics events after consent, browser/device details, and page interactions.",
            "Enquiry data: contact information, society details, address/location context, rooftop details, and electricity bill information.",
            "Project data: site assessment notes, proposal figures, contract drafts, billing records, maintenance records, and support history.",
          ],
        ],
      },
      {
        title: "Security practices",
        body: [
          "We use access controls, limited internal access, service-provider review, backups where appropriate, and reasonable technical and organisational safeguards for business records. Sensitive operational or identity documents should not be sent unless requested through an agreed channel.",
        ],
      },
      {
        title: "Access control",
        body: [
          "Access to enquiry, proposal, contract, billing, and maintenance data is limited to partners, employees, consultants, and service providers who need it for Bright Roof work.",
        ],
      },
      {
        title: "Data transfers",
        body: [
          "Some service providers may process data outside Telangana or India, depending on hosting, email, analytics, document, or cloud tools used. We aim to use providers that maintain appropriate security and confidentiality commitments.",
        ],
      },
      {
        title: "Incident handling",
        body: [
          "If we become aware of a material data-security issue affecting personal data, we will investigate, take containment steps, and provide notices required by applicable law.",
        ],
      },
      {
        title: "Future apps",
        body: [
          "Calculator, PPA generation, accounting, and customer-service apps should inherit this policy baseline but may need separate notices, consent flows, role-based access controls, audit logs, and retention schedules before launch.",
        ],
      },
    ],
  },
  "/terms": {
    title: "Terms of Service",
    intro:
      "These Terms govern use of the Bright Roof website. Project-specific proposals, PPAs, invoices, and signed contracts will control over website content where they differ.",
    sections: [
      {
        title: "Website purpose",
        body: [
          "This website provides general information about Bright Roof rooftop solar services. It does not by itself create a binding installation, supply, finance, maintenance, or power purchase agreement.",
        ],
      },
      {
        title: "Estimates and savings examples",
        body: [
          "Generation, tariff, and savings examples are indicative. Bright Roof's public offer is structured around a minimum 10% reduction from the society's current electricity bills, subject to rooftop assessment, consumption pattern, DISCOM tariff, outages, maintenance conditions, and signed contract terms.",
        ],
      },
      {
        title: "Free installation star",
        body: [
          "The star next to free solar panel installation means the society does not pay upfront system installation cost under the Bright Roof ownership model. Electricity supply, minimum bill-reduction terms, tariff structure, tenure, maintenance, payment, site, and termination terms are governed by the signed agreement.",
        ],
      },
      {
        title: "Permitted use",
        body: [
          "You may use the site to learn about Bright Roof and contact us. Do not misuse the website, attempt unauthorised access, interfere with security, scrape at unreasonable volume, or submit false or unlawful information.",
        ],
      },
      {
        title: "No professional advice",
        body: [
          "Website content is not legal, tax, engineering, electrical-safety, financial, or regulatory advice. Formal project decisions should be based on site assessment, technical design, statutory approvals where applicable, and signed documents.",
        ],
      },
      {
        title: "Intellectual property",
        body: [
          "The Bright Roof name, logo, website design, images, copy, and brand materials belong to Bright Roof or its licensors. You may not reuse them commercially without written permission.",
        ],
      },
      {
        title: "Liability",
        body: [
          "The website is provided on an informational basis. To the extent permitted by law, Bright Roof is not liable for indirect, incidental, consequential, or reliance losses arising from use of this website.",
        ],
      },
      {
        title: "Governing law",
        body: [
          "These Terms are governed by the laws of India. Courts and competent forums in Hyderabad, Telangana will have jurisdiction, subject to any mandatory law or signed contract term that applies.",
        ],
      },
      {
        title: "Contact",
        body: [
          `For website or service questions, contact ${legalName} at ${email}, ${phone}, or ${address}.`,
        ],
      },
    ],
  },
};

function setPageMeta(title: string, description: string, path: string) {
  document.title = `${title} | Bright Roof Power Systems`;

  const descriptionTag = document.querySelector<HTMLMetaElement>('meta[name="description"]');
  if (descriptionTag) {
    descriptionTag.content = description;
  }

  const canonical = document.querySelector<HTMLLinkElement>('link[rel="canonical"]');
  if (canonical) {
    canonical.href = `https://www.brightroofpower.com${path === "/" ? "/" : path}`;
  }
}

function LegalPage({ page }: { page: (typeof legalPages)[string] }) {
  return (
    <>
      <main className="legal-page">
        <div className="legal-hero">
          <div className="amber-rule" />
          <h1>{page.title}</h1>
          <p>{page.intro}</p>
          <span>Last updated: {lastUpdated}</span>
        </div>
        <div className="legal-content">
          {page.sections.map((section) => (
            <section key={section.title}>
              <h2>{section.title}</h2>
              {section.body.map((item, index) =>
                Array.isArray(item) ? (
                  <ul key={index}>
                    {item.map((point) => (
                      <li key={point}>{point}</li>
                    ))}
                  </ul>
                ) : (
                  <p key={index}>{item}</p>
                ),
              )}
            </section>
          ))}
        </div>
      </main>
      <SiteFooter />
    </>
  );
}

function loadClarity() {
  const win = window as typeof window & {
    clarity?: (...args: unknown[]) => void;
  };

  if (win.clarity || document.querySelector(`script[src*="clarity.ms/tag/${clarityProjectId}"]`)) {
    return;
  }

  win.clarity = function clarity(...args: unknown[]) {
    (win.clarity as typeof win.clarity & { q?: unknown[] }).q =
      (win.clarity as typeof win.clarity & { q?: unknown[] }).q || [];
    (win.clarity as typeof win.clarity & { q?: unknown[] }).q?.push(args);
  };

  const script = document.createElement("script");
  script.async = true;
  script.src = `https://www.clarity.ms/tag/${clarityProjectId}`;
  document.head.appendChild(script);
}

function CookieConsent() {
  const [choice, setChoice] = useState(() => localStorage.getItem(analyticsConsentKey));

  useEffect(() => {
    if (choice === "accepted") {
      loadClarity();
    }
  }, [choice]);

  useEffect(() => {
    const reopen = () => setChoice(null);
    window.addEventListener("bright-roof:privacy-choices", reopen);
    return () => window.removeEventListener("bright-roof:privacy-choices", reopen);
  }, []);

  if (choice) {
    return null;
  }

  const saveChoice = (value: "accepted" | "declined") => {
    localStorage.setItem(analyticsConsentKey, value);
    setChoice(value);
  };

  return (
    <aside className="cookie-banner" aria-label="Privacy choices">
      <div>
        <strong>Privacy choices</strong>
        <p>
          We use optional analytics to understand how this site is used. Clarity
          loads only if you accept.
        </p>
      </div>
      <div className="cookie-actions">
        <button type="button" onClick={() => saveChoice("declined")}>Decline</button>
        <button type="button" onClick={() => saveChoice("accepted")}>Accept analytics</button>
      </div>
    </aside>
  );
}

function App() {
  const path = window.location.pathname.replace(/\/$/, "") || "/";
  const legalPage = legalPages[path];

  useEffect(() => {
    if (legalPage) {
      setPageMeta(legalPage.title, legalPage.intro, path);
      return;
    }

    setPageMeta(
      "Free Solar Panel Installation",
      "Bright Roof installs, owns, and maintains rooftop solar systems for Hyderabad apartment societies, with a minimum 10% reduction from current electricity bills under the signed agreement.",
      "/",
    );
  }, [legalPage, path]);

  if (legalPage) {
    return (
      <>
        <Header />
        <LegalPage page={legalPage} />
        <CookieConsent />
      </>
    );
  }

  return (
    <>
      <Header />
      <main>
        <Hero />
        <ProofStrip />
        <HowItWorks />
        <Savings />
        <TrustBand />
        <DetailSection />
        <FAQ />
        <Assessment />
      </main>
      <SiteFooter />
      <CookieConsent />
    </>
  );
}

createRoot(document.getElementById("root")!).render(<App />);

# CLAUDE.md — oxygenbioinnovations.com

Context and standing rules for any work on this repository. Read fully before editing any page.

---

## 1. What this site is

Marketing and credibility site for Oxygen Bioinnovations Private Limited (OBI), a DPIIT-recognised
deep-tech food biotechnology startup, CIN U72100TZ2026PTC038160, DPIIT DIPP258270, incubated at
TBI-DETI@ACE, Hosur, Tamil Nadu.

Static HTML/CSS, deployed on Vercel.

The company is pre-revenue and pre-launch. There is no FSSAI manufacturing licence. Nothing on this
site may read as if a product is for sale, available, or licensed.

## 2. Primary job of the rebuild

The existing site publishes information that is intended to be covered by a patent application that
has not yet been filed. Removing that material is the highest-priority objective of this work and
overrides every aesthetic or copywriting consideration.

Secondary objectives, in order:

1. Correct factual and compliance errors in existing copy (see section 6)
2. Reduce nine pages to six (see section 5)
3. Move visual identity onto the company document palette (see section 7)

## 3. DISCLOSURE BOUNDARY — non-negotiable

This is the most important section in this file. It applies to page copy, headings, alt text, meta
descriptions, Open Graph tags, JSON-LD, image filenames, code comments, and commit messages.

### 3a. NEVER publish

Do not write these, do not leave them in place if found, do not reintroduce them in rewritten copy:

- **Any named grain substrate.** No ragi, finger millet, Eleusine coracana, black rice, Karuppu
  Kavuni, KK, heirloom rice, or GI-tag provenance story. No cyanidin-3-glucoside or anthocyanin
  claims tied to a substrate.
- **Any legume or co-substrate**, named or hinted (horse gram, bengal gram, pottukadalai, urad dal).
- **Process staging language**: "multi-stage", "phase transitions", "controlled cycle", "defined
  phases", or any description of the fermentation as having sequence or structure.
- **Enzyme mechanism attributed to the process**: phytase, amylase, protease, phytate hydrolysis,
  phytic acid degradation, mineral liberation. Phytic acid may not be presented as a problem this
  company solves.
- **"Endogenous synthesis of metabolites during fermentation"** or any paraphrase. This single
  sentence is the core claim concept.
- **Organism identity at any level**, including generic phrasings such as "grain-adapted LAB
  strains", "proprietary strains", "defined consortium", "wild isolates".
- **Named metabolites**: GABA, EPS, exopolysaccharides, bacteriocins, bioactive peptides,
  liberated phenolics.
- **Any number attached to process**: temperature, pH, hold time, ratio, inoculum percentage,
  working volume, yield.
- **Supplier or vendor names** of any kind.
- **Named analytical techniques.** Refer to "instrumental analysis" only.

### 3a-i. Banned term list (literal)

These exact strings must not appear anywhere in the repository: page copy, headings, alt text,
meta descriptions, Open Graph and Twitter tags, JSON-LD, image filenames, CSS class names, HTML
comments, or commit messages.

    phytic          phytate         phytase
    amylase         protease        cellulase
    LAB             lactic acid bacteria   lactobacill
    plantarum       pediococcus
    leuconostoc     weissella       bacillus
    multi-stage     multi stage     controlled fermentation
    phase transition                defined phase
    ragi            finger millet   eleusine
    kavuni          karuppu         black rice      heirloom rice
    anthocyan       cyanidin
    postbiotic
    horse gram      bengal gram     pottukadalai    urad
    GABA            exopolysaccharide       bacteriocin
    bioactive peptide

"Mineral bioavailability" and "nutrient absorption" are permitted as outcomes, provided no
mechanism, enzyme, organism, or anti-nutrient is named as the means.

### 3b. Permitted

- "Indigenous Indian grains" as a category only. Never a species, never a variety.
- "Fermentation" as a bare category word, never attached to a mechanism, stage, or outcome claim.
- Mushroom species by name: Hericium erinaceus (Lion's Mane), Cordyceps militaris, Ganoderma
  lucidum (Reishi). These carry no novelty and will appear on a label. Do not place them in the
  same paragraph as any fermentation reference.
- Ambient stability, stated as a product property. Never as a method or a mechanism.
- Company facts: CIN, DPIIT number, incubation, knowledge partner, team.

### 3c. Hold until further notice

- The word **"postbiotic"** and all variants.

### 3d. If in doubt

Leave it out and flag it in your summary. An omission costs nothing. A disclosure is irreversible.

## 4. Delete outright

`ingredients.html` and every inbound link to it, including nav, dropdown menus, footer quick links,
and the "View Full Ingredient Index" CTA on the science page. Nothing on this page survives the
disclosure boundary. Do not attempt to rewrite it.

Add a Vercel redirect from `/ingredients` and `/ingredients.html` to `/platform` so existing
inbound links and search results do not 404.

## 5. Target structure

| New page | Absorbs | Purpose |
|---|---|---|
| `index.html` | index | Positioning, credibility, three SKUs as working titles, waitlist |
| `platform.html` | science + ingredients + problem | Problem framing and capability, non-enabling |
| `about.html` | about + investors | Company, team, incubation, partners, traction |
| `careers.html` | careers | Talent |
| `updates.html` | blog | Build-in-public log, the only page that changes often |
| `contact.html` | contact | General, investor, and partnership enquiry routing |

Keep `privacy.html`, `terms.html`, `faq.html` as legal/support pages outside the main nav.

Set up redirects for every retired URL.

## 6. Copy corrections required

- **Factual error.** Current science and ingredients copy states that hericenones cross the
  blood-brain barrier. They do not. Erinacines are the fraction with blood-brain barrier evidence;
  hericenones are NGF-active in vitro. Correct or remove the claim.
- **Competitor disparagement.** The homepage comparison table asserts the industry has "Zero
  Efficacy Data" and "No Transparency" and uses "Highly Processed Flours", "Generic or Unverified
  Method". Remove the competitor column entirely. State OBI's own standard as a plain list.
- **Unsupportable promise.** The waitlist offers "access to our clinical study results". No clinical
  study exists or is protocolled. Remove.
- **Health data collection.** The waitlist form collects a Primary Health Goal field. Either remove
  the field or confirm the privacy policy explicitly covers collection of health-related personal
  data. Do not ship it uncovered.
- **Register mismatch.** Mechanism copy is written in product voice while the footer disclaimer says
  pre-commercial R&D. Rewrite all mechanism and benefit copy into research voice: what is being
  investigated, not what the product does.
- **Remove unverifiable counters.** Phytic acid reduction percentage, SOP counts, layer counts,
  standardisation figures such as calcium per 100g.

Retain and keep prominent: the footer disclaimer that products are pre-commercial R&D and claims
have not been evaluated by FSSAI. Keep "FSSAI licence application to be filed" honest. Never imply
a licence is held.

## 7. Visual direction

Move the site onto the OBI document palette so the site, the DPR, the pitch decks and grant
submissions read as one identity.

- Primary: navy `#1F3864`
- Support: ice blue `#DCE6F1`
- Light-first, not the current dark treatment
- One accent colour maximum
- Generous whitespace, larger type scale, fewer sections per page
- Real lab and team photography over abstract gradients and stock

Remove entirely: the scrolling ticker, the scroll-percentage counters, the large numbered section
chrome (01 / 02 / 03 markers), and the animated stat counters. The current density reads as
compensating. Restraint reads as confidence.

Accessibility: WCAG AA contrast minimum, semantic headings in order, alt text on every image, visible
focus states, keyboard-navigable menus.

## 8. Audience weighting

Primary register is grant evaluators and investors. Consumers get one strong waitlist section on the
home page, not a brand skin across the site. Talent gets one page.

Write for a reader who is technically literate, sceptical, and short on time.

## 9. Working style

- Propose the page plan before writing full copy. Confirm direction first.
- No em-dashes anywhere in site copy. Use colons, semicolons, or plain punctuation.
- Work one page at a time. Start with `platform.html`, where the disclosure damage is concentrated.
- After each page, list explicitly what was removed under section 3 so it can be checked.
- Do not deploy. Leave changes for review and manual commit.
- Never create a blog post, article, update, or changelog entry with a date earlier than the date
  it is actually written. Do not backdate content under any circumstance.
- Never write meta-commentary about what the company is withholding, redacting, or keeping
  confidential ahead of patent filing. Describing the existence of withheld material is itself a
  signpost. Say nothing rather than saying that something is unsaid.
- Do not invent content. If a page needs material that does not exist, leave a TODO and report it.
  Do not write placeholder articles, fake milestones, or speculative dates.
- Do not publish forward-looking dates unless given one explicitly. Never leave a date in the past
  labelled as upcoming.

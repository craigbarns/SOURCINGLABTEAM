---
name: rfq-generator
description: Generates professional Request for Quotation (RFQ) packages for industrial sourcing. Collects product specifications, commercial terms, and quality requirements, then produces a ready-to-send RFQ document (Word/DOCX) with a cover letter, technical spec sheet, and compliance checklist.
---

# RFQ Generator

This skill guides the generation of a professional, complete, and unambiguous RFQ (Request for Quotation) package for industrial suppliers.

## Mandatory Workflow

Follow these steps **in order**. Do not skip Step 1.

### Step 1: Information Gathering (Interview)

Before generating anything, collect the following from the user. If any item is missing, ask for it explicitly. Do not invent product data.

**A. Product Identification**
- Product name / internal reference
- Target market / country of destination
- Link to drawings (PDF/DWG/STEP) or photos

**B. Technical Specifications**
- Materials (grade, standards: e.g., ASTM, EN, GB)
- Dimensions and tolerances (critical vs. general)
- Surface treatment / finish
- Weight (net/unit)
- Packing requirements (carton specs, pallet, labeling)

**C. Commercial Requirements**
- Estimated annual volume + initial order quantity (MOQ target)
- Target unit price (if known, else "ask supplier to quote")
- Incoterms (e.g., FOB, EXW, CIF, DDP) + port/destination
- Payment terms (e.g., T/T 30/70, L/C at sight)
- Required lead time (sample + production)
- Validity period of the quotation (default: 30 days)

**D. Quality & Compliance**
- Required certifications (e.g., ISO 9001, CE, RoHS, REACH, FDA, UL)
- Inspection standards (AQL level, third-party inspection allowed?)
- Sample policy (free sample? who pays shipping?)

### Step 2: Draft the RFQ

1. Read the template at the skill directory: `templates/rfq-template.md`
2. Fill the template with the collected data. Use `[TBD]` for anything the user has not provided — never fabricate.
3. Write the RFQ in **English** by default (international standard for sourcing), unless the user requests another language.
4. Apply house style: neutral tone, numbered sections, no marketing language.

### Step 3: Generate the Document

1. Use the `docx_tool` (computercontroller extension) to create a Word file:
   - File name convention: `RFQ_<ProductRef>_<YYYYMMDD>.docx`
   - Save to the user's working directory under `rfq/`
2. Use `structured` mode with proper heading levels (Heading1 for main sections, Heading2 for subsections).
3. Include the cover letter, spec table, and compliance checklist from the template.

### Step 4: Self-Verification (Before Delivery)

Before presenting the final RFQ to the user, verify:
- [ ] Every technical field is either filled or marked `[TBD]` — no invented data
- [ ] Incoterms, payment terms, and lead time are stated explicitly
- [ ] A response deadline is included
- [ ] File opens correctly and section numbering is coherent
- [ ] No confidential internal information (e.g., internal cost targets) is exposed to suppliers — remove internal margin/target-price columns unless flagged "INTERNAL"

### Step 5: Delivery

Present to the user:
1. The file path of the generated `.docx`
2. A short summary of what is included
3. A list of any `[TBD]` items the user should complete before sending
4. Ask: "Souhaitez-vous ajuster des termes (Incoterms, paiement, volumes) avant envoi ?"

## Rules

- **Never invent** technical data, certifications, or prices.
- **Always include** a deadline for supplier response.
- **Always separate** internal information from supplier-facing content.
- Keep the document under 4 pages when possible; attach drawings separately and reference them by filename.

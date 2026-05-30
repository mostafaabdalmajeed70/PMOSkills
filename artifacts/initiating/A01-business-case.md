---
artifact_id: A01
name: Business Case
version: 1.0.0
status: "Definition · Active"
category: Initiating
authority: "PMBOK8 Guide §1.2 · Process Groups Practice Guide §3.1 · Standard §3 (Value Principle)"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §1.2 · Figure 1-4"
required_by_skills:
  - SKL-02-01
  - SKL-06-01
created_by_skills:
  - SKL-02-01
file_path: artifacts/initiating/A01-business-case.md
---

# A01 — Business Case
**Artifact ID:** A01  
**Artifact Name:** Business Case  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §1.2 · Process Groups Practice Guide §3.1 · Standard §3 (Value Principle)  
**Source Type:** PMI-derived  
**File Path:** `artifacts/initiating/A01-business-case.md`

---

## Definition

A01 is the pre-authorization document that provides the justification for undertaking a project. It analyzes the problem or opportunity, evaluates alternative solutions, and recommends the preferred option with its expected benefits, costs, and risks. It is the primary strategic input to the Project Charter (A04) and the Benefits Record (A02).

**PMI Source:** PMBOK8 Guide §1.2 — Project Business Documents; Process Groups Practice Guide §3.1.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Initiating |
| **Type** | Pre-authorization justification document |
| **Lifecycle** | Created before project authorization · Referenced in Initiating · Reviewed at phase gates · Closed at project close |
| **Baseline?** | Business case is baselined at authorization; changes require sponsor review |
| **Ownership** | Sponsor / Portfolio / Business Owner |

---

## Purpose

- Justify the investment of organizational resources in the project
- Document the problem or opportunity being addressed
- Evaluate alternative options including a "do nothing" baseline
- Define expected benefits, costs, ROI, and payback period
- Establish success criteria for benefits realization
- Provide strategic alignment evidence (portfolio / program fit)
- Serve as the authorization trigger for A04 Project Charter

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Executive Summary | 1-page summary of problem, recommended solution, and key financials | Sponsor / Business Owner |
| §2 Problem / Opportunity Statement | Clear definition of what business problem or opportunity the project addresses | Sponsor |
| §3 Strategic Alignment | Link to organizational strategy, portfolio, or program | Sponsor / PMO |
| §4 Options Analysis | ≥3 options evaluated: do nothing, minimum viable, preferred solution | PM / Business Analyst |
| §5 Recommended Option | Detailed description of the recommended approach | PM / Sponsor |
| §6 Benefits Analysis | Quantified benefits: financial (ROI, NPV, IRR, payback) and non-financial | PM / Finance |
| §7 Cost Estimate | High-level cost estimate for recommended option (capital + operational) | PM / Finance |
| §8 Risk Summary | Top risks to benefits realization (detailed in A19) | PM |
| §9 Assumptions | Key assumptions on which benefits projections rest | PM / Sponsor |
| §10 Benefits Realization Timeline | When benefits are expected to be realized (input to A02) | PM / Sponsor |
| §11 Approval and Signatures | Business owner / sponsor authorization | Sponsor |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| Problem / Opportunity | Clear statement of what the project solves or captures | Mandatory |
| Strategic Alignment | Link to strategic objective or portfolio goal | Mandatory |
| Options Analyzed | ≥2 alternatives documented and compared | Mandatory |
| Recommended Option | Single preferred solution with rationale | Mandatory |
| Financial Metrics | At least one: ROI / NPV / IRR / payback period | Mandatory |
| Expected Benefits | Quantified (financial and/or non-financial) | Mandatory |
| Cost Estimate | Order-of-magnitude or preliminary estimate | Mandatory |
| Approval Signature | Authorized sponsor signature | Mandatory |
| Risk Summary | ≥1 top risk to benefits realization | Recommended |
| Benefits Timeline | Expected benefit realization dates | Recommended |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| Strategic plan / portfolio registry | Portfolio / Exec | Strategic context and alignment evidence |
| A05 — Context Register (EEF/OPA) | SKL-01-02 | Org policies, market data, historical costs |
| Market / feasibility research | Business analyst | Problem / opportunity quantification |
| Financial models | Finance / PMO | NPV, ROI, payback calculation |
| Expert judgment | Sponsor, SMEs, PMO | Options evaluation |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Justification and strategic alignment | A04 — Project Charter |
| Benefits metrics and timeline | A02 — Benefits Record |
| Cost and risk summary | A04 §7 (Budget) · A19 (Risk Register) |
| Approved investment decision | Portfolio / governance body |

---

## Scope Boundaries

| In Scope | Out of Scope |
|---|---|
| Pre-authorization business justification | Detailed project scope definition (see A08) |
| High-level options analysis | Technical design or architecture decisions |
| Financial case for the project | Detailed cost estimates (see A16) |
| Benefits expected from the project | Benefits measurement tracking (see A02) |

---

## Financial Metrics Reference

| Metric | Definition | Notes |
|---|---|---|
| **ROI** | (Net Benefit / Total Cost) × 100 | Simple return measure |
| **NPV** | Sum of discounted future cash flows minus initial investment | Preferred for multi-year projects |
| **IRR** | Discount rate at which NPV = 0 | Compare against cost of capital |
| **Payback Period** | Time to recover initial investment from net cash flows | Simple liquidity measure |
| **BCR** | Benefit-Cost Ratio = PV of benefits / PV of costs | BCR > 1 = viable |

---

## Quality Criteria

- Business case exists and is approved before A04 Project Charter is signed
- ≥2 alternatives evaluated including a "do nothing" option
- Financial metrics are calculated (not estimated verbally)
- Benefits are quantified — not described only qualitatively
- Strategic alignment is traced to a named organizational objective
- Risk summary identifies the top threats to benefits realization
- Business case reviewed and confirmed still valid at each phase gate

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A04 — Project Charter | A01 is the primary authorization trigger for A04 |
| A02 — Benefits Record | A01 §10 (Benefits Timeline) seeds A02 |
| A05 — Context Register | EEF/OPA provide inputs to A01 options and cost analysis |
| A19 — Risk Register | A01 risk summary seeds initial risk register |
| A16 — Budget | A01 cost estimate is the pre-authorization funding reference |
| A27 — Closure Record | Benefits realized vs. A01 projections reported at closure |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §1.2 | Project Business Documents — Business Case |
| PMBOK8 Guide §1.2.1 | Business case content and purpose |
| Process Groups PG §3.1 | Develop Project Charter — Business Case as input |
| PMBOK8 Standard §3 | Value principle — projects exist to deliver value |
| PMI Lexicon | "Business Case" — documented economic feasibility study |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 1 | Initial definition — Phase B1 |

---

*Owner: Business Owner / Sponsor*  
*Change Control: Business case changes require sponsor and portfolio authorization (T3 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 1*

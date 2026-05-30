---
artifact_id: A11
name: Procurement Management Plan
version: 1.0.0
status: "Definition · Active"
category: Procurement
authority: "PMBOK8 Guide §2.6 · Process Groups PG §4.9 · Standard §3 (Stewardship)"
source_type: PMI-derived
pmbok8_anchor: "PMBOK8 Guide §2.6 · Plan Procurement Management"
required_by_skills:
  - SKL-04-09
created_by_skills:
  - SKL-03-11
file_path: artifacts/extended-procurement/A11-procurement-management-plan.md
---

# A11 — Procurement Management Plan
**Artifact ID:** A11  
**Artifact Name:** Procurement Management Plan  
**Version:** 1.0.0  
**Status:** Definition · Active  
**Authority:** PMBOK8 Guide §2.6 · Process Groups PG §4.9 (Plan Procurement Management) · Standard §3 (Stewardship)  
**Source Type:** PMI-derived  
**File Path:** `artifacts/extended-procurement/A11-procurement-management-plan.md`

---

## Definition

A11 defines how the project team will acquire goods, services, or results from outside the organization. It documents what will be procured, the procurement approach, contract types, vendor selection criteria, and contract management procedures.

**PMI Source:** PMBOK8 Guide §2.6 — Project Work Performance Domain; PG §4.9 — Plan Procurement Management.

---

## Artifact Type

| Field | Value |
|---|---|
| **Category** | Procurement |
| **Type** | Subsidiary plan (component of A06 PM Plan) |
| **Lifecycle** | Created in Planning · Applied in Executing (Conduct Procurements) · Monitored in M&C |
| **Baseline?** | Yes — procurement approach is baselined at planning approval |
| **Ownership** | Project Manager · Procurement Officer |

---

## Purpose

- Identify what will be procured vs. built in-house (make-or-buy analysis)
- Define the procurement approach, contract types, and authority thresholds
- Establish the source selection process and evaluation criteria
- Define vendor management and contract administration responsibilities
- Specify how risks are allocated between buyer and seller
- Comply with organizational procurement policies and legal requirements

---

## Sections

| Section | Content | Populated By |
|---|---|---|
| §1 Make-or-Buy Analysis | What is procured vs. delivered in-house with rationale | SKL-03-11 |
| §2 Procurement List | All items/services to be procured with description and priority | SKL-03-11 |
| §3 Contract Types | Type per procurement: FFP, T&M, CPFF, CPIF | SKL-03-11 |
| §4 Source Selection Criteria | Evaluation factors and weights for vendor selection | SKL-03-11 |
| §5 Procurement Timeline | Key procurement milestones | SKL-03-11 |
| §6 Contract Administration | How contracts are managed, monitored, and closed | SKL-04-09 |
| §7 Risk Allocation | How procurement risks are shared between buyer and seller | SKL-03-11 |
| §8 Procurement Authority | Who can authorize and sign contracts (thresholds) | SKL-03-11 |

---

## Contract Types Reference

| Type | Description | Risk Bearer |
|---|---|---|
| **FFP** | Firm Fixed Price — price set at contract signing | Seller |
| **FP-EPA** | Fixed Price with Economic Price Adjustment | Shared |
| **T&M** | Time and Materials — pay per hour + materials | Buyer |
| **CPFF** | Cost Plus Fixed Fee | Buyer |
| **CPIF** | Cost Plus Incentive Fee | Shared |
| **CPAF** | Cost Plus Award Fee | Buyer |

---

## Required Fields

| Field | Description | Required |
|---|---|---|
| Make-or-buy decisions | Decision + rationale for each major procurement item | Mandatory |
| Procurement list | Named items/services to be procured | Mandatory |
| Contract types | Contract type per procurement | Mandatory |
| Source selection criteria | Evaluation factors with weights | Mandatory |
| Procurement authority thresholds | Who can sign what value | Mandatory |
| Contract administration approach | Named owner and monitoring approach | Mandatory |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| A04 — Project Charter | SKL-02-01 | Budget constraints and organizational authority |
| A05 — Context Register | SKL-01-02 | Procurement policies, preferred vendors, legal requirements |
| A08 — Scope Documentation | SKL-03-03 | What needs to be delivered — input to make-or-buy |
| A19 — Risk Register | SKL-03-12 | Procurement risks — inform contract type selection |
| A25 — Resource Management Plan | SKL-03-10 | Internal resource gaps requiring external procurement |

---

## Outputs / Produces

| Output | Used By |
|---|---|
| Procurement list and contract types | A23 (Bid Documents) · A24 (Source Selection) · A31 (Contract Log) |
| Source selection criteria | A24 — Source Selection Criteria |
| Contract administration plan | SKL-04-09 · SKL-05-01 |

---

## Quality Criteria

- Make-or-buy decision documented for all significant procurement items
- Contract types selected based on risk profile (not defaulted to T&M for convenience)
- Source selection criteria defined before solicitation begins
- Procurement authority thresholds aligned with AUTHORITY-ROUTING.md
- A11 reviewed and updated when scope or resource assumptions change materially

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A06 — PM Plan | A11 is a subsidiary plan of A06 |
| A08 — Scope Documentation | Deliverable list drives make-or-buy analysis |
| A23 — Bid Documents | A11 procurement list seeds A23 |
| A24 — Source Selection Criteria | A11 §4 expanded into A24 |
| A31 — Contract and Vendor Log | A11 defines what A31 tracks |
| A32 — Procurement SOW | A11 procurement list seeds individual SOWs |

---

## PMBOK8 Anchors

| Reference | Detail |
|---|---|
| PMBOK8 Guide §2.6 | Project Work Performance Domain — procurement |
| Process Groups PG §4.9 | Plan Procurement Management |
| PMBOK8 Standard §3 | Stewardship — responsible resource acquisition |

---

## Change Log

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0.0 | 2026-05-30 | B1 Batch 2 | Initial definition — Phase B1 |

---

*Owner: Project Manager · Procurement Officer*  
*Change Control: Procurement approach changes require PM + Sponsor (T2 per AUTHORITY-ROUTING.md)*  
*Last Updated: 2026-05-30 · B1 Batch 2*

# A31 — Procurement and Contract Log
**Artifact ID:** A31
**Artifact Name:** Procurement and Contract Log
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.8 · Process-Groups §4.8 (closure) · Forms-Book
**Source Type:** PMI-derived
**File Path:** `artifacts/procurement/A31-procurement-contract-log.md`

---

## Definition

The Procurement and Contract Log is the single artifact that consolidates the procurement management plan, the make-or-buy analysis record, all procurement actions (solicitation, evaluation, selection), active contract records, contract performance monitoring, and contract closure records. It is the authoritative procurement record across the full project lifecycle.

**PMI Source:** PMBOK8 Guide §2.8 — Project Procurement Management; Process-Groups §4.8; Forms-Book procurement templates.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Procurement |
| **Type** | Consolidated procurement and contract record |
| **Lifecycle** | Created in Planning (if procurement in scope) · Active in Executing · Monitored in M&C · Closed in Closing |
| **Baseline?** | Procurement plan is governed; contract records are living |
| **Ownership** | Project Manager / Procurement Lead / Contracts Manager |

---

## Purpose

- Define the procurement strategy and make-or-buy decisions
- Record all procurement actions from solicitation through contract award
- Maintain active contract records and vendor performance data
- Track contract deliverables, milestones, and payment schedules
- Confirm formal contract closure before project closure (A27 §8)
- Provide the procurement audit trail

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Procurement Management Plan | Procurement strategy, contract types, solicitation approach, evaluation criteria, approval authority | SKL-03-01 (planning) |
| §2 Make-or-Buy Analysis | Decision record per work package or deliverable requiring external resource | SKL-03-01 |
| §3 Procurement Register | All procurement actions using schema below | SKL-04-09 |
| §4 Active Contract Records | Contract details, deliverables, milestones, payment schedule, SLAs, penalties | SKL-04-09 |
| §5 Vendor Performance Log | Delivery performance, quality ratings, issues, corrective actions per vendor | SKL-04-09 (ongoing) |
| §6 Contract Closure Record | Formal closure confirmation per contract, final payment, release of obligations | SKL-06-01 |

---

## Procurement Register Schema (§3)

| Field | Description |
|-------|-------------|
| **Procurement ID** | Format: P-NNN (e.g., P-001) |
| **Description** | What is being procured |
| **Justification** | Make-or-buy rationale |
| **Contract Type** | Fixed Price / Time & Materials / Cost-Reimbursable / Hybrid |
| **Solicitation Method** | RFP / RFQ / RFI / Sole Source / Framework Agreement |
| **Vendor Name** | Selected vendor |
| **Contract Value** | Total contracted value |
| **Contract Start Date** | |
| **Contract End Date** | |
| **Key Deliverables** | Contracted deliverables with acceptance criteria |
| **Payment Schedule** | Milestone-based / periodic / on-completion |
| **Status** | Planning / Solicitation / Evaluation / Awarded / Active / Closed |

---

## Contract Types Reference

| Type | Risk Allocation | Best Used When |
|------|----------------|----------------|
| Fixed Price (FP) | Vendor bears cost risk | Scope well-defined |
| Time & Materials (T&M) | Buyer bears cost risk | Scope uncertain; expertise needed |
| Cost-Reimbursable (CR) | Buyer bears cost risk | R&D or uncertain scope |
| Fixed Price + Incentive (FPI) | Shared | Performance incentives desired |

---

## Inputs

| Input | Source |
|-------|--------|
| A08 — Scope Document (WBS — items to procure) | SKL-03-05 |
| A15 — Schedule Model (procurement timeline) | SKL-03-06 |
| A16 — Financial Record (procurement budget) | SKL-03-15 |
| A19 — Risk Record (procurement risks) | SKL-03-10 |
| A05 — Context Register (approved vendor lists, OPA) | SKL-01-02 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Active contracts | SKL-04-09 · SKL-05-01 (monitoring) |
| Vendor performance data | A17 (Performance Report) · A21 (Lessons Learned) |
| Contract closure confirmation | A27 §8 (Closure Record) |
| Procurement lessons | A21 §1 |

---

## Quality Criteria

- Make-or-buy analysis documented before solicitation begins
- Evaluation criteria defined before vendors are assessed
- All contracts have formal acceptance criteria per deliverable
- Vendor performance reviewed at defined intervals
- All contracts formally closed (written confirmation) before A27 is signed
- No outstanding financial obligations at project close

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A08 — Scope Document | WBS identifies items to procure |
| A16 — Financial Record | Procurement costs in cost baseline |
| A19 — Risk Record | Procurement risks tracked |
| A17 — Performance Report | Vendor performance summarized |
| A27 — Closure Record | Contract closure confirmed in §8 |
| A21 — Lessons Learned | Procurement lessons captured |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.8.2.1–2.8.2.4 | Plan through Control Procurements |
| PMBOK8 Guide Figures 2-54 to 2-57 | Procurement management process flows |
| Process-Groups §4.8 | Close Procurements |
| Forms-Book | Procurement templates and forms |

---

*Owner: Project Manager / Procurement Lead · Version Control: Semantic versioning · Change Control: T2–T3 per AUTHORITY-ROUTING.md*
*Last Updated: 2026-05-30 · Patch H*

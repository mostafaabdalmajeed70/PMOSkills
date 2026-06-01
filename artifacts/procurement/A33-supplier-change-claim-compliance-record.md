# A33 — Supplier Change, Claim, and Compliance Record

## Artifact Metadata

| Field | Value |
|---|---|
| **Artifact ID** | A33 |
| **Artifact Name** | Supplier Change, Claim, and Compliance Record |
| **Artifact Type** | Supplier administration and exception artifact |
| **Source Type** | synthesis |
| **Governance Layer** | Project Governance |
| **Version** | 1.0.5 |
| **Status** | Active |
| **File Path** | `artifacts/procurement/A33-supplier-change-claim-compliance-record.md` |

---

## Purpose

Capture supplier-related changes, disputes, claims, compliance checks, inbound acceptance findings, and resolution decisions in one auditable record throughout supplier delivery and during closing.

---

## When Used

- Throughout active supplier delivery when changes, claims, or compliance issues arise
- During acceptance testing of supplier deliverables
- At contract closeout

---

## PMI Authority

| Field | Detail |
|---|---|
| **Primary PMI Source** | PMBOK8 |
| **Exact Section** | Appendix X4 procurement-related guidance; Table 2-1 Assess and Implement Changes; Close Project or Phase |
| **Purpose of Citation** | Align supplier change and claim handling with PMI-aligned control and closure practices |
| **Source Type** | synthesis |

---

## Performance Domains

Governance · Finance · Risk · Scope · Schedule

## Focus Areas

Monitoring and Controlling · Closing

## Related Processes

- Assess and Implement Changes
- Monitor and Control Project Performance
- Close Project or Phase

---

## Inputs

- A31 Procurement and Supplier Management Record
- Change requests from supplier
- Claims or dispute notices
- Compliance check findings
- Acceptance inspection results

---

## Outputs

- Supplier decisions and approvals
- Approved contract adjustments
- Claim resolutions
- Compliance evidence for audit
- Closeout action items

---

## Core Fields

| Field | Description |
|---|---|
| Supplier event or issue | Brief description of the change, claim, or compliance matter |
| Type of event | Change order / Claim / Dispute / Compliance finding / Acceptance finding |
| Impact summary | Effect on cost, schedule, scope, or quality |
| Compliance finding | Specific compliance requirement involved (if applicable) |
| Decision authority | Role authorized to resolve this event per threshold |
| Resolution | Decision made, conditions, adjustments |
| Follow-up action | Outstanding items, owner, due date |

---

## Ownership and Authority

| Role | Holder |
|---|---|
| **Owner** | Project manager, contract administrator, or procurement lead |
| **Approval Authority** | Procurement authority, legal authority, sponsor, or quality authority depending on issue type and threshold |
| **Escalation Trigger** | Claim, dispute, compliance breach, or supplier change exceeds delegated limits |

---

## Tailoring Guidance

Use one record for supplier-side change, claim, and compliance history. Separate registers are justified only if legal or audit requirements specifically demand them. Most projects can operate with a single integrated log.

---

## Waste Test

**Fail if:** Change orders, claims logs, and supplier acceptance checklists are maintained as separate files with the same case identifiers and decision fields.

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| A31 | Planning and ongoing administration — A33 captures exceptions within that context |
| A32 | Pre-award — A33 is post-award administration |
| A12 | Project-level change log; supplier-specific events route to A33 |
| A19 | Risk triggers may generate A33 entries and vice versa |

---

## Change Log

| Version | Date | Change |
|---|---|---|
| 1.0.5 | 2026-05-xx | Original version in extended-procurement/ |
| 1.0.6 | 2026-06-01 | Migrated from artifacts/extended-procurement/ to artifacts/procurement/ (P0-0I) |

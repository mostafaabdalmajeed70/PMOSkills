---
artifact_id: A33
name: Supplier Change, Claim, and Compliance Record
template_version: "1.0.0"
status: "Template · Active"
category: Supplier Administration and Exceptions
authority: "PMBOK8 Appendix X4 procurement-related guidance; Table 2-1 Assess and Implement Changes; Close Project or Phase"
source_type: synthesis
file_path: artifacts/procurement/A33-supplier-change-claim-compliance-record-template.md
---

## [A33] — Supplier Change, Claim, and Compliance Record | Template

> **Usage note:** This is a blank template. Every `[FIELD: ...]` cell must be completed by the project team before use. Static text, rules, and checklist items are pre-filled and must not be removed.

---

## Section 1 — Header / Identification

| Field | Value |
|---|---|
| Project Name | [FIELD: Full project name] |
| Supplier Name / ID | [FIELD: Legal name and internal identifier] |
| Contract Reference | [FIELD: Contract number or agreement reference] |
| Contract Administrator | [FIELD: Name and title] |
| Date | [FIELD: YYYY-MM-DD] |
| Version | [FIELD: e.g. 1.0] |
| Status | [FIELD: Active / Suspended / Closed / Terminated] |
| Linked Artifacts | A31, A32, A12, A19 |

---

## Section 2 — Event Register

| Event ID | Date | Type | Description | Impact Summary | Decision Authority | Resolution | Follow-up Action | Owner | Due Date | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| [FIELD: e.g. EV-001] | [FIELD: YYYY-MM-DD] | [FIELD: Change Order / Claim / Dispute / Compliance Finding / Acceptance Finding] | [FIELD: description] | [FIELD: cost/schedule/scope/quality impact] | [FIELD: authority name and role] | [FIELD: resolution or "Pending"] | [FIELD: follow-up or "None"] | [FIELD: owner] | [FIELD: YYYY-MM-DD] | [FIELD: Open / In Progress / Resolved / Escalated / Closed] |
| [FIELD: EV-002] | [FIELD: YYYY-MM-DD] | [FIELD: type] | [FIELD: description] | [FIELD: impact] | [FIELD: authority] | [FIELD: resolution] | [FIELD: follow-up] | [FIELD: owner] | [FIELD: YYYY-MM-DD] | [FIELD: status] |

---

## Section 3 — Change Order Log

| CO ID | Event Ref | Original Contract Ref | Change Description | Cost Impact | Schedule Impact | Decision | Approving Authority | Approval Date |
|---|---|---|---|---|---|---|---|---|
| [FIELD: CO-001] | [FIELD: Event ID] | [FIELD: contract ref] | [FIELD: description] | [FIELD: cost impact or "None"] | [FIELD: schedule impact or "None"] | [FIELD: Approved / Rejected / Pending] | [FIELD: authority] | [FIELD: YYYY-MM-DD or "Pending"] |

---

## Section 4 — Claims and Disputes Log

| Claim ID | Event Ref | Claim Description | Amount Claimed | Basis | Resolution | Resolution Status | Date Resolved |
|---|---|---|---|---|---|---|---|
| [FIELD: CL-001] | [FIELD: Event ID] | [FIELD: description] | [FIELD: amount or "Non-monetary"] | [FIELD: contractual basis] | [FIELD: resolution] | [FIELD: Negotiated / Arbitration / Litigation / Withdrawn / Settled / Pending] | [FIELD: YYYY-MM-DD or "Pending"] |

---

## Section 5 — Compliance Findings Log

| Finding ID | Event Ref | Compliance Area | Finding Description | Severity | Required Action | Responsible Party | Resolution Date | Status |
|---|---|---|---|---|---|---|---|---|
| [FIELD: CF-001] | [FIELD: Event ID] | [FIELD: e.g. Health & Safety / Regulatory / Contractual / Data Protection] | [FIELD: description] | [FIELD: Minor / Moderate / Major / Critical] | [FIELD: required action] | [FIELD: responsible party] | [FIELD: YYYY-MM-DD] | [FIELD: Open / In Progress / Resolved / Closed] |

---

## Section 6 — Acceptance Findings Log

| Finding ID | Event Ref | Deliverable | Acceptance Criterion | Finding Description | Disposition | Resolution Notes | Date |
|---|---|---|---|---|---|---|---|
| [FIELD: AF-001] | [FIELD: Event ID] | [FIELD: deliverable name or ref] | [FIELD: acceptance criterion] | [FIELD: finding description] | [FIELD: Accepted / Conditionally Accepted / Rejected / Resubmission Required] | [FIELD: resolution notes] | [FIELD: YYYY-MM-DD] |

---

## Section 7 — Contract Closeout Checklist

| # | Closeout Item | Status | Confirmed Date | Notes |
|---|---|---|---|---|
| 1 | All contractual deliverables received and formally accepted | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 2 | All open Change Orders resolved and closed | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 3 | All claims and disputes resolved or formally settled | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 4 | All compliance findings resolved and closed | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 5 | Final invoice received, verified, and processed | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 6 | Supplier performance evaluation completed and filed | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 7 | All project-owned assets returned or destroyed | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 8 | Contract closeout notice issued to supplier in writing | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 9 | Lessons learned captured in A30 | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |
| 10 | Contract file archived in document management system | [FIELD: Complete / Incomplete / N/A] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: notes] |

---

## Section 8 — Waste Test

- [ ] Every sub-section event has a corresponding entry in the Event Register (Section 2)?
- [ ] All open Change Orders tracked with named authority and due date?
- [ ] All claims with "Pending" resolution escalated appropriately?
- [ ] All Critical compliance findings linked to open corrective action?
- [ ] All rejected deliverables followed up with resubmission or formal disposition?
- [ ] Contract Closeout Checklist only marked complete when all items are confirmed?
- [ ] Entries consistent with Change Log (A12) for all approved change orders?
- [ ] Unresolved issues flagged in Issue Register (A19)?

---

## Change Log

| Version | Date | Author/Event | Description |
|---|---|---|---|
| 1.0.0 | 2026-05-31 | Phase B2 Batch B | Initial template |
| 1.0.1 | 2026-06-01 | Phase 0 cleanup | Migrated from artifacts/extended-procurement/ to artifacts/procurement/ (P0-0I) |

---

*Template for: A33 — Supplier Change, Claim, and Compliance Record*
*Authority: PMBOK8 Appendix X4; Table 2-1 Assess and Implement Changes; Close Project or Phase*
*See definition file: `artifacts/procurement/A33-supplier-change-claim-compliance-record.md`*

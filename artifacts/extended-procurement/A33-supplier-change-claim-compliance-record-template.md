---
artifact_id: A33
name: Supplier Change, Claim, and Compliance Record
template_version: "1.0.0"
status: "Template · Active"
category: Supplier Administration and Exceptions
authority: "PMBOK8 Appendix X4 procurement-related guidance; Table 2-1 Assess and Implement Changes; Close Project or Phase"
source_type: synthesis
file_path: artifacts/extended-procurement/A33-supplier-change-claim-compliance-record-template.md
---

## [A33] — Supplier Change, Claim, and Compliance Record | Template

> **Usage note:** This is a blank template. Every `[FIELD: ...]` cell must be completed by the project team before use. Static text, rules, and checklist items are pre-filled and must not be removed. Do not pre-populate fields with example data.

---

## Section 1 — Header / Identification

| Field | Value |
|---|---|
| Project Name | [FIELD: Full project name as registered in the project charter] |
| Supplier Name / ID | [FIELD: Legal name and internal identifier of the supplier] |
| Contract Reference | [FIELD: Contract number or agreement reference associated with this supplier relationship] |
| Contract Administrator | [FIELD: Name and title of the individual administering this contract] |
| Date | [FIELD: Date this record was created or last updated — YYYY-MM-DD] |
| Version | [FIELD: Version number, e.g., 1.0] |
| Status | [FIELD: select from Active / Suspended / Closed / Terminated] |
| Linked Artifacts | A31 — Procurement Management Plan; A32 — Supplier Evaluation and Award Decision Record; A12 — Change Log; A19 — Issue Register |

---

## Section 2 — Event Register

Record all notable supplier events in this master register. Event Types: **Change Order / Claim / Dispute / Compliance Finding / Acceptance Finding**. Status values: **Open / In Progress / Resolved / Escalated / Closed**.

| Event ID | Date | Type | Description | Impact Summary | Decision Authority | Resolution | Follow-up Action | Owner | Due Date | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| [FIELD: e.g., EV-001] | [FIELD: YYYY-MM-DD] | [FIELD: select from Change Order / Claim / Dispute / Compliance Finding / Acceptance Finding] | [FIELD: Brief description of the event] | [FIELD: Summary of the impact on cost, schedule, scope, or quality] | [FIELD: Name and role of the authority empowered to decide on this event] | [FIELD: Resolution outcome — or "Pending"] | [FIELD: Any follow-up action required after resolution — or "None"] | [FIELD: Name of the individual responsible for managing this event] | [FIELD: YYYY-MM-DD] | [FIELD: select from Open / In Progress / Resolved / Escalated / Closed] |
| [FIELD: e.g., EV-002] | [FIELD: YYYY-MM-DD] | [FIELD: select from Change Order / Claim / Dispute / Compliance Finding / Acceptance Finding] | [FIELD: Brief description of the event] | [FIELD: Impact summary] | [FIELD: Decision authority] | [FIELD: Resolution or "Pending"] | [FIELD: Follow-up action or "None"] | [FIELD: Owner name] | [FIELD: YYYY-MM-DD] | [FIELD: select from Open / In Progress / Resolved / Escalated / Closed] |
| [FIELD: e.g., EV-003] | [FIELD: YYYY-MM-DD] | [FIELD: select from Change Order / Claim / Dispute / Compliance Finding / Acceptance Finding] | [FIELD: Brief description of the event] | [FIELD: Impact summary] | [FIELD: Decision authority] | [FIELD: Resolution or "Pending"] | [FIELD: Follow-up action or "None"] | [FIELD: Owner name] | [FIELD: YYYY-MM-DD] | [FIELD: select from Open / In Progress / Resolved / Escalated / Closed] |

> Add rows as needed. Each event in the sub-sections below (Sections 3–6) must have a corresponding entry in this master register.

---

## Section 3 — Change Order Log

Record all contract change orders. Decision values: **Approved / Rejected / Pending**.

| CO ID | Event Register Ref | Original Contract Ref | Change Description | Cost Impact | Schedule Impact | Decision | Approving Authority | Approval Date |
|---|---|---|---|---|---|---|---|---|
| [FIELD: e.g., CO-001] | [FIELD: Corresponding Event ID from Section 2] | [FIELD: Original contract section or clause being changed] | [FIELD: Description of what is being changed in the contract] | [FIELD: Cost impact, positive or negative, in currency — or "None"] | [FIELD: Schedule impact in days or milestones affected — or "None"] | [FIELD: select from Approved / Rejected / Pending] | [FIELD: Name and role of the authority approving or rejecting the change order] | [FIELD: YYYY-MM-DD — or "Pending"] |
| [FIELD: e.g., CO-002] | [FIELD: Event ID] | [FIELD: Contract ref] | [FIELD: Change description] | [FIELD: Cost impact] | [FIELD: Schedule impact] | [FIELD: select from Approved / Rejected / Pending] | [FIELD: Approving authority] | [FIELD: YYYY-MM-DD or "Pending"] |
| [FIELD: e.g., CO-003] | [FIELD: Event ID] | [FIELD: Contract ref] | [FIELD: Change description] | [FIELD: Cost impact] | [FIELD: Schedule impact] | [FIELD: select from Approved / Rejected / Pending] | [FIELD: Approving authority] | [FIELD: YYYY-MM-DD or "Pending"] |

---

## Section 4 — Claims and Disputes Log

Record all formal claims and disputes raised by either the project or the supplier. Resolution Status: **Negotiated / Arbitration / Litigation / Withdrawn / Settled**.

| Claim ID | Event Register Ref | Claim Description | Amount Claimed | Basis | Resolution | Resolution Status | Date Resolved |
|---|---|---|---|---|---|---|---|
| [FIELD: e.g., CL-001] | [FIELD: Corresponding Event ID from Section 2] | [FIELD: Description of the claim or dispute — what is being claimed and by whom] | [FIELD: Amount claimed in currency — or "Non-monetary"] | [FIELD: Contractual or legal basis for the claim, e.g., contract clause, force majeure, scope change] | [FIELD: Description of the resolution outcome] | [FIELD: select from Negotiated / Arbitration / Litigation / Withdrawn / Settled / Pending] | [FIELD: YYYY-MM-DD — or "Pending"] |
| [FIELD: e.g., CL-002] | [FIELD: Event ID] | [FIELD: Claim description] | [FIELD: Amount claimed] | [FIELD: Basis] | [FIELD: Resolution outcome] | [FIELD: select from Negotiated / Arbitration / Litigation / Withdrawn / Settled / Pending] | [FIELD: YYYY-MM-DD or "Pending"] |

---

## Section 5 — Compliance Findings Log

Record all compliance findings arising from audits, inspections, or contract monitoring. Severity: **Minor / Moderate / Major / Critical**.

| Finding ID | Event Register Ref | Compliance Area | Finding Description | Severity | Required Action | Responsible Party | Resolution Date | Status |
|---|---|---|---|---|---|---|---|---|
| [FIELD: e.g., CF-001] | [FIELD: Corresponding Event ID from Section 2] | [FIELD: Area of compliance, e.g., Health & Safety, Regulatory, Contractual Obligation, Data Protection] | [FIELD: Description of the compliance finding] | [FIELD: select from Minor / Moderate / Major / Critical] | [FIELD: Specific action required to remediate the finding] | [FIELD: Party responsible for remediation — project team or supplier] | [FIELD: YYYY-MM-DD — target or actual resolution date] | [FIELD: select from Open / In Progress / Resolved / Closed] |
| [FIELD: e.g., CF-002] | [FIELD: Event ID] | [FIELD: Compliance area] | [FIELD: Finding description] | [FIELD: select from Minor / Moderate / Major / Critical] | [FIELD: Required action] | [FIELD: Responsible party] | [FIELD: YYYY-MM-DD or "Pending"] | [FIELD: select from Open / In Progress / Resolved / Closed] |

---

## Section 6 — Acceptance Findings Log

Record findings from formal deliverable acceptance reviews. Disposition: **Accepted / Conditionally Accepted / Rejected / Resubmission Required**.

| Finding ID | Event Register Ref | Deliverable | Acceptance Criterion | Finding Description | Disposition | Resolution Notes | Date |
|---|---|---|---|---|---|---|---|
| [FIELD: e.g., AF-001] | [FIELD: Corresponding Event ID from Section 2] | [FIELD: Name or reference of the deliverable under review] | [FIELD: The specific acceptance criterion that was evaluated] | [FIELD: Description of the finding — deviation, defect, or gap identified] | [FIELD: select from Accepted / Conditionally Accepted / Rejected / Resubmission Required] | [FIELD: Notes on conditions, corrective actions required, or final acceptance confirmation] | [FIELD: YYYY-MM-DD] |
| [FIELD: e.g., AF-002] | [FIELD: Event ID] | [FIELD: Deliverable name or ref] | [FIELD: Acceptance criterion] | [FIELD: Finding description] | [FIELD: select from Accepted / Conditionally Accepted / Rejected / Resubmission Required] | [FIELD: Resolution notes] | [FIELD: YYYY-MM-DD] |

---

## Section 7 — Contract Closeout Checklist

Complete this checklist at contract closeout. Check each item only when confirmed. Status and date fields must be completed; checklist item text is static.

| # | Closeout Item | Status | Confirmed Date | Notes |
|---|---|---|---|---|
| 1 | All contractual deliverables have been received and formally accepted | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 2 | All open Change Orders have been resolved and closed | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 3 | All claims and disputes have been resolved or formally settled | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 4 | All compliance findings have been resolved and closed | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 5 | Final invoice has been received, verified, and processed for payment | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 6 | Supplier performance evaluation has been completed and filed | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 7 | All project-owned assets, intellectual property, and data in supplier possession have been returned or destroyed | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 8 | Contract closeout notice has been issued to the supplier in writing | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 9 | Lessons learned related to this supplier have been captured in A30 | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |
| 10 | Contract file has been archived in the organisational document management system | [FIELD: select from Complete / Incomplete / Not Applicable] | [FIELD: YYYY-MM-DD or N/A] | [FIELD: Any exceptions or notes] |

---

## Section 8 — Waste Test

*Answer each question before finalising this record. If any answer is "No", revisit the relevant section.*

- [ ] Does every event in the sub-sections (Sections 3–6) have a corresponding entry in the Event Register (Section 2)?
- [ ] Are all open Change Orders (Section 3) tracked with a named approving authority and due date?
- [ ] Have all claims and disputes with a "Pending" resolution been escalated appropriately?
- [ ] Are all Critical compliance findings (Section 5) linked to an open corrective action with a responsible party?
- [ ] Have all rejected or conditionally accepted deliverables (Section 6) been followed up with a resubmission or formal disposition?
- [ ] Is the Contract Closeout Checklist (Section 7) only marked complete when all items are confirmed — not before?
- [ ] Are this record's entries consistent with the Change Log (A12) for all approved change orders?
- [ ] Are unresolved issues from this record flagged in the Issue Register (A19)?
- [ ] Has the contract administrator reviewed and signed off on this record at each update?
- [ ] Is this record referenced in the Project Closure Report at project closeout?

---

## Change Log

| Version | Date | Author/Event | Description |
|---|---|---|---|
| 1.0.0 | 2026-05-31 | Phase B2 Batch B | Initial template |

---

*Template for: Supplier Change, Claim, and Compliance Record*
*Authority: PMBOK8 Appendix X4 procurement-related guidance; Table 2-1 Assess and Implement Changes; Close Project or Phase*
*See definition file: artifacts/extended-procurement/A33-supplier-change-claim-compliance-record-template.md*

# A27 — Project Closure Record
**Artifact ID:** A27
**Artifact Name:** Project Closure Record
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.1.6.7 · Process-Groups §4.8
**Source Type:** PMI-derived
**File Path:** `artifacts/closing/A27-closure-record.md`

---

## Definition

The Project Closure Record is the formal artifact that documents the completion of the project or phase — confirming deliverable acceptance, releasing resources, archiving project artifacts, and recording final performance and lessons. It is the last artifact produced on a project and must be signed by the project sponsor or governing authority to formally close the project.

**PMI Source:** PMBOK8 Guide §2.1.6.7 — Close Project or Phase; Process-Groups §4.8.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Closing |
| **Type** | Formal closure document |
| **Lifecycle** | Produced during Closing focus area · Signed at project or phase close · Archived permanently |
| **Baseline?** | No — formal record, not a baseline |
| **Ownership** | Project Manager · Approved by Sponsor / Governing Body |

---

## Purpose

- Formally confirm that all deliverables have been accepted or properly dispositioned
- Document release of all resources (human, financial, physical)
- Summarize final performance against all baselines
- Record final lessons learned summary
- Confirm all contracts are closed (A31)
- Authorize archive of all project artifacts
- Provide the formal governance sign-off that closes the project

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Project Summary | Project name, ID, charter reference, sponsor, PM, final dates | SKL-06-01 |
| §2 Deliverable Acceptance Record | List of all project deliverables, acceptance status, accepted by, date | SKL-06-01 |
| §3 Final Performance Summary | SPI, CPI, EAC vs. BAC, scope delivery %, key variances | SKL-06-02 (A17 final) |
| §4 Change History Summary | Total CRs raised / approved / rejected, net baseline impact | SKL-06-02 (A12 summary) |
| §5 Risk Closure Summary | Risks realized, risks closed without occurring, residual risks transferred | SKL-06-02 (A19 summary) |
| §6 Lessons Learned Summary | Top lessons by category (detail in A21) | SKL-06-03 |
| §7 Resource Release Record | All team members released, resource managers notified, dates | SKL-06-01 |
| §8 Contract Closure Confirmation | All contracts closed (reference A31), vendor release confirmed | SKL-06-01 |
| §9 Archive Record | Artifact archive location, access details, retention period | SKL-06-03 |
| §10 Formal Closure Sign-Off | Sponsor / governing body signature, date, closing statement | SKL-06-01 |

---

## Deliverable Acceptance Schema (§2)

| Deliverable ID | Deliverable Name | Acceptance Status | Accepted By | Acceptance Date | Notes |
|----------------|-----------------|------------------|-------------|-----------------|-------|
| D-001 | [Name] | Accepted / Deferred / Cancelled | [Name, Role] | [Date] | |

---

## Closure Prerequisites

Before A27 can be signed, all of the following must be confirmed:

- [ ] All deliverables accepted, deferred, or formally cancelled with documented rationale
- [ ] Final Performance Report (A17 — final version) complete and reviewed by sponsor
- [ ] All open change requests (A12) dispositioned (no pending CRs)
- [ ] All open issues (A18) resolved or formally transferred
- [ ] All contracts closed (A31)
- [ ] All resources formally released
- [ ] Lessons Learned Record (A21) finalized and submitted to OPA (A05)
- [ ] Archive record complete (§9)
- [ ] Benefits realization plan handed off (A02) if benefits are post-project

---

## Inputs

| Input | Source |
|-------|--------|
| A17 — Final Performance Report | SKL-06-02 |
| A21 — Lessons Learned (final) | SKL-06-03 |
| A12 — Change Log (summary) | SKL-05-02 |
| A18 — Issue Log (resolved) | SKL-04-01 |
| A19 — Risk Record (closure summary) | SKL-05-06 |
| A31 — Procurement/Contract Log | SKL-04-09 |
| A02 — Benefits Record | SKL-02-01 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Formal closure authorization | Governance / PMO |
| Archive record | Organization / future project teams |
| OPA updates (via A21 → A05) | Future projects |
| Resource release notifications | Resource managers / HR |
| Benefits handoff record | Benefits owner / operations |

---

## Quality Criteria

- All 10 sections complete before sponsor signature is sought
- No open CRs or unresolved critical issues at time of sign-off
- Deliverable acceptance documented per stakeholder (not just PM self-certification)
- Lessons submitted to OPA (A05) before archive
- Archive location accessible to authorized future project teams
- Sponsor or governing body signature obtained within defined closure window

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A04 — Project Charter | Closure confirms charter objectives delivered |
| A14 — Integrated PM Plan | Final baselines referenced in §3 |
| A17 — Performance Report | Final version feeds §3–§5 |
| A21 — Lessons Learned | Final version feeds §6 and OPA |
| A12 — Change Log | Summary feeds §4 |
| A31 — Procurement Log | Contract closure confirmed in §8 |
| A05 — Context Register | OPA updated with lessons and archive record |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.1.6.7 | Close Project or Phase · Figure 2-9 |
| Process-Groups §4.8 | Close Project or Phase — inputs, outputs |
| PMBOK8 Standard §3 | Stewardship principle — responsible closure |

---

*Owner: Project Manager · Approval Authority: Sponsor / Governing Body · Retention: Per organizational records policy*
*Last Updated: 2026-05-30 · Patch F*

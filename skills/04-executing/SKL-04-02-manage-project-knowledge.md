---
skill_id: SKL-04-02
skill_name: Manage Project Knowledge
pack: "04 — Executing"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A21 — Lessons Learned Record"
artifacts_updated:
  - "A05 — Context Register (OPA updates)"
pmbok8_anchor: "Guide §2.1.6.4 Manage Project Knowledge · Figure 2-6"
performance_domains:
  - Governance
  - Delivery
focus_area: Executing
upstream_prerequisites:
  - "SKL-04-01 — project work must be underway"
downstream_skills:
  - "SKL-06-03 — Capture and Archive Lessons Learned"
file_path: "skills/04-executing/SKL-04-02-manage-project-knowledge.md"
tests: 7
---

# SKL-04-02 — Manage Project Knowledge

**Pack:** 04 — Executing
**Status:** Draft · Untested
**Primary Artifact:** A21 — Lessons Learned Record
**PMBOK8 Anchor:** Guide §2.1.6.4 · Figure 2-6

---

## Purpose

Manage Project Knowledge ensures that explicit and tacit knowledge generated during project execution is captured, shared among the team, and transferred to the organization's process assets (OPA). A21 is a continuous execution artifact — it is not a closure document and must be updated throughout all project phases.

---

## Inputs

| Input | Artifact | Section | Notes |
|---|---|---|---|
| Issues and resolutions | A18 | Closed items | Every significant closed issue triggers an A21 entry |
| Change decisions | A12 | Closed items | Approved and rejected CRs with learning value |
| Work performance data | — | From SKL-04-01 | Observations from execution |
| OPA repository | A05 | OPA section | Existing knowledge to avoid duplication |

---

## Steps

### Step 1 — Establish Knowledge Capture Cadence
Define when and how lessons are captured. Minimum cadence:
- After each phase gate
- After any significant issue resolved from A18
- After any key milestone (hit or missed)
- After any risk event triggered (from A19)
Document cadence in A14 knowledge management section.

### Step 2 — Capture Explicit Knowledge
Record factual findings, decisions, and outcomes in A21. Each entry must include:
- Date
- Phase
- Category: scope / schedule / cost / risk / stakeholder / quality / resource / procurement
- Description of what happened
- Impact (positive or negative, quantified if possible)
- Root cause (for negative events)
- Recommendation for future projects

### Step 3 — Facilitate Tacit Knowledge Sharing
Create structured opportunities for team members to share experience-based knowledge:
- Workshops and retrospectives
- Peer reviews of deliverables
- Lunch-and-learn sessions
- Pair work and shadowing assignments
Document key outputs of these sessions in A21 with the session type and participants noted.

### Step 4 — Update OPA
For lessons that represent reusable organizational learning:
- Update A05 Context Register with the new OPA entry
- Reference the A21 entry ID as the source
- Tag the A21 entry with OPA transfer status = Transferred
- PM must confirm each OPA transfer before it is marked complete

### Step 5 — Make Knowledge Accessible
Ensure A21 is accessible to all relevant team members and stakeholders per A28 communications plan. Any access restriction must be documented with justification in A06.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Lessons learned entries | A21 | Execution section — continuous |
| OPA updates | A05 | OPA section |

---

## Operating Rules

1. A21 is not a closure document — it must be updated continuously throughout all packs, starting in Pack 04.
2. Every resolved A18 issue that is classified as high-impact must generate at least one A21 entry.
3. No A21 entry may be anonymous — each entry must have a date, category, and identified contributor.
4. OPA transfer from A21 to A05 requires PM confirmation; team members cannot self-transfer to OPA.
5. Tacit knowledge facilitation events are not optional — at least one structured sharing event per project phase is required.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Lessons deferred to closure | A21 is empty during active execution | Immediate triage: collect lessons from team retroactively; reset cadence |
| Anonymous entries | A21 entries with no contributor | Audit A21; assign contributor to each entry |
| OPA not updated | A21 entries marked for transfer with no A05 update | Review all transfer-tagged entries; complete A05 updates |
| Knowledge siloed | Key team member departing with undocumented knowledge | Emergency tacit capture session; update A21 before departure |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Continuous update | A21 has entries for every reporting period during active execution | A21 has no entries during an active execution period |
| T-2 | A18 linkage | Every closed high-impact A18 issue has a corresponding A21 entry | Closed high-impact A18 issues with no A21 entry |
| T-3 | Entry completeness | Every A21 entry has date, category, description, impact, recommendation | Any A21 entry missing category or recommendation |
| T-4 | No anonymous entries | Every A21 entry has an identified contributor | Any A21 entry with no contributor |
| T-5 | OPA transfer completed | A21 entries tagged for OPA transfer have a confirmed A05 update | Transfer-tagged entry with no A05 update |
| T-6 | Tacit knowledge facilitated | At least one structured knowledge-sharing event per phase documented in A21 | No knowledge-sharing event recorded in any phase |
| T-7 | Accessibility confirmed | A21 accessible to all team members per A28 | A21 restricted without documented justification in A06 |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial build |

---

*Authority: PMBOK8 Guide §2.1.6.4 · Figure 2-6*
*Source type: PMI-derived*

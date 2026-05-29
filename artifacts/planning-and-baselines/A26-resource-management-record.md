# A26 — Resource Management Record
**Artifact ID:** A26
**Artifact Name:** Resource Management Record
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.6 · Process-Groups §4.6
**Source Type:** PMI-derived
**File Path:** `artifacts/planning-and-baselines/A26-resource-management-record.md`

---

## Definition

The Resource Management Record consolidates the resource management plan, resource estimates, acquisition records, team development log, team performance/conflict log, and resource control log. It is the single authority for all human and physical resource decisions across the project lifecycle.

**PMI Source:** PMBOK8 Guide §2.6; Process-Groups §4.6.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Planning & Baselines |
| **Type** | Consolidated resource record |
| **Lifecycle** | Created in Planning · Maintained in Executing · Controlled in M&C · Archived in Closing |
| **Baseline?** | Resource plan governed; individual entries are living records |
| **Ownership** | Project Manager / Resource Manager |

---

## Purpose

- Define how resources will be planned, acquired, managed, developed, and controlled
- Record resource estimates, actuals, and variances
- Track team acquisition, onboarding, development, and performance
- Serve as evidence base for resource-related decisions and escalations
- Feed the Final Performance Report (A17) at closure

---

## Sections

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Resource Management Plan | Team structure, RACI, acquisition strategy, development approach, release plan | SKL-03-16 |
| §2 Resource Estimates | Effort/duration estimates per work package, resource types, basis of estimate | SKL-03-17 |
| §3 Resource Capacity and Acquisition Record | Acquisition actions, staffing decisions, onboarding records, contract resources | SKL-04-03 |
| §4 Team Development Log | Training, coaching, mentoring, team-building activities, skill development records | SKL-04-04 |
| §5 Performance and Conflict Log | Performance feedback, conflict events, resolution actions, escalations | SKL-04-05 |
| §6 Resource Control Log | Resource variances, reallocation decisions, shortage responses, actuals vs. planned | SKL-05-08 |

---

## RACI Matrix (embedded in §1)

| Role | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| [Role 1] | [Activity] | [Activity] | [Activity] | [Activity] |
| [Role 2] | ... | ... | ... | ... |

*Full RACI populated during SKL-03-16 — Plan Resource Management.*

---

## Inputs

| Input | Source |
|-------|--------|
| A08 §4 — WBS | SKL-03-05 |
| A15 — Schedule Model | SKL-03-06 |
| A04 — Project Charter (resource constraints) | SKL-02-01 |
| A05 — Context Register (resource pool, OPA) | SKL-01-02 |
| A16 — Cost baseline (resource cost inputs) | SKL-03-13 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| RACI + team structure | A14 (PMP assembly) · SKL-04-04 · SKL-04-05 |
| Resource estimates | A15 (schedule loading) · A16 (cost estimates) |
| Acquisition record | SKL-05-08 (Control Resources) |
| Performance log | SKL-06-02 (Final Performance Review) |

---

## Quality Criteria

- RACI covers all WBS work packages and governance decisions
- Resource estimates traceable to WBS work packages
- Acquisition plan approved before execution begins
- All team members have documented onboarding records
- Performance feedback documented at defined cadence
- Resource variances recorded with corrective actions

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A08 — Scope Document | WBS drives resource estimates |
| A15 — Schedule Model | Resource loading linked to schedule |
| A16 — Financial Record | Resource costs feed cost baseline |
| A17 — Performance Report | Resource utilization reported |
| A19 — Risk Record | Resource risks tracked |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.6.2.1–2.6.2.6 | Plan Resource through Control Resources |
| PMBOK8 Guide Figures 2-41 to 2-45 | Resource management process flows |

---

*Owner: Project Manager / Resource Manager · Version Control: Semantic versioning · Change Control: T2 per AUTHORITY-ROUTING.md*
*Last Updated: 2026-05-30 · Patch D*

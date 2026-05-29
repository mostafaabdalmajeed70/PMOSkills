# A17 — Performance Report
**Artifact ID:** A17
**Artifact Name:** Performance Report
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** PMBOK8 Guide §2.1.6.5 · EVM · Process-Groups §4.5
**Source Type:** PMI-derived
**File Path:** `artifacts/monitoring-and-decisions/A17-performance-report.md`

---

## Definition

The Performance Report is the periodic (and final) communication of project performance status against the approved baselines — covering schedule, cost, scope, risk, resources, and stakeholder engagement. It is produced by SKL-05-01 (Monitor and Control Project Work) each reporting cycle and by SKL-06-02 (Final Performance Review) at closure.

**PMI Source:** PMBOK8 Guide §2.1.6.5 — Monitor and Control Project Work; EVM Standard; Process-Groups §4.5.

---

## Artifact Type

| Field | Value |
|-------|-------|
| **Category** | Monitoring & Decisions |
| **Type** | Periodic performance communication |
| **Lifecycle** | First issued when execution begins · Produced each reporting cycle · Final version issued at closure |
| **Baseline?** | No — reporting artifact |
| **Ownership** | Project Manager |

---

## Purpose

- Communicate project health to stakeholders and governance authorities
- Report variance against scope, schedule, cost, and risk baselines
- Trigger escalation when thresholds are breached
- Provide the evidentiary basis for change requests
- Support governance decisions and sponsor oversight
- Final version (SKL-06-02) provides the definitive project performance record at closure

---

## Sections — Periodic Report

| Section | Content | Populated By |
|---------|---------|-------------|
| §1 Executive Summary | Overall RAG status, key decisions needed, period highlights | SKL-05-01 |
| §2 Schedule Performance | SV, SPI, critical path status, milestone forecast, EAC-T | SKL-05-04 |
| §3 Cost Performance | CV, CPI, AC vs. EV vs. PV, EAC, ETC, TCPI, VAC | SKL-05-05 |
| §4 Scope Status | Deliverable completion %, scope changes approved in period | SKL-05-03 |
| §5 Risk Status | Top risks, new risks, closed risks, response effectiveness | SKL-05-06 |
| §6 Resource Status | Resource utilization, availability issues, actions taken | SKL-05-08 |
| §7 Stakeholder Engagement | Engagement level changes, issues, actions | SKL-05-07 |
| §8 Change Summary | CRs raised / approved / rejected / deferred in period | SKL-05-02 |
| §9 Issues | Open issues from A18, priority, owner, resolution status | SKL-04-01 |
| §10 Decisions Required | Items requiring sponsor or governance decision this cycle | SKL-05-01 |
| §11 Forecast | Next period plan, upcoming milestones, risks to watch | SKL-05-01 |

---

## RAG Status Definitions

| Status | Meaning | Action |
|--------|---------|--------|
| 🟢 Green | On track — within variance thresholds | Continue; report normally |
| 🟡 Amber | At risk — approaching threshold or one baseline off-track | Corrective action plan required |
| 🔴 Red | Off track — threshold breached on one or more baselines | Escalate; change request likely needed |

*Variance thresholds defined in A06 §6 (cost) and A06 §5 (schedule) per project.*

---

## Sections — Final Performance Report (SKL-06-02)

| Section | Content |
|---------|---------|
| §1 Project Summary | Charter objectives vs. actual outcomes |
| §2 Scope Delivery | Deliverables delivered, accepted, deferred, cancelled |
| §3 Schedule Performance | Planned vs. actual finish, SPI trend, milestone adherence |
| §4 Cost Performance | BAC vs. EAC vs. actual cost, CPI trend, variance analysis |
| §5 Risk Outcomes | Risks realized, impact, response effectiveness |
| §6 Change History | Total CRs, approved / rejected breakdown, baseline impact summary |
| §7 Stakeholder Assessment | Final engagement assessment, key relationship outcomes |
| §8 Lessons Learned Summary | Top lessons (detail in A21) |
| §9 Benefits Realization | Value delivered vs. A02 (Benefits Record) |
| §10 Recommendations | For future similar projects |

---

## Inputs

| Input | Source |
|-------|--------|
| A15 — Schedule Model (SV, SPI, EAC-T) | SKL-05-04 |
| A16 — Financial Record (CV, CPI, EAC, TCPI) | SKL-05-05 |
| A19 — Risk Record (risk status) | SKL-05-06 |
| A18 — Issue Log (open issues) | SKL-04-01 |
| A12 — Change Log (CR statistics) | SKL-05-02 |
| A07 — Stakeholder SEAM (engagement status) | SKL-05-07 |
| A26 — Resource Record (utilization data) | SKL-05-08 |

---

## Outputs / Produces

| Output | Used By |
|--------|--------|
| Periodic status report | Stakeholders · Sponsor · Governance |
| Escalation triggers | AUTHORITY-ROUTING.md (T3/T4 decisions) |
| Final performance record | A27 (Closure Record) · A21 (Lessons Learned) |

---

## Quality Criteria

- All EVM metrics correctly calculated against approved baselines
- RAG status consistent with variance thresholds defined in A06
- Issued on schedule per A28 communications plan
- Escalation items clearly identified with decision needed
- Final report covers all 10 sections listed above
- Final report reviewed by sponsor before A27 closure record is signed

---

## Related Artifacts

| Artifact | Relationship |
|----------|--------------|
| A14 — Integrated PM Plan | Baselines against which performance is measured |
| A15 — Schedule Model | SV/SPI/EAC-T source |
| A16 — Financial Record | CV/CPI/EAC/TCPI source |
| A18 — Issue Log | Open issues summarized in §9 |
| A12 — Change Log | Change statistics in §8 |
| A27 — Closure Record | Final performance report feeds closure |
| A28 — Comms Record | Report delivery tracked in delivery log |

---

## PMBOK8 Anchors

| Reference | Detail |
|-----------|--------|
| PMBOK8 Guide §2.1.6.5 | Monitor and Control Project Work · Figure 2-7 |
| EVM Standard §4–6 | EVM metrics definitions and reporting |
| Process-Groups §4.5 | Monitor and Control Project Work outputs |

---

*Owner: Project Manager · Frequency: Per A28 communications plan · Final: At closure per SKL-06-02*
*Last Updated: 2026-05-30 · Patch E*

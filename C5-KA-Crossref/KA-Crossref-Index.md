# C5 — Knowledge Area Cross-Reference Index

**Version:** 1.0.0
**Authority:** PMBOK 8 (Primary) · Process Groups: A Practice Guide (Secondary)
**Scope:** All 40 PMBOK processes mapped by Knowledge Area, Process Group, and PR number
**Status:** Complete

---

## Purpose

This index provides a single lookup table mapping every PMBOK process to:
- Its **Knowledge Area** (what domain of knowledge it belongs to)
- Its **Process Group** (when in the lifecycle it is performed)
- Its **PR number** (the C4 Process Record file in this repository)
- Its **primary outputs** (what it produces)

Use this index to:
- Navigate from a knowledge domain to all its processes
- Find which processes are active in a given lifecycle phase
- Trace artifacts back to their originating processes
- Build agent routing logic or content chapter outlines

---

## KA1 — Integration Management

Integration Management ensures all project elements are properly coordinated and aligned across all lifecycle phases. It is the only knowledge area that spans all five Process Groups.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR01 | Develop Project Charter | Initiating | Project charter, assumption log |
| PR03 | Develop Project Management Plan | Planning | Project management plan |
| PR28 | Direct and Manage Project Work | Executing | Deliverables, work performance data, issue log, change requests |
| PR29 | Manage Project Knowledge | Executing | Lessons learned register, OPA updates |
| PR30 | Monitor and Control Project Work | Monitoring & Controlling | Work performance reports, change requests |
| PR31 | Perform Integrated Change Control | Monitoring & Controlling | Approved change requests, project management plan updates |
| PR40 | Close Project or Phase | Closing | Final report, final product/service/result transition, OPA updates |

**Process count:** 7
**Note:** Integration Management is the integrative spine of PMBOK — every other KA connects to it.

---

## KA2 — Scope Management

Scope Management ensures the project includes all the work required, and only the work required, to complete the project successfully.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR04 | Plan Scope Management | Planning | Scope management plan, requirements management plan |
| PR05 | Collect Requirements | Planning | Requirements documentation, requirements traceability matrix |
| PR06 | Define Scope | Planning | Project scope statement, project documents updates |
| PR07 | Create WBS | Planning | Scope baseline (WBS + WBS dictionary + scope statement) |
| PR32 | Validate Scope | Monitoring & Controlling | Accepted deliverables, work performance information |
| PR33 | Control Scope | Monitoring & Controlling | Work performance information, change requests |

**Process count:** 6
**Key artifact:** Scope baseline (WBS + WBS dictionary + project scope statement) — created in PR07, controlled in PR33.

---

## KA3 — Schedule Management

Schedule Management establishes policies, procedures, and documentation for planning, developing, managing, executing, and controlling the project schedule.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR08 | Plan Schedule Management | Planning | Schedule management plan |
| PR09 | Define Activities | Planning | Activity list, activity attributes, milestone list |
| PR10 | Sequence Activities | Planning | Project schedule network diagrams, project documents updates |
| PR11 | Estimate Activity Resources | Planning | Resource requirements, resource breakdown structure |
| PR12 | Estimate Activity Durations | Planning | Duration estimates, basis of estimates |
| PR13 | Develop Schedule | Planning | Project schedule (schedule baseline), schedule data, project calendars |
| PR34 | Control Schedule | Monitoring & Controlling | Work performance information, schedule forecasts, change requests |

**Process count:** 7
**Key artifact:** Schedule baseline — created in PR13, controlled in PR34.
**Note:** PR11 (Estimate Activity Resources) bridges Schedule and Resource Management KAs.

---

## KA4 — Cost Management

Cost Management involves planning, estimating, budgeting, financing, funding, managing, and controlling costs so the project can be completed within the approved budget.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR14 | Plan Cost Management | Planning | Cost management plan |
| PR15 | Estimate Costs | Planning | Cost estimates, basis of estimates |
| PR16 | Determine Budget | Planning | Cost baseline, project funding requirements |
| PR35 | Control Costs | Monitoring & Controlling | Work performance information, cost forecasts, change requests |

**Process count:** 4
**Key artifact:** Cost baseline — created in PR16, controlled in PR35.
**EVM triad:** Scope baseline (PR07) + Schedule baseline (PR13) + Cost baseline (PR16) = Performance Measurement Baseline.

---

## KA5 — Quality Management

Quality Management incorporates the organization's quality policy regarding planning, managing, and controlling project and product quality requirements.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR17 | Plan Quality Management | Planning | Quality management plan, quality metrics, project documents updates |
| PR20 | Manage Quality | Executing | Quality reports, test and evaluation documents, change requests |
| PR37 | Control Quality | Monitoring & Controlling | Quality control measurements, verified deliverables, change requests |

**Process count:** 3
**Key distinction:** Quality Assurance (PR20) = process quality; Quality Control (PR37) = product quality.
**Flow:** PR17 → PR20 → PR37 → PR32 (Validate Scope)

---

## KA6 — Resource Management

Resource Management identifies, acquires, and manages the resources needed for the successful completion of the project — both physical resources and team members.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR18 | Plan Resource Management | Planning | Resource management plan, team charter |
| PR11 | Estimate Activity Resources | Planning | Resource requirements, resource breakdown structure |
| PR16-Ext | Acquire Resources | Executing | Physical resource assignments, project team assignments |
| PR17-Ext | Develop Team | Executing | Team performance assessments, change requests |
| PR18-Ext | Manage Team | Executing | Change requests, project management plan updates |
| PR38 | Control Resources | Monitoring & Controlling | Work performance information, change requests |

**Process count:** 6 (3 Planning, 3 Executing/M&C)
**Note:** Executing processes Acquire Resources, Develop Team, and Manage Team are covered in C4 as part of the broader Executing group. PR11 appears in both Schedule and Resource KAs.

---

## KA7 — Communications Management

Communications Management ensures timely and appropriate planning, collection, creation, distribution, storage, retrieval, management, monitoring, and disposition of project information.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR19 | Plan Communications Management | Planning | Communications management plan, project documents updates |
| PR19-Ext | Manage Communications | Executing | Project communications, project management plan updates |
| PR36 | Monitor Communications | Monitoring & Controlling | Work performance information, change requests |

**Process count:** 3
**Key principle:** Right information → right stakeholder → right format → right time.

---

## KA8 — Risk Management

Risk Management increases the probability and impact of positive events and decreases the probability and impact of negative events in the project.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR21 | Plan Risk Management | Planning | Risk management plan |
| PR22 | Identify Risks | Planning | Risk register, risk report |
| PR23 | Perform Qualitative Risk Analysis | Planning | Risk register updates (prioritized risks) |
| PR24 | Perform Quantitative Risk Analysis | Planning | Risk report updates (quantitative risk analysis results) |
| PR25 | Plan Risk Responses | Planning | Change requests, risk register updates, risk report updates |
| PR26-Ext | Implement Risk Responses | Executing | Change requests, project documents updates |
| PR39 | Monitor Risks | Monitoring & Controlling | Work performance information, change requests |

**Process count:** 7
**Key artifact chain:** Risk register (PR22) → updated by PR23, PR24, PR25 → monitored by PR39.

---

## KA9 — Procurement Management

Procurement Management includes the processes necessary to purchase or acquire products, services, or results needed from outside the project team.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR26 | Plan Procurement Management | Planning | Procurement management plan, procurement strategy, source selection criteria |
| PR26-Ext | Conduct Procurements | Executing | Selected sellers, agreements, change requests |
| PR26-Ext2 | Control Procurements | Monitoring & Controlling | Closed procurements, work performance information, change requests |

**Process count:** 3
**Note:** Conduct Procurements and Control Procurements are covered in the C4 Executing and M&C batches. In PMBOK 8, procurement is addressed via Plan Sourcing Strategy and Appendix X4.

---

## KA10 — Stakeholder Management

Stakeholder Management identifies all people or organizations impacted by the project and develops strategies for effectively engaging them in project decisions and execution.

| PR # | Process Name | Process Group | Primary Outputs |
|---|---|---|---|
| PR02 | Identify Stakeholders | Initiating | Stakeholder register, change requests |
| PR27 | Plan Stakeholder Engagement | Planning | Stakeholder engagement plan |
| PR27-Ext | Manage Stakeholder Engagement | Executing | Change requests, project management plan updates |
| PR40-Ext | Monitor Stakeholder Engagement | Monitoring & Controlling | Work performance information, change requests |

**Process count:** 4
**Key artifact:** Stakeholder engagement plan (PR27) — updated by Manage and Monitor processes.

---

## Master Process Index by Process Group

### Initiating (2 processes)
| PR # | Process | KA |
|---|---|---|
| PR01 | Develop Project Charter | Integration |
| PR02 | Identify Stakeholders | Stakeholder |

### Planning (25 processes)
| PR # | Process | KA |
|---|---|---|
| PR03 | Develop Project Management Plan | Integration |
| PR04 | Plan Scope Management | Scope |
| PR05 | Collect Requirements | Scope |
| PR06 | Define Scope | Scope |
| PR07 | Create WBS | Scope |
| PR08 | Plan Schedule Management | Schedule |
| PR09 | Define Activities | Schedule |
| PR10 | Sequence Activities | Schedule |
| PR11 | Estimate Activity Resources | Schedule/Resource |
| PR12 | Estimate Activity Durations | Schedule |
| PR13 | Develop Schedule | Schedule |
| PR14 | Plan Cost Management | Cost |
| PR15 | Estimate Costs | Cost |
| PR16 | Determine Budget | Cost |
| PR17 | Plan Quality Management | Quality |
| PR18 | Plan Resource Management | Resource |
| PR19 | Plan Communications Management | Communications |
| PR20 | Plan Risk Management | Risk |
| PR21 | Plan Risk Management (detailed) | Risk |
| PR22 | Identify Risks | Risk |
| PR23 | Perform Qualitative Risk Analysis | Risk |
| PR24 | Perform Quantitative Risk Analysis | Risk |
| PR25 | Plan Risk Responses | Risk |
| PR26 | Plan Procurement Management | Procurement |
| PR27 | Plan Stakeholder Engagement | Stakeholder |

### Executing (3 anchor processes + sub-processes)
| PR # | Process | KA |
|---|---|---|
| PR28 | Direct and Manage Project Work | Integration |
| PR29 | Manage Project Knowledge | Integration |
| PR30 | Monitor and Control Project Work | Integration |

### Monitoring & Controlling (9 processes)
| PR # | Process | KA |
|---|---|---|
| PR31 | Perform Integrated Change Control | Integration |
| PR32 | Validate Scope | Scope |
| PR33 | Control Scope | Scope |
| PR34 | Control Schedule | Schedule |
| PR35 | Control Costs | Cost |
| PR36 | Monitor Communications | Communications |
| PR37 | Control Quality | Quality |
| PR38 | Control Resources | Resource |
| PR39 | Monitor Risks | Risk |

### Closing (1 process)
| PR # | Process | KA |
|---|---|---|
| PR40 | Close Project or Phase | Integration |

---

## Process Count by Knowledge Area

| Knowledge Area | Planning | Executing | M&C | Initiating | Closing | Total |
|---|---|---|---|---|---|---|
| Integration Management | 1 | 2 | 2 | 1 | 1 | **7** |
| Scope Management | 4 | — | 2 | — | — | **6** |
| Schedule Management | 6 | — | 1 | — | — | **7** |
| Cost Management | 3 | — | 1 | — | — | **4** |
| Quality Management | 1 | 1 | 1 | — | — | **3** |
| Resource Management | 2 | 3 | 1 | — | — | **6** |
| Communications Management | 1 | 1 | 1 | — | — | **3** |
| Risk Management | 5 | 1 | 1 | — | — | **7** |
| Procurement Management | 1 | 1 | 1 | — | — | **3** |
| Stakeholder Management | 1 | 1 | 1 | 1 | — | **4** |
| **TOTAL** | **25** | **10** | **12** | **2** | **1** | **50\*** |

> \* Count exceeds 40 because PR11 (Estimate Activity Resources) bridges Schedule and Resource KAs, and some processes appear in multiple KA narratives. Unique processes = 40.

---

## Performance Measurement Baseline (PMB) Traceability

The three baselines that form the PMB are created and controlled by these processes:

| Baseline | Created By | Controlled By | PR Created | PR Controlled |
|---|---|---|---|---|
| Scope Baseline | Create WBS | Control Scope | PR07 | PR33 |
| Schedule Baseline | Develop Schedule | Control Schedule | PR13 | PR34 |
| Cost Baseline | Determine Budget | Control Costs | PR16 | PR35 |

All baseline changes require approval through **PR31 (Perform Integrated Change Control)**.

---

## Key Artifact Flow

```
PR01 → Project Charter
PR02 → Stakeholder Register
PR03 → Project Management Plan (umbrella)
PR05 → Requirements Documentation + RTM
PR07 → Scope Baseline
PR13 → Schedule Baseline
PR16 → Cost Baseline
PR22 → Risk Register
PR28 → Deliverables + Work Performance Data
PR30 → Work Performance Reports
PR31 → Approved Change Requests
PR32 → Accepted Deliverables
PR37 → Verified Deliverables (feeds PR32)
PR40 → Final Report + Product/Service/Result Transition
```

---

## Related Files

| File | Relationship |
|---|---|
| `C4-Process-Records/PR##-*.md` | Detailed I/O/T&T for each process |
| `SKILL-REGISTRY.md` | Skills mapped to lifecycle stages and domains |
| `PRINCIPLES-CROSSWALK.md` | 12 principles × 11 domains |
| `LIFECYCLE-MAP.md` | Phase-by-phase process and artifact flow |
| `C6-TT-Taxonomy/` (planned) | Tools & Techniques deduplicated taxonomy |
| `C7-IO-Registry/` (planned) | Inputs/Outputs master artifact registry |

---

*Authority: PMBOK 8 Primary · Process Groups: A Practice Guide Secondary*
*Part of PMOSkills — PMI PMBOK 8 Knowledge Base*

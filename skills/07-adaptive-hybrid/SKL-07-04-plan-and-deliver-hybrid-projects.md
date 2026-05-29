# SKL-07-04 — Plan and Deliver Hybrid Projects

**Skill ID:** SKL-07-04  
**Pack:** 07 — Adaptive & Hybrid  
**Version:** 1.0.0  
**Status:** Active  
**Authority:** PMI-derived  
**Primary Reference:** PMBOK 8 Standard §4.2.3 (Hybrid Approaches) · PMBOK 8 Guide §2.3 · APG §3.1.6–3.1.11  
**Secondary References:** APG §3.1.7–3.1.10 (Hybrid Patterns) · DA Toolkit (Hybrid Levels 1–3) · Artifacts-V-1.0.2.md (Item 75 — Approach-Tailored Scope Structure Elaboration Blueprint)  
**Lifecycle Stage:** Planning · Executing · Monitoring & Controlling  
**Performance Domains:** Development Approach and Life Cycle · Planning · Delivery · Governance  
**PMBOK 8 Principles Applied:** Stewardship · Value · Adaptability · Systems Thinking · Governance  

---

## Purpose

Design, plan, and deliver a project that intentionally combines predictive and adaptive approaches across different streams, phases, or workstreams. This skill operationalizes hybrid lifecycle patterns, defines how governance, planning, and measurement work differently across streams, and ensures integration points between predictive and adaptive components are explicitly managed.

---

## Scope

| In Scope | Out of Scope |
|---|---|
| Defining hybrid project structure (streams, phases, cadences) | Full predictive delivery (see Packs 03–05) |
| Mapping each deliverable to its approach (predictive vs. adaptive) | Full adaptive delivery (see SKL-07-01 through 07-03) |
| Designing integration points between streams | Organizational hybrid transformation |
| Tailoring governance for dual-approach contexts | Program-level hybrid management |
| Hybrid schedule: high-level milestones + iterative cadence | |
| Hybrid change control model | |
| Hybrid measurement and reporting | |

---

## Trigger Conditions

Activate this skill when:
- SKL-07-01 has selected a Hybrid (Level 1, 2, or 3) lifecycle approach
- A project has two or more deliverable streams with different certainty profiles
- An organization is transitioning from predictive to adaptive and needs a structured hybrid path
- External constraints (regulatory, contractual, vendor) require a predictive component within an otherwise adaptive project

---

## The Four Hybrid Patterns (PMBOK 8 §4.2.3)

| Pattern | Structure | Example Use Case |
|---|---|---|
| **P1: Adaptive → Predictive rollout** | Agile development phase followed by structured rollout/deployment | Drug development trials (agile) + FDA approval (predictive) |
| **P2: Adaptive + Predictive simultaneously** | Separate parallel streams; different teams, different cadences | Software (agile) + Data center build (predictive) running in parallel |
| **P3: Largely predictive + Adaptive component** | Routine project with one innovative or uncertain workstream | Construction project with new smart-building IT component |
| **P4: Largely adaptive + Predictive component** | Agile-dominant project with one fixed external integration | Mobile app (agile) + external OECD calculation module (predictive) |

---

## Hybrid Project Structure Template

```markdown
## Hybrid Project Structure (A06 §2 — Hybrid Extension)

**Project Name:**
**Hybrid Pattern:** [ ] P1  [ ] P2  [ ] P3  [ ] P4
**DA Hybrid Level:** [ ] Level 1 (Predictive dominant)  [ ] Level 2 (Both significant)  [ ] Level 3 (Adaptive dominant)

---

### Stream Map
| Stream ID | Stream Name | Approach | Cadence | Lead | Key Deliverables |
|---|---|---|---|---|---|
| STR-01 | | [ ] Predictive  [ ] Adaptive | | | |
| STR-02 | | [ ] Predictive  [ ] Adaptive | | | |

---

### Integration Points
| Integration Point ID | Description | STR from | STR to | Dependency Type | Date / Trigger |
|---|---|---|---|---|---|
| INT-01 | | | | [ ] Hard dependency  [ ] Soft dependency | |

---

### Governance Model per Stream
| Stream | Governance Type | Change Authority | Review Cadence |
|---|---|---|---|
| STR-01 (Predictive) | Structured — phase gates, CCB | Change Control Board | Phase gate |
| STR-02 (Adaptive) | Guided self-governance | Product Owner + PM | Sprint review |

---

### Schedule Architecture
| Level | Planning Approach | Artifact |
|---|---|---|
| High-level milestones | Predictive — planned upfront | Master schedule (A15) |
| Predictive stream detail | WBS + Gantt | A08 WBS + A15 schedule |
| Adaptive stream cadence | Backlog + sprint cadence | A08 backlog |
| Release plan | Iteration-based delivery plan | Release roadmap |

---

### Change Control Architecture
| Change Type | Stream | Process | Authority |
|---|---|---|---|
| Scope change (predictive stream) | STR-01 | Formal CCB via SKL-05-02 | CCB / T2–T3 |
| Backlog reprioritization (adaptive stream) | STR-02 | Product Owner decision | Product Owner / T1 |
| Integration point change | Either | CCB — cross-stream impact | T2–T3 |
| Approach change (adaptive ↔ predictive) | Any | Governing body | T3 |

---

### Reporting Model
| Report Type | Stream | Frequency | Format |
|---|---|---|---|
| EVM performance report | Predictive stream | Weekly / biweekly | A17 |
| Sprint velocity + burndown | Adaptive stream | Per sprint | Sprint report |
| Integrated project status | Whole project | Weekly | Combined dashboard |
| Integration point status | Both | At each integration event | Integration brief |
```

---

## Hybrid Governance Design

### Structured Governance (Predictive Streams)
- Phase gates with formal entry/exit criteria
- Change Control Board for scope changes
- Formal change requests (SKL-05-02)
- Progress tracked against baseline (EVM)

### Guided Self-Governance (Adaptive Streams)
- Sprint planning as planning mechanism
- Product Owner as scope authority within sprint
- Backlog prioritization as continuous planning
- Team empowered to determine “how”; PO determines “what”

### Hybrid Governance Bridges
- **Integration point reviews** — formal gateway when adaptive output feeds predictive stream
- **Cross-stream dependency management** — shared risk register covers both streams
- **Joint status reporting** — single integrated dashboard for sponsor/PMO
- **Change escalation path** — clear threshold for when adaptive change requires CCB review

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| Project Charter | A01 | Objectives, constraints, delivery expectations |
| Hybrid Lifecycle Selection | A06 §2 (from SKL-07-01) | Pattern and DA level already selected |
| Requirements Documentation | A08 | Identifies which requirements are stable vs. evolving |
| Risk Register | A19 | Risk profile per stream |
| Stakeholder Register | A10 | Stakeholder preferences for delivery cadence and visibility |
| OPA / PMO Standards | A05 | Org-defined hybrid templates and governance requirements |
| Team Profile | HR / Resource data | Team skills, agile experience, location |

---

## Tools and Techniques

| Tool / Technique | Application |
|---|---|
| Stream Mapping | Identify deliverables and assign predictive vs. adaptive approach |
| Integration Point Analysis | Map dependencies between streams; identify hard vs. soft dependencies |
| Rolling Wave Planning | High-level predictive milestones + iterative sprint planning for adaptive portions |
| Hybrid Governance Design | Define change control and review cadence per stream |
| Expert Judgment | PM + PMO design hybrid structure based on experience |
| Meetings — Hybrid Kickoff | Align all streams on structure, integration points, and governance |
| Risk Management (cross-stream) | Assess risks that span both streams, especially at integration points |

---

## Outputs

| Output | Artifact | Notes |
|---|---|---|
| Hybrid Project Structure | A06 §2 (extended) | Stream map, integration points, governance model |
| Master Schedule (high-level milestones) | A15 | Covers all streams; adaptive sprints shown as blocks |
| Release Roadmap | A08 (release section) | Adaptive delivery plan; shows sprint-to-milestone mapping |
| Integrated Risk Register | A19 | Cross-stream risks, especially at integration points |
| Hybrid Reporting Dashboard | A17 | Combined EVM + velocity view |

---

## Common Hybrid Anti-Patterns to Avoid

| Anti-Pattern | Description | Correction |
|---|---|---|
| **Waterfall with agile vocabulary** | Sprints used but scope is fully locked; no backlog flexibility | Genuinely allow scope to flex in adaptive streams |
| **Change control applied to backlog** | Every backlog item requires CCB approval | Separate: CCB for baseline changes; PO for backlog reprioritization |
| **Ignoring integration points** | Adaptive stream finishes but predictive stream not ready to receive | Formally track integration points in schedule and risk register |
| **Different velocity definitions** | Predictive and adaptive teams measure progress differently, confusing sponsors | Define unified reporting layer: EVM for predictive, velocity for adaptive, combined dashboard for sponsor |
| **Adaptive team overridden by predictive governance** | PMO applies full change control to sprint backlog | Educate PMO on guided self-governance; define clear boundary |

---

## Authority Routing

| Decision | Authority Level | Threshold |
|---|---|---|
| Approve hybrid structure | PM + Sponsor + PMO | T2–T3 |
| Change integration point schedule | PM + CCB | T2 |
| Reprioritize adaptive backlog | Product Owner | T1 |
| Change scope in predictive stream | CCB | T2–T3 |
| Change approach of any stream | Governing Body | T3 |
| Terminate a stream | Sponsor + Governing Body | T3 |

---

## Validation Criteria

This skill output is valid when:
- [ ] All deliverable streams are mapped to a specific approach (predictive or adaptive)
- [ ] Hybrid pattern (P1–P4) is identified and documented in A06 §2
- [ ] DA Hybrid Level (1–3) is assigned
- [ ] All integration points are identified with dependency type and trigger
- [ ] Governance model is defined per stream with clear change authority
- [ ] Reporting model covers both EVM (predictive) and velocity/burndown (adaptive)
- [ ] Hybrid kickoff conducted and all stream leads aligned

---

## Failure Cases

| Failure | Indicator | Resolution |
|---|---|---|
| No stream separation | Project called “hybrid” but managed entirely predictively | Perform stream mapping; assign approach per deliverable |
| Integration points not tracked | Adaptive stream finishes but predictive stream is not ready | Add integration points to risk register and master schedule |
| Reporting confusion | Sponsor asks “how are we doing?” and gets two incompatible reports | Create unified hybrid dashboard |
| Governance mismatch | Product Owner decisions constantly escalated to CCB | Clarify governance boundaries; educate stakeholders |
| Approach change not controlled | Mid-project switch from agile to waterfall without governance | Require T3 governing body decision; document rationale |

---

## Linked Skills

| Skill ID | Skill Name | Relationship |
|---|---|---|
| SKL-07-01 | Select and Tailor Lifecycle Approach | Prerequisite — hybrid selected before this skill activates |
| SKL-07-02 | Manage Backlog and Iterations | Governs adaptive streams |
| SKL-07-03 | Facilitate Retrospectives | Both streams benefit; cadence differs |
| SKL-05-02 | Perform Integrated Change Control | Governs predictive stream changes and cross-stream changes |
| SKL-03-01 | Develop Project Management Plan | A06 is updated with hybrid structure |
| SKL-05-01 | Monitor and Control Project Work | Cross-stream performance monitoring |

---

*Authority: PMI-derived — PMBOK 8 Standard §4.2.3 · APG §3.1.6–3.1.11 · DA Toolkit Hybrid Levels 1–3*  
*PMO Skill Repository v1.0.0 · Pack 07 — Adaptive & Hybrid*

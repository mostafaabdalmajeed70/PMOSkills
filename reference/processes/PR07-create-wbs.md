---
reference_type: Process
reference_id: PR07
name: Create WBS
process_group: Planning
knowledge_area: Project Scope Management
version: "1.0.0"
status: Active
pmbok8_source: "Process Groups: A Practice Guide § 3.5 — Create WBS"
authority: PMI-derived
---

# PR07 — Create WBS
**Type:** Process
**Process Group:** Planning
**Knowledge Area:** Project Scope Management
**PMBOK8 Source:** Process Groups: A Practice Guide § 3.5
**Version:** 1.0.0

## Definition
Create WBS is the process of subdividing project deliverables and project work into smaller, more manageable components (PG:APG § 3.5). The Work Breakdown Structure (WBS) organizes the total scope of the project into work packages — the lowest level of the WBS — which represent deliverable-oriented groupings of work. The WBS is the foundation for all subsequent planning: schedule, cost, resource, and risk all trace to WBS elements.

## Purpose
To decompose the full project scope into discrete, manageable work packages that can be estimated, assigned, scheduled, and controlled, providing the structural backbone for all other planning.

## Key Inputs
| Input | Source |
|---|---|
| Project Management Plan (scope management plan) | PR04 |
| Project documents (project scope statement, requirements documentation) | PR06/PR05 |
| Enterprise Environmental Factors (EEFs) | Organization |
| Organizational Process Assets (OPAs) | Organization |

## Key Tools and Techniques
| Tool / Technique | Description |
|---|---|
| Expert judgment | Using decomposition experience to determine appropriate WBS depth |
| Decomposition | Breaking down deliverables into progressively smaller components until work packages are reached |

## Key Outputs
| Output | Description |
|---|---|
| Scope Baseline | WBS + WBS Dictionary + Project Scope Statement (the full scope baseline) |
| Project documents updates | Updates to assumption log and requirements documentation |

## Key Characteristics
- **Deliverable-oriented:** Every WBS element is a deliverable or component of a deliverable — not an activity or action; this distinguishes the WBS from a schedule activity list (PG:APG § 3.5, WBS-3E).
- **100% rule:** The WBS must capture 100% of the work defined in the project scope statement — nothing more, nothing less (WBS-3E).
- **Work package level:** Decomposition continues until work packages are small enough to be estimated, assigned, and controlled — typically 8–80 hours of effort (WBS-3E).
- **WBS Dictionary:** Every WBS element has a corresponding WBS Dictionary entry describing the work, responsible party, milestones, quality requirements, and resource requirements (PG:APG § 3.5).
- **Scope baseline:** The WBS, WBS Dictionary, and approved scope statement together constitute the scope baseline — the formal benchmark for scope control (PG:APG § 3.5).

## Relationship to Other Processes
| Process | Relationship |
|---|---|
| PR06 — Define Scope | Scope statement is the primary input to WBS decomposition |
| PR09 — Define Activities | Activities are defined by decomposing WBS work packages further into schedule activities |
| PR14 — Estimate Costs | Cost estimates are developed at the work package level, rolling up through the WBS |
| PR40 — Control Scope | Scope changes are assessed against the scope baseline (WBS + scope statement) |

## Artifact Connections
| Artifact | Connection |
|---|---|
| A08 — Scope and Requirements Backlog | Requirements in this artifact map to WBS work packages via traceability |
| A14 — Integrated Project Management Plan | Scope baseline (WBS + WBS Dictionary + scope statement) is a component of the PMP |
| A15 — Schedule Baseline | Built from schedule activities decomposed from WBS work packages |

## Skill Connections
| Skill ID | Skill Name | Connection |
|---|---|---|
| SKL-03-02 | Define and Manage Scope | The WBS is the primary deliverable of scope definition work |
| SKL-03-04 | Build WBS and Schedule | This process is the PMBOK 8 anchor for WBS creation |

## Questions to Ask in Practice
1. Does every element in the WBS represent a deliverable, not a task or activity — and have activities been kept out of the WBS and reserved for schedule planning?
2. Does the WBS account for 100% of the scope defined in the scope statement — including management work, quality activities, and integration work?
3. Is the WBS Dictionary complete enough that a new team member could understand what work is required for any element without needing to ask the PM?
4. Have work packages been decomposed to a level where reliable estimates can be produced, or are some work packages still too large to estimate confidently?

*Authority: Process Groups: A Practice Guide § 3.5 · Practice Standard for Work Breakdown Structures (3rd Ed.) · Source type: PMI-derived*
*Repository: https://github.com/fakhruldeen/PMOSkills*

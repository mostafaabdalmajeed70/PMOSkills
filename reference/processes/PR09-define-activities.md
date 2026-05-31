---
reference_type: Process
reference_id: PR09
name: Define Activities
process_group: Planning
knowledge_area: Project Schedule Management
version: "1.0.0"
status: Active
pmbok8_source: "Process Groups: A Practice Guide § 3.7 — Define Activities"
authority: PMI-derived
---

# PR09 — Define Activities
**Type:** Process
**Process Group:** Planning
**Knowledge Area:** Project Schedule Management
**PMBOK8 Source:** Process Groups: A Practice Guide § 3.7
**Version:** 1.0.0

## Definition
Define Activities is the process of identifying and documenting the specific actions to be performed to produce the project deliverables (PG:APG § 3.7). It decomposes WBS work packages into schedule activities — the smallest units of schedulable work — producing the activity list, activity attributes, and milestone list that feed into sequencing, estimating, and scheduling.

## Purpose
To translate the WBS from deliverable-oriented work packages into action-oriented schedule activities that can be assigned, sequenced, estimated, and tracked.

## Key Inputs
| Input | Source |
|---|---|
| Project Management Plan (schedule management plan, scope baseline) | PR08, PR07 |
| Enterprise Environmental Factors (EEFs) | Organization |
| Organizational Process Assets (OPAs) | Organization |

## Key Tools and Techniques
| Tool / Technique | Description |
|---|---|
| Expert judgment | Decomposition experience for the project type |
| Decomposition | Breaking WBS work packages into schedule activities |
| Rolling wave planning | Progressive elaboration of near-term activities while future activities remain at higher levels |
| Meetings | Activity definition workshops with team members |

## Key Outputs
| Output | Description |
|---|---|
| Activity List | Comprehensive list of all schedule activities required for the project |
| Activity Attributes | Detailed attributes for each activity: description, predecessor/successor, resource requirements, constraints |
| Milestone List | List of significant project milestones with dates and whether mandatory or optional |
| Change Requests | If decomposition reveals scope gaps or errors |
| Project Management Plan updates | Updates to schedule and scope baselines if scope gaps are found |

## Key Characteristics
- **Action-oriented decomposition:** Activities are actions (“Develop,” “Test,” “Review”) while WBS elements are deliverables — this distinction is critical for schedule integrity (PG:APG § 3.7).
- **WBS traceability:** Every activity must trace to a WBS work package; activities without WBS parents indicate unplanned scope (PG:APG § 3.7).
- **Rolling wave support:** Not all activities need to be defined at the same level of detail at the same time — near-term activities are defined in detail, future activities in lower detail (PG:APG § 3.7).
- **Milestone identification:** Milestones are zero-duration events marking the completion of a significant deliverable or decision point (PG:APG § 3.7).

## Relationship to Other Processes
| Process | Relationship |
|---|---|
| PR07 — Create WBS | WBS work packages are the input decomposed into activities here |
| PR10 — Sequence Activities | Activity list is the primary input to sequencing |
| PR11 — Estimate Activity Durations | Activity attributes from this process inform duration estimates |
| PR18 — Estimate Activity Resources | Activity list is used to estimate resources required |

## Artifact Connections
| Artifact | Connection |
|---|---|
| A15 — Schedule Baseline | Built from the activity list and attributes produced by this process |
| A14 — Integrated Project Management Plan | Activity list and milestone list are referenced within the schedule component |

## Skill Connections
| Skill ID | Skill Name | Connection |
|---|---|---|
| SKL-03-04 | Build WBS and Schedule | Define Activities is a core step within the schedule building skill |

## Questions to Ask in Practice
1. Is every activity in the activity list traceable to a WBS work package — are there any orphan activities with no parent deliverable?
2. Are activity attributes complete enough for team members to understand what is expected without requiring verbal explanation?
3. Has rolling wave planning been applied deliberately, or have future activities been defined at the same granularity as near-term activities — creating false precision?
4. Are mandatory milestones (contractual, regulatory) clearly distinguished from optional milestones in the milestone list?

*Authority: Process Groups: A Practice Guide § 3.7 · Practice Standard for Scheduling (3rd Ed.) · Source type: PMI-derived*
*Repository: https://github.com/fakhruldeen/PMOSkills*

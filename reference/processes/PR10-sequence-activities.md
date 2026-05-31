---
reference_type: Process
reference_id: PR10
name: Sequence Activities
process_group: Planning
knowledge_area: Project Schedule Management
version: "1.0.0"
status: Active
pmbok8_source: "Process Groups: A Practice Guide § 3.8 — Sequence Activities"
authority: PMI-derived
---

# PR10 — Sequence Activities
**Type:** Process
**Process Group:** Planning
**Knowledge Area:** Project Schedule Management
**PMBOK8 Source:** Process Groups: A Practice Guide § 3.8
**Version:** 1.0.0

## Definition
Sequence Activities is the process of identifying and documenting relationships among the project activities (PG:APG § 3.8). Every activity except the first and last must have at least one predecessor and one successor. The network diagram produced by this process models the logical flow of work and is the foundation for critical path analysis, schedule compression, and resource optimization.

## Purpose
To establish the logical order of all project activities by defining their dependencies, enabling the development of a realistic, network-based project schedule that reflects how work actually must be sequenced.

## Key Inputs
| Input | Source |
|---|---|
| Project Management Plan (schedule management plan, scope baseline) | PR08, PR07 |
| Project documents (activity attributes, activity list, assumption log, milestone list) | PR09 |
| Enterprise Environmental Factors (EEFs) | Organization |
| Organizational Process Assets (OPAs) | Organization |

## Key Tools and Techniques
| Tool / Technique | Description |
|---|---|
| Precedence Diagramming Method (PDM) | Node-based network diagram using Finish-to-Start, Start-to-Start, Finish-to-Finish, Start-to-Finish relationships |
| Dependency determination and integration | Classifying dependencies as mandatory (hard logic), discretionary (soft logic), external, or internal |
| Leads and lags | Adjusting dependency timing — leads allow overlap, lags introduce waiting time |
| Project Management Information System (PMIS) | Software tools for network diagram creation |

## Key Outputs
| Output | Description |
|---|---|
| Project Schedule Network Diagrams | Visual or data representations of activity sequences and logical relationships |
| Project documents updates | Updates to activity attributes, activity list, assumption log, milestone list |

## Key Characteristics
- **Every activity must connect:** Except the start and end activities, every activity must have at least one predecessor and one successor — islands indicate planning gaps (PG:APG § 3.8).
- **Four dependency types:** Finish-to-Start (FS), Start-to-Start (SS), Finish-to-Finish (FF), Start-to-Finish (SF) — FS is the most common; SF is rarely used (PG:APG § 3.8, PSS-3E).
- **Dependency classification:** Mandatory dependencies (hard logic, physical or contractual) must be respected; discretionary dependencies (soft logic) represent best practices and can be changed to compress the schedule (PG:APG § 3.8).
- **Critical path prerequisite:** The network diagram is the input required for critical path method analysis in PR12 (PG:APG § 3.8).
- **Leads and lags with caution:** Excessive use of lags introduces schedule risk; leads that are unrealistic create false confidence in compressed timelines (PG:APG § 3.8).

## Relationship to Other Processes
| Process | Relationship |
|---|---|
| PR09 — Define Activities | Activity list and attributes are the primary input to sequencing |
| PR11 — Estimate Activity Durations | Duration estimates are applied to the sequenced network |
| PR12 — Develop Schedule | Network diagrams are a primary input to schedule development and critical path analysis |
| PR41 — Control Schedule | Network dependencies are referenced when assessing the impact of schedule changes |

## Artifact Connections
| Artifact | Connection |
|---|---|
| A15 — Schedule Baseline | Network sequence logic is embedded in the schedule baseline |
| A14 — Integrated Project Management Plan | Network structure informs the schedule management approach described in the PMP |

## Skill Connections
| Skill ID | Skill Name | Connection |
|---|---|---|
| SKL-03-04 | Build WBS and Schedule | Activity sequencing is a core step in schedule construction |

## Questions to Ask in Practice
1. Are mandatory dependencies clearly distinguished from discretionary dependencies — and have the discretionary ones been challenged to explore schedule compression opportunities?
2. Are there any activities in the network with no predecessor or successor (other than the start and end milestones) that might indicate sequencing gaps?
3. Have leads and lags been used judiciously — are they realistic, or have they been used to force an unrealistically compressed schedule?
4. Does the network diagram reflect how work will actually be sequenced by the team, or does it reflect an idealized sequence that the team won’t follow in practice?

*Authority: Process Groups: A Practice Guide § 3.8 · Practice Standard for Scheduling (3rd Ed.) · Source type: PMI-derived*
*Repository: https://github.com/fakhruldeen/PMOSkills*

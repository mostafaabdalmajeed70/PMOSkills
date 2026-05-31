# PR10 — Sequence Activities

**Type:** Process Record  
**Primary Source:** PMBOK 8 — Schedule Performance Domain  
**Companion Source:** Process Groups: A Practice Guide — 5.8 Sequence Activities  
**Process Group:** Planning  
**Version:** 1.0.0  
**Status:** Active

## Definition

Sequence Activities is the process of identifying and documenting relationships among the project activities to establish the logical order in which activities will be performed.

## Purpose

This process establishes the schedule network by defining the logical dependencies among activities. Every activity except the first and last should connect to at least one predecessor and one successor. The resulting project schedule network diagram provides the structural basis for critical path analysis, schedule compression, and resource optimization. These logical relationships directly affect the schedule baseline and execution sequencing.

## When Used

This process follows Define Activities (PR09) and is performed during Planning. It is repeated as needed when activities are added or changed, especially in rolling-wave and adaptive projects.

## Key Inputs

- Project management plan, especially the schedule management plan (from PR08) and scope baseline.
- Project documents, including the activity list and attributes (from PR09), assumption log, milestone list, and risk register.
- Enterprise environmental factors.
- Organizational process assets.

## Key Tools and Techniques

- Precedence diagramming method (PDM).
- Dependency determination and integration, distinguishing mandatory, discretionary, internal, and external dependencies.
- Leads and lags.
- Project management information system (PMIS).

## Key Outputs

- Project schedule network diagram.
- Project document updates, including activity list, activity attributes, assumption log, and milestone list updates.

## Relationship to Other Processes

- Relies on Define Activities (PR09) for the complete activity list needed to establish relationships.
- Directly feeds Estimate Activity Durations and Develop Schedule, which require a sequenced network to calculate the critical path and schedule baseline.
- Informs risk identification and risk response planning, as network logic reveals critical dependencies and float sensitivity.
- Supports Control Schedule, which monitors whether actual execution respects or deviates from planned sequencing.

## Artifact Connections

- **A15 Schedule Baseline:** the schedule network diagram is the structural foundation from which the schedule baseline is developed through duration estimating and schedule compression.
- **A14 Integrated Project Management Plan:** schedule management plan updates may reflect changes to dependency logic or scheduling methodology driven by sequencing analysis.
- **A19 Risk Register / risk-related record:** critical path items and activities with high dependency concentration are risk candidates that should be logged and analyzed.
- **A05 Context Register:** external dependency constraints and calendar assumptions that affect how activities can be logically ordered.

## Skill Connections

- SKL-03-04 Plan Schedule.
- SKL-04-01 Control Schedule and Monitor Progress.

## Domain and Focus Area Links

- Strongest PMBOK 8 alignment: Schedule Performance Domain.
- Secondary alignment: Risk, because critical path logic and dependency concentration are primary sources of schedule risk.
- Strongest focus area alignment: Planning.

## Practitioner Questions

- Are all mandatory dependencies (hard logic) correctly identified and distinguished from discretionary ones (soft logic)?
- Have external dependencies — supplier deliveries, regulatory approvals, or other project handoffs — been explicitly captured?
- Are leads and lags applied judiciously and documented with justification?
- Does the schedule network diagram reveal any loops, open ends, or illogical sequences?
- Which activities lie on the critical path, and have those been flagged for risk and resource priority?

*Authority: PMBOK 8 — Schedule Performance Domain; Process Groups: A Practice Guide — 5.8 Sequence Activities*

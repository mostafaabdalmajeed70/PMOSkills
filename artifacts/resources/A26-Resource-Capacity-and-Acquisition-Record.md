---
artifact_id: A26
artifact_name: Resource Capacity and Acquisition Record
artifact_type: Resource planning and acquisition artifact
source_type: synthesis
governance_layer: Project Governance
version: "1.0.5"
status: Draft
supersedes: "v1.0.2 Items 110–118 (resource planning, staffing, and acquisition templates)"
primary_pmi_source: PMBOK8
exact_section: "Guide §2.6 Resource Performance Domain; Table 2-1 Plan Resource Management, Estimate Resources, Acquire Resources, Manage Project Execution"
performance_domains:
  - Resources
  - Governance
  - Schedule
  - Finance
focus_areas:
  - Planning
  - Executing
  - Monitoring and Controlling
related_processes:
  - Plan Resource Management
  - Estimate Resources
  - Acquire Resources
  - Manage Project Execution
linked_artifacts:
  - A14
  - A15
  - A16
  - A17
  - A25
owner: Project manager with resource management support
approval_authority: Project manager within thresholds; sponsor or functional authority for out-of-threshold acquisition, external hiring, or vendor engagement
---

# A26 Resource Capacity and Acquisition Record

**Artifact ID:** A26  
**Artifact type:** Resource planning and acquisition artifact  
**Source type:** Synthesis  
**Governance layer:** Project Governance  
**Version:** 1.0.5  
**Status:** Draft  
**Supersedes:** v1.0.2 Items 110–118 (resource planning, staffing, and acquisition templates)

---

## 1. Artifact Definition

| Field | Entry |
|---|---|
| Purpose | Define resource management approach, estimate resource requirements, document acquisition decisions, and track resource capacity and availability throughout the project. |
| When used | During Planning (resource management approach and estimates); updated through Executing and Monitoring and Controlling as resource availability changes. |
| Primary PMI source | PMBOK8 |
| Exact section | Guide §2.6 Resource Performance Domain; Table 2-1 Plan Resource Management, Estimate Resources, Acquire Resources |
| Purpose of citation | Ground resource planning, estimation, and acquisition in PMBOK 8 resource performance domain and related processes. |
| Performance domains | Resources, Governance, Schedule, Finance |
| Focus areas | Planning; Executing; Monitoring and Controlling |
| Related processes | Plan Resource Management; Estimate Resources; Acquire Resources; Manage Project Execution |
| Inputs | Scope structure (A08); schedule model (A15); financial plan (A16); team governance (A25); organizational resource pool and availability data |
| Outputs | Resource management approach; resource estimates; resource calendar; acquisition decisions; capacity status |
| Core fields | Resource management approach; resource types; estimates; availability calendar; acquisition method; cost; status; variance |
| Owner | Project manager with resource management support |
| Approval authority | Project manager within thresholds; sponsor or functional authority for out-of-threshold acquisition, external hiring, or vendor engagement |
| Tailoring guidance | For small teams with known, available resources, a simple availability table and confirmation of assignment is sufficient. For large programs with competitive resource markets or vendor acquisition, a full resource management plan and acquisition log is warranted. |
| Waste test | Fail if a resource management plan, staffing plan, and resource tracker are maintained in parallel with reconciled data. |
| Notes | Replaces v1.0.2 Items 110–118. Team governance and RACI lives in A25. A26 holds capacity, estimation, and acquisition. |

---

## 2. Record Header

| Field | Entry |
|---|---|
| Project or initiative name | |
| Project ID | |
| Project manager | |
| Resource management lead | |
| Version | |
| Last updated | |
| Linked artifacts | A14, A15, A16, A25 |

---

## 3. Resource Management Approach

| Field | Entry |
|---|---|
| Resource types in scope | Human / Equipment / Materials / Facilities / Other |
| Acquisition strategy | Internal pool / External hire / Contractor / Vendor / Mixed |
| Resource leveling approach | |
| Over-allocation resolution approach | |
| Resource calendar basis | |
| Estimation method | Bottom-up / Analogous / Parametric / Expert judgment |
| Cost linkage | A16 — Financial Management and Cost Baseline Record |
| Linked schedule | A15 — Schedule Model and Baseline Record |

---

## 4. Resource Estimates

| Resource ID | Resource name / role | Type | Skill requirements | Estimated quantity | Unit | Duration | Linked activity (A15) | Cost rate | Total estimated cost | Estimation basis |
|---|---|---|---|---:|---|---|---|---:|---:|---|
| | | | | | | | | | | |

---

## 5. Resource Calendar and Availability

| Resource name / role | Availability start | Availability end | Allocation % | Working calendar | Known constraints / leave | Confirmed? |
|---|---|---|---:|---|---|---|
| | | | | | | |

---

## 6. Acquisition Log

| Acquisition ID | Resource name / role | Type | Acquisition method | Source | Planned start | Planned end | Cost | Status | Approval authority | Approval date | Notes |
|---|---|---|---|---|---|---|---:|---|---|---|---|
| | | | | | | | | | | | |

**Acquisition method values:** `Internal assignment` / `Internal transfer` / `External hire` / `Contractor` / `Vendor` / `Secondment`  
**Status values:** `Planned` / `In progress` / `Confirmed` / `On board` / `Released` / `Cancelled`

---

## 7. Capacity Status (Monitoring)

| Resource name / role | Planned allocation % | Actual utilization % | Variance | Over-allocated? | Action taken | Next review |
|---|---:|---:|---:|---|---|---|
| | | | | | | |

---

## 8. Resource Variance and Issues

| Issue ID | Resource | Issue description | Impact | Action | Owner | Due date | Status | Linked A18 entry |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

---

## 9. Operating Rules

1. A26 holds resource capacity, estimates, and acquisition data. Team governance, RACI, and operating norms live in A25 — do not duplicate them here.
2. Resource cost data in A26 must be reconciled with A16 (Financial Management and Cost Baseline Record) at each reporting cycle.
3. Schedule-linked resource assignments in A26 Section 4 must align with A15 activity assignments.
4. All external acquisition decisions (hire, contract, vendor) require approval per the authority levels in A25 Section 6 and A06 thresholds.
5. Over-allocation identified in Section 7 must be resolved before the next baseline cycle; unresolved over-allocation must be logged in A18.
6. Fail the waste test if a resource management plan, a staffing plan, and a capacity tracker each hold the same resource availability data.

---

## 10. Migration Note

| Legacy items | Legacy names | Migration action |
|---|---|---|
| 110–118 | Resource planning, staffing, and acquisition templates (various) | CONSOLIDATED INTO A26 |

---

*Primary PMI source: PMBOK8 — Guide §2.6 Resource Performance Domain; Table 2-1 Plan Resource Management, Estimate Resources, Acquire Resources*  
*Source type: Synthesis*  
*Repository version: 1.0.5*

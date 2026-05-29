---
skill_id: SKL-05-08
skill_name: Control Resources
pack: "05 — Monitoring & Controlling"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A26 — Resource Capacity and Acquisition Record"
artifacts_updated:
  - "A17 — Integrated Performance Reporting Record (resource section)"
  - "A18 — Issue, Impediment and Action Log (resource issues)"
  - "A12 — Integrated Change Log (resource baseline changes)"
pmbok8_anchor: "Guide §2.6.2.6 Control Resources · Process Groups Practice Guide §5.9"
performance_domains:
  - Resources
  - Delivery
focus_area: Monitoring & Controlling
upstream_prerequisites:
  - "SKL-04-03 — A26 resource acquisition actuals must be flowing"
  - "SKL-04-05 — A25 team management must be active"
downstream_skills:
  - "SKL-06-01 — Close Project or Phase (resource release)"
file_path: "skills/05-monitoring-controlling/SKL-05-08-control-resources.md"
tests: 8
---

# SKL-05-08 — Control Resources

**Pack:** 05 — Monitoring & Controlling
**Status:** Draft · Untested
**Primary Artifact:** A26 — Resource Capacity and Acquisition Record
**PMBOK8 Anchor:** Guide §2.6.2.6 · Process Groups Practice Guide §5.9

---

## Purpose

Control Resources ensures that physical and human resources are available as planned, monitors actual utilization against the A26 resource plan, identifies resource variances and shortfalls, takes corrective action when resources are overallocated or unavailable, and manages resource baseline changes through A12. It is the monitoring complement to SKL-04-03 (Acquire Resources) and SKL-04-05 (Manage Team).

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Resource management plan | A26 | §1 plan section | Current |
| Resource actuals | A26 | Actuals section | Current period |
| Team assignment | A25 | RACI section | Current |
| Work package status | A08 | WBS status | Current |
| Issue log | A18 | Resource issues | Current |
| Change requests | A12 | Pending items | Current |

---

## Steps

### Step 1 — Collect Resource Utilization Actuals
Gather resource utilization data for all active resources:
- Human resources: actual hours worked per work package (from A25/A26)
- Physical resources: actual usage vs. planned usage (equipment, materials, facilities)
- External resources: actuals from A31 supplier performance log
Record in A26 actuals section for current period.

### Step 2 — Compare Actuals to Resource Plan
For each resource, compare actual utilization to A26 planned utilization:

| Variance type | Definition | Threshold (default) |
|---|---|---|
| Overallocation | Actual hours > planned hours by threshold | >110% of planned |
| Underutilization | Actual hours < planned hours by threshold | <80% of planned |
| Unavailability | Resource absent or unable to perform | Any absence affecting critical path |
| Skill gap emerging | Resource performing below quality standard | Quality issue in A20 linked to resource |

Document variance type and magnitude in A26 monitoring section.

### Step 3 — Identify Root Causes and Corrective Actions
For each resource variance:

| Variance type | Common root cause | Corrective action options |
|---|---|---|
| Overallocation | Scope growth; inaccurate estimates; competing priorities | Redistribute work; acquire additional resource; defer lower-priority tasks |
| Underutilization | Delayed work packages; dependency blockage | Reassign to other work packages; adjust release date; notify A26 acquisition record |
| Unavailability | Illness; organization change; competing project | Activate replacement plan from A26; log in A18; assess A15 schedule impact |
| Skill gap | Wrong skill acquired; development not effective | Training action in A25; reassign; supplement with specialist |

Document selected corrective action with owner and target date in A26.

### Step 4 — Process Resource Baseline Changes
For resource changes that affect the cost or schedule baseline:
- Raise A12 change request with impact on A16 (cost) and A15 (schedule)
- Route per A06 authority thresholds
- Update A26 after approval only

### Step 5 — Update A17 Resource Section
Record resource control findings in A17:
- Overall resource utilization rate (planned vs. actual)
- Count of overallocated, underutilized, and unavailable resources
- Critical path resources at risk
- Corrective actions taken and owner
- Resource change requests submitted and approved this period

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Resource utilization actuals | A26 | Actuals section |
| Resource variance analysis | A26 | Monitoring section |
| Resource performance information | A17 | Resource section |
| Resource issues | A18 | Issue log |
| Resource change requests | A12 | Pending items |

---

## Operating Rules

1. Resource actuals must be updated in A26 at every reporting period — not estimated.
2. Overallocated critical path resources must be flagged in A18 within the same period they are identified.
3. Resource baseline changes (changing planned quantities or types) must route through A12.
4. Unavailable resources that affect the critical path must trigger an immediate A15 schedule impact assessment.
5. Corrective actions for resource variances must have a named owner and target date in A26.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Resource actuals not collected | A26 actuals section empty for current period | Collect actuals from A25 and A26 managers; retroactive update; enforce collection process |
| Overallocation not detected until burnout | Team member reports exhaustion; quality drops | Immediate workload rebalancing; A18 issue; A25 performance log entry; assess schedule impact |
| Unavailability handled informally | Resource absent with no A18 entry or replacement plan activated | Log in A18; activate replacement plan from A26; assess critical path impact |
| Resource change made without A12 | A26 shows resource type or quantity changed with no A12 entry | Retroactive A12 entry; assess if baseline was affected; sponsor notification if above threshold |
| Physical resource not tracked | Equipment or material usage not in A26 actuals | Audit physical resource entries; retroactive actuals; confirm tracking process with resource managers |
| Corrective action has no owner | A26 shows variance with proposed action but no assigned owner | Assign owner immediately; set due date; follow up at next period |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Resource actuals updated | A26 actuals section has entries for current period | Any period with no A26 actuals update |
| T-2 | Overallocation detected | Overallocated resources identified and documented within same period | Overallocation discovered after consecutive periods undetected |
| T-3 | Unavailability in A18 | Resource unavailability affecting critical path logged in A18 | Critical resource unavailable with no A18 entry |
| T-4 | Critical path impact assessed | Every unavailability event has A15 schedule impact assessment | Unavailability event with no A15 review |
| T-5 | Corrective actions owned | Every A26 corrective action has a named owner and target date | Corrective action without owner or date |
| T-6 | Resource changes via A12 | Resource baseline changes have A12 Approved entry | Resource type or quantity changed without A12 entry |
| T-7 | Physical resources tracked | A26 includes physical resource actuals where applicable | Physical resource used with no A26 entry |
| T-8 | A17 resource section current | A17 contains resource performance information at every period | A17 issued without resource section |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-30 | Initial build |

---

*Authority: PMBOK8 Guide §2.6.2.6 · Process Groups Practice Guide §5.9*
*Source type: PMI-derived*

---
skill_id: SKL-03-16
skill_name: Plan Resource Management
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A26 — Resource Capacity and Acquisition Record (Resource Management Plan section)"
artifacts_updated:
  - "A14 — Integrated PM Plan (subsidiary reference)"
pmbok8_process_anchor: "Guide §2.6.2.1 Plan Resource Management · Figure 2-41"
performance_domains:
  - Resources
  - Governance
focus_area: Planning
upstream_prerequisites:
  - "SKL-02-01 — A04 must be baselined"
  - "SKL-03-05 — Scope baseline (WBS) must be complete"
downstream_skills:
  - "SKL-03-17 — Estimate Resources"
  - "SKL-04-xx — Acquire Resources"
file_path: "skills/03-planning/SKL-03-16-plan-resource-management.md"
tests: 8
version: "1.0.0"
---

# SKL-03-16 — Plan Resource Management

**Skill ID:** SKL-03-16  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** Guide §2.6.2.1 Plan Resource Management · Figure 2-41  
**File path:** `skills/03-planning/SKL-03-16-plan-resource-management.md`

---

## Purpose

Establish the resource management approach — defining how resources will be identified, estimated, acquired, managed, and released — and record it in the Resource Management Plan section of A26.

---

## Scope

This skill covers the planning approach only. Resource estimation is SKL-03-17. Acquisition execution is in Pack 04. This skill's output is Section 3 (Resource Management Approach) of A26.

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Project Charter | A04 | Yes |
| Scope baseline (WBS) | A08 | Yes |
| Tailoring Decision Record | A06 | Yes |
| Context Register (OPA — resource policies, org structure) | A05 | Yes |
| Delivery approach and lifecycle decision | A09 / A13 | Yes |
| Team governance record | A25 | Yes |

**Gate check:** Scope baseline (WBS) must be complete before resource management is planned — resource types and quantities are derived from the work structure.

---

## Instructions

### Step 1 — Identify resource types required
1. From A08 WBS dictionary, identify the resource types needed per work package: human (skills and roles), equipment, materials, facilities.
2. From A25 team governance record, confirm what roles are already defined and what gaps exist.
3. Classify each resource type as internal, external contractor, vendor-supplied, or shared organizational resource.

### Step 2 — Define acquisition strategy
1. Determine acquisition approach per resource type:
   - Internal assignment from existing pool
   - Internal transfer from another project or department
   - External hire (permanent or fixed-term)
   - Contractor or vendor engagement
   - Mixed approach
2. Identify any organizational constraints on acquisition (budget authority, procurement policy from A05, lead times).
3. Confirm that external acquisition will route through A31 (Procurement and Supplier Management) where applicable.

### Step 3 — Define resource leveling approach
1. Determine how resource conflicts and over-allocations will be resolved: priority-based leveling, schedule adjustment, or scope deferral.
2. Define the over-allocation resolution authority — team self-manages, PM resolves, or escalates to functional manager or sponsor.
3. For adaptive approaches, define how team capacity is managed across sprints (velocity-based allocation).

### Step 4 — Define competency and development approach
1. Identify skill gaps between required competencies (from WBS/A25) and available resources.
2. Define whether gaps will be addressed by training, hiring, or scope adjustment.
3. Document the team development approach — coaching, mentoring, formal training, or certification.

### Step 5 — Define recognition and team performance approach
1. Define how individual and team performance will be assessed.
2. Define how contributions will be recognized (consistent with organizational policy from A05).
3. For adaptive approaches, define team retrospective practices for continuous improvement.

### Step 6 — Define release plan
1. Define when resources will be released (by phase, by milestone, at project close).
2. Identify return-to-pool or handover obligations.

### Step 7 — Write the Resource Management Plan section of A26
Populate Section 3 of A26 (Resource Management Approach) with all decisions from Steps 1–6.

### Step 8 — Register A26 as subsidiary in A14
Add or confirm A26 reference in the A14 Subsidiary Plan Index.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Resource Management Plan | A26 | Section 3 — Resource Management Approach |
| Subsidiary reference | A14 | Subsidiary Plan Index |

---

## Constraints

- Do not estimate quantities or costs here — that is SKL-03-17.
- External resource acquisition must be consistent with A31 (Procurement) and organizational policy in A05.
- Resource authority levels must align with A25 Section 6 and A06 thresholds — do not define independent authority.
- Release planning must be documented — resources do not self-release.

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Small / co-located team | Brief acquisition note + competency gap check is sufficient |
| Large / distributed | Full resource management plan with leveling rules, acquisition lead times, and release schedule |
| Adaptive | Team capacity model based on velocity; sprint allocation rules |
| Multi-vendor | Formal acquisition strategy per vendor category; procurement linkage to A31 |

---

## Failure Cases

| Failure | Symptom | Resolution |
|---|---|---|
| WBS not complete | Resource types identified without scope structure | Complete SKL-03-05 first |
| Acquisition approach undefined | Resources assumed available without plan | Define acquisition strategy per type |
| Over-allocation rule missing | Resource conflicts unresolved during scheduling | Define leveling approach and authority |
| Release plan absent | Resources remain assigned beyond need | Add release triggers per role |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — scope baseline complete | A08 WBS = Baselined | WBS not baselined |
| T-2 | Resource types identified | All resource types from WBS listed in A26 Section 3 | Missing resource type |
| T-3 | Acquisition strategy defined per type | Each resource type has an acquisition approach | Any type with no strategy |
| T-4 | Over-allocation resolution defined | Leveling approach and authority documented | No over-allocation rule |
| T-5 | Competency gaps identified | Gap between required and available skills documented | No gap assessment |
| T-6 | Release plan defined | Release triggers documented per role or resource type | Release approach absent |
| T-7 | External acquisition references A31 | Vendor/contractor acquisition routes through A31 | Procurement bypass |
| T-8 | A26 referenced in A14 subsidiary index | A14 Subsidiary Plan Index row for A26 present | A14 not updated |

---

*Authority: PMBOK8 — Guide §2.6.2.1 Plan Resource Management · Figure 2-41*  
*Source type: PMI-derived*  
*Owner: Project manager*  
*Approval authority: Project manager; functional authority for shared resources; sponsor for external acquisition*

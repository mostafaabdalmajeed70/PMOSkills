---
skill_id: SKL-03-18
skill_name: Integrate Sustainability Into Project Planning
pack: "03 — Planning"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "A-NEW-SUST — Sustainability Register"
artifacts_updated:
  - "A08 — Project Scope Statement (sustainability specifications)"
  - "A16 — Cost Estimates (lifecycle costing reference)"
  - "A19 — Risk Register (sustainability/climate risks)"
pmbok8_process_anchor: "PMBOK8 Standard §3.6 Integrate Sustainability Within All Project Areas · Guide §2.5.2 Collect Stakeholder Requirements"
performance_domains:
  - Scope
  - Resources
  - Risk
focus_area: Planning
upstream_prerequisites:
  - "SKL-02-01 — A04 Project Charter must be baselined"
  - "SKL-02-02 — A07 Stakeholder Identification section must exist"
  - "SKL-03-02 — Plan Scope Management"
downstream_skills:
  - "SKL-03-14 — Estimate Costs"
  - "SKL-04-09 — Conduct Procurements"
  - "SKL-05-01 — Monitor and Control Project Work"
file_path: "skills/03-planning/SKL-03-18-integrate-sustainability-into-project-planning.md"
tests: 8
version: "1.0.0"
---

# SKL-03-18 — Integrate Sustainability Into Project Planning

**Skill ID:** SKL-03-18  
**Pack:** 03 — Planning  
**Status:** Draft · Untested  
**Source type:** PMI-derived  
**PMBOK8 anchor:** PMBOK8 Standard §3.6 Integrate Sustainability Within All Project Areas · Guide §2.5.2 Collect Stakeholder Requirements  
**File path:** `skills/03-planning/SKL-03-18-integrate-sustainability-into-project-planning.md`

---

## Purpose

Formulate the project's sustainability goals and actively integrate Environmental, Social, and Governance (ESG) requirements into all project areas. This skill operationalizes **Principle 6 (§4.6)** by producing the central **Sustainability Register (A-NEW-SUST)**, documenting resource utilization, recycling paths, and social equity metrics to ensure sustainable project delivery.

---

## Scope

This skill covers the integration of sustainability constraints, lifecycle assessments, and ESG goals into project scope, estimating, risk management, and procurement during planning. It does not perform general scope definition (SKL-03-04) or general risk identification (SKL-03-10).

---

## Inputs Required

| Input | Source | Mandatory? |
|---|---|---|
| Project Charter | A04 | Yes |
| Stakeholder Register | A07 | Yes |
| Scope Management Plan | A08 | Yes |
| Regulatory and ESG Context | A05 | Yes |

**Gate check:** A04 must be approved and baselined before this skill runs.

---

## Instructions

### Step 1 — Establish ESG Context and Constraints
1. Review A04 and A05 to identify external environmental regulations, industry ESG codes, and corporate social responsibility standards.
2. Conduct a stakeholder needs assessment (`A07`) focused on local community, public health, and ecological expectations.

### Step 2 — Formulate Sustainability Goals
1. Define 3 to 5 high-impact sustainability goals (e.g., net-zero emission operations, 100% cloud hardware recycling, zero-waste supply chain).
2. Establish baseline carbon targets, energy efficiency thresholds, and waste diversion percentages.

### Step 3 — Map Sustainability to Scope and Specifications
1. Review A08 Scope Statement. Add non-functional environmental specifications (e.g., recyclable materials, certified low-power hardware) to the requirements catalog.
2. Integrate a "Decommissioning and Recycling Plan" into the final product scope boundary.

### Step 4 — Formulate the Sustainability Register (A-NEW-SUST)
Populate the central **Sustainability Register** with:
- Identified ESG goals and target metrics
- Environmental indicators (Carbon footprint estimates, energy consumption limits)
- Waste management parameters (diverted percentage, hazardous material controls)
- Social equity metrics (workplace safety rules, community feedback checkpoints)
- Lifecycle assessment data (decommissioning approach, disposal costs)

### Step 5 — Map ESG Risks to the Risk Register
1. Extract sustainability-related risks (e.g., regulatory changes, supply chain climate blockages, adverse public reaction).
2. Log these risks in `A19` (Risk Register) with clear risk owners and response plans.

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Sustainability Register | A-NEW-SUST | Entire Document |
| Sustainability specifications | A08 | Scope Statement / Requirements section |
| Lifecycle Costing inputs | A16 | Cost Estimates / Lifecycle assumptions |
| ESG risks | A19 | Risk Register updates |

---

## Tailoring Guidance

| Approach | Adjustment |
|---|---|
| Simple / Low-risk | Standard one-page ESG Checklist; simplify metric collections |
| Predictive | Full lifecycle costing, detailed carbon estimation, formal ESG vendor scorecards |
| Adaptive / Hybrid | Agile user story acceptance criteria includes sustainability DoD; recurring sprint feedback |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | Gate check — A04 baselined | A04 status = Approved | A04 in Draft status |
| T-2 | Goals defined in A-NEW-SUST | 3+ ESG goals with clear targets present | Empty or generic goals |
| T-3 | Environmental metrics defined | Carbon footprint or energy limits recorded | Metrics absent |
| T-4 | Waste management defined | Diversion targets or material limits specified | Waste planning absent |
| T-5 | Social equity metrics defined | Safety or community metrics present | Metrics absent |
| T-6 | Lifecycle decommissioning defined | Active disposal or decommissioning plan recorded | Planning absent |
| T-7 | Sustainability specifications mapped to A08 | A08 contains environmental non-functional specs | Specifications absent |
| T-8 | Climate risks mapped to A19 | 2+ ESG or climate risks logged in Risk Register | Risks missing from A19 |

---

*Authority: PMBOK8 Standard Principle 6 (§4.6) · PMOSkills Repository*  
*Owner: Project Manager & PMO Lead*  

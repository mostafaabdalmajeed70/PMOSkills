# SKL-07-01 — Select and Tailor Lifecycle Approach

**Skill ID:** SKL-07-01  
**Pack:** 07 — Adaptive & Hybrid  
**Version:** 1.0.0  
**Status:** Active  
**Authority:** PMI-derived  
**Primary Reference:** PMBOK 8 Standard §4.2–4.3 · PMBOK 8 Guide §2.3 (Development Approach and Life Cycle Performance Domain)  
**Secondary References:** APG §3 (Life Cycle Selection) · APG §3.3 (Project Factors That Influence Tailoring) · DA Toolkit (Hybrid Levels 1–3)  
**Lifecycle Stage:** Initiating · Planning (and iteratively throughout)  
**Performance Domains:** Development Approach and Life Cycle · Governance · Planning  
**PMBOK 8 Principles Applied:** Stewardship · Value · Adaptability · Change · Quality  

---

## Purpose

Select the most appropriate development approach — predictive, adaptive, hybrid, or a custom blend — and tailor it to the project’s specific characteristics. Document the lifecycle selection rationale in the Project Management Plan (A06), ensuring the approach is proportionate to the project’s uncertainty, complexity, team maturity, stakeholder needs, and organizational context.

---

## Scope

| In Scope | Out of Scope |
|---|---|
| Lifecycle approach selection (predictive / adaptive / hybrid) | Organizational agile transformation (OCM) |
| Tailoring decisions per project, team, and organization context | Prescriptive methodology selection (e.g., “use Scrum”) |
| Documenting approach rationale in A06 | Portfolio lifecycle governance |
| Applying PMBOK 8 4-step tailoring framework | Program-level approach design |
| DA Hybrid Level 1–3 classification | |
| Suitability filter assessment | |

---

## Trigger Conditions

Activate this skill when:
- A new project or phase is being initiated and an approach has not been formally selected
- The current approach is failing to deliver value and a re-tailoring is needed
- A phase gate review determines that the lifecycle approach must be changed
- The project environment changes materially (scope, team, regulation, technology)

---

## Key Concept: The Development Approach Spectrum

| Approach | Best Fit | Constraint Model |
|---|---|---|
| **Predictive** | Stable scope, regulated environment, large investment, low uncertainty | Scope fixed; time and cost managed |
| **Adaptive / Agile** | High uncertainty, evolving requirements, frequent feedback needed | Time and cost fixed; scope varies (inverted triangle) |
| **Hybrid** | Mixed certainty across deliverables; transitional environments; most modern projects | Context-dependent per component |

**PMBOK 8 Hybrid Levels (DA Toolkit):**
- **Hybrid Level 1** — Predictive dominant; adaptive elements reduce specific pain points
- **Hybrid Level 2** — Both predictive and adaptive contribute significantly
- **Hybrid Level 3** — Adaptive dominant; predictive elements satisfy business constraints

---

## PMBOK 8 Four-Step Tailoring Framework

| Step | Action | Key Question |
|---|---|---|
| 1 | **Select initial development approach** using suitability filters | Does the project have stable or evolving requirements? |
| 2 | **Tailor for the organization** — align methodology to org policies, culture, maturity | What does the organization’s governance and PMO require? |
| 3 | **Tailor for the project** — evaluate product, team, and culture attributes | What does this specific project’s profile demand? |
| 4 | **Implement ongoing improvement** — retrospectives, phase gates, continuous adaptation | What is working and what should change each cycle? |

---

## Suitability Filter — Deliverable Factors

| Factor | Predictive ⭐ | Adaptive ⭐ |
|---|---|---|
| Degree of innovation | Low | High |
| Requirements certainty | High | Low |
| Scope stability | High | Low |
| Ease of change | Low (costly to change) | High |
| Regulatory oversight | High | Low |
| Value from early feedback | Low | High |
| Safety requirements | High | Low |

## Suitability Filter — Project Factors

| Factor | Predictive ⭐ | Adaptive ⭐ |
|---|---|---|
| Stakeholder involvement needed | Low | High |
| Fixed end date | High | Low |
| Financing uncertainty | Low | High |
| Project size and complexity | Large, stable | Complex, evolving |
| Team skills | Specialized, sequential | Cross-functional, collaborative |

## Suitability Filter — Organizational Factors

| Factor | Predictive ⭐ | Adaptive ⭐ |
|---|---|---|
| Org structure | Functional, hierarchical | Network-oriented, flat |
| Culture | Managing/directing | Self-managing, innovative |
| Org capability | Established process | Agile-ready |
| Team size | Large | Small (3–9 preferred for adaptive) |
| Team location | Distributed | Co-located or virtual-enabled |

---

## Hybrid Pattern Selection Guide

Use these patterns (PMBOK 8 §4.2.3, Figures 4-8 through 4-11) to select the appropriate hybrid structure:

| Pattern | When to Use |
|---|---|
| **Adaptive development → Predictive rollout** | Uncertain development phase; known, repeatable deployment |
| **Adaptive + Predictive simultaneously** | Separate streams with different certainty profiles; transitioning teams |
| **Largely predictive + Adaptive component** | Mostly routine project; one uncertain or innovative component |
| **Largely adaptive + Predictive component** | Mostly agile; one external or regulatory-fixed deliverable |

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| Project Charter | A01 | Project objectives, constraints, sponsor intent |
| Business Case | A02 | Value drivers, benefit type, timeline pressure |
| Organizational Process Assets | OPA (A05) | Existing methodology standards, lifecycle templates |
| Enterprise Environmental Factors | EEF | Org structure, culture, regulation, team location |
| Stakeholder Register | A10 | Stakeholder involvement expectations |
| Risk Register (initial) | A19 | Initial uncertainty and risk profile |
| Benefits Management Plan | Sponsor/PMO | Delivery cadence and value realization timing |

---

## Tools and Techniques

| Tool / Technique | Application |
|---|---|
| Suitability Filters | Assess deliverable, project, and org factors against approach criteria |
| Expert Judgment | PM + PMO assess fit based on experience with similar projects |
| Meetings — Lifecycle Selection Workshop | Facilitated session with sponsor, PM, team, PMO |
| Data Analysis — Alternatives Analysis | Compare predictive vs. adaptive vs. hybrid options |
| PMBOK 8 Tailoring Framework | Structured 4-step process |
| DA Hybrid Level Assessment | Determine which hybrid level fits the context |

---

## Outputs

| Output | Artifact | Notes |
|---|---|---|
| Development Approach Section | A06 §2 — Project Management Plan | Documents selected approach, rationale, tailoring decisions |
| Tailoring Decision Log | A06 or standalone | Records what was adapted and why |
| Lifecycle Map | LIFECYCLE-MAP.md | Phase/iteration structure for this project |

---

## A06 Development Approach Section Template

```markdown
## Development Approach and Lifecycle (A06 §2)

**Approach Selected:** [ ] Predictive  [ ] Adaptive  [ ] Hybrid — Level: ___
**Hybrid Pattern (if applicable):** [ ] Adaptive→Predictive  [ ] Simultaneous  [ ] Pred+Adaptive Component  [ ] Adaptive+Pred Component

### Suitability Rationale
| Factor | Assessment | Weight ⭐ |
|---|---|---|
| Requirements certainty | | |
| Scope stability | | |
| Stakeholder feedback need | | |
| Regulatory environment | | |
| Team size and experience | | |
| Organizational culture | | |

**Verdict:** [Approach selection narrative — 2–3 sentences]

### Tailoring Decisions
| PMBOK 8 Tailoring Step | Decision Made | Rationale |
|---|---|---|
| 1. Initial approach selection | | |
| 2. Org tailoring | | |
| 3. Project tailoring | | |
| 4. Ongoing improvement mechanism | | |

### Delivery Cadence
[ ] Single delivery  [ ] Multiple deliveries  [ ] Periodic (timebox: ___ weeks)  [ ] Continuous delivery

### Governance Model for This Approach
[ ] Structured governance (phase gates, formal change control)  
[ ] Guided self-governance (agile, empowered team, light oversight)  
[ ] Hybrid governance (structured at program level, self-governing at team level)

**Approved By:** _____________  **Date:** ___________
```

---

## Authority Routing

| Decision | Authority Level | Threshold |
|---|---|---|
| Select initial lifecycle approach | Project Manager + Sponsor | T2 |
| Override org-standard methodology | PMO + Sponsor | T2–T3 |
| Re-tailor approach mid-project | PM + CCB or Governing Body | T2–T3 |
| Change from predictive to adaptive (or vice versa) | Governing Body | T3 |

---

## Validation Criteria

This skill output is valid when:
- [ ] All four PMBOK 8 tailoring steps are completed and documented
- [ ] Suitability filter assessment covers deliverable, project, and org factors
- [ ] Approach selection rationale is documented in A06 §2
- [ ] Delivery cadence is explicitly defined
- [ ] Governance model is named and authorized
- [ ] Hybrid level (if applicable) is identified per DA framework

---

## Failure Cases

| Failure | Indicator | Resolution |
|---|---|---|
| Approach selected by default (“we always do waterfall”) | No suitability filter completed | Run suitability filter; document rationale explicitly |
| Adaptive selected without team readiness | Team has no agile experience; no servant leader | Assess team maturity; plan hybrid L1 as transition |
| Hybrid selected without pattern defined | No clear description of which streams are adaptive vs. predictive | Map streams to pattern from PMBOK 8 Figures 4-8 to 4-11 |
| No tailoring log maintained | Approach changes mid-project with no record | Initiate tailoring changelog; retrospect at each iteration |
| Approach not re-evaluated after major change | Scope or team changes but approach unchanged | Trigger re-tailoring via SKL-05-02 (Integrated Change Control) |

---

## Linked Skills

| Skill ID | Skill Name | Relationship |
|---|---|---|
| SKL-02-01 | Develop Project Charter | Approach constraints visible in charter |
| SKL-03-01 | Develop Project Management Plan | A06 §2 is an output of this skill |
| SKL-07-02 | Manage Backlog and Iterations | Required if adaptive/hybrid selected |
| SKL-07-04 | Plan and Deliver Hybrid Projects | Required if hybrid selected |
| SKL-05-02 | Perform Integrated Change Control | Governs approach change requests |

---

*Authority: PMI-derived — PMBOK 8 Standard §4.2–4.3 · APG §3 · DA Toolkit (Hybrid Levels)*  
*PMO Skill Repository v1.0.0 · Pack 07 — Adaptive & Hybrid*

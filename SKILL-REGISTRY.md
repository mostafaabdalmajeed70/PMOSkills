# SKILL-REGISTRY.md — Project Management Skills Repository
**Version:** 1.0.0-draft  
**Status:** Active · Maintained  
**Authority:** PMBOK8 · Artifacts-V-1.0.5 · Repository Operating Rules  
**Last Updated:** 2026-05-29  
**File Path:** `skills/SKILL-REGISTRY.md`

---

## Purpose

This registry is the single authoritative index of all skills in the PM Skills Repository. It catalogs every skill by ID, pack, name, status, primary artifact, PMBOK8 anchor, and dependency chain. It does not duplicate skill content — it indexes it.

**Use this registry to:**
- Determine which skills exist and their current build status
- Identify upstream prerequisites before executing a skill
- Trace which artifact each skill produces or updates
- Plan the remaining skill build order
- Confirm pack completeness before declaring a pack ready for use

---

## Registry Schema

Each skill entry contains the following fields:

| Field | Description |
|-------|-------------|
| **Skill ID** | Unique identifier — format: `SKL-PP-NN` where PP = pack number, NN = sequence within pack |
| **Skill Name** | Full name matching the skill file heading |
| **Pack** | Lifecycle pack number and name |
| **Status** | `Draft · Untested` / `Draft · In Review` / `Reviewed` / `Approved · Production` |
| **Source Type** | `PMI-derived` / `organization-defined` / `synthesis` |
| **Primary Artifact (Output)** | The artifact this skill produces or whose primary section it populates |
| **Artifacts Updated** | Additional artifacts modified as outputs |
| **PMBOK8 Process Anchor** | The PMBOK8 Guide process or section this skill operationalizes |
| **Performance Domains** | PMBOK8 performance domains this skill operates within |
| **Focus Area** | PMBOK8 focus area(s): Initiating / Planning / Executing / Monitoring and Controlling / Closing |
| **Upstream Prerequisites** | Skills that must complete before this skill can execute |
| **Downstream Skills** | Skills that consume this skill's outputs |
| **File Path** | Relative path to the skill markdown file |
| **Tests** | Number of tests defined in the skill file |
| **Notes** | Key design decisions, constraints, or open items |

---

## Pack Index

| Pack | Name | Skills Built | Skills Remaining (Planned) | Status |
|------|------|-------------|---------------------------|--------|
| 01 | Organizational Setup | 0 | TBD | Not started |
| **02** | **Initiating** | **2** | TBD | In progress |
| **03** | **Planning** | **6** | TBD | In progress |
| 04 | Executing | 0 | TBD | Not started |
| 05 | Monitoring and Controlling | 0 | TBD | Not started |
| 06 | Closing | 0 | TBD | Not started |

---

## Pack 02 — Initiating

> **Pack Purpose:** Skills that execute during the Initiating focus area — authorizing the project, establishing governance context, identifying stakeholders, and producing the foundational records that all planning skills depend on.

> **Pack Prerequisites:** A business case or equivalent authorization trigger must exist before any Pack 02 skill runs.

> **Pack Completion Criteria:** A04 (Project Charter), A05 (Context Register), and A07 (Stakeholder Register — Identification section) must all be baselined before Pack 03 skills begin.

---

### SKL-02-01 — Initiate Project or Phase

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-02-01 |
| **Skill Name** | Initiate Project or Phase |
| **Pack** | 02 — Initiating |
| **Status** | Draft · Untested |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A04 — Project Charter |
| **Artifacts Updated** | A05 — Context Register (initial EEF/OPA capture) · A02 — Benefits and Value Measurement Record (benefit baseline) |
| **PMBOK8 Process Anchor** | Guide §2.1.6.1 Initiate Project or Phase · Figure 2-3 |
| **Performance Domains** | Governance · Stakeholders |
| **Focus Area** | Initiating |
| **Upstream Prerequisites** | A01 (Business Case) must exist · A03 (Feasibility and Viable Options Record) recommended |
| **Downstream Skills** | SKL-02-02 (consumes A04 as primary input) · SKL-03-01 and all planning skills (consume A04) |
| **File Path** | `skills/02-initiating/SKL-02-01-initiate-project-or-phase.md` |
| **Tests** | 8 |
| **Governance Layer** | Project Governance |
| **Primary PMBOK8 Tools** | Expert judgment · Data gathering (brainstorming, interviews) · Interpersonal skills · Meetings |
| **Approval Authority** | Sponsor or designated project authorizing body |
| **Threshold Band** | T1 — charter authorization requires sponsor sign-off regardless of project size |
| **Notes** | Charter is the enabling artifact for all downstream work. Skill enforces the rule that planning artifacts cannot precede the charter. Includes predictive and adaptive tailoring paths. |

---

### SKL-02-02 — Identify Stakeholders

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-02-02 |
| **Skill Name** | Identify Stakeholders |
| **Pack** | 02 — Initiating |
| **Status** | Draft · Untested |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A07 — Stakeholder Register and Engagement Strategy (Identification section) |
| **Artifacts Updated** | A05 — Context Register (OPA updates) · A19 — Risk Management Record (engagement risks flagged) |
| **PMBOK8 Process Anchor** | Guide §2.5.2.1 Identify Stakeholders · Figure 2-33 |
| **Performance Domains** | Stakeholders · Governance |
| **Focus Area** | Initiating |
| **Upstream Prerequisites** | SKL-02-01 — A04 must be baselined before this skill runs |
| **Downstream Skills** | SKL-03-07 — A07 Identification section is the primary input to engagement planning |
| **File Path** | `skills/02-initiating/SKL-02-02-identify-stakeholders.md` |
| **Tests** | 8 |
| **Governance Layer** | Project Governance |
| **Primary PMBOK8 Tools** | Stakeholder analysis · Power/interest grid · Salience model · Expert judgment · Data representation · Meetings |
| **Core Technique** | Power/Interest Grid + Salience Model + Engagement Level Assessment (Unaware → Resistant → Neutral → Supportive → Leading) |
| **Approval Authority** | Sponsor (initial strategic alignment); ongoing updates managed by PM |
| **Threshold Band** | T2 — governance body and high-power stakeholders require sponsor awareness |
| **Re-run Triggers** | Phase gates · New stakeholders identified · Major scope or authority changes |
| **Notes** | Merged record — A07 holds both identification and engagement strategy in a single artifact. Skill populates the Identification section only; SKL-03-07 completes the Engagement Strategy section. Includes power/interest grid as the core analytical tool. |

---

## Pack 03 — Planning

> **Pack Purpose:** Skills that execute during the Planning focus area — translating authorization and context into actionable project management plans, baselines, and subsidiary plans. Pack 03 skills produce the integrated planning set that Pack 04 (Executing) skills will operate against.

> **Pack Prerequisites:** All Pack 02 skills must complete and their primary artifacts must be baselined before Pack 03 skills begin (A04, A05, A07 Identification section).

> **Pack Completion Criteria:** A14 (Integrated PM Plan) must be assembled with all applicable subsidiary plan references before Pack 04 skills begin. Pack 03 is considered complete when all applicable subsidiary plans are baselined and A14 references them.

> **Pack 03 Stakeholder/Communications Cluster:** SKL-03-07 and SKL-03-08 form an inseparable pair — SKL-03-07 must always precede SKL-03-08. The output of SKL-03-08 (A28) is a direct input to SKL-04-Manage Communications.

---

### SKL-03-01 — Integrate and Align Project Plans

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-01 |
| **Skill Name** | Integrate and Align Project Plans |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A14 — Integrated Project Management Plan |
| **Artifacts Updated** | All subsidiary plan artifacts cross-referenced in A14 |
| **PMBOK8 Process Anchor** | Guide §2.1.6.2 Integrate and Align Project Plans · Figure 2-4 |
| **Performance Domains** | Governance · All domains (integrative) |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-02-01 · SKL-02-02 · All applicable subsidiary planning skills in Pack 03 |
| **Downstream Skills** | SKL-04 Manage Project Execution (primary input) · all monitoring skills |
| **File Path** | `skills/03-planning/SKL-03-01-integrate-align-project-plans.md` |
| **Tests** | TBD |
| **Notes** | This is the final Pack 03 skill — it assembles all subsidiary plans into A14. It cannot run until all applicable planning skills are complete. Build last in Pack 03. |

---

### SKL-03-02 — Plan Scope Management

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-02 |
| **Skill Name** | Plan Scope Management |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A08 — Scope and Requirements Decision Record (Scope Management Plan section) |
| **Artifacts Updated** | A14 — Integrated PM Plan (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.2.2.1 Plan Scope Management · Figure 2-14 |
| **Performance Domains** | Scope · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-02-01 · SKL-02-02 |
| **Downstream Skills** | SKL-03-03 (Elicit and Analyze Requirements) · SKL-03-04 (Define Scope) |
| **File Path** | `skills/03-planning/SKL-03-02-plan-scope-management.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-03 — Elicit and Analyze Requirements

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-03 |
| **Skill Name** | Elicit and Analyze Requirements |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A08 — Scope and Requirements Decision Record (Requirements section) |
| **Artifacts Updated** | A07 — Stakeholder Register (requirements-driven stakeholder updates) |
| **PMBOK8 Process Anchor** | Guide §2.2.2.2 Elicit and Analyze Requirements · Figure 2-15 |
| **Performance Domains** | Scope · Stakeholders |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-02 · SKL-02-02 |
| **Downstream Skills** | SKL-03-04 (Define Scope) · SKL-03-08 (consumes requirements for communication needs) |
| **File Path** | `skills/03-planning/SKL-03-03-elicit-analyze-requirements.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-04 — Define Scope

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-04 |
| **Skill Name** | Define Scope |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A08 — Scope and Requirements Decision Record (Project Scope Statement section) |
| **Artifacts Updated** | A06 — Tailoring Decision Record (scope-driven tailoring updates) |
| **PMBOK8 Process Anchor** | Guide §2.2.2.3 Define Scope · Figure 2-16 |
| **Performance Domains** | Scope · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-03 |
| **Downstream Skills** | SKL-03-05 (Develop Scope Structure / WBS) |
| **File Path** | `skills/03-planning/SKL-03-04-define-scope.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-05 — Develop Scope Structure

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-05 |
| **Skill Name** | Develop Scope Structure |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A08 — Scope and Requirements Decision Record (WBS / Scope Structure section) |
| **Artifacts Updated** | A15 — Schedule Model (work packages feed activity decomposition) |
| **PMBOK8 Process Anchor** | Guide §2.2.2.4 Develop Scope Structure · Figure 2-17 |
| **Performance Domains** | Scope · Schedule |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-04 |
| **Downstream Skills** | SKL-03-06 (Plan Schedule Management) · SKL-03-10 (Estimate Costs) |
| **File Path** | `skills/03-planning/SKL-03-05-develop-scope-structure.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-06 — Plan Schedule Management

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-06 |
| **Skill Name** | Plan Schedule Management |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A15 — Schedule Model and Baseline Record (Schedule Management Plan section) |
| **Artifacts Updated** | A14 — Integrated PM Plan (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.3.2.1 Plan Schedule Management · Figure 2-21 |
| **Performance Domains** | Schedule · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-05 · SKL-02-01 |
| **Downstream Skills** | SKL-03-06b Develop Schedule |
| **File Path** | `skills/03-planning/SKL-03-06-plan-schedule-management.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-07 — Plan Stakeholder Engagement ✓

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-07 |
| **Skill Name** | Plan Stakeholder Engagement |
| **Pack** | 03 — Planning |
| **Status** | Draft · Untested |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A07 — Stakeholder Register and Engagement Strategy (Engagement Strategy section) |
| **Artifacts Updated** | A19 — Risk Management Record (engagement risks confirmed/added as risk entries) · A14 — Integrated PM Plan (A07 referenced as stakeholder engagement plan subsidiary) |
| **PMBOK8 Process Anchor** | Guide §2.5.2.2 Plan Stakeholder Engagement · Figure 2-34 |
| **Performance Domains** | Stakeholders · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-02-02 — A07 Identification section must be complete before this skill runs |
| **Downstream Skills** | SKL-03-08 (A07 engagement strategies are the primary input to communications planning) · SKL-04-Manage Stakeholder Engagement · SKL-05-Monitor Stakeholder Engagement |
| **File Path** | `skills/03-planning/SKL-03-07-plan-stakeholder-engagement.md` |
| **Tests** | 8 (T-1 through T-8) |
| **Governance Layer** | Project Governance |
| **Primary PMBOK8 Tools** | Stakeholder Engagement Assessment Matrix (SEAM) · Expert judgment · Root cause analysis · Data representation · Meetings · Decision-making (prioritization) |
| **Core Technique** | Stakeholder Engagement Assessment Matrix — Current (C) and Desired (D) positioning on 5-level scale: Unaware → Resistant → Neutral → Supportive → Leading |
| **Approval Authority** | Sponsor (initial baseline for high-power stakeholder strategies); PM manages ongoing updates |
| **Threshold Band** | T2 |
| **Re-run Triggers** | Phase gates · Monitoring signals strategy is failing · New stakeholder identified · Major change approved affecting authority or scope · Project enters deployment phase |
| **Key Design Decisions** | SEAM is embedded in A07 (not a separate artifact); root cause analysis gate for Resistant stakeholders (Step 5); vague strategy rejection enforced in Test T-3; engagement strategies must precede decision points (Tests T-5, T-6) |
| **Notes** | Inseparable upstream pair with SKL-03-08. Must always run before SKL-03-08. A07 is the single merged record — no separate engagement plan document permitted (Test T-8 enforces waste rule §3.2). |

---

### SKL-03-08 — Plan Communications Management ✓

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-08 |
| **Skill Name** | Plan Communications Management |
| **Pack** | 03 — Planning |
| **Status** | Draft · Untested |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A28 — Communications and Reporting Record |
| **Artifacts Updated** | A07 — Stakeholder Register and Engagement Strategy (communication-driven engagement updates) · A15 — Schedule Model (communication events added) · A14 — Integrated PM Plan (A28 referenced as comms plan subsidiary) |
| **PMBOK8 Process Anchor** | Guide §2.5.2.3 Plan Communications Management · Figure 2-35 |
| **Performance Domains** | Stakeholders · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-07 — A07 Engagement Strategy section must be complete before A28 can be built (Test T-1 enforces this gate) |
| **Downstream Skills** | SKL-04-Manage Communications (executes the delivery plan) · SKL-05-Monitor Communications (measures effectiveness) |
| **File Path** | `skills/03-planning/SKL-03-08-plan-communications-management.md` |
| **Tests** | 10 (T-1 through T-10) |
| **Governance Layer** | Project Governance |
| **Primary PMBOK8 Tools** | Communication requirements analysis · Communication technology selection · Communication models (Figure 5-2) · Communication methods classification (Interactive/Push/Pull) · Expert judgment · Meetings |
| **Core Technique** | Communication Requirements Analysis — 10-question per-stakeholder analysis producing every A28 row field |
| **Approval Authority** | Sponsor or governance body for high-sensitivity reporting; PM manages routine updates |
| **Threshold Band** | T2 — executive, external, or confidential communication entries require sponsor awareness |
| **Re-run Triggers** | Phase gates · A07 engagement strategy updates · Communication monitoring failure signal · New stakeholder added · Major change affecting communication obligations · Technology platform change |
| **Key Design Decisions** | A28 is the single merged record (consolidates v1.0.2 items 190, 191, 192, 211); all three communication methods required (push-only plan flagged in Test T-5); feedback route mandatory on every entry (Test T-4); cross-cultural entries require Communication Model analysis (Test T-10); communication events must precede decisions (Test T-7) |
| **Notes** | A07 (from SKL-03-07) is the primary input. A28 and A07 must remain internally consistent — every A07 stakeholder must have ≥ 1 A28 entry (Test T-2); every A28 entry must reference an A07 stakeholder (Test T-3). No separate "Communications Management Plan.docx" permitted (Test T-9 enforces waste rule §3.2). |

---

### SKL-03-09 — Plan Risk Management

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-09 |
| **Skill Name** | Plan Risk Management |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A19 — Risk Management Record (Risk Management Plan section) |
| **Artifacts Updated** | A14 — Integrated PM Plan (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.7.2.1 Plan Risk Management · Figure 2-48 |
| **Performance Domains** | Risk · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-02-01 · SKL-02-02 · SKL-03-07 (engagement risks from A19 feed into risk planning) |
| **Downstream Skills** | SKL-03-10 (Identify Risks) |
| **File Path** | `skills/03-planning/SKL-03-09-plan-risk-management.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. A19 has already received engagement risk entries from SKL-02-02 and SKL-03-07; this skill formalizes the risk management approach. |

---

### SKL-03-10 — Identify Risks

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-10 |
| **Skill Name** | Identify Risks |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A19 — Risk Management Record (Risk Register section) |
| **Artifacts Updated** | A08, A07, A15 (cross-domain risk entries) |
| **PMBOK8 Process Anchor** | Guide §2.7.2.2 Identify Risks · Figure 2-49 |
| **Performance Domains** | Risk · Governance · Scope · Schedule |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-09 |
| **Downstream Skills** | SKL-03-11 (Perform Risk Analysis) |
| **File Path** | `skills/03-planning/SKL-03-10-identify-risks.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-11 — Perform Risk Analysis

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-11 |
| **Skill Name** | Perform Risk Analysis |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A19 — Risk Management Record (Risk Analysis section) · A20 — Quantitative Risk and Reserve Decision Record (conditional) |
| **Artifacts Updated** | A14 (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.7.2.3 Perform Risk Analysis · Figure 2-50 |
| **Performance Domains** | Risk · Finance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-10 |
| **Downstream Skills** | SKL-03-12 (Plan Risk Responses) |
| **File Path** | `skills/03-planning/SKL-03-11-perform-risk-analysis.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. Covers both qualitative and quantitative analysis paths. |

---

### SKL-03-12 — Plan Risk Responses

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-12 |
| **Skill Name** | Plan Risk Responses |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A19 — Risk Management Record (Risk Response section) |
| **Artifacts Updated** | A07 (engagement risks get response strategies) · A15 (schedule reserves) · A16 (cost reserves) |
| **PMBOK8 Process Anchor** | Guide §2.7.2.4 Plan Risk Responses · Figure 2-51 |
| **Performance Domains** | Risk · Finance · Stakeholders |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-11 |
| **Downstream Skills** | SKL-04-Implement Risk Responses · SKL-05-Monitor Risks |
| **File Path** | `skills/03-planning/SKL-03-12-plan-risk-responses.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. Engagement risk responses from SKL-03-07 must be confirmed or revised here. |

---

### SKL-03-13 — Plan Financial Management

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-13 |
| **Skill Name** | Plan Financial Management |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A16 — Financial Management and Cost Baseline Record (Financial Management Plan section) |
| **Artifacts Updated** | A14 — Integrated PM Plan (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.4.2.1 Plan Financial Management · Figure 2-27 |
| **Performance Domains** | Finance · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-02-01 · SKL-03-05 |
| **Downstream Skills** | SKL-03-14 (Estimate Costs) · SKL-03-15 (Develop Budget) |
| **File Path** | `skills/03-planning/SKL-03-13-plan-financial-management.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-14 — Estimate Costs

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-14 |
| **Skill Name** | Estimate Costs |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A16 — Financial Management and Cost Baseline Record (Cost Estimates section) |
| **Artifacts Updated** | A19 (cost risk feeds) · A15 (resource-cost linkage) |
| **PMBOK8 Process Anchor** | Guide §2.4.2.2 Estimate Costs · Figure 2-28 |
| **Performance Domains** | Finance · Risk |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-13 · SKL-03-05 |
| **Downstream Skills** | SKL-03-15 (Develop Budget) |
| **File Path** | `skills/03-planning/SKL-03-14-estimate-costs.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-15 — Develop Budget

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-15 |
| **Skill Name** | Develop Budget |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A16 — Financial Management and Cost Baseline Record (Cost Baseline / BAC section) |
| **Artifacts Updated** | A14 — Integrated PM Plan (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.4.2.3 Develop Budget · Figure 2-29 |
| **Performance Domains** | Finance · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-14 · SKL-03-11 (risk reserves) |
| **Downstream Skills** | SKL-05-Monitor and Control Finances |
| **File Path** | `skills/03-planning/SKL-03-15-develop-budget.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-16 — Plan Resource Management

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-16 |
| **Skill Name** | Plan Resource Management |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A26 — Resource Capacity and Acquisition Record (Resource Management Plan section) |
| **Artifacts Updated** | A14 — Integrated PM Plan (subsidiary reference) |
| **PMBOK8 Process Anchor** | Guide §2.6.2.1 Plan Resource Management · Figure 2-41 |
| **Performance Domains** | Resources · Governance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-02-01 · SKL-03-05 |
| **Downstream Skills** | SKL-03-17 (Estimate Resources) · SKL-04-Acquire Resources |
| **File Path** | `skills/03-planning/SKL-03-16-plan-resource-management.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

### SKL-03-17 — Estimate Resources

| Field | Value |
|-------|-------|
| **Skill ID** | SKL-03-17 |
| **Skill Name** | Estimate Resources |
| **Pack** | 03 — Planning |
| **Status** | Planned · Not yet built |
| **Source Type** | PMI-derived |
| **Primary Artifact (Output)** | A26 — Resource Capacity and Acquisition Record (Resource Estimates section) |
| **Artifacts Updated** | A15 (resource-loaded schedule) · A16 (resource cost feeds) |
| **PMBOK8 Process Anchor** | Guide §2.6.2.2 Estimate Resources · Figure 2-42 |
| **Performance Domains** | Resources · Schedule · Finance |
| **Focus Area** | Planning |
| **Upstream Prerequisites** | SKL-03-16 · SKL-03-06b (Develop Schedule) |
| **Downstream Skills** | SKL-04-Acquire Resources |
| **File Path** | `skills/03-planning/SKL-03-17-estimate-resources.md` |
| **Tests** | TBD |
| **Notes** | Not yet built. |

---

## Dependency Chain Diagram

```
Pack 02 — Initiating
────────────────────────────────────────────────────────
SKL-02-01 (Initiate Project or Phase)
    └──▶ SKL-02-02 (Identify Stakeholders)
              └──▶ [Pack 03 Planning begins]

Pack 03 — Planning (Stakeholder/Comms cluster — BUILT)
────────────────────────────────────────────────────────
SKL-02-02 ──▶ SKL-03-07 (Plan Stakeholder Engagement)
                   └──▶ SKL-03-08 (Plan Communications Management)
                              └──▶ SKL-04-Manage Communications
                              └──▶ SKL-05-Monitor Communications
         SKL-03-07 ──▶ SKL-04-Manage Stakeholder Engagement
                   └──▶ SKL-05-Monitor Stakeholder Engagement

Pack 03 — Planning (Scope cluster — PLANNED)
────────────────────────────────────────────────────────
SKL-02-02 ──▶ SKL-03-02 (Plan Scope Management)
                   └──▶ SKL-03-03 (Elicit and Analyze Requirements)
                              └──▶ SKL-03-04 (Define Scope)
                                        └──▶ SKL-03-05 (Develop Scope Structure)
                                                  ├──▶ SKL-03-06 (Plan Schedule Management)
                                                  ├──▶ SKL-03-13 (Plan Financial Management)
                                                  └──▶ SKL-03-16 (Plan Resource Management)

Pack 03 — Planning (Risk cluster — PLANNED)
────────────────────────────────────────────────────────
SKL-03-07 + SKL-03-02 ──▶ SKL-03-09 (Plan Risk Management)
                              └──▶ SKL-03-10 (Identify Risks)
                                        └──▶ SKL-03-11 (Perform Risk Analysis)
                                                  └──▶ SKL-03-12 (Plan Risk Responses)

Pack 03 — Integration (final step — PLANNED)
────────────────────────────────────────────────────────
All Pack 03 skills ──▶ SKL-03-01 (Integrate and Align Project Plans → A14)
                              └──▶ [Pack 04 Executing begins]
```

---

## Build Progress Summary

| Pack | Skill ID | Skill Name | Status |
|------|----------|-----------|--------|
| 02 | SKL-02-01 | Initiate Project or Phase | ✅ Draft · Untested |
| 02 | SKL-02-02 | Identify Stakeholders | ✅ Draft · Untested |
| 03 | SKL-03-01 | Integrate and Align Project Plans | 🔲 Planned |
| 03 | SKL-03-02 | Plan Scope Management | 🔲 Planned |
| 03 | SKL-03-03 | Elicit and Analyze Requirements | 🔲 Planned |
| 03 | SKL-03-04 | Define Scope | 🔲 Planned |
| 03 | SKL-03-05 | Develop Scope Structure | 🔲 Planned |
| 03 | SKL-03-06 | Plan Schedule Management | 🔲 Planned |
| 03 | **SKL-03-07** | **Plan Stakeholder Engagement** | ✅ **Draft · Untested** |
| 03 | **SKL-03-08** | **Plan Communications Management** | ✅ **Draft · Untested** |
| 03 | SKL-03-09 | Plan Risk Management | 🔲 Planned |
| 03 | SKL-03-10 | Identify Risks | 🔲 Planned |
| 03 | SKL-03-11 | Perform Risk Analysis | 🔲 Planned |
| 03 | SKL-03-12 | Plan Risk Responses | 🔲 Planned |
| 03 | SKL-03-13 | Plan Financial Management | 🔲 Planned |
| 03 | SKL-03-14 | Estimate Costs | 🔲 Planned |
| 03 | SKL-03-15 | Develop Budget | 🔲 Planned |
| 03 | SKL-03-16 | Plan Resource Management | 🔲 Planned |
| 03 | SKL-03-17 | Estimate Resources | 🔲 Planned |
| 04 | SKL-04-xx | (Executing skills — TBD) | 🔲 Not started |
| 05 | SKL-05-xx | (Monitoring skills — TBD) | 🔲 Not started |
| 06 | SKL-06-xx | (Closing skills — TBD) | 🔲 Not started |

**Built:** 4 skills  
**Planned (shell entries):** 15+ skills  
**Not started:** Pack 04, 05, 06

---

## Artifact Cross-Reference

This table shows which artifact each built skill writes to, to prevent conflicts and confirm handoff points.

| Artifact | Created By | Written By (Identification) | Written By (Strategy/Plan) | Updated By |
|---------|-----------|---------------------------|--------------------------|-----------|
| A04 — Project Charter | SKL-02-01 | — | — | — |
| A05 — Context Register | SKL-02-01 | SKL-02-01 | SKL-02-02 (OPA updates) | SKL-03-07 · SKL-03-08 |
| A07 — Stakeholder Register and Engagement Strategy | SKL-02-02 | SKL-02-02 | SKL-03-07 | SKL-03-08 (engagement updates) |
| A14 — Integrated PM Plan | SKL-03-01 | — | SKL-03-01 | All planning skills (subsidiary references) |
| A15 — Schedule Model and Baseline Record | SKL-03-06 | — | — | SKL-03-08 (communication events) |
| A19 — Risk Management Record | SKL-03-09 | SKL-02-02 (engagement risk flags) | SKL-03-09 | SKL-03-07 · SKL-03-10 · SKL-03-11 · SKL-03-12 |
| A28 — Communications and Reporting Record | SKL-03-08 | — | SKL-03-08 | SKL-04-Manage Communications |

---

## Naming and ID Conventions

| Convention | Rule |
|-----------|------|
| Skill ID format | `SKL-PP-NN` — PP = 2-digit pack number; NN = 2-digit sequence within pack |
| File naming | `SKL-PP-NN-kebab-case-skill-name.md` |
| Pack folder | `skills/PP-packname/` (e.g., `skills/03-planning/`) |
| Status values | `Draft · Untested` → `Draft · In Review` → `Reviewed` → `Approved · Production` |
| Source type | `PMI-derived` / `synthesis` / `organization-defined` — must match artifact model labels |
| PMBOK8 anchor | Always cite Guide section number + Figure number (e.g., `§2.5.2.3 · Figure 2-35`) |

---

## Registry Maintenance Rules

1. **Add a shell entry for every planned skill before it is built** — the registry must always show the full planned build scope, not just what exists.
2. **Update status immediately** when a skill file is created, reviewed, or approved.
3. **Update the Artifact Cross-Reference table** whenever a skill adds a new artifact write target.
4. **Update the Dependency Chain Diagram** when a new skill is added whose position in the chain is not obvious.
5. **Never remove a skill entry** — if a skill is deprecated, mark it as `Deprecated · Replaced by SKL-XX-XX` and add a note.
6. **This registry is not a skill file** — it does not contain instructions, tests, or step-by-step guidance; those belong in the individual skill files.

---

*Authority: PMBOK8 · Artifacts-V-1.0.5 · Repository Operating Rules §3.2 Consolidation Rule*  
*Owner: Repository Maintainer (PM or designated skills lead)*  
*Approval Authority: None required for routine updates; sponsor awareness for major structural changes*  
*Re-run: Maintained continuously — updated with every new skill build or status change*

<p align="center">
  <img src="docs/img/pmoskills.jpeg" alt="PMOSkills logo" width="360">
</p>

```
===================================================================
      _____   __  __   ____     ____   _  __  _   _   _       ____  
     |  __ \ |  \/  | / __ \   / ___| | |/ / | | | | | |     / ___| 
     | |__) || \  / || |  | |  \___ \ | ' /  | | | | | |     \___ \ 
     |  ___/ | |\/| || |  | |   ___) || . \  | | | | | |___   ___) |
     |_|     |_|  |_| \____/   |____/ |_|\_\ |_| |_| |_____| |____/ 
                                                                    
========================= PMBOK 8 ALIGNED =========================
```

# PMO Skill Repository
**Version:** 1.4.0
**Authority:** PMBOK 8 (Primary) · PMI Companion References (Secondary) · Organization-Defined Methods (Tertiary)
**Scope:** Organizational Setup through Project Closure — full project lifecycle PMO reference and point of truth
**Status:** Active development

---

## Disclaimer
This repository contains personal summaries, interpretations, and educational notes
compiled from public project management frameworks. "PMBOK" and "PMI" are registered
trademarks of the Project Management Institute, Inc. This project is independently
developed and is not affiliated with, endorsed by, or sponsored by PMI.

---

## Purpose

This repository is the **authoritative PMO reference** for all project management templates, charters, logs, processes, task outputs, and input-handling procedures. It serves as an executable skill system — not just a template library — grounded in PMI PMBOK 8th Edition.

Every skill in this repository can:
- **Generate** a first draft of a required artifact
- **Update** an artifact under change or new information
- **Validate** an artifact against PMBOK 8 quality criteria
- **Route** decisions to the correct governance authority
- **Close or archive** artifacts at phase or project end

---

## Coverage

| Layer | Coverage |
|-------|----------|
| **Lifecycle** | Organizational Setup → Initiating → Planning → Executing → Monitoring & Controlling → Closing → Adaptive & Hybrid |
| **Skills Built** | **47 skills across 7 packs** (SKL-01-01 through SKL-07-04) — all packs complete |
| **Performance Domains** | Governance · Scope · Schedule · Finance · Stakeholders · Resources · Risk · Team · Measurement · Delivery · Development Approach & Life Cycle |
| **Principles** | All 12 PMBOK 8 Standard principles embedded in every skill |
| **Processes** | All 40 PMBOK processes — fully documented in `/C4-Process-Records/` (PR01–PR40) |
| **Appendices** | PMO (X2) · AI (X3) · Procurement (X4) · PMBOK Evolution (X5) |
| **Governance Layers** | Organizational · OPM · PMO · Portfolio/Program/Project · Delivery Team |
| **Artifacts** | A01–A41 (Artifacts-V-1.1.md) fully mapped to skills |

---

## Repository Structure

```
pmo-skill-repo/
├── README.md                        ← This file
├── SKILL-REGISTRY.md                ← Master index of all 47 skills (v1.3.0)
├── AUTHORITY-ROUTING.md             ← T1–T4 threshold model and escalation rules
├── LIFECYCLE-MAP.md                 ← Visual and tabular lifecycle flow
├── PRINCIPLES-CROSSWALK.md          ← 12 principles × 11 domains × 40 processes
├── source-authority.md              ← Source authority rules and reference list
├── pmi_reference_list.md            ← Canonical PMI reference list
│
├── docs/
│   └── img/
│       └── pmoskills.jpg            ← Repository logo
│
├── C4-Process-Records/              ← ✅ All 40 PMBOK process records (PR01–PR40)
│   ├── PR01-Develop-Project-Charter.md
│   ├── PR02-Identify-Stakeholders.md
│   ├── PR03-Develop-Project-Management-Plan.md
│   ├── PR04-Plan-Scope-Management.md
│   ├── PR05-Collect-Requirements.md
│   ├── PR06-Define-Scope.md
│   ├── PR07-Create-WBS.md
│   ├── PR08-Plan-Schedule-Management.md
│   ├── PR09-Define-Activities.md
│   ├── PR10-Sequence-Activities.md
│   ├── PR11-Estimate-Activity-Resources.md
│   ├── PR12-Estimate-Activity-Durations.md
│   ├── PR13-Develop-Schedule.md
│   ├── PR14-Plan-Cost-Management.md
│   ├── PR15-Estimate-Costs.md
│   ├── PR16-Determine-Budget.md
│   ├── PR17-Plan-Quality-Management.md
│   ├── PR18-Plan-Resource-Management.md
│   ├── PR19-Plan-Communications-Management.md
│   ├── PR20-Plan-Risk-Management.md  [note: PR20=Plan-Risk listed; PR21 in files]
│   ├── PR21-Plan-Risk-Management.md
│   ├── PR22-Identify-Risks.md
│   ├── PR23-Perform-Qualitative-Risk-Analysis.md
│   ├── PR24-Perform-Quantitative-Risk-Analysis.md
│   ├── PR25-Plan-Risk-Responses.md
│   ├── PR26-Plan-Procurement-Management.md
│   ├── PR27-Plan-Stakeholder-Engagement.md
│   ├── PR28-Direct-and-Manage-Project-Work.md
│   ├── PR29-Manage-Project-Knowledge.md
│   ├── PR30-Monitor-and-Control-Project-Work.md
│   ├── PR31-Perform-Integrated-Change-Control.md
│   ├── PR32-Validate-Scope.md
│   ├── PR33-Control-Scope.md
│   ├── PR34-Control-Schedule.md
│   ├── PR35-Control-Costs.md
│   ├── PR36-Monitor-Communications.md
│   ├── PR37-Control-Quality.md
│   ├── PR38-Control-Resources.md
│   ├── PR39-Monitor-Risks.md
│   └── PR40-Close-Project-or-Phase.md
│
├── C5-KA-Crossref/                  ← ✅ Knowledge Area Cross-Reference Index
│   └── KA-Crossref-Index.md
│
├── reference/                       ← [planned] PMBOK 8 reference layer
│   ├── principles/                  ← [planned] 12 PMBOK 8 principles, detailed notes
│   ├── performance-domains/         ← [planned] 11 domain summaries with process maps
│   ├── focus-areas/                 ← [planned] 5 focus areas with artifact triggers
│   ├── inputs-outputs/              ← [planned] inputs-outputs-registry.md (PMBOK 8 §4)
│   ├── tools-techniques/            ← [planned] tools-techniques-registry.md (PMBOK 8 §5)
│   └── appendices/
│       ├── X2-pmo.md                ← [planned]
│       ├── X3-ai.md                 ← [planned]
│       ├── X4-procurement.md        ← [planned]
│       └── X5-evolution.md          ← [planned]
│
├── artifacts/
│   ├── closing/                     ← Closing artifacts (A21-final, A27)
│   ├── monitoring-and-decisions/    ← M&C artifacts (A12, A17, A18)
│   ├── planning-and-baselines/      ← Planning artifacts (A06, A08, A14, A15, A16, A19, A26, A28)
│   ├── procurement/                 ← Procurement artifacts (A31)
│   ├── resources/                   ← Resource artifacts (A03, A26-ext)
│   └── stakeholders/                ← Stakeholder artifacts (A02, A07)
│
├── skills/
│   ├── 01-organizational-setup/     ← Governance, doc control, repo config (3 skills)
│   ├── 02-initiating/               ← Initiate Project or Phase focus area (2 skills)
│   ├── 03-planning/                 ← Planning focus area (17 skills)
│   ├── 04-executing/                ← Executing focus area (9 skills)
│   ├── 05-monitoring-controlling/   ← Monitor and Control focus area (9 skills)
│   ├── 06-closing/                  ← Close Project or Phase focus area (3 skills)
│   └── 07-adaptive-hybrid/          ← Adaptive & Hybrid lifecycle skills (4 skills)
│
├── shared/                          ← [planned] Reusable components and validators
│   ├── components/                  ← [planned] Reusable field blocks and section patterns
│   ├── validators/                  ← [planned] Waste-test and quality-check routines
│   ├── routing/                     ← [planned] Authority routing logic per decision type
│   └── checklists/                  ← [planned] Domain and phase readiness checklists
│
└── tests/                           ← [planned] Skill and integration test cases
    ├── skill-tests/                 ← [planned] Test cases per skill (inputs → expected outputs)
    └── integration-tests/           ← [planned] Cross-skill flow tests (e.g., Setup → Close)
```

---

## Skills Summary

| Pack | Name | Skills | Status |
|------|------|--------|--------|
| 01 | Organizational Setup | 3 | ✅ Complete |
| 02 | Initiating | 2 | ✅ Complete |
| 03 | Planning | 17 | ✅ Complete |
| 04 | Executing | 9 | ✅ Complete |
| 05 | Monitoring & Controlling | 9 | ✅ Complete |
| 06 | Closing | 3 | ✅ Complete |
| 07 | Adaptive & Hybrid | 4 | ✅ Complete |
| **—** | **TOTAL** | **47** | ✅ **All packs complete** |

---

## Process Records Summary (C4)

| Process Group | Count | PR Range | Status |
|---|---|---|---|
| Initiating | 2 | PR01–PR02 | ✅ |
| Planning | 25 | PR03–PR27 | ✅ |
| Executing | 3 | PR28–PR30 | ✅ |
| Monitoring & Controlling | 9 | PR31–PR39 | ✅ |
| Closing | 1 | PR40 | ✅ |
| **TOTAL** | **40** | **PR01–PR40** | ✅ **Complete** |

---

## Reference Indices Summary (C5)

| Index | File | Status |
|---|---|---|
| Knowledge Area Cross-Reference | `C5-KA-Crossref/KA-Crossref-Index.md` | ✅ Complete |
| Tools & Techniques Taxonomy | `C6-TT-Taxonomy/` | 🔜 Next |
| Inputs/Outputs Master Registry | `C7-IO-Registry/` | 🔜 Planned |

---

## Authority Model

1. **Primary:** PMBOK8 — The Standard for Project Management + PMBOK Guide 8th Edition
2. **Secondary:** PMO-Guide · GPPP · OPM-Standard · Process-Groups · PMI-BA · BAP-2E · Requirements · Complexity · Risk-PPP · Forms-Book
3. **Tertiary:** Organization-defined operating methods (explicitly labeled)

All artifacts are labeled: `PMI-derived` | `synthesis` | `organization-defined`

---

## Governance Layer Model

| Layer | Concern | Typical Authority |
|-------|---------|------------------|
| Organizational Governance | Enterprise direction, policy, compliance | Executive leadership, governing body |
| OPM Governance | Strategic alignment across portfolios/programs/projects | OPM governing body, portfolio forums |
| PMO Governance | PMO services, methods, improvement | PMO leader, PMO governance forum |
| Portfolio/Program/Project Governance | Prioritization, authorization, oversight, value delivery | Portfolio board, sponsor, project governing body |
| Delivery Team Ways of Working | Day-to-day execution, cadence, collaboration | Project manager, delivery lead, team |

---

## Decision Threshold Model (T1–T4)

| Band | Characteristics | Default Authority |
|------|----------------|------------------|
| T1 Operational | Localized, low risk, inside plan tolerances | Project manager or designated lead |
| T2 Controlled Change | Material effect on one baseline, within project authority | Sponsor-delegated board or change authority |
| T3 Governance Change | Cross-baseline, major financial/schedule/value impact | Project governing body or sponsor |
| T4 Enterprise Portfolio | Cross-project, strategic, regulatory, or enterprise impact | Portfolio authority, PMO forum, or executive |

---

## How to Use This Repository

### As a PMO Reference
1. Navigate to `SKILL-REGISTRY.md` and filter by lifecycle stage, domain, or artifact
2. Open the relevant skill file for instructions, inputs, outputs, and constraints
3. Use templates from `artifacts/` to generate the artifact
4. Apply authority routing from `AUTHORITY-ROUTING.md`

### As an AI Agent
1. Load `SKILL-REGISTRY.md` as the routing index
2. Parse the user's intent against lifecycle stage + domain + artifact type
3. Execute the matched skill instruction set
4. Validate output against the skill's defined failure cases and tests
5. Route for approval per the T1–T4 threshold model

### As a Book Authoring Reference
1. Use `C4-Process-Records/` for all 40 process records with full I/O/T&T detail
2. Use `C5-KA-Crossref/` for Knowledge Area to process mapping
3. Use `PRINCIPLES-CROSSWALK.md` for principle-to-domain mappings
4. Use artifact definitions in `artifacts/` for structured chapter sections

---

## Related Repository Files

| File | Purpose |
|------|---------|
| `SKILL-REGISTRY.md` | Master skill index — all 47 skills, dependency chains, artifact cross-reference |
| `AUTHORITY-ROUTING.md` | T1–T4 threshold model, escalation rules, authority RACI |
| `LIFECYCLE-MAP.md` | Phase-by-phase process and artifact flow |
| `PRINCIPLES-CROSSWALK.md` | 12 principles × 11 domains matrix |
| `source-authority.md` | Source authority rules, reference hierarchy |
| `pmi_reference_list.md` | Canonical list of all PMI references used in this repo |
| `C4-Process-Records/` | All 40 PMBOK process records (PR01–PR40) |
| `C5-KA-Crossref/KA-Crossref-Index.md` | Knowledge Area × Process Group × PR number cross-reference |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0-draft | 2026-05-29 | Initial structure — repo skeleton, README, registry schema defined |
| 1.1.0 | 2026-05-29 | Pack 02 (Initiating) and Pack 03 (Planning, 17 skills) complete; SKILL-REGISTRY.md established |
| 1.2.0 | 2026-05-29 | Pack 04 (Executing, 9 skills) complete; artifacts/ subdirectories created |
| 1.3.0 | 2026-05-30 | Packs 05–07 complete (22 skills); all 47 skills built; SKILL-REGISTRY.md v1.3.0; README updated to reflect actual repo structure |
| 1.3.1 | 2026-05-31 | Added logo reference (docs/img/pmoskills.jpg), ASCII art banner, and PMI disclaimer |
| 1.4.0 | 2026-05-31 | C4 complete: all 40 process records (PR01–PR40) in C4-Process-Records/; C5 KA Cross-Reference Index added; README updated |

---

*Authority: PMBOK 8 Primary · PMI Companion References Secondary · Organization-Defined Tertiary*
*This repository is part of the PMI PMBOK 8 Knowledge Base Space.*

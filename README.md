<p align="center">
  <img src="docs/img/pmoskills.jpeg" alt="PMOSkills logo" width="460">
</p>



# PMO Skill Repository
**Version:** 4.5.0
**Authority:** PMBOK 8 (Primary) · PMI Companion References (Secondary) · Organization-Defined Methods (Tertiary)
**Scope:** Organizational Setup through Project Closure — full project lifecycle PMO reference and point of truth
**Status:** Active development

---

## Disclaimer
This repository contains personal summaries, interpretations, and educational notes compiled from public project management frameworks. "PMBOK" and "PMI" are registered trademarks of the Project Management Institute, Inc. This project is independently developed and is not affiliated with, endorsed by, or sponsored by PMI.

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
| **Processes** | All 40 PMBOK processes — fully documented in `reference/processes/` (PR01–PR40) |
| **Appendices** | PMO (X2) · AI (X3) · Procurement (X4) · PMBOK Evolution (X5) |
| **Governance Layers** | Organizational · OPM · PMO · Portfolio/Program/Project · Delivery Team |
| **Artifacts** | A01–A39 (Artifacts-V-1.1.md) fully mapped to skills |

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
├── MASTER-PLAN.md                   ← Master tracking roadmap (v4.7.0)
├── QUALITY-STANDARDS.md             ← Single source of truth for schemas & gates (v2.0.0)
│
├── Archive/                         ← Creation artifacts, old completion plans, and legacy drafts
│   ├── COMPLETION-PLAN.md           ← Phase-by-phase completion plan (v4.1.0)
│   ├── legacy/                      ← Archived historical draft files and monolithic exports
│   └── meta/                        ← Skills generation metadata
│
├── docs/
│   └── image/
│       └── pmoskills.jpeg           ← Repository logo
│
├── reference/                       ← PMBOK 8 Reference Layer
│   ├── README.md                    ← Reference structure explanation
│   ├── principles/                  ← 12 PMBOK 8 principles (P01–P12 + index)
│   ├── performance-domains/         ← 8 performance domains (PD01–PD08 + index)
│   ├── focus-areas/                 ← 5 focus areas (FA01–FA05)
│   ├── processes/                   ← 40 process records (PR01–PR40 + indices)
│   ├── knowledge-areas/             ← Knowledge Area index (migrated from C5)
│   ├── tools-techniques/            ← Tools & Techniques index (migrated from C6)
│   ├── inputs-outputs/              ← Inputs & Outputs registry (migrated from C7)
│   └── appendices/                  ← PMO, AI, Sourcing appendices [planned]
│
├── artifacts/                       ← Lean and Audited Artifacts Catalog
│   ├── initiating/                  ← Project startup records (A01, A02, A04)
│   ├── planning-and-baselines/      ← Subsidiary management plans & models (A06, A08, A14, A15, A16, A28)
│   ├── resources/                   ← Resource registries and team documents (A03, A20, A25, A26, A27)
│   ├── stakeholders-communications/ ← Communication models (A07, A10, A28, A29)
│   ├── procurement/                 ← Procurement & supplier records (A11, A31, A32, A33)
│   ├── quality/                     ← Requirements traceability & quality (A09, A13)
│   ├── knowledge/                   ← Lesson registries & data records (A30)
│   ├── monitoring-and-decisions/    ← Controls (A12, A17, A18, A19, A20, A21)
│   ├── closure/                     ← Realization & transition logs (A24, A27)
│   ├── governance/                  ← Retention & privacy registers (A05, A34, A35, A37, A39)
│   ├── pmo/                         ← PMO metrics & improvements (A23, A36)
│   └── portfolio/                   ← Interdependency models (A22)
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
├── shared/                          ← Reusable components and validators
│   ├── README.md
│   ├── components/                  ← Field blocks and section patterns [planned]
│   ├── validators/                  ← Waste-test and quality-check routines [planned]
│   ├── routing/                     ← Authority routing logic per decision type [planned]
│   └── checklists/                  ← Domain and phase readiness checklists [planned]
│
└── tests/                           ← Skill and integration test cases
    ├── README.md
    ├── skill-tests/                 ← Test cases per skill [planned]
    └── integration-tests/           ← Cross-skill flow tests (e.g., Setup → Close) [planned]
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

## Process Records Summary

| Process Group | Count | PR Range | Status |
|---|---|---|---|
| Initiating | 2 | PR01–PR02 | ✅ Complete |
| Planning | 25 | PR03–PR27 | ✅ Complete |
| Executing | 3 | PR28–PR30 | ✅ Complete |
| Monitoring & Controlling | 9 | PR31–PR39 | ✅ Complete |
| Closing | 1 | PR40 | ✅ Complete |
| **TOTAL** | **40** | **PR01–PR40** | ✅ **Complete** |

---

## Reference Indices Summary

| Index | Canonical Location | Status |
|---|---|---|
| Knowledge Area Cross-Reference | `reference/knowledge-areas/KA-Crossref-Index.md` | ✅ Complete |
| Tools & Techniques Taxonomy | `reference/tools-techniques/TT-Taxonomy-Index.md` | ✅ Complete |
| Inputs/Outputs Master Registry | `reference/inputs-outputs/IO-Registry-Index.md` | ✅ Complete |

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
1. Use `reference/processes/` for all 40 process records with full I/O/T&T detail
2. Use `reference/knowledge-areas/KA-Crossref-Index.md` for Knowledge Area to process mapping
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
| `MASTER-PLAN.md` | Master development plan and session log |
| `docs/implementation-plan.md` | Approved Phase 8 next steps implementation plan |
| `Archive/COMPLETION-PLAN.md` | Phase-by-phase completion roadmap (archived) |
| `QUALITY-STANDARDS.md` | Canonical quality gates, YAML schemas, and pre-commit checklists |

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
| **4.5.0** | **2026-06-01** | **Phase 0 Cleanup Complete: all legacy root directories and duplicate standards files removed. Post-migration README alignment to show clean reference/ and artifacts/ structures.** |
| **4.7.0** | **2026-06-02** | **Phases 6 & 7 Complete: 48 skill test suites, 7 integration tests, naming normalization, and archiving of non-relevant development files.** |

---

*Authority: PMBOK 8 Primary · PMI Companion References Secondary · Organization-Defined Tertiary*
*This repository is part of the PMI PMBOK 8 Knowledge Base Space.*

---

```
===================================================================
      _____   __  __   ____     ____   _  __  _   _   _       ____  
     |  __ \ |  \/  | / __ \   / ___| | |/ / | | | | | |     / ___| 
     | |__) || \  / || |  | |  \___ \ | ' /  | | | | | |     \___ \ 
     |  ___/ | |\/| || |  | |   ___) || . \  | | | | | |___   ___) |
     |_|     |_|  |_| \____/   |____/ |_|\_\ |_| |_| |_____| |____/ 
                                                                     
========================= PMBOK 8 ALIGNED =========================
```
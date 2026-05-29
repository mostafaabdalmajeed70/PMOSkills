# PMO Skill Repository
**Version:** 1.0.0-draft  
**Authority:** PMBOK 8 (Primary) · PMI Companion References (Secondary) · Organization-Defined Methods (Tertiary)  
**Scope:** Pre-sign through Project Closure — full project lifecycle PMO reference and point of truth  
**Status:** Active development

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
| **Lifecycle** | Pre-sign → Initiating → Planning → Executing → Monitoring & Controlling → Closing |
| **Performance Domains** | Governance · Scope · Schedule · Finance · Stakeholders · Resources · Risk |
| **Principles** | All 6 PMBOK 8 Standard principles embedded in every skill |
| **Processes** | All 40 nonprescriptive PMBOK 8 processes mapped and anchored |
| **Appendices** | PMO (X2) · AI (X3) · Procurement (X4) · PMBOK Evolution (X5) |
| **Governance Layers** | Organizational · OPM · PMO · Portfolio/Program/Project · Delivery Team |
| **Artifacts** | A01–A41 (Artifacts-V-1.1.md) fully mapped to skills |

---

## Repository Structure

```
pmo-skill-repo/
├── README.md                        ← This file
├── SKILL-REGISTRY.md                ← Master index of all skills
├── AUTHORITY-ROUTING.md             ← T1–T4 threshold model and escalation rules
├── LIFECYCLE-MAP.md                 ← Visual and tabular lifecycle flow
├── PRINCIPLES-CROSSWALK.md          ← 6 principles × 7 domains × 40 processes
│
├── reference/
│   ├── principles/                  ← 6 PMBOK 8 principles, detailed notes
│   ├── performance-domains/         ← 7 domain summaries with process maps
│   ├── focus-areas/                 ← 5 focus areas with artifact triggers
│   ├── processes/                   ← 40 process records (I/O/T&T per process)
│   ├── inputs-outputs/              ← inputs-outputs-registry.md (PMBOK 8 §4)
│   ├── tools-techniques/            ← tools-techniques-registry.md (PMBOK 8 §5)
│   └── appendices/
│       ├── X2-pmo.md
│       ├── X3-ai.md
│       ├── X4-procurement.md
│       └── X5-evolution.md
│
├── artifacts/
│   ├── definitions/                 ← A01–A41 definitions (from Artifacts-V-1.1.md)
│   ├── templates/                   ← Fillable markdown templates per artifact
│   └── examples/                   ← Completed examples per artifact type
│
├── skills/
│   ├── 00-core/                     ← Shared skill components, validators, helpers
│   ├── 01-pre-sign/                 ← Before formal project authorization
│   ├── 02-initiating/               ← Initiate Project or Phase focus area
│   ├── 03-planning/                 ← Integrate and Align Project Plans focus area
│   ├── 04-executing/                ← Manage Project Execution focus area
│   ├── 05-monitoring-controlling/   ← Monitor and Control focus area
│   ├── 06-closing/                  ← Close Project or Phase focus area
│   ├── 07-pmo/                      ← PMO configuration, services, maturity
│   └── 08-ai-procurement/           ← AI governance and procurement skills
│
├── shared/
│   ├── components/                  ← Reusable field blocks and section patterns
│   ├── validators/                  ← Waste-test and quality-check routines
│   ├── routing/                     ← Authority routing logic per decision type
│   └── checklists/                  ← Domain and phase readiness checklists
│
└── tests/
    ├── skill-tests/                 ← Test cases per skill (inputs → expected outputs)
    └── integration-tests/           ← Cross-skill flow tests (e.g., Pre-sign → Close)
```

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
3. Use templates from `artifacts/templates/` to generate the artifact
4. Apply authority routing from `AUTHORITY-ROUTING.md`

### As an AI Agent
1. Load `SKILL-REGISTRY.md` as the routing index
2. Parse the user's intent against lifecycle stage + domain + artifact type
3. Execute the matched skill instruction set
4. Validate output against the skill's defined failure cases and tests
5. Route for approval per the T1–T4 threshold model

### As a Book Authoring Reference
1. Use `reference/` directories for PMBOK 8 source-grounded chapter content
2. Use `PRINCIPLES-CROSSWALK.md` for principle-to-domain mappings
3. Use artifact definitions in `artifacts/definitions/` for structured chapter sections

---

## Related Repository Files

| File | Purpose |
|------|---------|
| `Artifacts-V-1.1.md` | Canonical artifact definitions A01–A41 |
| `Artifacts-Authorities-V-1.1.md` | Authority matrix, T1–T4 model, RACI defaults |
| `SKILL-REGISTRY.md` | Master skill index (this repo) |
| `LIFECYCLE-MAP.md` | Phase-by-phase process and artifact flow |
| `PRINCIPLES-CROSSWALK.md` | 6 principles × 7 domains matrix |
| `inputs-outputs-registry.md` | All 40 process I/O per PMBOK 8 §4 |
| `tools-techniques-registry.md` | All tools and techniques per PMBOK 8 §5 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0-draft | 2026-05-29 | Initial structure — repo skeleton, README, registry schema defined |

---

*Authority: PMBOK 8 Primary · PMI Companion References Secondary · Organization-Defined Tertiary*  
*This repository is part of the PMI PMBOK 8 Knowledge Base Space.*

# 🚀 PMOSkills Release Notes — v0.1

We are thrilled to announce the first stable release of **PMOSkills (v0.1)** — the industry's first **executable project management framework** and authoritative PMO reference architecture built directly upon the **PMI PMBOK® 8th Edition** and 23 secondary companion standards.

PMOSkills bridges the gap between high-level management standards and day-to-day workspace execution. It provides a unified, deterministic, and machine-readable operating system designed equally for **Human Project Managers** and **Autonomous AI Agents**.

---

## 🏷️ Release Metadata

* **Release Tag:** `v0.1`
* **Release Date:** June 2, 2026
* **Primary Authority:** PMI PMBOK® 8th Edition Compliant
* **Secondary Authority:** 23 Companion Reference Manuals (OPM, GPPP, BA, Risk-PPP, etc.)
* **Total Assets Audited:** **341 production-ready, verified files**

---

## 🌟 Core Feature Highlights

### 1. ⚙️ The Executable Skills Layer (48 Active Skills)
The core engine of PMOSkills consists of **48 programmatically modeled skills** organized across 7 functional packs representing the full project lifecycle:
* **Pack 01: Organizational Setup** (3 skills) — Repo setup, governance models, document control.
* **Pack 02: Initiating** (2 skills) — Project chartering, stakeholder identification.
* **Pack 03: Planning** (18 skills) — subsidiary plan developments (Scope, Budget, Schedule, Quality, Risk, Procurement).
* **Pack 04: Executing** (9 skills) — Work direction, resource acquisition, risk response implementation.
* **Pack 05: Monitoring & Controlling** (9 skills) — Baseline tracking, formal change control, gate reviews.
* **Pack 06: Closing** (3 skills) — Project transitions, administrative archivals, post-project reviews.
* **Pack 07: Adaptive & Hybrid** (4 skills) — Agile overlays, iteration planning, backlog grooming.

*Every skill is structured with strict YAML front-matter (`GOV` schema), programmatic input expectations, concrete execution steps, and clear exit criteria.*

### 2. 📁 Audited Artifacts Catalog (78 Clean Templates)
A comprehensive repository of lean and audited deliverables mapped directly to their execution skills. Unlike standard static templates, every file here:
* Features zero pre-filled brackets (`[...]` markers are reserved strictly for human/AI inputs).
* Enforces strict PMBOK 8 performance domain traceability.
* Separated into **12 logical subdirectories** representing distinct PMO lifecycle stages.

### 3. 📖 Unified Reference Layer (115 Standard Records)
Provides the baseline "rules of the game" derived directly from PMI standards:
* **12 Principles** and **8 Performance Domains** mapped as interactive reference documents.
* **41 Process Records (`PR01–PR41`)** providing process definitions, input/output registries, and tools/techniques.
* **Tailoring Frameworks & PMO Governance Models** built explicitly to match T1-T4 Decision Threshold definitions.

### 4. 🤖 AI Agent-Ready Infrastructure
Designed with LLM developers in mind, PMOSkills is a zero-dependency, machine-parsable environment:
* Every markdown document contains a **strict YAML header** specifying metadata attributes.
* **Prompting directives** and deterministic process maps allow LLMs to act as autonomous PMO co-pilots.
* Clean relative pathing allows agents to fetch context and read schemas instantly.

---

## 📈 System Composition & Verification

A summary of the verified assets packaged in this release:

```
Total Verified Assets: 341 files
├── Reference Layer: 115 files (100% complete)
├── Skills Layer: 48 active files (100% complete)
├── Artifacts Layer: 78 templates and examples (100% complete)
├── Shared Validators: 25 script components (100% complete)
└── Compliance Test Suites: 69 test files (100% complete)
```

### 🧪 Automated Quality Gates (L1–L3 PASSED)
Prior to this release, the repository successfully passed the **3-Tier Continuous Quality Gates** checked programmatically:
1. **L1 (Structural):** Programmatic verification of all filenames (strict lower-case kebab-case) and schema alignments.
2. **L2 (Content & Citation):** Core citation verification mapping to PMBOK 8th Edition performance domains.
3. **L3 (Integration & Flow):** End-to-end scenario flow tests mapping predictive, hybrid, and adaptive project routes.

---

## 🚀 How to Get Started

### For Human Project Managers
1. Read the **[`README.md`](README.md)** and the **[`docs/user-friendly-guide.md`](docs/user-friendly-guide.md)** for a friendly onboarding walkthrough.
2. Consult the **[`SKILL-REGISTRY.md`](SKILL-REGISTRY.md)** to find the exact skill file for your task.
3. Fetch the clean template from the corresponding **[`artifacts/`](artifacts/)** folder and execute the task!

### For AI Agent Developers
1. Point your agent framework (LangChain, AutoGPT, custom LLMs) to **[`SKILL-REGISTRY.md`](SKILL-REGISTRY.md)** as the primary tool lookup catalog.
2. Direct the agent to parse the strict YAML headers under `skills/` for execution rules and constraints.
3. Instruct the agent to run **[`shared/validate_structure.py`](shared/validate_structure.py)** to confirm output structure is mathematically aligned with the framework rules.

---

## ⚖️ License & Maintainer

* **License:** MIT License
* **Framework Authority:** PMBOK 8 Core Standard & PMO Governance Board
* **Repository:** [fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
* **Lead Architect:** **Mohamed Fouad Fakhruldeen** (Website: [fakhruldeen.me](https://fakhruldeen.me) | LinkedIn: [in/fakhruldeen](https://www.linkedin.com/in/fakhruldeen))

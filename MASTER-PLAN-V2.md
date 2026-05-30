# PMOSkills Repository — Master Development Plan
**Version:** 2.0.0
**Date:** 2026-05-30
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0

---

## 1. Current State Assessment (as of 2026-05-30)

### 1.1 Repository Structure

| Directory / File | Status | Notes |
|---|---|---|
| `README.md` | ✅ v1.3.0 | Updated Patch C |
| `SKILL-REGISTRY.md` | ✅ 54,932 bytes | Full registry — Packs 01–07 |
| `AUTHORITY-ROUTING.md` | ✅ 14,543 bytes | T1–T4 routing complete |
| `LIFECYCLE-MAP.md` | ✅ 12,559 bytes | All 7 packs mapped |
| `PRINCIPLES-CROSSWALK.md` | ✅ 8,110 bytes | 12 principles × domains |
| `pmi_reference_list.md` | ✅ 6,819 bytes | 23 references catalogued |
| `source-authority.md` | ✅ 8,344 bytes | Authority hierarchy documented |
| `CODE_OF_CONDUCT.md` | ✅ New | Contributor Covenant 2.1 + PMI ethics |
| `CONTRIBUTING.md` | ✅ New | Full workflow, authority rules, commit conventions |
| `SECURITY.md` | ✅ New | Secrets, PII, AI agent security |
| `.github/ISSUE_TEMPLATE/` | ✅ New | 3 templates: bug, content, improvement |
| `.github/pull_request_template.md` | ✅ New | Full PMBOK-quality PR checklist |
| `LICENSE` | ✅ Present | |
| `.gitignore` | ✅ Present | |

### 1.2 Skills Layer

| Pack | Folder | Skills Present | Target | Gap |
|---|---|---|---|---|
| Pack 00 — Core / Org Setup | `skills/00-organizational-setup/` | SKL-01-01, 01-02, 01-03 | 3 | ✅ 0 missing |
| Pack 01 — Pre-Sign | `skills/01-pre-sign/` | **Status: confirm** | 3 | ❓ Verify |
| Pack 02 — Initiating | `skills/02-initiating/` | SKL-02-01, 02-02 | 2 | ✅ 0 missing |
| Pack 03 — Planning | `skills/03-planning/` | SKL-03-01 through 03-17 | 17 | ✅ 0 missing |
| Pack 04 — Executing | `skills/04-executing/` | SKL-04-01 through 04-09 | 9 | ⚠️ Naming collision exists |
| Pack 05 — Monitoring & Controlling | `skills/05-monitoring-controlling/` | SKL-05-01 (monitor-risks only) | 9 | ❌ 8 missing |
| Pack 06 — Closing | `skills/06-closing/` | None | 3 | ❌ 3 missing |
| Pack 07 — Adaptive & Hybrid | `skills/07-adaptive-hybrid/` | None | 4 | ❌ 4 missing |
| Pack PMO | `skills/07-pmo/` | None | 6 (proposed) | ❌ Not started |
| Pack AI | `skills/08-ai-procurement/` | None | 4 (proposed) | ❌ Not started |
| **TOTAL (core packs)** | | **~33 confirmed** | **47** | **❌ 14+ missing** |

### 1.3 Artifact Definitions Layer

| Subfolder | Files Present | Target | Status |
|---|---|---|---|
| `artifacts/planning-and-baselines/` | A06, A08, A14, A15, A16, A19, A26, A28 — 8 definition files | 8 definitions | ✅ Complete (definitions) |
| `artifacts/monitoring-and-decisions/` | A12, A17, A18 — 3 definition files | 3 definitions | ✅ Complete (definitions) |
| `artifacts/closing/` | A21, A27 — 2 definition files | 2 definitions | ✅ Complete (definitions) |
| `artifacts/stakeholders/` | A02, A07 — 2 definition files | 2 definitions | ✅ Complete (definitions) |
| `artifacts/resources/` | A03 — 1 definition file | 1 definition | ✅ Complete (definitions) |
| `artifacts/procurement/` | A31 — 1 definition file | 1 definition | ✅ Complete (definitions) |
| **Templates layer** | None | 17 template files | ❌ 0 of 17 done |
| **Examples layer** | None | 17 example files | ❌ 0 of 17 done |
| **Missing artifact definitions** | A01, A04, A05, A09, A10, A11, A13, A20, A22-A25, A29-A30, A32-A41 | ~24 definitions | ❌ Not yet written |

### 1.4 Reference / Shared / Tests Layer

| Directory | Status | Content Present |
|---|---|---|
| `reference/` | 🟡 Seeded | `README.md` + `principles/index.md` — structure defined, no content files |
| `shared/` | 🟡 Seeded | `README.md` — structure defined, no content files |
| `tests/` | 🟡 Seeded | `README.md` — structure defined, no content files |

### 1.5 Community / Governance Layer

| Area | Status |
|---|---|
| GitHub Community Standards | ✅ All 5 standards present — Code of Conduct, Contributing, Security, Issue Templates (×3), PR Template |
| Branch protection | ⚠️ Recommended — verify main branch protection is configured |
| GitHub Discussions | 🔵 Optional — consider enabling for community Q&A |
| GitHub Pages / Wiki | 🔵 Optional — future documentation site |

---

## 2. What the Old Plan Covered (v1.0.0) — Reconciliation

The `NEXT-STEPS-PLAN.md` v1.0.0 (2026-05-29) identified 7 phases. Here is the reconciliation against current state:

| Old Phase | What It Called For | Current Status |
|---|---|---|
| Phase 1 — Repair (Pack 04 naming collision) | Fix `SKL-04-01-implement-risk-responses.md` | ⚠️ Still required — action below |
| Phase 1 — Verify Pack 04 quality | Check all 9 Pack 04 files against template | ⚠️ Still required |
| Phase 2.1 — Complete Pack 05 (8 skills) | Write SKL-05-02 through 05-09 | ❌ Still missing |
| Phase 2.2 — Create Pack 06 (3 skills) | Write SKL-06-01 through 06-03 | ❌ Still missing |
| Phase 2.3 — Create Pack 07 Adaptive (4 skills) | Write SKL-07-01 through 07-04 | ❌ Still missing |
| Phase 2.4 — Confirm Pack 01 Pre-Sign | Verify `skills/01-pre-sign/` | ❓ Status unknown |
| Phase 3 — Artifact definitions + templates | Populate all A01–A41 definition, template, example files | 🟡 17 definitions done · templates and examples not started |
| Phase 4 — Reference layer | Build `reference/` tree | 🟡 Seeded only · no content files |
| Phase 5 — Shared + Tests | Build `shared/` and `tests/` | 🟡 Seeded only · no content files |
| Phase 6 — PMO + AI packs | Design and write Pack PMO + Pack AI skills | ❌ Not started |
| Phase 7 — QA sweep | Full quality pass + registry + README update | ❌ Not started |

**New items NOT in old plan (added in this version):**
- Community standards layer (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, issue templates, PR template) ✅ Done
- Book authoring track (dedicated phase — new)
- MCP server design and build track (dedicated phase — new)
- AI agent design track (dedicated phase — new)
- GitHub Actions / CI validation track (new)
- Glossary / Lexicon file (new)
- Artifact templates and examples (more explicit than old plan)
- CHANGELOG.md (new — versioning and release tracking)

---

## 3. Priority Issues — Fix Before Next Build Phase

### 3.1 ⚠️ Pack 04 Naming Collision (IMMEDIATE)

**Problem:** `skills/04-executing/SKL-04-01-implement-risk-responses.md` uses the ID prefix `SKL-04-01` but contains risk response content belonging to `SKL-04-08`.

**Action:**
1. Delete `skills/04-executing/SKL-04-01-implement-risk-responses.md`
2. Confirm `skills/04-executing/SKL-04-08-implement-risk-responses.md` is the canonical file
3. Verify `SKILL-REGISTRY.md` does not reference the deleted file path

### 3.2 ⚠️ SKL-05-01 Numbering Decision (IMMEDIATE)

**Problem:** The existing `SKL-05-01-monitor-risks.md` conflicts with the canonical registry where SKL-05-01 = "Monitor and Control Project Work" and SKL-05-06 = "Monitor Risks."

**Decision required:**
- **Option A:** Rename current file to `SKL-05-06-monitor-risks.md` (matches canonical registry)
- **Option B:** Keep as SKL-05-01 and renumber the rest of Pack 05

**Recommendation:** Option A — rename to SKL-05-06 to preserve registry integrity.

### 3.3 ⚠️ Pack 04 Quality Verification

Several Pack 04 files are below target depth. Compare against SKL-03-12 (49,673 bytes) as reference:

| Skill | Size | Action |
|---|---|---|
| SKL-04-01 | 7,160 bytes | Review — may need expansion |
| SKL-04-02 | 5,874 bytes | Likely needs expansion |
| SKL-04-03 | 6,832 bytes | Review |
| SKL-04-04 to 04-07 | 7,000–7,400 bytes | Acceptable — verify template completeness |
| SKL-04-08, 04-09 | 7,053 / 8,574 bytes | Acceptable |

### 3.4 ⚠️ Branch Protection

Verify that `main` branch has protection rules enabled:
- Require pull request before merging
- Require at least 1 review
- Disallow force pushes
- Disallow branch deletion

---

## 4. Master Build Roadmap — Phases and Tracks

### Phase A — Repair and Stabilize
**Priority:** 🔴 Immediate · **Estimated effort:** Low

| Task | Action | Output |
|---|---|---|
| A1 | Delete `SKL-04-01-implement-risk-responses.md` (naming collision) | Clean Pack 04 |
| A2 | Rename `SKL-05-01-monitor-risks.md` → `SKL-05-06-monitor-risks.md` | Registry-aligned Pack 05 |
| A3 | Verify Pack 01 Pre-Sign folder exists (`skills/01-pre-sign/`) | Confirmed or created |
| A4 | Verify Pack 04 skills against full template (YAML, Steps, Failure Modes, Tests) | Quality confirmed or expanded |
| A5 | Enable GitHub branch protection rules on `main` | Governance enforced |
| A6 | Add `CHANGELOG.md` to root | Version history tracking |

---

### Phase B — Complete Skills Layer (Core Packs)
**Priority:** 🔴 High · **Estimated effort:** High

#### B1 — Complete Pack 05: Monitoring & Controlling

| Skill ID | Skill Name | Primary Artifact | PMBOK8 Anchor |
|---|---|---|---|
| SKL-05-01 | Monitor and Control Project Work | A17 | Guide §2.1.6.6 |
| SKL-05-02 | Perform Integrated Change Control | A12 | Guide §2.1.6.7 |
| SKL-05-03 | Control Scope | A08 | Guide §2.3.2.7 |
| SKL-05-04 | Control Schedule | A15 | Guide §2.3.3.7 |
| SKL-05-05 | Control Costs | A16 | Guide §2.3.4.7 |
| SKL-05-06 | Monitor Risks *(rename from current 05-01)* | A19 | Guide §2.3.7.7 |
| SKL-05-07 | Monitor Stakeholder Engagement | A07 | Guide §2.5.2.7 |
| SKL-05-08 | Control Resources | A26 | Guide §2.6.2.7 |
| SKL-05-09 | Monitor Communications | A28 | Guide §2.4.2.7 |

**Delivery sequence:** SKL-05-01 → 05-02 → 05-03 → 05-04 → 05-05 → 05-06 → 05-07 → 05-08 → 05-09

#### B2 — Create Pack 06: Closing

| Skill ID | Skill Name | Primary Artifact | PMBOK8 Anchor |
|---|---|---|---|
| SKL-06-01 | Close Project or Phase | A27 | Guide §2.1.6.10 |
| SKL-06-02 | Final Performance Review | A17 | Guide §2.1.6.11 |
| SKL-06-03 | Capture and Archive Lessons Learned | A21 + A05 | Guide §2.1.6.12 |

#### B3 — Create Pack 07: Adaptive & Hybrid

| Skill ID | Skill Name | Primary Artifact | PMBOK8 Anchor |
|---|---|---|---|
| SKL-07-01 | Select and Tailor Lifecycle Approach | A06 | Guide §2.2 + Appendix §3 |
| SKL-07-02 | Manage Backlog and Iterations | A08 backlog section | Guide §2.3 adaptive |
| SKL-07-03 | Facilitate Retrospectives and Continuous Improvement | A21 | Guide §2.6.2.6 |
| SKL-07-04 | Plan and Deliver Hybrid Projects | A06 hybrid section | Guide §2.3.2 hybrid |

#### B4 — Confirm or Create Pack 01: Pre-Sign

| Skill ID | Skill Name | Primary Artifact |
|---|---|---|
| SKL-01-01 | Assess Business Need and Feasibility | A01 — Business Case |
| SKL-01-02 | Conduct Pre-Authorization Governance Review | A02 — Benefits Record |
| SKL-01-03 | Perform Stakeholder Pre-Identification | A07 pre-sign section |

**Skills layer completion target: 47 core skills total (Packs 00–07)**

---

### Phase C — Complete Artifact Definitions Layer
**Priority:** 🔴 High · **Estimated effort:** Very High

#### C1 — Missing Artifact Definitions (not yet written)

These 24 artifacts have no definition file yet:

| Artifact | Name | Priority Group |
|---|---|---|
| A01 | Business Case | 🔴 Initiating |
| A04 | Project Charter | 🔴 Initiating |
| A05 | Context Register (EEF/OPA) | 🔴 Initiating |
| A09 | Quality Management Plan | 🟠 Planning |
| A10 | Communications Management Plan | 🟠 Planning |
| A11 | Procurement Management Plan | 🟠 Planning |
| A13 | Requirements Traceability Matrix | 🟠 Planning |
| A20 | Team Charter | 🟠 Executing |
| A22 | Resource Acquisition Record | 🟡 Executing |
| A23 | Vendor Bid Documents | 🟡 Procurement |
| A24 | Source Selection Criteria | 🟡 Procurement |
| A25 | Resource Management Plan / RACI | 🟡 Executing |
| A29 | Meeting Records | 🟡 Executing |
| A30 | Project Closure Report | 🟡 Closing |
| A32 | Procurement SOW | 🟡 Procurement |
| A33 | PMO Charter | 🔵 PMO |
| A34 | Portfolio Register | 🔵 Portfolio |
| A35 | Program Benefits Plan | 🔵 Program |
| A36 | Governance Framework Record | 🔵 Governance |
| A37 | AI Project Readiness Assessment | 🔵 AI |
| A38 | AI Risk Register | 🔵 AI |
| A39 | Change Management Plan | 🟡 Change |
| A40 | OPM Maturity Assessment | 🔵 OPM |
| A41 | Benefits Realization Report | 🔵 Post-project |

#### C2 — Artifact Templates (all 41 artifacts)

For every artifact with a definition file, create a corresponding `*-template.md` file following the schema in `Artifacts-Templates-V-1.0.5-3.md`:

- File naming: `A##-[name]-template.md`
- Location: same subdirectory as definition file
- Content: fillable Markdown with `[FIELD: description]` placeholder syntax
- Each template must match its definition's section structure exactly

**Priority order:** A04 → A07 → A06 → A14 → A15 → A16 → A17 → A19 → A08 → A12 → A21 → A27 → A28 → A31 → A02 → A03 → A18 → remaining

#### C3 — Artifact Examples (priority artifacts)

For the 10 most-referenced artifacts, create a `*-example.md` with a realistic, anonymized project scenario:

Priority: A04 (Charter), A06 (PM Plan), A08 (Scope), A14 (WBS), A15 (Schedule), A16 (Budget), A17 (Performance Report), A19 (Risk Register), A21 (Lessons Learned), A27 (Closure Record)

---

### Phase D — Build Reference Layer
**Priority:** 🟠 Medium-High · **Estimated effort:** High

#### D1 — Principles Files (12 files)
Path: `reference/principles/`

Create one file per principle (P01–P12) containing:
- Full principle statement (PMBOK8 Standard §3)
- Behavioral indicators
- Anti-patterns
- Skill cross-references
- Domain applicability
- Supporting PMI references

**Priority:** P04 (Value), P07 (Tailoring), P10 (Risk), P01 (Stewardship) first — most referenced across skills.

#### D2 — Performance Domain Files (8 files)
Path: `reference/performance-domains/`

| File | Domain | PMBOK8 Section |
|---|---|---|
| PD01-stakeholders.md | Stakeholder Performance Domain | §2.5 |
| PD02-team.md | Team Performance Domain | §2.6 |
| PD03-development-approach.md | Development Approach & Life Cycle | §2.2 |
| PD04-planning.md | Planning Performance Domain | §2.3 |
| PD05-project-work.md | Project Work Performance Domain | §2.4 |
| PD06-delivery.md | Delivery Performance Domain | §2.7 |
| PD07-measurement.md | Measurement Performance Domain | §2.8 |
| PD08-uncertainty.md | Uncertainty Performance Domain | §2.9 |

#### D3 — Focus Area Files (5 files)
Path: `reference/focus-areas/`

FA01 through FA05 — each file maps: skills in focus area · artifacts triggered · principle anchors · entry/exit criteria.

#### D4 — Process Records (40 files)
Path: `reference/processes/`

One file per PMBOK 8 process covering: process name, process group, knowledge area, purpose, inputs, tools & techniques, outputs, PMBOK8 figure reference, skill cross-reference.

**Build in batches:** Initiating (2) → Planning (24) → Executing (10) → M&C (12) → Closing (2)

#### D5 — Registries
- `reference/inputs-outputs/inputs-outputs-registry.md` — all 40 processes × I/O
- `reference/tools-techniques/tools-techniques-registry.md` — all T&T indexed

#### D6 — Appendices
- `reference/appendices/X2-pmo.md` — needed before PMO pack
- `reference/appendices/X3-ai.md` — needed before AI pack
- `reference/appendices/X4-procurement.md`
- `reference/appendices/X5-evolution.md`

#### D7 — Lexicon / Glossary File
Path: `reference/GLOSSARY.md`

A single file mapping every PMBOK 8 term used in this repository to its PMBOK 8 Lexicon definition, with:
- Term · Definition (PMI Lexicon source) · First used in (Skill or Artifact ID) · Related terms

Source: `PMI Lexicon of Project Management Terms.pdf` (Space files)

---

### Phase E — Build Shared Layer
**Priority:** 🟡 Medium · **Estimated effort:** Medium

#### E1 — Routing Logic
- `shared/routing/threshold-router.md` — T1–T4 decision routing with decision trees
- `shared/routing/escalation-paths.md` — escalation path definitions per decision type

#### E2 — Validators
- `shared/validators/artifact-completeness-checker.md` — validates any artifact against required fields
- `shared/validators/waste-test.md` — waste detection routine for project activities
- `shared/validators/baseline-integrity-check.md` — cross-baseline consistency checker

#### E3 — Pack Readiness Checklists
- One file per pack: `shared/checklists/pack-readiness/pack-0X-readiness.md`
- Pre-gate checklist: `shared/checklists/domain-checklists/closure-readiness.md` (highest value first)

#### E4 — Reusable Field Components
- `shared/components/field-blocks/id-formats.md` — all ID schemas (A-NNN, B-NNN, CR-NNN, etc.)
- `shared/components/field-blocks/status-fields.md`
- `shared/components/section-patterns/quality-criteria-section.md`

---

### Phase F — Build Tests Layer
**Priority:** 🟡 Medium · **Estimated effort:** Medium-High

#### F1 — Skill Test Files
Target: 9 test cases per skill × 47 skills = **423 test case files**

Test case schema per `tests/README.md`:
```
Test ID: T-PP-NN-##
Skill: SKL-PP-NN
Preconditions:
Inputs:
Expected Outputs:
Pass Criteria:
Failure Cases:
Notes:
```

**Priority build order:**
1. `tests/skill-tests/00-organizational-setup/` — SKL-01-01, 01-02, 01-03 (3 files)
2. `tests/skill-tests/02-initiating/` — SKL-02-01, 02-02 (2 files)
3. `tests/skill-tests/03-planning/` — SKL-03-01 to 03-17 (17 files — highest leverage)
4. Remaining packs after skills are written and stabilized

#### F2 — Integration Test Files
Target: 7 integration tests

| File | Flow |
|---|---|
| IT-01-setup-to-initiating.md | Pack 00 → Pack 02 |
| IT-02-initiating-to-planning.md | Pack 02 → Pack 03 |
| IT-03-planning-to-executing.md | Pack 03 → Pack 04 |
| IT-04-executing-to-mc.md | Pack 04 → Pack 05 |
| IT-05-mc-to-closing.md | Pack 05 → Pack 06 |
| IT-06-hybrid-overlay.md | Pack 07 overlay on Pack 03–05 |
| IT-07-full-lifecycle.md | End-to-end flow test |

---

### Phase G — Extended Packs (PMO + AI)
**Priority:** 🔵 Lower · **Estimated effort:** Medium

#### G1 — Pack PMO (`skills/07-pmo/`)

| Skill ID | Skill Name | Authority Source |
|---|---|---|
| SKL-PMO-01 | Define PMO Charter and Mandate | PMO Practice Guide §3 |
| SKL-PMO-02 | Configure PMO Service Model | PMO Practice Guide §4 |
| SKL-PMO-03 | Establish Portfolio Intake and Governance | Standard for Portfolio Management §5 |
| SKL-PMO-04 | Define PM Methodology and Templates | OPM Standard §4 |
| SKL-PMO-05 | Manage PMO Maturity Assessment | OPM Standard §5 |
| SKL-PMO-06 | Run PMO Portfolio Review | Governance Practice Guide §5 |

**Prerequisite:** `reference/appendices/X2-pmo.md` must exist before these skills are written.

#### G2 — Pack AI (`skills/08-ai-procurement/`)

| Skill ID | Skill Name | Authority Source |
|---|---|---|
| SKL-AI-01 | Assess AI Readiness for Project Work | Leading AI Transformation §3 |
| SKL-AI-02 | Govern AI Use in Project Delivery | Guide to Leading AI Projects §4 |
| SKL-AI-03 | Evaluate AI Tools for PMO | Guide to Leading AI Projects §5 |
| SKL-AI-04 | Manage AI-Enhanced Procurement | PMBOK8 §2.8 + AI guide |

**Prerequisite:** `reference/appendices/X3-ai.md` must exist before these skills are written.

---

### Phase H — MCP Server Design and Build
**Priority:** 🟡 Medium · **Estimated effort:** High

The repository is designed to serve as the knowledge source for an MCP (Model Context Protocol) server. This phase defines and builds that server.

#### H1 — MCP Server Architecture Design

Create `mcp/` directory with the following design documents:

```
mcp/
├── README.md                     ← Server overview and setup guide
├── architecture.md               ← Server architecture: tools, resources, prompts
├── tool-schemas/
│   ├── index.md                  ← All tool schemas catalog
│   ├── get-skill.md              ← Tool: retrieve a skill by ID
│   ├── get-artifact.md           ← Tool: retrieve an artifact definition
│   ├── get-process.md            ← Tool: retrieve a PMBOK 8 process record
│   ├── list-skills-by-pack.md    ← Tool: list all skills in a pack
│   ├── validate-artifact.md      ← Tool: validate an artifact against its schema
│   └── route-decision.md         ← Tool: run T1–T4 routing logic
├── resource-schemas/
│   ├── index.md                  ← All resource schemas
│   ├── skill-resource.md         ← Resource: skill file content
│   ├── artifact-resource.md      ← Resource: artifact definition
│   └── reference-resource.md     ← Resource: PMBOK 8 reference content
├── prompt-contracts/
│   ├── index.md                  ← All prompt contracts
│   ├── execute-skill.md          ← Prompt: execute a skill with inputs
│   ├── generate-artifact.md      ← Prompt: generate a filled artifact from inputs
│   └── plan-phase.md             ← Prompt: plan a project phase
└── endpoints.md                  ← API endpoint catalog with auth and error handling
```

#### H2 — Tool Schema Specification

Each tool schema must include:
- Tool name and description
- Input schema (parameters, types, required/optional)
- Output schema
- Example request
- Example response
- Error cases
- Authentication requirements

#### H3 — Server Implementation Notes

- Language: Python (preferred) or Node.js
- Transport: stdio (local) and HTTP/SSE (remote)
- Authentication: API key per deployment
- Rate limiting: per-tool configurable
- Logging: structured JSON logs per request
- Repository content served as read-only resources

---

### Phase I — AI Agent Design
**Priority:** 🔵 Medium-Low · **Estimated effort:** High

Design AI agents grounded in the PMBOK 8 skill and artifact layer.

#### I1 — Agent Architecture Documents

Create `agents/` directory:

```
agents/
├── README.md                     ← Agent overview and design principles
├── PM-AGENT-01-project-planner.md ← Full agent definition
├── PM-AGENT-02-risk-manager.md
├── PM-AGENT-03-change-controller.md
├── PM-AGENT-04-stakeholder-manager.md
├── PM-AGENT-05-pmo-advisor.md
└── shared/
    ├── agent-schema-template.md  ← Template for defining any agent
    └── safety-rules.md           ← Common safety and escalation rules
```

#### I2 — Agent Definition Schema

Each agent definition must include:
- Role definition
- Operating instructions
- Tool policy (which MCP tools it can call)
- Memory policy (what it retains across sessions)
- Workflow (step-by-step operating procedure)
- Safety rules (what it must never do)
- Escalation logic (when to defer to human)
- Evaluation criteria (how to assess quality)
- Sample prompts (3–5 example interactions)
- Skill cross-references (which skills it executes or assists with)

---

### Phase J — Book Authoring Track
**Priority:** 🔵 Medium-Low · **Estimated effort:** Very High

The repository content is designed to support a book on PMBOK 8 project management. This phase organizes that authoring work.

#### J1 — Book Structure and Outline

Create `book/` directory:

```
book/
├── README.md                     ← Book overview, target audience, structure
├── OUTLINE.md                    ← Full chapter outline
├── STYLE-GUIDE.md                ← Writing style, terminology rules, citation format
├── chapters/
│   ├── 00-introduction.md
│   ├── 01-pmbok8-overview.md
│   ├── 02-principles.md
│   ├── 03-performance-domains.md
│   ├── 04-lifecycle-and-tailoring.md
│   ├── 05-initiating.md
│   ├── 06-planning.md
│   ├── 07-executing.md
│   ├── 08-monitoring-controlling.md
│   ├── 09-closing.md
│   ├── 10-adaptive-hybrid.md
│   ├── 11-pmo.md
│   ├── 12-ai-in-projects.md
│   └── 13-artifacts-reference.md
└── editorial/
    ├── review-notes.md
    └── revision-log.md
```

#### J2 — Authoring Rules

- Every chapter statement must cite a PMBOK 8 section or companion reference
- No paraphrasing of PMI copyrighted content — synthesize and interpret
- Use artifact examples from `artifacts/*/example.md` as chapter figures
- Every chapter must have a practical case study section
- Terminology must match `reference/GLOSSARY.md` at all times

---

### Phase K — Quality, CI/CD, and Release Track
**Priority:** 🟡 Ongoing · **Estimated effort:** Medium

#### K1 — Quality Standards for All Skills

Every skill file must pass:
- [ ] YAML front matter: valid, complete, `skill_id` matches filename prefix
- [ ] `pmbok8_anchor` cites a real PMBOK 8 section or figure
- [ ] `primary_artifact` matches canonical A-code from Artifacts-V-1.0.5
- [ ] All upstream/downstream skill IDs exist in SKILL-REGISTRY.md
- [ ] Steps are numbered and action-oriented
- [ ] Tests table has minimum 7 entries with Pass/Fail conditions
- [ ] No unresolved `[TBD]` or `[placeholder]` text
- [ ] `source_type` is one of: `PMI-derived`, `synthesis`, `organization-defined`

#### K2 — CHANGELOG.md

Create `CHANGELOG.md` at root following [Keep a Changelog](https://keepachangelog.com) format:

```
## [Unreleased]
## [1.3.0] — 2026-05-30
### Added
- Community standards: CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, issue templates, PR template
- Artifact definitions: A02, A03, A06, A07, A08, A12, A14–A19, A21, A26–A28, A31
- Reference layer seeds: reference/, shared/, tests/ README files
- Principles index: reference/principles/index.md
...
```

#### K3 — GitHub Actions CI Validation

Create `.github/workflows/` with:
- `validate-skill-frontmatter.yml` — checks YAML front matter in all skill files
- `check-broken-links.yml` — validates internal cross-references
- `lint-markdown.yml` — enforces markdown formatting standards
- `registry-sync-check.yml` — verifies SKILL-REGISTRY.md is consistent with actual skill files

#### K4 — Versioning and Release Policy

| Version increment | Trigger |
|---|---|
| Patch (x.x.N) | Bug fix, typo, reference correction |
| Minor (x.N.0) | New skill(s), new artifact definition(s), new reference file(s) |
| Major (N.0.0) | New pack, structural reorganization, breaking change to schema |

Current version: **1.3.0**
Next milestone: **1.4.0** — Pack 05 complete + Pack 06 complete
Target release: **2.0.0** — All core packs (00–07) + artifact definitions complete

#### K5 — SKILL-REGISTRY.md Updates Required

After Phase A repairs:
1. Update Pack 04 status from `Planned` → `Draft · Untested`
2. Add Pack 05–07 rows with correct IDs and artifact references
3. Reconcile SKL-05-01 numbering after rename
4. Bump version to `1.4.0-draft`

#### K6 — README.md Updates Required

After Phase B (skills complete):
- Update skill count in coverage table
- Update version history
- Bump to `1.4.0-draft` → `2.0.0` at milestone

---

## 5. Execution Scorecard

| Phase | Deliverable | Effort | Priority | Status |
|---|---|---|---|---|
| A | Repair + Stabilize (naming, quality, branch protection, CHANGELOG) | Low | 🔴 Immediate | ❌ Not done |
| B1 | Pack 05 — M&C (8 skills) | High | 🔴 High | ❌ Not done |
| B2 | Pack 06 — Closing (3 skills) | Medium | 🔴 High | ❌ Not done |
| B3 | Pack 07 — Adaptive (4 skills) | Medium | 🟠 High | ❌ Not done |
| B4 | Pack 01 — Pre-Sign (3 skills confirm/create) | Low | 🟠 High | ❓ Unknown |
| C1 | Missing artifact definitions (A01, A04, A05, A09–A13, A20, A22–A25, A29–A32) | High | 🟠 High | ❌ Not done |
| C2 | Artifact templates (all 41) | Very High | 🟠 High | ❌ Not done |
| C3 | Artifact examples (top 10) | Medium | 🟡 Medium | ❌ Not done |
| D1–D3 | Reference: principles, domains, focus areas | High | 🟠 Medium-High | 🟡 Index only |
| D4–D5 | Reference: 40 processes + I/O + T&T registries | Very High | 🟡 Medium | ❌ Not done |
| D6 | Reference: appendices (X2–X5) | Medium | 🟡 Medium | ❌ Not done |
| D7 | Reference: GLOSSARY.md (PMI Lexicon) | Medium | 🟡 Medium | ❌ Not done |
| E1–E4 | Shared: routing, validators, checklists, components | Medium | 🟡 Medium | 🟡 Seeded |
| F1–F2 | Tests: 423 skill tests + 7 integration tests | Very High | 🟡 Medium | 🟡 Seeded |
| G1 | Pack PMO (6 skills) | Medium | 🔵 Lower | ❌ Not done |
| G2 | Pack AI (4 skills) | Medium | 🔵 Lower | ❌ Not done |
| H | MCP Server design + schemas | High | 🟡 Medium | ❌ Not done |
| I | AI Agent definitions (5 agents) | High | 🔵 Medium-Low | ❌ Not done |
| J | Book authoring track | Very High | 🔵 Medium-Low | ❌ Not done |
| K | QA sweep + CI/CD + CHANGELOG + registry + README | Ongoing | 🟡 Ongoing | 🟡 Partial |

---

## 6. Recommended Session Order

For maximum progress in future sessions, tackle in this order:

1. **Session next:** Phase A repairs (naming collision fix, SKL-05-01 rename, CHANGELOG.md)
2. **Session +1:** Phase B1 — Pack 05 skills (SKL-05-01 through 05-09)
3. **Session +2:** Phase B2+B3 — Pack 06 and Pack 07 skills
4. **Session +3:** Phase C1 — Missing artifact definitions (A01, A04, A05 first)
5. **Session +4:** Phase C2 — Artifact templates (priority 17 first)
6. **Session +5:** Phase D1–D3 — Principles, Domains, Focus Areas reference files
7. **Session +6:** Phase D4–D5 — Process records (batch in groups of 10)
8. **Session +7:** Phase H — MCP server design documents
9. **Session +8:** Phase E + F — Shared validators and test cases
10. **Sessions beyond:** Phase G (extended packs), Phase I (agents), Phase J (book)

---

## 7. Version History of This Plan

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan — 7 phases · focused on skills + artifacts + reference layers |
| 2.0.0 | 2026-05-30 | Full rebuild: added MCP server track (Phase H), AI agent track (Phase I), book authoring track (Phase J), CI/CD track (Phase K), community standards (now done), CHANGELOG, GLOSSARY, branch protection, extended packs G1/G2, artifact templates + examples explicit plan, lexicon/glossary explicit item, reconciled with live repo state |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-30 · Version 2.0.0*

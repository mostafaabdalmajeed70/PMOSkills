# PMOSkills — Quality Standards and Enforcement Rules
**Version:** 1.0.0  
**Date:** 2026-06-01  
**Repository:** https://github.com/fakhruldeen/PMOSkills  
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary  
**Status:** Active · Enforced from v4.4.0 of MASTER-PLAN  
**Applies to:** Every file in this repository — past, present, and future

> This document is the single authoritative source for quality standards, structural requirements, file naming rules, and quality gate enforcement for the PMOSkills repository. All other documents that reference quality standards defer to this file. When this document conflicts with `COMPLETION-PLAN-V4.md §2`, this document takes precedence.

---

## Table of Contents

1. [File Type Registry](#1-file-type-registry)
2. [YAML Front-Matter Schemas](#2-yaml-front-matter-schemas)
3. [File Structure Standards](#3-file-structure-standards)
4. [File Naming Conventions](#4-file-naming-conventions)
5. [Directory Structure Rules](#5-directory-structure-rules)
6. [Source Traceability Rules](#6-source-traceability-rules)
7. [Quality Gate Checklists](#7-quality-gate-checklists)
8. [Enforcement and Failure Protocol](#8-enforcement-and-failure-protocol)
9. [AI Agent Pre-Commit Checklist](#9-ai-agent-pre-commit-checklist)
10. [Version History](#10-version-history)

---

## 1. File Type Registry

Every file in this repository belongs to exactly one of the following canonical types. File type determines: YAML schema, section structure, naming pattern, and quality gate.

| Type Code | File Type | Location Pattern | Naming Pattern |
|---|---|---|---|
| `SKL` | Skill file | `skills/NN-pack-name/` | `SKL-NN-NN-kebab-name.md` |
| `ART-DEF` | Artifact definition | `artifacts/category-name/` | `ANN-kebab-name.md` |
| `ART-TPL` | Artifact template | `artifacts/category-name/` | `ANN-kebab-name-template.md` |
| `ART-EX` | Artifact example | `artifacts/category-name/` | `ANN-kebab-name-example.md` |
| `REF` | Reference file | `reference/subdirectory/` | `XXnn-kebab-name.md` |
| `DOC` | Documentation file | `docs/` | `kebab-name.md` |
| `SHR` | Shared component | `shared/subdirectory/` | `kebab-name.md` |
| `TST` | Test file | `tests/subdirectory/` | `ST-SKL-NN-NN.md` or `IT-NN.md` |
| `GOV` | Governance/root file | root `/` | `UPPER-KEBAB.md` |

---

## 2. YAML Front-Matter Schemas

Every file **must** begin with a YAML front-matter block. Fields marked `required` cause a quality gate failure if absent. Fields marked `if-applicable` must be present when the condition is met.

### 2.1 Skill File (`SKL`) — Required YAML

Derived from live file `skills/01-organizational-setup/SKL-01-01-establish-pm-governance-framework.md`.

```yaml
---
skill_id: SKL-NN-NN                          # required · format: SKL-[pack_num]-[seq_num]
skill_name: [Full Skill Name]                # required · title case · no abbreviations
pack: "NN — Pack Name"                       # required · matches directory name
version: "1.0.0"                            # required · semver
status: "Draft · Untested"                  # required · see status vocabulary §2.6
source_type: PMI-derived                     # required · PMI-derived | PMI-adapted | org-defined
primary_artifact_output: "ANN — Artifact Name"  # required · one primary output only
artifacts_updated:                           # required · list all artifacts written/updated
  - "ANN — Artifact Name (section note)"
artifacts_consumed:                          # if-applicable · list all artifacts read as inputs
  - "ANN — Artifact Name"
pmbok8_process_anchor: "[PMBOK8 section reference]"  # required · §X.X or principle name
performance_domains:                         # required · one or more from canonical list
  - Governance
focus_area: [Phase Name]                     # required · see focus area vocabulary §2.7
upstream_prerequisites:                      # required · what must exist before this skill runs
  - "ANN — Artifact name must exist"
downstream_skills:                           # if-applicable · skills unlocked by this skill
  - "SKL-NN-NN — Skill Name"
file_path: "skills/NN-pack-name/SKL-NN-NN-kebab-name.md"  # required · exact repo path
tests: 9                                     # required · count of test cases in ## Tests section
---
```

**Canonical `status` vocabulary:**
- `Draft · Untested` — stub or initial build, no test cases verified
- `Draft · In Review` — content complete, under peer or PMO review
- `Active · Tested` — all test cases pass, approved for use
- `Deprecated` — superseded; do not use for new work

**Canonical `performance_domains` vocabulary (PMBOK 8 Guide):**
Governance · Scope · Schedule · Finance · Stakeholders · Resources · Risk · Delivery

**Canonical `focus_area` vocabulary:**
Organizational Setup · Initiating · Planning · Executing · Monitoring and Controlling · Closing · Adaptive and Hybrid · PMO Operations · Portfolio and Program Management

---

### 2.2 Artifact Definition File (`ART-DEF`) — Required YAML

Derived from live files `A06-project-management-plan.md`, `A08-scope-requirements-backlog.md`.

```yaml
---
artifact_id: ANN                             # required · format: A[two-digit-num]
artifact_name: [Full Artifact Name]          # required · title case
version: "1.0.0"                            # required · semver
status: Active                               # required · Active | Draft | Deprecated
authority: "PMBOK8 Guide §X.X.X"            # required · specific section, not just chapter
pmbok8_process_group: [Process Group Name]   # required · Initiating|Planning|Executing|M&C|Closing
performance_domains:                          # required
  - [Domain Name]
produced_by_skills:                          # required · list of SKL IDs
  - SKL-NN-NN
consumed_by_skills:                          # if-applicable
  - SKL-NN-NN
related_artifacts:                           # if-applicable
  - ANN
has_template: true                           # required · true|false
has_example: true                            # required · true|false
file_path: "artifacts/category-name/ANN-kebab-name.md"  # required
---
```

---

### 2.3 Artifact Template File (`ART-TPL`) — Required YAML

```yaml
---
template_for: ANN                            # required · parent artifact ID
artifact_name: [Full Artifact Name]          # required · must match parent definition
version: "1.0.0"                            # required · must match parent definition version
status: Active                               # required
file_path: "artifacts/category-name/ANN-kebab-name-template.md"  # required
parent_definition: "artifacts/category-name/ANN-kebab-name.md"   # required · relative path
---
```

**Template rule:** Every `[FIELD: description]` placeholder must remain as-is. Pre-filling a template placeholder with sample data is a critical quality failure.

---

### 2.4 Artifact Example File (`ART-EX`) — Required YAML

```yaml
---
example_for: ANN                             # required · parent artifact ID
artifact_name: [Full Artifact Name]          # required
version: "1.0.0"                            # required
scenario: "Meridian CRM System Upgrade"     # required · all examples use Meridian scenario
status: Active                               # required
file_path: "artifacts/category-name/ANN-kebab-name-example.md"  # required
parent_definition: "artifacts/category-name/ANN-kebab-name.md"  # required
parent_template: "artifacts/category-name/ANN-kebab-name-template.md"  # required
---
```

**Example scenario lock:** All artifact examples in this repository use the **Meridian CRM System Upgrade** scenario for cross-artifact consistency. No other scenario may be used without a governance decision logged in CHANGELOG.md.

---

### 2.5 Reference File (`REF`) — Required YAML

Applies to all files under `reference/principles/`, `reference/performance-domains/`, `reference/focus-areas/`, `reference/processes/`, and all new reference subdirectories.

```yaml
---
ref_id: XXnn                                 # required · e.g. P01, PD02, FA03, PR11
ref_type: Principle|PerformanceDomain|FocusArea|Process|KnowledgeArea|Tool|IO|Appendix|Glossary|CompanionRef|Tailoring|PMO
ref_name: [Full Reference Name]              # required · title case
version: "1.0.0"                            # required
status: Active                               # required
pmbok8_source: "PMBOK8 Guide §X.X.X"        # required · specific section
companion_ref_shortcode: [code]             # if-applicable · e.g. WBS-3E, PSS-3E, PMO-PG
related_skills:                              # if-applicable
  - SKL-NN-NN
related_artifacts:                           # if-applicable
  - ANN
file_path: "reference/subdir/XXnn-kebab-name.md"  # required
---
```

---

### 2.6 Documentation File (`DOC`) — Required YAML

```yaml
---
doc_id: DOC-NN                               # required · sequential
doc_name: [Full Document Name]               # required
version: "1.0.0"                            # required
status: Active                               # required
audience:                                    # required · one or more
  - Project Manager
  - PMO Director
  - AI Agent
file_path: "docs/kebab-name.md"             # required
---
```

---

### 2.7 Test File (`TST`) — Required YAML

```yaml
---
test_id: ST-SKL-NN-NN                        # required · format: ST-[parent-skill-id]
test_type: SkillTest|IntegrationTest         # required
target: SKL-NN-NN                            # required · skill or flow under test
version: "1.0.0"                            # required
status: Active                               # required
test_case_count: 9                           # required · must match actual cases in file
file_path: "tests/skill-tests/ST-SKL-NN-NN.md"  # required
---
```

---

## 3. File Structure Standards

### 3.1 Skill File Structure (`SKL`)

Every full skill file must contain exactly these sections in this order. No section may be omitted. No section may be renamed.

```
[YAML front-matter]                    ← required · per §2.1

# SKL-NN-NN — [Skill Name]            ← H1 heading · exact format

**Skill ID:** SKL-NN-NN               ← metadata block (5 lines, bold labels)
**Pack:** NN — Pack Name
**Status:** [status]
**Source type:** PMI-derived
**PMBOK8 anchor:** [section ref]
**File path:** `skills/...`

---

## Purpose                             ← §3.1.1 · 1–3 sentences · no bullet lists

## Scope                               ← §3.1.2 · what this skill covers AND does not cover

## Inputs Required                     ← §3.1.3 · table: Input | Source | Mandatory?
                                         + Gate check: what must exist before running

## Instructions                        ← §3.1.4 · H3 steps · numbered sub-steps
### Step 1 — [Name]
### Step 2 — [Name]
...

## Outputs                             ← §3.1.5 · table: Output | Artifact | Section | Notes

## Constraints                         ← §3.1.6 · bullet list of hard rules and limits

## Tailoring Guidance                  ← §3.1.7 · table: Approach | Adjustment
                                         Rows: Simple | Large/multi-phase | Program | Regulated | Adaptive | Hybrid

## Failure Cases                       ← §3.1.8 · table: Failure | Symptom | Resolution

## Tests                               ← §3.1.9 · table: Test ID | Description | Pass | Fail
                                         Minimum 9 test cases per skill

## Change Log                          ← §3.1.10 · table: Version | Date | Change description

---

*Authority: [PMBOK8 ref]*             ← footer block (4 italic lines)
*Source type: PMI-derived*
*Owner: [role]*
*Approval authority: [role]*
```

**Minimum test case count:** 9 per skill file (matching `tests:` YAML field).

---

### 3.2 Artifact Definition File Structure (`ART-DEF`)

```
[YAML front-matter]                    ← required · per §2.2

# ANN — [Artifact Name]               ← H1 heading

**Artifact ID:** ANN                  ← metadata block (bold labels)
**Version:** 1.0.0
**Status:** Active
**Authority:** PMBOK8 Guide §X.X.X
**Process Group:** [name]

---

## Purpose                             ← what problem this artifact solves; 2–4 sentences

## When to Create                      ← trigger condition; lifecycle phase; who initiates

## Inputs                              ← table: Input | Source | Mandatory?

## Content Requirements                ← table or nested list of required fields/sections
                                         each field: Field Name | Description | Format

## Outputs / Downstream Use            ← which skills or processes consume this artifact

## Quality Criteria                    ← table: Criterion | Standard | Failure Indicator
                                         minimum 5 criteria

## Waste Test                          ← 5 binary yes/no questions; all must be YES to pass

## Related Artifacts                   ← table: Artifact ID | Name | Relationship

## Authority and Governance            ← who creates, approves, and baselines this artifact

## Change Log                          ← table: Version | Date | Change description

---

*Authority: PMBOK8 Guide §X.X.X*
*Owner: [role]*
```

---

### 3.3 Artifact Template File Structure (`ART-TPL`)

```
[YAML front-matter]                    ← required · per §2.3

# ANN — [Artifact Name] — Template

> **Usage note:** [1–2 sentences on how to fill this template]
> **Parent definition:** [link to ANN definition file]
> **Version:** must match parent definition version

---

[Template sections matching Content Requirements in parent ART-DEF]

Each field uses this format:
  **[FIELD: Field Name]** — [description of what to enter]

OR table rows with:
  | [FIELD: field name] | [FIELD: description] | [FIELD: format] |

---

*Template for: ANN — [Artifact Name]*
*Do not pre-fill. Remove this note when completing.*
```

**Enforcement:** No `[FIELD: ...]` placeholder may contain actual data. This is a critical failure.

---

### 3.4 Artifact Example File Structure (`ART-EX`)

```
[YAML front-matter]                    ← required · per §2.4

# ANN — [Artifact Name] — Example
## Scenario: Meridian CRM System Upgrade

> **Note:** This is a worked example. All data is fictional and for illustration only.
> **Parent definition:** [link to ANN definition file]
> **Parent template:** [link to ANN template file]

---

[Completed fields following the template structure]
[All [FIELD: ...] placeholders replaced with Meridian scenario data]

---

## Reviewer Notes                      ← what this example demonstrates; quality callouts

---

*Example for: ANN — [Artifact Name] · Scenario: Meridian CRM System Upgrade*
```

---

### 3.5 Reference File Structure (`REF`)

Applies to all files under `reference/` regardless of subdirectory.

```
[YAML front-matter]                    ← required · per §2.5

# [Ref ID] — [Reference Name]         ← H1 heading

**Ref ID:** XXnn                      ← metadata block
**Type:** [ref_type]
**PMBOK8 Source:** §X.X.X
**Version:** 1.0.0

---

## Definition                          ← PMI definition, cited with section number

## Key Characteristics                 ← bullet list: 4–8 characteristics

## PMBOK 8 Context                     ← how this element functions within PMBOK 8 structure

## Inputs                              ← table: what feeds into this element (if applicable)

## Outputs                             ← table: what this element produces (if applicable)

## Tools and Techniques                ← table or list (if applicable)

## Cross-References                    ← table: Related Item | Type | Relationship

## Practitioner Notes                  ← 3–5 questions a practitioner should ask when using this

## Change Log                          ← table: Version | Date | Change

---

*Authority: PMBOK8 Guide §X.X.X*
```

---

### 3.6 Documentation File Structure (`DOC`)

```
[YAML front-matter]                    ← required · per §2.6

# [Document Name]

**Version:** 1.0.0  
**Audience:** [audience list]  
**Status:** Active

---

## Purpose                             ← what this document helps the reader do

## Audience                            ← who should read this and why

## Prerequisites                       ← what the reader must know or have before reading

[Main content sections — H2/H3 headings as needed]

## Related Files                       ← table: File | Description | When to use

## Change Log                          ← table: Version | Date | Change
```

---

### 3.7 Test File Structure (`TST`)

```
[YAML front-matter]                    ← required · per §2.7

# ST-SKL-NN-NN — [Skill Name] — Test Cases

**Target skill:** SKL-NN-NN  
**Test count:** 9  
**Version:** 1.0.0

---

## Test Environment
[Pre-conditions that must be true for all tests in this file]

## Test Cases

### TC-01 — [Test Case Name]
**Scenario:** [description]  
**Input:** [what is provided]  
**Expected output:** [what must result]  
**Pass condition:** [measurable criteria]  
**Fail condition:** [measurable criteria]  
**Authority check:** [PMBOK8 or source ref]

[Repeat for TC-02 through TC-09 minimum]

## Integration Notes
[How this skill connects to upstream/downstream in the lifecycle]

## Change Log
```

---

## 4. File Naming Conventions

### 4.1 Universal Rules

- All filenames use **lowercase kebab-case**: `kebab-case-words.md`
- **No spaces**, no underscores, no camelCase in filenames
- **Exceptions:** Root governance files use `UPPER-KEBAB.md` (e.g., `MASTER-PLAN.md`, `SKILL-REGISTRY.md`)
- All content files use `.md` extension
- Machine-readable manifests use `.json` or `.yaml`
- Data files use `.csv`
- Maximum filename length: **80 characters** (including extension)

### 4.2 Skill Files

**Pattern:** `SKL-{pack_num}-{seq_num}-{kebab-name}.md`

```
SKL-01-01-establish-pm-governance-framework.md    ✅
SKL-03-07-develop-risk-register.md               ✅
SKL-08-01-establish-pmo-charter-and-mandate.md   ✅
skl-01-01.md                                      ❌ missing name
SKL_01_01_governance.md                          ❌ underscores
SKL-1-1-governance.md                            ❌ missing leading zeros
```

- Pack number: 2-digit zero-padded (`01`, `02`, ... `09`)
- Sequence number: 2-digit zero-padded (`01`, `02`, ... `17`)
- Name: full descriptive kebab slug (minimum 3 words)

### 4.3 Artifact Files

**Definition:** `A{nn}-{kebab-name}.md`  
**Template:** `A{nn}-{kebab-name}-template.md`  
**Example:** `A{nn}-{kebab-name}-example.md`

```
A06-project-management-plan.md                    ✅ definition
A06-project-management-plan-template.md          ✅ template
A06-project-management-plan-example.md           ✅ example
A14-Integrated-Project-Management-Plan.md        ⚠️ capital letters — non-conformant (legacy)
A14-integrated-project-management-plan.md        ✅ correct form
```

- Artifact number: 2-digit zero-padded (`A01` through `A41`)
- Every artifact **must** have all three files (definition + template + example) to be fully complete
- Partial delivery (definition only, or definition + template only) is acceptable during build phases but must be flagged in scorecard

**Legacy non-conformance:** Files `A14-Integrated-Project-Management-Plan.md` and `A15-Schedule-Model-and-Baseline-Record.md` and `A16-Financial-Management-and-Cost-Baseline-Record.md` use title case — these are non-conformant and must be renamed in Phase 7 quality audit.

### 4.4 Reference Files

| Subdir | ID Pattern | Example |
|---|---|---|
| `principles/` | `P{nn}-{kebab}.md` | `P01-be-a-diligent-steward.md` |
| `performance-domains/` | `PD{nn}-{kebab}.md` | `PD01-governance.md` |
| `focus-areas/` | `FA{nn}-{kebab}.md` | `FA01-project-integration.md` |
| `processes/` | `PR{nn}-{kebab}.md` | `PR11-develop-project-charter.md` |
| `knowledge-areas/` | `KA{nn}-{kebab}.md` | `KA01-integration-management.md` |
| `tools-techniques/` | `TT{nn}-{kebab}.md` | `TT01-expert-judgment.md` |
| `inputs-outputs/` | `IO{nn}-{kebab}.md` | `IO01-inputs-outputs-registry.md` |
| `appendices/` | `X{n}-{kebab}.md` | `X2-pmo.md` |
| `companion-references/` | `CR{nn}-{kebab}.md` | `CR01-pmo-practice-guide.md` |
| `tailoring/` | `TLR-{kebab}.md` | `TLR-governance.md` |
| `pmo/` | `PMO-{kebab}.md` | `PMO-types.md` |

### 4.5 Test Files

**Skill test:** `ST-SKL-{pack}-{seq}.md` → `ST-SKL-01-01.md`  
**Integration test:** `IT-{nn}.md` → `IT-01.md`  
**Index files:** `index.md` in every directory that contains 3+ files

### 4.6 Shared Files

**Validators:** `shared/validators/{kebab-name}.md`  
**Checklists:** `shared/checklists/{kebab-name}.md`  
**Components:** `shared/components/{kebab-name}.md`  
**Routing:** `shared/routing/{kebab-name}.md`

### 4.7 Root Governance Files

Root-level governance and plan files use `SCREAMING-KEBAB.md` (all caps, hyphens):

```
MASTER-PLAN.md          ✅
SKILL-REGISTRY.md       ✅
AUTHORITY-ROUTING.md    ✅
LIFECYCLE-MAP.md        ✅
QUALITY-STANDARDS.md    ✅
README.md               ✅
CHANGELOG.md            ✅
```

---

## 5. Directory Structure Rules

### 5.1 Canonical Directory Tree

The following is the **only** permitted directory structure. No directory may be created outside this tree without a governance decision recorded in CHANGELOG.md and MASTER-PLAN.md.

```
PMOSkills/
│
├── [Root governance files — UPPER-KEBAB.md]     ← no subdirectories except listed below
│
├── .github/                                     ← issue + PR templates only
│   └── [templates]
│
├── docs/                                        ← documentation files only
│   ├── img/                                     ← images only (.jpg, .png, .svg)
│   ├── legacy/                                  ← archived superseded files only
│   └── [DOC files: kebab-name.md]
│
├── artifacts/                                   ← artifact triplets (DEF + TPL + EX)
│   ├── closing/
│   ├── communications/                          ← pending audit (P0-R2)
│   ├── extended-procurement/                    ← pending audit (P0-R3)
│   ├── extended-resources/                      ← pending audit (P0-R4)
│   ├── governance/                              ← pending audit (P0-R5)
│   ├── initiating/                              ← pending audit (P0-R6)
│   ├── knowledge/                              ← pending audit (P0-R7)
│   ├── monitoring-and-decisions/
│   ├── planning-and-baselines/
│   ├── pmo/                                     ← pending audit (P0-R8)
│   ├── portfolio/                               ← pending audit (P0-R9)
│   ├── procurement/
│   ├── quality/                                 ← pending audit (P0-R10)
│   ├── resources/
│   ├── stakeholders/
│   └── stakeholders-communications/             ← pending audit (P0-R11)
│       [Note: closure/, team-resources/ pending consolidation decision]
│
├── skills/                                      ← skill files only
│   ├── 01-organizational-setup/
│   ├── 02-initiating/
│   ├── 03-planning/
│   ├── 04-executing/
│   ├── 05-monitoring-controlling/
│   ├── 06-closing/
│   ├── 07-adaptive-hybrid/
│   ├── 08-pmo-operations/                       ← Phase 3-EXT · Pack 08
│   └── 09-portfolio-program-management/         ← Phase 3-EXT · Pack 09
│
├── reference/
│   ├── README.md
│   ├── GLOSSARY.md                              ← Phase 4-C9
│   ├── principles/                              ← ✅ complete
│   ├── performance-domains/                     ← ✅ complete
│   ├── focus-areas/                             ← ✅ complete
│   ├── processes/                               ← partial: PR01–PR10 needed
│   ├── knowledge-areas/                         ← pending Phase 0 migration from C5
│   ├── tools-techniques/                        ← pending Phase 0 migration from C6
│   ├── inputs-outputs/                          ← pending Phase 0 migration from C7
│   ├── appendices/                              ← Phase 4-C8
│   ├── companion-references/                    ← Phase 4-C10 (NEW)
│   ├── tailoring/                               ← Phase 4-C11 (NEW)
│   └── pmo/                                     ← Phase 4-C12 (NEW)
│
├── shared/
│   ├── README.md
│   ├── validators/
│   ├── checklists/
│   ├── components/
│   └── routing/
│
└── tests/
    ├── README.md
    ├── skill-tests/
    └── integration-tests/
```

### 5.2 Directory Rules

1. **No files at root level except the canonical root governance files** listed in §4.7. Any other file at root is a structural violation.
2. **No new top-level directories** may be created. `C4-Process-Records/`, `C5-KA-Crossref/`, `C6-TT-Taxonomy/`, `C7-IO-Registry/`, and `repo/` are structural violations awaiting Phase 0 cleanup.
3. **Every directory with 3+ files must have an `index.md`** that lists all files, their status, and their purpose.
4. **No file may exist in a parent directory** if it belongs in a subdirectory. (e.g., a skill file cannot be placed in `skills/` directly — it must be in the correct pack subdirectory.)
5. **Directory names use lowercase kebab-case** with numeric prefix for ordered packs: `01-organizational-setup/`, `03-planning/`.
6. **The `docs/legacy/` subdirectory** is the only permitted archive location for superseded files. Files in legacy/ are never referenced by active content.

### 5.3 Index File Requirements

Every directory with 3+ content files must contain `index.md` with:

```markdown
# [Directory Name] — Index
**Directory:** `path/to/dir/`
**Status:** Active | In Progress | Pending
**File count:** N
**Last updated:** YYYY-MM-DD

| File | ID | Name | Status | Phase |
|---|---|---|---|---|
| filename.md | ID | Name | Draft/Active | Phase N |
```

---

## 6. Source Traceability Rules

### 6.1 Citation Format

Every substantive claim in every file must be traceable to a source. Use this format at the end of the relevant sentence or section:

```
*Authority: [Source] — [§Section or Chapter or Page]*
```

**Source short-codes (from `pmi_reference_list.md`):**

| Short-code | Source |
|---|---|
| `PMBOK8-G` | PMBOK 8th Edition Guide |
| `PMBOK8-S` | The Standard for Project Management (within PMBOK 8) |
| `PMO-PG` | Project Management Offices: A Practice Guide |
| `PROG-5E` | The Standard for Program Management, 5th Ed. |
| `PORT-4E` | The Standard for Portfolio Management, 4th Ed. |
| `PROC-PG` | Process Groups: A Practice Guide |
| `WBS-3E` | Practice Standard for Work Breakdown Structures, 3rd Ed. |
| `SCH-3E` | Practice Standard for Scheduling, 3rd Ed. |
| `RISK-PG` | Risk Management in Portfolios, Programs, and Projects |
| `REQ-PG` | Requirements Management: A Practice Guide |
| `BA-PG` | PMI Guide to Business Analysis |
| `EVM-PG` | Earned Value Management Practice Standard |
| `GOV-PG` | Governance of Portfolios, Programs and Projects |
| `CHG-PG` | Managing Change in Organizations: A Practice Guide |
| `CMPLX-PG` | Navigating Complexity: A Practice Guide |
| `AI-PG` | Guide to Leading and Managing AI Projects |
| `AI-ORG` | Leading AI Transformation |
| `DAD-2E` | Introduction to Disciplined Agile Delivery, 2nd Ed. |
| `OPM-STD` | The Standard for Organizational Project Management |
| `OPM-IMP` | Implementing Organizational Project Management |
| `FORMS-3E` | Project Manager's Book of Forms, 3rd Ed. |
| `LEXICON` | PMI Lexicon of Project Management Terms v4.0 |
| `OPM-RISK` | Risk Management in Portfolios, Programs, and Projects |

### 6.2 What Must Be Cited

- Every definition or term from PMI sources
- Every process, input, output, tool, or technique referenced
- Every performance domain or principle referenced
- Every prescriptive statement ("must", "shall", "required")
- Every claim about what PMBOK 8 recommends or requires

### 6.3 What Must NOT Be Done

- **Never copy verbatim text** from PMI copyrighted materials
- **Never cite without a section number** — `*Authority: PMBOK8-G*` alone is not valid
- **Never use** "per PMI" or "according to PMBOK" without a specific section reference
- **Never use** vague source labels like "best practice" or "industry standard" without a named source

---

## 7. Quality Gate Checklists

### 7.1 Pre-Commit Checklist (every file, every commit)

```
[ ] YAML front-matter present and all required fields populated
[ ] File type matches YAML schema (§2)
[ ] File structure matches type structure (§3)
[ ] Filename matches naming convention (§4)
[ ] File is in the correct directory (§5)
[ ] Every substantive claim cites a source with section number (§6)
[ ] No verbatim PMI text reproduced
[ ] No [FIELD: ...] placeholders pre-filled in template files
[ ] All artifact cross-references (ANN IDs) resolve to existing files
[ ] All skill cross-references (SKL-NN-NN IDs) resolve to existing files
[ ] version field is semver and matches YAML + metadata block
[ ] Commit message follows §7.5 convention
```

### 7.2 Phase Exit Gate — Phase 0 (Structural Cleanup)

```
[ ] No C4/C5/C6/C7 directories exist at root level
[ ] No repo/ directory exists at root level
[ ] reference/ contains no legacy subdirectories (C4/C5/C6/C7)
[ ] All live content from C5/C6/C7 migrated to canonical reference/ subdirs
[ ] root README.md updated to reflect clean structure
[ ] reference/README.md updated
[ ] SKILL-REGISTRY.md has no stale path references
[ ] All 11 undocumented artifacts/ subdirs audited and documented or consolidated
[ ] docs/skill-reference-map.csv promoted from repo/
```

### 7.3 Phase Exit Gate — Phase 3 (Skills)

```
[ ] All 47 skill files (Packs 01–07) fully populated (no stub sections)
[ ] Every skill has exactly the 10 sections in §3.1
[ ] Every skill has ≥ 9 test cases in ## Tests section
[ ] YAML tests: field matches actual test case count
[ ] Every primary_artifact_output resolves to an existing ART-DEF file
[ ] Every artifacts_updated entry resolves to an existing ART-DEF file
[ ] Tailoring Guidance table present with ≥ 5 approach rows
[ ] No skill references an artifact that does not exist
[ ] SKILL-REGISTRY.md updated with all 47 skills at Active status
```

### 7.4 Phase Exit Gate — Phase 3-EXT (PMO + PPM Skills, Packs 08–09)

```
[ ] All 14 skill files (Pack 08: 8 files, Pack 09: 6 files) fully populated
[ ] Pack 08 skills cite PMO Practice Guide by chapter and service number
[ ] Pack 09 skills cite PMBOK8-S §2 or PMBOK8-G with specific section
[ ] skills/08-pmo-operations/ directory exists with index.md
[ ] skills/09-portfolio-program-management/ directory exists with index.md
[ ] All referenced artifacts (A34–A36 and any new) exist in artifacts/
[ ] SKILL-REGISTRY.md updated with Pack 08 and 09 entries
```

### 7.5 Phase Exit Gate — Phase 4 (Reference Layer)

```
[ ] PR01–PR10 + PR41 built in reference/processes/ (11 files)
[ ] reference/GLOSSARY.md built (≥ 50 terms)
[ ] reference/appendices/ contains X2, X3, X4, X5
[ ] reference/companion-references/ contains index.md + 23 companion files
[ ] reference/tailoring/ contains index.md + 8 domain tailoring files
[ ] reference/pmo/ contains index.md + 5 PMO reference files
[ ] Every reference file cites a specific PMBOK8 section (not chapter alone)
[ ] reference/README.md reflects complete directory state
[ ] All migrated C5/C6/C7 content upgraded to REF file structure (§3.5)
```

### 7.6 Phase Exit Gate — Phase 5 (Shared Components)

```
[ ] All validators produce deterministic pass/fail output (not narrative only)
[ ] Waste test validator covers all 10 waste detection questions
[ ] Skill quality checklist covers all 10 sections of §3.1
[ ] Routing logic is machine-readable (table-based with explicit conditions)
[ ] shared/ README.md updated with all file listings
```

### 7.7 Phase Exit Gate — Phase 6 (Tests)

```
[ ] Every skill (47 + 14 = 61 total) has a corresponding ST- test file
[ ] Every ST- file has ≥ 9 test cases
[ ] All 6 integration tests trace artifact flow end-to-end
[ ] IT-01 covers organizational-setup → initiating flow
[ ] IT-06 covers full lifecycle (setup through close)
[ ] tests/skill-tests/index.md lists all 61 skill test files
[ ] tests/integration-tests/index.md lists all 6 integration tests
```

### 7.8 Commit Message Convention

```
type(scope): short description (max 72 chars)

Body: What changed and why. Reference any gap IDs or task IDs.
Files: [list every file added/modified/deleted]
Phase: [Phase N or Governance]
```

**Allowed types:** `feat` · `fix` · `docs` · `chore` · `refactor` · `test` · `style`  
**Allowed scopes:** `skills` · `artifacts` · `docs` · `reference` · `shared` · `tests` · `root`  

**Examples:**
```
feat(skills): add SKL-03-07 develop-risk-register full content

Body: Full 10-section skill file. 9 test cases. Tailoring table for 6 approaches.
Files: skills/03-planning/SKL-03-07-develop-risk-register.md
Phase: Phase 3
```

```
chore(root): delete C4-Process-Records/ root dir (Phase 0-B)

Body: SHA verification confirmed all 30 files are exact duplicates of reference/processes/.
Files: [30 files deleted from C4-Process-Records/]
Phase: Phase 0
```

---

## 8. Enforcement and Failure Protocol

### 8.1 Failure Severity Levels

| Level | Label | Description | Action |
|---|---|---|---|
| **L1** | Critical | Missing YAML front-matter; wrong directory; pre-filled template placeholder; verbatim PMI copy | **Block commit. Do not proceed.** Fix immediately. |
| **L2** | Major | Missing required section; citation without section number; artifact cross-ref does not resolve; test count mismatch | **Fix before phase exit gate.** Flag in CHANGELOG. |
| **L3** | Minor | Non-conformant filename (legacy); missing index.md in dir with 3+ files; status vocabulary mismatch | **Fix in Phase 7 quality audit.** Log in MASTER-PLAN. |
| **L4** | Advisory | Tailoring table has fewer than 6 rows; Failure Cases table has fewer than 5 rows; Change Log missing entry | **Note in PR/commit.** Resolve in next session. |

### 8.2 Quality Audit Schedule

| Trigger | Audit Scope | Logged In |
|---|---|---|
| After every Phase 0 operation | Migrated/deleted files + affected index.md | CHANGELOG.md |
| After every Phase 3 skill file | Pre-commit checklist §7.1 + skill gate §7.3 | Commit message |
| After completing each Pack (01–09) | Full pack review: YAML, structure, cross-refs, test counts | MASTER-PLAN §8 session log |
| After Phase 4 sub-phase (C4–C12) | Reference structure + citation check | Commit message |
| After Phase 5 completion | Validator determinism test | MASTER-PLAN §7 scorecard |
| After Phase 6 completion | Full test coverage scan | MASTER-PLAN §7 scorecard |
| Phase 7 — continuous | L3 legacy naming issues; cross-reference integrity | CHANGELOG.md v bump |

### 8.3 Non-Conformance Register

Known current non-conformances that must be resolved in Phase 7:

| NC-ID | File | Issue | Severity | Phase |
|---|---|---|---|---|
| NC-001 | `artifacts/planning-and-baselines/A14-Integrated-Project-Management-Plan.md` | Title case filename — should be `a14-integrated-project-management-plan.md` | L3 | Phase 7 |
| NC-002 | `artifacts/planning-and-baselines/A15-Schedule-Model-and-Baseline-Record.md` | Title case filename | L3 | Phase 7 |
| NC-003 | `artifacts/planning-and-baselines/A16-Financial-Management-and-Cost-Baseline-Record.md` | Title case filename | L3 | Phase 7 |
| NC-004 | All root-level stale dirs (C4–C7, repo/) | Structural violation — wrong location | L1 | Phase 0 |
| NC-005 | `reference/README.md` | Stale — does not reflect current structure | L3 | Phase 0 |
| NC-006 | Root `README.md` | References C4/C5 stale paths | L2 | Phase 0 |
| NC-007 | `artifacts/` — 11 undocumented subdirs | Undocumented directories | L2 | Phase 0 |
| NC-008 | `reference/` — missing `index.md` files in most subdirs | Missing index files | L3 | Phase 7 |

---

## 9. AI Agent Pre-Commit Checklist

Before committing **any** file, an AI agent must answer YES to every question below. A NO answer on any L1 or L2 item is a hard stop.

```
FILE IDENTITY
[ ] Does the file have a YAML front-matter block as its first content?         [L1 if NO]
[ ] Does the YAML match the schema for this file's type (§2)?                  [L1 if NO]
[ ] Is the file type correct for its directory location (§5)?                  [L1 if NO]

FILE NAMING
[ ] Does the filename match the naming pattern for this type (§4)?             [L2 if NO]
[ ] Is the filename all lowercase kebab (or UPPER-KEBAB for root governance)?  [L3 if NO]
[ ] Is the filename under 80 characters?                                        [L4 if NO]

FILE STRUCTURE
[ ] Does the file contain all required sections for its type (§3)?             [L2 if NO]
[ ] Are all sections in the correct order per §3?                              [L3 if NO]
[ ] Does the ## Tests section (skills) have ≥ 9 test cases?                   [L2 if NO]
[ ] Does the YAML tests: field match the actual test count?                    [L2 if NO]

CROSS-REFERENCES
[ ] Do all ANN artifact IDs referenced in this file exist in artifacts/?       [L2 if NO]
[ ] Do all SKL-NN-NN skill IDs referenced in this file exist in skills/?       [L2 if NO]
[ ] Do all ref IDs (PRnn, PDnn, Pnn, FAnn) exist in reference/?                [L2 if NO]

SOURCE TRACEABILITY
[ ] Does every substantive claim cite a source with a section number (§6)?    [L2 if NO]
[ ] Is every citation using a recognized short-code from §6.1?                 [L3 if NO]
[ ] Is there NO verbatim PMI text in the file?                                 [L1 if NO]

TEMPLATE INTEGRITY
[ ] If this is a template (ART-TPL), are ALL [FIELD: ...] placeholders intact? [L1 if NO]
[ ] If this is an example (ART-EX), is the Meridian scenario used throughout?  [L2 if NO]

COMMIT HYGIENE
[ ] Does the commit message follow the §7.5 convention?                        [L3 if NO]
[ ] Does the commit message include Files: and Phase: lines?                   [L3 if NO]
[ ] Is this a single-file commit (preferred) or a justified multi-file commit? [L4 if NO]
```

---

## 10. Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-06-01 | Initial build — derived from live repo audit of SKL-01-01, A06/A08/A14/A15/A16 triplets, PD/PR/FA reference files, COMPLETION-PLAN-V4 §2. Adds YAML schemas for all 7 file types, exact section structures for all types, naming regex patterns, canonical directory tree, source short-codes for all 23 companion refs, 8-level phase exit gate checklists, non-conformance register NC-001–NC-008, AI agent pre-commit checklist. |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*  
*Repository: https://github.com/fakhruldeen/PMOSkills*  
*Maintainer: @fakhruldeen*  
*Last Updated: 2026-06-01 · Version 1.0.0*

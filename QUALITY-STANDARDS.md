# PMOSkills — Quality Standards and Enforcement Rules
**Version:** 1.1.0  
**Date:** 2026-06-01  
**Repository:** https://github.com/fakhruldeen/PMOSkills  
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary  
**Status:** Active · Enforced from v4.4.0 of MASTER-PLAN  
**Applies to:** Every file in this repository — past, present, and future

> This document is the **single authoritative source** for quality standards, structural requirements, file naming rules, and quality gate enforcement for the PMOSkills repository. All other documents that reference quality standards defer to this file. When this document conflicts with `COMPLETION-PLAN-V4.md §2`, this document takes precedence.

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

**Example scenario lock:** All artifact examples in this repository use the **Meridian CRM System Upgrade** scenario for cross-artifact consistency. No other scenario may be used without a governance decision logged in CHANGELOG.md and MASTER-PLAN.md.

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

### 2.7 Shared Component File (`SHR`) — Required YAML

New in v1.1.0. Applies to all files under `shared/validators/`, `shared/checklists/`, `shared/components/`, and `shared/routing/`.

```yaml
---
shared_id: SHR-{subtype}-NN                  # required · e.g. SHR-VAL-01, SHR-CL-03
shared_name: [Full Component Name]           # required · title case
shared_type: Validator|Checklist|Component|Routing  # required
version: "1.0.0"                            # required
status: Active                               # required
applies_to:                                  # required · file type(s) this component is used for
  - SKL
  - ART-DEF
file_path: "shared/subdir/kebab-name.md"    # required
---
```

---

### 2.8 Test File (`TST`) — Required YAML

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

### 2.9 Root Governance File (`GOV`) — Required YAML

New in v1.1.0. Applies to all UPPER-KEBAB.md files at root level.

```yaml
---
gov_id: [FILENAME without extension]         # required · e.g. MASTER-PLAN
gov_name: [Full Document Name]               # required · title case
version: "N.N.N"                            # required · semver
status: Active                               # required
authority: PMBOK8 Primary                   # required
supersedes: [filename or "none"]            # required · traceability chain
file_path: "[FILENAME].md"                  # required
---
```

---

## 3. File Structure Standards

### 3.1 Skill File Structure (`SKL`)

Every full skill file must contain exactly these sections in this order. No section may be omitted. No section may be renamed.

```
[YAML front-matter]                    ← required · per §2.1

# SKL-NN-NN — [Skill Name]            ← H1 heading · exact format

**Skill ID:** SKL-NN-NN               ← metadata block (bold labels)
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
                                         Minimum 6 rows: Simple | Large/multi-phase | Program | Regulated | Adaptive | Hybrid

## Failure Cases                       ← §3.1.8 · table: Failure | Symptom | Resolution
                                         Minimum 5 rows

## Tests                               ← §3.1.9 · table: Test ID | Description | Pass | Fail
                                         Minimum 9 test cases per skill

## Change Log                          ← §3.1.10 · table: Version | Date | Change description

---

*Authority: [PMBOK8 ref]*             ← footer block (4 italic lines)
*Source type: PMI-derived*
*Owner: [role]*
*Approval authority: [role]*
```

**Minimums enforced:**
- Test cases: ≥ 9 (matching `tests:` YAML field)
- Tailoring rows: ≥ 6 approaches
- Failure cases: ≥ 5 rows
- Instructions: ≥ 4 named steps

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

**Minimums enforced:**
- Quality criteria: ≥ 5 rows
- Waste test: exactly 5 yes/no questions
- Related artifacts: ≥ 1 entry

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

**Enforcement:** No `[FIELD: ...]` placeholder may contain actual data. This is a critical (L1) failure.

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

**Minimums enforced:**
- Key characteristics: 4–8 bullets
- Practitioner notes: 3–5 questions
- Cross-references: ≥ 2 entries

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
[YAML front-matter]                    ← required · per §2.8

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

**Minimums enforced:**
- Test cases: ≥ 9 per skill test file (must match `test_case_count:` in YAML)
- Every test case must have all 6 fields: Scenario, Input, Expected output, Pass condition, Fail condition, Authority check

---

### 3.8 Shared Component File Structure (`SHR`) — New in v1.1.0

Applies to all files under `shared/validators/`, `shared/checklists/`, `shared/components/`, `shared/routing/`.

```
[YAML front-matter]                    ← required · per §2.7

# [Component Name]

**Component ID:** SHR-{type}-NN  
**Type:** Validator | Checklist | Component | Routing  
**Applies to:** [file type(s)]  
**Version:** 1.0.0  
**Status:** Active

---

## Purpose                             ← what this component does and when to invoke it

## Applies To                          ← which file types, phases, or contexts use this

## Inputs                              ← what the component needs to operate

## Instructions / Logic                ← numbered steps or decision table

## Output / Result Format              ← what the component produces (PASS/FAIL/score/decision)

## Failure Handling                    ← what to do when output is FAIL or BLOCK

## Examples                            ← at least one worked example showing PASS and FAIL

## Change Log                          ← table: Version | Date | Change
```

**Validator-specific rule:** Every validator must produce a binary or categorical output (PASS/FAIL/WARN) — it must not produce only narrative text. Narrative explanation may accompany the binary output but is not sufficient alone.

---

### 3.9 Root Governance File Structure (`GOV`) — New in v1.1.0

Applies to all UPPER-KEBAB.md files at root.

```
[YAML front-matter]                    ← required · per §2.9

# [Document Title]
**Version:** N.N.N  
**Date:** YYYY-MM-DD  
**Repository:** [URL]  
**Authority:** [primary authority]  
**Status:** Active  
**Supersedes:** [filename or "none"]

> [One-line purpose statement or update note for this version]

---

[Document sections — H2/H3 as appropriate to document type]

---

## Version History (or Change Log)     ← table: Version | Date | Changes

---
*Authority: [source]*  
*Repository: [URL]*  
*Maintainer: @[handle]*  
*Last Updated: YYYY-MM-DD · Version N.N.N*
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
A14-Integrated-Project-Management-Plan.md        ⚠️ capital letters — non-conformant (legacy, NC-001)
A14-integrated-project-management-plan.md        ✅ correct form
```

- Artifact number: 2-digit zero-padded (`A01` through `A41`)
- Every artifact **must** have all three files (definition + template + example) to be fully complete
- Partial delivery is acceptable during build phases but must be flagged in scorecard

**Legacy non-conformances (must fix in Phase 7):**
- `A14-Integrated-Project-Management-Plan.md` → NC-001
- `A15-Schedule-Model-and-Baseline-Record.md` → NC-002
- `A16-Financial-Management-and-Cost-Baseline-Record.md` → NC-003

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
COMPLETION-PLAN-V4.md   ✅
README.md               ✅
CHANGELOG.md            ✅
```

### 4.8 Prohibited Filename Patterns — New in v1.1.0

The following filename patterns are **never permitted** and constitute an L1 or L2 failure:

| Pattern | Example | Failure Level | Reason |
|---|---|---|---|
| Contains spaces | `my skill.md` | L1 | Breaks tooling and links |
| Uses underscores | `SKL_01_01.md` | L2 | Not kebab-case standard |
| Mixed case (non-root) | `ProjectCharter.md` | L2 | Not kebab-case standard |
| No ID prefix (skills) | `governance-framework.md` in skills/ | L1 | Not traceable |
| No ID prefix (artifacts) | `project-plan.md` in artifacts/ | L1 | Not traceable |
| Generic names | `template.md`, `index2.md`, `test.md` | L2 | Not descriptive |
| Version in filename | `SKL-01-01-v2.md` | L2 | Version belongs in YAML only |
| Duplicate names in diff dirs | Same filename in two different subdirs | L2 | Creates ambiguity |

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
│   ├── knowledge/                               ← pending audit (P0-R7)
│   ├── monitoring-and-decisions/
│   ├── planning-and-baselines/
│   ├── pmo/                                     ← pending audit (P0-R8)
│   ├── portfolio/                               ← pending audit (P0-R9)
│   ├── procurement/
│   ├── quality/                                 ← pending audit (P0-R10)
│   ├── resources/
│   ├── stakeholders/
│   └── stakeholders-communications/             ← pending audit (P0-R11)
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
│   ├── companion-references/                    ← Phase 4-C10
│   ├── tailoring/                               ← Phase 4-C11
│   └── pmo/                                     ← Phase 4-C12
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
2. **No new top-level directories** may be created without a governance decision. `C4-Process-Records/`, `C5-KA-Crossref/`, `C6-TT-Taxonomy/`, `C7-IO-Registry/`, and `repo/` are current structural violations (NC-004) awaiting Phase 0 cleanup.
3. **Every directory with 3+ files must have an `index.md`** that lists all files, their status, and their purpose.
4. **No file may exist in a parent directory** if it belongs in a subdirectory.
5. **Directory names use lowercase kebab-case** with numeric prefix for ordered packs.
6. **The `docs/legacy/` subdirectory** is the only permitted archive location for superseded files.

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

### 5.4 New Directory Creation Governance Protocol — New in v1.1.0

Before creating any directory not listed in §5.1:

1. **Check §5.1** — confirm the directory does not already exist under another canonical name.
2. **Log intent** in MASTER-PLAN.md under a new task entry.
3. **Log decision** in CHANGELOG.md with `chore(root):` commit.
4. **Update §5.1** in this file (QUALITY-STANDARDS.md) in the same commit.
5. **Update reference/README.md or relevant parent README** if the new dir is inside `reference/`.

Failure to follow this protocol = L2 non-conformance (NC entry required).

---

## 6. Source Traceability Rules

### 6.1 Citation Format

Every substantive claim in every file must be traceable to a source. Use this format at the end of the
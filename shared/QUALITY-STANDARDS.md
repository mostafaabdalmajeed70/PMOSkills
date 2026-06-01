---
document_id: QS-01
document_name: PMOSkills Quality Standards
version: "1.0.0"
status: Active · Enforced
authority: PMBOK8 Primary · Repository Governance
applies_to: All files in PMOSkills repository
enforceable_from: 2026-06-01
---

# PMOSkills Quality Standards

**Document ID:** QS-01  
**Version:** 1.0.0  
**Status:** Active · Enforced  
**Applies to:** Every file created or modified in the PMOSkills repository  
**Authority:** PMBOK8 Standard and Guide · Repository Governance  
**Enforcement:** Every file must pass all applicable checks before commit is accepted.

> These standards are derived from the actual structures present in the repository as of 2026-06-01.
> They are the law of this repo. No file may be committed that fails its applicable quality gate.

---

## 1. Directory Structure and File Naming

### 1.1 Canonical Directory Structure

```
PMOSkills/
├── README.md
├── SKILL-REGISTRY.md
├── AUTHORITY-ROUTING.md
├── LIFECYCLE-MAP.md
├── PRINCIPLES-CROSSWALK.md
├── MASTER-PLAN.md
├── COMPLETION-PLAN-V4.md
├── CHANGELOG.md
├── source-authority.md
├── pmi_reference_list.md
│
├── docs/
│   ├── img/
│   └── *.md                              (lowercase, hyphen-separated)
│
├── artifacts/
│   ├── initiation/
│   ├── organizational-setup/
│   ├── planning-and-baselines/
│   ├── monitoring-and-decisions/
│   ├── execution/
│   ├── resources/
│   ├── closing/
│   ├── procurement/
│   ├── adaptive-hybrid/
│   └── organizational/
│
├── skills/
│   ├── 01-organizational-setup/
│   ├── 02-initiating/
│   ├── 03-planning/
│   ├── 04-executing/
│   ├── 05-monitoring-controlling/
│   ├── 06-closing/
│   ├── 07-adaptive-hybrid/
│   ├── 08-pmo/
│   └── 09-portfolio-program/
│
├── reference/
│   ├── README.md
│   ├── principles/
│   ├── performance-domains/
│   ├── focus-areas/
│   ├── processes/
│   ├── inputs-outputs/
│   ├── tools-techniques/
│   ├── appendices/
│   ├── companion-references/
│   ├── pmo/
│   └── GLOSSARY.md
│
├── shared/
│   ├── QUALITY-STANDARDS.md              ← This file
│   ├── validators/
│   ├── components/
│   ├── routing/
│   └── checklists/
│
└── tests/
    ├── skill-tests/
    └── integration-tests/
```

### 1.2 File Naming Rules

| File Type | Pattern | Example |
|---|---|---|
| Skill file | `SKL-NN-NN-short-hyphenated-name.md` | `SKL-03-02-define-project-scope.md` |
| Artifact definition | `ANN-short-hyphenated-name.md` | `A08-scope-requirements-backlog.md` |
| Artifact template | `ANN-short-hyphenated-name-template.md` | `A08-scope-requirements-backlog-template.md` |
| Artifact example | `ANN-short-hyphenated-name-example.md` | `A08-scope-requirements-backlog-example.md` |
| Reference — principle | `PNN-hyphenated-name.md` | `P01-stewardship.md` |
| Reference — perf domain | `PDNN-hyphenated-name.md` | `PD01-stakeholders.md` |
| Reference — focus area | `FANN-hyphenated-name.md` | `FA01-uncertainty.md` |
| Reference — process | `PRNN-hyphenated-name.md` | `PR11-develop-project-charter.md` |
| Reference — appendix | `XN-hyphenated-name.md` | `X2-pmo.md` |
| Test — skill | `ST-SKL-NN-NN.md` | `ST-SKL-03-02.md` |
| Test — integration | `IT-NN-hyphenated-name.md` | `IT-01-setup-to-initiate.md` |
| Shared validator | `hyphenated-name.md` | `artifact-waste-test.md` |
| Docs file | `hyphenated-name.md` | `getting-started.md` |

**Absolute naming rules:**
- All filenames: **lowercase only**, **hyphens only** (no underscores, no spaces, no camelCase)
- IDs (SKL-NN-NN, ANN, PNN, PDNN, etc.): **uppercase prefix, zero-padded numbers**
- No version numbers in filenames — version is tracked in front matter only
- No special characters except hyphens and dots (for extension)

### 1.3 Prohibited Patterns

| Pattern | Reason | Example of violation |
|---|---|---|
| Files at repo root that are not governance docs | Clutters root namespace | `C4-Process-Records/` at root |
| Directories not in canonical structure | Creates orphaned content | `/repo/`, `/C5-KA-Crossref/` |
| Mixed-case filenames | Breaks cross-platform compatibility | `A14-Integrated-Project-Management-Plan.md` |
| Underscores in filenames | Inconsistent with repo standard | `skill_template.md` |
| Duplicate content in multiple directories | Creates authority confusion | Same content in `reference/C4/` and `reference/processes/` |
| Version numbers in filenames | Version belongs in front matter | `A08-v2-scope.md` |

---

## 2. Skill File Standard

### 2.1 Required YAML Front Matter

Every skill file must begin with this exact front-matter block (all fields mandatory):

```yaml
---
skill_id: SKL-NN-NN
skill_name: [Full descriptive skill name]
pack: "NN — [Pack name]"
version: "1.0.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact_output: "ANN — [Artifact name] ([section if applicable])"
artifacts_updated:
  - "ANN — [Artifact name] ([section])"
pmbok8_process_anchor: "[PMBOK8 source — Guide or Standard — specific section]"
performance_domains:
  - [Domain name]
focus_area: [Initiating / Planning / Executing / Monitoring and Controlling / Closing / Adaptive-Hybrid / Organizational Setup / PMO / Portfolio-Program]
upstream_prerequisites:
  - "[ANN or SKL-NN-NN — what must exist before this skill runs]"
downstream_skills:
  - "[SKL-NN-NN — [Skill name]]"
file_path: "skills/NN-[pack-folder]/SKL-NN-NN-[hyphenated-name].md"
tests: [number of test cases]
---
```

### 2.2 Required Sections (in order)

Every skill file must contain all of these sections, in this exact order:

```
# SKL-NN-NN — [Skill Name]         ← H1 heading

[Identity block: Skill ID, Pack, Status, Source type, PMBOK8 anchor, File path]

## Purpose
## Scope
## Inputs Required                  ← Table: Input | Source | Mandatory?
## Instructions                     ← Numbered steps, grouped under ### Step N — [Name] headings
## Outputs                          ← Table: Output | Artifact | Section | Notes
## Constraints
## Tailoring Guidance               ← Table: Approach | Adjustment
## Failure Cases                    ← Table: Failure | Symptom | Resolution
## Tests                            ← Table: Test ID | Description | Pass condition | Fail condition
## Change Log                       ← Table: Version | Date | Change description

[Footer: Authority line · Source type · Owner · Approval authority]
```

### 2.3 Skill Quality Gates

A skill file **passes** only if ALL of the following are true:

- [ ] YAML front matter is complete — all 12 fields present and populated
- [ ] `skill_id` matches the filename prefix exactly (e.g. `SKL-03-02` in file named `SKL-03-02-*.md`)
- [ ] `pmbok8_process_anchor` contains a specific section number (e.g. `§2.2.2.1`) — not a chapter title alone
- [ ] `status` is one of: `Draft · Untested` / `Active` / `Deprecated`
- [ ] All sections present in required order
- [ ] `## Inputs Required` is a table with columns: Input | Source | Mandatory?
- [ ] `## Instructions` has minimum 3 numbered steps, each under a `### Step N —` heading
- [ ] `## Outputs` is a table with columns: Output | Artifact | Section | Notes
- [ ] `## Failure Cases` is a table with columns: Failure | Symptom | Resolution — minimum 3 rows
- [ ] `## Tests` has minimum 2 test cases, each with: Test ID | Description | Pass condition | Fail condition
- [ ] `## Tailoring Guidance` is a table covering at least: simple/predictive, large/complex, and adaptive/agile approaches
- [ ] `## Change Log` has at least one entry with version, date, and change description
- [ ] Footer authority line cites PMBOK8 with specific section number
- [ ] No `[FIELD: ...]` placeholders left unfilled
- [ ] No PMI copyrighted text reproduced verbatim (synthesis and paraphrase only)
- [ ] All artifact references (ANN) resolve to existing files in `artifacts/`
- [ ] All skill cross-references (SKL-NN-NN) resolve to entries in `SKILL-REGISTRY.md`
- [ ] File is in the correct `skills/NN-[pack-folder]/` directory
- [ ] Filename follows pattern: `SKL-NN-NN-hyphenated-name.md` (all lowercase, hyphens only)

---

## 3. Artifact Definition File Standard

### 3.1 Required Header Block

Artifact definition files do NOT use YAML front matter — they use a Markdown header block:

```markdown
# ANN — [Artifact Full Name]
**Artifact ID:** ANN
**Artifact Name:** [Full name]
**Version:** 1.0.0
**Status:** Definition · Active
**Authority:** [PMBOK8 Guide §X.X · companion reference codes]
**Source Type:** PMI-derived
**File Path:** `artifacts/[category-folder]/ANN-hyphenated-name.md`
```

### 3.2 Required Sections (in order)

```
## Definition          ← 1–2 paragraphs. PMI source cited inline.
## Artifact Type       ← Table: Category | Type | Lifecycle | Baseline? | Ownership
## Purpose             ← Bullet list of what this artifact achieves
## Sections            ← Table: Section | Content | Populated By (skill ID)
## Inputs              ← Table: Input | Source (ANN or EEF/OPA)
## Outputs / Produces  ← Table: Output | Used By
## Quality Criteria    ← Bullet list — measurable, testable criteria only
## Related Artifacts   ← Table: Artifact | Relationship
## PMBOK8 Anchors      ← Table: Reference | Detail

[Footer: Owner · Version Control · Change Control · Last Updated]
```

### 3.3 Artifact Definition Quality Gates

- [ ] Header block complete — all 6 fields present
- [ ] `Artifact ID` in header matches filename prefix (e.g. `A08` in `A08-*.md`)
- [ ] `## Definition` cites PMBOK8 with specific section number inline
- [ ] `## Artifact Type` table contains: Category, Type, Lifecycle, Baseline?, Ownership
- [ ] `## Sections` table has column: Populated By — populated with skill IDs (e.g. `SKL-03-02`)
- [ ] `## Inputs` and `## Outputs / Produces` are both tables with Source/Used By columns
- [ ] `## Quality Criteria` contains only measurable, testable statements (no vague language)
- [ ] `## PMBOK8 Anchors` cites at least one specific section number
- [ ] Waste test passes: the artifact cannot be removed without breaking a downstream skill or output
- [ ] Footer includes: Owner, Version Control method, Change Control threshold, Last Updated date
- [ ] A corresponding template file exists: `ANN-[name]-template.md`
- [ ] File is in the correct `artifacts/[category]/` directory
- [ ] Filename: `ANN-hyphenated-name.md` (all lowercase, hyphens only, no version in name)

---

## 4. Artifact Template File Standard

### 4.1 Required YAML Front Matter

```yaml
---
artifact_id: ANN
artifact_name: [Full artifact name]
artifact_type: template
version: "1.0.0"
status: Template · Active
parent_definition: artifacts/[category]/ANN-hyphenated-name.md
authority: [PMBOK8 Guide §X.X · companion reference codes]
---
```

### 4.2 Required Structure

```
# ANN — [Artifact Name] Template

> **Usage note:** [One paragraph — when to use, how to complete, approval required before use]

## Section 1 — [Section name]
### 1.1 Record Header        ← Always the first sub-section. Contains standard metadata table.
[Tables or fields using [FIELD: description] placeholders]

## Section N — ...
[Repeat per definition §Sections table]

## Section [Last] — [Approval/Sign-off section]
[Table: Version | Date | Status | Approved by | Notes]

[Footer: Authority line · Source type · Version · Parent definition reference]
```

### 4.3 Template Quality Gates

- [ ] YAML front matter complete — all 6 fields present
- [ ] `artifact_id` matches filename prefix
- [ ] `parent_definition` path resolves to an existing artifact definition file
- [ ] `artifact_type: template` is set exactly
- [ ] Usage note is present and describes approval requirement
- [ ] Every section from the parent definition's `## Sections` table is represented
- [ ] Section 1 begins with a Record Header sub-section (standard project metadata)
- [ ] Last section is an Approval/Sign-off section
- [ ] All fillable fields use exact format: `[FIELD: description of what to enter]`
- [ ] No `[FIELD: ...]` is pre-filled with sample data (templates must be blank)
- [ ] Footer authority line matches parent definition authority
- [ ] Filename: `ANN-hyphenated-name-template.md`

---

## 5. Artifact Example File Standard

### 5.1 Required YAML Front Matter

```yaml
---
artifact_id: ANN
artifact_name: [Full artifact name]
artifact_type: example
version: "1.0.0"
status: Example · Active
scenario: Meridian CRM Platform — Phase 1
parent_template: artifacts/[category]/ANN-hyphenated-name-template.md
parent_definition: artifacts/[category]/ANN-hyphenated-name.md
authority: [PMBOK8 Guide §X.X · companion reference codes]
---
```

### 5.2 Required Structure

```
# ANN — [Artifact Name]: Meridian CRM Platform Example

> **Scenario context:** [Brief description of the Meridian CRM scenario context for this artifact]
> **Purpose of this example:** [What this example demonstrates]

[All sections from the template, fully completed with Meridian CRM scenario data]

## Example Notes
[Table or bullets: Field | Note — explains non-obvious decisions in the example]

[Footer: Scenario · Template · Definition · Authority]
```

### 5.3 Example Quality Gates

- [ ] YAML front matter complete — all 7 fields present
- [ ] `scenario: Meridian CRM Platform — Phase 1` is set (all examples use same scenario)
- [ ] `artifact_type: example` is set exactly
- [ ] Both `parent_template` and `parent_definition` paths resolve to existing files
- [ ] No `[FIELD: ...]` placeholders remain — all are filled with realistic Meridian CRM data
- [ ] All sections from the template are represented
- [ ] `## Example Notes` section explains key decisions
- [ ] No PMI copyrighted text reproduced verbatim
- [ ] Filename: `ANN-hyphenated-name-example.md`

---

## 6. Reference File Standard

### 6.1 Required YAML Front Matter

All reference files (principles, performance domains, focus areas, processes, appendices) use YAML front matter:

```yaml
---
reference_type: [Principle / Performance Domain / Focus Area / Process / Appendix / Companion Reference / PMO / Tailoring]
reference_id: [PNN / PDNN / FANN / PRNN / XN / CR-NN]
name: [Short reference name]
version: "1.0.0"
status: Active
pmbok8_source: "PMBOK8 [Guide or Standard] §X.X — [Section title]"
authority: PMI-derived
---
```

### 6.2 Required Sections (in order)

```
# [ID] — [Full Name]                ← H1
**Type:** [reference_type]
**PMBOK8 Source:** [specific section]
**Version:** [version]

## Definition
## Desired Outcomes               (for Performance Domains)
## Key Activities and Considerations
## Relationship to Principles      ← Table: Principle | Connection
## Artifact Connections            ← Table: Artifact | Connection
## Skill Connections               ← Table: Skill ID | Skill Name | Connection
## Interaction with Other Domains  (for Performance Domains)
## Questions to Ask in Practice

[Footer: Authority line · Repository URL]
```

> **Note:** Process files (PRNN) use a different section order:
> Inputs → Tools & Techniques → Outputs → Connected Skills → PMBOK8 Anchor

### 6.3 Reference File Quality Gates

- [ ] YAML front matter complete — all 7 fields present
- [ ] `reference_type` is one of the defined types
- [ ] `pmbok8_source` contains a specific section number
- [ ] `## Definition` is present and cites PMBOK8 inline
- [ ] `## Artifact Connections` table resolves all ANN references to existing artifact files
- [ ] `## Skill Connections` table resolves all SKL-NN-NN references to SKILL-REGISTRY.md entries
- [ ] `## Questions to Ask in Practice` has minimum 3 questions
- [ ] Footer includes repository URL
- [ ] No PMI copyrighted text reproduced verbatim
- [ ] Filename follows the correct ID prefix pattern for its type
- [ ] File is in the correct `reference/[subdir]/` directory

---

## 7. Documentation (`docs/`) File Standard

### 7.1 Required Structure

Docs files do not use YAML front matter. They use a Markdown header block:

```
# [Document Title]
**Version:** 1.0.0  
**Audience:** [Target audience]  
**Last Updated:** YYYY-MM-DD  

## Purpose
## Audience
## Prerequisites
[Numbered or bulleted instructions / content]
## Related Files
[Table: File | Purpose | Link]

[Footer: Repository link · Version]
```

### 7.2 Docs Quality Gates

- [ ] Title is an H1 heading
- [ ] Version, Audience, Last Updated in header block
- [ ] `## Purpose`, `## Audience`, `## Prerequisites` all present
- [ ] `## Related Files` table with File | Purpose | Link columns
- [ ] No orphaned sections — every heading has content
- [ ] Filename: `lowercase-hyphenated.md`
- [ ] File is in `docs/` (not in repo root or subdirectories of `docs/`)

---

## 8. Test File Standard

### 8.1 Skill Test File (ST-SKL-NN-NN.md)

```yaml
---
test_id: ST-SKL-NN-NN
test_name: Skill Test — [Skill name]
target_skill: SKL-NN-NN
version: "1.0.0"
status: Active
---
```

Required sections:
```
# ST-SKL-NN-NN — Skill Test: [Skill Name]
## Test Scope
## Pre-conditions
## Test Cases        ← Table: TC-ID | Scenario | Steps | Expected output | Pass/Fail criteria
## Regression Checks
## Test Log          ← Table: Run date | Tester | Result | Notes
```

### 8.2 Integration Test File (IT-NN-*.md)

Required sections:
```
# IT-NN — Integration Test: [Lifecycle Segment]
## Scope
## Artifact Flow     ← Diagram or table showing artifact hand-offs
## Steps
## Expected End State
## Pass Criteria
## Test Log
```

### 8.3 Test File Quality Gates

- [ ] YAML front matter complete (skill tests only)
- [ ] Target skill or scope clearly identified
- [ ] Minimum 2 test cases per skill test
- [ ] Each test case has: scenario, steps, expected output, pass/fail criteria
- [ ] Integration tests trace artifact flow end-to-end across at least 2 lifecycle phases
- [ ] All referenced skill IDs and artifact IDs resolve
- [ ] Filename: `ST-SKL-NN-NN.md` or `IT-NN-hyphenated-name.md`

---

## 9. Shared Component File Standard

### 9.1 Validator Files (`shared/validators/`)

```
# [Validator Name]
## Purpose
## Target File Type
## When to Run
## Checklist               ← Numbered list of pass/fail checks
## Scoring                  ← Pass threshold definition
## Output Format            ← What a passing result looks like vs failing
```

Quality gate: Every checklist item must produce a deterministic **pass** or **fail** — no partial or subjective results.

### 9.2 Checklist Files (`shared/checklists/`)

```
# [Checklist Name]
## Purpose
## Audience
## When to Use
## Checklist Items          ← [ ] Checkbox format, each item is independently verifiable
## Exit Criterion
```

---

## 10. PMBOK8 Citation Standard

Every PMI citation must follow one of these exact formats:

| Source | Format | Example |
|---|---|---|
| PMBOK8 Guide chapter section | `PMBOK8 Guide §X.X.X` | `PMBOK8 Guide §2.2.2.1` |
| PMBOK8 Standard principle | `PMBOK8 Standard §3 — [Principle name]` | `PMBOK8 Standard §3 — Stewardship` |
| Companion reference | `[SHORT-CODE] §X.X` or `[SHORT-CODE] Chapter N` | `WBS-3E §3.2` · `PSS-3E Chapter 4` |
| PMO Practice Guide | `PMO-PG §X.X` | `PMO-PG §2.3` |
| Process Groups Guide | `PG-PG §X.X` | `PG-PG §4.2` |

**Violations that will cause a quality gate failure:**
- Citation with no section number (e.g. "per PMBOK8" alone)
- Chapter title without section number (e.g. "Planning chapter")
- Unresolvable reference (short code not in `pmi_reference_list.md`)
- Reproduced verbatim PMI text without paraphrase

---

## 11. Commit Message Standard

Every commit must follow this format exactly:

```
type(scope): short description (max 72 chars)

Body:
- What changed and why
- Files added/modified/deleted (list each)

Phase: [Phase N — description]
Authority: [PMBOK8 source if applicable]
```

| Field | Allowed values |
|---|---|
| `type` | `feat` · `fix` · `docs` · `chore` · `refactor` · `test` · `quality` |
| `scope` | `skills` · `artifacts` · `docs` · `reference` · `shared` · `tests` · `root` · `pmo` · `ppp` |

**Rules:**
- Subject line max 72 characters
- No emoji in commit messages
- Must reference a Phase from COMPLETION-PLAN-V4.md or MASTER-PLAN.md
- Batch commits (multiple files in one commit) are acceptable only within the same file type and phase

---

## 12. Version Numbering Standard

All files use semantic versioning: `MAJOR.MINOR.PATCH`

| Increment | When |
|---|---|
| MAJOR (1.0.0 → 2.0.0) | Structural change — sections added, removed, or reordered; breaking change to cross-references |
| MINOR (1.0.0 → 1.1.0) | Content addition — new rows in tables, new steps, new test cases |
| PATCH (1.0.0 → 1.0.1) | Correction — typo fix, citation correction, clarification without structural change |

**Rules:**
- New files always start at `1.0.0`
- Every version bump requires a `## Change Log` entry (skills) or CHANGELOG.md entry (repo-level)
- Never put version number in the filename — front matter only

---

## 13. Cross-Reference Integrity Standard

All cross-references in any file must be **resolvable** at commit time:

| Reference type | Must resolve to |
|---|---|
| `ANN` | Existing file in `artifacts/[category]/ANN-*.md` |
| `SKL-NN-NN` | Existing entry in `SKILL-REGISTRY.md` |
| `PRNN` | Existing file in `reference/processes/PRNN-*.md` |
| `PDNN` | Existing file in `reference/performance-domains/PDNN-*.md` |
| `PNN` | Existing file in `reference/principles/PNN-*.md` |
| `FANN` | Existing file in `reference/focus-areas/FANN-*.md` |
| Short code (WBS-3E, etc.) | Entry in `pmi_reference_list.md` |
| File path in `file_path:` or `parent_definition:` | Actual file at that path in the repo |

**Broken cross-references are a quality gate failure and must block commit.**

---

## 14. Quality Audit Schedule

| Trigger | Audit scope | Auditor |
|---|---|
| After every individual file commit | File-level quality gate (applicable section from §2–§9) | Committer (self-check before commit) |
| After every phase completion | Full phase output — all files in phase | AI agent or PMO reviewer |
| When any root governance file is modified | Cross-reference integrity check across all files that cite it | Committer |
| Monthly | Full repo scan — naming violations, broken cross-refs, missing sections | PMO Director |

### 14.1 Quality Audit Output Format

Every audit must produce an entry in `CHANGELOG.md` with:

```
## [Date] — Quality Audit — [Scope]
- Files audited: N
- Violations found: N
- Violations resolved: N
- Outstanding issues: [list or "None"]
- Next audit trigger: [Phase completion / Monthly / Governance change]
```

---

## 15. Retroactive Enforcement (Current Repo Contents)

The following known violations in existing files must be remediated in Phase 0 or the first available session:

| Violation | Files affected | Action |
|---|---|---|
| Mixed-case filenames | `A14-Integrated-Project-Management-Plan.md`, `A15-Schedule-Model-and-Baseline-Record.md`, `A16-Financial-Management-and-Cost-Baseline-Record.md` | Rename to all-lowercase hyphenated |
| Artifact definitions missing YAML front matter | All ANN definition files (they use Markdown header blocks by design — see §3.1) | Not a violation — definition files use header blocks, not YAML |
| Stale directories at repo root | `/C4-Process-Records/`, `/C5-KA-Crossref/`, `/C6-TT-Taxonomy/`, `/C7-IO-Registry/`, `/repo/` | Delete after content migration (Phase 0) |
| Legacy reference subdirectories | `reference/C4-Process-Records/`, `reference/C5-KA-Crossref/`, etc. | Delete after content migration (Phase 0) |
| PR01–PR10 process records missing | `reference/processes/` | Rebuild (Phase 4-C4) |

---

*Document ID: QS-01 · Version: 1.0.0 · Date: 2026-06-01*  
*Authority: Repository Governance · PMBOK8 Standard and Guide*  
*Owner: PMO Director / Repository Maintainer*  
*Review cycle: After each major phase completion*  
*Repository: https://github.com/fakhruldeen/PMOSkills*

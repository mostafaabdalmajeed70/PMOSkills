# 🚀 PMOSkills Release Notes — v0.4

We are proud to present **PMOSkills Release v0.4** — the **NPM SDK Publication** milestone. This release transforms the PMOSkills repository from a documentation-only knowledge base into a fully **programmatically accessible, distributable NPM package** — making the entire corpus queryable in any Node.js, Edge, or Browser environment with a single `npm install`.

---

## 🏷️ Release Metadata

* **Release Tag:** `v0.4`
* **Release Date:** June 2, 2026
* **NPM Package:** [`pmoskills@0.3.0`](https://www.npmjs.com/package/pmoskills)
* **NPM Publisher:** `fakhruldeen`
* **Primary Authority:** PMI PMBOK® 8th Edition Compliant
* **Secondary Authority:** 23 Companion Reference Manuals (OPM, GPPP, BA, Risk-PPP, etc.)
* **Total SDK Corpus Items:** **369+** (compiled at build time into zero-dependency bundle)
* **Zenodo DOI:** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20510540-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20510540) (`10.5281/zenodo.20510540`)

---

## 🌟 What's New in v0.4

### 1. 📦 NPM Package — `pmoskills` (Published Public)

The `pmoskills` package is now publicly available on the NPM registry:

```bash
npm install pmoskills
```

* **Zero production dependencies** — fully self-contained
* **Dual module output:** ESM (`dist/index.mjs`) + CommonJS (`dist/index.js`)
* **Full TypeScript declarations** (`.d.ts` files included)
* **Edge-compatible:** works in Cloudflare Workers, Vercel Edge, and Browser environments

---

### 2. 🏗️ Full Corpus Build-Time Compiler

A new build pipeline (`sdk/scripts/compile-db.ts`) recursively crawls the entire repository and serializes all content into a single embedded JSON store (`src/db/store.json`) at build time:

| Directory | Files Compiled | Description |
|---|:---:|---|
| `skills/` | 48 | Executable PMO skill definitions |
| `reference/processes/` | 41 | PMBOK 8 process records |
| `artifacts/` | 92 | Deliverable templates (A01–A39) |
| `reference/` (non-process) | 97 | Principles, domains, focus areas |
| `shared/` | 28 | Validators, checklists, scripts |
| `tests/` | 59 | ST-SKL-* compliance test scenarios |
| `docs/ai-agents/` | 4 | System prompts + ontology |
| **Total** | **369+** | |

**Advanced Title Fallback:** The compiler extracts clean human-readable titles using a priority chain: `metadata.name` → `metadata.title` → first markdown `# heading` → filename.

---

### 3. 🔌 Type-Safe SDK API (`PMOSkillsLoader`)

All corpus items are exposed via a singleton `pmoskills` instance with fully type-safe getters:

```typescript
import { pmoskills, inject } from 'pmoskills';

// Executable Skills
const skill = pmoskills.getSkill('SKL-01-01');
const govSkills = pmoskills.getSkillsByDomain('Governance');

// PMBOK 8 Process Records
const process = pmoskills.getProcess('PR01');

// Artifact Templates
const template = pmoskills.getArtifact('A01');
console.log(template.title);    // → "Business Case"
console.log(template.category); // → "Authorization"

// Reference Files
const principle = pmoskills.getReferenceFile('reference/principles/P01-stewardship.md');
console.log(principle.title); // → "Be a Diligent, Respectful, and Caring Steward"

// Shared Validators & Checklists
const validator = pmoskills.getSharedFile('shared/validate_structure.py');

// Compliance Test Scenarios
const testSuite = pmoskills.getTestFile('ST-SKL-01-01');

// System Prompts & Ontology
const orchestrator = pmoskills.getSystemPrompt('pmo-orchestrator');
const ontology = pmoskills.getOntology();

// Dynamic Prompt Template Injection
const output = inject(skill.prompt, {
  projectName:        'Apex Initiative',
  authorityThreshold: '$100,000'
});
```

---

### 4. ✅ 100% Test Coverage

The Vitest unit test suite was expanded to **18 tests** covering all 7 corpus collections:

```
 ✓ PMOSkills SDK Test Suite (18)
   ✓ Executable Skills (3)
   ✓ Process Records (2)
   ✓ System Prompts and Ontology (2)
   ✓ Artifact Templates (2)
   ✓ Reference Files (2)
   ✓ Shared Assets (2)
   ✓ Compliance and Skill Tests (2)
   ✓ Prompt Template Injector (3)

 Tests  18 passed (18) — Duration: 1.05s
```

Repository structural validator also confirmed **100% schema compliance** with zero regressions.

---

### 5. 🔧 Build System Fixes

* Fixed Rollup configuration to use `module: 'ESNext'` and `moduleResolution: 'Node'` in the TypeScript plugin — enabling full tree-shaking and inlining of the 2.7MB JSON corpus into a single self-contained bundle.
* Added `"type": "module"` hint to eliminate Rollup module-type warnings.

---

## 🚀 How to Get Started in v0.4

### Option A — Use the NPM Package (Programmatic)

```bash
npm install pmoskills
```

```typescript
import { pmoskills } from 'pmoskills';

const skills = pmoskills.getSkills();     // 48 executable skills
const artifacts = pmoskills.getArtifacts(); // 92 templates
```

### Option B — Use the Repository Directly (Markdown / AI Agents)

1. Review **[`README.md`](README.md)** for the full 361+ verified asset inventory.
2. Access **[`docs/user-friendly-guide.md`](docs/user-friendly-guide.md)** to select your practitioner or AI agent execution pathway.
3. Consult **[`SKILL-REGISTRY.md`](SKILL-REGISTRY.md)** as your master API index.

---

## ⚖️ License & Maintainer

* **License:** MIT License
* **NPM Package:** [`pmoskills`](https://www.npmjs.com/package/pmoskills)
* **Framework Authority:** PMBOK 8 Core Standard & PMO Governance Board
* **Repository:** [fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
* **Lead Architect:** **Mohamed Fouad Fakhruldeen** (Website: [fakhruldeen.me](https://fakhruldeen.me) | LinkedIn: [in/fakhruldeen](https://www.linkedin.com/in/fakhruldeen))

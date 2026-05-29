# SKL-03-11 — Perform Risk Analysis

**Skill ID:** SKL-03-11  
**Pack:** 03 — Planning  
**Version:** 1.0.0-draft  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/03-planning/SKL-03-11-perform-risk-analysis.md`  
**Authority:** PMBOK8 Guide §2.7.2.3 · Figure 2-50 · §2.7.1 Key Concepts · Figure 5-14 (P×I Matrix with Scoring) · Tools and Techniques §5 · A19 Risk Management Record · A20 Quantitative Risk and Reserve Decision Record (Artifacts-V-1.0.5)  
**Last Updated:** 2026-05-29

---

## 1. Purpose

Perform Risk Analysis evaluates every risk entry in the A19 Risk Register to determine **priority** (which risks deserve response effort) and **exposure** (the aggregate effect of uncertainty on project objectives). The process outputs are the scored, ranked, and banded A19 Risk Register and — when the project context justifies quantitative work — a populated A20 Quantitative Risk and Reserve Decision Record that supports reserve sizing.

Without this skill, the A19 register is a list of named threats and opportunities with no indication of which deserve immediate attention. SKL-03-12 (Plan Risk Responses) cannot allocate response effort or design strategies without the priority ranking this skill produces.

This skill runs **iteratively** — every re-run of SKL-03-10 (Identify Risks) that adds new entries, every phase gate, and every material re-assessment cycle triggers a partial or full re-run of this skill against the affected entries.

---

## 2. Scope

This skill covers:
- Qualitative risk analysis: assessing probability and impact for every A19 entry and computing a risk score using the A19 P×I matrix
- Banding every entry into its threshold band (Very High / High / Medium / Low / Watch-only)
- Identifying urgent risks and risks with data-quality limitations
- Risk categorization and correlation analysis (shared root causes, cascade chains)
- Assessing overall project risk — the aggregate exposure — distinct from individual risk scores
- Deciding the **trigger condition** for quantitative risk analysis (QRA)
- Quantitative risk analysis (when triggered): Expected Monetary Value (EMV), sensitivity analysis / tornado diagram, simulation (Monte Carlo)
- Producing a preliminary reserve sizing recommendation for A20 (when QRA is performed)
- Updating A19 with all scored, ranked, and status-updated entries

This skill does **not** cover:
- Writing risk responses or assigning response owners (SKL-03-12)
- Formally approving or sizing contingency reserves (A16 — done in coordination with SKL-03-12 and the Finance domain)
- Identifying new risks (SKL-03-10)
- Implementing responses (SKL-04-Implement Risk Responses)
- Ongoing risk monitoring (SKL-05-Monitor Risks)

---

## 3. PMBOK8 Anchor

| Field | Value |
|-------|-------|
| **Process** | Perform Risk Analysis |
| **Guide Section** | §2.7.2.3 |
| **Figure** | Figure 2-50 — Perform Risk Analysis Inputs, Tools and Techniques, and Outputs |
| **P×I Matrix Figure** | Figure 5-14 — Example Probability and Impact Matrix With Scoring Scheme |
| **Tornado Diagram Figure** | Figure 5-21 — Example Tornado Diagram |
| **Monte Carlo Figure** | Figure 5-22 — Example Probability Distribution of a Target Milestone |
| **Performance Domain** | Risk · Finance · Governance |
| **Focus Area** | Planning (initial run); iterative throughout Executing and Monitoring and Controlling |
| **Domain Key Concepts** | Risk appetite · Risk threshold · Risk exposure · Individual risk vs. overall project risk · Qualitative vs. quantitative analysis · Sensitivity analysis · Reserve analysis (PMBOK8 Guide §2.7.1) |
| **Domain Check Results** | PMBOK8 Guide Table 2-11 |
| **Secondary Authority** | Risk-PPP (PMI Practice Standard for Project Risk Management) |

**PMI Definition (paraphrased — not reproduced):** Perform Risk Analysis involves an iterative process combining qualitative and quantitative risk analysis. Qualitative analysis evaluates individual risks by assessing probability of occurrence and impact throughout the project. Quantitative analysis, when required, assesses the combined effect of identified risks and other uncertainty sources on overall project objectives (PMBOK8 Guide §2.7.2.3).

---

## 4. Two-Track Model: Qualitative and Quantitative

PMBOK8 treats risk analysis as a **combined iterative process** that may involve qualitative analysis alone or qualitative plus quantitative analysis depending on context [file:22]. This skill uses a two-track model:

| Track | When Used | Primary Output | Feeds |
|-------|-----------|---------------|-------|
| **Track 1 — Qualitative Only** | All projects, every analysis run | Scored and ranked A19 register; threshold band assignments; overall risk assessment | SKL-03-12 (Plan Risk Responses) |
| **Track 2 — Qualitative + Quantitative** | When QRA trigger conditions are met (see Section 7) | Track 1 outputs + A20 populated with EMV / Monte Carlo / reserve recommendation | A16 (Financial Management Record), A20 (Quantitative Risk and Reserve Decision Record), SKL-03-12 |

**Critical principle:** Quantitative analysis is **not always required** — PMBOK8 §2.7.2.3 explicitly states that QRA "may not always be required" [file:22]. Performing Monte Carlo or EMV worksheets when the project does not justify them violates the A20 waste test and the repository waste rule §3.1. The trigger conditions in Section 7 enforce this.

---

## 5. Individual Risk vs. Overall Project Risk

These are **two distinct analytical objects** — both must be assessed in this skill.

### 5.1 Individual Risk Assessment
Evaluates each A19 entry independently — assigns a probability, impact, and score that places the risk on the P×I matrix. The output is a ranked list of individual risks sorted by priority band.

### 5.2 Overall Project Risk Assessment
Evaluates the **aggregate effect of all uncertainty** on the project as a whole — not the sum of individual risk scores. Overall project risk may be:
- Higher than any single risk suggests (when risks are correlated or clustered in the same objective area)
- Lower than the total score sum suggests (when risks are independent and offsetting)
- A qualitative judgment at the end of this skill, stated as a band: Very Low / Low / Moderate / High / Very High

PMBOK8 §2.7.1 defines overall project risk as "the effect of uncertainty on the portfolio, program, or project as a whole" [file:22]. This overall assessment feeds the "Overall Risk Status" field in A19 and informs whether the sponsor should be notified of a potential threshold breach.

**Governance rule:** If the overall project risk assessment band reaches **Very High**, the PM must escalate to the sponsor regardless of whether any individual risk has reached that band on its own.

---

## 6. Probability × Impact Matrix (Inherited from A19)

The P×I matrix applied in this skill is the one designed and approved in SKL-03-09 and recorded in A19. This skill **applies** that matrix — it does not redesign it.

### 6.1 PMBOK8 Numeric Scoring Reference (Figure 5-14)

PMBOK8 Figure 5-14 provides the canonical example numeric scoring scheme (reproduced in structure, not verbatim) [file:22]:

| Probability | Very High (0.90) | High (0.70) | Medium (0.50) | Low (0.30) | Very Low (0.10) |
|-------------|-----------------|-------------|--------------|-----------|----------------|
| **Very High Impact (0.80)** | 0.72 | 0.56 | 0.40 | 0.24 | 0.08 |
| **High Impact (0.40)** | 0.36 | 0.28 | 0.20 | 0.12 | 0.04 |
| **Moderate Impact (0.20)** | 0.18 | 0.14 | 0.10 | 0.06 | 0.02 |
| **Low Impact (0.10)** | 0.09 | 0.07 | 0.05 | 0.03 | 0.01 |
| **Very Low Impact (0.05)** | 0.05 | 0.04 | 0.03 | 0.01 | 0.00 |

*Threats score in the negative domain; opportunities score in the positive domain (symmetric mirror).*

**Note:** The actual matrix applied must be the one from A19 (defined in SKL-03-09). The PMBOK8 Figure 5-14 values are reference. If A19 uses a 3-point scale or a different scoring model, that model governs here — not the Figure 5-14 defaults.

### 6.2 Applying the Matrix: Step-by-Step

For each A19 risk entry:
1. **Assign probability** using the A19 scale definitions (Very Low / Low / Medium / High / Very High or equivalent) — use expert judgment, historical data, or probabilistic assessment
2. **Assign impact** across each relevant objective dimension (schedule, cost, scope/quality, stakeholder satisfaction, value) — record the **highest dimension score** as the primary impact score
3. **Compute risk score** = Probability × Impact (per the A19 numeric scheme)
4. **Assign threshold band** per the A19 thresholds from SKL-03-09
5. **Record urgency** — is this risk likely to materialize soon? Proximity matters even for medium-scored risks

### 6.3 Multi-Objective Impact Assessment

For risks with significant multi-dimensional impact, assess impact on each objective domain separately and record all scores. The risk's band is determined by the highest impact dimension, but the multi-dimensional view informs the response strategy in SKL-03-12.

| Objective Domain | Impact Definition (negative) | Impact Definition (positive) |
|-----------------|------------------------------|------------------------------|
| Schedule | Days or weeks of delay vs. baseline | Days or weeks of recovery potential |
| Cost | $ or % overrun vs. budget baseline | $ or % cost saving |
| Scope / Quality | Deliverables affected, acceptance criteria jeopardized | Additional value or features within approved scope |
| Stakeholder Satisfaction | Engagement disruption, trust damage, escalation likelihood | Relationship improvement, satisfaction gain |
| Value / Benefits | Benefit realization degraded or delayed | Benefit acceleration or amplification |

---

## 7. QRA Trigger Conditions

Quantitative risk analysis (Track 2) is triggered when **any of the following conditions** are confirmed:

| Trigger | Rationale |
|---------|-----------|
| **Budget > organizational QRA threshold** | High financial exposure justifies numerical precision |
| **Multiple Very High or High individual risks** | Combined exposure may exceed individual scores — Monte Carlo reveals the aggregate |
| **Fixed-price or fixed-date contract** | Schedule/cost distribution analysis supports credible commitment defense |
| **Sponsor or governing body explicitly requires QRA** | Governance mandate overrides project-size heuristics |
| **Reserve sizing dispute or ambiguity** | EMV or Monte Carlo provides evidence for reserve negotiation |
| **Significant schedule/cost uncertainty on critical path activities** | Sensitivity analysis identifies which uncertainty sources drive project outcome variability |
| **Regulatory or audit requirement** | Compliance environment mandates quantitative justification |

**If no trigger is met:** Record the rationale in A19 analysis run notes. Proceed with Track 1 only. Do not create an A20 entry — the waste rule §3.1 applies.

---

## 8. Inputs

### 8.1 Required Inputs

| Input | Source | What the Skill Uses It For |
|-------|--------|---------------------------|
| **A19 — Risk Register section (all entries)** | SKL-03-10 (complete) | All identified risks with C–E–C statements, RBS categories, knowledge classification, owners, and trigger indicators — the analysis subject |
| **A19 — Risk Management Plan section** | SKL-03-09 (approved) | P×I matrix, scale definitions, threshold bands, risk appetite statement, QRA decision criteria — the governing analysis framework |
| **A04 — Project Charter** | SKL-02-01 | Objective baselines against which impact is calibrated |
| **A05 — Context Register** | SKL-02-01 | OPAs, historical data, and lessons learned that inform probability assessments |

### 8.2 Supporting Inputs (use if available)

| Input | Source | What the Skill Uses It For |
|-------|--------|---------------------------|
| **A15 — Schedule Model** | SKL-03-06b | Activity durations and dependencies — mandatory for schedule Monte Carlo; required for sensitivity analysis on critical path |
| **A16 — Financial Management Record** | SKL-03-13 | Cost estimates — mandatory for cost Monte Carlo and EMV |
| **A08 — Scope and Requirements Decision Record** | SKL-03-02/03 | Scope assumptions feeding impact assessments |
| **A18 — Issue, Impediment, and Action Log** | Ongoing | Confirms current issues are not double-counted as risks |
| **Stakeholder register (A07)** | SKL-02-02 | Stakeholder risk tolerance insights that calibrate impact definitions |

---

## 9. Tools and Techniques

*Per PMBOK8 Figure 2-50.*

### 9.1 Expert Judgment
Used to calibrate probability and impact assessments — particularly for risks where no historical data exists. The same experts who participated in SKL-03-10 identification sessions are the primary source. Expert judgment must also be applied as a cross-check on QRA model assumptions.

**Anchor bias warning:** Experts tend to anchor on recent events. For each expert assessment, require the expert to articulate their reasoning — not just provide a number. Reasoning quality is a data-quality indicator.

### 9.2 Data Gathering — Interviews
Structured expert interviews to elicit probability and impact ratings. Conduct individually (not in groups) to avoid anchoring and herding. Protocol:
- Present the C–E–C statement
- Ask for a probability rating with reasoning
- Ask for impact ratings per objective dimension with reasoning
- Ask: "Is this risk urgent — could it materialize in the next [planning horizon]?"
- Ask: "Are there other risks in the register that share a root cause with this one?"

Record reasoning alongside each rating in the A19 entry. The reasoning is evidence that the rating is not arbitrary.

### 9.3 Risk Probability and Impact Assessment
The core qualitative analysis technique. Per PMBOK8 §5 (Tools and Techniques): probability and impact are assessed for each individual risk using the A19 scale definitions [file:22]. Both probability and impact assessments consider the risk's effect on individual project objectives (schedule, cost, quality, scope, stakeholder satisfaction).

**Consensus approach (for contested ratings):** When expert opinions diverge significantly, document the range, use the most conservative (highest-impact) rating for priority banding, and record the divergence as a data-quality flag.

### 9.4 Probability and Impact Matrix
Applies the A19 P×I matrix to compute a risk score for each entry. The resulting matrix view shows the distribution of risks across priority bands and visually reveals concentration in any particular band or RBS category.

**Opportunity scoring note:** Opportunities use the positive mirror of the P×I matrix — higher probability and positive impact scores indicate higher opportunity priority. Opportunity banding uses the same band labels (Very High / High / Medium / Low) with a "+" qualifier to distinguish from threats.

### 9.5 Risk Categorization
Groups risks by RBS category, shared root cause, affected WBS area, or related objective to identify concentrations and correlations. Key outputs:
- **Category clusters:** RBS categories with disproportionate numbers of High/Very High risks signal a domain exposure requiring a programmatic response
- **Root cause groups:** Multiple risks sharing one root cause may be addressed with a single response in SKL-03-12 (more efficient than N separate responses)
- **Cascade chains:** Where one risk materializing increases the probability of a second risk — document the cascade and treat both together

### 9.6 Data Analysis — Sensitivity Analysis
Identifies which individual risks or uncertainty sources have the greatest potential impact on project outcomes. The standard display is a **tornado diagram** — risks listed in descending order of correlation with the primary project outcome variable (usually total project duration or total cost).

**When to use:** Required when QRA is triggered and when multiple high-scoring risks affect the same critical path activities. Optional but recommended for any project with a High overall risk band.

**Tornado diagram construction:**
- Identify the key project outcome variable (e.g., total project cost, project finish date)
- For each High/Very High risk: estimate the outcome range if the risk occurs at its upper bound, lower bound, and expected value
- Sort risks by the width of their impact range (widest = most sensitive)
- Present as horizontal bars ordered widest-to-narrowest
- The top 3–5 risks on the tornado are the **critical risks** for response planning in SKL-03-12

### 9.7 Data Analysis — Decision Tree Analysis (EMV)
Used when decisions with probabilistic outcomes must be evaluated. The primary application in this skill is **Expected Monetary Value (EMV)** — a quantitative technique that estimates the financial exposure of a risk or set of risks.

**EMV Formula:**

\[ EMV = P 	imes I \]

where \(P\) is probability (expressed as a decimal, e.g., 0.30) and \(I\) is the monetary impact if the event occurs (positive for opportunities, negative for threats).

**Portfolio EMV (for reserve sizing input):**

\[ EMV_{total} = \sum_{i=1}^{n} P_i 	imes I_i \]

where the sum runs across all identified risks.

**Practical rules:**
- Negative EMV values (threats) represent expected cost exposure; they sum to a preliminary contingency reserve estimate
- Positive EMV values (opportunities) represent expected cost recovery potential; they may offset the reserve need
- Net portfolio EMV (threats minus opportunities) is a lower-bound input to A20 reserve sizing
- EMV does not capture correlation effects — it assumes risk independence. When risks are correlated, Monte Carlo is required for an accurate portfolio estimate.

### 9.8 Data Analysis — Simulations (Monte Carlo)
Models the combined effect of individual risks and estimate uncertainty ranges on the total project schedule or cost. Monte Carlo applies probability distributions (not single-point estimates) to activity durations and costs, then runs thousands of simulated project outcomes to produce a probability distribution of the project finish date or total cost.

**Per PMBOK8 Figure 5-22:** The output is a cumulative probability curve showing the probability of achieving a specific outcome value (e.g., 80% probability of finishing by a given date) [file:22].

**When required:** A15 (schedule model) is mandatory for schedule Monte Carlo. A16 (cost estimates with ranges) is mandatory for cost Monte Carlo. If neither is available, Monte Carlo cannot run — record this as a trigger deferral.

**Reading the output:**
- **P50 value:** 50% probability of being at or below this outcome — represents the most-likely scenario
- **P80 value:** 80% probability — common basis for contingency reserve sizing
- **P90 value:** 90% probability — used for high-risk-appetite environments or contractual commitments
- **P50 to P80 gap:** The contingency reserve sizing range — represents the additional time or cost needed to move from the most-likely scenario to an 80% confidence level

**A20 input:** The P50–P80 gap (or P80–P90 if the governance context requires higher confidence) is the primary quantitative input to the A20 reserve recommendation.

### 9.9 Data Representation — Influence Diagrams
Graphical representation of causal relationships and uncertainties among project variables. Used when risks have complex interdependencies that are not visible in a linear risk list. Particularly useful for identifying cascade chains and feedback loops that would distort independent-risk analyses.

**When to use:** Complex technical projects where a risk event in one domain has second-order effects in other domains. Not required for most projects.

### 9.10 Interpersonal and Team Skills — Facilitation
The PM or risk lead facilitates the analysis session in a way that:
- Separates probability and impact discussions to prevent conflation
- Challenges unreasonably high or low ratings with reasoning prompts
- Ensures opportunities receive the same analytical rigor as threats
- Manages anchor bias by presenting risks in shuffled order during group review

---

## 10. Step-by-Step Instructions

### Step 1 — Confirm Prerequisites (Gate)

Before analysis begins, verify:
- [ ] SKL-03-10 complete: A19 Risk Register section has at least one fully populated entry
- [ ] All entries have C–E–C statements (T-3 from SKL-03-10 passes)
- [ ] All entries have RBS categories and named risk owners
- [ ] A19 Risk Management Plan section (from SKL-03-09) contains the approved P×I matrix, scale definitions, and threshold bands
- [ ] Probability and impact fields in all A19 entries are blank (status: "Identified — Awaiting Analysis")

**If entries lack C–E–C statements or RBS categories:** Return to SKL-03-10 for remediation before proceeding. Analysis of malformed entries produces unreliable priority rankings.

### Step 2 — Retrieve Analysis Inputs

Pull:
- All A19 risk entries (full list)
- A19 Risk Management Plan section (P×I matrix, thresholds, scale definitions, risk appetite statement)
- A04 Project Charter (objective baselines for impact calibration)
- A05 Context Register (OPAs, historical probability data)
- A15, A16, A08 if available (for impact calibration and QRA pre-check)

Review A19 for any entries previously analyzed (in a re-run context). For re-runs, focus on:
- New entries added since the last run (status: "Identified — Awaiting Analysis")
- Existing entries where a re-assessment trigger has been noted by the risk owner

### Step 3 — Check QRA Trigger Conditions

Review the trigger conditions in Section 7 against the current project context. Document the outcome in A19 analysis run notes:
- **Track 1 only:** Record which trigger conditions were evaluated and why none were met; confirm no A20 entry will be created for this run
- **Track 1 + Track 2:** Record which trigger condition is met; note that A20 will be opened or updated after qualitative analysis is complete

### Step 4 — Conduct Probability and Impact Assessment (Qualitative — Track 1)

For each A19 entry with status "Identified — Awaiting Analysis":

1. **Probability assessment:** Interview relevant risk owners and domain experts. Assign a probability band from the A19 scale. Record the probability value and the reasoning in the A19 entry.

2. **Impact assessment:** Assess impact across all relevant objective dimensions (schedule, cost, scope/quality, stakeholders, value). Record all dimension scores. Assign the primary impact band as the highest-scoring dimension.

3. **Urgency assessment:** Assess how soon the risk could materialize. A risk scheduled to materialize in the next 2 weeks is urgent regardless of its probability-impact score. Record urgency as: Immediate / Near-term / Distant.

4. **Data quality assessment:** Rate the confidence in the probability and impact assessment: High (multiple expert sources, historical precedent) / Medium (single expert source or limited precedent) / Low (intuitive judgment, no data). Record in A19. Low-confidence ratings trigger a watch-list flag.

5. **Score computation:** Risk Score = Probability × Impact (per A19 numeric scheme). Record the score in the A19 probability, impact, and score fields.

### Step 5 — Assign Threshold Bands

Using the threshold bands from A19 (established in SKL-03-09), assign each entry to its band:
- **Very High:** Escalate immediately; sponsor awareness required; priority response
- **High:** PM acts; active response planning required in SKL-03-12
- **Medium:** Watch and control; response planned but may be passive
- **Low:** Accept; monitor at standard cadence
- **Watch-only:** Score below Low threshold; documented and reviewed periodically but no active response

Update the A19 entry Status field:
- Very High / High: "Analysis Complete — Response Required"
- Medium: "Analysis Complete — Watch and Plan"
- Low / Watch-only: "Analysis Complete — Accept / Monitor"

### Step 6 — Conduct Risk Categorization Analysis

After all entries are scored:

1. **Group by RBS category:** Count threats and opportunities per category. Identify categories with disproportionate Very High/High concentrations — these signal domain-level exposure.

2. **Group by root cause:** Identify clusters of risks sharing a root cause. Document these clusters in the A19 analysis run notes. Flag them for consolidated response design in SKL-03-12.

3. **Identify cascade chains:** For each Very High or High threat, ask: "If this risk occurs, which other register entries become more likely?" Document confirmed cascades in the A19 entry notes.

4. **Identify opportunity clusters:** Group opportunities that share enabling conditions — these may be jointly exploited in SKL-03-12 with a single enhancement strategy.

### Step 7 — Assess Overall Project Risk

After individual entries are scored and categorized, assess the **overall project risk** — the aggregate effect of all uncertainty on the project as a whole.

Factors to consider:
- Number and distribution of Very High/High entries
- Presence of cascade chains or correlated clusters
- Whether multiple risks target the same critical path activities
- Whether the combined scope of uncertainty could threaten project viability
- Whether any individual risk, if it materialized, could breach the project's risk thresholds (per A19 appetite statement)

**Overall risk band assignment:** Very Low / Low / Moderate / High / Very High.

Update A19 header: "Overall Project Risk Assessment: [Band] as of [Date]."

**Escalation rule:** If Overall = High or Very High, notify the sponsor and relevant governance forum immediately per the A19 escalation threshold. Do not wait for SKL-03-12 to begin. Record the escalation in A12 (Change and Exception Decision Log).

### Step 8 — Conduct Sensitivity Analysis (if Track 2 or if High overall band)

If QRA is triggered or if the overall project risk band is High or Very High:

1. Identify the primary outcome variable (project finish date, total cost, or both)
2. For each Very High and High risk: estimate the range of impact on the outcome variable (optimistic, most likely, pessimistic)
3. Calculate the correlation of each risk's range with the outcome variable
4. Construct the tornado diagram: rank risks by descending absolute correlation
5. Identify the top 3–5 risks on the tornado as **critical risks** — flag them in A19 with the "Critical (Sensitivity)" tag
6. Record the tornado in A20 (if Track 2) or as an attachment reference in A19 (if Track 1 with High overall)

### Step 9 — Conduct EMV Analysis (if Track 2)

For each monetized Very High and High entry:
1. Confirm the monetary impact value (from A16 or A08 — if unavailable, estimate with documented assumptions)
2. Calculate EMV per entry: \( EMV = P 	imes I \)
3. Sum all negative EMV values (threats) to get the **total threat exposure**
4. Sum all positive EMV values (opportunities) to get the **total opportunity value**
5. Compute net EMV: total threat exposure minus total opportunity value
6. Document in A20 as the EMV-based reserve sizing input

### Step 10 — Conduct Monte Carlo Simulation (if Track 2 and if A15/A16 available)

1. Confirm A15 (Schedule Model) is available with activity duration estimates and ranges
2. Confirm A16 (Financial Management Record) has cost estimate ranges
3. Configure the simulation model: apply three-point estimates (optimistic, most likely, pessimistic) to activities and costs; incorporate Very High/High risk events as discrete risk distributions
4. Run the simulation (minimum 1,000 iterations; 10,000+ preferred for stable output)
5. Read the cumulative probability distribution:
   - P50: most likely project finish date and total cost
   - P80: 80th percentile finish date and total cost
   - Contingency reserve input: P80 minus P50 (for time and cost separately)
6. Document methodology, key input assumptions, P50/P80/P90 values, and the reserve recommendation in A20

### Step 11 — Produce A20 Decision Record (if Track 2)

Populate the A20 Quantitative Risk and Reserve Decision Record with:

| A20 Field | Content |
|-----------|---------|
| Analysis method | EMV / Monte Carlo / sensitivity analysis (check all used) |
| Scenarios assessed | Optimistic, most likely, pessimistic for key entries |
| Quantified exposure | Total threat EMV; total opportunity EMV; net EMV |
| Monte Carlo results | P50, P80, P90 values for schedule and cost (if run) |
| Reserve recommendation | Contingency reserve: P80 minus P50 gap (or net EMV if Monte Carlo not run); management reserve basis (% of cost baseline or explicit estimate) |
| Assumptions | All input assumptions that materially affect the output |
| Decision requested | Sponsor/finance authority: approve recommended contingency reserve level |

**Approval chain:** A20 is reviewed by the sponsor and/or finance authority per the A20 approval authority field. The PM does not self-approve reserve levels.

### Step 12 — Produce Risk Priority Output (A19 Update)

Update A19 to reflect the complete analysis run:

| A19 Field Updated | Content |
|------------------|---------|
| Probability | Assigned value (e.g., 0.70) |
| Impact | Assigned value (e.g., 0.40) — highest dimension |
| Risk score | Computed P × I value (e.g., 0.28) |
| Priority band | Very High / High / Medium / Low / Watch-only |
| Urgency | Immediate / Near-term / Distant |
| Data quality | High / Medium / Low (with reasoning) |
| Status | "Analysis Complete — Response Required" / "Watch and Plan" / "Accept / Monitor" |
| Analysis date | Today's date |
| Cascade flags | If cascades were identified, reference the linked entries |
| Critical (Sensitivity) | Flag if in top tornado tier |

Update A19 header with:
- Overall Project Risk Assessment band
- Date of this analysis run
- Analysis techniques used
- Number of Very High, High, Medium, Low, and Watch-only entries
- Trigger decision for QRA (Track 1 or Track 2) with rationale

### Step 13 — Trigger Downstream

Hand off to SKL-03-12 (Plan Risk Responses): "A19 Risk Register is fully scored, banded, and ranked. [N] entries are Analysis Complete — Response Required (Very High: X, High: Y). Overall project risk is [Band]. [If Track 2: A20 has been prepared and is awaiting approval from [Authority].]"

---

## 11. Outputs

| Output | Artifact | Section/Field Updated |
|--------|---------|----------------------|
| **Scored and ranked risk register** | A19 — Risk Management Record | All risk register fields: probability, impact, score, band, urgency, data quality, status, cascade flags, sensitivity tags |
| **Overall project risk assessment** | A19 — Risk Management Record | A19 header: overall risk band, analysis date, technique summary |
| **Quantitative analysis decision record** | A20 — Quantitative Risk and Reserve Decision Record | All A20 fields (only when Track 2 is triggered) |
| **Assumption log updates** | A05 — Context Register | New assumptions discovered during probability/impact assessment that should be tracked |

---

## 12. Tailoring Guidance

| Dimension | Guidance |
|-----------|---------|
| **Small / low-complexity project** | Track 1 only; 3-point scale (High / Medium / Low) is sufficient; one analysis session; qualitative overall assessment; no A20 required |
| **Medium project** | Track 1 with 5-point scale; sensitivity analysis recommended if multiple High entries; EMV for reserve input if no Monte Carlo |
| **Large / high-complexity project** | Full Track 1 + Track 2; Monte Carlo for both schedule and cost; formal tornado diagram; dedicated A20 requiring sponsor approval |
| **Adaptive project (sprint-based)** | Qualitative analysis at sprint planning using the simplified 3-point matrix; no Monte Carlo per sprint; cumulative trend monitored in A19 over iterations |
| **Fixed-price contract** | QRA (Track 2) is strongly recommended regardless of project size — EMV or Monte Carlo supports credible reserve and bid justification |
| **Regulated environment** | Document analysis methodology in full for audit; any QRA models and assumptions must be traceable and reproducible |
| **Re-run (mid-project)** | Only re-analyze entries that have changed status since the last run (new entries + re-triggered existing entries); update A19 header with current overall risk band; update A20 if reserve assumptions have shifted materially |

---

## 13. Failure Cases

| Failure Mode | Consequence | Prevention |
|-------------|-------------|-----------|
| Analysis run without approved P×I matrix from A19 | Scores are ungoverned; no band thresholds to apply; register is unactionable | Test T-1 gate enforces prerequisite |
| Assigning probability without reasoning | Scores are arbitrary; anchoring bias corrupts the priority ranking; SKL-03-12 misallocates response effort | Test T-3 requires reasoning for each rating |
| Treating threats and opportunities asymmetrically (scoring threats but not opportunities) | Opportunities are not prioritized; no exploitation strategy enters SKL-03-12 | Test T-4 checks opportunity scoring completeness |
| Skipping overall project risk assessment | Governance has no aggregate view; sponsor cannot make an informed threshold decision | Test T-5 checks overall band is recorded |
| Running Track 2 (QRA) without trigger justification | Wasted analytical effort; A20 waste test fails; repository noise; §3.1 violated | Test T-6 requires documented trigger |
| Running Monte Carlo without A15 or A16 | Simulation inputs are fabricated; outputs are unreliable; reserve recommendations are unsupported | Test T-7 checks input artifact availability before simulation |
| Using analysis scores to re-write C–E–C statements | Risk identity conflated with risk score; subsequent re-run loses the baseline statement for comparison | Never modify the C–E–C statement during analysis; scoring is a separate field |
| Separate analysis spreadsheet created outside A19 | Dual maintenance; A19 becomes stale; waste rule §3.2 violated | Test T-8 enforces single-artifact rule |

---

## 14. Tests

### T-1 — Prerequisite Gate

**Assertion:** SKL-03-11 cannot begin until the A19 Risk Register has at least one fully populated entry from SKL-03-10, and the A19 Risk Management Plan section contains an approved P×I matrix with threshold bands.

**Pass condition:** Both prerequisites confirmed before the first analysis rating is assigned.

**Fail condition:** Analysis begins with empty probability fields but no confirmed P×I matrix — the analyst is improvising the scoring framework.

**Test type:** Pre-execution gate (block)

---

### T-2 — All A19 Entries Scored

**Assertion:** After this skill runs, every A19 entry has non-blank values in the probability, impact, risk score, priority band, urgency, data quality, and status fields.

**Pass condition:** Zero blank analysis fields in the A19 risk register.

**Fail condition:** Any entry still has "Awaiting Analysis" status or blank probability/impact/score fields.

**Test type:** Field completeness check

---

### T-3 — Reasoning Documented for Each Rating

**Assertion:** Every probability and impact rating in A19 has a reasoning note — not just a numeric value.

**Pass condition:** Each entry has at least one sentence in the analysis notes field explaining why the probability and impact values were assigned.

**Fail condition:** Any entry has a score with no reasoning. A score with no reasoning is equivalent to a guess — it cannot be challenged, updated, or used as evidence.

**Test type:** Content quality check — applied per entry

---

### T-4 — Opportunities Scored on the Positive Matrix

**Assertion:** All A19 entries with Risk Type = "Opportunity" have been scored using the positive (opportunity) domain of the P×I matrix and have been assigned a positive band label.

**Pass condition:** All opportunities have opportunity-domain scores and bands. Their urgency and status fields are populated.

**Fail condition:** Opportunities exist in A19 with blank scores or "Awaiting Analysis" status after this skill runs.

**Test type:** Coverage check for opportunity parity

---

### T-5 — Overall Project Risk Band Recorded

**Assertion:** The A19 header contains an "Overall Project Risk Assessment" band entry, a date, and a brief rationale for the band assignment.

**Pass condition:** Band is one of Very Low / Low / Moderate / High / Very High; date is the analysis run date; rationale references specific register characteristics (e.g., "4 Very High entries, 2 cascade chains targeting critical path").

**Fail condition:** No overall risk band entry; or band is "TBD" without a note.

**Test type:** Completeness check on A19 header

---

### T-6 — QRA Trigger Decision Documented

**Assertion:** The A19 analysis run notes contain a documented QRA trigger decision — either which trigger condition was met (Track 2) or a statement that no trigger was met (Track 1 only), with rationale for each trigger condition reviewed.

**Pass condition:** Clear, traceable trigger decision in A19; if Track 2, A20 is opened or updated; if Track 1, no A20 entry is created.

**Fail condition:** QRA was performed but no trigger was documented; or A20 was created without a trigger; or a clear trigger existed but QRA was skipped without rationale.

**Test type:** Governance decision check

---

### T-7 — Monte Carlo Only Runs with A15 and A16 Available

**Assertion:** If Monte Carlo simulation is included in Track 2, both A15 (Schedule Model) and A16 (Financial Management Record) with estimate ranges exist as confirmed inputs.

**Pass condition:** A15 reference and A16 reference are cited in the A20 simulation input assumptions section.

**Fail condition:** A Monte Carlo was run but A15 or A16 is missing, unavailable, or references only single-point estimates — the simulation is mathematically underdetermined.

**Test type:** Input availability check (pre-simulation gate)

---

### T-8 — No Separate Analysis Spreadsheet

**Assertion:** No standalone risk scoring spreadsheet, risk matrix workbook, or QRA Excel file exists as a separate artifact. All analysis data lives in A19 (qualitative) and A20 (quantitative, if applicable).

**Pass condition:** Post-skill review finds no separate analysis artifact. Working-session files that were used as scratch pads are either deleted or embedded as A20 appendices — not maintained as independent living documents.

**Fail condition:** A "Risk Analysis.xlsx" or equivalent standalone file exists alongside A19 with fields that overlap the A19 risk register. Waste rule §3.2 is violated.

**Test type:** Artifact waste check

---

### T-9 — Escalation Triggered for High/Very High Overall

**Assertion:** If the overall project risk assessment band is High or Very High, a sponsor escalation notification has been sent and recorded in A12 (Change and Exception Decision Log) before SKL-03-12 begins.

**Pass condition:** A12 contains an entry logging the escalation event, the overall risk band, and the sponsor acknowledgment (or pending acknowledgment).

**Fail condition:** Overall band is High or Very High but no A12 entry exists; sponsor has not been notified; SKL-03-12 is proceeding without sponsor awareness of aggregate risk status.

**Test type:** Governance escalation check

---

## 15. Dependency Chain

```
UPSTREAM (must complete before SKL-03-11)
─────────────────────────────────────────
SKL-03-10 → A19 Risk Register populated            [mandatory gate — Test T-1]
SKL-03-09 → A19 Risk Management Plan section        [mandatory gate — P×I matrix]
SKL-02-01 → A04, A05                                [mandatory for calibration]
A15, A16, A08                                        [mandatory only for Track 2 simulation]

DOWNSTREAM (cannot start until SKL-03-11 produces scored A19 register)
──────────────────────────────────────────────────────────────────────
SKL-03-12 — Plan Risk Responses
  ├── Reads: priority band (Very High / High → response required)
  ├── Reads: cascade flags (combined response design)
  ├── Reads: critical (sensitivity) tags (tornado-top risks → priority strategies)
  ├── Reads: urgency field (time-sensitive responses first)
  └── Reads: A20 reserve recommendation (if Track 2 completed)
       └──▶ A16 Financial Management Record (reserve sizing confirmation)

ITERATIVE RE-ANALYSIS TRIGGERS:
SKL-03-10 re-run (new entries added) → re-run SKL-03-11 on new + re-triggered entries
Phase gate review → full re-run SKL-03-11
Major scope/schedule/cost change → partial re-run SKL-03-11 for affected entries
Risk owner trigger signal → re-run SKL-03-11 for that entry
```

---

## 16. Examples

### Example A — Small Predictive Project (Office Relocation, 3 months)

**Analysis approach:** Track 1 only; 3-point scale (High / Medium / Low); single 1-hour analysis session with PM and logistics lead.

**Sample scored entries:**

| Risk ID | Type | P | I | Score | Band | Urgency | Status |
|---------|------|---|---|-------|------|---------|--------|
| R-001 | Threat | High (0.50) | High (0.40) | 0.20 | High | Near-term | Response Required |
| R-002 | Threat | Medium (0.30) | Medium (0.20) | 0.06 | Low | Distant | Accept / Monitor |
| R-003 | Opportunity | Medium (0.50) | Medium (0.20) | 0.10 | Medium+ | Near-term | Watch and Plan |

**Overall Project Risk Assessment:** Low — 1 High entry, no cascade chains, 3-month timeline, no critical path dependency concentration.

**QRA decision:** No trigger conditions met. Track 1 only. No A20 created.

---

### Example B — Adaptive Software Project (Scrum, Sprint 1)

**Analysis approach:** Track 1; 3-point scale embedded in sprint planning; 20-minute analysis session.

**Per-sprint process:**
- Score new entries at the beginning of each sprint analysis
- Re-assess any entry whose urgency escalated (e.g., trigger indicator observed)
- Update overall project risk band in A19 header for the sprint

**Sprint 1 scored entries:**

| Risk ID | Type | P | I | Score | Band | Urgency | Status |
|---------|------|---|---|-------|------|---------|--------|
| R-001 | Threat | High (0.70) | High (0.40) | 0.28 | High | Immediate | Response Required |
| R-002 | Threat | Medium (0.50) | Medium (0.20) | 0.10 | Medium | Near-term | Watch and Plan |
| R-003 | Opportunity | Medium (0.50) | Low (0.10) | 0.05 | Low+ | Near-term | Accept / Monitor |

**Overall Project Risk Assessment:** Moderate — 1 High (immediate urgency).

**QRA decision:** No trigger. R-001 is high urgency; sprint response planning in SKL-03-12 will address it immediately.

---

### Example C — Large Infrastructure Project (24 months, $12M)

**Analysis approach:** Track 1 + Track 2; 5-point numeric matrix; two-day analysis workshop + specialist QRA session using schedule and cost models.

**Analysis outputs:**

- **Individual risk scoring:** 67 entries scored; distribution: Very High: 4, High: 14, Medium: 23, Low: 18, Watch-only: 8
- **Overall Project Risk Assessment:** High — 4 Very High entries, 2 cascade chains on critical path activities, High concentration in Technical RBS category
- **Sensitivity analysis (tornado diagram):** Top 5 critical risks identified; Risk 5.2 (DCS installation failure) has the highest correlation with project finish date
- **Sponsor escalation:** Logged in A12 per Test T-9

**Track 2 outputs (A20):**

| A20 Field | Value |
|-----------|-------|
| Analysis method | Monte Carlo (schedule and cost) + EMV (all Very High/High entries) |
| Monte Carlo P50 finish | 15 May 2027 |
| Monte Carlo P80 finish | 28 May 2027 |
| Contingency reserve (schedule) | 13 days additional to P80 finish date |
| EMV — total threat exposure | –$620,000 |
| EMV — total opportunity value | +$95,000 |
| Net EMV | –$525,000 |
| Contingency reserve recommendation (cost) | $525,000 (net EMV basis, to be confirmed against P80 cost analysis) |
| Decision requested | Sponsor and Finance Authority: approve $525,000 contingency reserve in A16 |

---

## 17. Governance Layer and Threshold Band

| Field | Value |
|-------|-------|
| **Governance Layer** | Project Governance |
| **Threshold Band** | T2 — PM manages analysis process; sponsor review required when overall project risk band reaches High or Very High; A20 reserve sizing requires sponsor and/or finance authority approval |
| **Iterative nature** | Re-runs at every cadence trigger defined in A19 plan section and SKL-03-09; not a one-time planning event |

---

## 18. Primary References

| Reference | Alias | Section | Purpose |
|-----------|-------|---------|---------|
| PMBOK Guide, Eighth Edition | PMBOK8 | Guide §2.7.2.3; Figure 2-50; §2.7.1 Key Concepts; Figure 5-14; Figure 5-21; Figure 5-22; §5 Tools and Techniques | Process basis, I/T/O, P×I scoring, tornado diagram, Monte Carlo, sensitivity analysis, risk concepts |
| Artifacts-V-1.0.5 | Artifacts-V-1.0.5 | A19 Risk Management Record; A20 Quantitative Risk and Reserve Decision Record | Artifact schema, field definitions, governance layer, waste tests |
| PMI Practice Standard for Project Risk Management | Risk-PPP | Qualitative and quantitative analysis methodology | Secondary authority for analysis technique depth |
| PMI Lexicon of Project Management Terms | Lexicon | v5.0, January 2026 | Definitions: risk exposure, risk threshold, risk appetite, overall risk, EMV, sensitivity analysis |

---

*Authority: PMBOK8 · Artifacts-V-1.0.5 · Repository Operating Rules §3.1 Waste Rule · §3.2 Consolidation Rule*  
*Owner: Project Manager or designated risk lead*  
*Iterative: Re-runs at every cadence trigger defined in A19 plan section*  
*Next Skill: SKL-03-12 — Plan Risk Responses*

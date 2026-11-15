# Review rubric and output modes

Use this reference to keep reviews rigorous without making every response long.

## Argument-quality rubric

Assess the dimensions separately. Use `high`, `medium`, or `low` confidence instead of false numerical precision.

| Dimension | Strong signal | Weak signal |
| --- | --- | --- |
| Claim clarity | Specific, bounded, and falsifiable | Elastic wording or moving goalposts |
| Evidence | Relevant primary data, representative examples, transparent limits | Anecdotes, cherry-picking, citation by reputation |
| Inference | Premises justify the conclusion; alternatives are compared | Causal leap, scope drift, false dichotomy |
| Calibration | Time horizon, uncertainty, and failure conditions are explicit | Certainty theater or prediction without a resolution test |
| Counterarguments | Best objection is addressed fairly | Straw man, ignored base rate, selective skepticism |
| Decision value | Changes a choice, test, or prioritization | Interesting but operationally inert |

Do not mechanically score every claim. Apply the rubric to the claims carrying the central thesis.

## Recurring reasoning traps

- Capability-to-adoption leap: a system can do a task, therefore organizations will deploy it broadly.
- Task-to-job leap: some tasks can be automated, therefore the occupation disappears.
- Revenue-to-profit leap: demand exists, therefore the vendor has durable margins or defensibility.
- Product-to-valuation leap: the product is useful, therefore the security is attractively priced.
- Demo-to-production leap: a curated demo implies reliable operation under real constraints.
- Correlation-to-causation leap: two trends move together, therefore one caused the other.
- Anecdote-to-base-rate leap: one vivid company, customer, or failure represents the market.
- Time-horizon switch: a long-run claim is used to justify a near-term forecast, or vice versa.
- Unresolved denominator: impressive totals without users, spend, cohort, or opportunity size.
- Unpriced dependency: inference ignores integration, data quality, security, governance, or human review.

## Example topic lenses

These examples illustrate how to connect reasoning to a decision. Use only a requested or relevant lens and adapt it to the user's subject; do not treat these examples as default user interests.

### Enterprise AI

- What workflow and user are actually changing?
- Is the bottleneck model capability, data, integration, trust, procurement, governance, or change management?
- What evidence shows adoption beyond pilots and demos?
- Is value measured in revenue, cost, cycle time, quality, risk, or optionality?
- Who captures the value, and what are the implementation and inference costs?
- Are technical capability, customer value, vendor economics, and valuation being conflated?

### Forward Deployed Engineering

- What customer constraint makes generic product behavior insufficient?
- Does the proposed work create reusable product learning or permanent bespoke services?
- Which technical, stakeholder, and deployment tradeoffs must an FDE own?
- What would count as evidence of impact in production?
- Where can requirements ambiguity, data access, security, or organizational incentives break the plan?

### AI engineering job market

- Is the claim about tasks, roles, headcount, wages, hiring signals, or skill composition?
- Which geography, seniority, company type, and time horizon does the evidence cover?
- Are job postings being confused with employment, or social-media anecdotes with market data?
- Which complementary skills become more valuable as tools improve?
- What observation would distinguish displacement from productivity-driven demand?

### Prediction markets

- What exactly does the contract resolve on, by what source and date?
- Is a market price being treated as a calibrated probability without considering liquidity, fees, limits, or participant selection?
- What is the relevant base rate, and what new information should move it?
- Are forecasts evaluated against the information available at the time?
- Could ambiguous resolution criteria or correlated positions distort the apparent signal?

## Output modes

### `quick`

Keep the brief proportionate to the user's requested depth and the source material:

- decision-relevant verdict;
- central thesis in one paragraph;
- the material strengths and weaknesses with timestamp links; avoid a fixed count when fewer are supported;
- relevance to the requested topics;
- the most useful segments to watch;
- one-line transcript provenance.

Verify at most one representative claim whose result could materially change the central-thesis assessment or the watch recommendation. List other load-bearing current claims as unverified. A `quick` review may omit a separate claim map or action list when the same information is already conveyed under the strengths, weaknesses, and topic relevance sections.

### Standard review

Use when no mode is supplied:

- verdict and central thesis;
- compact claim map;
- material strengths and weaknesses supported by the source;
- up to three pivotal fact-checks;
- project implications and concrete next actions;
- recommended watch segments and provenance.

### `deep`

Add:

- speaker-by-speaker argument map;
- source-backed fact-check table;
- hidden assumptions and strongest countercase;
- what was knowable at publication versus now, if material;
- confidence by major conclusion;
- evidence that would change the assessment.

Spend depth on the load-bearing claims, not exhaustive plot summary.

### `post`

First complete at least a `quick` audit internally. Then deliver:

- one optional headline;
- a platform-appropriate post in the requested language;
- a concise source link;
- an optional shorter variant only when useful.

For a paragraph-oriented social platform, favor readable paragraphs and a human opening over a thread-like numbered list. Avoid presenting the speaker's forecast as established fact. Preserve at least one material caveat and end with a genuine question when it invites discussion.

## Recommended claim table

Use this only when it improves clarity:

| Time | Claim | Type | Evidence in video | Assessment | External check | Why it matters |
| --- | --- | --- | --- | --- | --- | --- |

Types: `fact`, `inference`, `forecast`, `value judgment`, or `anecdote`.

## Timestamp discipline

- Link to the start of the relevant claim, not a nearby chapter boundary.
- Use a range when context spans more than about a minute.
- Check at least a sample of links against the transcript or media before delivery.
- If chapters and transcript timing disagree, prefer the transcript timing and note material drift.

---
name: eval-ui-contract-builder
description: Spec-first workflow for eval-heavy or trace-heavy software projects that need non-trivial UI, dashboards, review consoles, eval browsers, trace inspectors, golden/candidate management, or demo surfaces. Use when implementing or modifying UI that displays eval results, traces, datasets, candidate packets, golden fixtures, LLM-judge outputs, human review state, telemetry, trace context, or other correctness/governance data where stale state, wrong binding, hidden mutation, or missing tests could mislead users.
---

# Eval UI Contract Builder

## Purpose

Use this skill to prevent UI work from outrunning eval architecture. The output should be a UI backed by an explicit contract, tests that lock the contract, and verification that eval/trace data is scoped to the right run, case, dataset, or fixture.

## Required Workflow

1. Inspect before editing.
   - Read existing UI files, API routes, eval runners, models/schemas, tests, and docs.
   - Run `git status --short` and check for dirty files.
   - Identify source-of-truth boundaries: strict goldens, trace-repair cases, live candidates, human review, LLM suggestions, telemetry, dataset exports.

2. Write or update a UI contract before implementation.
   - Prefer a checked-in spec such as `docs/ui-workflow-spec.md`, `docs/eval-ui-contract.md`, or a similarly local convention.
   - Include acceptance criteria with stable IDs like `AC-1`.
   - State identity keys explicitly: `run_id`, `trace_id`, `case_id`, `dataset_id`, `dataset_version_id`, `example_id`, `claim_id`, or equivalent.
   - For multi-panel review, define one immutable binding tuple shared by the
     source, normalized thesis, review focus, candidate evidence, and submitted
     decision. A panel with a different tuple is a blocking data-integrity
     error, not an empty-state fallback.
   - Define nullable choices as distinct states. In particular, `unanswered`,
     an explicit `none` verdict, and a selected candidate must not share one
     falsy UI value.
   - State which actions are allowed to mutate canonical truth and which are read-only.
   - For multi-gate flows, state exactly which surface appears after each gate; for example, advisory triage must not open a promotion/review console unless the review gate was explicitly answered yes.
   - State whether retrieved items are candidates, relevant results, reviewed evidence, or canonical truth. Do not call retrieved candidates "relevant" unless the product has actually scored or reviewed relevance.

3. Implement only after the contract exists.
   - Bind every UI panel to an explicit identity key.
   - Clear stale selections when a new run/case/dataset is loaded.
   - Permit submission of an explicit governed `none` when the contract allows
     abstention; validate presence of the choice rather than truthiness of a
     selected object ID.
   - Keep strict eval truth separate from candidate/review/triage views.
   - Make failure modes visible instead of silently falling back.
   - Do not let a user bypass required workflow gates, such as running a trace-repair rerun without trace inspection.
   - Sort ranked/scored UI rows by the displayed score, descending, unless the contract explicitly says another ordering is canonical.
   - Keep advisory scores next to the objects being scored; do not hide them on a separate review surface while showing unscored rows in the active workflow.
   - For retrieval UIs, treat irrelevant or noisy live results as a product risk. Add provider/filter tests for representative noisy cases rather than solving them only with display text.

4. Add tests that prove the contract.
   - Map each material acceptance criterion to an observable UI/API behavior and a test at the owning boundary. Checking that spec wording exists is not a behavior test.
   - Add UI/API tests for state binding and stale-state prevention.
   - Add a cross-panel mismatch test that refuses to render or submit when the
     source/thesis/review/candidate identity tuples differ.
   - Add a three-state selection test covering unanswered, explicit `none`, and
     selected-candidate submission.
   - Add fixture/eval tests proving data shown in the UI comes from the correct source.
   - Add regression tests for any bug found during manual testing.
   - Test each workflow gate's negative path: answering yes to one optional step must not open, mutate, or select another step.
   - Test display ordering when the UI renders scores, rankings, priorities, or sorted eval rows.
   - Add at least one noisy live-retrieval fixture or provider-level test when a UI depends on external retrieval quality.

5. Verify with the actual app when feasible.
   - Run unit tests and relevant eval commands.
   - Use an available, authorized browser tool for substantial frontend changes. If browser access is unavailable, report which UI behavior remains unverified.
   - Check that dynamic numbers, traces, links, and IDs update per run/case.
   - Check that empty, missing, or failed trace/eval states degrade visibly.
   - Verify the served frontend bundle changed, not only the source file. For static apps, fetch `/`, inspect the JS/CSS cache key, then fetch the served asset and confirm it contains a new sentinel string.
   - After fixing a UI bug, retest the exact click path that failed, from page reload through the final rendered surface.

## Contract Checklist

Every non-trivial eval UI contract should answer:

- What are the UI modes or surfaces?
- What identity key binds each surface?
- What data source backs each field?
- Which data is canonical truth?
- Which immutable tuple proves every visible panel belongs to the same case?
- Which fields distinguish unanswered, explicit abstention/`none`, and a
  selected candidate?
- Which data is advisory, pending review, or candidate-only?
- Which UI actions mutate files, datasets, or expected labels?
- Which actions are explicitly forbidden?
- Which optional gate opens which surface, and which surfaces must remain closed?
- If rows are scored or ranked, what is the required ordering and where is the score displayed?
- Are retrieved rows merely candidates, or have they been reviewed/scored enough to call relevant?
- How are stale selections cleared?
- What happens when trace/eval/dataset data is missing?
- Which tests enforce each acceptance criterion?

## Eval Boundary Rules

- Strict correctness goldens are canonical expected truth. UI may display them but must not mutate `expected_outputs.jsonl` or equivalent expected-label files unless the user explicitly asks for promotion/editing work.
- Trace-repair cases are transition tests. First-run failure can be expected, but must live in a separate repair suite from strict correctness goldens.
- Live retrieval candidates are evidence packets. Candidate triage, LLM-judge suggestions, and human review metadata are not strict eval truth.
- A blind-review projection must enumerate allowed fields. Composition flags,
  expected labels, outcomes, ranks, and other side channels stay absent unless
  the review contract explicitly requires them.
- Human review remains authoritative for promotion when the product architecture says so.
- LLM-as-judge output must be labeled as advisory unless the repo explicitly defines it as canonical.
- Telemetry and traces are evidence/context. Do not imply they decide policy unless a deterministic gate consumes them and tests prove that path.

## UI Data-Binding Rules

- Use explicit IDs in state and rendered metadata.
- Never infer current run context from the first available candidate, dataset row, or trace.
- Never pair panels by list position, presentation ordinal, filename order, or
  first match. Resolve the complete immutable binding tuple and fail visibly on
  zero or multiple matches.
- Do not mix global dataset totals with active-run metrics without labels.
- Show actual retrieved fixtures/markets/examples, not just counts, when relevance matters.
- Clear selected candidate/review/dataset state when the source text, run, or golden changes.
- Keep manual debug controls separate from judge/user workflow controls.
- Never auto-select or auto-scroll into an existing candidate/review queue after a current-run triage action unless the user explicitly chose that queue/review gate.
- When a current-run action creates a candidate artifact, keep the current-run surface active unless the contract says to switch surfaces.
- Label live retrieval rows as candidate/evidence rows until scoring or human review justifies stronger language.
- Collapse or cap long evidence/rules/provenance text so one long row cannot dominate or hide the rest of the workflow.

## Testing Pattern

Use the repo's existing test style, but cover at least:

- Each material acceptance criterion has a behavioral check; review the contract for completeness without treating a text-presence assertion as proof.
- API rejects bypass paths that would skip required trace/eval/review gates.
- API accepts an explicit governed `none` without treating it as unanswered,
  while still rejecting a truly missing decision.
- Source, normalized thesis, review focus, candidate evidence, and submission
  share the same immutable case binding; a cross-case fixture is rejected.
- UI renders current-run metrics from the current run response.
- UI does not auto-select stale candidates/datasets/traces.
- Frozen fixture replay uses only fixture data for that example.
- Advisory output cannot write canonical expected labels.
- Missing external services degrade to explicit unavailable/no-suggestion states, not silent success.
- Scored or ranked rows render in the same order as their visible score/rank.
- Static frontend changes are actually served: the HTML references a fresh asset key and the fetched asset contains the expected new code.
- Live retrieval filters are covered with representative noisy examples, such as high-volume wrong-entity/wrong-context rows.

## Completion Criteria

Do not call the UI work done until:

- Contract/spec file exists and its material behaviors are covered by tests.
- Relevant UI/API/model changes are implemented.
- Tests and evals relevant to the changed boundary pass.
- Manual browser verification is performed for substantial frontend work when access is available and authorized; otherwise the unverified UI behavior and its effect on completion are explicit.
- Final response reports changed files, commands run, test/eval results, and remaining risks.

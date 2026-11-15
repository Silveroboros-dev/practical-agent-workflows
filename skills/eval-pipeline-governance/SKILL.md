---
name: eval-pipeline-governance
description: Design, run, or audit governed evaluation pipelines, blind holdouts, live model evaluations, artifact lineage, and human or agent review evidence. Use for evaluation validity and external-effect controls; do not use for ordinary unit testing or routine UI implementation.
---

# Eval Pipeline Governance

Build evidence that survives later audit. Treat a passing score as insufficient unless the evaluated cohort, execution authority, runtime, review boundary, and artifact chain are also bound.

## Start with the evaluation claim

State what is being evaluated and keep stages separate. Typical stages include source eligibility, transformation or normalization, candidate retrieval, semantic classification, final decision quality, and later monitoring. Give each stage its own denominator, metric, failure class, and gate. Do not let a downstream pass hide an upstream exclusion or combine stage metrics into one ambiguous accuracy number.

Record unknowns and the cheapest outcome-blind validation needed to resolve them. Do not broaden live authority merely because more evidence would be useful.

## Preserve identity and lineage

- Derive immutable identity from bound content and provenance. Treat case numbers, row ordinals, filenames, paths, and UI IDs as presentation metadata.
- Join artifacts by immutable identity or an exact, validated content tuple. Fail on missing or ambiguous joins. Test that arbitrary presentation-ID renumbering leaves membership, exclusions, and results unchanged.
- Bind the complete comparison corpus, exposure registry, projection version, ordered identity sets, source bytes or their private receipts, and every derived artifact.
- Never repair a frozen cohort or receipt in place. Create a new version or private root, retain predecessor bindings, and state which artifact supersedes which.
- Distinguish exact overlap evidence from semantic novelty. Lexical or nearest-neighbor screens nominate comparators; they do not prove semantic clearance.
- State external-seal limitations. A digest inside the same mutable directory is integrity metadata, not an independent seal. The next artifact must bind the prior artifact's raw hash, size, and internal digest; a commit, signature, or separately controlled ledger is the external chain head.

## Enforce blindness and separation

Keep source intake, candidate or model outputs, and outcome or truth labels in separate artifacts and access scopes. Project only the fields needed for the current decision. A semantic reviewer should not receive normalization output, retrieval ranks, market or candidate catalogs, labels, or outcomes unless the review question explicitly requires them.

Define the review packet schema and forbidden fields. Bind the packet to the exact corpus and candidate identities. Require reviewer-authored attestation bytes for identity and content-boundary claims. Describe the assurance truthfully: an agent self-attestation is not a cryptographic signature, human review, or product-owner authority.

## Govern external effects

Before any live call, freeze a run contract covering exact provider API operations, per-operation limits, retry policy, maximum cost, model and endpoint, and stop conditions. Do not call unmetered authentication or SDK transport exchanges “network calls” when only provider API operations are governed; name and meter the controlled unit precisely.

For every potentially billable or externally mutating operation, use a durable state machine:

`prepared -> started -> succeeded | failed_before_effect | uncertain`

Persist `started` before the effect. Preserve effect truth: a returned operation that completed but produced mechanically unusable bytes is still `succeeded`; parsing, capture, semantic, and gate states belong in separate fields. After an ambiguous timeout or crash with no conclusive effect evidence, record `uncertain` and stop by default.

Permit a possible duplicate external effect only through one of two explicit paths:

- fresh successor authority with proof that the duplicate is impossible or an explicit acceptance of the bounded duplicate risk; or
- an original authority that, before the first start, preregistered a closed and versioned bounded-duplicate policy.

Both paths must preserve the immutable operation identity and exact request/configuration digest, allow at most one successor start per operation, remain within a finite phase cap, use an outcome-blind mechanical trigger, preserve every predecessor terminal state, and make the first mechanically valid response permanent. A changed request, configuration, or outcome-triggered resample is a new experiment, not a resume.

Duplicate-risk acceptance without idempotency proof is available only for billable or nondeterministic effects that do not mutate governed external state and whose possible duplicate is explicitly declared tolerable. An externally state-mutating successor requires provider-enforced idempotency proof; human acceptance alone is insufficient.

The preregistered path must additionally bind a stable policy ID and a closed, versioned allowlist of mechanically derived predecessor states and failure codes. A provider-response byte, envelope, or schema-validation failure may qualify only when that exact mechanical check was preregistered; local parser implementation, configuration, programming, persistence, sealing, usage, semantic, downstream, or other open-ended failures must never authorize a duplicate. A cap is only a ceiling, not retry authority.

A hash-linked journal is necessary but not sufficient: validate legal transitions, ordinals, attempt limits, exact retry eligibility from durable predecessor evidence, cross-case bindings, terminal uniqueness, and semantic consistency.

Quarantine exact raw response bytes with restrictive permissions before parsing. Bind their hash and size in a sanitized receipt; do not print or publish raw content. Make journal and quarantine durability explicit: flush and `fsync` the file, atomically rename where applicable, and `fsync` the parent directory before advancing state.

Bind the runtime and code envelope: source revision, dirty-state policy, dependency and SDK versions, schemas, prompts, generation configuration, provider metadata, and relevant environment decisions. Drift invalidates authorization unless the contract explicitly permits it.

## Keep telemetry separate from governed evidence

When a governed evaluation uses operational telemetry, define its evidentiary
role explicitly. Sampled traces alone do not establish semantic truth, human
approval, retry authority or evaluation PASS. If telemetry supplies a declared
measurement, bind its identity, capture/sampling policy and completeness to
that measurement; do not infer missing operations from an empty export.

- Keep immutable operation/run identity separate from W3C trace context.
  Propagation metadata must not change semantic identity, idempotency or
  external-effect authority. Distinguish queue, execution and human wait;
  use bounded operation spans and appropriate parentage or links across
  asynchronous/resumed work.
- Record the instrumentation and semantic-convention versions actually used
  in the execution envelope. Do not silently turn evolving provider
  attributes into evaluation gates.
- Use versioned structured events linked to the execution envelope: requested
  and observed model versions, actual generation settings, prompt/policy
  versions, stage outcomes and available usage. Preserve unknowns. Semantic
  error claims require attributable checks/review, not just a log level.
  Route diagnostics away from protocol channels such as MCP STDIO stdout.
- Default to an explicit metadata allowlist. Exclude prompts, responses,
  arbitrary baggage, raw URL/query/header payloads and unsanitized exception
  chains from general telemetry. Content capture requires a separately
  scoped purpose, access and retention policy; prefer controlled evidence
  artifacts with safe references. A digest is not inherently anonymous.
- Exporter failure may degrade observability, but must not change effect
  truth, authorize retries or bypass required journal/receipt persistence.
  Verify bounded failure and disabled-mode behavior when instrumenting the
  workflow; sampling must not sample away mandatory evidence.
- Define measurement boundaries: queue time differs from execution time;
  non-streaming total duration is not TTFT; time to first chunk is not
  automatically an observed first token. Unknown usage is not zero, and
  estimated cost is not confirmed billing. Keep technical failure separate
  from valid domain outcomes such as clarification or no clean match.

## Challenge executable contracts before authority

For a new or changed live-run, canary, holdout, or automated-gate contract, perform a read-only contract challenge before execution authority is claimed. Inventory every predicate that can block, authorize, retry, or report success; classify its evidentiary basis; bind the exact execution context; and verify that external-effect state and gate state remain independent.

A challenge may block execution but never grants, expands, claims, consumes, or renews authority. Preserve every completed challenge as a new predecessor-bound `challenge_packet_vN`; never repair or overwrite a prior packet. A packet marked `ready` means only that no blocker was found within its declared scope.

For contract preflight, canary or holdout freeze review, or recurring evidence-drift monitoring, read [references/contract-witness-formula.md](references/contract-witness-formula.md). Use its default read-only, offline boundary unless the user separately authorizes a broader operation.

## Review and finalization

Derive gates mechanically from bound decisions; never hard-code pass or zero collisions. Validate reviewer evidence, rationale, identity sets, counts, timestamps, content-boundary attestations, and independence claims from reviewer-authored artifacts. Keep authority limitations visible.

Use adversarial negative tests proportional to risk, including:

- presentation-ID renumbering and stale or cross-case bindings;
- placeholder identity collapse or omitted corpus rows;
- receipt re-chaining, reordered or duplicated decisions, and forged counts;
- ambiguous external effects followed by an unauthorized retry;
- arbitrary failure codes, changed request/configuration digests, or cap-only reasoning used to authorize a bounded duplicate;
- symlinked private roots or parent directories;
- mutated runtime, corpus, response, rationale, or attestation bindings.

For a live model run, blind holdout freeze, semantic clearance, or final amendment bridge, read [references/live-holdout-checklist.md](references/live-holdout-checklist.md). For evaluation or review UI work, also use `eval-ui-contract-builder`; this skill governs evidence and execution, not UI implementation.

## Report

Report the evaluated claim, stage-specific counts and metrics, authority consumed, artifact chain, validations run, exclusions, unresolved risks, and whether any live action remains authorized. Never imply that a private digest chain is externally sealed or that self-attested independence is stronger than its stated assurance scope.

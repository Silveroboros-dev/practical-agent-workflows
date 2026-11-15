# Live Eval and Blind Holdout Checklist

Read this reference for live provider calls, blind holdout freezing, semantic review, or final cohort promotion. Adapt the mechanics to the risk; do not add a live dependency or call merely to satisfy the checklist.

## 1. Preregister the claim and stages

- Define each stage, its input cohort, denominator, metric, exclusion policy, and pass condition.
- Separate source eligibility, transformation, retrieval, semantic fit, decision quality, and monitoring.
- Freeze the intended composition and heuristic coverage as planning evidence, not truth labels.
- State which failures remain in the audit denominator and which make a case ineligible for later stages.

## 2. Freeze inputs and exposure lineage

- Bind source bytes or private capture receipts, canonical text, publication evidence, URL aliases, story identity, and immutable source identity.
- Bind all prior eval cohorts, review packets, training or SFT exposure inputs, author packs, and other comparison corpora relevant to novelty.
- Record projection and canonicalization versions plus ordered row-to-identity mappings.
- Reject placeholders, invalid digests, missing rows, ambiguous content tuples, and silent deduplication.
- Keep presentation IDs outside immutable identity. Add in-memory and serialized renumber-invariance tests.
- Create a new root/version for repairs and preserve every predecessor seal.

## 3. Define the blind boundary

- List allowed input artifacts and forbidden outcome, label, catalog, retrieval, or model-output fields for each role.
- Build the smallest review projection that supports the decision.
- Treat exact checks and nearest-neighbor scores as evidence, not semantic verdicts.
- Bind reviewer evidence and rationale sidecars to immutable candidate identities, corpus digest, and review-input digest.
- Require a reviewer-authored attestation. Validate its raw bytes, internal digest, artifact bindings, reviewer identifier, timestamps, decision identity set, and self-declared access boundary.
- Record whether assurance is human, cryptographically signed, organizationally authorized, or only agent self-attestation. Do not upgrade one into another.

## 4. Freeze live authority

Bind before the first external operation:

- model, endpoint, region, provider metadata, SDK and dependency versions;
- prompt, response schema, safety and tool settings, generation configuration, and parsing contract;
- exact provider API operations allowed and their maximum counts;
- token ceilings, price source and validity period, cost formula, and total cap;
- transport and SDK retry settings, timeout or max-silence rules, and idempotency strategy;
- any bounded-duplicate policy ID, exact mechanically derived trigger allowlist, immutable operation/request/configuration binding, at most one successor start per operation, finite phase cap, duplicate-risk or idempotency evidence, and deterministic first-valid-response rule;
- runtime files, source revision, dirty-state policy, environment decisions, and credential identity digests without secret values;
- explicit exclusions such as deployment, market access, outcome access, writes, publication, or a second attempt.

Count what is actually governed. OAuth refresh, DNS, redirects, and SDK transport may add HTTP exchanges outside a cap on provider API operations. Do not claim a raw-network-call cap unless all transport is instrumented.

## 5. Persist attempts before effects

For each case and operation:

1. Validate authority, identity, prior terminal state, and budget.
2. Append `started` with case identity, operation identity, request digest, attempt ordinal, and predecessor entry digest.
3. Flush and `fsync` the journal file and parent directory.
4. Perform the single authorized external operation.
5. Quarantine raw response bytes before parsing; use owner-only directories and files, reject symlinked roots or parents, flush, `fsync`, and atomically finalize.
6. Append exactly one terminal state: `succeeded`, `failed_before_effect`, or `uncertain`. A completed operation with mechanically unusable returned bytes remains `succeeded`; record capture, parsing, semantic, and gate results separately.
7. On `uncertain`, stop the current attempt. Do not start a successor unless either:
   - fresh authority proves that a duplicate effect is impossible or explicitly accepts the bounded duplicate risk; or
   - the original authority preregistered a closed, versioned, outcome-blind bounded-duplicate policy that applies exactly.
8. For either path, preserve the immutable operation identity and exact request/configuration digest, permit at most one successor start per operation, remain within the finite phase cap, use an outcome-blind mechanical trigger, preserve predecessor terminal states, and permanently select the first mechanically valid response. Treat a changed request, configuration, or outcome-triggered resample as a new experiment.
9. Duplicate-risk acceptance without idempotency proof applies only to billable or nondeterministic effects that do not mutate governed external state and whose possible duplicate is explicitly tolerable. Require provider-enforced idempotency proof for an externally state-mutating successor.
10. For the preregistered path, re-derive eligibility from durable predecessor evidence. Require the exact policy ID, allowed predecessor state and failure code, no disqualifying response evidence, remaining budgets, and explicit duplicate-risk acceptance or idempotency evidence. A provider-response byte, envelope, or schema-validation failure may qualify only when that exact mechanical check was preregistered. Local parser implementation, configuration, programming, persistence, sealing, usage, semantic, downstream, arbitrary, or unknown failures never qualify. A cap alone is not authority.

Validate journal meaning, not just hashes: legal transitions, monotonic ordinals, one terminal per start, no terminal without start, exact bounded-duplicate eligibility, unchanged operation and request/configuration bindings, no cross-case request or response binding, attempt and cost ceilings, deterministic response selection, and consistent raw-receipt references. Test that an attacker cannot edit rows and simply recompute the hash chain.

## 6. Parse and score fail-closed

- Parse only quarantined bytes whose receipt matches the started operation and candidate identity.
- Reject missing, extra, malformed, cross-case, stale, or multiply selected responses.
- Preserve raw and canonical hashes separately.
- Compute stage metrics only from their registered denominators; publish exclusion and failure counts beside scores.
- Never convert transport success, parse success, lexical distance, or reviewer confidence into a semantic pass implicitly.

## 7. Finalize the evidence chain

Use a non-circular sequence such as:

`frozen inputs -> run receipt -> reviewer decision receipt -> reviewer-authored attestation -> mechanically derived final summary -> external bridge or seal`

Each later artifact binds the earlier artifact's raw hash, byte count, and internal digest. Validate every binding from bytes. The final summary must derive counts and gate status from records. The bridge must say whether it is merely private, committed, signed, or anchored in a separately controlled ledger.

## 8. Required adversarial checks

- Delete, duplicate, reorder, or replace a decision while resealing its container.
- Rename every presentation ID in memory and after canonical serialization.
- Replace valid identities with a shared placeholder or invalid digest.
- Omit a corpus version, exposure source, or row mapping.
- Rebind a response, rationale, attestation, or terminal journal entry to another case.
- Mutate runtime, prompt, schema, model metadata, price, or cost authority.
- Re-chain an illegal journal transition.
- Crash after `started`, after response receipt, and before terminal persistence.
- Offer an arbitrary or semantic failure code as a bounded-duplicate trigger.
- Change the bounded-duplicate policy ID, request/configuration digest, operation identity, or cap between attempts.
- Try a second successor start for the same immutable operation.
- Accept duplicate risk for an externally state-mutating effect without provider-enforced idempotency.
- Present two mechanically valid responses and verify that the first remains permanently selected.
- Point the private root or any parent through a symlink.
- Change reviewer boundary claims, reviewer identity, authority scope, timestamps, or bound artifacts.
- Verify deterministic rebuilding and preservation of all predecessor roots.

## 9. Stop conditions

Stop rather than infer success when identity mapping is ambiguous, source or exposure coverage is incomplete, a receipt cannot be validated, the runtime drifts, the budget unit is unclear, a reviewer attestation overclaims authority, an external effect is uncertain without an exact still-valid successor path, bounded-duplicate eligibility cannot be mechanically re-derived, or an external seal is absent but required by the claim.

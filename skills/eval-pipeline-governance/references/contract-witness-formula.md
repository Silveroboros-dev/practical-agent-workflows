# Read-Only Contract Witness Formula

Use this formula to challenge an executable evaluation contract before live authority is claimed, or to monitor a previously challenged contract for material drift. The witness produces advisory evidence. It is not an implementer, an authorization source, an execution receipt, or proof that the contract is correct.

## Required inputs

Bind, rather than reconstruct from memory:

- the exact contract or freeze candidate;
- predecessor contract and challenge receipts, if any;
- repository, worktree, source revision, and dirty-state policy;
- relevant runtime, dependency, prompt, schema, endpoint, model, dataset, and evidence-root bindings;
- intended external-effect state machine and gate semantics;
- authority artifact, or an explicit statement that authority is absent.

If a required input is missing or ambiguous, record a blocker. Do not infer it from a filename, task title, UI state, conversation summary, or nearby artifact.

## 1. Bind the execution context

Record from observable state:

- command working directory and real path;
- repository and worktree roots;
- branch or detached state and exact revision;
- dirty paths and permitted dirty-state policy;
- contract raw hash, byte count, and internal digest;
- relevant prompt, schema, dataset, dependency lock, model, endpoint, and runtime bindings;
- state root, evidence root, predecessor receipt, and intended output namespace;
- witness implementation revision and declared access boundary.

Treat task metadata, saved-project metadata, and UI branch labels as claims to compare with execution truth. A material mismatch invalidates the challenge until resolved. Never record secret values; bind only permitted non-secret identifiers or credential-identity digests.

## 2. Inventory and classify predicates

Inventory every Boolean condition or ordering assumption that influences whether an external effect may start or retry, a response is accepted, compatibility or quality passes, a process exits successfully, or an artifact is promoted or reported complete.

For each predicate record its stable ID, exact expression, entities/types/units/scope, operational purpose, classification, evidence bindings, falsifying example, gate role, and status (`supported`, `scoped_observation`, `unsupported`, or `ambiguous`).

| Classification | Meaning | Gate eligibility |
| --- | --- | --- |
| `computed_definition` | True by the registered computation or schema definition. | Eligible after deterministic verification. |
| `local_invariant` | Guaranteed by bound local code, format, or protocol. | Eligible when exact implementation and tests are bound. |
| `external_documented_guarantee` | Guaranteed by an authoritative external contract for an exact API, model, endpoint, version, and date scope. | Eligible only within that pinned scope. |
| `policy_choice` | A product or governance decision, not a discovered fact. | Eligible only with its authorizing artifact and scope. |
| `empirical_observation` | Observed in a bounded sample or canary. | May gate only that registered observational test; never promote it to a provider guarantee. |
| `unknown` | No sufficient evidence establishes the predicate. | Ineligible; block any gate that depends on it. |

Names, apparent semantics, correlated values, and one successful response do not establish equality, ordering, causality, or interchangeability. Provider behavior is scoped evidence, not a universal invariant.

## 3. Apply four challenge passes

1. **Entity and type:** identify conflated states or values, such as missing versus present-but-empty, estimated versus actual, transport success versus semantic success, or presentation identity versus immutable identity.
2. **Purpose:** state the safety or product goal. Prefer direct controls for that goal; independent ceilings can enforce cost safety without inventing equality or ordering between differently defined metrics.
3. **Evidence and causality:** distinguish evidence for the exact predicate from coexistence, correlation, bounded observation, or plausible explanation.
4. **Boundary and failure semantics:** verify the predicate's runtime and contract scope and that false, unknown, malformed, or drifted inputs fail closed in every consuming interface.

Do not repair code or rewrite the contract during the challenge. Record the smallest scoped correction or validation needed and require a new contract digest and packet.

## 4. Keep effect and gate states independent

External-effect state:

`prepared -> started -> succeeded | failed_before_effect | uncertain`

Gate state:

`not_evaluated | passed | failed | blocked | invalidated`

Rules:

- `succeeded` records only that the governed external operation completed; it does not imply `passed`.
- A succeeded operation may produce `passed`, `failed`, or `blocked`.
- `failed_before_effect` is not a semantic failure or success.
- `uncertain` keeps that attempt's effect terminal state and requires its gate to remain `blocked`; never rewrite it to justify a later attempt.
- Default to no retry after `uncertain`. A successor attempt requires either fresh authority with proof that a duplicate is impossible or explicit acceptance of the bounded duplicate risk, or an original authority that preregistered the narrow bounded-duplicate exception below.
- Both paths preserve immutable operation identity and the exact request/configuration digest, permit at most one successor start per operation, remain within a finite phase cap, use an outcome-blind mechanical trigger, preserve predecessor terminal states, and permanently select the first mechanically valid response. A changed request, configuration, or outcome-triggered resample is a new experiment, not a resume.
- Duplicate-risk acceptance without idempotency proof applies only to billable or nondeterministic effects that do not mutate governed external state and whose possible duplicate is explicitly tolerable. An externally state-mutating successor requires provider-enforced idempotency proof.
- A preregistered bounded-duplicate exception is eligible only when the contract additionally binds a stable policy ID and a closed, versioned allowlist of mechanically derived predecessor states and failure codes.
- A completed operation with mechanically unusable returned bytes remains `succeeded`; capture, parsing, semantic, and gate failures remain separate. A provider-response byte, envelope, or schema-validation failure may qualify only when that exact mechanical check was preregistered. Local parser implementation, configuration, programming, persistence, sealing, usage, semantic, downstream, arbitrary, or unknown failures do not.
- The witness must re-derive retry eligibility from durable predecessor evidence. A two-attempt or cost ceiling alone never grants retry authority.
- Context or artifact drift after challenge produces `invalidated`.
- Never rewrite an effect terminal state to match a later gate result.
- For a command whose purpose is enforcing a gate, only `passed` may return success. Other required states must be machine-distinguishable failures.
- Bind the exact predicate set and contract digest used to derive the gate.

## 5. Respect the authority boundary

Default mode is `read_only_offline`.

Permitted:

- read and hash already authorized local artifacts;
- use read-only repository inspection;
- parse and recompute deterministic receipts;
- run proven-offline adversarial fixtures in an isolated temporary root with credentials absent and network disabled;
- prepare findings and a challenge packet.

Forbidden unless separately authorized:

- editing project or evidence files other than a new packet in its designated output transaction;
- changing Git state, committing, pushing, merging, tagging, or releasing;
- installing dependencies or loading/refreshing credentials;
- provider, cloud, API, deployment, database, or other network calls;
- starting, retrying, or acknowledging an external effect;
- claiming, consuming, renewing, or broadening run authority;
- sending messages or approvals on a person's behalf;
- repairing the challenged implementation.

If current external documentation is required, record the missing evidence. A separately authorized documentation lookup may create a pinned evidence artifact, but it does not authorize a provider invocation.

## 6. Write an immutable challenge packet

Use a new `challenge_packet_vNNNN.json` for every completed challenge. The sequence is monotonic within the contract family; identity comes from bound bytes. Include at least:

```yaml
schema_version: eval_contract_challenge_packet_v1
packet_sequence: 1
created_at_utc: ...
witness:
  identity: ...
  implementation_revision: ...
  mode: read_only_offline
  declared_access: [...]
challenged_contract:
  raw_sha256: ...
  byte_count: ...
  internal_digest: ...
predecessor:
  packet_raw_sha256: null
  packet_byte_count: null
  packet_internal_digest: null
context_binding:
  command_cwd_realpath: ...
  repository_root_realpath: ...
  worktree_root_realpath: ...
  branch_or_detached: ...
  source_revision: ...
  dirty_state: ...
  runtime_bindings: ...
  artifact_roots: ...
predicates: [...]
effect_gate_contract:
  effect_states: [...]
  gate_states: [...]
  derivation_binding: ...
authority_assessment:
  authority_present: false
  authority_state: none
  permitted_operations: [...]
  prohibited_operations: [...]
adversarial_fixture_results: [...]
findings: [...]
overall_state: ready | blocked | invalidated
scope_limitations: [...]
notification_keys: [...]
```

Finalize a receipt binding the packet's raw hash, byte count, and internal digest. Every later packet binds the prior receipt and newly challenged contract.

- Refuse to overwrite an existing packet or receipt; corrections require the next version.
- Issue a new packet after any material contract, source, context, predicate, authority, or witness-version change.
- Preserve predecessors and report when the chain is not externally sealed.
- Exclude environment values, tokens, credentials, raw provider responses, and quarantined content.
- `ready` means only that no blocker was detected within the declared scope. It grants no live authority.

## 7. Run adversarial fixtures

Use fixtures proportional to risk. The minimum reusable set is:

| Fixture | Expected result |
| --- | --- |
| Tracked zero-byte file and genuinely missing file | Presence logic distinguishes them. |
| Related metrics with `<`, `=`, and `>` values | No relationship becomes an invariant without classified evidence. |
| Effect `succeeded`, gate predicate false | Effect remains succeeded; gate fails. |
| Effect `uncertain` without an exact authorized bounded-duplicate path | Gate blocks and no retry becomes authorized. |
| Exact preregistered bounded-duplicate trigger | Eligibility is re-derived from durable evidence; identity and request/configuration digest remain unchanged; at most one successor, phase cap, and first-valid selection hold. |
| Arbitrary, semantic, local-parser, configuration, programming, persistence, sealing, usage, or downstream failure code | No bounded duplicate becomes authorized. |
| Accepted-risk successor for a governed-state-mutating effect without provider-enforced idempotency | No bounded duplicate becomes authorized. |
| Bounded-duplicate policy ID, request/configuration digest, trigger allowlist, or cap drifts | Prior authority invalidates before another effect. |
| Gate command gets false, malformed, or required-but-unknown state | Machine-distinguishable failure. |
| Task/UI cwd differs from bound worktree | Context invalidates before execution. |
| Branch, revision, dirty path, prompt, schema, or model changes | Prior challenge invalidates. |
| Packet version already exists | Writer refuses overwrite and requires the next version. |
| Authority is pending, stale, claimed, consumed, or cross-contract | Witness does not treat it as available. |
| Receipt, predicate result, or response is rebound across contracts/cases | Validation fails closed. |
| Secret-shaped value is offered for the packet | Excluded and reported without echoing it. |
| Unchanged finding recurs | Notification is deduplicated. |

A fixture must not contact a provider or consume live authority.

## 8. Notify only on material change

Derive a stable notification key from contract digest, finding code, predicate identity, and relevant evidence digest. Notify only for a new blocker or severity increase, context drift, authority lifecycle change, ambiguous effect, attempted overwrite, or proven resolution/supersession. State the affected binding, evidence, consequence, cheapest scoped correction, and whether live execution is blocked. Do not send unchanged reminders or contact third parties without separate authority.

## 9. Stop rules

Stop rather than infer or repair when:

- repository, worktree, revision, or contract cannot be bound;
- the challenged artifact changes during inspection;
- an unsupported or ambiguous predicate controls authority or a required gate;
- packet lineage, immutable identity, or context bindings fail;
- an external effect is `uncertain` and no exact, still-valid fresh or preregistered bounded-duplicate authority applies;
- authority is absent, stale, consumed, changed, or cross-contract;
- continuing requires credentials, network access, mutation, or a live operation outside the witness boundary;
- secret material would need exposure;
- the designated packet version already exists.

Emit `blocked` or `invalidated` only when that can be done without violating the same stop condition. Otherwise report the blocker without creating an artifact.

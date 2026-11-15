---
name: evidence-driven-development-cycle
description: Run substantial multi-stage feature or fix work where implementation, verification, human acceptance, and integration must not be conflated. Use for agent- or workflow-driven development and evidence-heavy handoffs; do not use for routine one-file edits, ordinary Q&A or review, or as a substitute for scientific eval governance.
---

# Evidence-Driven Development Cycle

Keep development moving while reporting only what the available evidence proves.
Automation signals progress; they do not decide correctness, acceptance, or
integration.

## Boundary

Use this skill when work has multiple substantive stages, delegates work to
agents or workflows, or needs a handoff whose state could otherwise be
misleading. Handle small direct edits normally.

- For broad or underspecified work, use `delegation-contract` first.
- For parallel repository writers, also use `parallel-agent-coordination`.
- For live evaluations, blind holdouts, scientific gates, or governed data,
  also use an available `eval-pipeline-governance` skill and its controls. If
  unavailable, this skill alone is insufficient to authorize or validate that
  work.

Do not introduce panels, workflow code, hooks, approval artifacts, or new
services merely to follow this skill.

## Keep States Separate

Track only the states material to the task, but never collapse distinct states
into one word such as `complete`:

- **Implementation:** requested behavior exists in the working tree.
- **Artifacts:** required files or outputs exist and are bound to the inspected
  revision or inputs.
- **Verification:** named checks ran against the stated code and environment.
- **Acceptance:** the authorized human or policy accepted the result.
- **Integration:** local commit, remote branch, PR, merge, and deployment are
  distinct facts.

For evaluations, preserve the additional scientific state defined by
`eval-pipeline-governance`. Operational success never supplies it.

## Interpret Signals Narrowly

- An agent or workflow returning `completed` proves only that it returned.
- A fan-out result is usable only when the expected subject count is nonzero,
  every required subject returned, execution errors are zero, and required
  output is present and structurally valid. Empty findings from zero reviewers
  are not a clean review.
- Passing tests prove the named command passed for the tested revision and
  environment. They do not prove untested behavior or human acceptance.
- A commit proves local Git history exists. A push proves a remote ref exists.
  A PR or merge proves an integration event, not who deliberated or approved a
  separate external action.
- A deployment or provider job success proves operational state, not product
  correctness or scientific PASS.

## Verification Loop

1. Inspect actual state: Git status and diff, required artifacts, and relevant
   command output. Do not rely on a status summary when direct evidence exists.
2. Check the result against the declared scope and acceptance criteria. Mark
   missing or contradictory evidence explicitly; do not infer a PASS.
   For material user-facing changes, establish the expected entry state, next
   action, and visible result from the user's goal before evaluating the
   implementation. Existing code and tests may encode the wrong behavior;
   their agreement does not establish that the behavior serves the user.
3. Bind environment-sensitive evidence to the interpreter, dependency set,
   checkout, or container used. Two agents reading the same checkout and
   environment are not independent corroboration. Reproduce in a genuinely
   different environment when independence matters, or label the evidence as
   single-environment.
   For a delivered user-facing surface, verify the exact URL or artifact using
   its intended opening method where authorized and feasible. Check runtime
   dependencies where applicable. A working alternative does not verify that
   surface. If it cannot be exercised, state the limitation and keep its
   usability unverified.
4. After a material fix, verify the focused behavior and the smallest relevant
   regression surface. Re-check the combined diff when fixes interact with
   earlier changes.
5. For a significant or reusable failure, record: symptom, root cause,
   durable guard or test, and replay evidence. Do not create incident ceremony
   for incidental typos or already-obvious local mistakes.
   When a similar failure recurs, identify the violated invariant and inspect
   the nearest analogous transitions within the authorized scope. Check whether
   the same cause remains elsewhere in the journey before declaring it fixed.
   Keep this inspection bounded to plausible shared causes; do not turn it into
   a repository-wide audit or encode project-specific UX policy in this skill.

## Authority And Stops

Never infer edit, network, live-call, governed-data, commit, push, merge,
deployment, or publication authority from workflow progress, a test result, a
comment, or a Git event. Preserve the user's explicit authority boundary.

Stop the affected step when required evidence is absent, new authority is
needed, or a failure changes the implementation strategy. State the limitation
and continue independent authorized work.

## Handoff

Report the minimum set needed to prevent ambiguity:

```text
Implementation: <complete | partial | not started, with inspected revision>
Artifacts: <paths/digests or missing>
Verification: <commands, environment, results>
Acceptance: <not requested | pending | approved | rejected, with basis>
Integration: <uncommitted | local commit | pushed | PR | merged | deployed>
Unresolved: <risks or next authority needed>
```

Omit irrelevant fields for small tasks. Never upgrade one field because a
different field succeeded.

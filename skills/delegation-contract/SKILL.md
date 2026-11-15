---
name: delegation-contract
description: Establish a bounded mission contract for substantial delegated work, and check mission alignment during execution when scope, evidence, cost, failures, or the expected outcome change materially. Use for delegation, execution planning, agent work packets, or consequential mid-task drift; skip routine steps and straightforward scoped edits.
---

# Delegation Contract

## Overview

Use this skill to turn an open-ended request into a bounded, executable agent mission and keep substantial work aligned with the user’s intended outcome as circumstances change. For a new mission, fill required fields from context or clearly marked assumptions; ask only when necessary. For an ongoing mission, use the existing agreement and the Mission Alignment section without restarting the interview.

## Contract-First Rule

Do not begin substantial task execution until the delegation contract is complete.

Read-only discovery is allowed when it helps fill the contract. Do not edit files, install dependencies, create branches, commit, push, call paid/external services, or take destructive actions unless the contract grants that authority.

## Required Fields

Fill these fields before proceeding:

```text
Mode:
Scope:
Authority:
Evidence:
Stop condition:
```

Use only these primary modes:

- `assess only` - inspect, reason, identify risks, recommend; no implementation.
- `implement` - make scoped code or artifact changes.
- `review` - code-review stance: findings first, file/line references, risks, missing tests.
- `test` - run or design verification without broad implementation.
- `commit` - stage and commit an already-scoped change; may include implementation only if explicitly authorized.

## Interview Workflow

1. Parse the request and local context first. Infer obvious values, but label them `Assumed`.
2. Draft the contract in the required format.
3. Ask concise follow-up questions only for missing or risky fields. Ask no more than three questions at a time.
4. Prefer proposing a default over asking an open-ended question when the default is low-risk.
5. Repeat until every required field has a value.
6. Once complete, restate the final contract briefly and proceed only within it.

## Mission Alignment During Execution

At a material change or warning, compare the user's original and any explicitly
revised objective and intended deliverable with the current plan and next step.
Triggers include a substantial increase in scope, evidence standard, time,
money or human effort; repeated failures; or new evidence that makes the plan
unlikely to serve its purpose. Do not run this check for every routine action
or on a fixed schedule.

For a consequential proposed change to an agreed plan, tell the user what
changed and why, the recommended action and a viable alternative, and their
effects on the original goal, deliverable, schedule, budget and user effort
where relevant. Explain material risks, likely consequences and qualitative
likelihood when supported; mark unknown probabilities as unknown instead of
inventing numbers. Distinguish existing evidence, assumptions and estimates.
Ask for the user's explicit decision before the change; prepare a concrete,
reviewable proposal first and continue independent work already authorized.
An earlier approval does not imply understanding or consent to an undisclosed
material tradeoff, nor does it revoke an explicit user decision.

Handle routine implementation choices and reversible work within the agreed
scope autonomously; do not add approval gates, recurring check-ins, extra
agents or documents just to follow this practice. Pause the affected action
if continuing would violate authority or a stop condition, or if repeated
failure makes further execution unproductive; preserve the evidence and notify
the user. Recommend the next direction, but do not silently change the mission,
declare it complete, discard an agreed requirement, or resume a paused goal.

## Field Guidance

### Mode

Infer from verbs when safe:

- "audit", "think through", "assess", "readiness", "strategy" -> `assess only`
- "build", "fix", "add", "write", "update" -> `implement`
- "review", "find bugs", "critique this diff" -> `review`
- "verify", "run tests", "smoke test", "check" -> `test`
- "commit", "stage", "PR", "push" -> `commit` only if commit authority is explicit

If the request mixes modes, choose the narrowest primary mode and list secondary allowed actions under Authority.

### Scope

Make scope concrete enough that another agent could know what is in and out.

Include:

- target repo, file area, feature, artifact, or decision
- explicit exclusions
- expected depth: quick pass, focused slice, or thorough pass

If scope is broad, ask for a narrower target or propose the smallest useful slice.

### Authority

Record permissions explicitly:

```text
Authority:
- Read/search:
- Edit files:
- Run commands/tests:
- Install dependencies:
- Network/external services:
- Create/switch branches:
- Stage/commit:
- Push/open PR:
```

Default to:

- `Read/search: yes`
- `Edit files: no` unless the user asked for implementation or artifact creation
- `Run commands/tests: ask` unless the command is low-risk and local
- `Install dependencies: ask`
- `Network/external services: ask`
- `Create/switch branches: ask`
- `Stage/commit: ask`
- `Push/open PR: ask`

Respect stronger repo or user instructions. If project instructions say "no code changes without approval," require explicit edit authority even for implementation-shaped requests.

### Evidence

Define what counts as done before starting. Use evidence appropriate to the mode:

- `assess only`: cited files, command outputs, risk ranking, recommendation, unknowns
- `implement`: changed files, tests run, behavior verified, remaining risks
- `review`: findings with severity and file/line references, test gaps
- `test`: commands run, pass/fail output, reproduction notes
- `commit`: staged files, commit hash, verification, branch status

If required evidence is missing, report the gap. Propose a standard and ask
only when adequacy is consequential and cannot be resolved from the user's
instructions or existing evidence.

### Stop Condition

State when the agent must pause and ask before continuing.

Default stop conditions:

- scope expands beyond the contract
- authority is missing for a needed action
- tests fail in a way that changes implementation strategy
- a new dependency, service, database, credential, or paid API appears necessary
- destructive or hard-to-reverse action is needed
- evidence cannot be produced
- commit, push, deploy, or external publication is requested but not authorized

## Output Format

Use this format while interviewing:

```text
Draft delegation contract
Mode: <value or Unknown>
Scope: <value or Unknown>
Authority:
- Read/search: <yes/no/ask>
- Edit files: <yes/no/ask>
- Run commands/tests: <yes/no/ask>
- Install dependencies: <yes/no/ask>
- Network/external services: <yes/no/ask>
- Create/switch branches: <yes/no/ask>
- Stage/commit: <yes/no/ask>
- Push/open PR: <yes/no/ask>
Evidence: <value or Unknown>
Stop condition: <value or Unknown>
Assumptions: <short list, or None>

Questions:
1. <only if needed>
```

When all fields are filled, use:

```text
Delegation contract
Mode:
Scope:
Authority:
Evidence:
Stop condition:
```

Then proceed, or say exactly what first action will be taken.

## Quality Bar

Keep the interview tight. The contract is a control surface, not a ceremony. A good contract prevents accidental overreach, vague completion, and hidden escalation while preserving momentum.

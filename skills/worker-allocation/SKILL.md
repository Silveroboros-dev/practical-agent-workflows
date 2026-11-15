---
name: worker-allocation
description: Choose a worker model and reasoning effort for delegated or recurring agent work by expected cost of a verified result. Use when a task is actually being delegated or routed; skip ordinary single-agent answers.
---

# Worker Allocation

Choose the least costly available route likely to complete the task with adequate evidence. Total cost includes model usage, context transfer, tool calls, retries, review, rework, and human intervention. Honor an explicit user choice and the host's current dispatch constraints.

## Select a route

1. Check the **current host's** available workers, model/effort options, inheritance rules, and pricing only when cost affects the choice. Do not assume a model name, tier, price, or override capability from this skill.
2. Classify the task before dispatch:
   - **Mechanical and directly checkable:** bounded file inventory, hash/size comparison, known-ID status lookup, or a fixed command with an objective result. Choose a capable low-cost route and a direct verification check.
   - **Scoped implementation or semantic review:** code changes, tests, evidence interpretation, or a bounded design decision. Choose a route that can reason through the relevant invariants and produce reviewable artifacts.
   - **Complex or consequential reasoning:** concurrency, ambiguous authority, multi-system failures, or an architecture decision with costly mistakes. Use a stronger route or higher effort when the difficulty is known before dispatch, or when a smaller authorized attempt exposed a reasoning limit.
3. Compare the handoff cost with the work. A single simple command can be cheaper to execute locally. Split mechanical verification from semantic judgment only when that reduces total cost without losing context or accountability.
4. Set model and effort only through supported dispatch controls, and report what was actually sent. If a full-history fork inherits the parent's settings, use a supported minimal-context route only when it preserves the required context and authority. If the intended route is unavailable, explain the fallback rather than silently upgrading cost.

Higher effort is not evidence that two models have equal capability. Do not escalate solely because a result was inconvenient. Access denial, missing tools, transport failure, hash mismatch, and unresolved target or authority ambiguity need diagnosis or a stop at the affected step; a stronger model does not grant access or repair evidence.

## Bound the handoff

Give the worker a self-contained packet: objective, exact scope and inputs, existing authority, expected output and completion evidence, stop conditions, and relevant skill or file paths. Preserve inherited authorization without expanding it. Routing creates no new right to mutate, make external calls, publish, commit, push, export, or notify others.

If the user is already working with a visible worker, coordinate through that worker when suitable. Create a new user-visible task only when requested. The coordinator should inspect compact evidence, not repeat every step. Match independent review to impact and uncertainty; keep human decision authority where required.

For a more detailed decision framework, read [references/policy.md](references/policy.md). Revise the route using ordinary authorized work: completion, evidence quality, rework, interventions, time, and usage when available. Do not create a benchmark or quota merely to choose a worker.

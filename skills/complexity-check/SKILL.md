---
name: complexity-check
description: Reduce over-engineering by resolving consequential uncertainty with the cheapest useful evidence before adding architecture or process. Use when simplifying an engineering proposal, challenging speculative abstractions or infrastructure, or deciding how to validate unclear behavior before costly implementation. Skip straightforward changes with understood behavior and routine verification.
---

# Complexity Check

Make added complexity earn its place. Compare total implementation, operation,
maintenance, and human attention costs while preserving the user's requirements.
A short implementation that shifts substantial cost onto its users is not a win.

## Practice

Use only the parts that change the decision; this is not a mandatory phase gate.

1. **Name the consequential uncertainty.** Identify the assumption most likely
   to invalidate the feature or proposed mechanism. State what decision depends
   on it and what observation would change that decision. Start with existing
   evidence; do not manufacture an experiment for a settled question.

2. **Choose the cheapest useful evidence.** Match the method to the uncertainty:
   a decision table or sample outputs for unclear behavior; a small execution
   against the actual dependency for API or integration assumptions; a measured
   workload for performance or scale. A mock demonstrates the mock's behavior.
   Use a reference model only when its behavior is materially cheaper to inspect
   and revise than the implementation and its likely reuse justifies upkeep.
   Timebox investigation according to the cost of being wrong and of delaying
   delivery; avoid a fixed universal budget.

3. **Separate facts from choices.** Record what the evidence establishes and
   what remains unknown. Model/implementation agreement establishes consistency
   on checked cases, not that the policy serves the user. Resolve intent from
   existing instructions first. Ask for human judgment only when a consequential
   choice about desired behavior remains unresolved; present concrete outputs,
   the tradeoff, and a recommendation. Continue independent authorized work;
   keep work that depends on the unresolved choice pending.

4. **Build the smallest sufficient slice.** Prove the uncertain behavior through
   a real path, then complete the authorized deliverable. Preserve useful cases
   as focused regression tests when they protect meaningful behavior. For a
   material omission, identify a concrete check or an observable revisit trigger;
   a list alone is not evidence. If the omission could invalidate the current
   release, resolve it before relying on that release. Keep the note in an
   existing task or artifact when possible.

5. **Justify each additional mechanism.** Connect a proposed abstraction,
   service, agent, gate, or process rule to a concrete requirement or failure and
   explain why a simpler option is insufficient. Count ongoing maintenance and
   review cost. Credible severe failures and known future requirements can
   justify preventive work before an incident occurs. For speculative needs,
   defer the mechanism and name the evidence that would make it worthwhile.
   Recommend retiring existing steps only when their protection is unnecessary
   or adequately covered elsewhere; obtain any required authorization.

## Finish and learn

Stop this check when the evidence supports a decision and the remaining
uncertainty is acceptable for the task's stakes. Resume delivery. If the cheap
check is inconclusive, report the uncertainty and choose the next proportionate
step; do not label uncertainty resolved to meet a timebox.

Before turning the practice into reusable workflow machinery, try it on a real
feature. Briefly record effort, decisions clarified, and observed rework or
failures. Compare with the simpler approach; do not claim hypothetical avoided
work as a measured saving. Keep only mechanisms that earn their ongoing cost.

Do not require reference models, panels, new services, per-assertion mutation
runs, or approval artifacts merely to follow this skill. Simplicity does not
waive correctness, security, required checks, or the user's scope and authority.

## Response

Use a few sentences or a small table covering the material items: uncertainty,
evidence, decision, smallest next step, and remaining limit or revisit trigger.
Do not create a separate report or repeat other skills' handoff fields unless
that artifact serves the user's task.

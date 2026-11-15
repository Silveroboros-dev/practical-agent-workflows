# Answer patterns and claim repairs

All examples are synthetic. Replace brackets only with evidence from the candidate.

## “Why customer-facing engineering?”

> I work well where a software system meets a messy operating workflow. In [supplied project], I had to understand [user constraint], build [specific technical part], and make [control or failure path] explicit. The evidence I have is [artifact or observed result]. That is the kind of ownership I want in a customer-facing engineering role.

Do not claim production impact merely because the motivation sounds persuasive.

## “The agent self-corrected”

Prefer:

> The model proposed [candidate output]. A deterministic validator detected [specific condition], and the controller [rejected, routed, or retried] according to [bound policy]. The test covers [cases]; behavior outside those cases is not yet measured.

## “It was the source of truth”

Prefer:

> [System A] owned [domain]; [System B] owned [other domain]. The service reconciled them for [decision] and recorded conflicts rather than silently choosing one.

## “It was production ready”

Prefer a statement matching the evidence:

- **Prototype:** “The workflow ran end to end in a controlled demo; deployment, operations, and adoption remain unproven.”
- **Pilot:** “A bounded user group used it for [period and workload], with [observed failure/quality metrics].”
- **Production:** “It served [real workload], with [operating owner, monitoring, incident response, and measured results].”

## Customer asks for a risky shortcut

> I would first identify the outcome the customer needs. I would show the concrete failure caused by the shortcut, offer the smallest safer path, and define the evidence and decision owner needed to proceed. If the shortcut is only a tradeoff, I would explain it; if it crosses a policy or access boundary, I would stop the affected action and escalate through the established owner.

## Debugging a failed assistant

> I would trace the input, retrieved evidence, model output, tool calls, deterministic gates, user-visible result, and any external effect. I would reproduce the failure with bound inputs, classify the failed layer, add a targeted regression check, repair the smallest component, and watch for recurrence. I would not infer a model failure from a transport timeout or a user complaint alone.

# Worker allocation decision framework

This is a portable decision aid. Current model names, effort levels, dispatch behavior, prices, and quotas come from the host, not from this file.

## Optimize for a verified result

Estimate total cost as model and tool usage plus context transfer, retries, coordinator review, rework, and human intervention. A cheap first pass that cannot establish the required claim may cost more than a capable single pass. Conversely, a strong model doing hours of fixed mechanical work may waste budget. Use observed task outcomes to revise the route; do not assume statistical equivalence between models or effort levels.

| Task evidence | Route tendency | Verification |
| --- | --- | --- |
| Fixed procedure, exact input, objective output | Lower-cost capable worker if available | Direct file/hash/status or deterministic check |
| Bounded code or document change with clear acceptance criteria | General implementation worker | Focused tests, diff review, or artifact inspection |
| Semantic evidence, policy or provenance interpretation | Stronger reasoning route proportionate to risk | Source-backed rationale and independent review where material |
| Concurrency, multi-system failure, unresolved architecture tradeoff | Higher capability or effort when complexity is known | Reproduce and test the specific failure mode |

The table suggests a route, not an authorization. Mechanical identity matching is different from deciding whether the matched evidence supports a claim. Do not underfund a consequential semantic decision because its input contains hashes or manifests.

## Classify a failed attempt before rerouting

- **Access, authorization, tool availability, or transport:** establish the failed layer. A different model cannot change the permission boundary.
- **Mismatched or missing evidence:** stop the consequential step, preserve the mismatch, and use bounded read-only diagnosis. Continue independent authorized work where useful.
- **Missing context:** inspect the available source or improve the worker packet before paying for a stronger route.
- **Reasoning limit after adequate context:** use a more capable available route, more effort, or independent review, then compare the verified result with the earlier failure.

Do not retry an ambiguous external effect merely by changing worker, model, process, or output path. Existing user authorization persists across a handoff; new scope or external effects still need their own authority.

## Dispatch and review

Use only controls the host actually exposes. A full-history fork may inherit model and effort; a different route may require a fresh packet with selected context. Record the chosen settings and any limitation. Do not invent an unavailable model, hidden dispatcher, price, or fast tier.

A useful packet names the task, source files or IDs, allowed actions, exclusions, acceptance evidence, and stop conditions. Keep it short enough for the worker to orient, complete enough to prevent silent scope drift. Return compact evidence to the coordinator, who checks the material claims and retains consequential decisions. Use independent review when failure would be costly; ordinary directly checked work does not need ceremonial review.

Revisit the routing policy from real authorized tasks using completion, corrections, elapsed time, and total usage if available. Treat a small sample as directional evidence, not a quality benchmark.

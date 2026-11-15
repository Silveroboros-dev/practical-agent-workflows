# Architecture drills

These are synthetic prompts for rehearsal, not facts about the candidate.

## Enterprise intake assistant

A customer wants an assistant to read incoming requests and approve routine exceptions. Ask:

- Which system owns the request, policy, approval, and audit record?
- What information may the model extract, and which decision must deterministic code or a human make?
- How are duplicate requests, stale policy, missing evidence, and contradictory sources handled?
- What is the smallest safe pilot, and what would prove value beyond a demo?
- What happens if the model call succeeds but the response cannot be captured or parsed?

A strong answer names the data contract, authority boundary, explicit abstention path, review queue, idempotency or reconciliation plan, traces without secret payloads, and measurable false-positive/false-negative costs. It does not promise “autonomous approval” before policy and evidence are known.

## Cross-system reporting

A customer asks for one dashboard across two operational systems whose entities and calendars differ. Ask:

- What is the authoritative source for each field and when is it fresh?
- How are entity IDs, currencies, effective dates, and corrections reconciled?
- Which discrepancy blocks a decision, and who resolves it?
- Does the user need a dashboard, a transaction workflow, or both?

A strong answer distinguishes display from system of action and shows a vertical slice with one decision, one reconciled data path, and a measurable baseline. Do not infer that a prettier view fixes inconsistent upstream data.

## Live evaluation incident

A model request may have reached the provider, but the client crashed before persisting a qualifying response. Ask:

- What attempt record existed before the call?
- Can the provider prove whether the operation completed? Does idempotency apply?
- Is a duplicate billable call tolerable and authorized? Could it mutate governed state?
- Which cohort, response, and review artifacts are still valid?

A strong answer preserves the attempt as uncertain, separates external effect from parsing and quality gates, reconciles before retry, and requires exact authority for a successor. It does not turn a broken capture into a failed model result or an automatic retry.

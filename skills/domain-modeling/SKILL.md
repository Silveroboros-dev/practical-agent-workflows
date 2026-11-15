---
name: domain-modeling
description: Clarify or change a project's business concepts, terminology, or consequential design decisions. Use when resolving domain ambiguity, maintaining a glossary, or recording a real tradeoff. Excludes ordinary article editing and documentation phrasing changes.
---

# Domain modeling

Build a shared model of the project's domain: what concepts mean, how they relate, and which decisions explain the design.

## Establish the context

- Read the relevant existing glossary, decision records, and task evidence. Follow an existing glossary map when the project has several business contexts.
- Keep meanings scoped to their context; the same word may legitimately mean different things in different teams or systems.
- Reuse the team's terminology, formats, and knowledge base. Read code, policies, or workflows when needed to check a claimed behavior.

## Resolve material ambiguity

1. Identify overloaded terms, conflicting definitions, or relationships that could change a requirement, behavior, or decision.
2. Check available evidence before asking the user. Distinguish documented intent, observed behavior, and assumptions.
3. Propose a precise meaning and test it with a small number of concrete scenarios, including the edge case most likely to expose a boundary. For example: does cancelling an order also cancel already shipped items?
4. Ask only for unresolved choices that materially affect the task. Batch independent questions and give a recommendation. Continue work that does not depend on their answers.

Use the depth appropriate to the decision. A useful model can have explicitly recorded open questions; it does not require an exhaustive interview.

## Capture the result

Within the user's authorized editing scope, update the relevant existing artifact. An analysis-only request returns proposed changes. Use the destination's authoring workflow and access rules; this skill grants no additional publishing, sharing, or messaging authority.

For a glossary entry, record:

- **Term and context:** the canonical name and where the meaning applies.
- **Meaning:** a concise business definition.
- **Boundary:** a useful inclusion, exclusion, or example when confusion is likely.
- **Aliases:** former or alternative names only when they help readers map existing usage.

Keep implementation choices and task notes outside glossary definitions. Mark proposed meanings and unresolved contradictions explicitly instead of silently turning them into agreed facts.

Record a decision separately when it is costly to reverse, surprising without its context, and the result of a genuine tradeoff. Include the decision, relevant context, alternatives, reasons, consequences, and any condition for revisiting it. Prefer a few useful records over recording every routine choice.

Create a new glossary or decision artifact only when needed to deliver the requested work and consistent with the established destination. Avoid duplicating an existing source of truth.

## Finish

The work is complete when material terms and relationships are consistent with the available evidence, consequential tradeoffs are captured where appropriate, and unresolved choices are visible with their effect on the task. Report the changed artifacts or proposed changes and any remaining blocker briefly.

For human-facing technology posts, use an available `$technical-writing` skill when its trigger applies. If that skill is unavailable, preserve the author's thesis and voice directly. Domain definitions do not replace editorial judgment.

## Provenance

Adapted from [Matt Pocock's domain-modeling skill](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md). Adaptation narrows activation, uses existing project destinations, and allows bounded discovery and explicit open questions. See [LICENSE](LICENSE) for the original MIT notice.

---
name: writing-for-agents
description: Create or edit instructions an AI agent will execute, including SKILL.md, AGENTS.md, and referenced procedures. Human-facing technology posts and ordinary developer documentation are outside this skill's scope.
---

# Writing for agents

Make agent instructions easy to discover, appropriate to the task, and clear about the intended result. Preserve the user's goals and the environment's existing safeguards.

## Establish the contract

- Read the target instructions, applicable local guidance, and relevant examples or observed failures. Identify the intended models and host capabilities when available.
- State the skill's purpose, input, expected deliverable, material constraints, and observable completion criteria. Keep facts, user decisions, and assumptions distinct.
- Reuse existing conventions and validation tools. Change the requested behavior without silently removing unrelated requirements or weakening checks, approval boundaries, or access controls.

## Write the instructions

1. Give each skill a short description with concrete activation cases. Include an exclusion only where a nearby skill or common task would otherwise collide. Match the host's supported metadata and package layout.
2. Put the minimum shared guidance in the entry document. Link task-specific references and scripts behind clear conditions, using paths that resolve in the target environment.
3. Describe the result and decision boundaries first. Add ordered steps where their sequence matters; allow the model to choose routine implementation details.
4. Keep one authoritative location for each rule. Reference discoverable configuration instead of copying it unless the lookup is costly or a hidden convention needs explanation.
5. Prefer concise, positive instructions with checkable completion criteria. Preserve explicit guardrails where required. Treat generic prompting claims as hypotheses to evaluate with the actual model.

Specify which choices the agent can make and which genuinely need user input. Existing authorization remains valid; avoid repeated approval loops. The skill itself grants no new authority to send messages, publish, share, or change permissions. Use destination-specific authoring workflows when saving content.

## Keep writing skills distinct

Use this skill to edit the instructions inside an available `$technical-writing` skill. Preserve that skill's thesis, scale, causal logic, and authorial-voice requirements. If no such skill is installed, use the author's stated editorial requirements.

Use an available `$technical-writing` skill when its trigger fits an authored technology, AI, or API post or article opening. A human-facing article about agents belongs to that editorial workflow when available. This skill applies to executable instructions, including instructions for producing such an article.

For a mixed task, apply each skill to its relevant artifact. Follow any explicitly invoked skills and the host's routing rules.

## Verify and finish

- Run the existing checks relevant to the changed instructions. Keep the original checks and requirements intact; report any unavailable check accurately.
- Validate supported frontmatter, unique naming, package layout, referenced files, and declared dependencies.
- Check activation against a representative intended request, a nearby request that should not activate it, and a mixed case involving an existing skill. Review the body for conflicting or redundant instructions.
- When behavior changes materially, use representative tasks and the same model/context to compare the existing instructions with the proposed revision. Evaluate useful output, human corrections, unnecessary tool use, time, and cost where measurable. Label a static review as a static review.

The work is complete when the requested instructions are saved in the authorized destination, relevant available checks pass, and remaining limitations are reported. Distinguish prepared files from skills successfully registered and active in the user's catalog. A name or description passing validation is not evidence of improved task performance.

## Provenance

Adapted from [Matt Pocock's writing-for-agents skill](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md). This adaptation narrows activation, reduces prescriptive prompting, preserves existing checks, and distinguishes human-facing editorial work. See [LICENSE](LICENSE) for the original MIT notice.

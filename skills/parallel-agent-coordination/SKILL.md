---
name: parallel-agent-coordination
description: Coordinate multiple contributors who will edit the same Git repository through scoped branches, one integrator, and evidence-based handoffs. Use for simultaneous coding agents or shared integration work; skip read-only parallel review and single-writer tasks.
---

# Parallel Agent Coordination

Use this skill when two or more contributors are expected to edit the same repository. Prevent branch and integration races with the repository's actual conventions. This skill does not create branch, network, push, merge, deployment, or publication authority.

## Establish the protocol

Inspect applicable repository instructions and the current checkout before editing. Identify the base branch, remote, review host, active worktrees, dirty files, and existing task branches using the available Git tools. Local `git status --short --branch`, `git rev-parse HEAD`, and `git worktree list` are useful starting points. Fetching a remote or querying a review host needs the task's existing authority and an available connection; if unavailable, report which remote facts remain unknown.

Identify one integrator for the shared base branch. Use an owner already designated by the user or project. If ownership is genuinely unresolved and parallel writes would collide, recommend an integrator and ask for the missing decision while continuing read-only work. Do not create extra agents or a new approval ceremony to follow this skill.

Agree on a compact per-task record:

```text
Base branch and revision:
Integrator:
Worker branch or worktree:
Scoped files or subsystem:
Out of scope:
Expected verification:
Remote/review state:
```

Use the repository's branch naming convention. Each worker should have an isolated branch or worktree for a bounded task. One integrator owns updates to the shared base branch; workers do not push directly to it while parallel work is active.

## Worker practice

Before editing, check the actual branch and working tree. Start from the agreed base revision without discarding another contributor's changes. Create or switch branches only within granted authority. Keep each diff scoped; stage explicit files after reviewing the diff. Do not use `git add .` unless the full diff was reviewed, rewrite another worker's branch without agreement, or force-push the shared base branch.

Run the smallest meaningful checks for the changed behavior using the repository's own test command. `git diff --check` can catch whitespace errors, but it does not replace relevant tests. Before pushing, check the current branch, its base, and whether the same task or commit already has a remote branch. Use one canonical review branch per task. Resolve obvious conflicts limited to your own files; otherwise stop the affected integration and report the conflict.

Report branch and review states precisely:

- **Local branch:** the commit exists only in the current repository.
- **Pushed branch, no review request:** a remote ref exists, but no review request has been opened.
- **Review request opened:** the review host reports an actual request identifier and URL. A URL to a creation form is not an opened request.
- **Merged or deployed:** verify these as separate events; neither follows automatically from a branch push or review request.

Use the actual hosting tool or connector to verify remote and review state when authorized. If it cannot be checked, say so instead of inferring it from a local branch name or a proposed URL. If two remote branches point to the same commit for one task, report the duplicate and choose one canonical review branch before further pushes.

## Integrator practice

The integrator acknowledges active branch scopes, reviews diffs, resolves cross-branch conflicts, and selects the required tests before updating the shared base. Integrate only with the authority granted for that repository. Keep the base branch usable according to its project policy; use its actual merge or fast-forward policy and test command rather than a hardcoded `main`, `origin`, or virtual environment.

An agent or workflow returning `completed` is only a delivery signal. Before accepting a handoff, verify that the expected number of contributors or reviewers is nonzero, all required participants returned, execution errors and missing outputs are zero, and the branch, diff, artifacts, and test results match the claimed revision. Empty findings from zero reviewers are not a clean review.

Agents sharing a checkout, environment, cache, or service state do not provide independent environment evidence. Reproduce an environment-sensitive finding in a genuinely different environment when independence matters, or label it single-environment evidence. Passing tests prove only the named checks on the tested revision and environment. A commit, push, review request, merge, and deployment are distinct states.

## Handoff

Each worker reports enough for the integrator to verify without replaying the whole task:

```text
Branch and worktree:
Commit and base revision:
Remote/review state:
Changed areas:
Verification command, environment, and result:
Known risks and integration order:
```

Honor the repository's actual tracking and ignore rules. Instruction files such as `AGENTS.md` may be tracked project policy; do not blanket-ignore them or change their status to satisfy this skill. Keep local secrets and runtime artifacts out of commits according to the repository's policy.

When a declared single committer remains, direct work on the base branch may be acceptable under project policy. If a second writer begins, establish this protocol before overlapping edits or integration.

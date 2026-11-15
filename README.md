# Practical Agent Workflows

Practical workflows for better decisions, bounded delegation, reliable delivery,
and clear communication. Choose the skill that fits the task; ordinary work does
not require applying the whole collection.

## Try it

- “Challenge this architecture and suggest the cheapest useful validation.”
- “Turn this task into a bounded mission with evidence and stop conditions.”
- “Draft stakeholder questions that will help us choose a migration approach.”
- “Improve these agent instructions while preserving checks and permissions.”
- “Convert this Markdown into readable dark and light HTML, then validate it.”

## Included skills

| Area | Skills |
| --- | --- |
| Discover and decide | `complexity-check`, `domain-modeling`, `to-questionnaire`, `piecemeal-growth` |
| Delegate and deliver | `delegation-contract`, `worker-allocation`, `parallel-agent-coordination`, `evidence-driven-development-cycle` |
| Evaluate and diagnose | `eval-pipeline-governance`, `eval-ui-contract-builder`, `network-failure-diagnosis` |
| Write, review, and design | `writing-for-agents`, `technical-writing`, `video-reasoning-review`, `editorial-visual-design`, `markdown-reading-artifacts` |
| Prepare career evidence | `career-workspace`, `engineering-interview-coach` |

The writing skills have different purposes: `technical-writing` improves prose
for people, while `writing-for-agents` edits instructions an agent will execute.
`editorial-visual-design` offers a particular visual direction when it fits the
request; it does not replace the user's chosen style.

## Install from GitHub

### As a plugin

In a compatible Codex CLI, add this repository as a marketplace:

```bash
codex plugin marketplace add Silveroboros-dev/practical-agent-workflows
```

Then open the host's plugin browser, choose the **Practical Agent Workflows**
marketplace, and install the plugin. Start a new chat or session after installation.
Other hosts may use a different GitHub plugin installation flow.

### Individual skills

Use your host's skill installer with this repository and a directory under
`skills/`. For example, ask Codex:

> Install complexity-check and delegation-contract from
> Silveroboros-dev/practical-agent-workflows.

### Inspect the source

```bash
git clone https://github.com/Silveroboros-dev/practical-agent-workflows.git
cd practical-agent-workflows
```

Cloning provides the source files; it does not enable the plugin in a host.
The repository contains no private configuration or account connections.

## Use in a compatible host

Install through the host's supported plugin or skill workflow. Skill invocation
syntax and available tools vary by host. Select a skill by name or describe its
task; inspect the host's discovery list for the actual installed package path.

Most skills can work with text and files the user supplies. Repo inspection,
browsing, transcription, document authoring, and file changes require suitable
host tools and existing permission. A skill does not add those tools or grant
access to a repository, service, computer, or account.

The Markdown reading-artifact helpers run with Python 3.9 or later and its standard
library in an authorized filesystem environment. They produce self-contained
HTML and an optional static index. They do not deploy or host a website.

## Scope and dependencies

This is a skills-only package. It declares no MCP server, connected app, hook,
scheduled job, publisher-operated backend, or payment flow. Its bundled helpers
do not require an API key. External services used through other host tools keep
their own authentication, permissions, terms, and data handling.

Operational work stays within the user's current authorization. Analysis-only
requests return proposals. Skills distinguish implementation, checks, human
acceptance, and integration, and report uncertainty where evidence is missing.

## Validation and limits

The public edition is checked for package structure, local references,
supporting assets, personal/project identifiers, and selected executable and
behavioral fixtures. Those checks do not establish that every model or host will
follow every workflow correctly. Review outputs before relying on them.

To run the bundled helper regression checks from the package directory:

```bash
python3 -m unittest discover -s skills/markdown-reading-artifacts/tests -v
```

The small renderer supports a useful Markdown subset rather than full CommonMark.
Check unsupported constructs before conversion. Its validator checks structure,
not complete semantic equivalence; generated document metadata currently uses
English as the document language.

## Feedback

Report reproducible problems or propose improvements through the
[repository issues](https://github.com/Silveroboros-dev/practical-agent-workflows/issues).
Include the relevant skill, host, and a minimal example without private data.

## License

MIT for original material and adaptations; retained third-party notices apply
to their respective portions. See [LICENSE](LICENSE) and
[PROVENANCE.md](PROVENANCE.md).

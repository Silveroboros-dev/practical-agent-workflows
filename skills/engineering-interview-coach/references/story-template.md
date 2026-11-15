# Evidence map and story template

Use the candidate's supplied material. The examples here are synthetic and must not be presented as anyone's experience.

| Claim element | Ask for | Safe boundary if absent |
| --- | --- | --- |
| Problem | User, workflow, baseline, constraint | Describe the stated problem as context, not a measured fact |
| System | Components, data flow, source of truth for each domain | Say “the design called for” if only a diagram exists |
| Personal work | Commits, design decisions, ownership, collaborators | State exactly what the candidate did; name team work as team work |
| Deployment | Environment, users, dates, operation record | Call a demo or prototype by that name |
| Result | Baseline, denominator, measurement method, time window | Report observable output or test result without invented impact |
| Reliability | Failure cases, monitoring, recovery, incident evidence | State what was tested and what remains unknown |

## Architecture answer

```text
The user needed [workflow outcome] under [constraints]. The prior process was [observed baseline or explicit unknown].
The system moved [data] from [source] through [transformation and control] to [user action].
I owned [specific components or decisions]; [team/partner] owned [other parts].
We chose [option] over [alternative] because [measured or reasoned tradeoff].
The main failure mode was [specific failure]; we handled or tested it through [control/evidence].
The result I can substantiate is [artifact, test, deployment, usage, or measured outcome]. I cannot yet claim [larger unsupported result].
```

A pre-model enterprise systems story can show relevant field engineering skills when it demonstrates ambiguous workflow discovery, integration contracts, stakeholder ownership, controls, rollout, and measurement. Explain the bridge; do not retroactively call it an AI system.

An AI prototype can demonstrate architecture and failure handling. It does not establish customer adoption or production reliability without deployment and usage evidence.

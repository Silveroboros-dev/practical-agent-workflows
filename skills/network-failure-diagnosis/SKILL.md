---
name: network-failure-diagnosis
description: Diagnose API connection failures, timeouts, remote data-read errors, or apparently stalled tool processes by identifying the failed layer and collecting bounded evidence. Use for uncertain network failure attribution; skip ordinary successful API calls and known local setup fixes.
---

# Network Failure Diagnosis

Identify the last verified successful stage, the observed failure, and the
smallest test that separates the remaining explanations. A timeout, exception
name, or tool yield alone is not a root cause.

## Establish what actually ran

- Inspect existing raw evidence before issuing another request. Record exact
  hostname, endpoint, method, execution host/egress, interpreter and client
  versions, start/end times, and actual exit status. Redact credentials.
- Separate a website, its API hosts, an object store, and the local tool runner.
  They have different routes and access policies. Record a user's reported
  regional restriction with date and affected surface; do not turn it into
  evidence about every related endpoint or into an unverified legal claim.
- Verify the SDK method and its version-specific defaults. A projected query
  may still scan every partition; one logical API call can cause many HTTP
  exchanges and hidden SDK retries. State which unit an existing limit covers.
- Compare raw logs with receipts. Preserve originals and append corrections
  when they disagree. A corrected narrative does not restore overwritten bytes.

## Classify before changing anything

| Observed boundary | What to investigate next |
| --- | --- |
| Import/config failure before a call | Local runtime/dependencies; no network conclusion |
| Resolver failure or unexpected answer | Resolver and returned records; an IP alone does not prove blocking |
| DNS completed, connection did not | Route, proxy, address family, firewall or endpoint reachability; attribution remains open |
| Connection established, TLS failed | Certificate/SNI/trust and the actual TLS error |
| HTTP response received | Status, response headers/body, access denial, rate limit or upstream error |
| Body arrived but parser/Parquet reader failed | Byte completeness, object identity, metadata/schema and decoder compatibility |
| Tool returned a running handle | Process lifecycle; wait on that handle before concluding failure |

A Polars panic may arise while handling remotely fetched bytes. It establishes
a reader failure, not automatically a corrupt file, network outage, or harmless
transport error. An HTTP success also does not prove useful or correct data.

## Choose one discriminating test

Reuse existing bytes or reproduce locally when that answers the question.
For a live test, state the target, operation, host, deadline, retry/operation
budget and expected evidence. Preserve already granted authority; request only
new scope when needed. An exhausted or uncertain allowance is not reset by a
new process, script name, worker or output directory.

Change one relevant variable when practical. Comparing two hosts can establish
different observed outcomes, but it does not by itself isolate geography:
DNS, proxy, route, runtime and time may also differ. Use only authorized hosts;
do not quietly introduce proxy routing or alter firewall/DNS/TLS settings.

For HTTP phase measurements and remote-object consistency checks, read
[references/measurements.md](references/measurements.md).

## Preserve execution and evidence

1. Reserve a unique attempt directory with exclusive creation before network
   work. Persist a started record. Reusing an existing attempt must fail before
   any external call; do not use shared output paths for concurrent launches.
2. Launch once. Retain the tool's returned session/cell identifier, show it to
   the coordinator through the tool output, and resume that same operation.
   In Codex, `exec_command` sessions are polled with `write_stdin`;
   `functions.exec` running cells are resumed with `functions.wait`.
   A yield is not a timeout or an exit. Avoid an extra `nohup` launch as a
   substitute for polling a process that may still be running.
3. Keep body bytes, transport metadata, and stderr separate. Record terminal
   exit status, elapsed time and sanitized exception details/stack. Protect raw
   diagnostics privately: URLs, headers and traces may contain credentials.
   Return a sanitized report, never an environment dump or signed URL.
4. If the process disappears or evidence is incomplete, record uncertainty and
   check the original operation. Do not count it as unstarted, successful or an
   empty result. Ambiguous external outcomes cannot justify an automatic retry.
5. Hash completed captures and record their source/version/extent before
   parsing. If an old capture mixed a body and diagnostic trailer, validate the
   exact known framing; preserve the original and identify the parsed derivative.

## Close the diagnosis

Report observed facts, rejected explanations, remaining hypotheses, and one
next discriminating action. State the count of launched logical operations,
known transport attempts and uncertainty separately. Do not report an exact
count when duplicate launches or overwritten files prevent reconciliation.

Keep product semantics unchanged while repairing transport or execution.
Failed retrieval is not zero matches; partial coverage is not catalog-wide
absence. Do not replace failed evidence with synthetic data or relabel success
to make the workflow pass. Validate a proposed repair against its observed
failure before resuming the original task.

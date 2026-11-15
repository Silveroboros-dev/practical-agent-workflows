---
name: video-reasoning-review
description: Analyze videos, podcasts, talks, interviews, or their transcripts in the context of the user's topics and projects. Retrieve or transcribe the spoken content, reconstruct the argument, identify the strongest and weakest reasoning with timestamps, verify pivotal current claims, and turn the result into an actionable brief or social post. Use for evidence-grounded video review; do not use for simple playback, editing, or reproducing a full copyrighted transcript.
---

# Video Reasoning Review

Turn long-form video into a context-aware argument audit. Answer the useful question—whether the reasoning is sound and relevant—not merely what was said.

## Establish the job

Accept a URL, local audio/video file, or transcript. Also use any supplied:

- focus topics or projects;
- desired depth: `quick`, `deep`, or `post`;
- audience and output language;
- specific question, decision, or hypothesis to test.

Default to `quick` when the user asks for a fast read, `deep` when they ask to assess, challenge, or fact-check the reasoning, and `post` when they want publishable copy. If no mode is clear, use a concise standard review between `quick` and `deep`.

Infer low-risk omissions from the prompt and current workspace context, and state the assumption briefly. Do not block on optional preferences. Respond in the user's language unless they request another.

## Invocation examples

The user can invoke `$video-reasoning-review` or ask for the same work in natural language. A URL is enough to identify the source when the host can access a transcript or transcribe authorized media. Optional mode, focus, language, and audience can come from the request; do not assume the host has retrieval or transcription tools.

```text
$video-reasoning-review <URL> — quick
Focus on the implications for a small software team.
```

```text
$video-reasoning-review <URL> — deep
Check the main inference, pivotal factual claims, hidden assumptions,
and the strongest counterargument.
```

```text
$video-reasoning-review <URL> — post
Draft a concise post for the stated audience, keeping claims and caveats distinct.
```

```text
$video-reasoning-review <LOCAL VIDEO, AUDIO, OR TRANSCRIPT FILE>
Assess which ideas apply to the supplied project decision and what evidence is missing.
```

Read [references/review-rubric.md](references/review-rubric.md) for a deep review or when its argument rubric and example topic lenses would help. Apply lenses to the user's actual question rather than treating the examples as a fixed agenda. Drafting a post does not authorize publishing or sharing it.

## Acquire trustworthy source material

1. Record the title, creator or speakers, recording date when disclosed, publication date, duration, canonical URL, and available chapters. Treat this as working metadata; show only the fields useful to the requested output, and mark material unavailable fields as `not provided` rather than searching indefinitely.
2. Prefer source material in this order: a user-designated transcript; publisher captions or transcript; platform captions; locally generated speech-to-text.
3. Preserve timestamps and speaker labels. For an unlabeled interview transcript, use neutral labels such as `host` and `guest` only when turn-taking or context makes the attribution reliable; otherwise use `speaker` and disclose the limitation.
4. When transcription is required, use existing tools first. Keep downloaded media and intermediate files temporary unless the user asks to retain them. Do not add dependencies or mutate the user's project merely to process a video. If a durable installation or a large model download is necessary, explain the time, size, and privacy tradeoff before proceeding when approval is required.
5. If no available, authorized tool can retrieve or transcribe the source, report that limitation and ask for a transcript or another accessible source. Do not infer the video's argument from its title, description, or comments.
6. Record transcript provenance and limitations: official, automatic captions, local speech-to-text, partial coverage, language mismatch, or inaudible passages. Never silently repair uncertain wording.

Use the minimum media needed. Audio is normally sufficient; inspect visuals only when slides, charts, demonstrations, or on-screen text carry part of the argument.

Do not reproduce a full copyrighted transcript. Paraphrase by default and use only short excerpts when wording itself matters. A user-provided or user-owned transcript may be handled according to the user's stated rights and request.

## Reconstruct the reasoning

Build a claim map rather than a chronological recap:

- state the central thesis and major supporting claims;
- separate premises, evidence, inference, prediction, value judgment, and conclusion;
- identify hidden assumptions and material counterarguments;
- distinguish each speaker's position from the reviewer's assessment;
- attach a timestamp or timestamp range to every speaker claim and every piece of video-derived evidence discussed in the review.

Evaluate inferential quality and empirical support separately. A claim can be conceptually well reasoned yet poorly evidenced. Judge strength on both axes, not because the conclusion is appealing. Judge weakness by naming the exact broken link: missing evidence, scope shift, correlation treated as causation, anecdote used as a base rate, false dichotomy, inconsistent time horizon, ignored counterevidence, or an unfalsifiable prediction.

Steelman the best opposing case. For important conclusions, say what new evidence would change the assessment.

## Verify only load-bearing claims

Fact-check claims that materially support the thesis, are current or unstable, are high-stakes, or are easy to misremember. Do not spend most of the review verifying decorative facts. The `verdict` means the decision-relevant assessment of the central thesis plus whether the video is worth the user's time for the requested focus.

- Prefer primary sources, official data, original research, filings, and direct documentation.
- Use the disclosed recording date as the historical cutoff when available; otherwise use publication date. Separate what was reasonably knowable at that cutoff from what is known now whenever the distinction changes the verdict, in every mode.
- Label findings `supported`, `partly supported`, `unsupported`, `contradicted`, or `unknown`.
- Cite the source next to the finding. Never turn an unverified recollection into a fact.
- Clearly label inferences made from sources.
- In `quick` mode, verify one representative pivotal claim when needed, list other load-bearing current claims as unverified, and lower confidence rather than implying that the broader empirical thesis is established.

## Make timestamps useful

Use clickable deep links when the platform supports them. For YouTube, link to the canonical video at the relevant start second, for example `https://www.youtube.com/watch?v=VIDEO_ID&t=502s`. Avoid duplicate or conflicting time parameters. For local files or unsupported platforms, use `HH:MM:SS` or `MM:SS` labels.

If transcript timing is coarse, prefix the time with `≈`. If no reliable timing exists, say `timestamp unavailable`; never invent precision.

## Deliver the review

Lead with the verdict in two to four sentences: whether the video is worth the user's time, its most valuable idea, its biggest limitation, and an overall `high`, `medium`, or `low` confidence. Add claim-level confidence only when it materially differs.

Then provide, in the depth appropriate to the selected mode:

1. A compact argument map.
2. The strongest arguments with timestamps, the supporting evidence, and why the inference works.
3. The weakest arguments with timestamps, the precise failure, and the strongest charitable counter-reading.
4. A short pivotal-claim fact-check when external verification materially changes confidence.
5. Relevance to each requested topic or project: implications, testable hypotheses, and concrete next actions—not generic thematic similarity. If the video does not cover a topic sufficiently, say `insufficient coverage` and give the cheapest useful validation test instead of inventing implications.
6. The best segments to watch, including why each earns the time.
7. A provenance note covering transcript source, coverage, and confidence.

For `post` mode, perform the analysis first, then produce social-ready copy that preserves the distinction between the speaker's claims and the reviewer's conclusions. Match the requested platform and language. Prefer a clear thesis, a few specific insights, one honest caveat, and a closing question over clickbait.

Keep the main response concise. Put detailed claim tables or research notes after the decision-relevant conclusions, or offer them as a separate artifact when they would overwhelm the result.

## Quality bar

- Do not confuse a polished speaker with a well-supported argument.
- Do not reduce disagreement to a single numerical score; explain the important dimensions.
- Preserve uncertainty and disagreements between sources.
- Separate technical capability, workflow adoption, customer value, vendor economics, and valuation when the speaker moves between those layers.
- Look for meaningful limitations in convincing material and useful insights in weak material. Report only findings supported by the source; do not invent a balance quota.
- If the transcript is incomplete enough to undermine the audit, narrow the claims or report the limitation rather than bluffing.

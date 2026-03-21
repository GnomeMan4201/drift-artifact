# I Built a Document That Demonstrates AI Drift — On Itself

*A method for writing that shows you what iterative AI generation actually does to coherence.*

---

## The problem I kept running into

Every time I tried to explain how AI personalization systems drift — how a loop that was accurate six months ago can be confidently wrong today — I ended up with an article. Competent, readable, correct. And completely unable to make you *feel* what I was describing.

The concept is this: iterative systems don't preserve coherence. They reconstruct it each pass. Confidence increases even as alignment drifts. You can read that sentence and understand it. You cannot fully believe it until you experience it.

So I built something that would make you experience it.

---

## What a Drift Artifact is

A **Drift Artifact** is a document produced across multiple passes through prompt space, where register degradation is preserved intentionally and instrumented explicitly.

The document doesn't describe a system behavior. It performs it.

Here's the structure:

- **Pass 1 — Institutional:** High formality, full argument, long sentences, precise vocabulary
- **Pass 2 — Compression:** Same content, reduced syntax, shorter clauses, elevated hedging
- **Pass 3 — Drift:** Informal register, slang intrusion, capitalization rules suspended
- **Pass 4 — Collapse:** Fragments. Near-terminal coherence. Still arriving, technically.
- **Convergence:** A step outside the loop that reframes the entire document as output, not article

Between each pass: system log annotations. Not commentary — instrumentation. Lines like:

```
> register shift detected
> feedback loop stabilized — local maximum reached — divergence unobserved
> collapse confirmed — prior register irrecoverable
```

These read like console output because they're meant to. The document has a control plane.

---

## The three-channel system

What makes this more than a writing experiment is that the degradation runs across three parallel channels simultaneously:

**Linguistic channel** — sentence structure collapses, register fragments, syntax breaks down  
**Visual channel** — contrast fades with each pass, typography shifts from serif to sans to mono  
**Structural channel** — system logs expose state transitions the prose doesn't acknowledge

All three must degrade in sync. A single channel holding while the others collapse reads as inconsistency. All three degrading together reads as signal.

The typography is not styling. It is part of the data.

---

## The calibration problem

The hardest design constraint: the artifact has to stay inside this boundary —

> *The reader feels the degradation but is not blocked by it.*

Too little fade: drift is imperceptible, argument is lost.  
Too much fade: reader exits before convergence, argument is lost.

The correct target is an experience where each pass requires slightly more effort than the last — but all passes are completable. The convergence has to land. If the reader quits in pass 4, the whole thing fails.

After iteration, the contrast values that work are:

```css
/* light mode */
--p1-color: #1a1a1a;
--p2-color: #2a2a2a;
--p3-color: #444444;
--p4-color: #666666;
```

Perceptible decay. No cliff.

---

## The core claim

This is the portable thesis underneath the method:

> Iterative AI-assisted writing does not preserve coherence. It reconstructs it each pass, and alignment can drift while confidence increases.

This is not a new observation about prompt engineering. It is a demonstration of a known mechanism in a form designed to make the mechanism observable — in real time, on the reader, using the document itself as the test environment.

---

## The artifact

[→ Read the Drift Artifact](link-to-artifact)

The HTML version is the canonical form. The typography cascade is doing active work — the plain text version loses the visual channel and with it roughly a third of the argument.

---

## The method (if you want to build one)

The skeleton is repeatable:

```
1. Generate initial pass — high coherence, high formality
2. Iterate across N passes — compress → shift → collapse
3. Preserve drift — no normalization between passes
4. Instrument transitions — logs + pass markers
5. Converge — name the loop from outside the loop
6. Attach generation trace — document transformation types per pass
```

The repo is at [github.com/gnomeman4201/drift-artifact](https://github.com/gnomeman4201/drift-artifact) with method documentation and extension paths (adversarial prompts, memory injection, cross-model comparisons).

---

## Why this format

Because there's a difference between understanding something and having seen it operate on you.

The convergence section of the artifact ends with this:

> *You have now seen it operate on you.*

That sentence only works if the preceding 2,000 words actually did what they claimed to. The artifact is a test it has to pass to make its argument.

That's the part I couldn't do with a normal article.

---

*GnomeMan4201 builds offensive security tools and writes about adversarial systems, AI behavior, and tools that do things.*  
*[DEV.to](https://dev.to/gnomeman4201) · [GitHub](https://github.com/gnomeman4201)*

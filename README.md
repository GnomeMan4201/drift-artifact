# Drift Artifact (Prompt-Space Execution)

A method for producing documents that demonstrate iterative authorship instability as part of their argument.

---

## What this is

A **Drift Artifact** is a document produced across multiple passes through prompt space, where register degradation is preserved intentionally and instrumented explicitly.

The document does not describe a system behavior. It performs it.

---

## Core claim

> Iterative AI-assisted writing does not preserve coherence. It reconstructs it each pass. Alignment can drift while confidence increases.

---

## The method
```
1. Generate initial pass — high coherence, high formality
2. Iterate across N passes
   - compression
   - tone shift
   - collapse
3. Preserve drift — no normalization between passes
4. Instrument transitions — logs + pass markers
5. Converge — reframe the document as output, not article
6. Attach generation trace
```

---

## Repo structure
```
drift-artifact/
  /artifact
    drift_artifact_v2.html
  /method
    companion-post.md
    social-hooks.md
  CALIBRATION.md
  README.md
```

---

## Artifact

Live: https://gnomeman4201.github.io/drift-artifact/artifact/drift_artifact_v2.html

---

*drift-artifact // badBANANA research // GnomeMan4201*

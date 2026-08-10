# Drift Artifact

**A static research artifact and production method for preserving measurable authorship drift across iterative AI-assisted writing passes.**

[![Static validation](https://github.com/GnomeMan4201/drift-artifact/actions/workflows/validate.yml/badge.svg)](https://github.com/GnomeMan4201/drift-artifact/actions/workflows/validate.yml)
[![Live artifact](https://img.shields.io/badge/live-artifact-222222)](https://gnomeman4201.github.io/drift-artifact/artifact/drift_artifact_v2.html)

---

## What this is

A **Drift Artifact** is deliberately produced across multiple prompt-space passes while changes in register, compression, framing, and coherence are preserved instead of normalized away. The output is both a document and an instrumented example of the process being discussed.

The project tests a narrower claim than “AI writing always degrades”:

> Iterative AI-assisted rewriting can reconstruct coherence differently from pass to pass, allowing alignment and authorship characteristics to drift even when the resulting prose remains confident and superficially coherent.

The artifact demonstrates the method. It does not, by itself, establish how often that behavior occurs across models, prompts, writers, or domains.

---

## View the artifact

Hosted version:

**https://gnomeman4201.github.io/drift-artifact/artifact/drift_artifact_v2.html**

Local preview requires no package installation:

```bash
git clone https://github.com/GnomeMan4201/drift-artifact.git
cd drift-artifact
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/artifact/drift_artifact_v2.html
```

The repository intentionally has no runtime dependencies; `requirements.txt` records that fact explicitly.

---

## Method

```text
1. Generate an initial pass with a defined register and purpose.
2. Iterate across N controlled transformations.
3. Preserve the resulting drift instead of normalizing every pass.
4. Instrument transitions with pass markers and generation trace.
5. Compare the trajectory rather than only the final document.
6. Publish the artifact together with its method and calibration notes.
```

Useful variables to preserve between experiments include model/version, prompt text, transformation order, temperature or sampling settings when available, manual edits, timestamps, and any context introduced between passes.

---

## Repository structure

```text
drift-artifact/
├── artifact/
│   └── drift_artifact_v2.html   # primary rendered research artifact
├── method/
│   ├── companion-post.md        # explanatory publication material
│   └── social-hooks.md          # supporting publication notes
├── CALIBRATION.md               # calibration / interpretation notes
├── requirements.txt             # explicitly no runtime dependencies
└── README.md
```

---

## Verify the checkout

Run the zero-dependency static validation:

```bash
python3 tools/validate_artifact.py
```

The validation checks that the primary artifact exists, is non-empty, contains expected document markers, and can be parsed by Python's standard HTML parser. GitHub Actions runs the same check on pushes and pull requests.

This is a **packaging/integrity smoke test**. It does not validate the research claim, measure semantic drift, or establish causal attribution to a model.

---

## Calibration and interpretation

Read [`CALIBRATION.md`](CALIBRATION.md) before treating visible changes between passes as evidence. The useful unit is the documented transformation sequence plus its trace, not an isolated final paragraph.

For stronger experiments, compare against controls such as:

- repeated generation without an instructed transformation
- human-only revision across the same number of passes
- reordered transformation sequences
- multiple model families or versions
- blinded reviewer judgments alongside machine-derived similarity metrics

---

## Scope

This repository is a research artifact, not a general-purpose writing application. Its value is reproducibility of the demonstrated method and transparency about what the artifact can and cannot support.

---

*drift-artifact // badBANANA research // GnomeMan4201*

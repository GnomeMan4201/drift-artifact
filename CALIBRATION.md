# Calibration — Drift Artifact Visual System

Documentation of contrast values, rationale, and the calibration constraint.

---

## The constraint

> The reader feels the degradation but is not blocked by it.

This is the only rule that matters. Everything else is tuning toward it.

---

## The three failure modes

| Mode | Symptom | Cause |
|---|---|---|
| Under-faded | Drift imperceptible | Passes too similar, effect invisible |
| Over-faded | Reader exits pass 3 or 4 | Contrast too low, engagement breaks |
| Cliff | Sharp drop at one pass | Uneven decay curve, reads as error |

The correct target is a smooth, even decay where each pass costs ~10–15% more effort than the last. No single pass should feel like a wall.

---

## Light mode values

```css
--p1-color: #1a1a1a;   /* 16.7:1 on white — full readability */
--p2-color: #2a2a2a;   /* 13.2:1 — imperceptibly shifted     */
--p3-color: #444444;   /*  9.7:1 — clearly degraded, readable */
--p4-color: #666666;   /*  5.7:1 — strained, legible          */

--log-color: #666666;  /* same as p4 — logs are instrumentation, not content */
--preface-color: #555555; /* slightly higher — preface is load-bearing framing */
--marker-color: #999999;  /* lowest — chrome, not signal */
```

WCAG AA minimum: 4.5:1 for body text. All passes clear it. Pass 4 clears with margin.

---

## Dark mode values

```css
--p1-color: #e4e4e0;   /* ~16:1 on #1a1a1a background — full */
--p2-color: #d0d0cc;   /* ~12:1 — imperceptibly shifted       */
--p3-color: #a0a09c;   /*  ~7:1 — clearly degraded, readable  */
--p4-color: #787874;   /* ~4.5:1 — strained, legible          */

--log-color: #787874;
--preface-color: #909090;
--marker-color: #686864;
```

Dark mode decay is symmetric with light mode: same perceptual distance per step, calculated from the opposite end of the luminance scale.

---

## Font stack cascade

Typography degrades in parallel with contrast:

| Pass | Font family | Rationale |
|---|---|---|
| Pass 1 | Georgia (serif) | Formal, editorial, maximum authority |
| Pass 2 | Helvetica Neue (sans) | Utilitarian, compressed, still coherent |
| Pass 3 | Helvetica Neue (sans) | Same stack, degraded color — continuity breaking |
| Pass 4 | Courier New (mono) | Terminal register — system output, not authorship |
| Convergence | Georgia (serif) | Register recovery — return signals reframe |

The serif → sans → mono cascade mimics the linguistic register collapse. A reader who doesn't consciously notice the font shift still feels it.

---

## System log weighting

Logs are structural instrumentation. They should not degrade with the passes.

```css
.log {
  color: var(--log-color);  /* #666 light / #787 dark */
  background: var(--log-bg);
  border-left: 1px solid var(--border);
}
```

Logs remain at a fixed contrast level across all passes. This creates a deliberate tension: as the body text fades, the system logs hold their weight. The control plane remains legible even as the content collapses.

That tension is intentional. It is part of the argument.

---

## The anchor event log

One log in pass 3 functions differently from the others:

```
> feedback loop stabilized — local maximum reached — divergence unobserved
```

This is placed immediately after the "cage" paragraph — where the user describes feeling trapped by a recommendation system. The log names the same moment from the system's perspective: not entrapment, but stabilization. Not divergence, but convergence.

The gap between what the system reports and what the user experiences is the thesis in a single line.

---

## Emphasis in collapse (pass 4)

```css
.p4 em {
  font-style: normal;
  color: #505050;   /* slightly above p4 body — #666 */
}
```

In collapse, `em` does not mean emphasized. It means residual signal — fragments of prior coherence still readable through the noise. The slight contrast increase above p4 body text performs this: something is still there, barely.

---

## What to adjust if replicating

If you are building a new Drift Artifact for a different argument:

1. **Keep the constraint** — feel the degradation, complete the loop
2. **Adjust the pass count** — 4 is the tested minimum; more passes = more gradual decay per step
3. **Keep the font cascade** — serif → sans → mono is not decorative, it is data
4. **Keep the log separation** — logs must hold contrast while body fades
5. **The convergence must earn its reframe** — if the reader didn't feel the drift, the convergence reads as a claim, not a demonstration

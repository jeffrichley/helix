---
name: ml-experimentation
description: Experimental discipline for neural-net training, benchmark iteration, and model-quality improvement.
---

Use this skill when the task is about model training, hyperparameters, architecture,
optimizer changes, or benchmark-driven ML iteration.

## Goal

Improve a target metric under explicit compute, memory, latency, or stability
constraints.

## Working Rules

- establish a baseline first
- change one major factor at a time when possible
- record both quality and cost metrics
- separate crashes, instability, and poor ideas
- avoid overfitting to tiny or unrepresentative eval slices

## Typical Metrics

- validation loss
- task score
- bits per byte
- throughput
- wall-clock time
- memory usage
- training stability

## Evaluation Guidance

- keep changes that improve the target metric without unacceptable cost regressions
- discard changes that improve speed while damaging correctness or quality
- retry runs with invalid measurement or obvious execution failure
- branch promising but riskier ideas that need more evidence

## Common Failure Modes

- noisy comparisons
- invalid baselines
- changing too many variables
- comparing runs with different evaluation conditions
- keeping unstable wins that do not reproduce

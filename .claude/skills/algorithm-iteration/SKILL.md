---
name: algorithm-iteration
description: Correctness-preserving algorithm and implementation improvement through bounded experiments.
---

Use this skill when the task is improving an algorithm, implementation, or system
behavior while preserving correctness.

## Goal

Improve the chosen objective, such as throughput, latency, memory use, or code
clarity, without breaking behavior.

## Working Rules

- confirm the baseline and hot path first
- prioritize correctness before speed
- prefer targeted changes over wide refactors
- profile before optimizing non-obvious bottlenecks
- retain attribution by limiting variables per experiment

## Evaluation Guidance

- require correctness checks on every meaningful change
- compare against a stable benchmark, not intuition
- treat microbenchmark wins skeptically if system-level performance does not improve
- prefer simpler changes when gains are comparable

## Common Failure Modes

- optimizing the wrong path
- using noisy benchmarks
- confusing asymptotic improvement with practical improvement
- accepting regressions on edge cases

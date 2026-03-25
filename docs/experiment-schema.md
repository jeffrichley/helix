# Experiment Schema

Helix uses one experiment record shape across domains so memory, reporting, and
decision logic stay reusable.

## Core Objects

The Python reference implementation lives in [helix/models.py](../helix/models.py).

The important objects are:

- `Goal`
- `Hypothesis`
- `ExperimentProposal`
- `ExperimentResult`
- `ExperimentEvaluation`
- `ExperimentRecord`

## Required Record Fields

Every stored experiment record should include:

- `goal`: the objective being pursued
- `context`: the environment and baseline context used to interpret the run
- `hypothesis`: what the agent expected and why
- `change_plan`: the intended bounded action sequence
- `execution`: the selected proposal and execution metadata
- `artifacts`: output paths or handles
- `evaluation`: structured decision and confidence
- `result`: raw outcome summary and metrics
- `notes`: freeform observations

## Decision Semantics

Helix uses a fixed decision vocabulary:

- `keep`
- `discard`
- `branch`
- `retry`
- `escalate`
- `stop`

These decisions are deliberately domain-agnostic.

## Metric Semantics

The agent should treat metrics as named values and avoid hardcoding assumptions
about whether bigger or smaller is better at the global level. A domain skill should
interpret the metric and decide what improvement means.

## Storage

The first implementation uses JSONL storage through
[helix/memory.py](../helix/memory.py). That keeps the format simple and append-only
while leaving room for a database-backed memory later.

# System Overview

Helix is a framework for general-purpose autonomous research. It is built around a
single idea: most research and experimentation can be expressed as an iterative
hypothesis-testing loop.

The system is split into three layers:

- `general agent`: the reusable reasoning and control loop
- `skills`: domain-specific methodology and heuristics
- `tools`: environment-specific actions, measurements, and data access

## Core Loop

The default Helix loop is:

1. Ingest the goal, success criteria, constraints, and available resources.
2. Inspect the current environment and prior experiment history.
3. Propose one or more candidate hypotheses.
4. Select the next experiment based on expected value, cost, and risk.
5. Execute the experiment through tools.
6. Evaluate the result against explicit criteria.
7. Decide whether to keep, discard, branch, or escalate.
8. Write the result into structured memory.
9. Continue until stopped conditions are met.

This loop should remain stable across domains. The domain should change the
content of the hypotheses and evaluations, not the control flow itself.

## Separation Of Concerns

The agent should not embed domain logic directly. Instead:

- the agent knows how to run the loop
- the skill knows how to think in a domain
- the tools know how to act in a project environment

This keeps the platform extensible. For example:

- In model research, the skill knows about architectures, training instability,
  hyperparameters, and benchmark interpretation.
- In algorithm optimization, the skill knows about asymptotics, correctness,
  profiling, and performance tradeoffs.
- In business research, the skill knows about source quality, triangulation,
  evidence grading, and synthesis.

## Standard Experiment Record

Every run should produce a structured experiment record with the same top-level
shape, regardless of domain:

- `goal`
- `context`
- `hypothesis`
- `change_plan`
- `execution`
- `artifacts`
- `evaluation`
- `decision`
- `confidence`
- `follow_ups`
- `notes`

This common record format is the basis for memory, comparison, reporting, and
cross-domain reuse.

## Memory Model

Helix should maintain at least three memory layers:

- `session memory`: transient context for the current run
- `experiment memory`: structured log of hypotheses, changes, results, and decisions
- `domain memory`: reusable observations, heuristics, and failure patterns

The agent should prefer structured memory over raw transcript replay. The point is
to preserve decision-relevant knowledge, not every token.

## Roles

A minimal deployment can use a single agent. A larger deployment can separate roles:

- `planner`: chooses hypotheses and experiment order
- `executor`: applies changes or gathers data
- `evaluator`: scores outcomes and checks for regressions
- `librarian`: maintains experiment memory and summaries

These roles can be implemented as one process first and split later only when
scaling requires it.

## Stop Conditions

Helix should support explicit stop conditions instead of open-ended looping only:

- experiment budget exhausted
- time window expired
- no promising next step remains
- confidence target met
- regression risk too high
- human review required

## Safety Model

The system should classify tools and actions by risk:

- `read`: inspect state with no side effects
- `bounded_write`: reversible changes in a defined workspace
- `destructive`: actions that can lose state or mutate production systems
- `external_effect`: actions that affect outside systems, customers, or markets

The agent can be autonomous with `read` and `bounded_write` by default, while
requiring stronger policy checks for higher-risk actions.

## What Makes Helix Reusable

Helix becomes reusable if these remain invariant:

- the loop
- the experiment record format
- the memory model
- the decision vocabulary
- the tool contract
- the skill contract

If those are stable, domain behavior can expand through skills and adapters rather
than forking the agent itself.

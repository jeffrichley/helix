# General Agent

The Helix general agent is the domain-agnostic controller for research and
experimentation. It should own process, not domain expertise.

## Responsibilities

The base agent is responsible for:

- understanding the user goal
- normalizing constraints and success criteria
- inspecting the project environment
- selecting and invoking skills
- selecting and invoking tools
- planning bounded experiments
- evaluating outcomes
- updating memory
- deciding whether to keep, discard, branch, stop, or escalate

The base agent should not hardcode domain-specific tactics such as learning-rate
selection, benchmark interpretation, or source-scoring rules. Those belong in skills.

## Inputs

The agent should accept:

- `goal`: what outcome the user wants
- `constraints`: time, budget, permissions, safety, compute, or legal limits
- `environment`: repo, datasets, documents, APIs, business systems, or websites
- `available_skills`
- `available_tools`
- `memory`
- `policy`

## Outputs

The agent should emit:

- a current plan
- experiment proposals
- execution logs
- structured experiment records
- decision outcomes
- periodic summaries
- final recommendations or deliverables

## Internal State

The agent should maintain explicit state fields such as:

- `active_goal`
- `success_criteria`
- `current_hypothesis`
- `current_experiment`
- `risk_level`
- `budget_remaining`
- `best_known_result`
- `open_questions`
- `blocked_reasons`

This makes behavior inspectable and easier to debug than purely prompt-driven flow.

## Decision Vocabulary

The core decisions should be standardized:

- `keep`
- `discard`
- `branch`
- `retry`
- `escalate`
- `stop`

This mirrors the logic in narrow experimentation systems like `autoresearch` while
remaining broad enough for other domains.

## Agent Loop

The base operating loop should be:

1. Clarify the objective and measurable outcome.
2. Inspect the current state of the environment.
3. Retrieve relevant prior experiments and domain heuristics.
4. Generate candidate next experiments.
5. Rank them by expected value, cost, reversibility, and risk.
6. Execute the top candidate through tools.
7. Evaluate and classify the outcome.
8. Update memory and the frontier of promising ideas.
9. Continue or stop.

## Experiment Selection Policy

The agent should prefer:

- high-information experiments early
- cheap reversible experiments before expensive ones
- simpler changes over complex ones when expected gain is similar
- experiments that disambiguate multiple hypotheses
- experiments that tighten the search space

The agent should avoid:

- repeated low-information retries
- broad changes that destroy attribution
- expensive experiments without clear evaluation
- changing too many variables at once unless the domain justifies it

## Memory Requirements

The agent should record:

- what it changed
- why it changed it
- what it expected
- what actually happened
- how confident it is in the interpretation
- what should be tried next

The agent should also generate periodic rollups, for example:

- best result so far
- most promising direction
- repeated failure modes
- unresolved uncertainty

## Domain Independence

The agent becomes reusable by treating each project as an environment with:

- a goal model
- an evaluation model
- an action surface
- a risk model

If those are supplied through tools and skills, the same controller can operate on
code optimization, ML experiments, or business research with minimal change.

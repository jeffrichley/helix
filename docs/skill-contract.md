# Skill Contract

Skills are domain modules that teach the Helix general agent how to reason well in a
specific class of projects.

The purpose of a skill is not to replace the agent loop. The purpose is to inject
domain methodology into that loop.

## What A Skill Contains

Each skill should provide five things:

1. `domain framing`
2. `experiment heuristics`
3. `evaluation guidance`
4. `failure patterns`
5. `output conventions`

## Required Skill Interface

Each skill should define the following sections in a stable format.

### 1. Scope

- What kinds of goals the skill applies to
- What kinds of environments it expects
- What it explicitly does not cover

### 2. Objectives

- Common success metrics in the domain
- Typical tradeoffs
- Secondary metrics and guardrails

### 3. Experiment Templates

- Common experiment patterns
- How large or small changes should be
- What a baseline run looks like
- When to use ablations, comparisons, or exploratory sweeps

### 4. Evaluation Rules

- How to interpret outcomes
- What counts as a meaningful improvement
- What counts as noise
- What evidence is required before promoting a result

### 5. Failure Modes

- Known ways the agent can misread signals
- Common implementation errors
- Common evaluation pitfalls
- When to escalate to human review

### 6. Tool Usage Guidance

- Which tools are usually relevant
- Safe order of operations
- Tool-specific caveats
- When to prefer read-only inspection over mutation

### 7. Reporting Conventions

- Required artifacts
- Naming rules
- Summary format
- Decision tags or status vocabulary

## Skill Design Principles

Skills should be:

- `methodological`, not procedural spaghetti
- `opinionated`, but evidence-driven
- `portable` across multiple projects in the same domain
- `small enough` to load selectively
- `explicit` about assumptions and boundaries

## Examples

### ML Experimentation Skill

Should teach:

- baseline-first workflow
- isolate one major variable when possible
- track compute, throughput, and memory with quality metrics
- distinguish instability from bad ideas
- avoid overfitting to tiny validation slices

### Algorithm Optimization Skill

Should teach:

- correctness before speed
- benchmark design and noise control
- asymptotic versus constant-factor wins
- profiling before major rewrites
- regression checks on edge cases

### Business Research Skill

Should teach:

- source quality ranking
- claim-evidence separation
- triangulation across independent sources
- recency sensitivity
- confidence scoring and citation discipline

## Skill Loading

The base agent should load only the skills relevant to the current goal. Skills should
be composable, but conflicts must be resolved explicitly.

For example:

- a `python-code-optimization` skill may combine with a `benchmarking` skill
- a `business-research` skill may combine with a `source-validation` skill
- an `ml-training` skill may combine with a `gpu-experimentation` skill

## Skill Output To The Agent

A skill should not merely be text. Conceptually, it should yield:

- `recommended_metrics`
- `recommended_experiment_patterns`
- `risk_flags`
- `interpretation_hints`
- `tool_preferences`
- `promotion_thresholds`

This can start as markdown and later become structured configuration.

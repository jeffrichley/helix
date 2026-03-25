# Tool Contract

Tools are the environment interface for Helix. If skills teach the agent how to think,
tools determine how the agent can act and measure.

The tool contract should be stable across domains so the agent can reason about tool
use generically.

## Tool Categories

Helix tools should usually fall into one of these categories:

- `inspect`: read the current state
- `change`: apply a bounded modification
- `execute`: run a process or workflow
- `evaluate`: score an outcome against criteria
- `record`: persist memory, artifacts, or summaries
- `communicate`: report or request review

## Required Metadata

Every tool should publish metadata that the agent can rely on:

- `name`
- `purpose`
- `inputs`
- `outputs`
- `side_effect_level`
- `reversibility`
- `cost_class`
- `timeout_behavior`
- `failure_modes`
- `artifacts_emitted`

## Standard Side-Effect Levels

Tools should declare one of:

- `read_only`
- `workspace_mutation`
- `external_mutation`
- `destructive`

The agent should use this classification when selecting autonomous actions.

## Tool Design Principles

Tools should:

- do one meaningful job clearly
- return high-signal outputs
- avoid dumping unnecessary raw context
- expose stable, explicit parameters
- encode common multi-step actions when that reduces agent error
- be safe to retry when practical

This mirrors the lesson from tool design for LLMs generally: agent ergonomics matter
at least as much as raw capability.

## Recommended Response Shape

Tools should return a normalized structure whenever possible:

- `status`
- `summary`
- `data`
- `artifacts`
- `metrics`
- `warnings`
- `next_options`

That gives the general agent a predictable interface for comparison and follow-up.

## Minimal Project Adapter

A new project should become Helix-compatible by implementing a small adapter layer.
The minimum useful adapter should expose tools for:

- environment inspection
- baseline execution
- experiment execution
- result extraction
- artifact capture
- rollback or reset
- persistent experiment recording

## Example Tool Sets

### ML Experimentation

- `inspect_training_repo`
- `run_training_experiment`
- `parse_training_metrics`
- `compare_checkpoint_results`
- `record_experiment_result`
- `revert_code_to_baseline`

### Algorithm Improvement

- `inspect_codebase`
- `run_test_suite`
- `run_benchmark`
- `profile_hot_paths`
- `compare_outputs`
- `record_performance_result`

### Business Research

- `search_sources`
- `fetch_document`
- `extract_claims`
- `score_source_quality`
- `synthesize_findings`
- `record_research_brief`

## Evaluators As First-Class Tools

Evaluation should not be implicit. Helix should treat evaluators as first-class tools.
That means every serious workflow should expose tools that answer questions like:

- Did the result improve?
- By how much?
- Is the change statistically or practically meaningful?
- What regressed?
- How confident should we be?

Without explicit evaluators, the agent drifts into subjective judgment.

## Artifact Contract

Every execution and evaluation tool should declare where artifacts go, for example:

- logs
- reports
- result tables
- benchmark outputs
- generated deliverables
- snapshots or checkpoints

A research system becomes much easier to audit once artifacts are first-class outputs.

## Future Direction

The initial implementation can wrap local scripts and filesystem operations. Later,
the same contract can support:

- remote workers
- sandboxed runners
- cloud experiments
- browser tools
- data warehouses
- external APIs

The important part is keeping the contract stable while adapters change underneath.

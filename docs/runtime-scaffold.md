# Runtime Scaffold

Helix now includes a minimal Python scaffold for the generalized architecture.

## Package Layout

- [helix/agent.py](../helix/agent.py): base controller and single-step run loop
- [helix/models.py](../helix/models.py): typed experiment and decision schema
- [helix/contracts.py](../helix/contracts.py): abstract skill and tool contracts
- [helix/memory.py](../helix/memory.py): append-only JSONL experiment memory
- [helix/skills/algorithm_improvement.py](../helix/skills/algorithm_improvement.py): first example skill
- [helix/tools/mock.py](../helix/tools/mock.py): first example tool adapter

## What This Scaffold Does

- selects applicable skills for a goal
- asks those skills for experiment proposals
- ranks proposals with a simple reusable heuristic
- executes the selected experiment through a tool
- evaluates the result through the selected skill
- persists a normalized experiment record

## What It Does Not Do Yet

- multi-step autonomous looping
- branching worktrees or git integration
- rich policy enforcement
- concurrent workers
- remote execution
- domain-specific adapters for ML or business research

Those can now be added against concrete contracts instead of more prose-only design.

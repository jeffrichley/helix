# helix

Helix is a reusable framework for autonomous research and experimentation.

The core idea is to separate three concerns:

- A general research agent that owns the experiment loop
- Skills that teach domain-specific methodology
- Tools that expose concrete actions and evaluations in a project environment

This lets the same agentic system work across different domains:

- model training and tuning
- algorithm improvement
- software performance optimization
- business and market research
- other hypothesis-driven work with measurable outcomes

## Architecture

- [System Overview](docs/system-overview.md)
- [General Agent](docs/general-agent.md)
- [Skill Contract](docs/skill-contract.md)
- [Tool Contract](docs/tool-contract.md)
- [Experiment Schema](docs/experiment-schema.md)
- [Runtime Scaffold](docs/runtime-scaffold.md)

## Design goal

Helix is not meant to be a single hardcoded "research agent". It is meant to be a
general iterative research runtime:

1. Understand the goal and constraints.
2. Form a hypothesis.
3. Execute a bounded experiment.
4. Evaluate the result.
5. Keep, discard, branch, or escalate.
6. Record what was learned.
7. Repeat.

The reusable part is the loop. Skills and tools adapt that loop to a domain.

## Reference Runtime

The repo now includes a small Python scaffold for the architecture:

- [helix/agent.py](helix/agent.py)
- [helix/models.py](helix/models.py)
- [helix/contracts.py](helix/contracts.py)
- [helix/memory.py](helix/memory.py)
- [helix/skills/algorithm_improvement.py](helix/skills/algorithm_improvement.py)
- [helix/tools/mock.py](helix/tools/mock.py)

This is intentionally minimal. It establishes the contracts and a single-step
research loop without yet committing to a large runtime or a single domain.

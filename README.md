# helix

Helix is a markdown-first repository for reusable autonomous research workflows.

The repo is structured around the way current coding agents are commonly extended:

- `AGENTS.md` at the repo root for persistent, repo-wide agent instructions
- `.claude/agents/*.md` for specialized subagents
- `.claude/skills/<skill>/SKILL.md` for reusable domain skills

The design goal is to support one general research agent that can be adapted to
different domains by loading the right markdown skillset instead of rewriting the
agent itself.

## Current Layout

- [AGENTS.md](AGENTS.md): repo-wide operating model for a general experimentation agent
- [.claude/agents/research-orchestrator.md](.claude/agents/research-orchestrator.md): primary coordinating agent
- [.claude/agents/evaluator.md](.claude/agents/evaluator.md): result interpretation and keep/discard judgment
- [.claude/agents/tool-designer.md](.claude/agents/tool-designer.md): tool and adapter design specialist
- [.claude/skills/research-loop/SKILL.md](.claude/skills/research-loop/SKILL.md): base experimentation loop
- [.claude/skills/ml-experimentation/SKILL.md](.claude/skills/ml-experimentation/SKILL.md): neural-net and benchmark iteration
- [.claude/skills/algorithm-iteration/SKILL.md](.claude/skills/algorithm-iteration/SKILL.md): correctness-preserving algorithm improvement
- [.claude/skills/business-research/SKILL.md](.claude/skills/business-research/SKILL.md): evidence-based market and business research
- [.claude/skills/tool-design/SKILL.md](.claude/skills/tool-design/SKILL.md): agent-facing tool design guidance

## Model

Helix assumes:

- one reusable general agent
- domain-specific skills
- project-specific tools

The agent owns the loop:

1. clarify the goal
2. inspect the environment
3. form a bounded hypothesis
4. execute an experiment or research step
5. evaluate the result
6. keep, discard, branch, retry, or escalate
7. record what was learned

The skills supply domain judgment. The tools supply the action surface.

## Why Markdown First

This repo is intentionally biased toward markdown control files instead of a custom
runtime because that matches the current extension model used by modern coding
agents more closely. The point of Helix is to define reusable behavior and structure
that agents can load directly.

## References

- [System Overview](docs/system-overview.md)
- [General Agent](docs/general-agent.md)
- [Skill Contract](docs/skill-contract.md)
- [Tool Contract](docs/tool-contract.md)

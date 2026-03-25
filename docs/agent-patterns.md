# Agent Patterns

Helix is now organized around the markdown extension patterns used by current
coding agents.

## Compatibility Pattern

- `AGENTS.md` is the repo-wide instruction surface for Codex-style agents.
- `.claude/agents/*.md` contains specialized subagents.
- `.claude/skills/<name>/SKILL.md` contains reusable skills that can be loaded
  automatically or invoked directly in Claude-style workflows.

## Why This Structure

This structure keeps the reusable behavior in markdown instead of locking it into a
custom runtime too early.

That gives Helix three useful properties:

- the general operating model is visible and easy to edit
- domain specialization happens by adding skills, not rewriting the base agent
- tool design guidance can evolve alongside actual project adapters

## Initial Helix Set

The initial set is intentionally small:

- one general operating file: [AGENTS.md](../AGENTS.md)
- three specialized agents:
  [research-orchestrator](../.claude/agents/research-orchestrator.md),
  [evaluator](../.claude/agents/evaluator.md),
  [tool-designer](../.claude/agents/tool-designer.md)
- five skills:
  [research-loop](../.claude/skills/research-loop/SKILL.md),
  [ml-experimentation](../.claude/skills/ml-experimentation/SKILL.md),
  [algorithm-iteration](../.claude/skills/algorithm-iteration/SKILL.md),
  [business-research](../.claude/skills/business-research/SKILL.md),
  [tool-design](../.claude/skills/tool-design/SKILL.md)

## Intended Use

The expected usage is:

1. start from [AGENTS.md](../AGENTS.md)
2. load `research-loop`
3. add exactly the domain skill or skills needed
4. use specialized agents when the platform supports delegation
5. evolve the skill library as new project classes emerge

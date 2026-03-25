---
name: tool-design
description: Design guidance for agent-facing tools and project adapters.
---

Use this skill when designing, refining, or documenting tools for agent use.

## Principles

- choose tools based on workflows, not raw API coverage
- prefer clear tool boundaries
- return high-signal context only
- optimize for token efficiency
- make wrong usage difficult
- provide actionable errors

## Tool Checklist

For each tool, define:

- purpose
- inputs
- outputs
- side effects
- reversibility
- typical call patterns
- failure modes

## Strong Patterns

- search tools instead of dump-everything tools
- higher-level workflow tools instead of thin wrappers when the workflow is common
- output formats that the agent can read and chain easily
- namespacing that reduces ambiguity across many tools

## Weak Patterns

- overlapping tools with vague boundaries
- responses bloated with irrelevant metadata
- opaque errors
- parameters that require hidden context to use correctly

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class Decision(str, Enum):
    KEEP = "keep"
    DISCARD = "discard"
    BRANCH = "branch"
    RETRY = "retry"
    ESCALATE = "escalate"
    STOP = "stop"


class SideEffectLevel(str, Enum):
    READ_ONLY = "read_only"
    WORKSPACE_MUTATION = "workspace_mutation"
    EXTERNAL_MUTATION = "external_mutation"
    DESTRUCTIVE = "destructive"


@dataclass(slots=True)
class Goal:
    name: str
    description: str
    success_metric: str
    constraints: list[str] = field(default_factory=list)
    stop_conditions: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Hypothesis:
    summary: str
    rationale: str
    expected_outcome: str
    risk_level: str = "medium"
    tags: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ExperimentProposal:
    title: str
    hypothesis: Hypothesis
    change_plan: list[str]
    evaluation_plan: list[str]
    expected_value: float
    expected_cost: float
    reversibility: float
    risk_score: float
    skill_name: str | None = None

    def priority_score(self) -> float:
        # Higher is better. Favor value and reversibility, penalize cost and risk.
        return (self.expected_value * 2.0) + self.reversibility - self.expected_cost - self.risk_score


@dataclass(slots=True)
class ExperimentResult:
    status: str
    summary: str
    metrics: dict[str, float] = field(default_factory=dict)
    artifacts: list[str] = field(default_factory=list)
    raw_data: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ExperimentEvaluation:
    decision: Decision
    reason: str
    confidence: float
    score_delta: float | None = None
    regressions: list[str] = field(default_factory=list)
    next_steps: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ExperimentRecord:
    goal: Goal
    context: dict[str, Any]
    hypothesis: Hypothesis
    change_plan: list[str]
    execution: dict[str, Any]
    artifacts: list[str]
    evaluation: ExperimentEvaluation
    result: ExperimentResult
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

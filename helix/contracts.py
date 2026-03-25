from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .models import ExperimentEvaluation, ExperimentProposal, ExperimentResult, Goal, SideEffectLevel


@dataclass(slots=True)
class ToolMetadata:
    name: str
    purpose: str
    side_effect_level: SideEffectLevel
    reversibility: str
    cost_class: str
    timeout_behavior: str
    artifacts_emitted: list[str] = field(default_factory=list)
    failure_modes: list[str] = field(default_factory=list)


class HelixTool(ABC):
    metadata: ToolMetadata

    @abstractmethod
    def invoke(self, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError


class HelixSkill(ABC):
    name: str
    description: str

    @abstractmethod
    def applies_to(self, goal: Goal) -> bool:
        raise NotImplementedError

    @abstractmethod
    def propose_experiments(self, goal: Goal, context: dict[str, Any]) -> list[ExperimentProposal]:
        raise NotImplementedError

    @abstractmethod
    def evaluate_result(
        self,
        goal: Goal,
        proposal: ExperimentProposal,
        result: ExperimentResult,
        context: dict[str, Any],
    ) -> ExperimentEvaluation:
        raise NotImplementedError

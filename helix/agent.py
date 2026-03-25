from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .contracts import HelixSkill, HelixTool
from .memory import JsonlExperimentMemory
from .models import Decision, ExperimentProposal, ExperimentRecord, ExperimentResult, Goal


@dataclass(slots=True)
class AgentState:
    active_goal: Goal | None = None
    best_known_score: float | None = None
    open_questions: list[str] = field(default_factory=list)
    blocked_reasons: list[str] = field(default_factory=list)


class HelixAgent:
    def __init__(
        self,
        skills: list[HelixSkill],
        tools: dict[str, HelixTool],
        memory: JsonlExperimentMemory | None = None,
    ) -> None:
        self.skills = skills
        self.tools = tools
        self.memory = memory or JsonlExperimentMemory()
        self.state = AgentState()

    def applicable_skills(self, goal: Goal) -> list[HelixSkill]:
        return [skill for skill in self.skills if skill.applies_to(goal)]

    def propose(self, goal: Goal, context: dict[str, Any]) -> list[ExperimentProposal]:
        proposals: list[ExperimentProposal] = []
        for skill in self.applicable_skills(goal):
            proposals.extend(skill.propose_experiments(goal, context))
        return sorted(proposals, key=lambda proposal: proposal.priority_score(), reverse=True)

    def select_next_experiment(self, goal: Goal, context: dict[str, Any]) -> ExperimentProposal:
        proposals = self.propose(goal, context)
        if not proposals:
            raise ValueError(f"No skills produced experiments for goal '{goal.name}'.")
        self.state.active_goal = goal
        return proposals[0]

    def execute(self, proposal: ExperimentProposal, context: dict[str, Any]) -> ExperimentResult:
        tool_name = context.get("experiment_tool")
        if not tool_name:
            raise ValueError("Context must include 'experiment_tool'.")
        if tool_name not in self.tools:
            raise KeyError(f"Unknown experiment tool '{tool_name}'.")
        payload = self.tools[tool_name].invoke(proposal=proposal, context=context)
        return ExperimentResult(
            status=payload.get("status", "unknown"),
            summary=payload.get("summary", ""),
            metrics=payload.get("metrics", {}),
            artifacts=payload.get("artifacts", []),
            raw_data=payload.get("data", {}),
            warnings=payload.get("warnings", []),
        )

    def evaluate(self, goal: Goal, proposal: ExperimentProposal, result: ExperimentResult, context: dict[str, Any]):
        skill = next((skill for skill in self.skills if skill.name == proposal.skill_name), None)
        if skill is None:
            applicable = self.applicable_skills(goal)
            skill = applicable[0] if applicable else None
        if skill is None:
            raise ValueError(f"No skill available to evaluate goal '{goal.name}'.")
        evaluation = skill.evaluate_result(goal, proposal, result, context)
        score = result.metrics.get(goal.success_metric)
        if score is not None and evaluation.decision == Decision.KEEP:
            if self.state.best_known_score is None:
                self.state.best_known_score = score
            else:
                self.state.best_known_score = max(self.state.best_known_score, score)
        return evaluation

    def run_once(self, goal: Goal, context: dict[str, Any]) -> ExperimentRecord:
        proposal = self.select_next_experiment(goal, context)
        result = self.execute(proposal, context)
        evaluation = self.evaluate(goal, proposal, result, context)
        record = ExperimentRecord(
            goal=goal,
            context=context,
            hypothesis=proposal.hypothesis,
            change_plan=proposal.change_plan,
            execution={
                "proposal_title": proposal.title,
                "evaluation_plan": proposal.evaluation_plan,
                "skill_name": proposal.skill_name,
            },
            artifacts=result.artifacts,
            evaluation=evaluation,
            result=result,
            notes=[],
        )
        self.memory.append(record)
        return record

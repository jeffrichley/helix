from __future__ import annotations

from .base import KeywordSkillMixin
from ..contracts import HelixSkill
from ..models import Decision, ExperimentEvaluation, ExperimentProposal, ExperimentResult, Goal, Hypothesis


class AlgorithmImprovementSkill(KeywordSkillMixin, HelixSkill):
    name = "algorithm_improvement"
    description = "Guidance for correctness-preserving algorithm and implementation improvement."
    keywords = ("algorithm", "performance", "latency", "throughput", "benchmark", "optimiz")

    def applies_to(self, goal: Goal) -> bool:
        return self.goal_matches(goal)

    def propose_experiments(self, goal: Goal, context: dict[str, object]) -> list[ExperimentProposal]:
        baseline = float(context.get("baseline_score", 0.0))
        return [
            ExperimentProposal(
                title="Establish baseline and hot path",
                hypothesis=Hypothesis(
                    summary="A focused benchmark and profiling pass will identify the best next optimization.",
                    rationale="Optimization work should start by confirming the real bottleneck.",
                    expected_outcome="A reliable baseline and a ranked list of candidate hotspots.",
                    risk_level="low",
                    tags=["baseline", "profiling"],
                ),
                change_plan=[
                    "Run the benchmark suite against the current implementation.",
                    "Profile the hottest code path and capture the dominant cost centers.",
                    "Use the results to constrain later code changes.",
                ],
                evaluation_plan=[
                    "Verify correctness stays unchanged.",
                    f"Record the baseline value for {goal.success_metric}.",
                ],
                expected_value=max(0.5, baseline + 0.3),
                expected_cost=0.2,
                reversibility=1.0,
                risk_score=0.1,
                skill_name=self.name,
            ),
            ExperimentProposal(
                title="Apply one targeted optimization",
                hypothesis=Hypothesis(
                    summary="A narrow change on the hottest path can improve the target metric without harming correctness.",
                    rationale="Small isolated changes preserve attribution and are easier to revert.",
                    expected_outcome="Improved benchmark result with tests still passing.",
                    risk_level="medium",
                    tags=["optimization", "correctness"],
                ),
                change_plan=[
                    "Modify only the hottest path identified by the profiler.",
                    "Keep behavior identical and avoid broad refactors.",
                    "Re-run tests and benchmarks after the change.",
                ],
                evaluation_plan=[
                    "Compare benchmark delta against baseline.",
                    "Reject changes that improve speed but break edge-case correctness.",
                ],
                expected_value=max(0.8, baseline + 0.5),
                expected_cost=0.6,
                reversibility=0.8,
                risk_score=0.4,
                skill_name=self.name,
            ),
        ]

    def evaluate_result(
        self,
        goal: Goal,
        proposal: ExperimentProposal,
        result: ExperimentResult,
        context: dict[str, object],
    ) -> ExperimentEvaluation:
        baseline = float(context.get("baseline_score", 0.0))
        score = result.metrics.get(goal.success_metric)
        tests_passed = result.raw_data.get("tests_passed", True)
        if not tests_passed:
            return ExperimentEvaluation(
                decision=Decision.DISCARD,
                reason="Correctness regressed.",
                confidence=0.95,
                regressions=["Tests failed after the change."],
                next_steps=["Revert the change and isolate a smaller optimization."],
            )
        if score is None:
            return ExperimentEvaluation(
                decision=Decision.RETRY,
                reason=f"Missing success metric '{goal.success_metric}' in result.",
                confidence=0.6,
                next_steps=["Fix metric extraction before attempting another optimization."],
            )
        delta = score - baseline
        if delta > 0:
            return ExperimentEvaluation(
                decision=Decision.KEEP,
                reason="Benchmark improved without correctness regression.",
                confidence=0.85,
                score_delta=delta,
                next_steps=["Use the new result as the next baseline."],
            )
        return ExperimentEvaluation(
            decision=Decision.DISCARD,
            reason="No measurable improvement over baseline.",
            confidence=0.8,
            score_delta=delta,
            next_steps=["Try a different hotspot or a smaller isolated change."],
        )

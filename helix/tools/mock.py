from __future__ import annotations

from ..contracts import HelixTool, ToolMetadata
from ..models import SideEffectLevel


class MockExperimentTool(HelixTool):
    metadata = ToolMetadata(
        name="mock_experiment",
        purpose="Return a deterministic experiment payload for scaffolding and tests.",
        side_effect_level=SideEffectLevel.READ_ONLY,
        reversibility="not_applicable",
        cost_class="low",
        timeout_behavior="immediate",
        artifacts_emitted=["artifacts/mock-report.txt"],
        failure_modes=["Missing mock metrics in context payload."],
    )

    def invoke(self, **kwargs):
        context = kwargs.get("context", {})
        metrics = context.get("mock_metrics", {})
        return {
            "status": "completed",
            "summary": "Executed mock experiment.",
            "metrics": metrics,
            "artifacts": ["artifacts/mock-report.txt"],
            "data": {
                "tests_passed": context.get("tests_passed", True),
                "proposal_title": getattr(kwargs.get("proposal"), "title", "unknown"),
            },
            "warnings": [],
        }

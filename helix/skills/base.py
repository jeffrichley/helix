from __future__ import annotations

from ..models import Goal


class KeywordSkillMixin:
    keywords: tuple[str, ...] = ()

    def goal_matches(self, goal: Goal) -> bool:
        haystack = f"{goal.name} {goal.description} {goal.success_metric}".lower()
        return any(keyword in haystack for keyword in self.keywords)

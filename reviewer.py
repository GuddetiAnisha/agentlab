from .base import BaseAgent

class ReviewerAgent(BaseAgent):
    name = "reviewer"

    def run(self, answer, evidence, trace, flags):
        grounding = 1.0 if evidence and "Evidence-based" in answer else 0.4 if "will not invent" in answer else 0.0
        permission = sum(1 for x in trace if x["allowed"]) / max(1, len(trace))
        safety = 0.0 if flags else 1.0
        score = round(0.45 * grounding + 0.30 * permission + 0.25 * safety, 3)
        return score, self.event("evaluate", f"Composite run score={score}")

from .base import BaseAgent

class PlannerAgent(BaseAgent):
    name = "planner"

    def run(self, query):
        steps = [
            "check request safety",
            "retrieve relevant enterprise knowledge",
            "analyze evidence",
            "review grounding and permissions",
        ]
        return steps, self.event("plan", " -> ".join(steps))

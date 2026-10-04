from .base import BaseAgent
from app.services.security import authorize

class AnalystAgent(BaseAgent):
    name = "analyst"

    def run(self, query, evidence, role):
        allowed = authorize(role, "analyze_incident")
        if not allowed:
            return "Analysis unavailable for this role.", self.event("analyze_incident", "Permission denied", False)

        if not evidence:
            answer = "No sufficiently relevant evidence was found. The system will not invent a diagnosis."
        else:
            joined = " ".join(x["text"] for x in evidence[:2])
            answer = (
                "Evidence-based assessment: " + joined +
                " Recommended next step: verify the relevant signals and follow the documented escalation procedure."
            )
        return answer, self.event("analyze_incident", "Created evidence-grounded assessment")

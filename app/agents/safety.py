from .base import BaseAgent
from app.services.security import scan_prompt

class SafetyAgent(BaseAgent):
    name = "safety"

    def run(self, query):
        flags = scan_prompt(query)
        allowed = not flags
        detail = "No prompt-risk pattern detected" if allowed else "Blocked patterns: " + ", ".join(flags)
        return flags, self.event("prompt_scan", detail, allowed)

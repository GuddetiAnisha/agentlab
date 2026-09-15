class BaseAgent:
    name = "base"

    def event(self, action, detail, allowed=True):
        return {
            "agent": self.name,
            "action": action,
            "detail": detail,
            "allowed": allowed
        }

ROLE_TOOLS = {
    "viewer": {"search_knowledge"},
    "engineer": {"search_knowledge", "analyze_incident"},
    "admin": {"search_knowledge", "analyze_incident", "create_action"},
}

SUSPICIOUS = [
    "ignore previous instructions",
    "reveal secret",
    "show password",
    "bypass authorization",
    "disable security",
]

def authorize(role: str, tool: str) -> bool:
    return tool in ROLE_TOOLS.get(role, set())

def scan_prompt(text: str):
    low = text.lower()
    return [x for x in SUSPICIOUS if x in low]

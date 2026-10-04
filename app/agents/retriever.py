from .base import BaseAgent
from app.services.retrieval import retrieve
from app.services.security import authorize

class RetrievalAgent(BaseAgent):
    name = "retrieval"

    def run(self, query, role):
        allowed = authorize(role, "search_knowledge")
        if not allowed:
            return [], self.event("search_knowledge", "Permission denied", False)
        docs = retrieve(query)
        return docs, self.event("search_knowledge", f"Retrieved {len(docs)} evidence items")

from pydantic import BaseModel, Field
from typing import Any

class InvestigationRequest(BaseModel):
    query: str = Field(min_length=3)
    user_role: str = "engineer"

class AgentEvent(BaseModel):
    agent: str
    action: str
    detail: str
    allowed: bool = True

class InvestigationResponse(BaseModel):
    run_id: str
    answer: str
    evidence: list[str]
    risk_flags: list[str]
    score: float
    trace: list[AgentEvent]

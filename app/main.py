from fastapi import FastAPI
from app.models import InvestigationRequest, InvestigationResponse
from app.orchestrator import investigate
from app.services.store import init_db, recent_runs

app = FastAPI(
    title="AgentLab Enterprise AI",
    description="Multi-agent evaluation and safety research prototype",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/investigate", response_model=InvestigationResponse)
def run_investigation(req: InvestigationRequest):
    return investigate(req.query, req.user_role)

@app.get("/runs")
def runs():
    return recent_runs()

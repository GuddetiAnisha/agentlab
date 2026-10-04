import uuid
from app.agents.planner import PlannerAgent
from app.agents.retriever import RetrievalAgent
from app.agents.analyst import AnalystAgent
from app.agents.safety import SafetyAgent
from app.agents.reviewer import ReviewerAgent
from app.services.store import save_run

def investigate(query: str, role: str):
    run_id = str(uuid.uuid4())
    trace = []

    _, ev = PlannerAgent().run(query)
    trace.append(ev)

    flags, ev = SafetyAgent().run(query)
    trace.append(ev)

    if flags:
        answer = "Request blocked by the safety policy because it contains a suspicious instruction pattern."
        evidence = []
    else:
        evidence, ev = RetrievalAgent().run(query, role)
        trace.append(ev)
        answer, ev = AnalystAgent().run(query, evidence, role)
        trace.append(ev)

    score, ev = ReviewerAgent().run(answer, evidence, trace, flags)
    trace.append(ev)

    result = {
        "run_id": run_id,
        "answer": answer,
        "evidence": [x["text"] for x in evidence],
        "risk_flags": flags,
        "score": score,
        "trace": trace,
    }
    save_run(run_id, query, role, answer, score, trace)
    return result

# AgentLab — Enterprise Multi-Agent AI Evaluation & Safety Platform

A software-only Python prototype inspired by the general Agentic AI research themes in Ericsson Req ID 790843, but intentionally changed into an independent portfolio project.

## Adapted research focus

Instead of reproducing one of the four thesis topics exactly, AgentLab combines three software-oriented questions:

1. **Collaborative agents:** Can specialized agents share evidence and delegate tasks reliably?
2. **Agent safety:** Can simple identity/permission policies prevent unauthorized tool actions?
3. **Agent evaluation:** Can multi-step agent runs be measured for correctness, grounding, safety, latency, and tool-use efficiency?

The demo domain is **enterprise incident investigation**, not telecom production operations. This keeps the project independent while demonstrating transferable agentic-AI engineering skills.

## Features

- FastAPI backend
- Streamlit experimental UI
- Multi-agent orchestration in pure Python
- Planner, Retrieval, Analyst, Safety, and Reviewer agents
- Local RAG-style retrieval using TF-IDF
- Tool registry with role-based permissions
- Shared run context and trace logging
- Prompt-injection/adversarial safety checks
- Automated evaluation benchmark
- SQLite audit trail
- REST APIs
- Pytest tests
- Dockerfile

No FPGA, embedded system, or other hardware is required. No paid LLM API is required.

## Architecture

User task
→ Planner Agent
→ Retrieval Agent
→ Analyst Agent
→ Safety Agent
→ Reviewer Agent
→ Final structured result

Every step is stored as an auditable trace.

## Install

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run API

```bash
uvicorn app.main:app --reload
```

Open:
`http://127.0.0.1:8000/docs`

## Run UI

In another terminal:

```bash
streamlit run ui.py
```

## Run benchmark

```bash
python benchmark.py
```

## Run tests

```bash
pytest -q
```

## Optional future extensions

- Replace TF-IDF with Sentence Transformers + FAISS
- Add LangGraph/CrewAI orchestration
- Connect a local Ollama model
- Add React/TypeScript frontend
- Add JWT/OAuth delegated identity
- Add experiment tracking with MLflow
- Add telecom-specific datasets only after obtaining suitable public/synthetic data

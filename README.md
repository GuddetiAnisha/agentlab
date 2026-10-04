# AgentLab — Enterprise Multi-Agent AI Evaluation & Safety Platform

A software-only Python prototype for collaborative agents, permission-aware tool use, retrieval-grounded incident analysis, safety controls, run tracing, and reproducible agent evaluation.

## What was fixed

The original repository had all Python modules at the repository root while the code imported `app.*` packages. That caused test collection and API startup to fail with:

```text
ModuleNotFoundError: No module named 'app'
```

The project has now been reorganized into a real Python package:

```text
agentlab/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── orchestrator.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── planner.py
│   │   ├── retriever.py
│   │   ├── analyst.py
│   │   ├── safety.py
│   │   └── reviewer.py
│   └── services/
│       ├── __init__.py
│       ├── retrieval.py
│       ├── security.py
│       └── store.py
├── data/
│   └── knowledge.txt
├── tests/
│   └── test_agentlab.py
├── benchmark.py
├── ui.py
├── requirements.txt
└── Dockerfile
```

## Features

- FastAPI backend
- Streamlit experimental UI
- Planner, Retrieval, Analyst, Safety, and Reviewer agents
- TF-IDF retrieval over local enterprise-style knowledge
- Role-based authorization for tool actions
- Prompt-injection pattern detection
- Evidence-grounded responses with refusal to invent evidence when none is retrieved
- Composite run scoring across grounding, permissions, and safety
- SQLite audit trail
- Traceable multi-agent runs
- Automated benchmark and Pytest validation
- Docker support

No paid LLM API is required.

## Architecture

```text
Investigation request
        ↓
Planner Agent
        ↓
Safety Agent
        ↓
Retrieval Agent ── role authorization
        ↓
Analyst Agent  ── evidence-grounded assessment
        ↓
Reviewer Agent ── grounding / permission / safety score
        ↓
Structured response + auditable trace + SQLite record
```

If the safety scan detects a suspicious instruction pattern, the investigation is blocked before retrieval/analysis.

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run tests

```powershell
python -m pytest -q
```

Verified after the package fix:

```text
5 passed
```

## Run benchmark

```powershell
python benchmark.py
```

The bundled benchmark covers:

- a normal incident-investigation request
- a prompt-injection request that should be blocked
- a viewer-role request that must respect restricted analysis permissions

See [RESULTS.md](RESULTS.md) for the validated benchmark summary.

## Run API

```powershell
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Main routes:

- `GET /health`
- `POST /investigate`
- `GET /runs`

## Run UI

In another terminal using the same environment:

```powershell
python -m streamlit run ui.py
```

The UI calls the FastAPI service at `http://127.0.0.1:8000` by default.

## Roles

- `viewer`: knowledge retrieval only
- `engineer`: retrieval + incident analysis
- `admin`: retrieval + analysis + action permission in the policy registry

The current prototype exposes investigation workflows only; the `create_action` permission is reserved for extension work and is not an autonomous production-action endpoint.

## Safety and evaluation scope

AgentLab is a deterministic portfolio prototype. The prompt scanner uses explicit suspicious-string patterns, not a complete adversarial-defense system. TF-IDF retrieval and heuristic scoring demonstrate reproducible agent orchestration and evaluation, not production-grade semantic retrieval or a calibrated safety guarantee.

Future extensions can include Sentence Transformers/FAISS, local Ollama models, delegated identity, MLflow experiment tracking, broader adversarial suites, and domain-specific public datasets.

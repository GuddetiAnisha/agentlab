# AgentLab: Enterprise Multi-Agent AI Evaluation & Safety Platform

## Research question

How can collaborative AI agents be designed so that multi-step enterprise investigations remain evidence-grounded, permission-aware, auditable, and measurable?

## Independent changes from the job description

The Ericsson opportunity lists four separate research areas. This prototype does not reproduce a specific Ericsson thesis. Instead:

- it combines collaboration, security and evaluation into one experimental platform;
- it uses a generic enterprise incident domain instead of telecom production data;
- it uses local TF-IDF retrieval instead of requiring proprietary enterprise data;
- it uses deterministic Python agents so experiments are reproducible without paid APIs;
- it focuses entirely on software, APIs, UI, evaluation and security controls.

## Agents

- Planner Agent — decomposes a task.
- Retrieval Agent — retrieves evidence.
- Analyst Agent — creates an evidence-grounded assessment.
- Safety Agent — detects suspicious prompt patterns.
- Reviewer Agent — evaluates grounding, permission compliance and safety.

## Evaluation dimensions

- evidence grounding
- authorization compliance
- prompt-safety behavior
- latency
- trace length/tool efficiency
- reproducibility

## Technologies

Python, FastAPI, Streamlit, Scikit-learn, TF-IDF, SQLite, REST APIs, Pytest, Docker.

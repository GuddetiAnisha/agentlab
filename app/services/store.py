import sqlite3, json
from pathlib import Path

DB = Path(__file__).resolve().parents[2] / "agentlab.db"

def init_db():
    with sqlite3.connect(DB) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS runs(
            run_id TEXT PRIMARY KEY,
            query TEXT,
            role TEXT,
            answer TEXT,
            score REAL,
            trace TEXT
        )""")

def save_run(run_id, query, role, answer, score, trace):
    with sqlite3.connect(DB) as c:
        c.execute(
            "INSERT OR REPLACE INTO runs VALUES(?,?,?,?,?,?)",
            (run_id, query, role, answer, score, json.dumps(trace))
        )

def recent_runs(limit=20):
    with sqlite3.connect(DB) as c:
        rows = c.execute(
            "SELECT run_id,query,role,answer,score,trace FROM runs ORDER BY rowid DESC LIMIT ?",
            (limit,)
        ).fetchall()
    return [
        {"run_id":r[0],"query":r[1],"role":r[2],"answer":r[3],
         "score":r[4],"trace":json.loads(r[5])}
        for r in rows
    ]

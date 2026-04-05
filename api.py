"""
========================================================
🌐 FASTAPI BACKEND
========================================================

WHAT THIS FILE DOES:
--------------------
Exposes your AI system as an API.

WHY:
----
Allows:
✔ UI (Streamlit)
✔ Mobile apps
✔ External systems

to talk to your AI system.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

# Create API app
app = FastAPI()


class Query(BaseModel):
    """
    Request format for API
    """
    query: str


@app.get("/")
def home():
    """
    Health check endpoint
    """
    return {"message": "MCP AI Running 🚀"}


@app.post("/ask")
def ask(q: Query):
    """
    Main AI endpoint

    Example:
    --------
    POST /ask
    {
        "query": "Compare Dallas and Miami"
    }
    """

    return {"response": run_agent(q.query)}
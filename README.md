# 🌍 MCP + RAG + Agent AI System

## 🚀 Overview

This project demonstrates a modern AI system using:

- MCP (Model Context Protocol)
- RAG (Pinecone vector search)
- LangChain Agent
- FastAPI backend
- Streamlit UI

---

## 🧠 Architecture

User → Streamlit → FastAPI → Agent → MCP → Tools → Response

---

## ⚙️ Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn streamlit langchain langchain-openai openai pinecone python-dotenv requests


🔐 Environment
OPENAI_API_KEY=your_key
PINECONE_API_KEY=your_key

▶️ Run
uvicorn api:app --reload
streamlit run streamlit_app.py

🧠 Concepts
	•	MCP → tool abstraction layer
	•	RAG → knowledge retrieval
	•	Agent → decision making



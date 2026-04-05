"""
========================================================
🖥 STREAMLIT UI (FRONTEND FOR MCP AI SYSTEM)
========================================================

WHAT THIS FILE DOES:
--------------------
Provides a user interface for interacting with your AI system.

FLOW:
-----
User (UI)
   ↓
Streamlit → FastAPI → Agent → MCP → Tools → Response

FEATURES:
---------
✔ User enters query
✔ Sends request to FastAPI
✔ Displays AI response
✔ Shows loading state
"""

import streamlit as st
import requests


# ======================================================
# CONFIGURATION
# ======================================================

# Backend API URL (change if port changes)
API_URL = "http://127.0.0.1:8000"


# ======================================================
# UI SETUP
# ======================================================

# Page configuration
st.set_page_config(
    page_title="MCP AI City Analyzer",
    layout="centered"
)

# App title
st.title("🌍 MCP AI City Analyzer")

# Description
st.markdown("""
Ask questions about cities.

Examples:
- Compare Dallas weather and insights
- What is the weather in Miami?
- Tell me about Chicago cost of living
""")


# ======================================================
# INPUT SECTION
# ======================================================

# User input box
query = st.text_input("💬 Enter your question")


# ======================================================
# BUTTON ACTION
# ======================================================

if st.button("Ask"):

    # Validate input
    if not query:
        st.warning("⚠️ Please enter a question")
    else:

        # Show loading spinner while waiting
        with st.spinner("🤖 Thinking..."):

            try:
                # --------------------------------------------------
                # CALL FASTAPI BACKEND
                # --------------------------------------------------
                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "query": query,
                        "tools": []  # 👈 keep empty → agent decides tools
                    }
                )

                # Extract result
                result = response.json().get("response", "No response")

            except Exception as e:
                st.error(f"❌ Error connecting to API: {e}")
                result = None

        # --------------------------------------------------
        # DISPLAY RESPONSE
        # --------------------------------------------------
        if result:
            st.success("✅ Done")

            st.markdown("### 🤖 AI Response")
            st.write(result)


# ======================================================
# FOOTER (optional)
# ======================================================

st.markdown("---")
st.markdown("Built with MCP + FastAPI + Streamlit 🚀")
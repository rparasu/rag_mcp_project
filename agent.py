"""
========================================================
🤖 AGENT (MCP DISCOVERY + ORCHESTRATION)
========================================================

WHAT THIS FILE DOES:
--------------------
This is the "brain" of the system.

UPDATED FLOW (REAL MCP STYLE):
-----------------------------
1. Ask MCP → what tools are available
2. Decide which tools to use
3. Call MCP server
4. Combine results
5. Generate final response
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from mcp_server import call_tool, list_tools


# ======================================================
# LLM SETUP
# ======================================================
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def run_agent(query: str):
    """
    Main agent function using MCP discovery
    """

    print("\n===== AGENT START =====")
    print("User Query:", query)

    # ==================================================
    # STEP 1: DISCOVER TOOLS FROM MCP
    # ==================================================
    available_tools = list_tools()

    print("\n--- AVAILABLE TOOLS ---")
    print(available_tools)

    # ==================================================
    # STEP 2: DECIDE WHICH TOOLS TO USE
    # ==================================================
    decision_prompt = f"""
    You are an AI agent.

    Available tools:
    {available_tools}

    User query:
    {query}

    Decide which tools to use.

    Respond like:
    weather: yes/no
    rag: yes/no
    """

    decision = llm.invoke([HumanMessage(content=decision_prompt)])
    decision_text = decision.content.lower()

    use_weather = "weather: yes" in decision_text
    use_rag = "rag: yes" in decision_text

    print("\n--- DECISION ---")
    print("Raw Decision:", decision_text)
    print("Use Weather:", use_weather)
    print("Use RAG:", use_rag)

    # ==================================================
    # STEP 3: CALL TOOLS VIA MCP
    # ==================================================
    weather_data = ""
    rag_data = ""

    if use_weather:
        weather_data = call_tool("weather", query)

    if use_rag:
        rag_data = call_tool("rag", query)

    print("\n--- TOOL OUTPUTS ---")
    print("Weather Data:", weather_data)
    print("RAG Data:", rag_data)

    # ==================================================
    # STEP 4: FINAL RESPONSE
    # ==================================================
    final_prompt = f"""
    Answer the user query using this data:

    Query:
    {query}

    Weather Data:
    {weather_data}

    Knowledge Data:
    {rag_data}

    Provide a clear structured answer.
    """

    final = llm.invoke([HumanMessage(content=final_prompt)])

    print("\n--- FINAL RESPONSE ---")
    print(final.content)
    print("===== AGENT END =====\n")

    return final.content
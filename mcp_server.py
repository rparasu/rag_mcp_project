"""
========================================================
🔌 MCP SERVER (MODEL CONTEXT PROTOCOL - SIMPLIFIED)
========================================================

CORE IDEA:
----------
Agent SHOULD NOT call tools directly.

Instead:
--------
Agent → MCP Server → Tool

WHY THIS IS IMPORTANT:
---------------------
✔ Decouples agent from tools
✔ Easier to scale
✔ Central place to manage tools

THIS FILE IS:
-------------
A simple tool router (switchboard)
"""

from tools.weather_tool import get_weather
from tools.rag_tool import rag_search


# ======================================================
# TOOL REGISTRY
# ======================================================
# This dictionary maps:
# tool_name → function
#
# Think of this as:
# "Available tools in the system"
# ======================================================

TOOLS = {
    "weather": get_weather,
    "rag": rag_search,
}


def list_tools():
    """
    Returns available tool names.

    WHY:
    ----
    In real MCP:
    Agent can ask:
    "What tools do I have?"

    RETURNS:
    --------
    list
    """

    print("\n[MCP] Listing available tools...")
    tools = list(TOOLS.keys())
    print("[MCP] Tools:", tools)

    return tools


def call_tool(name: str, input_text: str):
    """
    Executes a tool dynamically.

    PARAMETERS:
    -----------
    name : str
        Tool name (e.g., 'weather')

    input_text : str
        Input passed to tool

    RETURNS:
    --------
    str
        Tool output

    EXAMPLE:
    --------
    call_tool("weather", "Dallas")
    """

    print(f"\n[MCP] Tool requested: {name}")
    print(f"[MCP] Input: {input_text}")

    # Check if tool exists
    if name not in TOOLS:
        print("[MCP] ❌ Tool not found")
        return f"❌ Tool '{name}' not found"

    # Call the tool dynamically
    result = TOOLS[name](input_text)

    print(f"[MCP] Output: {result}")

    return result
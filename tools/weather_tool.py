"""
========================================================
🌦 WEATHER TOOL (MCP TOOL)
========================================================

WHAT THIS FILE DOES:
--------------------
This file defines a simple "weather tool".

WHY IT EXISTS:
--------------
In MCP architecture, tools represent external capabilities.
Examples:
- Weather API
- Database query
- File system access

Right now:
----------
This is a MOCK (fake) implementation.

Later:
------
You can replace this with a real API call like:
- OpenWeather API
"""

def get_weather(city: str) -> str:
    """
    Simulates fetching weather data.

    PARAMETERS:
    -----------
    city : str
        Name of the city

    RETURNS:
    --------
    str
        Weather description

    NOTE:
    -----
    In real-world, you would:
    - Call external API
    - Parse JSON response
    """

    return f"{city}: 75°F, sunny"
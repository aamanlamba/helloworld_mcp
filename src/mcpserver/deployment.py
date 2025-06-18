from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool("weather")
def get_weather(location: str) -> str:
    """
    Get the weather for a given location.
    """
    # This is a placeholder implementation.
    # In a real application, you would fetch the weather data from an API.
    return f"The weather in {location} is sunny with a high of 25°C."


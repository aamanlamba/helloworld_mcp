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

if __name__ == "__main__":
    print("Weather service is running...")
    print("Use the 'weather' topic to get weather information.")
    print("Example: mcp_client.publish('weather', 'New York')")
    print("Press Ctrl+C to stop the service.")
    try:
        mcp.run()
    except KeyboardInterrupt:
        print("Stopping the weather service...")
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client as StdioClient
import asyncio
import traceback

server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"]
)

async def run():
    try:
        async with StdioClient(server_params) as (read,write):
            async with ClientSession(read, write) as session:
                print("Weather service client is running...")
                print("Use the 'weather' topic to get weather information.")
                print("Example: mcp_client.publish('weather', 'New York')")
                await session.initialize()
                tools = await session.list_tools()
                print("Available tools:", tools)
                print("Calling the 'weather' tool with 'Boston' as location...")
                try:
                    result = await session.call_tool("weather", arguments = {"location":"Boston"})
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error calling tool: {e}")
                    traceback.print_exc()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
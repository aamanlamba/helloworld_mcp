from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client as StdioClient
import asyncio
import traceback

server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
)

async def run():
    try:
        async with StdioClient(server_params) as (read,write):
            async with ClientSession(read, write) as session:
                print("Airbnb service client is running...")
                print("Use the 'airbnb' topic to get Airbnb information.")
                print("Example: mcp_client.publish('airbnb', 'New York')")
                await session.initialize()
                tools = await session.list_tools()
                print("Available tools:", tools)
                print("Calling the 'weather' tool with 'Boston' as location...")
                try:
                    result = await session.call_tool("airbnb_search", arguments = {"location":"New York", "checkin":"2025-10-01", "checkout":"2025-10-05", "guests":2})
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error calling tool: {e}")
                    traceback.print_exc()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
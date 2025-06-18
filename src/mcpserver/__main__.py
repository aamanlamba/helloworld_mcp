from mcpserver.deployment import mcp
def main():
    mcp.run()
    
if __name__ == "__main__":
    main()
# This is the main entry point for the MCP server.
# It initializes the server and starts it.
# The server can be stopped gracefully with a keyboard interrupt (Ctrl+C).
# The server is designed to run the weather service, which provides weather information for a given location.
# The server uses the FastMCP framework to handle tool calls and manage the MCP session.
# The server can be extended to include more tools and functionalities as needed.
# The server is intended to be run in a terminal or command line environment.
# The server can be used in conjunction with a client that publishes messages to the 'weather' topic.
# The server is designed to be lightweight and easy to deploy.
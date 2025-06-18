# Test MCP Server

Test MCP Server Package

## Tools ##
weather (location) - returns a dummy weather for the location

To install the 'weather' tool, add the following to your MCP Client Config 

``` json
    "weather": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/aamanlamba/helloworld_mcp.git",
        "mcp-server"
      ]
    }
```
MCP_JSON = """
{
  "mcpServers": {
    "notes": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/evilynn/llm-notes"]
    }
  }
}
"""

transport = "stdio"
who_starts_it = "lmstudio"
if_command_not_found = "b"

# MCP Example 

**Create environment**
```Bash
uv init mcp-server-demo

cd mcp-server-demo

uv add "mcp[cli]"

uv run mcp
```

**Usage**: _mcp [OPTIONS] COMMAND [ARGS]_

### MCP development tools

- Options

--help

**Commands**

_**version**_   > Show the MCP version

_**dev**_   > Run a MCP server with the MCP Inspector

_**run**_   > Run a MCP Server

_**install**_   > Install a MCP server in the Claude desktop app

**Example** _(open **MCP** dev **Inspector**)_:
```Bash
uv run mcp dev <MYPYTHONFILE>

# Example output:
Starting MCP inspector...
⚙️ Proxy server listening on port <PORT>
🔍 MCP Inspector is up and running at http://127.0.0.1:<PORT> 🚀

```
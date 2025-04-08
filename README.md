# MCP Example 

uv init mcp-server-demo
cd mcp-server-demo

```Bash
uv add "mcp[cli]"
```

```bash
uv run mcp
```

**Usage**: _cp [OPTIONS] COMMAND [ARGS]_

 MCP development tools

### Options

--help

### **Commands**

_**version**_   > Show the MCP version
_**dev**_   > Run a MCP server with the MCP Inspector
_**run**_   > Run a MCP Server
_**install**_   > Install a MCP server in the Claude desktop app

**Example** _(open MCP dev window/browser)_:
```Bash
uv run mcp dev <MYPYTHONFILE>
```
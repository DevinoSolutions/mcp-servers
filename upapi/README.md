# upAPI MCP server

Call a catalog of ready-to-use APIs through one upAPI account and key, without signing up for each upstream service.

![upAPI](assets/logo.png)

- Endpoint: `https://app.upapi.io/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://upapi.io
- Docs: https://upapi.io/docs/mcp

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the upAPI sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `upapi` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=upapi&config=eyJ1cmwiOiJodHRwczovL2FwcC51cGFwaS5pby9hcGkvbWNwIn0%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "upapi": {
      "url": "https://app.upapi.io/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the upAPI MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/upapi" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "upapi": {
      "type": "streamableHttp",
      "url": "https://app.upapi.io/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=upapi&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.upapi.io%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "upapi": {
      "type": "http",
      "url": "https://app.upapi.io/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http upapi https://app.upapi.io/api/mcp`

**Claude and ChatGPT:** upAPI is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.upapi.io/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the upAPI operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Links

- Privacy: https://upapi.io/privacy
- Terms: https://upapi.io/terms
- Support: https://app.upapi.io/support

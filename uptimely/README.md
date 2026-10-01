# Uptimely MCP server

Manage uptime monitors, incidents and status pages, and read check results, in Uptimely.

![Uptimely](assets/logo.png)

- Endpoint: `https://app.getuptimely.com/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://getuptimely.com
- Docs: https://getuptimely.com/integrations

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the Uptimely sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `uptimely` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=uptimely&config=eyJ1cmwiOiJodHRwczovL2FwcC5nZXR1cHRpbWVseS5jb20vYXBpL21jcCJ9), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "uptimely": {
      "url": "https://app.getuptimely.com/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the Uptimely MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/uptimely" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "uptimely": {
      "type": "streamableHttp",
      "url": "https://app.getuptimely.com/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=uptimely&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.getuptimely.com%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "uptimely": {
      "type": "http",
      "url": "https://app.getuptimely.com/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http uptimely https://app.getuptimely.com/api/mcp`

**Claude and ChatGPT:** add `https://app.getuptimely.com/api/mcp` as a custom connector (remote MCP server, OAuth sign-in).

**Any other MCP client:** Streamable HTTP endpoint `https://app.getuptimely.com/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the Uptimely operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `adding-uptime-monitors`
- `checking-uptime-status`
- `responding-to-incidents`
- `writing-postmortems`

## Links

- Privacy policy: https://getuptimely.com/privacy
- Terms: https://getuptimely.com/terms
- Support: https://app.getuptimely.com/support or [hello@getuptimely.com](mailto:hello@getuptimely.com)

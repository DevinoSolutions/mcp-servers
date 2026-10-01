# GetItDone MCP server

Create, update and track tasks and projects across your GetItDone team workspaces.

![GetItDone](assets/logo.png)

- Endpoint: `https://app.nowgetitdone.com/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://nowgetitdone.com
- Docs: https://nowgetitdone.com/docs/connecting-ai-assistants

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the GetItDone sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `getitdone` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=getitdone&config=eyJ1cmwiOiJodHRwczovL2FwcC5ub3dnZXRpdGRvbmUuY29tL2FwaS9tY3AifQ%3D%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "getitdone": {
      "url": "https://app.nowgetitdone.com/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the GetItDone MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/getitdone" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "getitdone": {
      "type": "streamableHttp",
      "url": "https://app.nowgetitdone.com/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=getitdone&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.nowgetitdone.com%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "getitdone": {
      "type": "http",
      "url": "https://app.nowgetitdone.com/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http getitdone https://app.nowgetitdone.com/api/mcp`

**Claude and ChatGPT:** GetItDone is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.nowgetitdone.com/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the GetItDone operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `capturing-tasks`
- `investigating-tasks`
- `reviewing-workload`
- `searching-getitdone-api-docs`

## Links

- Privacy policy: https://nowgetitdone.com/privacy
- Terms: https://nowgetitdone.com/terms
- Support: https://app.nowgetitdone.com/support

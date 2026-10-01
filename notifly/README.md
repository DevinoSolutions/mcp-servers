# Notifly MCP server

Manage notification workflows, subscribers and topics, and trigger delivery across email, SMS, push, chat and in-app channels with Notifly.

![Notifly](assets/logo.png)

- Endpoint: `https://api.notifly.io/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://notifly.io
- Docs: https://notifly.io/developers

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the Notifly sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `notifly` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=notifly&config=eyJ1cmwiOiJodHRwczovL2FwaS5ub3RpZmx5LmlvL21jcCJ9), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "notifly": {
      "url": "https://api.notifly.io/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the Notifly MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/notifly" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "notifly": {
      "type": "streamableHttp",
      "url": "https://api.notifly.io/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=notifly&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapi.notifly.io%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "notifly": {
      "type": "http",
      "url": "https://api.notifly.io/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http notifly https://api.notifly.io/mcp`

**Claude and ChatGPT:** add `https://api.notifly.io/mcp` as a custom connector (remote MCP server, OAuth sign-in).

**Any other MCP client:** Streamable HTTP endpoint `https://api.notifly.io/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the Notifly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `checking-notification-delivery`
- `reviewing-notification-workflows`
- `sending-notifications`

## Links

- Privacy policy: https://notifly.io/privacy
- Terms: https://notifly.io/terms
- Support: https://app.notifly.io/support or [support@notifly.io](mailto:support@notifly.io)

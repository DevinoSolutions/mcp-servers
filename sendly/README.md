# Sendly MCP server

Send transactional email, run campaigns, and manage contacts, lists and segments in Sendly.

![Sendly](assets/logo.png)

- Endpoint: `https://app.sendly.now/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://sendly.now
- Docs: https://docs.sendly.now/guides/mcp

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the Sendly sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `sendly` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=sendly&config=eyJ1cmwiOiJodHRwczovL2FwcC5zZW5kbHkubm93L2FwaS9tY3AifQ%3D%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "sendly": {
      "url": "https://app.sendly.now/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the Sendly MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/sendly" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "sendly": {
      "type": "streamableHttp",
      "url": "https://app.sendly.now/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=sendly&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.sendly.now%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "sendly": {
      "type": "http",
      "url": "https://app.sendly.now/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http sendly https://app.sendly.now/api/mcp`

**Claude and ChatGPT:** Sendly is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.sendly.now/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the Sendly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `building-onboarding-workflows`
- `checking-email-deliverability`
- `reviewing-email-performance`
- `sending-email-campaigns`

## Links

- Privacy policy: https://sendly.now/privacy
- Terms: https://sendly.now/terms
- Support: [support@sendly.now](mailto:support@sendly.now)

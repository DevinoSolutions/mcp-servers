# Postify MCP server

Draft, schedule and publish social media posts to your connected channels, and read post analytics, from your Postify calendar.

![Postify](assets/logo.png)

- Endpoint: `https://app.usepostify.com/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://usepostify.com
- Docs: https://usepostify.com/developers

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the Postify sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `postify` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=postify&config=eyJ1cmwiOiJodHRwczovL2FwcC51c2Vwb3N0aWZ5LmNvbS9hcGkvbWNwIn0%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "postify": {
      "url": "https://app.usepostify.com/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the Postify MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/postify" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "postify": {
      "type": "streamableHttp",
      "url": "https://app.usepostify.com/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=postify&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.usepostify.com%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "postify": {
      "type": "http",
      "url": "https://app.usepostify.com/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http postify https://app.usepostify.com/api/mcp`

**Claude and ChatGPT:** Postify is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.usepostify.com/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the Postify operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `drafting-social-posts`
- `managing-content-calendar`
- `reviewing-social-performance`

## Links

- Privacy: https://usepostify.com/privacy
- Terms: https://usepostify.com/terms
- Support: https://app.usepostify.com/support

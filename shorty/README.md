# Shorty MCP server

Summarize and transcribe videos, audio files, documents and web pages with Shorty.

![Shorty](assets/logo.png)

- Endpoint: `https://aishorty.com/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://aishorty.com
- Docs: https://aishorty.com/docs/connecting-ai-assistants

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the Shorty sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `shorty` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=shorty&config=eyJ1cmwiOiJodHRwczovL2Fpc2hvcnR5LmNvbS9hcGkvbWNwIn0%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "shorty": {
      "url": "https://aishorty.com/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the Shorty MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/shorty" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "shorty": {
      "type": "streamableHttp",
      "url": "https://aishorty.com/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=shorty&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Faishorty.com%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "shorty": {
      "type": "http",
      "url": "https://aishorty.com/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http shorty https://aishorty.com/api/mcp`

**Claude and ChatGPT:** Shorty is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://aishorty.com/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the Shorty operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `researching-summary-library`
- `summarizing-sources`
- `transcribing-media`

## Links

- Privacy: https://aishorty.com/privacy
- Terms: https://aishorty.com/terms
- Support: https://aishorty.com/support

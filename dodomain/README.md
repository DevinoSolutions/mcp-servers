# doDomain MCP server

Connect customers' custom domains to your product: guided DNS setup, verification and certificates, managed from doDomain.

![doDomain](assets/logo.png)

- Endpoint: `https://app.dodomain.io/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://dodomain.io
- Docs: https://dodomain.io/docs/connecting-ai-assistants

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the doDomain sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `dodomain` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=dodomain&config=eyJ1cmwiOiJodHRwczovL2FwcC5kb2RvbWFpbi5pby9hcGkvbWNwIn0%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "dodomain": {
      "url": "https://app.dodomain.io/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the doDomain MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/dodomain" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "dodomain": {
      "type": "streamableHttp",
      "url": "https://app.dodomain.io/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=dodomain&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.dodomain.io%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "dodomain": {
      "type": "http",
      "url": "https://app.dodomain.io/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http dodomain https://app.dodomain.io/api/mcp`

**Claude and ChatGPT:** doDomain is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.dodomain.io/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the doDomain operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `checking-domain-connections`
- `connecting-customer-domains`
- `preflighting-domains`

## Links

- Privacy: https://dodomain.io/privacy
- Terms: https://dodomain.io/terms
- Support: https://app.dodomain.io/support

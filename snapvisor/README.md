# SnapVisor MCP server

Review visual regression builds, approve or reject screenshot changes, and manage SnapVisor projects.

![SnapVisor](assets/logo.png)

- Endpoint: `https://mcp.snapvisor.io/` (Streamable HTTP, OAuth 2.1)
- Product: https://snapvisor.io
- Docs: https://snapvisor.io/docs

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the SnapVisor sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `snapvisor` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=snapvisor&config=eyJ1cmwiOiJodHRwczovL21jcC5zbmFwdmlzb3IuaW8vIn0%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "snapvisor": {
      "url": "https://mcp.snapvisor.io/"
    }
  }
}
```

**Cline:** ask Cline to "install the SnapVisor MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/snapvisor" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "snapvisor": {
      "type": "streamableHttp",
      "url": "https://mcp.snapvisor.io/",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=snapvisor&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.snapvisor.io%2F%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "snapvisor": {
      "type": "http",
      "url": "https://mcp.snapvisor.io/"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http snapvisor https://mcp.snapvisor.io/`

**Claude and ChatGPT:** SnapVisor is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://mcp.snapvisor.io/`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the SnapVisor operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `discussing-builds`
- `handling-flaky-changes`
- `reporting-snapvisor-usage`
- `reviewing-visual-builds`

## Links

- Privacy policy: https://snapvisor.io/privacy
- Terms: https://snapvisor.io/terms
- Support: https://snapvisor.io/support or [support@snapvisor.io](mailto:support@snapvisor.io)

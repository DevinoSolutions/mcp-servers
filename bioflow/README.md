# BioFlow MCP server

Edit and publish your link-in-bio page, its links and blocks, and read page analytics and signups from BioFlow.

![BioFlow](assets/logo.png)

- Endpoint: `https://app.getbioflow.com/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://getbioflow.com
- Docs: https://getbioflow.com/mcp

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the BioFlow sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `bioflow` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=bioflow&config=eyJ1cmwiOiJodHRwczovL2FwcC5nZXRiaW9mbG93LmNvbS9hcGkvbWNwIn0%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "bioflow": {
      "url": "https://app.getbioflow.com/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the BioFlow MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/bioflow" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "bioflow": {
      "type": "streamableHttp",
      "url": "https://app.getbioflow.com/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=bioflow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.getbioflow.com%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "bioflow": {
      "type": "http",
      "url": "https://app.getbioflow.com/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http bioflow https://app.getbioflow.com/api/mcp`

**Claude and ChatGPT:** BioFlow is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.getbioflow.com/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the BioFlow operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `analyzing-page-performance`
- `editing-page-drafts`
- `publishing-pages`

## Links

- Privacy: https://app.getbioflow.com/privacy
- Terms: https://app.getbioflow.com/terms
- Support: https://app.getbioflow.com/support

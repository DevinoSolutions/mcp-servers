# SuperBooks MCP server

Work with your SuperBooks books: transactions and categories, invoices, customers, receipts, time tracking and financial reports.

![SuperBooks](assets/logo.png)

- Endpoint: `https://app.superbooks.io/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://superbooks.io
- Docs: https://docs.superbooks.io/mcp

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the SuperBooks sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `superbooks` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=superbooks&config=eyJ1cmwiOiJodHRwczovL2FwcC5zdXBlcmJvb2tzLmlvL21jcCJ9), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "superbooks": {
      "url": "https://app.superbooks.io/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the SuperBooks MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/superbooks" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "superbooks": {
      "type": "streamableHttp",
      "url": "https://app.superbooks.io/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=superbooks&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.superbooks.io%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "superbooks": {
      "type": "http",
      "url": "https://app.superbooks.io/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http superbooks https://app.superbooks.io/mcp`

**Claude and ChatGPT:** SuperBooks is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.superbooks.io/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the SuperBooks operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `chasing-unpaid-invoices`
- `cleaning-up-bookkeeping`
- `drafting-invoices`
- `reading-financial-reports`

## Links

- Privacy policy: https://superbooks.io/privacy/
- Terms: https://superbooks.io/terms/
- Support: [support@superbooks.io](mailto:support@superbooks.io)

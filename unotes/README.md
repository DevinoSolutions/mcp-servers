# uNotes MCP server

Search a library of university course materials (past exams, assignments, lab reports, lecture notes) and your uNotes flashcards and quizzes.

![uNotes](assets/logo.png)

- Endpoint: `https://unotes.net/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://unotes.net
- Docs: https://unotes.net/docs

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the uNotes sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `unotes` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=unotes&config=eyJ1cmwiOiJodHRwczovL3Vub3Rlcy5uZXQvYXBpL21jcCJ9), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "unotes": {
      "url": "https://unotes.net/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the uNotes MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/unotes" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "unotes": {
      "type": "streamableHttp",
      "url": "https://unotes.net/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=unotes&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Funotes.net%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "unotes": {
      "type": "http",
      "url": "https://unotes.net/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http unotes https://unotes.net/api/mcp`

**Claude and ChatGPT:** uNotes is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://unotes.net/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the uNotes operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `building-study-guides`
- `planning-revision`
- `researching-course-material`

## Links

- Privacy: https://unotes.net/privacy
- Terms: https://unotes.net/terms
- Support: https://unotes.net/support

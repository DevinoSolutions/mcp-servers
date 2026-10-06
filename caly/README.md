# Caly MCP server

Find open meeting times, book, reschedule and cancel meetings, and read your event types, bookings and schedules in Caly.

![Caly](assets/logo.png)

- Endpoint: `https://mcp.trycaly.com/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://trycaly.com
- Docs: https://trycaly.com/docs/

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the Caly sign-in and consent screen, where you approve what the assistant may do. A Caly API key sent as `Authorization: Bearer <key>` also works (Settings → Developer → API keys).

**Cursor:** [add the server in one click](https://cursor.com/install-mcp?name=caly&config=eyJ1cmwiOiJodHRwczovL21jcC50cnljYWx5LmNvbS9tY3AifQ%3D%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "caly": {
      "url": "https://mcp.trycaly.com/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the Caly MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/caly" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "caly": {
      "type": "streamableHttp",
      "url": "https://mcp.trycaly.com/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=caly&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.trycaly.com%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "caly": {
      "type": "http",
      "url": "https://mcp.trycaly.com/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http caly https://mcp.trycaly.com/mcp`

**Claude and ChatGPT:** add `https://mcp.trycaly.com/mcp` as a custom connector (remote MCP server, OAuth sign-in).

**Any other MCP client:** Streamable HTTP endpoint `https://mcp.trycaly.com/mcp`. It is also published in the official MCP Registry as `com.trycaly/caly`.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the Caly operations (who am I, event types, available slots, bookings, schedules, and creating, rescheduling or cancelling a booking), then runs them inside `execute_typescript` as `external_<name>` functions. Cancelling a booking takes two calls: the first returns a confirmation token, and the booking is only cancelled when the call is repeated with it.

## Skills (Cursor plugin)

- `finding-meeting-times`
- `booking-meetings`
- `managing-bookings`

## Links

- Privacy policy: https://trycaly.com/privacy
- Terms: https://trycaly.com/terms
- Support: [hello@devino.ca](mailto:hello@devino.ca)

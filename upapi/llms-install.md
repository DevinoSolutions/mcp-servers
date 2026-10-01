# Installing the upAPI MCP server

upAPI runs as a hosted remote MCP server. Do not clone, build or run anything locally.

1. Add this entry to the MCP settings file (in Cline: `cline_mcp_settings.json`). Keep `"type": "streamableHttp"` exactly as written; other spellings fall back to SSE and fail with HTTP 405.

```json
{
  "mcpServers": {
    "upapi": {
      "type": "streamableHttp",
      "url": "https://app.upapi.io/api/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

2. No API key or environment variable is needed. The server uses OAuth 2.1. When the server shows as needing authentication, click **Authenticate**; a browser window opens on the upAPI sign-in and consent screen. The user signs in (or creates a free account at https://upapi.io) and approves the scopes.

3. Check the connection by listing tools. The server exposes `search_tools` and `execute_typescript`. Call `search_tools` with no arguments to see which upAPI operations this sign-in can reach, then call them from `execute_typescript` as `external_<name>` functions, for example `return await external_<name>({})`.

If the tools do not appear, remove and re-add the server, then authenticate again. Docs: https://upapi.io/docs/mcp. Support: https://app.upapi.io/support.

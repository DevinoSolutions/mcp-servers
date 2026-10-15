# Installing the UpRank MCP server

UpRank runs as a hosted remote MCP server. Do not clone, build or run anything locally.

1. Add this entry to the MCP settings file (in Cline: `cline_mcp_settings.json`). Keep `"type": "streamableHttp"` exactly as written; other spellings fall back to SSE and fail with HTTP 405.

```json
{
  "mcpServers": {
    "uprank": {
      "type": "streamableHttp",
      "url": "https://uprank.devino.ca/api/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

2. No API key or environment variable is needed. The server uses OAuth 2.1 with PKCE and dynamic client registration (metadata at https://uprank.devino.ca/.well-known/oauth-authorization-server). When the server shows as needing authentication, click **Authenticate**; a browser window opens on the UpRank sign-in and consent screen. The user signs in and approves the scopes. Only a workspace owner can approve the consent screen. Bearer tokens issued in the app on https://uprank.devino.ca/mcp also work.

3. Check the connection by listing tools. The server defines 17 tools (an OAuth connection sees 16: live publishing, `publication_publish`, needs an API key with the `publication:live` scope), for example `brand_get`, `topic_research`, `pipeline_run`, `pipeline_status`, `article_get` and `article_score`. Long-running tools return a `workflowRunId`; poll `pipeline_status` with it.

`publication_create_draft` only records a draft publication in UpRank; it does not push to a CMS. `publication_publish` needs the `publication:live` scope, which OAuth sign-ins never carry; it is listed only for an API key that holds that scope.

If the tools do not appear, remove and re-add the server, then authenticate again. Docs: https://uprank.devino.ca/agent-setup. Support: support@devino.ca.

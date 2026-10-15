# UpRank MCP server

Research, draft, score and prepare evidence-backed articles for your company site in UpRank, with every claim traced to a source and hard quality gates before anything is published.

![UpRank](assets/logo.png)

- Endpoint: `https://uprank.devino.ca/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://uprank.devino.ca
- Docs: https://uprank.devino.ca/agent-setup

UpRank is an editorial control room for evidence-backed content. It researches, drafts, scores and prepares articles for a company's own site, every claim is traced to a source gathered before drafting, and nothing is published until it clears hard quality gates (11 scored dimensions, 13 hard gates). Publications are prepared for Strapi as drafts.

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration; metadata at https://uprank.devino.ca/.well-known/oauth-authorization-server): the first time your client calls it, a browser window opens on the UpRank sign-in and consent screen, where you choose what the assistant may do. Only a workspace owner can approve the consent. Bearer tokens issued in the app on https://uprank.devino.ca/mcp also work.

**Cursor:** install the `uprank` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=uprank&config=eyJ1cmwiOiJodHRwczovL3VwcmFuay5kZXZpbm8uY2EvYXBpL21jcCJ9), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "uprank": {
      "url": "https://uprank.devino.ca/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the UpRank MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/uprank" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "uprank": {
      "type": "streamableHttp",
      "url": "https://uprank.devino.ca/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=uprank&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fuprank.devino.ca%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "uprank": {
      "type": "http",
      "url": "https://uprank.devino.ca/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http uprank https://uprank.devino.ca/api/mcp`

**Claude and ChatGPT:** add `https://uprank.devino.ca/api/mcp` as a custom connector (remote MCP server, OAuth sign-in).

**Any other MCP client:** Streamable HTTP endpoint `https://uprank.devino.ca/api/mcp`.

## Tools

The server defines 17 tools (an OAuth connection sees 16: live publishing, `publication_publish`, needs an API key with the `publication:live` scope): `pipeline_run`, `pipeline_status`, `brand_ingest`, `brand_get`, `topic_research`, `brief_generate`, `article_generate`, `article_score`, `article_revise`, `links_suggest`, `media_select`, `publication_create_draft`, `publication_publish`, `publication_status`, `refresh_list`, `article_get` and `article_list`.

- Read-only: `pipeline_status`, `brand_get`, `publication_status`, `refresh_list`, `article_get`, `article_list`.
- Long-running tools return a `workflowRunId`; poll `pipeline_status` with it.
- `publication_create_draft` creates a DRAFT publication record in UpRank. It does not push to the CMS.
- `publication_publish` records a live publication request and needs the `publication:live` scope. OAuth sign-ins never carry that scope, so it is listed only for an API key that holds it.

## Skills (Cursor plugin)

- `drafting-evidence-backed-articles`
- `reviewing-article-quality`

## Links

- Privacy policy: https://uprank.devino.ca/privacy
- Support: support@devino.ca
- llms.txt: https://uprank.devino.ca/llms.txt

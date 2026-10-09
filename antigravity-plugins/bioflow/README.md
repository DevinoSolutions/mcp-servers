# BioFlow for Antigravity

Edit and publish your BioFlow link-in-bio page: add, reorder or remove links and blocks, go live on a schedule, and read page views, clicks and signups.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted BioFlow MCP server at `https://app.getbioflow.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the BioFlow sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://getbioflow.com.

Skills included: `analyzing-page-performance`, `editing-page-drafts`, `publishing-pages`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install bioflow@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/bioflow
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/bioflow`. In the Antigravity IDE, copy this folder into `.agents/plugins/bioflow` (workspace) or `~/.gemini/config/plugins/bioflow` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the BioFlow operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

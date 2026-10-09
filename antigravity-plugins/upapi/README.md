# upAPI for Antigravity

Call a catalog of ready-to-use APIs such as web search, Wikipedia, GitHub and more through one upAPI account and key, with no signup at each upstream service.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted upAPI MCP server at `https://app.upapi.io/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the upAPI sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://upapi.io.

This plugin ships the MCP server only; the server's own tool descriptions guide the agent.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install upapi@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/upapi
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/upapi`. In the Antigravity IDE, copy this folder into `.agents/plugins/upapi` (workspace) or `~/.gemini/config/plugins/upapi` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the upAPI operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

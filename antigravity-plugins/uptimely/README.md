# Uptimely for Antigravity

Manage uptime monitors, incidents and status pages in Uptimely: check what is down, add monitors, run incident response step by step and draft postmortems.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted Uptimely MCP server at `https://app.getuptimely.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the Uptimely sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://getuptimely.com.

Skills included: `adding-uptime-monitors`, `checking-uptime-status`, `responding-to-incidents`, `writing-postmortems`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install uptimely@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/uptimely
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/uptimely`. In the Antigravity IDE, copy this folder into `.agents/plugins/uptimely` (workspace) or `~/.gemini/config/plugins/uptimely` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Uptimely operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

# GetItDone for Antigravity

Create, update and track tasks and projects in your GetItDone team workspaces: capture to-dos from notes, review your workload and dig into any task.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted GetItDone MCP server at `https://app.nowgetitdone.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the GetItDone sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://nowgetitdone.com.

Skills included: `capturing-tasks`, `investigating-tasks`, `reviewing-workload`, `searching-getitdone-api-docs`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install getitdone@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/getitdone
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/getitdone`. In the Antigravity IDE, copy this folder into `.agents/plugins/getitdone` (workspace) or `~/.gemini/config/plugins/getitdone` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the GetItDone operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

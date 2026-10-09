# Caly for Antigravity

Find open meeting times, book, reschedule and cancel meetings, and read your event types, bookings and working-hours schedules in Caly, from the agent.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted Caly MCP server at `https://mcp.trycaly.com/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the Caly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://trycaly.com.

Skills included: `booking-meetings`, `finding-meeting-times`, `managing-bookings`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install caly@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/caly
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/caly`. In the Antigravity IDE, copy this folder into `.agents/plugins/caly` (workspace) or `~/.gemini/config/plugins/caly` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Caly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

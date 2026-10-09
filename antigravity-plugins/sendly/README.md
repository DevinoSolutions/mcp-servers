# Sendly for Antigravity

Send transactional email, draft and run campaigns, build onboarding workflows, manage contacts and segments, and fix deliverability with Sendly.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted Sendly MCP server at `https://app.sendly.now/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the Sendly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://sendly.now.

Skills included: `building-onboarding-workflows`, `checking-email-deliverability`, `reviewing-email-performance`, `sending-email-campaigns`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install sendly@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/sendly
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/sendly`. In the Antigravity IDE, copy this folder into `.agents/plugins/sendly` (workspace) or `~/.gemini/config/plugins/sendly` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Sendly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

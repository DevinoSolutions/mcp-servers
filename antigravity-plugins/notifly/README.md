# Notifly for Antigravity

Manage Notifly notification workflows, subscribers and topics, trigger delivery across email, SMS, push, chat and in-app, and check whether a message landed.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted Notifly MCP server at `https://api.notifly.io/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the Notifly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://notifly.io.

Skills included: `checking-notification-delivery`, `reviewing-notification-workflows`, `sending-notifications`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install notifly@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/notifly
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/notifly`. In the Antigravity IDE, copy this folder into `.agents/plugins/notifly` (workspace) or `~/.gemini/config/plugins/notifly` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Notifly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

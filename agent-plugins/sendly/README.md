# Sendly power

Send transactional email, run campaigns, and manage contacts, lists and segments in Sendly.

This power connects Kiro to the hosted Sendly MCP server at `https://app.sendly.now/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the Sendly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://sendly.now.

Skills included: `building-onboarding-workflows`, `checking-email-deliverability`, `reviewing-email-performance`, `sending-email-campaigns`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/sendly`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Sendly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://sendly.now/privacy
- Terms: https://sendly.now/terms
- Support: [support@sendly.now](mailto:support@sendly.now)
- Docs: https://docs.sendly.now/guides/mcp

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

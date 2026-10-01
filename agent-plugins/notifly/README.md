# Notifly power

Manage notification workflows, subscribers and topics, and trigger delivery across email, SMS, push, chat and in-app channels with Notifly.

This power connects Kiro to the hosted Notifly MCP server at `https://api.notifly.io/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the Notifly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://notifly.io.

Skills included: `checking-notification-delivery`, `reviewing-notification-workflows`, `sending-notifications`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/notifly`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Notifly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://notifly.io/privacy
- Terms: https://notifly.io/terms
- Support: https://app.notifly.io/support or [support@notifly.io](mailto:support@notifly.io)
- Docs: https://notifly.io/developers

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

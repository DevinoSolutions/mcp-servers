# Notifly plugin for GitHub Copilot CLI

Manage notification workflows, subscribers and topics, and trigger delivery across email, SMS, push, chat and in-app channels with Notifly.

The plugin adds the hosted Notifly MCP server (`https://api.notifly.io/mcp`, Streamable HTTP) to Copilot CLI, plus 3 skills for common tasks. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- A Notifly account (https://notifly.io). Notifly is a hosted service run by Devino Solutions, which also maintains this plugin. What the server lets the agent do depends on your Notifly plan and on the scopes you approve.

## Setup

1. Install the plugin from the Awesome Copilot marketplace, which ships with Copilot CLI:

   ```shell
   copilot plugin install notifly@awesome-copilot
   ```

   Or straight from this repository: `copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/notifly`.

2. Start Copilot CLI and ask for something that uses Notifly. The first call opens a browser window on the Notifly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth notifly`.
3. Run `/mcp show notifly` to check the connection and see its tools.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Notifly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills

- `sending-notifications`: Sends a Notifly workflow to a subscriber or topic through the two-step confirmation contract and verifies it in the activity feed.
- `checking-notification-delivery`: Finds out whether and how a Notifly notification reached a subscriber across email, SMS, push, chat, and in-app channels, from the activity feed.
- `reviewing-notification-workflows`: Reviews a Notifly environment's notification setup: workflows with their steps and channels, topics, and recent delivery activity.

## Limitations

- It needs network access to api.notifly.io and a signed-in Notifly account. There is no offline or self-hosted mode.
- The agent can only use the operations whose scopes you approved. To change them, revoke the connection in Notifly and run `/mcp auth notifly` to sign in again.
- Calls act on your real Notifly data. The included skills ask before any step that sends, publishes or changes something; other prompts should do the same.

## Links

- Docs: https://notifly.io/developers
- Privacy policy: https://notifly.io/privacy
- Terms: https://notifly.io/terms
- Support: https://app.notifly.io/support or [support@notifly.io](mailto:support@notifly.io)

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

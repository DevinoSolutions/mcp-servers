# Sendly plugin for GitHub Copilot CLI

Send transactional email, run campaigns, and manage contacts, lists and segments in Sendly.

The plugin adds the hosted Sendly MCP server (`https://app.sendly.now/api/mcp`, Streamable HTTP) to Copilot CLI, plus 2 skills for common tasks. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- A Sendly account (https://sendly.now). Sendly is a hosted service run by Devino Solutions, which also maintains this plugin. What the server lets the agent do depends on your Sendly plan and on the scopes you approve.

## Setup

1. Install the plugin from the Awesome Copilot marketplace, which ships with Copilot CLI:

   ```shell
   copilot plugin install sendly@awesome-copilot
   ```

   Or straight from this repository: `copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/sendly`.

2. Start Copilot CLI and ask for something that uses Sendly. The first call opens a browser window on the Sendly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth sendly`.
3. Run `/mcp show sendly` to check the connection and see its tools.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Sendly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills

- `checking-email-deliverability`: Diagnoses why Sendly mail is not landing and fixes the sending setup: domain health, DKIM, SPF, and DMARC records, sending-domain verification, suppressions, and address validation or list cleaning.
- `building-onboarding-workflows`: Builds, reviews, and troubleshoots Sendly workflow automations such as welcome, drip, and onboarding email series; new workflows are created disabled.

## Limitations

- It needs network access to app.sendly.now and a signed-in Sendly account. There is no offline or self-hosted mode.
- The agent can only use the operations whose scopes you approved. To change them, revoke the connection in Sendly and run `/mcp auth sendly` to sign in again.
- Calls act on your real Sendly data. The included skills ask before any step that sends, publishes or changes something; other prompts should do the same.

## Links

- Docs: https://docs.sendly.now/guides/mcp
- Privacy policy: https://sendly.now/privacy
- Terms: https://sendly.now/terms
- Support: [support@sendly.now](mailto:support@sendly.now)

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

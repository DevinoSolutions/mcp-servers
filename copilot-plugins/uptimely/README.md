# Uptimely plugin for GitHub Copilot CLI

Manage uptime monitors, incidents and status pages, and read check results, in Uptimely.

The plugin adds the hosted Uptimely MCP server (`https://app.getuptimely.com/api/mcp`, Streamable HTTP) to Copilot CLI, plus 3 skills for common tasks. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- An Uptimely account (https://getuptimely.com). Uptimely is a hosted service run by Devino Solutions, which also maintains this plugin. What the server lets the agent do depends on your Uptimely plan and on the scopes you approve.

## Setup

1. Install the plugin from the Awesome Copilot marketplace, which ships with Copilot CLI:

   ```shell
   copilot plugin install uptimely@awesome-copilot
   ```

   Or straight from this repository: `copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/uptimely`.

2. Start Copilot CLI and ask for something that uses Uptimely. The first call opens a browser window on the Uptimely sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth uptimely`.
3. Run `/mcp show uptimely` to check the connection and see its tools.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Uptimely operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills

- `checking-uptime-status`: Reports the current health and recent history of an Uptimely project: monitor status, open incidents and alerts, uptime over a period, who is on call, maintenance windows, status pages, and telemetry services.
- `responding-to-incidents`: Runs incident response in Uptimely one confirmed step at a time: declares incidents, acknowledges or resolves incidents and alerts, raises alerts, and runs on-demand monitor checks.
- `adding-uptime-monitors`: Adds a new uptime monitor to an Uptimely project without duplicating an existing one, and optionally runs a first check.

## Limitations

- It needs network access to app.getuptimely.com and a signed-in Uptimely account. There is no offline or self-hosted mode.
- The agent can only use the operations whose scopes you approved. To change them, revoke the connection in Uptimely and run `/mcp auth uptimely` to sign in again.
- Calls act on your real Uptimely data. The included skills ask before any step that sends, publishes or changes something; other prompts should do the same.

## Links

- Docs: https://getuptimely.com/integrations
- Privacy policy: https://getuptimely.com/privacy
- Terms: https://getuptimely.com/terms
- Support: https://app.getuptimely.com/support or [hello@getuptimely.com](mailto:hello@getuptimely.com)

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

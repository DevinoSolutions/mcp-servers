# upAPI plugin for GitHub Copilot CLI

Call a catalog of ready-to-use APIs through one upAPI account and key, without signing up for each upstream service.

The plugin adds the hosted upAPI MCP server (`https://app.upapi.io/api/mcp`, Streamable HTTP) to Copilot CLI. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- An upAPI account (https://upapi.io). upAPI is a hosted service run by Devino Solutions, which also maintains this plugin. What the server lets the agent do depends on your upAPI plan and on the scopes you approve.

## Setup

1. Install the plugin from the Awesome Copilot marketplace, which ships with Copilot CLI:

   ```shell
   copilot plugin install upapi@awesome-copilot
   ```

   Or straight from this repository: `copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/upapi`.

2. Start Copilot CLI and ask for something that uses upAPI. The first call opens a browser window on the upAPI sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth upapi`.
3. Run `/mcp show upapi` to check the connection and see its tools.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the upAPI operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Limitations

- It needs network access to app.upapi.io and a signed-in upAPI account. There is no offline or self-hosted mode.
- The agent can only use the operations whose scopes you approved. To change them, revoke the connection in upAPI and run `/mcp auth upapi` to sign in again.
- Calls act on your real upAPI data. Ask the agent to confirm before any call that sends or changes something.

## Links

- Docs: https://upapi.io/docs/mcp
- Privacy policy: https://upapi.io/privacy
- Terms: https://upapi.io/terms
- Support: https://app.upapi.io/support or [support@upapi.io](mailto:support@upapi.io)

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

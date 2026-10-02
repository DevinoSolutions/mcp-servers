# doDomain plugin for GitHub Copilot CLI

Connect customers' custom domains to your product: guided DNS setup, verification and certificates, managed from doDomain.

The plugin adds the hosted doDomain MCP server (`https://app.dodomain.io/api/mcp`, Streamable HTTP) to Copilot CLI, plus 3 skills for common tasks. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- A doDomain account (https://dodomain.io). doDomain is a hosted service run by Devino Solutions, which also maintains this plugin. What the server lets the agent do depends on your doDomain plan and on the scopes you approve.

## Setup

1. Install the plugin from the Awesome Copilot marketplace, which ships with Copilot CLI:

   ```shell
   copilot plugin install dodomain@awesome-copilot
   ```

   Or straight from this repository: `copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/dodomain`.

2. Start Copilot CLI and ask for something that uses doDomain. The first call opens a browser window on the doDomain sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth dodomain`.
3. Run `/mcp show dodomain` to check the connection and see its tools.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the doDomain operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills

- `preflighting-domains`: Pre-flights a domain in doDomain before anyone touches DNS: finds who runs DNS, the DNS provider and registrable zone, and whether the domain qualifies for one-click connect.
- `connecting-customer-domains`: Starts and follows a doDomain connect session that points a customer's own domain at one of the user's apps, returns the DNS records the customer must add, and verifies them.
- `checking-domain-connections`: Reviews the DNS health of existing doDomain connections and queues rechecks after confirmation.

## Limitations

- It needs network access to app.dodomain.io and a signed-in doDomain account. There is no offline or self-hosted mode.
- The agent can only use the operations whose scopes you approved. To change them, revoke the connection in doDomain and run `/mcp auth dodomain` to sign in again.
- Calls act on your real doDomain data. The included skills ask before any step that sends, publishes or changes something; other prompts should do the same.

## Links

- Docs: https://dodomain.io/docs/connecting-ai-assistants
- Privacy policy: https://dodomain.io/privacy
- Terms: https://dodomain.io/terms
- Support: https://app.dodomain.io/support or [support@dodomain.io](mailto:support@dodomain.io)

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

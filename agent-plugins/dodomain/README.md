# doDomain power

Connect customers' custom domains to your product: guided DNS setup, verification and certificates, managed from doDomain.

This power connects Kiro to the hosted doDomain MCP server at `https://app.dodomain.io/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the doDomain sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://dodomain.io.

Skills included: `checking-domain-connections`, `connecting-customer-domains`, `preflighting-domains`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/dodomain`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the doDomain operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://dodomain.io/privacy
- Terms: https://dodomain.io/terms
- Support: https://app.dodomain.io/support or [support@dodomain.io](mailto:support@dodomain.io)
- Docs: https://dodomain.io/docs/connecting-ai-assistants

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

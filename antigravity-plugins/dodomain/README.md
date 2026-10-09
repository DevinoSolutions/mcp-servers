# doDomain for Antigravity

Connect your customers' custom domains to your product with doDomain: preflight a domain, start a guided DNS connect session, verify records and check health.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted doDomain MCP server at `https://app.dodomain.io/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the doDomain sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://dodomain.io.

Skills included: `checking-domain-connections`, `connecting-customer-domains`, `preflighting-domains`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install dodomain@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/dodomain
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/dodomain`. In the Antigravity IDE, copy this folder into `.agents/plugins/dodomain` (workspace) or `~/.gemini/config/plugins/dodomain` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the doDomain operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

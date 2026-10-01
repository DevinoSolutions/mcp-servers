# upAPI power

Call a catalog of ready-to-use APIs through one upAPI account and key, without signing up for each upstream service.

This power connects Kiro to the hosted upAPI MCP server at `https://app.upapi.io/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the upAPI sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://upapi.io.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/upapi`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the upAPI operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://upapi.io/privacy
- Terms: https://upapi.io/terms
- Support: https://app.upapi.io/support or [support@upapi.io](mailto:support@upapi.io)
- Docs: https://upapi.io/docs/mcp

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

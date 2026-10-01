# Uptimely power

Manage uptime monitors, incidents and status pages, and read check results, in Uptimely.

This power connects Kiro to the hosted Uptimely MCP server at `https://app.getuptimely.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the Uptimely sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://getuptimely.com.

Skills included: `adding-uptime-monitors`, `checking-uptime-status`, `responding-to-incidents`, `writing-postmortems`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/uptimely`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Uptimely operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://getuptimely.com/privacy
- Terms: https://getuptimely.com/terms
- Support: https://app.getuptimely.com/support or [hello@getuptimely.com](mailto:hello@getuptimely.com)
- Docs: https://getuptimely.com/integrations

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

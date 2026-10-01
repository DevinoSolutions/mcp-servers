# Postify power

Draft, schedule and publish social media posts to your connected channels, and read post analytics, from your Postify calendar.

This power connects Kiro to the hosted Postify MCP server at `https://app.usepostify.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the Postify sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://usepostify.com.

Skills included: `drafting-social-posts`, `managing-content-calendar`, `reviewing-social-performance`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/postify`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Postify operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://usepostify.com/privacy
- Terms: https://usepostify.com/terms
- Support: https://app.usepostify.com/support or [hello@devino.ca](mailto:hello@devino.ca)
- Docs: https://usepostify.com/developers

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

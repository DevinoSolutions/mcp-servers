# Postify for Antigravity

Draft, schedule and publish social posts to your connected LinkedIn, X, Instagram, TikTok and other channels, and read post analytics in your Postify calendar.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted Postify MCP server at `https://app.usepostify.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the Postify sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://usepostify.com.

Skills included: `drafting-social-posts`, `managing-content-calendar`, `reviewing-social-performance`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install postify@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/postify
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/postify`. In the Antigravity IDE, copy this folder into `.agents/plugins/postify` (workspace) or `~/.gemini/config/plugins/postify` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Postify operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

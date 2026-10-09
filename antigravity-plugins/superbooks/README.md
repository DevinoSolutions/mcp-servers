# SuperBooks for Antigravity

Work with your SuperBooks books: categorize transactions, match receipts, draft and send invoices, chase unpaid ones, and read P&L, runway and spending reports.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted SuperBooks MCP server at `https://app.superbooks.io/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the SuperBooks sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://superbooks.io.

Skills included: `chasing-unpaid-invoices`, `cleaning-up-bookkeeping`, `drafting-invoices`, `reading-financial-reports`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install superbooks@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/superbooks
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/superbooks`. In the Antigravity IDE, copy this folder into `.agents/plugins/superbooks` (workspace) or `~/.gemini/config/plugins/superbooks` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the SuperBooks operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

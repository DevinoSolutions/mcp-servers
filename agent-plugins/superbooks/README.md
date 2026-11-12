# SuperBooks power

Work with your SuperBooks books: transactions and categories, invoices, customers, receipts, time tracking and financial reports.

This power connects Kiro to the hosted SuperBooks MCP server at `https://app.superbooks.io/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the SuperBooks sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://superbooks.io.

Skills included: `chasing-unpaid-invoices`, `cleaning-up-bookkeeping`, `drafting-invoices`, `reading-financial-reports`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/superbooks`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the SuperBooks operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://superbooks.io/privacy/
- Terms: https://superbooks.io/terms/
- Support: [support@superbooks.io](mailto:support@superbooks.io)
- Docs: https://docs.superbooks.io/mcp

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

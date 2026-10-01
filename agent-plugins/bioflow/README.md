# BioFlow power

Edit and publish your link-in-bio page, its links and blocks, and read page analytics and signups from BioFlow.

This power connects Kiro to the hosted BioFlow MCP server at `https://app.getbioflow.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the BioFlow sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://getbioflow.com.

Skills included: `analyzing-page-performance`, `editing-page-drafts`, `publishing-pages`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/bioflow`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the BioFlow operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://app.getbioflow.com/privacy
- Terms: https://app.getbioflow.com/terms
- Support: https://app.getbioflow.com/support or [hello@devino.ca](mailto:hello@devino.ca)
- Docs: https://getbioflow.com/mcp

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

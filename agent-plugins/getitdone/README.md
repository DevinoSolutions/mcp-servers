# GetItDone power

Create, update and track tasks and projects across your GetItDone team workspaces.

This power connects Kiro to the hosted GetItDone MCP server at `https://app.nowgetitdone.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the GetItDone sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://nowgetitdone.com.

Skills included: `capturing-tasks`, `investigating-tasks`, `reviewing-workload`, `searching-getitdone-api-docs`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/getitdone`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the GetItDone operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://nowgetitdone.com/privacy
- Terms: https://nowgetitdone.com/terms
- Support: https://app.nowgetitdone.com/support
- Docs: https://nowgetitdone.com/docs/connecting-ai-assistants

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

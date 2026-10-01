# Shorty power

Summarize and transcribe videos, audio files, documents and web pages with Shorty.

This power connects Kiro to the hosted Shorty MCP server at `https://aishorty.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the Shorty sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://aishorty.com.

Skills included: `researching-summary-library`, `summarizing-sources`, `transcribing-media`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/shorty`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Shorty operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://aishorty.com/privacy
- Terms: https://aishorty.com/terms
- Support: https://aishorty.com/support
- Docs: https://aishorty.com/docs/connecting-ai-assistants

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

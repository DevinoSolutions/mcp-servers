# Shorty for Antigravity

Summarize YouTube videos, web pages, articles and documents, transcribe audio and video, add captions, and search your saved summaries with Shorty.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted Shorty MCP server at `https://aishorty.com/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the Shorty sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://aishorty.com.

Skills included: `researching-summary-library`, `summarizing-sources`, `transcribing-media`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install shorty@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/shorty
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/shorty`. In the Antigravity IDE, copy this folder into `.agents/plugins/shorty` (workspace) or `~/.gemini/config/plugins/shorty` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Shorty operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

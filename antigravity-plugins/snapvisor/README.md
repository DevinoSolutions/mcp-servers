# SnapVisor for Antigravity

Review SnapVisor visual regression builds: see what changed in screenshot diffs, approve or reject builds, handle flaky changes and join review threads.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted SnapVisor MCP server at `https://mcp.snapvisor.io/` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the SnapVisor sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://snapvisor.io.

Skills included: `discussing-builds`, `handling-flaky-changes`, `reporting-snapvisor-usage`, `reviewing-visual-builds`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install snapvisor@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/snapvisor
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/snapvisor`. In the Antigravity IDE, copy this folder into `.agents/plugins/snapvisor` (workspace) or `~/.gemini/config/plugins/snapvisor` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the SnapVisor operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

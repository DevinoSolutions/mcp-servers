# SnapVisor power

Review visual regression builds, approve or reject screenshot changes, and manage SnapVisor projects.

This power connects Kiro to the hosted SnapVisor MCP server at `https://mcp.snapvisor.io/` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the SnapVisor sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://snapvisor.io.

Skills included: `discussing-builds`, `handling-flaky-changes`, `reporting-snapvisor-usage`, `reviewing-visual-builds`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/snapvisor`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the SnapVisor operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://snapvisor.io/privacy
- Terms: https://snapvisor.io/terms
- Support: https://snapvisor.io/support or [support@snapvisor.io](mailto:support@snapvisor.io)
- Docs: https://snapvisor.io/docs

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

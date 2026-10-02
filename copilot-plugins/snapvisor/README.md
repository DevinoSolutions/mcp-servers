# SnapVisor plugin for GitHub Copilot CLI

Review visual regression builds, approve or reject screenshot changes, and manage SnapVisor projects.

The plugin adds the hosted SnapVisor MCP server (`https://mcp.snapvisor.io/`, Streamable HTTP) to Copilot CLI, plus 2 skills for common tasks. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- A SnapVisor account (https://snapvisor.io). SnapVisor is a hosted service run by Devino Solutions, which also maintains this plugin. What the server lets the agent do depends on your SnapVisor plan and on the scopes you approve.

## Setup

1. Install the plugin from the Awesome Copilot marketplace, which ships with Copilot CLI:

   ```shell
   copilot plugin install snapvisor@awesome-copilot
   ```

   Or straight from this repository: `copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/snapvisor`.

2. Start Copilot CLI and ask for something that uses SnapVisor. The first call opens a browser window on the SnapVisor sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth snapvisor`.
3. Run `/mcp show snapvisor` to check the connection and see its tools.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the SnapVisor operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills

- `reviewing-visual-builds`: Reviews a SnapVisor visual regression build: shows what changed in the screenshot diffs for a branch or commit and approves or rejects the build after the user confirms.
- `handling-flaky-changes`: Handles flaky or known visual changes in SnapVisor: ignores or un-ignores a change after confirmation, finds flaky tests, and lists the ignored changes for a project.

## Limitations

- It needs network access to mcp.snapvisor.io and a signed-in SnapVisor account. There is no offline or self-hosted mode.
- The agent can only use the operations whose scopes you approved. To change them, revoke the connection in SnapVisor and run `/mcp auth snapvisor` to sign in again.
- Calls act on your real SnapVisor data. The included skills ask before any step that sends, publishes or changes something; other prompts should do the same.

## Links

- Docs: https://snapvisor.io/docs
- Privacy policy: https://snapvisor.io/privacy
- Terms: https://snapvisor.io/terms
- Support: https://snapvisor.io/support or [support@snapvisor.io](mailto:support@snapvisor.io)

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

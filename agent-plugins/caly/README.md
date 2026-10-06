# Caly power

Find open meeting times, book, reschedule and cancel meetings, and read your event types, bookings and schedules in Caly.

This power connects Kiro to the hosted Caly MCP server at `https://mcp.trycaly.com/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the Caly sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://trycaly.com.

Skills included: `booking-meetings`, `finding-meeting-times`, `managing-bookings`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/caly`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the Caly operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://trycaly.com/privacy
- Terms: https://trycaly.com/terms
- Support: [hello@devino.ca](mailto:hello@devino.ca)
- Docs: https://trycaly.com/docs/

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

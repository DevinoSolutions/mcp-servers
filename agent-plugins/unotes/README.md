# uNotes power

Search a library of university course materials (past exams, assignments, lab reports, lecture notes) and your uNotes flashcards and quizzes.

This power connects Kiro to the hosted uNotes MCP server at `https://unotes.net/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the uNotes sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://unotes.net.

Skills included: `building-study-guides`, `planning-revision`, `researching-course-material`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/unotes`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the uNotes operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://unotes.net/privacy
- Terms: https://unotes.net/terms
- Support: https://unotes.net/support
- Docs: https://unotes.net/docs

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

# uNotes for Antigravity

Search a library of university course material: past exams, assignments, lab reports and lecture notes, plus your uNotes flashcards and quizzes, to study.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted uNotes MCP server at `https://unotes.net/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the uNotes sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://unotes.net.

Skills included: `building-study-guides`, `planning-revision`, `researching-course-material`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install unotes@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/unotes
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/unotes`. In the Antigravity IDE, copy this folder into `.agents/plugins/unotes` (workspace) or `~/.gemini/config/plugins/unotes` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the uNotes operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

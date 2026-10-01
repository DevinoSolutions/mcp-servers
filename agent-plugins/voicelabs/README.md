# VoiceLabs power

Generate speech from text in your voices and transcribe audio with VoiceLabs.

This power connects Kiro to the hosted VoiceLabs MCP server at `https://app.voicelabs.now/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the VoiceLabs sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://voicelabs.now.

Skills included: `managing-voice-library`, `reading-text-aloud`, `transcribing-audio`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/voicelabs`.

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the VoiceLabs operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Privacy and support

- Privacy policy: https://voicelabs.now/privacy
- Terms: https://voicelabs.now/terms
- Support: https://voicelabs.now/support
- Docs: https://voicelabs.now/mcp

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

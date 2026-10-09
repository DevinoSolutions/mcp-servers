# VoiceLabs for Antigravity

Generate speech from text in your VoiceLabs voices, transcribe audio to text, and manage your voice library, including consented voice cloning, from the agent.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted VoiceLabs MCP server at `https://app.voicelabs.now/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the VoiceLabs sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. You need an account at https://voicelabs.now.

Skills included: `managing-voice-library`, `reading-text-aloud`, `transcribing-audio`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install voicelabs@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/voicelabs
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/voicelabs`. In the Antigravity IDE, copy this folder into `.agents/plugins/voicelabs` (workspace) or `~/.gemini/config/plugins/voicelabs` (global).

## How the tools appear

The server runs in Code Mode: it exposes `search_tools` and `execute_typescript`. The agent calls `search_tools` to see the VoiceLabs operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions, with the same scopes, confirmations and audit log as a direct call.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

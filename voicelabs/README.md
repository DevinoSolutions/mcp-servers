# VoiceLabs MCP server

Generate speech from text in your voices and transcribe audio with VoiceLabs.

![VoiceLabs](assets/logo.png)

- Endpoint: `https://app.voicelabs.now/api/mcp` (Streamable HTTP, OAuth 2.1)
- Product: https://voicelabs.now
- Docs: https://voicelabs.now/mcp

## Install

The server is remote, so there is nothing to run locally. It signs you in with OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 metadata): the first time your client calls it, a browser window opens on the VoiceLabs sign-in and consent screen, where you choose what the assistant may do.

**Cursor:** install the `voicelabs` plugin from the Cursor Marketplace, or [add the server in one click](https://cursor.com/install-mcp?name=voicelabs&config=eyJ1cmwiOiJodHRwczovL2FwcC52b2ljZWxhYnMubm93L2FwaS9tY3AifQ%3D%3D), or put this in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "voicelabs": {
      "url": "https://app.voicelabs.now/api/mcp"
    }
  }
}
```

**Cline:** ask Cline to "install the VoiceLabs MCP server from https://github.com/DevinoSolutions/mcp-servers/tree/main/voicelabs" (it follows [llms-install.md](llms-install.md)), or add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "voicelabs": {
      "type": "streamableHttp",
      "url": "https://app.voicelabs.now/api/mcp",
      "disabled": false
    }
  }
}
```

**VS Code (Copilot agent mode):** [install in one click](https://insiders.vscode.dev/redirect/mcp/install?name=voicelabs&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.voicelabs.now%2Fapi%2Fmcp%22%7D), or add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "voicelabs": {
      "type": "http",
      "url": "https://app.voicelabs.now/api/mcp"
    }
  }
}
```

**Claude Code:** `claude mcp add --transport http voicelabs https://app.voicelabs.now/api/mcp`

**Claude and ChatGPT:** VoiceLabs is listed in the Claude Connectors Directory and ChatGPT Apps.

**Any other MCP client:** Streamable HTTP endpoint `https://app.voicelabs.now/api/mcp`. It is also published in the official MCP Registry.

## How the tools appear

The server runs in Code Mode: `tools/list` shows `search_tools` and `execute_typescript`. The assistant calls `search_tools` to see the VoiceLabs operations your sign-in reached, then runs them inside `execute_typescript` as `external_<name>` functions. Every call keeps the same scopes, confirmations and audit log as a direct call. An operation whose scope you did not grant is never declared.

## Skills (Cursor plugin)

- `managing-voice-library`
- `reading-text-aloud`
- `transcribing-audio`

## Links

- Privacy policy: https://voicelabs.now/privacy
- Terms: https://voicelabs.now/terms
- Support: https://voicelabs.now/support

# UpRank for Antigravity

Research, draft and score evidence-backed articles for your company site in UpRank, with every claim traced to a source and hard quality gates before anything is published.

This plugin connects [Google Antigravity](https://antigravity.google) to the hosted UpRank MCP server at `https://uprank.devino.ca/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time the agent calls the server, a browser window opens on the UpRank sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. Only a workspace owner can approve the consent. You need an account at https://uprank.devino.ca.

Skills included: `drafting-evidence-backed-articles`, `reviewing-article-quality`.

## Install

From the Antigravity Marketplace, once listed:

```bash
agy plugin install uprank@antigravity-plugins-official
```

Directly from this repository:

```bash
agy plugin install https://github.com/DevinoSolutions/mcp-servers/antigravity-plugins/uprank
```

Or clone the repository and run `agy plugin install ./antigravity-plugins/uprank`. In the Antigravity IDE, copy this folder into `.agents/plugins/uprank` (workspace) or `~/.gemini/config/plugins/uprank` (global).

## Tools

The server defines 17 tools (an OAuth connection sees 16: live publishing, `publication_publish`, needs an API key with the `publication:live` scope). Long-running tools return a `workflowRunId` to poll with `pipeline_status`. `publication_create_draft` records a draft publication in UpRank and does not push to a CMS.

## Support

Maintained by [Devino Solutions](https://devino.ca). Contact support@devino.ca. MIT licensed.

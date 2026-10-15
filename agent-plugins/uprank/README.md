# UpRank power

Research, draft, score and prepare evidence-backed articles for your company site in UpRank, with every claim traced to a source and hard quality gates before anything is published.

This power connects Kiro to the hosted UpRank MCP server at `https://uprank.devino.ca/api/mcp` (Streamable HTTP). There is nothing to run locally and no API key: the first time Kiro calls the server, a browser window opens on the UpRank sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. Only a workspace owner can approve the consent. You need an account at https://uprank.devino.ca.

Skills included: `drafting-evidence-backed-articles`, `reviewing-article-quality`.

## Install

In Kiro, open the Powers panel, choose **Add Custom Power → Import power from GitHub** and enter `https://github.com/DevinoSolutions/mcp-servers/tree/main/agent-plugins/uprank`.

## Tools

The server lists 17 tools directly. Long-running tools return a `workflowRunId` to poll with `pipeline_status`. `publication_create_draft` records a draft publication in UpRank and does not push to a CMS; `publication_publish` needs the `publication:live` scope, which OAuth sign-ins never carry.

## Privacy and support

- Privacy policy: https://uprank.devino.ca/privacy
- Support: support@devino.ca
- Docs: https://uprank.devino.ca/agent-setup

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

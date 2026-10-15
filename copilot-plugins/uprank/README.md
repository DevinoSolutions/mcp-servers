# UpRank plugin for GitHub Copilot CLI

Research, draft, score and prepare evidence-backed articles for your company site in UpRank, with every claim traced to a source and hard quality gates before anything is published.

The plugin adds the hosted UpRank MCP server (`https://uprank.devino.ca/api/mcp`, Streamable HTTP) to Copilot CLI, plus 2 skills for common tasks. Nothing runs locally and there is no API key to configure.

## Requirements

- GitHub Copilot CLI.
- An UpRank account (https://uprank.devino.ca). UpRank is a hosted service run by Devino Solutions, which also maintains this plugin. Only a workspace owner can approve the OAuth consent.

## Setup

1. Install the plugin straight from this repository:

   ```shell
   copilot plugin install DevinoSolutions/mcp-servers:copilot-plugins/uprank
   ```

2. Start Copilot CLI and ask for something that uses UpRank. The first call opens a browser window on the UpRank sign-in and consent screen (OAuth 2.1 with PKCE and dynamic client registration), where you choose what the agent may do. If the server later shows `needs-auth`, run `/mcp auth uprank`.
3. Run `/mcp show uprank` to check the connection and see its tools.

## Tools

The server lists 17 tools directly: `pipeline_run`, `pipeline_status`, `brand_ingest`, `brand_get`, `topic_research`, `brief_generate`, `article_generate`, `article_score`, `article_revise`, `links_suggest`, `media_select`, `publication_create_draft`, `publication_publish`, `publication_status`, `refresh_list`, `article_get` and `article_list`. Long-running tools return a `workflowRunId` to poll with `pipeline_status`.

## Skills

- `drafting-evidence-backed-articles`: Runs the UpRank pipeline to research, draft and score an article, then records a draft publication. Never publishes live.
- `reviewing-article-quality`: Explains why an article fails the quality gates, and revises it, suggests internal links or picks media on request.

## Limitations

- It needs network access to uprank.devino.ca and a signed-in UpRank account. There is no offline or self-hosted mode.
- `publication_create_draft` records a draft publication in UpRank and does not push to a CMS. `publication_publish` needs the `publication:live` scope, which OAuth sign-ins never carry.
- UpRank makes no ranking or traffic promises.

## Links

- Docs: https://uprank.devino.ca/agent-setup
- Privacy policy: https://uprank.devino.ca/privacy
- Support: support@devino.ca

Maintained by [Devino Solutions](https://devino.ca). MIT licensed.

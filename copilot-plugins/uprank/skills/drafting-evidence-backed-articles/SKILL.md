---
name: drafting-evidence-backed-articles
description: "Runs the UpRank pipeline to research, draft and score an article for the user's own company site, then records a draft publication. Use when the user asks to 'write an article about X with UpRank', 'research topics for our blog', 'draft a post from this brief', 'run the UpRank pipeline', or 'prepare this article for our CMS as a draft'. Never publishes live."
---

# Draft an evidence-backed article with UpRank

Take a topic from research to a scored article and a draft publication record. Every claim in an UpRank article is traced to a source gathered before drafting, and nothing is published until it clears the hard quality gates.

## Connecting and calling the tools

Every tool in this skill comes from the `uprank` MCP server, the UpRank connector, and is written here as `uprank:<tool>`. The server lists its tools directly (it defines 17; an OAuth connection sees 16, because `publication_publish` is hidden), so call them by name.

- **"Tool not found" or no `uprank` tools at all:** UpRank is not connected yet. Add the server as shown in https://github.com/DevinoSolutions/mcp-servers/tree/main/uprank#install; it signs in with OAuth on first use, and only a workspace owner can approve the consent screen.
- **Long-running tools** (`uprank:pipeline_run`, `uprank:article_generate`, `uprank:article_revise`, and similar) return a `workflowRunId`. Poll `uprank:pipeline_status` with it until the run finishes instead of assuming it is done.

## Tools you will use

- `uprank:brand_get`: read the company's stored brand profile (read-only). If it is empty, offer `uprank:brand_ingest` first.
- `uprank:topic_research`: find topics worth writing about for this brand.
- `uprank:pipeline_run`: run research, brief, draft and scoring end to end for one topic. Returns a `workflowRunId`.
- `uprank:pipeline_status`: poll a run by `workflowRunId` (read-only).
- `uprank:article_get`: read the finished article, its sources and its scores (read-only).
- `uprank:article_score`: score an article on the 11 quality dimensions and check the 13 hard gates.
- `uprank:publication_create_draft`: record a DRAFT publication in UpRank for the article.

## Workflow

1. Call `uprank:brand_get`. If there is no brand profile, ask for the company site and call `uprank:brand_ingest`, then poll if it returns a `workflowRunId`.
2. If the user has no topic, call `uprank:topic_research` and let them choose. Do not pick for them.
3. Call `uprank:pipeline_run` for the chosen topic. Tell the user it can take a while.
4. Poll `uprank:pipeline_status` with the `workflowRunId` until the run reports it is finished or failed. Report a failure plainly with the reason given.
5. Call `uprank:article_get` and summarize: title, the sources behind the claims, and the scores.
6. Call `uprank:article_score` if the user wants a fresh score, and list any hard gate the article does not clear.
7. Only when the user asks to prepare it for their site, call `uprank:publication_create_draft`.

## Rules

- `uprank:publication_create_draft` creates a DRAFT publication record in UpRank. It does not push anything to the CMS. Say so; do not tell the user the article is on their site.
- Never call `uprank:publication_publish` from this skill. It records a live publication request and needs the `publication:live` scope, which OAuth sign-ins never carry; it is listed only for an API key that holds that scope.
- Do not promise rankings, traffic or search results. UpRank scores quality and traces sources; it does not guarantee how the article performs.
- Do not invent sources or claims. If a gate fails, report it and offer `uprank:article_revise` (see `reviewing-article-quality`).

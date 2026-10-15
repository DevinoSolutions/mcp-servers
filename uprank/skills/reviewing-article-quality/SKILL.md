---
name: reviewing-article-quality
description: "Reviews an existing UpRank article against its quality scores and hard gates, and revises it, suggests internal links or picks media on request. Use when the user asks 'why did this article fail the gates', 'score article X', 'revise this draft', 'suggest internal links', 'pick images for this article', 'what needs a refresh', or 'list my articles'."
---

# Review and improve an UpRank article

Explain where an article stands against UpRank's 11 scored dimensions and 13 hard gates, and improve it one confirmed step at a time.

## Connecting and calling the tools

Every tool in this skill comes from the `uprank` MCP server, the UpRank connector, and is written here as `uprank:<tool>`. The server lists its tools directly (it defines 17; an OAuth connection sees 16, because `publication_publish` is hidden), so call them by name.

- **"Tool not found" or no `uprank` tools at all:** UpRank is not connected yet. Add the server as shown in https://github.com/DevinoSolutions/mcp-servers/tree/main/uprank#install; it signs in with OAuth on first use, and only a workspace owner can approve the consent screen.
- **Long-running tools** (`uprank:pipeline_run`, `uprank:article_generate`, `uprank:article_revise`, and similar) return a `workflowRunId`. Poll `uprank:pipeline_status` with it until the run finishes instead of assuming it is done.

## Tools you will use

- `uprank:article_list` and `uprank:article_get`: find an article and read it with its sources and scores (read-only).
- `uprank:article_score`: re-score an article and report each gate.
- `uprank:article_revise`: revise an article to address specific findings. Returns a `workflowRunId`.
- `uprank:links_suggest`: suggest internal links for an article.
- `uprank:media_select`: select media for an article.
- `uprank:refresh_list`: list published articles that are due a refresh (read-only).
- `uprank:publication_status`: check the state of a publication record (read-only).
- `uprank:pipeline_status`: poll a long-running revision by `workflowRunId` (read-only).

## Workflow

1. Find the article with `uprank:article_list` if the user gave a name, then read it with `uprank:article_get`. Ask if more than one matches.
2. Call `uprank:article_score` and report the dimension scores and every hard gate that does not pass, in plain words.
3. Propose the changes that would address each finding and wait for the user to agree before calling `uprank:article_revise`.
4. Poll `uprank:pipeline_status` until the revision finishes, then score again and report the difference honestly, including when a gate still fails.
5. On request, call `uprank:links_suggest` or `uprank:media_select` and show the suggestions before anything is applied.
6. For "what is stale", call `uprank:refresh_list`.

## Rules

- Read the article and its scores before suggesting changes; do not guess at why a gate failed.
- Ask before `uprank:article_revise`; it rewrites the user's draft.
- Do not call `uprank:publication_publish` from this skill, and do not describe a draft publication as live.
- Do not promise ranking or traffic improvements from a higher score.

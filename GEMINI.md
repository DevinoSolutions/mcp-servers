# Devino MCP servers

This extension connects Gemini CLI to the hosted MCP servers of the Devino Solutions products. Each server is a Streamable HTTP endpoint protected by OAuth 2.1. Nothing runs locally.

## Signing in

A server stays disconnected until the user signs in to that product. Run `/mcp auth <server>` (for example `/mcp auth postify`), finish the sign-in in the browser, and approve the scopes. Only servers the user actually uses need to be authorized; the others can be ignored or disabled with `/mcp`.

## Servers

- `bioflow` (BioFlow): Edit and publish your link-in-bio page, its links and blocks, and read page analytics and signups from BioFlow. Docs: https://getbioflow.com/mcp
- `dodomain` (doDomain): Connect customers' custom domains to your product: guided DNS setup, verification and certificates, managed from doDomain. Docs: https://dodomain.io/docs/connecting-ai-assistants
- `getitdone` (GetItDone): Create, update and track tasks and projects across your GetItDone team workspaces. Docs: https://nowgetitdone.com/docs/connecting-ai-assistants
- `notifly` (Notifly): Manage notification workflows, subscribers and topics, and trigger delivery across email, SMS, push, chat and in-app channels with Notifly. Docs: https://notifly.io/developers
- `postify` (Postify): Draft, schedule and publish social media posts to your connected channels, and read post analytics, from your Postify calendar. Docs: https://usepostify.com/developers
- `sendly` (Sendly): Send transactional email, run campaigns, and manage contacts, lists and segments in Sendly. Docs: https://docs.sendly.now/guides/mcp
- `shorty` (Shorty): Summarize and transcribe videos, audio files, documents and web pages with Shorty. Docs: https://aishorty.com/docs/connecting-ai-assistants
- `snapvisor` (SnapVisor): Review visual regression builds, approve or reject screenshot changes, and manage SnapVisor projects. Docs: https://snapvisor.io/docs
- `superbooks` (SuperBooks): Work with your SuperBooks books: transactions and categories, invoices, customers, receipts, time tracking and financial reports. Docs: https://docs.superbooks.io/mcp
- `unotes` (uNotes): Search a library of university course materials (past exams, assignments, lab reports, lecture notes) and your uNotes flashcards and quizzes. Docs: https://unotes.net/docs
- `upapi` (upAPI): Call a catalog of ready-to-use APIs through one upAPI account and key, without signing up for each upstream service. Docs: https://upapi.io/docs/mcp
- `uptimely` (Uptimely): Manage uptime monitors, incidents and status pages, and read check results, in Uptimely. Docs: https://getuptimely.com/integrations
- `voicelabs` (VoiceLabs): Generate speech from text in your voices and transcribe audio with VoiceLabs. Docs: https://voicelabs.now/mcp

## Conventions

Most servers expose two tools, `search_tools` and `execute_typescript`. Call `search_tools` first to see what this connection can reach, then run one `execute_typescript` program that calls the declared `external_*` functions. Ask the user before any write that publishes, sends or deletes something.

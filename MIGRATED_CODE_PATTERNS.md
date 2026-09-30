# Code-pattern consolidation notes

This document records selective migrations from small historical repositories into `daily-growth`.

## `domain-driven-js`

Preserved the dungeon domain-modelling exercise under `architecture/ddd/javascript/dungeons/`. The generated Express/EJS shell was intentionally omitted because the durable lesson is the domain boundary and invariant modelling, not the framework scaffold.

## `quick-frontend-starter`

Preserved the authored lessons around authentication context, API hooks and project bootstrap under `frontend/patterns/`. The old Create React App project, generated assets, CSS and placeholder components were intentionally omitted. Security-sensitive demo behaviour such as storing credentials/client session data naively was not carried forward.

## `mcp-server-langchain`

Preserved the architecture exploration under `ai/mcp/langchain-experiment/`. The source repository was an early HTTP chat/LangChain/Redis scaffold rather than a completed MCP server, and the migrated note states that explicitly.

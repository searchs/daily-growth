# LangChain chat-service / MCP exploration

Consolidated from the historical `searchs/mcp-server-langchain` repository.

Despite the repository name, the implementation had not yet become a complete Model Context Protocol server. It was an early FastAPI-style chat-service scaffold with:

- an LLM client adapter;
- a chat/application service;
- Redis-backed user context/history;
- HTTP routes;
- environment-based API-key configuration.

The useful architectural direction is retained here rather than presenting the old scaffold as a finished MCP implementation.

## Better target architecture

```text
Protocol/HTTP adapter
        ↓
Application use case
        ↓
Conversation port ─────→ history/context adapter
        ↓
LLM port ──────────────→ LangChain/OpenAI adapter
```

The application layer should depend on interfaces/ports rather than importing a concrete LangChain model globally.

## Lessons from the historical scaffold

- Fail fast when required credentials/configuration are absent; avoid sentinel values such as `MISSING_KEY`.
- Keep the LLM provider behind a port so model/provider changes do not alter application logic.
- Treat chat history and user context as persistence concerns.
- Keep protocol-specific schemas at the outer adapter boundary.
- If this is developed into an MCP server later, implement actual MCP tools/resources/prompts and transport semantics rather than simply renaming an HTTP chat API.

This directory is therefore an architecture note/experiment, not a production MCP package.

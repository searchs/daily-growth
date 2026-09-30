# Daily Growth Consolidation Plan

This branch prepares `daily-growth` to become the canonical repository for durable software-engineering learning material.

## Migration principles

1. Preserve authored work that still teaches a useful concept.
2. Do not copy third-party course/reference repositories wholesale.
3. Keep explicit attribution for course-derived exercises that are worth retaining.
4. Prefer one curated migration commit for small examples; preserve full history only when the history itself is valuable.
5. Do not delete a source repository until migrated content has been verified in this repository.

## Planned destinations

| Source repository | Destination |
| --- | --- |
| `groovybox` | `languages/groovy/` |
| `mongobox` | `databases/mongodb/` |
| `algorithms` | `computer-science/algorithms/python/` |
| `ZioBegins` | `languages/scala/zio/` |
| `underscore-scala` | `languages/scala/functional-programming/` |
| `in-few-steps` | `guides/` |
| `domain-driven-js` | `architecture/ddd/javascript/` |
| `python-mastery-ztm` | selective material under `languages/python/` |
| `hotels_py_intro` | `languages/python/teaching/hotel-intro/` |
| `mcp-server-langchain` | `ai/mcp/langchain-experiment/` |
| `quick-frontend-starter` | selected patterns under `frontend/patterns/` |
| `rust-systems-programming` | useful CI workflow under `devops/github-actions/` |
| `SaaS-Foundations` | workflow example under `devops/github-actions/` |
| `rhema` | selected Python/data-analysis material |
| `analytics` | selected general engineering/analytics material |

## Existing-root restructuring

The current root folders (`builder`, `factory`, `mvc`, `solids`, `domain-driven`, `python`, `scala`, `typescripts`, etc.) will be moved incrementally into the target taxonomy. Moves should remain reviewable and should not mix unrelated refactoring with imported material.

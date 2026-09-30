# JavaScript/TypeScript DDD dungeon exercise

This exercise was consolidated from `searchs/domain-driven-js`.

The historical repository mixed an Express-generated application with a small in-memory `Dungeons` model. The durable idea is the domain boundary rather than the Express scaffolding, so the migrated version focuses on an aggregate-like domain object and a repository port.

## Concepts

- Keep invariants (`capacity`, `availableCells`) inside the domain object.
- Expose behaviour (`bookCells`) rather than allowing callers to mutate state directly.
- Keep persistence behind a repository interface.
- Let HTTP/framework adapters call application use cases rather than placing domain logic in routes.

A next step would be to add an application service such as `BookDungeonCells`, plus an in-memory repository implementation and tests around over-booking and invalid quantities.

# Migration from `in-few-steps`

The historical `searchs/in-few-steps` repository was consolidated into `daily-growth` so durable quick-start material lives in one maintained knowledge base.

## Preserved and modernised

- Terraform getting started
- Terraform GitHub provider
- SQLAlchemy ORM
- SQLite and parameterised search
- Beautiful Soup web scraping
- FastAPI blogging/API structure
- Apache Pulsar with Scala
- Apache Impala/HDFS notes
- Docker with Java and MySQL
- Next.js with headless WordPress

## Intentionally not preserved

The small birthday-notification note and the two lucky-number scripts were not migrated because they add little durable value relative to the canonical examples already retained in `daily-growth`.

The source guides were curated rather than copied verbatim. Security-sensitive or outdated patterns were corrected during migration, including inline Terraform credentials, dynamic SQL string construction, old Next.js APIs and Impala mutation semantics.

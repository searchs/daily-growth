# Web analytics and instrumentation principles

Curated from the old `analytics` repository.

## Instrument intentionally

Useful events and measurements include:
- request/response failures
- conversion goals
- authentication and authorisation outcomes
- feature activation and navigation
- performance timings
- page-ready/render timings
- experiment exposure and variation assignment

Never log passwords, secret tokens, payment-card data or unnecessary personal data.

## Experimentation

The old repository contained a JavaScript A/B-test inspection helper tied to a specific analytics implementation. The durable lesson is broader: keep experiment identifiers and variation assignments explicit, avoid dynamic `eval`, and expose experiment state through a typed analytics abstraction rather than reading vendor globals throughout the UI.

## Product metrics vocabulary

Common commercial metrics represented in the old notes included viral coefficient, churn, MRR, CAC and customer lifetime value. Treat these as product/business metrics, not substitutes for technical observability.

## Separation of concerns

Analytics should be an adapter behind application-owned events. Domain/application code emits meaningful events; vendor SDKs translate them into provider-specific calls. This keeps measurement replaceable and testable.

# FastAPI blogging API quickstart

Consolidated from the historical `in-few-steps` repository.

## Minimal API

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}
```

Run locally with:

```bash
uv run fastapi dev main.py
```

## Suggested structure

```text
app/
  api/
  application/
  domain/
  infrastructure/
  main.py
```

For a real blogging application, keep HTTP models separate from persistence/domain models. A typical flow is:

```text
HTTP request
  -> API validation
  -> application use case
  -> domain model
  -> repository port
  -> persistence adapter
```

## Production considerations

- Use Pydantic request/response schemas rather than ORM models as API contracts.
- Manage database sessions at request/use-case boundaries.
- Use migrations for schema evolution.
- Add authentication/authorisation before exposing write endpoints.
- Test application use cases separately from HTTP integration tests.

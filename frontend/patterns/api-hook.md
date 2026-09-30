# React API-hook pattern

Consolidated from `searchs/quick-frontend-starter`.

The historical `useAPI` hook combined request execution, authentication, timeout handling, response state and an in-memory cache. Those concerns are useful to study, but a production application should be deliberate about which belong in one hook.

## Minimal typed request helper

```ts
export async function requestJson<T>(
  input: RequestInfo | URL,
  init: RequestInit = {},
): Promise<T> {
  const response = await fetch(input, {
    ...init,
    headers: {
      Accept: "application/json",
      ...init.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }

  return (await response.json()) as T;
}
```

## Hook responsibilities

A thin hook can own:

- `loading` / pending state;
- the latest typed result;
- normalised errors;
- cancellation with `AbortController`.

Authentication headers should come from an authentication/session abstraction rather than inventing bearer tokens from a user id. Cache behaviour should normally be delegated to a mature query/cache library when the application needs invalidation, deduplication, retries or background refresh.

## Design lesson

Prefer composition:

```text
Auth/session adapter
        ↓
HTTP client
        ↓
Query/cache layer
        ↓
Feature-specific hook
        ↓
Component
```

rather than one global hook owning every network concern.

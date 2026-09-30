# React authentication-context pattern

Consolidated from `searchs/quick-frontend-starter` and corrected for safer authentication boundaries.

The historical starter demonstrated a React context/provider, protected routes and a login page. Its demo implementation also persisted a mock user object to `localStorage`; one later version even included the submitted password in that object. That behaviour is intentionally **not** preserved.

## Recommended boundary

```ts
export interface AuthUser {
  id: string;
  email: string;
  name: string;
}

export interface AuthContextValue {
  user: AuthUser | null;
  loading: boolean;
  signIn(email: string, password: string): Promise<void>;
  signOut(): Promise<void>;
}
```

The provider should delegate credentials to an authentication service and keep only the minimum client-side session state required by the application.

## Rules

- Never persist plaintext passwords.
- Prefer secure, HTTP-only cookies for browser session tokens when your architecture supports them.
- Treat `localStorage` as readable by JavaScript and therefore exposed to XSS.
- Keep authentication state separate from authorisation decisions.
- Protected client routes improve UX but do not replace server-side access control.
- Model loading/unknown-session state explicitly so protected routes do not flash unauthorised content.

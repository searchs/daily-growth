# Frontend project bootstrap pattern

Consolidated from the authored `create-app.sh` in `searchs/quick-frontend-starter`.

The original script automated project creation, dependency installation and a standard folder layout for auth, dashboard, services, types, hooks, contexts and routes. The reusable lesson is the bootstrap checklist, not the old Create React App command.

## Suggested modern bootstrap

For a contemporary React application, start from the framework/build tool appropriate to the product rather than hard-coding Create React App. For example:

```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
```

Then establish explicit boundaries:

```text
src/
  app/
  features/
  components/
  services/
  hooks/
  types/
  routes/
  test/
```

## Bootstrap checklist

1. Enable strict TypeScript.
2. Add formatting/linting before feature work.
3. Add unit/component tests and CI immediately.
4. Define environment-variable handling and an `.env.example`.
5. Establish routing and error boundaries.
6. Add authentication only through a real session/auth abstraction.
7. Keep reusable UI separate from feature/domain modules.
8. Avoid generating empty placeholder components solely to satisfy a folder convention.

The historical script is intentionally not copied verbatim because its dependencies and Create React App foundation are dated; its automation intent is retained here as a maintainable checklist.

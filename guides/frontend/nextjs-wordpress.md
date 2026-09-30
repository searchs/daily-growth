# Next.js with a headless WordPress backend

Consolidated from the historical `in-few-steps` repository and updated for modern Next.js patterns.

## Prerequisites

- A WordPress site with the REST API available
- A Next.js application
- `WORDPRESS_URL` configured through environment variables

## Fetch posts

```ts
const wordpressUrl = process.env.WORDPRESS_URL;

if (!wordpressUrl) {
  throw new Error("WORDPRESS_URL is required");
}

export async function fetchPosts() {
  const response = await fetch(
    `${wordpressUrl}/wp-json/wp/v2/posts?_embed=true&per_page=20`,
    { next: { revalidate: 300 } },
  );

  if (!response.ok) {
    throw new Error(`WordPress request failed: ${response.status}`);
  }

  return response.json();
}
```

## Fetch by slug

```ts
export async function fetchPostBySlug(slug: string) {
  const response = await fetch(
    `${wordpressUrl}/wp-json/wp/v2/posts?slug=${encodeURIComponent(slug)}&_embed=true`,
    { next: { revalidate: 300 } },
  );

  if (!response.ok) {
    throw new Error(`WordPress request failed: ${response.status}`);
  }

  const posts = await response.json();
  return posts[0] ?? null;
}
```

## Rendering considerations

WordPress post bodies contain HTML. If you render that HTML directly, treat WordPress as a trusted content source and consider sanitisation when authors or upstream plugins are not fully trusted.

For production systems, add caching/revalidation, explicit content types, error states, preview workflows and image-domain configuration.

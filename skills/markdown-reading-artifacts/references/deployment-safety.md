# Deployment Safety

Read this before publishing generated HTML.

1. Confirm the destination and the user's authorization to publish. Rendering and bundling alone do not grant deployment authority.
2. Inspect existing services, static sites, domains, and traffic routes that the proposed deployment could affect.
3. Prefer an isolated new static destination when the user has not specified an existing site to update.
4. Do not change unrelated applications, DNS, domain mappings, traffic splits, or load balancers without explicit authorization.
5. Verify the new URL and check any existing service URLs that the deployment could have affected.

Report the published URL, service or site name, project/region when applicable, and any changes to existing routing. Use the destination platform's current deployment procedure; the portal's generated Dockerfile is only an optional local artifact.

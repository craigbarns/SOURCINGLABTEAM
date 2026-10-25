# SEO audit follow-up — 25 October 2026

Based on `main` at `b110fab`, independently of the older
`codex/seo-geo-growth-2026-10-21` redesign branch. Changes are prepared for
review; production has not been updated by this follow-up.

Draft review: [GitHub PR #10](https://github.com/craigbarns/SOURCINGLABUSA/pull/10).
Final commit: `a932152e3714c38e3a97296e332a6d1b280c41e8`.
Working copy: `/Users/gregorybaranes/SOURCINGLABUSA-seo-audit`.

The final [GitHub quality check](https://github.com/craigbarns/SOURCINGLABUSA/actions/runs/40171341447)
passes, including the locked install, lint, TypeScript, tests, dependency audit
and production build. The final [Netlify deploy preview](https://deploy-preview-10--stunning-sundae-86a5b9.netlify.app)
is deployed successfully. The PR remains a draft and is not merged.

## Corrections

- Give the homepage process callout link an explicit dark text color. It sits
  on a white card inside a section with inherited light text. Contrast changes
  from 1.09:1 to 12.20:1.
- Replace the five supply-card `aria-label` overrides with native link text
  and a visually hidden product title. Accessible names now begin with the
  visible “View the page” / “Ver la página” text and retain the destination.
- Serve `/llms.txt` and `/llms-full.txt` as static, UTF-8 plain-text responses.
  Both take the promise from `src/lib/positioning.ts`; the extended overview
  also takes the scope, pillars, FAQ and guide directory from existing content.
  They describe the sourcing-only offer, the contracting company in France or
  China, and the limits written into the quotation.

## Production dependency corrections

The required GitHub security check found six vulnerable production package
entries already locked on `main`: one critical, three high and two moderate.
This was not detected by the supplied Lighthouse report. The corrected lockfile
now returns zero vulnerabilities from `npm audit --omit=dev`.

| Package | Before | After |
|---|---|---|
| Next.js and its ESLint configuration | 16.3.4 | 16.4.3 |
| Zod | 4.4.3 | 4.6.7 |
| Sharp | 0.35.4 | 0.35.5 |
| source-map-js | 1.2.1 | 1.2.2 |
| postcss-selector-parser used by Typography | 6.0.10 | 7.1.6 |

The Typography override is scoped to `@tailwindcss/typography`, whose current
release pins the older parser. Its actual parser calls were reviewed; all 281
generated Typography declarations are identical before and after the update.
The only changed declaration in the main stylesheet is the equivalent large
radius serialized for `.rounded-full` by the updated build toolchain.

Patched versions were checked against the published
[Next.js advisory](https://github.com/advisories/GHSA-673q-mjm6-r5xr),
[Zod advisory](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5),
[Sharp advisory](https://github.com/advisories/GHSA-wq5f-xc86-pv6w),
[source-map-js advisory](https://github.com/advisories/GHSA-68fv-2mgg-jv7q) and
[selector parser advisory](https://github.com/advisories/GHSA-rj75-hqrm-r3gf)
on 25 October 2026. These are dependency findings; no claim is made that the
site was compromised or that each affected feature was reachable.

## Validation

The existing 112 tests pass. ESLint, TypeScript and the production build pass.
The build reports existing `metadataBase` warnings; page canonicals and
absolute social URLs were not changed.

Lighthouse 13.5.0, mobile, against the final local production build using
Next.js 16.4.3:

| Page | Accessibility | SEO | Best practices | Agentic browsing |
|---|---:|---:|---:|---:|
| English homepage | 100 | 100 | 100 | 100 |
| Spanish homepage | 100 | 100 | 100 | Not requested |

The contrast audit passes on both pages. The label-content-name mismatch audit
has no failing elements; the conflicting ARIA overrides no longer exist.
The ten English/Spanish card names were also checked using the accessible-name
calculation, retaining both the visible label and the product title.

Both text endpoints return HTTP 200 and `text/plain; charset=utf-8`.
All 45 distinct canonical public URLs linked by the text files return HTTP 200
without a redirect; the linked FAQ fragment exists. Neither file links to the
private app, API, or retired market-entry URLs.

## Clarifications to the supplied audit

- The production sitemap already has 50 URLs and `lastmod` on all 15 blog
  articles. Adding those dates is unnecessary. No fabricated static-page
  modification dates were added. Google uses `lastmod` only when accurate and
  ignores `priority` and `changefreq` ([Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), checked 25 October 2026).
- `en-US`, `es-US`, `zh-Hans` and `x-default` are reciprocal in the compiled
  homepages. The Spanish content addresses U.S. customers, so `es-US` matches
  its audience; no new geographic target was introduced ([Google localized-page guidance](https://developers.google.com/search/docs/specialty/international/localized-versions), checked 25 October 2026).
- `llms.txt` is an optional content directory based on the
  [llms.txt proposal](https://llmstxt.org/), not evidence of rankings or AI
  citations. Google does not require special AI text files for AI Overviews
  or AI Mode ([Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features), checked 25 October 2026).
- The supplied JSON runs accessibility, SEO, best practices and agentic
  browsing. It contains neither a Performance category nor an LCP audit; the
  reported 241 ms LCP cannot be verified from that file.
- A live mobile CrUX history check returned insufficient Chrome traffic.
  This provides no field-data pass or fail for Core Web Vitals.

## Remaining evidence limits

The connected Search Console property `sc-domain:sourcinglabusa.com` is
discoverable, but the statistics query fails with Supermetrics
`LICENSE_NOT_FOUND`. The available Chrome session is not signed into Search
Console. No index-coverage or search-performance conclusion is drawn.

The backlink profile was not measured. Calling backlinks the leading growth
constraint would require evidence beyond this technical audit.

## Local review artifacts

The supplied report remains untouched in
`/Users/gregorybaranes/Documents/SOURCINGLABTEAM/seo-audit-reports/`.
The same folder contains `report-fixed-local-en.html`,
`report-fixed-local-en.json`, `report-fixed-local-es.html`,
`report-fixed-local-es.json`, and exports of both generated text files.
The before/after production dependency audits are saved as
`dependency-audit-before.json` and `dependency-audit-after.json`.

The Lighthouse results are local verification results, not a post-deployment
audit of the live site.

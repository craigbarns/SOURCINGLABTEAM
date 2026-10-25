# Intégration d'outils MCP aux agents SOURCING LAB — Plan validé

**Date :** 2026-10-25 · **Source :** liste 8 outils proposée par ChatGPT, évaluée contre le stack réel du projet

## Verdict global (table de décision)

| # | Outil | Verdict | Priorité | Pourquoi (basé sur les missions réelles) |
|---|---|---|---|---|
| 1 | **Firecrawl** | ✅ ADOPTER | P1 | Les extractions `curl + html2text` échouent sur les sites JS/Cloudflare (ex. ImportYeti bloqué, on.com). Firecrawl extrait aussi catalogues et fiches produits → gain direct supplier-hunter. API key requis. |
| 2 | **Hunter.io** | ✅ ADOPTER | P1 | Trou noir actuel : sur SKIMS on n'avait que `help@skims.com` (probabilité réponse faible). Hunter trouve + vérifie les emails pro (domaine vérifié, format `{first}@domaine`). Directement utile à lead-auditor + outreach-writer. API key requis, free tier 25 recherches/mo. |
| 3 | Mistral OCR | ⛔ SKIP | — | L'extension `pdfreader` déjà installée a lu parfaitement le PDF 20-F SEC d'On et suppliers-list.pdf (8 pages, tables). Redondant. |
| 4 | Google Workspace | 🟡 PLUS TARD | P3 | Gmail/Sheets utile pour `send_emails.py` et suivi prospects, mais OAuth + Google Cloud project = setup lourd. La règle playbook (jamais d'envoi sans validation humaine) doit être codée en dur dans le workflow avant de connecter un canal d'envoi. À faire après la mise en place des workflows. |
| 5 | Apify | ⛔ SKIP | — | Redondant avec Firecrawl à notre échelle (missions ciblées, pas du scraping de masse). ET : le playbook interdit le scraping LinkedIn — cas d'usage principal d'Apify hors limites. |
| 6 | Playwright | ✅ DÉJÀ INSTALLÉ | — | Extension `playwright` déjà active dans Goose. Preuve : mission On/ImportYeti du 2026-10-25 (recherche + extraction via navigateur). Rien à faire. |
| 7 | **Exa** | 🟡 TESTER | P2 | Recherche sémantique B2B > DDGS pour requêtes niche ("OEM seamless shapewear manufacturer Turkey"). Free credits à tester en parallèle de `ddgs`. Si measurably mieux → adopter. API key requis. |
| 8 | n8n | ⛔ DEFER | P4 | L'extension `scheduler` Goose couvre déjà les tâches récurrentes. n8n = passage serveur ; utile seulement si tu migres hors Mac. Revoir plus tard. |

**Bilan : 2 à adopter maintenant (Firecrawl, Hunter.io), 1 à tester (Exa), 1 déjà installé (Playwright), 3 à écarter/différer avec raisons.**

## Coûts estimés (à vérifier sur les sites, prix indicatifs 2026)

| Outil | Free tier | Payant d'entrée |
|---|---|---|
| Firecrawl | 500 crédits (~40 pages) | ~16 $/mois (Hobby) |
| Hunter.io | 25 recherches/mois + 50 vérifications | ~34 $/mois (Starter) |
| Exa | 10 $ de crédits | usage-based |

## Snippets MCP prêts à coller dans `~/.config/goose/config.yaml`

Format identique aux serveurs existants (fetch, playwright…). **Ne pas activer sans la clé API** — un serveur MCP sans clé valide ralentit/dégrade le démarrage de Goose.

```yaml
# --- Sous extensions: (à ajouter) ---
  firecrawl:
    enabled: false
    type: stdio
    cmd: npx
    args:
      - -y
      - firecrawl-mcp
    envs:
      FIRECRAWL_API_KEY: "<COLLER_CLE_ICI>"
    timeout: 300

  hunter:
    enabled: false
    type: stdio
    cmd: npx
    args:
      - -y
      - "@mcp/hunter-io-mcp"   # vérifier le nom exact du package MCP Hunter
    envs:
      HUNTER_API_KEY: "<COLLER_CLE_ICI>"
    timeout: 300

  exa:
    enabled: false
    type: stdio
    cmd: npx
    args:
      - -y
      - exa-mcp-server
    envs:
      EXA_API_KEY: "<COLLER_CLE_ICI>"
    timeout: 300
```

Passer `enabled: true` après insertion de la clé. Vérifier les noms exacts de packages : firecrawl-mcp-server (github.com/firecrawl/firecrawl-mcp-server), exa-mcp-server (github.com/exa-labs/exa-mcp-server), MCP Hunter (hunter.io/mcp).

## Checklist d'installation (Gregory)

1. [x] Clé Hunter.io fournie et validée (plan Free 50 crédits/mois) — 2026-10-25
2. [x] Clé Firecrawl fournie et validée (test scrape example.com OK) — 2026-10-25
3. [x] Config écrite dans `~/.config/goose/config.yaml` (hors repo) :
   - `hunter` : type `streamable_http`, `uri: https://mcp.hunter.io/mcp`, header `X-API-Key` (format vérifié dans le code source Goose `crates/goose/src/agents/extension.rs` — variant StreamableHttp avec champs uri/headers/timeout)
   - `firecrawl` : type `stdio`, `npx -y firecrawl-mcp` (package npm officiel), env `FIRECRAWL_API_KEY`
   - YAML validé par parse (26 extensions, hunter + firecrawl actifs)
4. [ ] **RESTART GOOSE requis** (action Gregory : quitter et relancer l'app / nouvelle session) — les outils n'apparaissent pas dans la session courante
5. [ ] Après restart : mission supplier-hunter de test (comparer temps / sources / qualité contacts vs baseline du 2026-10-25)

### Config finale installée (clés masquées)

```yaml
  hunter:
    enabled: true
    type: streamable_http
    uri: https://mcp.hunter.io/mcp
    headers:
      X-API-Key: "<CLÉ_HUNTER>"     # réel dans ~/.config/goose/config.yaml
    timeout: 300

  firecrawl:
    enabled: true
    type: stdio
    cmd: npx
    args: [-y, firecrawl-mcp]
    envs:
      FIRECRAWL_API_KEY: "<CLÉ_FIRECRAWL>"  # réel dans ~/.config/goose/config.yaml
    timeout: 300
```

## Impact par agent (mis à jour dans .agents/agents/*.md)

| Agent | Avant | Après |
|---|---|---|
| supplier-hunter | curl+html2text, échoue sur JS/Cloudflare | + Firecrawl (scrape JS, catalogues), + Exa (recherche B2B) |
| lead-auditor | contacts limités aux emails publics | + Hunter.io (emails vérifiés domaines + formats), critère "Contact vérifiable" renforcé |
| outreach-writer | placeholders ou emails génériques | emails Hunter vérifiés → taux de rebond réduit |
| supplier-auditor / rfq-analyst | inchangés (pdfreader suffit) | — |

## Règle de sécurité ajoutée au playbook

- Hunter.io et Firecrawl ne collectent que des données **publiquement exposées** — conforme au playbook. Interdiction maintenue : pas de scraping LinkedIn, pas d'emails privés non publiés.
- Toute clé API vit dans `~/.config/goose/config.yaml` ou variables d'env — **jamais** dans les livrables, CSV ou repo git.

# Audit complet — www.theklope.com

**Date :** 2026-10-25 · **Auditeur :** goose (orchestrateur) · **Cible :** boutique vape Marseille (188 rue de Rome, 13006) + e-commerce France métropolitaine · **Pile :** SPA React/Vite sur Vercel, checkout Mollie, catalogue ~532 produits
**Conformité mission :** lecture seule — aucune modification du site, aucun déploiement. Journal de traçabilité : `logs/mission-theklope.json`.

---

## 1. Méthode, agents mobilisés, erreurs

| Tâche | Agent mobilisé | Résultat | Erreurs / limites |
|---|---|---|---|
| SEO technique & performance | Subagent ad-hoc `20261025_10` (skill seo-audit côté orchestrateur) | Sitemap 647 URLs, canonicals, JSON-LD, images | API PageSpeed Insights en échec (quota 429 keyless) → **performance non mesurée, aucune donnée inventée** |
| CRO / UX | Subagent ad-hoc `20261025_9` (skill cro côté orchestrateur) | 15 constats qualifiés VÉRIFIÉ/HYPOTHÈSE | Checkout client-side non auditable en HTML brut → resté HYPOTHÈSE |
| Analyse concurrentielle | Subagent ad-hoc `20261025_11` | Comparatif 5 acteurs, preuves curl | lepetitvapoteur.com bloqué (403 Cloudflare) → non vérifié ; "avasvape" = domaine inexistant (NXDOMAIN) → remplacé par concurrents locaux CE-STORE et STOR e-cig |
| Visibilité IA (GEO) | Orchestrateur (skill ai-seo chargé, pas d'agent dédié summon) | Audit llms.txt, robots IA, extractabilité | Pas de sous-agent "GEO" disponible : fait par l'orchestrateur, sans prétendre à une délégation |
| Collecte de données | Orchestrateur (curl, 15+ pages, sitemap, robots, llms-full.txt 1 Mo) | Base de preuves commune | — |

> Transparence : aucun sous-agent spécialisé SEO/CRO/GEO n'existe dans la flotte summon (orientée sourcing/leads). Les délégations ont été des subagents ad-hoc ; les compétences spécialisées proviennent des skills chargés dans le contexte de l'orchestrateur.

**Arbitrage inter-agents (contradiction résolue) :** l'agent concurrentiel rapportait un JSON-LD `LocalBusiness` complet sur la homepage ; la vérification directe de l'orchestrateur sur le HTML SSR statique montre **0 bloc JSON-LD** sur la homepage et 1 sur la page locale. Statut ajusté : JSON-LD présent sur certaines pages, **incohérent/absent du SSR homepage** (voir F1).

---

## 2. Synthèse exécutive

**Points forts vérifiés** — socle technique au-dessus du marché local : sitemap complet avec 532 pages produit, canonicals auto-référencés, HTTPS/HSTS, redirections propres, 404 réels, robots.txt autorisant explicitement les crawlers IA, `llms.txt` + `llms-full.txt` (1,06 Mo) très bien construits, image LCP optimisée (WebP, dimensions, fetchpriority), image LCP, seuil de franco à 29 €, différenciation locale forte (retrait boutique + coursier le jour même).

**Freins majeurs aux ventes (vérifiés)** — le SSR ne sert que des coquilles : pages produit sans prix/CTA d'achat/stock en HTML serveur, homepage sans avis clients ni argument "livraison offerte dès 29 €" visible, boutique de 800 Ko sans un seul prix rendu. Google, les crawlers IA et les lents/mobiles voient un site vide ; les humains rapides voient un site lent à s'afficher.

**Opportunité Google/GEO n°1** — le JSON-LD produit n'existe pas en SSR et les pages /guides sont quasi vides en HTML alors que le concurrent local CE-STORE publie 12 articles en 2026. C'est le principal écart rattrapable.

---

## 3. Constats détaillés (statuts VÉRIFIÉ / HYPOTHÈSE)

### SEO technique
| # | Constat | Preuve | Statut | Impact |
|---|---|---|---|---|
| T1 | Sitemap : 647 URLs dont 532 produits, 48 catégories, 38 guides | curl sitemap.xml | VÉRIFIÉ | ✅ Positif |
| T2 | `lastmod` = date du jour sur les 647 URLs → signal de fraîcheur non crédible | sitemap.xml | VÉRIFIÉ | Moyen |
| T3 | **JSON-LD absent du SSR** sur homepage + 2 produits + catégories testés ; injection `application/ld+json` uniquement client-side (confirmé dans bundle index-DBTe7CSe.js) | grep HTML + bundle | VÉRIFIÉ | **Haut** |
| T4 | Pages produit : SSR squelettique (~8 Ko, 120–135 mots), description complète absente du HTML serveur | /produit/aegis-solo-3… | VÉRIFIÉ | **Haut** |
| T5 | 1 meta description avec guillemet orphelin (desc tronquée) | /produit/anis-51-50ml | VÉRIFIÉ | Bas |
| T6 | /categorie/pods : SSR mince (493 mots) vs /categorie/e-liquides riche (3 223 mots) | curl | VÉRIFIÉ | Moyen |
| T7 | Titles pages locales complets (la troncature suspectée initialement n'est pas confirmée) ; 71–78 caractères, troncature SERP possible | curl | VÉRIFIÉ | Bas |
| T8 | Performance (LCP/TBT/CLS) **non mesurée** : quota PSI épuisé. La page est une SPA lourde (bundle + Supabase) → risque CWV élevé mais non prouvé | logs API | HYPOTHÈSE à mesurer | Potentiel Haut |
| T9 | Pages /guides : index sans liens SSR ; article type = 6,8 Ko seulement | curl /guides/* | VÉRIFIÉ | Moyen |

### Visibilité IA (GEO)
| # | Constat | Preuve | Statut | Impact |
|---|---|---|---|---|
| G1 | `llms.txt` riche : faits vérifiables, horaires, RCS, FAQ, liens pages ; `llms-full.txt` catalogue 1,06 Mo | curl 200 | VÉRIFIÉ | ✅ **Avantage net vs concurrents (tous sans llms.txt)** |
| G2 | robots.txt : GPTBot, ClaudeBot, PerplexityBot, Applebot-Extended autorisés explicitement | robots.txt | VÉRIFIÉ | ✅ Positif |
| G3 | Aucun prix/stock/avis lisible sans JS sur 532 pages produit → les agents IA acheteurs ne peuvent pas comparer THEKLOPE | HTML produits | VÉRIFIÉ | **Haut** |
| G4 | FAQ du llms.txt excellente mais la page /faq elle-même ne sert que 240 caractères en SSR | curl | VÉRIFIÉ | Moyen |
| G5 | Téléphone `+33 4 91 55 55 55` dans llms.txt — plausible mais atypique ; à confirmer par le client | llms.txt | HYPOTHÈSE (à valider humain) | Moyen si faux |
| G6 | Pas de `/pricing.md` (404) — mineur pour du e-commerce, la donnée produit existe déjà dans llms-full | curl | VÉRIFIÉ | Bas |

### CRO / UX
| # | Constat | Preuve | Statut | Impact |
|---|---|---|---|---|
| C1 | CTA primaire unique et générique ("Découvrir la boutique"), 0 "Ajouter/Acheter/Commander" dans la homepage SSR | home.html | VÉRIFIÉ | **Haut** |
| C2 | **Zéro preuve sociale** sur la homepage (pas d'avis, note, logos) | home.html | VÉRIFIÉ | **Haut** |
| C3 | "Livraison offerte dès 29 €" absente du contenu visible (uniquement dans meta + section engagements basse) | home.html | VÉRIFIÉ | **Haut** |
| C4 | Header/footer non rendus en SSR : panier, nav, FAQ invisibles au premier paint | home.html | VÉRIFIÉ | **Haut** |
| C5 | Page produit sans bouton d'achat, sans sélection variantes, sans stock en SSR | produit.html | VÉRIFIÉ | **Haut** |
| C6 | /boutique : 800 Ko de HTML, ~100+ noms de produits, **0 prix, 0 badge** alors que stock/best-seller existent dans les données | boutique.html | VÉRIFIÉ | **Haut** |
| C7 | USP locale (retrait 188 rue de Rome + coursier jour même) absente de la homepage visible ; bien exploitée sur /cigarette-electronique-marseille | home.html vs page locale | VÉRIFIÉ | **Haut** |
| C8 | Confiance paiement : "Mollie" en texte seul, pas de logos moyens de paiement ni 3x/4x ni garantie près des CTA | home.html | VÉRIFIÉ | Moyen |
| C9 | Hero = énumération catalogue sans bénéfice client ; pas d'entrée "Je débute" | home.html | VÉRIFIÉ | Moyen |
| C10 | Horaires d'ouverture absents du body ; JSON-LD = Lun–Ven seulement (samedi fermé ? incohérence possible avec la pratique d'une boutique de centre-ville) | home.html | Absence VÉRIFIÉE / erreur samedi HYPOTHÈSE | Moyen |
| C11 | Stocks et badges ("Plus que 2", best-seller) disponibles en base mais non rendus | boutique.html JS | VÉRIFIÉ (données) | Moyen |
| C12 | Checkout (nb d'étapes, friction Mollie) non auditable sans navigateur | — | HYPOTHÈSE à tester | À mesurer |

### Concurrentiel (comparatif vérifiable)
| Critère | THEKLOPE | CE-STORE (Marseille) | STOR e-cig (Marseille) | Le Petit Vapoteur |
|---|---|---|---|---|
| Site actif (200) | ✅ | ✅ | ✅ | ✅ (403 anti-bot, contenu NON VÉRIFIÉ) |
| JSON-LD LocalBusiness | ✅ sur pages locales (SSR incohérent) | ❌ 0 | ⚠️ WebSite seul | ? |
| llms.txt | ✅ | ❌ 404 | ❌ 404 | ❌ 404 |
| Crawlers IA autorisés | ✅ explicites | ⚠️ standard | ⚠️ standard | ⚠️ standard Prestashop |
| Franco de port affiché | ✅ 29 € | ❌ non affiché | ❌ payant (2–9 €) | ? |
| Blog/guides actifs | ⚠️ SSR quasi vide | ✅ **12 articles en 2026** | ❌ | ? |
| Avis visibles dans HTML | ❌ | ❌ | ❌ | ? |
| Pages locales dédiées | ✅ (marseille, salon-de-provence, puff…) | ✅ par quartiers | ⚠️ | — |

**5 écarts majeurs :** (1) THEKLOPE seul sur la couche GEO/IA — avantage à capitaliser vite ; (2) données structurées locales supérieures (à fiabiliser en SSR) ; (3) avantage logistique 29 € mal exploité sur la homepage ; (4) **content gap : CE-STORE écrase le terrain /guides** ; (5) preuve sociale absente chez tous les locaux → gain rapide pour le premier qui l'ajoute.

---

## 4. Tableau de couverture

| Domaine | Couverture | Note |
|---|---|---|
| SEO technique | Établi | 15+ pages fetchées, sitemap, robots, canonicals, bundle JS |
| Visibilité IA | Établi | llms.txt/full, robots IA, extractabilité produits |
| CRO/UX | Partiel | HTML brut uniquement ; checkout et mobile réel non testés (navigateur requis) |
| Performance | Inconnu | PSI quota épuisé ; à relancer (Clé API gratuite ou Search Console CWV) |
| Concurrentiel | Partiel | 3/4 concurrents vérifiés ; Le Petit Vapoteur bloqué 403 |
| Indexation réelle (GSC) | Inconnu | Accès Search Console requis (clics, couverture, CWV) |

## 5. Sources
- HTML SSR : theklope.com (/, /boutique, /categorie/*, /produit/*, /guides/*, /faq, /contact, pages locales) — fetch 2026-10-25
- theklope.com/robots.txt, /sitemap.xml, /llms.txt, /llms-full.txt — 2026-10-25
- Bundle /assets/index-DBTe7CSe.js (preuve injection JSON-LD client) — 2026-10-25
- ce-store.fr, stor e-cig (Marseille), lepetitvapoteur.com — 2026-10-25
- API PSI : échec quota (2 essais, mobile+desktop) — 2026-10-25

---

## 6. Les 15 améliorations (classées par impact commercial × effort × priorité)

Légende : Impact commercial (H/M/B) · Effort (S/M/L) · P1 = immédiat, P2 = 30 j, P3 = trimestre. Statut du constat entre parenthèses.

| # | Amélioration | Impact | Effort | Prio |
|---|---|---|---|---|
| 1 | **Rendre le JSON-LD en SSR** (Product + Offer prix/stock + BreadcrumbList + AggregateRating) sur les 532 pages produit — aujourd'hui injecté client uniquement (T3, C5) | H | M | **P1** |
| 2 | **Enrichir le SSR des pages produit** : prix, disponibilité, bouton "Ajouter au panier", variantes dans le HTML serveur (T4, C5, C6, G3) | H | M | **P1** |
| 3 | **Ajouter la preuve sociale** : avis clients (note + nombre) sur homepage et fiches produit ; badges moyens de paiement (C2, C8) — champ libre chez tous les concurrents locaux | H | S | **P1** |
| 4 | **Remonter l'USP logique en hero** : "Livraison offerte dès 29 €", "Coursier le jour même à Marseille", "Retrait boutique 1 h" dès le premier écran (C3, C7) | H | S | **P1** |
| 5 | **SSR complet header/footer + panier visible au premier paint** (C4) — résout aussi CRO, SEO et IA d'un coup | H | M | **P1** |
| 6 | **Rempir /guides en SSR** : l'index et les 38 articles doivent livrer leur contenu en HTML ; rattraper le retard vs CE-STORE (12 articles 2026) (T9, écart 4) | H | M | **P1** |
| 7 | **CTA primaire actionnable** homepage : remplacer "Découvrir la boutique" par un CTA d'intention d'achat + CTA répétés (C1) | H | S | **P1** |
| 8 | **Rendre prix + badges stock/best-seller dans le SSR de /boutique** et ajouter filtres ; alléger les 800 Ko (C6, C11) | H | M | P2 |
| 9 | **Mesurer la performance** : PSI/Search Console CWV sur mobile ; si LCP > 2,5 s, prérendu des pages clés (T8) — prérequis : clé API | H (?) | S (mesure) | P2 |
| 10 | **Entrée "Je débute"** sur la homepage : parcours packs débutants + guides taux de nicotine (C9, C15) | M | S | P2 |
| 11 | **Harmoniser les horaires** : body, JSON-LD, Google Business Profile, llms.txt — valider samedi par un humain (C10, G5) | M | S | P2 |
| 12 | **Enrichir le SSR de /categorie/pods** + ItemList JSON-LD sur les 48 catégories (T6) | M | M | P2 |
| 13 | **lastmod réels** dans le sitemap (depuis les vraies dates de modif produit) (T2) | M | S | P2 |
| 14 | **Audit tunnel checkout** en navigation réelle (étapes, friction Mollie, frais affichés tôt) (C12) | M–H | M (test) | P2 |
| 15 | **Corrections fines** : meta desc guillemet orphelin (T5), titles locaux ≤ 65 car. (T7), envisager `LocalBusiness` + FAQPage en SSR sur /faq (G4) | B–M | S | P3 |

**Conformité :** aucune recommandation de promo agressive ni allégation santé (réglementation vape FR). Le socle "+18, réservé aux adultes" existant est à conserver.

---

## 7. Prochaines étapes (aucune action sur le site sans validation)
1. **Validation humaine** : horaires samedi (C10), téléphone llms.txt (G5), accès Search Console + clé API PSI pour lever T8/GSC.
2. Si validé : lancer les P1 (items 1–7) — la plupart sont des changements de rendu SSR, pas de refonte.
3. Test CRO A/B sur le hero (item 4) avant généralisation.

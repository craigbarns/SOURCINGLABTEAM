# Inventaire & Vérification des capacités — 2026-10-25 07:15 (+01:00)

## 1. Sous-agents (testés via load, invocables via delegate)
| Agent | Statut | Preuve |
|---|---|---|
| sourcing-manager | Invocable | Contenu chargé, workflow T1→T4 vérifié |
| supplier-hunter | Invocable | Recipe référence + mission passée (HIVIC) |
| supplier-auditor | Invocable | Test suite : coherence-scores PASS |
| rfq-analyst | Invocable | Recipe analyse-cotations |
| us-lead-hunter / v2 | Invocable | Missions USA-LEADS 20261024 (logs) |
| Recipes ×5 | Invocables | recipes/*.yaml (320 lignes) |

## 2. Skills (13, méthodologie — non exécutables directement)
supplier-qualification, sourcing-research-procedures, rfq-analysis, rfq-generator, prospecting, cold-email, seo-audit, ai-seo, competitor-profiling, cro, web-search, find-skills, goose-doc-guide.
Chargé dans ce contexte : sourcing-research-procedures (procédures SEARCH/VERIFY/COMPARE).

## 3. Outils / extensions — tests réels
| Outil | Test | Résultat |
|---|---|---|
| shell + python3 | exécution datée | ✅ OK 07:12:30 |
| web-search (ddgs) | requête "bucket manufacturer" | ✅ OK (résultats réels) |
| computercontroller | `permissions status` | ⚠️ Screen Recording OK ; **Accessibility NON accordée** → UI automation (click/type) indisponible jusqu'à autorisation Système > Confidentialité > Accessibilité |
| autovisualiser | list_resources | ✅ 8 types de graphiques disponibles |
| memory | retrieve | ✅ Standards agent (7 principes) chargés |
| suite tests interne | tests/test-suite-metrics.py | ✅ 6/6 PASS — verdict « système fiable » (exactitude 100%, doublons 0, coût $0.01) |
| apps | list | ✅ 1 app (clock) |

## 4. État du répertoire
- data/, deliverables/, logs/ (7 missions journalisées), playbook/, recipes/, reports/, tests/
- Standard agent actif en mémoire globale (traçabilité, sourçage URL+date, statuts Vérifié/Déclaré/Non vérifié/Contradictoire, record-and-continue, auto-validation, couverture, zéro contact sans autorisation).

## 5. Anomalies connues / limitations
- ImportYeti, RocketReach, pages LinkedIn dynamiques : bloqués (Cloudflare/CAPTCHA) → contournement par DDG/curl documenté dans journaux.
- DDG renvoie parfois "No results" selon formulation → reformulation requise (déjà loggé le 2026-10-24).
- Accessibility macOS non accordée : navigation UI réelle (clics/saisies) impossible pour l'instant ; navigation via curl/ddgs reste opérationnelle pour les missions web.

## 6. Règles d'engagement (confirmées)
- Aucune donnée de prospect fabriquée ; distinction documenté / déclaré / supposé.
- Aucune publication ni envoi commercial sans autorisation explicite.
- Journal de mission horodaté + tableau de couverture (établi/partiel/inconnu) dans chaque rapport final.
- Échec de délégation → signalé + alternative proposée (relance 1×, puis exécution directe documentée).

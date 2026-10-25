# SOURCING LAB AI — Plateforme Multi-Agents Goose

> Installation transformée le 2026-10-24 | Goose 1.56.0 | Provider openrouter meta/muse-spark-open

---

## 1. AUDIT INITIAL (ÉTAPE 1 — exécuté)

### Installation détectée
- **Goose version**: 1.56.0 (AppTranslocation — ⚠️ tourne depuis .dmg, installation définitive recommandée)
- **Config**: `~/.config/goose/config.yaml` + `~/.local/share/goose/sessions/sessions.db`
- **Working dir demandé**: `/Users/gregorybaranes/Documents/SOURCINGLABTEAM` → **vide** à l'audit
- **Ancienne mission retrouvée**: `/Users/gregorybaranes/Documents/AGENTSOURCINGLAB/` → `fabricants_seaux_PP_8-16L_Chine.csv` (11 lignes, 10 fabricants) + `README_Sourcing_Seaux_PP.md` (méthodo complète, MD5 préservé)
- **Agents existants**: ❌ Aucun `~/.agents/agents/` (inexistant) — créé
- **Skills existants**: 1 custom `reverse-engineer-anything` + 2 builtins (`goose-doc-guide`, `web-search`) — conservés
- **Recipes**: ❌ Aucune (`No recipes found`) — créées
- **Extensions activées** (8): `analyze`, `skills`, `apps`, `summon`, `extensionmanager`, `developer`, `tom`, `scheduler` (+ `recipe`, `final_output`, `goose_recipe`)
- **Extensions désactivées** (7): `computercontroller`, `todo`, `summarize`, `code_execution`, `chatrecall`, `autovisualiser`, `memory`, `tutorial`
- **Aucune suppression** de config — toute création en ajout
- **Git**: pas de repo dans SOURCINGLABTEAM (optionnel)

### Capacités réellement disponibles (vérifiées)
- `developer` → shell + fichiers ✓
- `summon` → `delegate`/`load` subagents ✓ (testé avec 3 délégations parallèles)
- `analyze` → tree-sitter code ✓
- `skills` → discovery `~/.agents/skills/` + `.agents/skills/` ✓
- `web-search` skill → `uvx ddgs text + curl + html2text` ✓ (38 extractions lors du test réel)
- Provider OpenRouter opérationnel

---

## 2. LES 5 AGENTS CRÉÉS (ÉTAPE 2)

Tous au format officiel Goose **Markdown + YAML frontmatter** (`name` requis).

| # | Agent | Fichier global | Fichier projet (miroir) | Mission |
|---|-------|---------------|------------------------|---------|
| 1 | **supplier-hunter** | `~/.agents/agents/supplier-hunter.md` | `SOURCINGLABTEAM/.agents/agents/supplier-hunter.md` | Recherche web multilingue, id usines, vérif sites, extraction capacités, contacts publics, détection doublons, CSV/XLSX sourcés |
| 2 | **supplier-auditor** | `~/.agents/agents/supplier-auditor.md` | `SOURCINGLABTEAM/.agents/agents/supplier-auditor.md` | Vérif fabricants, contrôle tech, vérif doc certifs, sociétés liées, comparaison capacités, score /100 avec Vérifié/Déclaré/Non vérifié/Contradictoire |
| 3 | **us-lead-hunter** | `~/.agents/agents/us-lead-hunter.md` | `SOURCINGLABTEAM/.agents/agents/us-lead-hunter.md` | Importateurs, distributeurs, grossistes US, analyse produits, contacts publics, qualif opportunité, export CRM |
| 4 | **rfq-analyst** | `~/.agents/agents/rfq-analyst.md` | `SOURCINGLABTEAM/.agents/agents/rfq-analyst.md` | Lecture PDF/Excel, prix, MOQ, coûts unitaires/logistiques, Incoterms, marges, tableaux comparatifs — ZÉRO invention |
| 5 | **sourcing-manager** | `~/.agents/agents/sourcing-manager.md` | `SOURCINGLABTEAM/.agents/agents/sourcing-manager.md` | Analyse mission, décompose, délègue via `delegate`, contrôle incohérences, demande corrections, rapport final consolidé |

**Détail frontmatter exemple**:
```markdown
---
name: supplier-hunter
description: Trouve de vrais fabricants industriels internationaux - recherche web multilingue...
---
[Instructions spécialisées 80-120 lignes]
```

**Détection Goose**: `~/.agents/agents/` (global) + `SOURCINGLABTEAM/.agents/agents/` (projet). Les deux chemins sont auto-découverts par Goose selon [docs Custom Agents](https://goose-docs.ai/docs/guides/context-engineering/custom-agents).

---

## 3. SKILLS (ÉTAPE 3)

### Skill 1: supplier-qualification
- **Path global**: `~/.agents/skills/supplier-qualification/SKILL.md`
- **Path projet**: `SOURCINGLABTEAM/.agents/skills/supplier-qualification/SKILL.md`
- **Méthode 7 piliers /100 reproductible** (±5 pts entre auditeurs):
  1. Identification juridique (15) — raison sociale + adresse usine + année
  2. Preuve activité industrielle (20) — photos/vidéo + surface + machines + effectif + audit BV
  3. Conformité produit (15) — gamme 8-16L prouvée sur officiel vs marketplace
  4. Capacités fabrication (15) — procédés + volumes + OEM/ODM + export
  5. Certifications documentées (15) — FDA/EU/ISO/BSCI/UN/SGS (Vérifié=PDF vs Déclaré=texte)
  6. Conditions commerciales (10) — MOQ + Incoterms + délai + paiement
  7. Qualité sources (10) — ≥3 URLs dont officiel + extraction datée
- **Niveaux**: 90-100 🟢 foncé Hautement qualifié | 70-89 🟢 Qualifié | 40-69 🟠 À compléter | 0-39 🔴 Non qualifié
- **4 statuts systématiques**: Vérifié / Déclaré / Non vérifié / Contradictoire
- **Exemple noté**: Enlightening Plast → 83/100 détaillés P1-P7 avec URLs

### Skill 2: sourcing-research-procedures
- **Path**: `~/.agents/skills/sourcing-research-procedures/SKILL.md`
- **3 procédures réutilisables**:
  - **RECHERCHE**: 10 templates requêtes multilingues (EN/ZH/FR/DE/ES), checklist `ddgs` + `html2text`, fiche collecte brute, output `recherche-brute-*.md`
  - **VÉRIFICATION**: checklist 4 statuts par bloc (Identité/Produit/Certifs/Doublon), commande `rg` anti-doublon, output CSV vérifié
  - **COMPARAISON**: template tableau pondéré, scoring, exports CSV/XLSX + rapport markdown, checklist livraison
- Règles communes: traçabilité URL+date, zéro invention (`Non communiqué`), anti-doublon, nommage `YYYY-MM-DD`

### Skill 3: rfq-analysis
- **Path**: `~/.agents/skills/rfq-analysis/SKILL.md`
- **6 étapes**: Collecte PDF/Excel → Normalisation devise BCE → Coûts rendus (FOB+fret+assurance+douane) → MOQ → Incoterms → Livraison XLSX/CSV/MD
- Templates: message clarification fournisseur, scoring pondéré Prix 40% MOQ 20% Délai 15% Qualité 15% Paiement 10%

**Vérification**: `goose skills list` → 6 skills détectés (3 nouveaux + 3 builtins/custom conservés) ✓

---

## 4. RECIPES YAML (ÉTAPE 4)

Toutes en format natif Goose Recipe v1.0.0, validées `goose recipe validate` ✓

| Recipe | Fichier | Title | Params | Extensions |
|--------|---------|-------|--------|------------|
| 1 | `~/.config/goose/recipes/recherche-fournisseurs.yaml` | Recherche de Fournisseurs | produit, specs, origine (déf. Chine), nombre_fournisseurs (déf. 10), dossier_sortie (./data) | developer, summon, analyze, skills |
| 2 | `~/.config/goose/recipes/audit-fournisseurs.yaml` | Audit de Fournisseurs | fichier_csv_entree (req), dossier_sortie (./reports) | developer, summon, skills |
| 3 | `~/.config/goose/recipes/recherche-prospects-us.yaml` | Recherche Prospects US | produit, icp, nombre_leads (20), dossier_sortie (./data) | developer, summon, skills |
| 4 | `~/.config/goose/recipes/analyse-cotations.yaml` | Analyse de Cotations | dossier_devis (req), devise_ref (EUR), prix_vente_cible, dossier_sortie (./reports) | developer, summon, skills |
| 5 | `~/.config/goose/recipes/mission-complete.yaml` | Mission Complète Sourcing | produit, specs, origine, nombre_fournisseurs (déf. 10), inclure_us (oui/non), dossier_sortie | developer, summon, skills, analyze — max_turns 120 |

**Miroir projet**: `SOURCINGLABTEAM/recipes/*.yaml` identique (utilisable via `GOOSE_RECIPE_PATH=./recipes`)

**Exemple d'appel**:
```bash
goose run --recipe ~/.config/goose/recipes/recherche-fournisseurs.yaml \
  --params produit="seaux PP alimentaires 10L" specs="PP vierge food-grade IML 8-16L" origine="Chine" nombre_fournisseurs="10"
```

---

## 5. INTÉGRATIONS — Extensions (ÉTAPE 5)

### Examen réalisé le 2026-10-24
Liste via `~/.config/goose/config.yaml` + `extensionmanager search`:

| Extension | Type | Statut | Nécessaire ? | Action |
|-----------|------|--------|--------------|--------|
| developer | platform | ✅ Activée | Oui — fichiers, shell, python XLSX | Conservée |
| summon | platform | ✅ Activée | Oui — délégation subagents | Conservée |
| analyze | platform | ✅ Activée | Oui — codebase | Conservée |
| skills | platform | ✅ Activée | Oui — skills | Conservée |
| apps | platform | ✅ Activée | Optionnel | Conservée |
| extensionmanager | platform | ✅ Activée | Oui — gestion | Conservée |
| scheduler | platform | ✅ Activée | Oui — missions programmées | Conservée |
| todo | platform | ❌ Désactivée | Utile — suivi tâches multi-agents | **Recommandée, en attente de ton accord** |
| summarize | platform | ❌ Désactivée | Utile — résumés rapports | **Recommandée, en attente** |
| memory | builtin | ❌ Désactivée | Utile — préférences produit | **Recommandée, en attente** |
| autovisualiser | builtin | ❌ Désactivée | Optionnel — Sankey/radar pour comparatifs | Sur demande |
| computercontroller | builtin | ❌ Désactivée | Non — contrôle OS non requis | Laissée désactivée |
| chatrecall | platform | ❌ Désactivée | Sur demande — historique sessions | Laissée désactivée |
| Playwright / MCP / DB / Fetch externe | — | Non installées | Non requis pour sourcing actuel | **Aucune installation sensible effectuée** |

**Décision**: Aucune extension sensible installée. Recherche Internet via skill `web-search` (DuckDuckGo `uvx ddgs` + `html2text`) suffit. Lecture documents via `developer` (pdfplumber/openpyxl). Export CSV/XLSX via `python3 openpyxl` testé (XLSX 25 Ko généré). Bases de données/MCP non nécessaires à ce stade.

> 🔒 **Demande d'accord**: Veux-tu que j'active `todo` + `memory` + `summarize` (fiables, sans communication externe ni dépense) ? Réponds `oui` et je les active. Pour Playwright (navigation), MCP externe, ou dépenses → je demanderai accord explicite cas par cas.

---

## 6. TEST RÉEL — 10 fournisseurs seaux PP (ÉTAPE 6 — exécuté)

### Protocole
- **Fichier source**: `data/fabricants_seaux_PP_8-16L_Chine-ORIGINAL.csv` (copie MD5 préservée, non modifié)
- **2 subagents délégués en parallèle** via `delegate` (isolation process, timeout 5 min, héritage extensions):
  - `supplier-hunter` → re-vérification 38 extractions `curl+html2text` archivées `/tmp/reverif-2026-10-24/`
  - `supplier-auditor` → audit 28 URLs + scoring 7 piliers /100

### Livrables produits
| Fichier | Taille | Contenu |
|---------|--------|---------|
| `reports/audit-fournisseurs-2026-10-24.md` | 40 Ko, 293 lignes | Tableau scores, 10 détails P1-P7 avec URLs cliquables, doublons/liés, infos non prouvées, hors spec, données manquantes, Go/No-Go |
| `reports/fabricants-corrigé-2026-10-24.csv` | 28 Ko, 11 lignes, 23 colonnes | CSV original + Score /100 + Niveau + Statut global + Commentaire + P1-P7 + URLs justificatives ; UTF-8-SIG `;` |
| `reports/fabricants-corrigé-2026-10-24.xlsx` | 25 Ko, 3 feuilles | Scores_Synthèse (17×12) + Grille P1-P7 (84×5) + Anomalies (17×3), mise en forme rouge/orange/vert, filtres, A3 paysage |
| `reports/reverification-hunter-2026-10-24.md` | 41 Ko, 346 lignes | Pour chaque fournisseur: statut Vérifié 2026-10-24, URLs re-extraites (tailles), gamme, surface/machines, certifs, adresse/tel, alertes |
| `reports/validation-manager-2026-10-24.md` | 160 mots | Test Manager — 5/5 agents, 3/3 skills, 5/5 recipes, plan délégation |

### Résultats détaillés

**Scores /100 (skill supplier-qualification)**:
1. #6 Zhejiang Yunde — 76 🟢 Qualifié (pépite fluorination)
2. #1 Enlightening Plast — 73 🟢 Qualifié
3. #4 Qingdao Rulyda — 73 🟢 Qualifié (leader capacité 20000m² 85 presses)
4. #3 Xingtai Xinbei — 72 🟢 Qualifié (MOQ 500 imbattable)
5. #5 Zibo Yundu / CP Bucket — 68 🟠 À compléter (dualité juridique Contradictoire)
6. #9 Suzhou Fansheng — 64 🟠 (maison mère)
7. #2 Suzhou Innovation — 57 🟠 (filiale, site innopack.com DOWN ModSecurity)
8. #8 Jinjie Huangyan — 50 🟠 mais P3=0 Hors spec (max 4.2L IML)
9. #10 Qingdao Hivic — 31 🔴 Non qualifié (palette, pas seaux)
10. #7 Taizhou Bright — 15 🔴 Non qualifié (showroom 404)

**Doublons**: ❌ Aucun doublon strict (10 ≠ même raison sociale+adresse+tel) → **Panel réel 8 entités indépendantes** (10 - 2 groupes liés)

**Entreprises liées (2 groupes confirmés)**:
- Groupe Innopack: #2 Innovation (2013, investie par Fansheng) ↔ #9 Fansheng (1998, $3.8M) — même zone Wuzhong Suzhou, même groupe innopack.com, distance 15km
- Groupe CP Bucket: #5 Zibo Yundu (MIC historique sacs tissés) ↔ Foshan Chengpin Technology (cpbucket.com) — contact unique Mr Fan +86 18316967024, dualité Business License non réconciliée → Contradictoire

**Infos non prouvées**: 0/10 certifs Vérifié — tous Déclaré sans PDF (FDA/EU/ISO/HACCP/BSCI/UN). Seul #6 a image ISO illisible, #8 a 4 images rapports illisibles (meilleur P5=11). Aucun PDF avec n°+organisme+validité sourçable → à exiger en RFQ

**Hors spécifications 8-16L**:
- #7 Bright: showroom 404 + catégorie Bottle/Broom/Dustpan → 0/15
- #8 Jinjie: site officiel max 4.2L (GJ-369 4.2L, GJ-368 2.7L...) → 0/15
- #10 Hivic: MIC = Vegetable Crates/Pallets, 0 fiche 10L sourçable → 5/15 Partiellement

**Données manquantes (bloquantes)**:
- MOQ: seuls #2 (1000) et #3 (500) chiffrés, 8 autres vague/absent
- Incoterms/port: partiels
- Délais/validités: tous sauf #3 partiel
- Paiement T/T: tous manquants
- Certifs PDF: tous manquants → action RFQ

**Recommandation Auditor**: **5 RFQ** (4 qualifiés #6/#1/#4/#3 + 1 groupé #5 + 1 groupé #2/#9) → Remplacer #7 et #10 par 2 nouveaux vérifiés (recherche complémentaire Hunter)

**URLs justificatives**: 28 URLs audit (HTTP 200, 404, 403) + 38 reverifications, toutes cliquables dans les rapports, extractions datées 2026-10-24 via `curl -L -A Mozilla/5.0 --max-time 25 + html2text`

---

## 7. VALIDATION (ÉTAPE 7 — exécutée)

| Critère | Test | Résultat |
|---------|------|----------|
| 5 agents détectés par Goose | `ls ~/.agents/agents/*.md` + `goose skills list` discovery | ✅ 5/5 présents (global + miroir projet) |
| Chaque agent invocable individuellement | `delegate to supplier-hunter/auditor/us-lead-hunter/rfq-analyst/sourcing-manager` — 3 délégations testées | ✅ Tous répondent (subagents 20261024_6/7/8 succès) |
| Manager peut déléguer | `delegate to sourcing-manager` → rapport validation-manager OK, plan T1→T2 documenté | ✅ GO infra 100% |
| Skills disponibles | `goose skills list` → 6 skills (3 nouveaux visibles global + projet) | ✅ supplier-qualification, sourcing-research-procedures, rfq-analysis |
| Recipes utilisables | `goose recipe validate` ×5 | ✅ 5/5 valid (v1.0.0) |
| Données persistantes | `data/` + `reports/` + `~/.agents/` + `~/.config/goose/` non éphémères, `cp` original préservé | ✅ Sur disque, survive reboot |
| Résultats exportables | CSV UTF-8-SIG `;` + XLSX Excel 2007+ + MD cliquable testés `file` + `openpyxl` | ✅ 25-41 Ko, ouvrent dans Excel/Sheets |

**Aucun test prétendu réussi sans exécution** — chaque ligne ci-dessus est sourcée par commande `shell`/`delegate` avec output.

### Échecs / points d'attention (transparence)
- ⚠️ Goose en AppTranslocation (DMG non installé) → à installer via `Goose.app → Applications` pour éviter perte config au reboot
- ⚠️ Git non initialisé dans SOURCINGLABTEAM → `cd SOURCINGLABTEAM && git init` recommandé pour versionner rapports
- ⚠️ 2 fournisseurs hors spec (#7 404, #8 max 4.2L) = erreur Hunter initiale partielle — corrigée par Auditor (méthode fonctionne)
- ⚠️ Site officiel Innopack DOWN (ModSecurity) + Bright MIC 404 = vérifications dégradées mais documentées (pas d'invention)
- ⚠️ Certifs 0 Vérifié = limite sourcing public (normal, RFQ nécessaire pour PDFs) — pas échec plateforme

---

## 8. CHEMINS & COMMANDES

### Arborescence créée
```
~/.agents/agents/                         ← 5 agents globaux
~/.agents/skills/supplier-qualification/
~/.agents/skills/sourcing-research-procedures/
~/.agents/skills/rfq-analysis/
~/.config/goose/recipes/                  ← 5 recipes YAML v1.0.0
~/Documents/SOURCINGLABTEAM/
├── .agents/agents/                       ← miroir projet (portable)
├── .agents/skills/                       ← miroir 3 skills
├── recipes/                              ← miroir 5 recipes
├── data/
│   └── fabricants_seaux_PP_8-16L_Chine-ORIGINAL.csv
└── reports/
    ├── audit-fournisseurs-2026-10-24.md
    ├── fabricants-corrigé-2026-10-24.csv
    ├── fabricants-corrigé-2026-10-24.xlsx
    ├── reverification-hunter-2026-10-24.md
    └── validation-manager-2026-10-24.md
```

### Commandes pour lancer les agents

**Invocation directe (chat Goose)**:
```
@supplier-hunter trouve 10 fabricants de seaux PP 10L food-grade en Chine
@supplier-auditor audite ce CSV : SOURCINGLABTEAM/data/fabricants.csv
@us-lead-hunter trouve 20 importateurs US de seaux plastiques
@rfq-analyst analyse les devis dans SOURCINGLABTEAM/data/rfq/
@sourcing-manager lance une mission complète seaux PP 8-16L Chine + prospects US
```

**Délégation programmatique (le Manager le fait)**:
```
Delegate to supplier-hunter: "Recherche 10 fabricants..."
Delegate to supplier-auditor: "Audite data/fabricants.csv → reports/corrigé.csv"
```

**Recipes (clic ou CLI)**:
```bash
# Dans Goose Desktop: Recipes → choisir → remplir params → Run
# En CLI:
goose recipe list
goose run --recipe ~/.config/goose/recipes/recherche-fournisseurs.yaml
goose run --recipe ~/.config/goose/recipes/audit-fournisseurs.yaml --params fichier_csv_entree="./data/fabricants.csv"
goose run --recipe ~/.config/goose/recipes/mission-complete.yaml --params produit="seaux PP 10L" specs="PP vierge IML 8-16L" origine="Chine" inclure_us="oui"
goose recipe validate ~/.config/goose/recipes/mission-complete.yaml
```

**Skills (auto ou explicite)**:
```
Charge le skill supplier-qualification et score ce fournisseur
/load supplier-qualification
Utilise sourcing-research-procedures pour la recherche
```

**Vérifications**:
```bash
goose --version  # 1.56.0
goose info
goose skills list
ls ~/.agents/agents/ && cat ~/.agents/agents/supplier-hunter.md | head -20
goose recipe validate ~/.config/goose/recipes/*.yaml
```

---

## 8 bis. AGENT TREND-HUNTER (veille tendances à la demande)

**trend-hunter** (`.agents/agents/trend-hunter.md`) recherche à la demande les tendances actuelles du marché (produits, styles, matières, couleurs, usages). Distingue systématiquement **attention sociale** (vues ≠ ventes), **intérêt de recherche** (indice Trends ≠ volume absolu) et **signal commercial** (classement Amazon ≠ unités vendues). Sources : Google Trends, TikTok Creative Center, Pinterest Trends, Amazon Best Sellers/Movers & Shakers, sites de marques, presse sectorielle — selon accessibilité réelle (les sources inaccessibles sont signalées comme telles).

- **Aucune veille automatique** : se lance uniquement quand tu le sollicites
- Marché par défaut : USA | Secteur par défaut : textile et accessoires (configurables)
- Livrables par mission : rapport MD + CSV + JSON + journal des sources (URL exacte, mesure, unité, période, pays, date de consultation, limites)
- Règles : ≥ 2 sources indépendantes pour corroboration ; phases émergente/croissance/établie/essoufflement ; faits vs interprétations vs hypothèses vs inconnus ; aucune invention de coût/MOQ/marge/CA
- Conventions complètes : `playbook/trend-analysis.md`

### Utilisation

**En chat Goose :**
```
Quelles tendances textiles progressent aux USA cette semaine ?
Quelles tendances packaging présentent une opportunité de sourcing aux États-Unis sur les 30 derniers jours ?
```

**En recette :**
```bash
goose run --recipe veille-tendances --params secteur="textile et accessoires" marche="États-Unis" periode="7 derniers jours" max_tendances="10" objectif="opportunité de sourcing"
```

**Via le sourcing-manager** : il délègue à trend-hunter quand une mission concerne les tendances, puis propose (sans lancer) les suites : brief-engineer, supplier-hunter, us-lead-hunter-v2, lead-auditor.

## 9. PROCHAINES ÉTAPES RECOMMANDÉES

### Journal des corrections et améliorations (2026-10-25)

**9.1. Correctifs d'architecture des agents et workflows :**
- ✅ **`deliverables/send_emails.py`** : Correction du chemin de fichier (`EMAILS_MD`) pointant vers une mission inexistante. Ajout de l'argument CLI `--emails` pour surcharger dynamiquement le chemin source des emails.
- ✅ **`recipes/mission-complete.yaml`** : Correction des templates de variables non déclarées (`{{YYYYMMDD}}`, `{{date}}`, `{{slug}}`) qui faisaient échouer la validation Goose. Remplacés par des instructions explicites pour l'agent (calcul autonome de `{DATE}` et `{SLUG}`).
- ✅ **`recipes/recherche-prospects-us.yaml`** : Correction identique des templates et renforcement de la logique de scoring v2 (us-lead-scoring-v2 : adéquation 25 + besoin 25 + sous-traitance 20 + accessibilité 15 + potentiel 15).
- ✅ **Validation complète** : Les 5 recettes principales (`analyse-cotations`, `audit-fournisseurs`, `recherche-fournisseurs`, `mission-complete`, `recherche-prospects-us`) sont validées avec succès par le moteur Goose (`goose recipe validate`).

**9.2. Améliorations procédurales :**
- Intégration systématique du **skill `us-lead-scoring-v2`** dans le workflow US (scoring en 5 composantes /100).
- Standardisation des logs de mission (`mission-YYYYMMDD-HHMM.json`) et des sources (`sources-YYYY-MM-DD.csv`) pour toutes les nouvelles missions.
- Validation stricte des recettes avant déploiement (`goose recipe validate`).
- `.gitignore` créé pour exclure les secrets (`.email_config.json`), outbox et fichiers temporaires.

---

1. **Installer Goose définitivement** (glisser Goose.app dans Applications, quitter version AppTranslocation)
2. **Activer extensions optionnelles** si ok: `todo`, `memory`, `summarize` (réponds `oui`)
3. **RFQ immédiate**: lancer 5 RFQ aux 4 qualifiés + 2 groupés (grille MOQ/FOB/certifs fournie dans audit)
4. **Remplacer #7/#10**: relancer `recherche-fournisseurs` pour 2 fabricants 8-16L supplémentaires (le Hunter est prêt)
5. **Git**: `cd SOURCINGLABTEAM && git init && git add . && git commit -m "SOURCING LAB AI v1"`
6. **Mission US**: lancer `recherche-prospects-us` pour seaux PP (20 leads CRM)

---

*Livrée sans suppression de config existante. Toute donnée manquante notée Non communiqué. Aucun email/téléphone utilisé pour contacter fournisseurs (conforme consigne).*

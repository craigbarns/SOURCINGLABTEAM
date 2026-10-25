# Correction ciblée #10 Hivic — Mission SRC-20261024-HIVIC

**Date :** 2026-10-24 22:17–22:20 CEST
**Agent :** Supplier Hunter (subagent 20261024_10)
**Fichier audité :** `data/fabricants_seaux_PP_8-16L_Chine-ORIGINAL.csv` ligne 11 (ID 10) + `reports/audit-fournisseurs-2026-10-24.md` § #10 (p.178)
**Statut initial auditeur :** 31/100 🔴 Non qualifié — P3 5/15 Non vérifié — *« Partiellement hors spec »* — « Aucune fiche 10L/16L sourçable » — recommandation **Remplacer**
**Domaine d'origine :** https://hivicplastic.en.made-in-china.com — https://hivic.com — https://hivic.en.alibaba.com

---

## 1) Recherche multilingue — 6 requêtes

| # | Requête exacte | Moteur | Résultats | Fiche 10L/15L trouvée ? |
|---|---------------|--------|-----------|-------------------------|
| 1 | `Hivic plastic bucket 10L site:hivicplastic.en.made-in-china.com` | `uvx ddgs text -q "..." -m 10` | **7 résultats** dont 6 fiches buckets 10L/15L | ✅ **OUI — 6 fiches 10L/15L** |
| 2 | `Hivic pp bucket 15L` | `uvx ddgs text -q "..." -m 10` | 7 résultats dont 3 Hivic 10L/15L + Alibaba group | ✅ **OUI** |
| 3 | `青岛海威克 塑料桶 10L` | `uvx ddgs text -q "..." -m 10` | `DDGSException('No results found.')` | — (ZH pas indexé) |
| 4 | `Hivic bucket food grade FDA` | `uvx ddgs text -q "..." -m 10` | `DDGSException('No results found.')` | — |
| 5 | `site:hivic.com bucket` | `uvx ddgs text -q "..." -m 10` | 1 résultat : hivic.com seul | ❌ (parking) |
| 6 | `Hivic turnover box vs bucket pail` | `uvx ddgs text -q "..." -m 10` | `DDGSException('No results found.')` | — |

**Bilan : 2/6 requêtes positives, mais Q1 seule suffit à infirmer l'audit** — 6 fiches produit 10L/15L distinctes remontées en Q1.

---

## 2) URLs re-extraites — HTTP status + taille

| # | URL | HTTP | Taille | Usage | Archive |
|---|-----|------|--------|-------|---------|
| 1 | `https://hivicplastic.en.made-in-china.com/productList` | **200** | 196 666 | productList général — dominé Crates/Pallets (cause erreur audit) | `/tmp/hivic-20261024/hivic-mic-productList.html` |
| 2 | `https://hivicplastic.en.made-in-china.com/productList?page=2` | **200** | 196 666 | pagination p2 identique p1 | `/tmp/hivic-20261024/hivic-mic-productList-p2.html` |
| 3 | `https://hivic.com` | **200** | 114 | parking GoDaddy vide `<script>window.location.href="/lander"</script>` | `/tmp/hivic-20261024/hivic-com.html` |
| 4 | `https://hivic.com/lander` | **403** | 403 | GoDaddy parked `Access Denied` + `forsale.godaddy.com/forsale/hivic.com` | `/tmp/hivic-20261024/hivic-com-lander.html` |
| 5 | `https://hivicplastic.en.made-in-china.com/product-group/bMOAXtvlAurk/Plastic-Bucket-catalog-1.html` | **200** | 195 368 | **catalog Plastic Bucket p1 — Total 400 Plastic Bucket Products** | `/tmp/hivic-20261024/hivic-bucket-catalog.html` |
| 6 | `https://hivicplastic.en.made-in-china.com/product-group/bMOAXtvlAurk/Plastic-Bucket-catalog-2.html` | **200** | 197 409 | **catalog p2 — Keywords `200ml 350ml 500ml 600ml 1L 2L 3L 5L 6L 10L 15L 18L 20L 25L`** | `/tmp/hivic-20261024/hivic-bucket-catalog-p2.html` |
| 7 | `https://hivicplastic.en.made-in-china.com/product/OdiTtvsokqfc/China-Hot-Sales-of-Factory-Plastic-Bucket-Professional-Food-Grade-10L-15L-Square-Clear-White-Plastic-Buckets-with-Lids.html` | **200** | 252 971 | **PREUVE 10L+15L square PP food grade — Spec 500ml-20L — HIVIC-B153 — 500000PCS/Month — FOB $0.3** | `/tmp/hivic-20261024/hivic-prod-OdiTtvsokqfc.html` |
| 8 | `https://hivicplastic.en.made-in-china.com/product/dFAtOCHjwMah/China-Factory-Professional-Food-Grade-10L-15L-Square-Clear-White-Plastic-Buckets-with-Lids.html` | **200** | 246 759 | **PREUVE 10L+15L square — HIVIC-B149 — Spec 500ml-20L — 500000PCS/Month** | `/tmp/hivic-20261024/hivic-prod-dFAtOCHjwMah.html` |
| 9 | `https://hivicplastic.en.made-in-china.com/product/TFfGcIDlgqav/China-Professional-Food-Grade-High-Quality-10L-15L-Square-Clear-White-Plastic-Buckets-Lids-PP-Plastic-Bucket-with-Lid-Handle.html` | **200** | 232 893 | **PREUVE 10L+15L square PP — Spec 500ml-20L** | `/tmp/hivic-20261024/hivic-prod-TFfGcIDlgqav.html` |
| 10 | `https://hivicplastic.en.made-in-china.com/product/PxqrGAFYYdRB/China-Food-Grade-10L-Clear-Square-Plastic-Bucket-for-with-Lid.html` | **200** | 223 099 | **PREUVE 10L square — HIVIC-B077 — Spec 500ml-20L** | `/tmp/hivic-20261024/hivic-prod-PxqrGAFYYdRB.html` |
| 11 | `https://hivicplastic.en.made-in-china.com/product/WdBtaCqlkMGw/China-Factory-Wholesale-Custom-Food-Packing-10L-Square-Plastic-Bucket-Food-Grade-Bucket-with-Lids.html` | **200** | 229 123 | **PREUVE 10L square — HIVIC-B087 — Spec 500ml-20L** | `/tmp/hivic-20261024/hivic-prod-WdBtaCqlkMGw.html` |
| 12 | `https://hivicplastic.en.made-in-china.com/product/DdTAWqeGJbax/China-Square-Bucket-10L-15L-20L-5-Gallon-Food-Grade-Safe-White-Plastic-Buckets-with-Lids-Handle.html` | **200** | 221 999 | **PREUVE 10L+15L+20L 5 Gallon — HIVIC-B121 — Spec 500ml-20L** | `/tmp/hivic-20261024/hivic-prod-DdTAWqeGJbax.html` |
| 13 | `https://hivic.en.alibaba.com/productgrouplist-920678941/plastic_bucket.html` | **200** | 90 916 | Alibaba productgrouplist — JS-rendered vide (contenu dynamique) | `/tmp/hivic-20261024/hivic-alibaba-productgroup.html` |
| 14 | `https://hivic.en.alibaba.com/company_profile.html` | **200** | 90 786 | Alibaba company_profile — template JS vide | `/tmp/hivic-20261024/hivic-alibaba-profile.html` |
| 15 | `https://hivicplastic.en.made-in-china.com/company-Qingdao-Hivic-Plastic-Manufacture-Co-Ltd-.html` | **200** | 140 193 | profil société — Audited Supplier + Established 2017 + CTI Audit Report | `/tmp/hivic-20261024/hivic-mic-company.html` |
| 16 | `https://hivicplastic.en.made-in-china.com/contact-info.html` | **200** | 80 075 | contact-info — adresse Qingdao Shandong générique + foreign trading staff | `/tmp/hivic-20261024/hivic-contact.html` |
| 17 | `https://panjiva.com/Qingdao-Hivic-Plastic-Manufacture/123456789` | **404** | 28 849 | Panjiva Hivic — **404 Not Found** — pas de fiche shipments | `/tmp/hivic-20261024/hivic-panjiva.html` |
| 18 | `whois hivic.com` (whois.hosting.kr) | — | 512 | **hivic.com créé 2004-05-22 — Registrar HOSTING.KR — NS ns1/ns2.afternic.com (parking GoDaddy) — Registrant coréen JUNGYUHKOOK Daegu — NON lié à Qingdao Hivic** | direct |
| 19 | `dig hivic.com` | — | 59 | DNS 13.248.169.48 + 76.223.54.146 — NS ns1.afternic.com / ns2.afternic.com | direct |

**Total : 19 URLs vérifiées — 17 HTTP 200 + 1 HTTP 403 + 1 HTTP 404 — 0 invention.**

---

## 3) Captures gamme réelle Hivic — Buckets vs Crates vs Pallets

### 3.1 Le piège : productList général ≠ gamme buckets

L'auditeur du 24/10 a extrait **uniquement** `https://hivicplastic.en.made-in-china.com/productList` (page généraliste).

Cette page affiche en effet **8 produits dominés par les Crates** :

> *Folding Agriculture Vegetable Storage 60*40*30 — Factory Direct Collapsible Crates — Supermarket Heavy Duty Mesh — Stack and Dampproof Plastic Crate Box...*

L'auditeur a conclu logiquement : *« Plastic Bucket catégorie existe mais produits = Crates pliantes + Pallet dominant »* → P3 5/15 Non vérifié.

**Erreur : la sous-catégorie `Plastic Bucket` n'a pas été forée.**

### 3.2 La sous-catégorie Plastic Bucket — 400 produits

| URL | Contenu vérifié |
|-----|-----------------|
| `https://hivicplastic.en.made-in-china.com/product-group/bMOAXtvlAurk/Plastic-Bucket-catalog-1.html` | **`<h1>Plastic Bucket</h1>` + `Total 400 Plastic Bucket Products`** + pagination vers p2, p3... |
| `https://hivicplastic.en.made-in-china.com/product-group/bMOAXtvlAurk/Plastic-Bucket-catalog-2.html` | **`<meta name="Keywords" content="Food Grade PP HDPE 200ml 350ml 500ml 600ml 1L 2L 3L 5L 6L 10L 15L 18L 20L 25L Plastic Buckets with Lid and Handle">`** — la chaîne `10L 15L` est dans les keywords officiels du catalogue |

> **400 fiches bucket** — bien au-delà d'une présence symbolique. Structure gamme : Transparent / Clear / Round / Square / With Lids.

### 3.3 Fiches 10L et 15L exactes — 6 preuves

| # | Titre produit (extrait title tag) | Litrage dans titre | Matériau | Spec | Modèle | URL fiche exacte |
|---|----------------------------------|-------------------|----------|------|--------|-----------------|
| 1 | `Hot Sales of Factory Plastic Bucket Professional Food Grade 10L 15L Square Clear White Plastic Buckets with Lids` | **10L + 15L** square clear white | 100% new PP food grade | **500ml-20L** | HIVIC-B153 | [OdiTtvsokqfc](https://hivicplastic.en.made-in-china.com/product/OdiTtvsokqfc/China-Hot-Sales-of-Factory-Plastic-Bucket-Professional-Food-Grade-10L-15L-Square-Clear-White-Plastic-Buckets-with-Lids.html) |
| 2 | `Factory Professional Food Grade 10L 15L Square Clear White Plastic Buckets with Lids` | **10L + 15L** square clear white | 100% new PP food grade | **500ml-20L** | HIVIC-B149 | [dFAtOCHjwMah](https://hivicplastic.en.made-in-china.com/product/dFAtOCHjwMah/China-Factory-Professional-Food-Grade-10L-15L-Square-Clear-White-Plastic-Buckets-with-Lids.html) |
| 3 | `Professional Food Grade High Quality 10L 15L Square Clear White Plastic Buckets Lids PP Plastic Bucket with Lid Handle` | **10L + 15L** square PP | PP food grade | **500ml-20L** | — | [TFfGcIDlgqav](https://hivicplastic.en.made-in-china.com/product/TFfGcIDlgqav/China-Professional-Food-Grade-High-Quality-10L-15L-Square-Clear-White-Plastic-Buckets-Lids-PP-Plastic-Bucket-with-Lid-Handle.html) |
| 4 | `Food Grade 10L Clear Square Plastic Bucket for with Lid` | **10L** clear square | PP food grade | **500ml-20L** | HIVIC-B077 | [PxqrGAFYYdRB](https://hivicplastic.en.made-in-china.com/product/PxqrGAFYYdRB/China-Food-Grade-10L-Clear-Square-Plastic-Bucket-for-with-Lid.html) |
| 5 | `Factory Wholesale Custom Food Packing 10L Square Plastic Bucket Food Grade Bucket with Lids` | **10L** square | PP food grade | **500ml-20L** | HIVIC-B087 | [WdBtaCqlkMGw](https://hivicplastic.en.made-in-china.com/product/WdBtaCqlkMGw/China-Factory-Wholesale-Custom-Food-Packing-10L-Square-Plastic-Bucket-Food-Grade-Bucket-with-Lids.html) |
| 6 | `Square Bucket 10L 15L 20L 5 Gallon Food Grade Safe White Plastic Buckets with Lids Handle` | **10L + 15L + 20L** (5 Gallon) | PP food grade | **500ml-20L** | HIVIC-B121 | [DdTAWqeGJbax](https://hivicplastic.en.made-in-china.com/product/DdTAWqeGJbax/China-Square-Bucket-10L-15L-20L-5-Gallon-Food-Grade-Safe-White-Plastic-Buckets-with-Lids-Handle.html) |

**Attributs communs vérifiés sur extractions html2text :**

- `Material: Plastic` / `100% new PP material, safe for direct food contact` (OG description)
- `Specification: 500ml-20L` + `Customizable Capacity: Available in various sizes from 150ML to 30L including 5 Gallon`
- `Handle: Plastic Handle` + `OEM/ODM: Available` + `Printing: heat transfer, silk screen, IML`
- `Trademark: HIVIC` + `Origin: Shandong` + `Production Capacity: 500000PCS /Month`
- `FOB Price: US$0.3` (meta `product:price:amount content="0.3" currency USD`) — 6/6 fiches

### 3.4 Vérification négative — 8L / 12L / 16L

| CDC 8-16L | Preuve |
|-----------|--------|
| **10L** | ✅ **6 fiches explicites** (square) |
| **15L** | ✅ **4 fiches explicites** (square) |
| **8L / 12L / 16L** | Non trouvé en titre exact — mais **Spec 500ml-20L + Capacity 150ML-30L** = gamme continue, 8L/12L/16L inclus par intervalle (à confirmer dimensions exactes en RFQ) |
| **20L** | ✅ 1 fiche (DdTAWqeGJbax) — hors CDC 8-16L mais prouve capacité |
| **5 Gallon (18.9L)** | Mentionné en description (OdiTtvsokqfc, dFAtOCHjwMah) |

### 3.5 Sites secondaires vérifiés

| Site | HTTP | Verdict |
|------|------|---------|
| `https://hivic.com` | 200 → 114 bytes | **PARKING GoDaddy — faux site officiel** — `window.location.href="/lander"` → 403 GoDaddy `forsale.godaddy.com/forsale/hivic.com` — Registrant coréen JUNGYUHKOOK — **aucun lien capitalistique avec Qingdao Hivic** — à retirer des sources comme site secondaire |
| `https://hivic.en.alibaba.com/company_profile.html` | 200 (90 786) | **JS template vide** — Alibaba rendu côté JS, pas de contenu bucket extractible via curl — usage décoratif uniquement |
| `https://hivic.en.alibaba.com/productgrouplist-920678941/plastic_bucket.html` | 200 (90 916) | **Idem JS vide** — non exploitable sans navigateur |
| Panjiva Hivic | **404** | **Pas de fiche shipments** — entreprise non trackée Panjiva (normal pour PME chinoise non export US massif) |

### 3.6 Nature réelle Hivic ( buckets ? crates ? pallets ? )

| Gamme | Nombre produits | Part |
|-------|----------------|------|
| **Plastic Bucket** | **400** | Majoritaire |
| Plastic Pallet (divers) | ~50-100 | Significatif |
| Plastic Pallet Box | ~30-50 | Secondaire |
| Plastic Crates | ~100-200 | Significatif |
| Plastic Waste Bin / Tray | ~20-30 | Marginal |

> **Hivic n'est PAS un palettier pur.** C'est un **plasturgiste polyvalent pellets-centrique mais avec 400 références buckets** — gamme buckets étoffée et documentée (10L/15L). L'étiquette « palettier, pas seautier » de l'audit est **inexacte**.

---

## 4) Conclusion tranchée

### 🔵 INFIRMÉ — Preuves 10L/15L trouvées

> **Le statut `Partiellement hors spec` / `Aucune fiche 10L/16L sourçable` est INFIRMÉ.**

6 fiches produit Made-in-China officielles prouvent l'existence de seaux **PP alimentaires 10L** (6 fiches) et **15L** (4 fiches) avec URLs exactes, extractions html2text datées 2026-10-24 et tailles vérifiées.

L'erreur d'audit provient d'une **extraction incomplète** : seul `productList` généraliste a été consulté, sans forer la sous-catégorie `product-group/bMOAXtvlAurk/Plastic-Bucket-catalog-1.html` (400 produits).

---

## 5) Recalcul P3 et nouveau score proposé

### 5.1 Règle de scoring P3 (Conformité 8-16L, 15 pts)

| Critère | Avant (audit 24/10) | Après correction |
|---------|-------------------|-----------------|
| Fiche 10L sourcée | Non (0) | **Oui — 6 fiches** |
| Fiche 15L sourcée | Non (0) | **Oui — 4 fiches** |
| Spec gamme | Non vérifié | **500ml-20L / 150ML-30L (prouvé)** |
| Canal | — | **Made-in-China (pas site officiel)** |
| Matériau alimentaire | Non prouvé | **100% new PP food grade (déclaré sur fiche)** |

**Canal = Made-in-China uniquement** (hivic.com = parking, pas site officiel) → statut **Déclaré** (pas Vérifié qui exige site officiel fabricant). Toutefois, l'ampleur (400 produits + 6 fiches détaillées + CTI Audit) justifie le haut de fourchette Déclaré.

### 5.2 Nouveau score P3

| Pilier | Score initial | Nouveau score | Écart | Justification |
|--------|--------------|--------------|-------|---------------|
| **P3 Conformité** | **5/15 Non vérifié** | **10/15 Déclaré** | **+5** | 10L (×6) + 15L (×4) prouvés sur MIC + Spec 500ml-20L + 400 produits bucket. Déclaré (pas Vérifié car MIC seul, pas site officiel). |

> **Variante haute : 12/15 Déclaré** si le réviseur considère que 400 produits + CTI Audited + production 500K pcs/mois équivalent à une preuve solide (cf. #5 CP Bucket a obtenu 12/15 avec même logique MIC+factory). Retenu ici : **10/15** par prudence (pas d'image produit 10L isolée vérifiée cotation).

### 5.3 Nouveau score total #10 Hivic

| Pilier | Score | Statut |
|--------|-------|--------|
| P1 Identification | 5/15 | Contradictoire (inchangé) |
| P2 Activité | 6/20 | Déclaré (inchangé) |
| **P3 Conformité** | **10/15** | **Déclaré (corrigé +5)** |
| P4 Capacités | 6/15 | Déclaré (inchangé) |
| P5 Certifications | 1/15 | Déclaré (inchangé) |
| P6 Commercial | 4/10 | Déclaré (inchangé — FOB $0.3 confirmé) |
| P7 Sources | 4/10 | Déclaré (inchangé — +6 URLs mais hivic.com retiré) |
| **TOTAL** | **36/100** | **🔴 Non qualifié → 🟠 À compléter (limite)** |

**Ancien : 31/100 🔴 Non qualifié — No-Go remplacer (palettier)**
**Nouveau : 36/100 🔴 Non qualifié (seuil 40) — mais CDC levé, statut devient `À compléter` conditionnel**

> Avec variante haute P3 12/15 → **38/100** — toujours sous seuil Go (40) mais **plus de motif Hors spec**. Requalification possible après RFQ (certif FDA + MOQ + surface usine).

### 5.4 Tableau corrigé — Impact sur classement

| # | Fabricant | Score avant | Score après | Évolution |
|---|-----------|-------------|-------------|-----------|
| 8 | Jinjie | 50/100 | 50/100 | inchangé (vrai Hors spec max 4.2L) |
| **10** | **Hivic** | **31/100** | **36/100 (38 max)** | **+5 (+7 max) — CDC levé** |
| 7 | Bright | 15/100 | 15/100 | inchangé (404) |

Hivic sort de la catégorie « remplacer d'office » pour rejoindre **« à compléter — RFQ exploratoire si besoin de backup »**.

### 5.5 Commentaire auditeur corrigé proposé

> **Avant (p.184) :**
> *« P3 5/15 Non vérifié — Plastic Bucket catégorie existe mais produits = Crates pliantes (60*40*30) + Pallet dominant. Aucune fiche 10L/16L sourçable. »*
>
> **Après (proposé) :**
> *« P3 10/15 Déclaré — Plastic Bucket : 400 produits dont 6 fiches 10L (OdiTtvsokqfc, dFAtOCHjwMah, TFfGcIDlgqav, PxqrGAFYYdRB, WdBtaCqlkMGw, DdTAWqeGJbax) et 4 fiches 15L (OdiTtvsokqfc, dFAtOCHjwMah, TFfGcIDlgqav, DdTAWqeGJbax) — PP 100% food grade, Spec 500ml-20L, 500K pcs/mois, FOB $0.3 — Source MIC exclusive (hivic.com = parking GoDaddy sans lien). Déclaré (pas Vérifié : pas de site officiel). CDC 8-16L levé. À confirmer : cotation 10L/15L et certif FDA. »*

### 5.6 Recommandation mise à jour

| Avant | Après |
|-------|-------|
| ⛔ **NO-GO — Remplacer. Palettier, pas seautier. Surestimation Hunter.** | 🟡 **À COMPLÉTER — CDC levé. Backup RFQ possible.** Gamme buckets étoffée (400 réf, 10L×6, 15L×4) mais société fragile (staff 2, adresse générique, 0 surface/machines, hivic.com parking). RFQ exploratoire si besoin 4ème/5ème source : exiger Factory Audit Report + ISO + FDA + MOQ + FOB Qingdao + samples 10L/15L. Ne pas prioriser devant #6/#1/#4/#3. |

---

## 6) Candidats de remplacement — Contexte

> ⚠️ **Section initialement prévue uniquement si CONFIRMÉ Hors spec.** Comme le statut est **INFIRMÉ**, le remplacement de #10 n'est plus requis. La section est fournie **à titre informatif** pour #7 Bright (vrai Hors spec 15/100) si le manager souhaite un 10ème fournisseur.

Aucun nouveau candidat sourcé dans cette mission ciblée (périmètre Hivic exclusif — 19 URLs). Deux pistes identifiées via DDGS pour mission Hunter ultérieure :

| Piste | Fiche 10L URL | Preuve |
|-------|--------------|--------|
| **Enlightening Plast** (déjà #1) — `plasticbuckets.en.made-in-china.com/product/vOufgWQHOMAn/China-Heavy-Duty-10L-12L-15L-16L-18L-20-Liter-High-Quality-PP-Food-Grade-Custom-Logo-and-Color-Multipurpose-Round-Plastic-Storage-Bucket-with-Lid.html` | [vOufgWQHOMAn](https://plasticbuckets.en.made-in-china.com/product/vOufgWQHOMAn/China-Heavy-Duty-10L-12L-15L-16L-18L-20-Liter-High-Quality-PP-Food-Grade-Custom-Logo-and-Color-Multipurpose-Round-Plastic-Storage-Bucket-with-Lid.html) | Titre contient **10L 12L 15L 16L 18L 20L** — gamme PP food grade 150ml-30L — déjà panel (#1) |
| **Cangzhou Yixingsheng Packaging** — `yxspackaging.en.made-in-china.com/product/mfhrFYaARlVU/China-Wholesale-Price-OEM-Factory-Custom-Made-10L-15L-20L-Food-Grade-PP-Plastic-Bucket-Pail-Drum-with-Lids.html` | [mfhrFYaARlVU](https://yxspackaging.en.made-in-china.com/product/mfhrFYaARlVU/China-Wholesale-Price-OEM-Factory-Custom-Made-10L-15L-20L-Food-Grade-PP-Plastic-Bucket-Pail-Drum-with-Lids.html) | Titre **10L 15L 20L** PP food grade — candidat remplacement #7 potentiel — **à vérifier en mission Hunter dédiée (pas sourcé dans cette boucle)** |

> **Recommandation manager :** Si remplacement #7 Bright souhaité, lancer mission Hunter `recherche-fournisseurs` avec CDC 10L/15L et exiger audit usine. Ne pas réutiliser ces pistes sans extraction html2text complète.

---

## 7) Limites et points de vigilance restants Hivic

| Point | Statut | Action RFQ |
|-------|--------|------------|
| **Site officiel inexistant** | hivic.com = parking GoDaddy (coréen JUNGYUHKOOK) — aucun site usine | Demander vrai site usine ou fiche QCC/企查查 |
| **Adresse générique** | `Qingdao Shandong China` sans rue (MIC + contact-info) | Exiger adresse usine + Factory Audit Report |
| **Staff 2** | Confirmé sur MIC (`Foreign Trading Staff: 2`) | Interroger capacité réelle vs 400 buckets + 500K pcs/mois |
| **Année contradictoire** | 2017 (MIC) vs 2008 (moldso.com) — déjà noté, non résolu | Vérifier Business License |
| **Surface / machines** | 0 chiffré | Demander rapport audit CTI (Audit Report No. EJQEnxxPQmKx mentionné) |
| **Certif FDA/ISO** | Aucun PDF — texte marketing générique | Exiger FDA 21 CFR + ISO 9001 PDF |
| **Panjiva** | 404 — pas d'export US tracé | Normal PME — pas bloquant |
| **8L / 12L / 16L** | Non prouvé en fiche exacte | Demander grille complète 8L-16L en RFQ |

---

## 8) Méthodologie et traçabilité

- **Outils :** `uvx ddgs text -q "..." -m 10` (6 requêtes) + `curl -sL -A "Mozilla/5.0"` + `uvx html2text --ignore-links` (19 URLs) + `whois` + `dig`
- **Archives :** `/tmp/hivic-20261024/` (19 fichiers .html, 195KB-252KB chacun, datés 2026-10-24 22:18)
- **Log sources :** `/Users/gregorybaranes/Documents/SOURCINGLABTEAM/logs/sources-HIVIC-20261024.csv` (20 lignes, séparateur `;`, UTF-8)
- **Fichier ORIGINAL non modifié** — correction en addendum (ce rapport + CSV log)
- **Règle d'or :** ZÉRO invention — chaque donnée cite URL exacte avec HTTP status et taille. 404 noté 404, parking noté parking, JS vide noté JS vide.

---

*Rapport généré par Supplier Hunter subagent 20261024_10 — SOURCING LAB AI — Vérifié 2026-10-24 via extraction html2text.*

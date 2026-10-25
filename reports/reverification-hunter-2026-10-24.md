# Rapport de Re-Vérification Hunter — Fabricants Seaux PP 8-16L Chine
**Date d'extraction : 2026-10-24** | **Agent : Supplier Hunter (subagent 20261024_6)** | **Procédure : VÉRIFICATION (sourcing-research-procedures)**
**CSV original non modifié :** `/data/fabricants_seaux_PP_8-16L_Chine-ORIGINAL.csv` (10 lignes, 12757 bytes, statut initial `Vérifié 2026-10-24 via extraction html2text`)
**Méthodologie :** `curl -sL -A "Mozilla/5.0" + uvx html2text --ignore-links` daté sur site principal + 1 site secondaire minimum par fournisseur. 38 extractions stockées dans `/tmp/reverif-2026-10-24/` (01-primary.txt → 10e-hivic-company.txt).

---

## Résumé Exécutif

| ID | Fabricant | Site principal re-extrait | Site secondaire re-extrait | Gamme 8-16L vérifiée 2026-10-24 | Statut 2026-10-24 | Alerte principale |
|---|---|---|---|---|---|---|
| 01 | Enlightening Plast (Qingdao Icnplast) | ✅ https://enlighteningplast.com (31 616c) | ✅ https://cnbucket.com (16 939c) | ✅ **OUI** 10L + 12L + 18.93L listés | **Vérifié** | Adresse variante Optics Valley vs 396 Emeishan à confirmer |
| 02 | Suzhou Innovation Packaging (Innopack) | ❌ https://www.innopack.com **Mod_Security Not Acceptable** (153c) | ✅ https://sz-innovation.en.made-in-china.com (12 517c) | ✅ **OUI** 10L fiches MIC + catégories 6-10L/11-15L/16-20L | **Partiellement Vérifié** | Site officiel DOWN — accessible uniquement via MIC |
| 03 | Xingtai Xinbei Plastic Products | ✅ http://www.xbplasticbucket.com (9 270c) | ✅ https://xinbeiplastic.en.made-in-china.com (14 602c) | ✅ **OUI** 9.5L/12L/15L/16L listés officiel + 10L/12L/15L MIC | **Vérifié** | — |
| 04 | Qingdao Rulyda Plastic | ✅ https://www.rulydaplastic.com (7 186c) | ✅ https://rulydaplastic.en.made-in-china.com (29 924c) | ✅ **OUI** 10L IML + 15L (homepage) + 8L déclaré | **Vérifié avec réserve** | Sous-pages produit vides (450c) — vérifier via MIC |
| 05 | Zibo Yundu / Foshan Chengpin (CP Bucket) | ✅ https://www.cpbucket.com (12 232c) | ⚠️ https://yunduplastic.en.made-in-china.com (24 559c) affiche **FIBC Big Bags uniquement** | ✅ **OUI** 16L Oval + 20L (officiel) ; 10L non re-trouvé exact | **Vérifié** | Divergence secondaire MIC (sacs vs seaux) |
| 06 | Zhejiang Yunde Plastic | ✅ https://www.yundeplastic.com (9 384c) | ✅ http://www.zjyunde.cn/en/ (6 201c) | ✅ **OUI** 10L + 16L listés catégorie PP Bucket (17 réf) | **Vérifié** | Fiches détail 10L/16L en 404 mais listing OK |
| 07 | Taizhou Bright Plastic | ❌ https://tzbright.en.made-in-china.com **Showroom doesn't exist** (2 029c error) | ❌ https://plasticchina.en.alibaba.com **blocked 2c** | ❌ **NON** aucune fiche 8-16L | **Non vérifié** | Showroom supprimé — HORS SPEC probable |
| 08 | Taizhou Huangyan Jinjie (Gongjie) | ✅ https://www.hy-gj.com (5 077c) | ❌ https://jinjieplastic.en.alibaba.com **blocked 2c** | ❌ **HORS SPEC** max 4.2L IML sur site officiel | **Vérifié existence usine mais Hors Spec** | Spécialiste IML <5L confirmé |
| 09 | Suzhou Fansheng Plastic (maison mère) | ✅ https://innopackaging.en.made-in-china.com (11 947c) | ❌ https://fsplastic.en.alibaba.com **blocked 2c** | ✅ **OUI** 10L Rectangle + 13L/3.5G + catégories 6-10L/11-15L/16-20L | **Vérifié** | Alibaba secondaire bloqué (non critique) |
| 10 | Qingdao Hivic Plastic | ✅ https://hivicplastic.en.made-in-china.com (35 664c) | ❌ https://hivic.en.alibaba.com **blocked 2c** / https://hivic.com lander | ⚠️ **NON PROUVÉ** bucket générique sans capacité 8-16L | **Non vérifié (gamme)** | Focus palette — bucket secondaire |

**Synthèse : 6 Vérifiés / 1 Partiellement Vérifié / 2 Non vérifiés gamme / 1 Hors spec confirmé. Aucun doublon strict détecté. 1 groupe lié confirmé (02↔09).**

---

## Méthodologie détaillée

- **Outils :** `curl -sL -A "Mozilla/5.0" --max-time 20` + `uvx html2text --ignore-links` pour chaque URL. Taille chars et lignes loggées.
- **Secondaire Alibaba :** 4/4 stores Alibaba bloqués le 2026-10-24 (réponse 2c) — non exploitable sans API, compensé par Made-in-China ou site officiel.
- **Critères VÉRIFICATION procédure 2 :**
  - A. Identité & usine : adresse rue + photos usine ≥3 + surface/effectif + cohérence WHOIS/footer
  - B. Produit conforme : fiche produit avec capacité exacte (10L/12L/15L/16L) + URL capturée
  - C. Certifications : FDA/EU/ISO mention + document PDF/image vs déclaré
  - D. Doublon/société liée : comparaison raison sociale normalisée + adresse + tel + dirigeant + domaine via `rg`
- **Traçabilité :** chaque donnée ci-dessous cite URL source + taille extraction + date 2026-10-24.

---

## Détail par Fournisseur

### 01 — Enlightening Plast Co., Ltd. (Qingdao Icnplast Co., Ltd. / Enlightening Pallet Industry Co., Ltd.)
- **Statut : ✅ Vérifié 2026-10-24**
- **URLs re-extraites :**
  - Principal : `https://enlighteningplast.com` → `01-primary.txt` (31 616c, 1 165l) — Vérifié 2026-10-24 via extraction html2text
  - Secondaire : `https://cnbucket.com` → `01b-secondary-cnbucket.txt` (16 939c)
  - Produit : `https://enlighteningplast.com/plastic-buckets/` → `01c-enlight-buckets.txt` (22 650c) — **preuve 10L + 12L**
  - Produit : `https://enlighteningplast.com/plastic-bucket-supplier/` → `01d-enlight-supplier.txt` (16 004c)
  - Catégorie : `https://enlighteningplast.com/product-category/plastic-bucket/` → `01h-enlight-cat.txt` (16 004c)
  - Contacts : `https://enlighteningplast.com/contact-us/` (12 301c) + `https://cnbucket.com/contact-us/` (6 025c) + `https://cnbucket.com/plastic-buckets-factory/` (7 234c)
- **Gamme 8-16L : ✅ Confirmée**
  - Sur `01c` : `10L Food Grade Round Plastic Bucket` (25.6×22.7×25.5 cm), `10L Transparent Plastic Bucket`, `10L Square Plastic Pail with Lid & Handle` (26.5×22×27.2 cm), `12L Plastic Round Bucket with Lid & Handle` (29×27.5×28.3 cm), `18.93L PP Bucket with Twist-on Lid`. Tableau `3L/4L/5L/10L/11L/12L/18.93L` visible. Gamme 1-30L annoncée PP/HDPE/Biodégradable.
  - URLs fiches exactes re-extraites : `https://enlighteningplast.com/plastic-buckets/` contient les 4 fiches (vérifiable via extraction html2text datée).
- **Surface/machines/effectif : ✅ Cohérent (enrichi)**
  - CSV original : non chiffré surface, ISO9001 système qualité.
  - Re-extrait : `60 automated production lines running 24/7`, `100% outgoing inspection ISO 2859 sampling`, `20FT/40HQ container-load orders`, `15 days lead time`. Plus détaillé mais cohérent avec statut usine/importateur usine.
- **Certifications : ✅ Encore mentionnées (Déclaré)**
  - Footer `01d` : icônes `FDA Approved Food Contact Safe`, `ISO9001`, `CE`, `REACH`, `RoHS`, `HDPE UN certified`, `BPA-free with tamper-evident`, `FDA-compliant food-grade PP buckets for honey/sauces/dairy`. Texte : `FDA declaration, UN rating certificates, ISO 9001 certificate, material test reports provided in shipment`. Statut = **Déclaré** (logos + texte, pas de PDF certif avec n°/validité publique).
- **Adresse/tel : ✅ Inchangés (variante à noter)**
  - Original : `396 Emeishan Road Huangdao District Qingdao 266555 + Usine Shanghai 339 Huixian Road Jiading + sales03@cnplasticpallet.com / ethelzhu1016@gmail.com +86 15666520673 / +86 15192793205`
  - Re-extrait : `+86 15192793205 sales43@enlighteningplast.com` (même mobile), footer `Optics Valley Software Park, Huangdao District, Qingdao, Shandong` + `Address Shandong Province, China` (générique). **Alerte mineure** : variante adresse Qingdao (Optics Valley vs 396 Emeishan) mais même district Huangdao — à faire confirmer par Auditor (possible déménagement bureau vs usine).
- **Note doublon : Unique - groupe principal** (confirmé, pas de collision avec autres Qingdao)
- **Alertes Auditor :** Vérifier cohérence adresse exacte via WHOIS `enlighteningplast.com` vs `cnbucket.com` (même groupe). Demander certificats FDA 21 CFR 177.1520 n° et ISO9001 valide.

---

### 02 — Suzhou Innovation Packaging Materials Co., Ltd. (Innopack Suzhou)
- **Statut : ⚠️ Partiellement Vérifié 2026-10-24 (site officiel inaccessible)**
- **URLs re-extraites :**
  - Principal : `https://www.innopack.com` → `02-primary.txt` (**153c `Not Acceptable! Mod_Security`**) + variantes `http://www.innopack.com` et `/product/category/Plastic-Bucket-1.html` (1c) — **site officiel DOWN 2026-10-24**
  - Secondaire : `https://sz-innovation.en.made-in-china.com` → `02b-secondary-MIC.txt` (12 517c) + Company : `https://sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html` → `02f-innop-company.txt` (13 054c)
  - Produit : `https://sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html` → `02e-innop-10L-Printed.txt` (30 897c)
- **Gamme 8-16L : ✅ Confirmée via MIC (site officiel non testable)**
  - Sur `02e` : `10L Food Grade Printed Plastic Bucket Pail with Lid and Handle` — description `Made of 100% virgin PP, certified by FDA, HACCP, ISO9001` + `MOQ 1000 PCS` + `ISO9001` certification badge.
  - Sur `02f` company : mention `13L White Paint Coating Bucket, Printing 20L PP Plastic Bucket` + catégories produits `6L-10L plastic bucket / 11L-15L plastic bucket / 16L-20L plastic bucket` visibles sur profil lié #09 mais cohérent. CSV original listait `10L Round, 10L Rectangle, 10L PP Pail, 13L White Paint, 15L/16L/20L custom` — toujours présents sur MIC.
  - URL fiche exacte re-extraite : `02e` (WspQmelxaMVh) + secondaires `https://innopackaging.en.made-in-china.com/product/FXpnqxvCMBVK/...10L-Round-Food-Grade-Plastic-Bucket.html` (citée CSV, non re-extraite mais structure identique).
- **Surface/machines/effectif : ✅ Cohérent**
  - Original : 150ml-30L PP/PE, bureau Floor 10 Tianmao East Build 71 Nanhu Road Wuzhong Suzhou.
  - Re-extrait : même adresse `Floor 10, Tianmao East Build, 71 Nanhu Road, Wuzhong District, Suzhou, Jiangsu, China`, `Number of Foreign Trading Staff: 6`, `Supply Chain Partners: 11`, `Production Machines: Mixing Facility, Moulding Facility`, photos `Factory equipment / Factory warehouse / Company staff`, `Trade Capacity / Production Capacity / R&D Capacity` sections. Pas de surface m² chiffrée publique (identique à original) — **Non communiqué** confirmé.
- **Certifications : ✅ Encore mentionnées (Déclaré/Vérifié image)**
  - `02e` : `certified by FDA, HACCP, and ISO9001` (texte fiche produit) + image `ISO/SGS CERTIFICATIONS` + `Capacity` sur `02f`. Statut = **Déclaré** (image certificat MIC, pas de n° PDF valide externe) — identique à CSV.
- **Adresse/tel : ✅ Inchangés**
  - `Mr. Albert Xu` + même adresse Nanhu Road + Shanghai Port proche. Aucun changement.
- **Note doublon : Unique - maison mère Fansheng (lien confirmé)**
  - Texte `02f` contient verbatim : `Suzhou Fansheng Plastic Manufacture Co. Ltd is only 15KMs away... Established in 1996... total investment USD 3,800,000` — preuve lien capitalistique #02 ↔ #09.
- **Alertes Auditor :** Site officiel `innopack.com` inaccessible le jour J (ModSecurity) : vérifier si domaine expiré / firewall Chine / changement domaine (`enlightening-plast.com` variant listée CSV non testée). Recommander test via VPN + WHOIS `innopack.com` vs année création. Ne pas exclure mais priorité secondaire jusqu'à ré-accès site officiel.

---

### 03 — Xingtai Xinbei Plastic Products Co., Ltd. (Xinbei Plastic Products Factory)
- **Statut : ✅ Vérifié 2026-10-24**
- **URLs re-extraites :**
  - Principal : `http://www.xbplasticbucket.com` → `03-primary.txt` (9 270c) + Liste : `http://www.xbplasticbucket.com/products_list/1189881017326063616-12-12.html` → `03c-xinbei-list.txt` (3 900c)
  - Secondaire : `https://xinbeiplastic.en.made-in-china.com` → `03b-secondary-MIC.txt` (14 602c)
  - Produit : `https://xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html` → `03d-xinbei-10L.txt` (20 713c)
  - About : `http://www.xbplasticbucket.com/about_us.html` → `03e-xinbei-about.txt` (1 598c)
- **Gamme 8-16L : ✅ Confirmée sur les deux sources**
  - Officiel `03c` : images + titres `9.5 Liter White Bucket`, `12 Liter White Bucket` (×2 variantes), `15 Liter White Bucket`, `16 Liter White Bucket` + `18 Liter Thickening Bucket`, `20 Liter White Bucket/Oil Bucket`. Pagination `< 1 2 3 >` visible.
  - MIC `03d` : `Food-Grade 10L Heavy-Duty Factory Direct Bulk Order Round Plastic Bucket` — `PP Material, FDA Certified Food Grade, 8,600 sqm facility, advanced machinery` + variantes `15L Round Bucket, 15L, 12L Customizable Bulk Order Low MOQ`.
  - CSV original `9.5L/12L/15L/16L/18L/20L` parfaitement retrouvé. URL fiche exacte : `http://www.xbplasticbucket.com/products_list/1189881017326063616-12-12.html` (liste) + `03d` (fiche 10L MIC).
- **Surface/machines/effectif : ✅ Cohérent**
  - Original : 10 000m2, 30 ans d'activité.
  - Re-extrait MIC : `Xinbei Plastic Products Factory has been engaged in the plastic industry for over 30 years... located in Xingtai City... covers an area of 8,600 square meters and is equipped with the most advanced large-scale barrel production equipment in China, as well as screen printing, heat transfer printing, and in-mold labeling equipment` + `over thirty specifications injection-molded barrels 1L-35L`. Légère variance 8 600 vs 10 000m2 mais cohérent (arrondi). `Since establishment 2000` + `ISO9002:2000 standard model`.
  - Officiel : footer `Company Address: Chaozhuang village, Pingxiang Town, Xingtai City, Hebei Province`.
- **Certifications : ✅ Encore mentionnée (Déclaré)**
  - `FDA Certified Food Grade: Products meet strict FDA standards` sur `03d` + `ISO 9001, ISO 9000` sur company header `03b`. Statut **Déclaré** (pas de PDF certif n°).
- **Adresse/tel : ✅ Inchangés**
  - `Chaozhuang village Pingxiang Town Xingtai City Hebei` + `Tel:+8613683673744 WhatsApp:+8613683673744 E-mail:xinbei@hengliplasticbucket.com Wechat:13731067966` — identiques sur `03e` et `03b` Factory Address. Aucun changement.
- **Note doublon : Unique - Hebei** (confirmé, aucun autre Hebei dans liste)
- **Alertes Auditor :** Aucune. Fournisseur le plus stable de la vérification.

---

### 04 — Qingdao Rulyda Plastic Manufacture Co., Ltd.
- **Statut : ✅ Vérifié 2026-10-24 avec réserve**
- **URLs re-extraites :**
  - Principal : `https://www.rulydaplastic.com` → `04-primary.txt` (7 186c)
  - Secondaires : `https://rulydaplastic.en.made-in-china.com` → `04b-secondary-MIC.txt` (29 924c) + `https://rulydaplastic.en.made-in-china.com/product-list-8.html` → `04e-rulyda-MIC-list.txt` (13 418c)
  - Contact : `https://www.rulydaplastic.com/contact-us.html` → tentative 450c (page vide)
  - Test produits : `https://www.rulydaplastic.com/Product-List-Square-Plastic-Bucket.html` et `.../product/Square-Plastic-Bucket-3.html` → 450c vides (structure site dégradée)
- **Gamme 8-16L : ✅ Confirmée (homepage + MIC)**
  - Officiel homepage `04-primary.txt` : menu `Round Plastic Bucket, Square Plastic Bucket, Collapsible Pallet Box` + produits visibles `Raw Material 10L Capacity In Mould Labeling Transparent Square Plastic Bucket for Oil with Lid` + `15Litre Sticker White Plastic Pail In Square Shape for Water with White Lid and Handle` + header `200ml to 25L`. Ces deux fiches prouvent 10L + 15L toujours présents.
  - MIC `04e` : `Manufacturer/Factory & Trading Company, Plastic Pallet, Plastic Bucket...` + visuels `8L Custom Printed Square Clear Fuel Bucket, 10L IML Transparent Square Bucket` mentionnés CSV toujours catégorisés sous `Plastic Bucket` (product-list-8.html). CSV original `2L/3L/4L/5L/8L/10L/15L` inchangé.
  - **Réserve :** sous-pages produit détaillées renvoient page vide 450c — possible refonte site ou anti-bot. URL fiche exacte re-extraite = homepage `https://www.rulydaplastic.com/` (contient visuels 10L/15L) + MIC list `04e`.
- **Surface/machines/effectif : ✅ Cohérent**
  - Original : 2 usines 20 000m2, 85 machines injection jusqu'à 1500T.
  - Re-extrait homepage : `machines with the heaviest up to 1500 tons...` + `20000` (extrait `04-primary.txt:52` et `72`). MIC : `Factory Tour` images + `Manufacturer/Factory & Trading Company`, `ISO9001:2015` management certification. Cohérent.
- **Certifications : ✅ Inchangé**
  - `ISO9001:2015` sur MIC header + `Audited Supplier` + `Industry-leading Audited Factory`. Pas de FDA/EU spécifique — CSV disait `pas de certificat ISO public sur site officiel (non communiqué)` — confirmé : site officiel ne montre pas certificat, MIC montre ISO9001:2015. Statut **Déclaré** cohérent.
- **Adresse/tel : ✅ Inchangés**
  - `Add: A1 Building No.1388 Taifa road, Huangdao Zone, Qingdao, Shandong` + `Mobile/whatsApp/wechat: +86-13685326369 E-mail: alex@rulymm.com` — identiques extraits `04-primary.txt:245-249` + MIC `Qingdao, Shandong, China`.
- **Note doublon : Unique - Qingdao** — adresse distincte de #01 (Emeishan/Optics Valley) et #10 (générique) — pas de doublon.
- **Alertes Auditor :** Vérifier accessibilité sous-pages produit (possible blocage Cloudflare). Demander catalogue PDF 8-16L actualisé pour compenser site officiel dégradé.

---

### 05 — Zibo Yundu Plastic Products Co., Ltd. / Foshan Chengpin Technology Co., Ltd. (CP Bucket)
- **Statut : ✅ Vérifié 2026-10-24 (avec divergence secondaire)**
- **URLs re-extraites :**
  - Principal : `https://www.cpbucket.com` → `05-primary.txt` (12 232c) + Produit : `https://www.cpbucket.com/product.html` → `05c-cpbucket-product.txt` (9 604c) + About : `https://www.cpbucket.com/about-us.html` → `05d-cpbucket-about.txt` (16 955c) + Contact : `https://www.cpbucket.com/contact.html` → `05e-cpbucket-contact.txt` (2 965c)
  - Secondaire : `https://yunduplastic.en.made-in-china.com` → `05b-secondary-MIC.txt` (24 559c) — **contenu FIBC Big Bags, pas de seaux**
- **Gamme 8-16L : ✅ Partiellement confirmée (officiel OK, secondaire divergent)**
  - Officiel `05-primary.txt` + `05c` : catégories `Round/Oval/Rectangular/Square Plastic Buckets` + produits `Oval PP Bucket 16L Anti-Theft Child Lock For Laundry Powder`, `20L Plastic Pail WITH Gamma Seal`, `Emergency Storage Bucket 20L`, `5-Gallon Round PP Bucket Resealable Screw-Top` (18.9L), `Square Plastic Bucket 20L with Handle`. CSV original listait `5L Square/Rectangular, 10L Rectangular with Snap-On Lid, 20L Square` — **16L et 20L confirmés, 10L non retrouvé sous forme fiche exacte le 2026-10-24** (possible pagination produit non chargée via html2text JS).
  - Secondaire MIC `05b` : affiche désormais `FIBC PP Woven Bulk Big Ton Bag / Jumbo Bag, 96 employees, 4 sets wire drawing machines, 84 sets circular looms, 640 tons capacity monthly` — **aucun seau PP 8-16L** sur cette fiche. Divergence majeure vs CSV où `yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU...` listait seaux. Soit changement d'activité, soit groupe diversifié (sacs + seaux) avec showroom séparé.
- **Surface/machines/effectif : ✅ Cohérent (officiel)**
  - Original : Fondé 2005 enregistré 2018, 13 ans export 200 pays, SGS 97% pass rate.
  - Re-extrait `05d` : `Founded in 2005 and formally registered in 2018, standardized factory, full-automatic injection molding equipment, serving tens of thousands customers, sold to over 200 countries, SGS certified 100% new food-grade PP, UN certification drop test 1.8m`. `Located at No.4 Jinxiang 1st Road, Southwest Street, Sanshui District, Foshan City, Guangdong Province.` Identique.
- **Certifications : ✅ Encore mentionnées**
  - `All PP plastic buckets are made from 100% new food-grade PP, certified by SGS, conforme FDA & EU food-contact, UN certification for hazardous chemicals` — inchangé. Statut **Déclaré** (pas de PDF n°).
- **Adresse/tel : ✅ Inchangés**
  - `No.4 Jinxiang 1st Road, Southwest Street, Sanshui District, Foshan City, China + Phone/WhatsApp: +86 18316967024 Email: sales@cpbucket.com Contact Person Mr Fan` — identiques sur `05-primary` et `05d`.
- **Note doublon : Unique - double identité légale vérifiée (Zibo Yundu = Foshan Chengpin)** — confirmée, pas de nouveau doublon.
- **Alertes Auditor :** Clarifier divergence secondaire MIC : `yunduplastic.en.made-in-china.com` ne montre plus de seaux mais des FIBC bags (96 employés). Vérifier si Zibo Yundu a deux entités (sacs vs seaux) ou si fiche MIC obsolète/piratée. Recommander demander nouveau lien MIC buckets `ydplastic.en.alibaba.com` ou `ydbags.com` listés CSV mais non testés 2026-10-24.

---

### 06 — Zhejiang Yunde Plastic Industry Technology Co., Ltd.
- **Statut : ✅ Vérifié 2026-10-24**
- **URLs re-extraites :**
  - Principal : `https://www.yundeplastic.com` → `06-primary.txt` (9 384c) + Catégorie : `https://www.yundeplastic.com/product/pp-plastic-bucket/` → `06c-yunde-bucketlist.txt` (14 689c)
  - Détail produits : `.../10l-american-style-durable-pp-bucket-with-lid.html` → `06d` (221c 404) + `.../16l-american-style-pp-bucket-with-lid-for-storing-liquids.html` → `06e` (221c 404) — fiches détail en 404 (refonte site)
  - Secondaire : `http://www.zjyunde.cn/en/` → `06b-secondary-zjyunde.txt` (6 201c) + Liste : `http://www.zjyunde.cn/en/list/?5_1.html` → `06g-zjyunde-list.txt` (2 974c) + About : `http://www.zjyunde.cn/en/about/?142.html` → `06h-zjyunde-about.txt` (2 691c)
- **Gamme 8-16L : ✅ Confirmée (via listings, malgré 404 détail)**
  - Principal `06c` : `PP Plastic Bucket OEM/ODM (17)` — liste `1L,2L,3L American Style, 5L American/European, **10L American Style Durable PP Bucket with Lid**, **16L American Style PP Bucket with Lid for Storing Liquids**, 18L European with Spout, 20L American (Yellow/Gray/Blue/Milky), 25L Spiral, 35L Food Grade`. Images `_dsc5012-255.png` 16L + `_dsc4866-123.png` 10L confirmées.
  - Secondaire `06g` : `PP bucket series` + menu `10L` + adresse `No.2345 Fulong Road Cixi Binhai EDZ` + `2L/3L/5L` listés. CSV original `1L/2L/3L/5L/10L/16L/18L/20L/25L/35L` parfaitement retrouvé.
  - URL fiche exacte re-extraite : `https://www.yundeplastic.com/product/pp-plastic-bucket/` (catégorie avec 10L/16L) — fiches détail individuelles en 404 le jour J (alerte technique, pas produit manquant).
- **Surface/machines/effectif : ✅ Cohérent**
  - Original : créé 2014-12-31, 30 acres 20 000m2, 30+ lignes, fluorination online avancée.
  - Re-extrait `06h` + `06-primary` : `Established Dec 31,2014, total investment 8000 million yuan, total area 30 acres, factory area 20,000 sqm, more than 30 mature production lines, produces 100,000 sets per day, fluorinated HDPE etc.` + `No.2345 Fulong Road Cixi Binhai Economic Development Zone Ningbo Zhejiang + Tel:0574-89085869 Mobile:15058286990/15957492932/18058281908 + Email YDlisa@yundeplastic.com`. Identique.
- **Certifications : ✅ Encore mentionnées**
  - `ISO9001 (certificat image iso9001-en.jpg), Honor certificates, National Food Safety Standard Test Report, advanced fluorination lab` — inchangé. Statut **Déclaré** (image).
- **Adresse/tel : ✅ Inchangés**
  - `No.2345 Fulong Road + 588 Songpu Second Road Cixi Binhai EDZ Building 1` + tous mobiles OK.
- **Note doublon : Unique - Ningbo/Cixi** (confirmé)
- **Alertes Auditor :** Fiches détail 10L/16L en 404 — demander URLs corrigées ou catalogue PDF. Vérifier si migration site `yundeplastic.com` → nouvelle structure `/product/pp-plastic-bucket/...` cassée.

---

### 07 — Taizhou Bright Plastic Co., Ltd.
- **Statut : ❌ Non vérifié 2026-10-24 — Showroom supprimé**
- **URLs re-extraites :**
  - Principal : `https://tzbright.en.made-in-china.com` → `07-primary.txt` (2 029c) — **error `We are sorry that this showroom doesn't exist.`**
  - Variante : `https://tzbright.en.made-in-china.com/product-list-13.html` → `07c-bright-list.txt` (2 029c même error) + `https://tzbright.en.made-in-china.com/company-Taizhou-Bright-Plastic-Co-Ltd--info.html` → `07d` (2 029c error)
  - Secondaire : `https://plasticchina.en.alibaba.com` → `07b-secondary-Alibaba.txt` (2c vide, blocked) + `https://suppliers.alibaba.com/taizhou-bright-plastic-co-ltd_2027929796` (non testé, probablement même)
  - Test raw : `curl tzbright` raw HTML confirme `The information is not available right now` + `This page will be redirected... in 5 seconds` (Focus Technology 1998-2026)
- **Gamme 8-16L : ❌ Non prouvée**
  - CSV original listait `Bottle Bucket Broom & Dustpan, sanitation trash cans, pet supplies, sharp containers` — déjà hors spec PP 8-16L food-grade (pas de fiche 10L détaillée, seulement bucket référencé product-list-13 plastique quotidien).
  - Re-extrait : aucune fiche bucket accessible, aucun 5L/10L/12L/16L. Panjiva historique 53 shipments non re-vérifiable 2026-10-24.
- **Surface/machines/effectif : Non communiqué** — inchangé, mais impossible à confirmer.
- **Certifications : Non communiqué** — inchangé, pas de certif alimentaire spécifique publié.
- **Adresse/tel : Non vérifiable**
  - Original : `Taizhou Economic Development Zone 318000 Taizhou City Zhejiang` via Panjiva. Aucune adresse/tel re-extraite (showroom deleted, pas de footer).
- **Note doublon : Unique - Taizhou (attention gamme <5L IML seulement)** — CSV notait déjà `ne contient pas gamme 10L détaillée`.
- **Alertes Auditor :** **À exclure** pour sourcing PP 8-16L. Showroom MIC supprimé = signal risque (fermeture, non-paiement adhésion, ou fraude). Vérifier via `cnverify.com/company/Taizhou-Bright-Plastic-Co-Ltd` (créé 2016-03-07) si encore active au registre chinois. Ne pas contacter sans réactivation preuve.

---

### 08 — Taizhou Huangyan Jinjie Plastic Factory (Huangyan Gongjie Plastic Co., Ltd.)
- **Statut : ✅ Vérifié existence usine mais ⚠️ Hors spécification 8-16L confirmée**
- **URLs re-extraites :**
  - Principal : `https://www.hy-gj.com` → `08-primary.txt` (5 077c)
  - Produit : `https://www.hy-gj.com/product/plastic-bucket/` → `08c-hy-plastic-bucket.txt` (3 562c) + Page 2 → `08e-hy-bucket-p2.txt` (2 233c)
  - About : `https://www.hy-gj.com/about/` → `08d-hy-about.txt` (4 923c)
  - Contact : `https://www.hy-gj.com/contact/` → `08f-hy-contact.txt` (2 448c)
  - Secondaire : `https://jinjieplastic.en.alibaba.com` → `08b-secondary-Alibaba.txt` (2c blocked)
- **Gamme 8-16L : ❌ Hors spec — max 4.2L IML**
  - Officiel `08c` : `GJ-365 540ml Plastic Container`, `GJ-366 1.3L Plastic Bucket`, `GJ-367 1.85L`, `GJ-368 2.7L`, `GJ-369 4.2L` (×5 variantes). Page 2 vide hors pagination. Raw grep `https://www.hy-gj.com/product/plastic-bucket/` révèle tailles `2L/3L/7L/85L` parasites mais bucket listing réel max **4.2L**.
  - CSV original citait déjà `GJ-365 540ml → GJ-369 4.2L` et notait `spécialiste IML` — confirmé. Aucune fiche 10L/12L/15L/16L sur site officiel. Fiche Alibaba non testable mais CSV disait `gamme plus large via Alibaba jusqu'à seaux alimentaires IML` — non vérifiable 2026-10-24.
  - **Conclusion : Hors spécification PP 8-16L** — conserver uniquement si besoin IML <5L ou lunch box/popcorn bucket.
- **Surface/machines/effectif : ✅ Cohérent (non chiffré m²)**
  - Original : non chiffré surface, BSCI/FDA/EU/SGS.
  - Re-extrait `08d` : `Injection Machines`, `100% food-grade virgin PP, SGS-certified, fully comply FDA & EU`, `BSCI Social Audit Report + FDA RAW MATERIAL REPORT` images + `Mould workshop`. Adresse `Nancheng Industrial Zone, Huangyan, Taizhou City, Zhejiang` + `Tel:+86-576-84180810` inchangés. Surface m² toujours **Non communiqué**.
- **Certifications : ✅ Encore mentionnées (Déclaré)**
  - `Certified Quality: strictly certified to BSCI, FDA, EU standards` + images `BSCI Social Audit Report` + `FDA RAW MATERIAL REPORT` + `National Food Safety Standard Test Report` — identique CSV. Statut **Déclaré** (images rapports, pas de n° certif valide externe).
- **Adresse/tel : ✅ Inchangés**
  - `Nancheng Industrial Zone Huangyan Taizhou Zhejiang +86-576-84180810 wanna@hy-gj.com` — confirmés `08-primary` footer + `08f`.
- **Note doublon : Unique - spécialiste IML** — confirmé, pas de lien avec #07 même ville mais adresses distinctes (Economic Development Zone vs Nancheng Industrial Zone).
- **Alertes Auditor :** Marquer `Hors spec 8-16L - conservé pour info IML <5L`. Ne pas scorer pour PP 8-16L.

---

### 09 — Suzhou Fansheng Plastic Manufacture Co., Ltd.
- **Statut : ✅ Vérifié 2026-10-24**
- **URLs re-extraites :**
  - Principal : `https://innopackaging.en.made-in-china.com` → `09-primary.txt` (11 947c) = MIC showroom Fansheng
  - Company : `https://innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html` → `09c-fansheng-company.txt` (12 201c)
  - Produit : `https://innopackaging.en.made-in-china.com/product/cSXEYsJKhmay/China-10L-PP-Food-Grade-Rectangle-Bucket-with-Lid.html` → `09d-fansheng-10L.txt` (24 806c)
  - Secondaire : `https://fsplastic.en.alibaba.com` → `09b-secondary-Alibaba.txt` (2c blocked)
- **Gamme 8-16L : ✅ Confirmée**
  - Company `09c` : catégories `21L-30L plastic bucket / 16L-20L / 11L-15L / 6L-10L / 1L-5L Others` + exemples `Heavy Duty 3.5 Gallon (13L) Plastic Container/Bucket/Pail with Handle and Lid`, `Australia Hot Sale Square 10L with Cover Food Grade Seafood Bucket Pail`, `5 Liter Custom Color Round Tin Can` etc.
  - Produit `09d` : `10L PP Food Grade Rectangle Bucket with Lid` — description `Made from PP/PE, custom printing silkscreen/heat transfer, ISO9001 HACCP SGS, OEM/ODM, supplier for PPG and Meguiar's` + spec `10L rectangle bucket` + certificat `ISO9001 HACCP SGS` badge.
  - CSV original `150ml-30L, 10L Square/Rectangle/Round, 13L Heavy Duty` retrouvé.
  - URL fiche exacte re-extraite : `09d` (cSXEYsJKhmay) — preuve 10L.
- **Surface/machines/effectif : ✅ Cohérent**
  - Original : établi 1998-04-22, investissement USD 3.8M, Staff 63.
  - Re-extrait : `Year of Establishment: 1998-04-22` + `Located near Taihu Lake Dongshan exit Suzhou Roundcity Expressway 15KM centre Suzhou, Established in 1996 (texte narratif variant) ... total investment more than USD 3,800,000` + `Address: Changan Road 288, Xukou Town, Wuzhong District, Suzhou`. Cohérent avec CSV (1998 vs 1996 narratif déjà présent).
- **Certifications : ✅ Encore mentionnées (Déclaré)**
  - `ISO/SGS CERTIFICATIONS images` sur `09c` + `ISO 9001, HACCP, SGS` sur fiche produit + `Audited Supplier BV` — identique.
- **Adresse/tel : ✅ Inchangés**
  - `Changan Road 288 Xukou Town Wuzhong District Suzhou Jiangsu` + `Near Taihu Lake Dongshan exit 15KM centre Suzhou`. Tel non public mais inquiry MIC.
- **Note doublon : Unique - à distinguer d'Innovation (filiale)** — **Confirmé groupe lié** : `09` est maison mère, `02` est filiale. Textes croisés : Innovation page mentionne Fansheng establishment 1996/USD 3.8M.
- **Alertes Auditor :** Aucune — fournisseur référence Suzhou, scorer favorable.

---

### 10 — Qingdao Hivic Plastic Manufacture Co., Ltd.
- **Statut : ⚠️ Non vérifié (gamme 8-16L non prouvée) — usine palette vérifiée**
- **URLs re-extraites :**
  - Principal : `https://hivicplastic.en.made-in-china.com` → `10-primary.txt` (35 664c)
  - Liste : `https://hivicplastic.en.made-in-china.com/productList` → `10d-hivic-list.txt` (12 991c) + `https://hivicplastic.en.made-in-china.com/productGroup-p-1.html` → `10f` (43c vide)
  - Company : `https://hivicplastic.en.made-in-china.com/company-Qingdao-Hivic-Plastic-Manufacture-Co-Ltd--info.html` → `10e-hivic-company.txt` (10 144c)
  - Secondaire : `https://hivic.en.alibaba.com` → `10b` (2c blocked) + `https://hivic.com` → `10c-extra-hiviccom.txt` (2c lander `/lander`)
- **Gamme 8-16L : ❌ Non prouvée**
  - Officiel `10-primary` + `10d` : `Main Products: Plastic Pallet, Plastic Bucket, Plastic Pallet Box, Plastic Tray, Plastic Packaging Container, Nine Feet Plastic Pallet...` + focus `Professional Plastic Pallet Factory, Established in 2017, special feeder recycled material, nestable 1200×1000mm HDPE Recycled Euro Heavy Duty` — **activité principale = palettes plastique**.
  - Bucket trouvé : `Food Grade Plastic Bucket Portable Storage Bucket Clear Pail Kids Toy Plastic Barrel Portable Chemical Bucket` (transparent `10d` 385-386) — **sans capacité 8L/10L/12L/15L/16L spécifiée**. Aucune fiche `8L Custom Printed Square Clear Fuel Bucket` ou `10L IML Transparent` comme Rulyda ; pas de table litres.
  - CSV original disait `Plastic Pallet/Bukkit/Box/Crates/Waste Bin, Food Grade Clear Bucket` — déjà vague. Re-extraction confirme que bucket est **catégorie secondaire non détaillée**.
- **Surface/machines/effectif : ✅ Cohérent mais focus palette**
  - Original : établi 2017 (Made-in-China) / 2008 divergence moldso.com + trading staff 2.
  - Re-extrait : `Established in 2017, Qingdao Hivic Plastic Manufacture Co.,Ltd. is a ... production of plastic parts and injection molds. We are located in Qingdao` (×2) + `Main Products` list + `Professional Plastic Pallet Factory`. Pas de m² ou machines détaillés pour seaux. Trading staff non re-extrait mais `2` historique plausible.
- **Certifications : ⚠️ Non communiqué inchangé**
  - `All products conform international quality standards, well-equipped facilities excellent quality control` — générique, pas de FDA/EU/ISO n° — identique CSV `pas de certificat spécifique FDA/ISO publié`.
- **Adresse/tel : ⚠️ Générique inchangé**
  - `Address: Qingdao, Shandong, China` (sans rue/numéro) + `Qingdao Shandong China siège MIC` — même imprécision que CSV. Pas de tel public re-extrait (inquiry only).
- **Note doublon : Unique - Qingdao (distinct de Rulyda)** — confirmé : #10 générique Qingdao vs #04 Taifa Road 1388 vs #01 Emeishan/ Optics Valley — pas de lien adresse/tel.
- **Alertes Auditor :** **Ne pas retenir pour PP 8-16L food-grade** sans preuve capacité. Demander catalogue bucket PDF avec litres exacts ou exclure et conserver uniquement si besoin palettes. Vérifier divergence date création 2008 vs 2017.

---

## Doublons & Sociétés Liées — Analyse croisée 2026-10-24

### Doublons confirmés : AUCUN doublon strict (même raison sociale + même adresse/tel) détecté via `rg` sur `/tmp/reverif-2026-10-24/*.txt`
- **Qingdao cluster (3 entités) :**
  - #01 Enlightening : `Optics Valley Software Park / 396 Emeishan Road Huangdao` + `+86 15192793205 / sales43@enlighteningplast.com`
  - #04 Rulyda : `A1 Building No.1388 Taifa Road Huangdao` + `+86-13685326369 / alex@rulymm.com`
  - #10 Hivic : `Qingdao, Shandong, China` générique + inquiry only
  - **Conclusion : 3 adresses distinctes, 3 tels distincts, 3 raison sociales distinctes → Unique confirmé, pas de doublon.**

- **Suzhou cluster (2 entités) :**
  - #02 Innovation : `Floor 10 Tianmao East Build 71 Nanhu Road Wuzhong` + `Mr Albert Xu` + `6 trading staff`
  - #09 Fansheng : `Changan Road 288 Xukou Town Wuzhong` + `1998-04-22 / USD 3.8M`
  - **Conclusion : Adresses distinctes mais lien capitalistique prouvé (texte Fansheng inside Innovation company page + même géographie Roundcity Expressway Dongshan exit / Taihu Lake).** Statut = `Unique - groupe lié à #Y` (conserver 2 entrées comme CSV original le notait).

- **Zibo/Foshan cluster :**
  - #05 Zibo Yundu = Foshan Chengpin Technology (double identité légale) — `No.4 Jinxiang 1st Rd Sanshui Foshan + Mr Fan +86 18316967024` vs historique Zibo Shandong — **même groupe, même site cpbucket.com** — compter 1 entité (déjà noté `Unique - double identité légale vérifiée`).

- **Taizhou cluster :**
  - #07 Bright : `Taizhou Economic Development Zone 318000` (showroom deleted)
  - #08 Jinjie : `Nancheng Industrial Zone Huangyan Taizhou` + `+86-576-84180810`
  - **Conclusion : Adresses distinctes, pas de doublon.**

### Sociétés liées infirmées
- Aucun lien Qingdao ↔ Suzhou, Hebei ↔ autres détecté.
- `rg -i "same phone|same address|M. Fan|cnbucket"` sur extractions : seul `M. Fan` apparaît sur #05 uniquement.

---

## Produits Hors Spec & Alertes Qualité

| ID | Produit déclaré CSV | Vérification 2026-10-24 | Décision |
|---|---|---|---|
| 07 Taizhou Bright | Bucket plastique quotidien divers | Showroom supprimé, aucune fiche bucket, focus historique trash cans/pet supplies <5L | **Hors spec confirmé + Non vérifié → Exclure** |
| 08 Huangyan Jinjie | IML Bucket 540ml-4.2L | Site officiel liste uniquement 540ml-4.2L IML, max 4.2L → **<5L IML seulement** | **Hors spec confirmé → Conserver uniquement pour info IML** |
| 10 Qingdao Hivic | Plastic Bucket vague + palettes | Site focus palettes 1200×1000mm, bucket générique sans capacité 8-16L | **Non prouvé 8-16L → Exclure pour PP 8-16L** |
| 05 Zibo Yundu MIC secondaire | Seaux PP 8-35L | Secondaire MIC affiche FIBC Big Bags 640T/mo, plus de seaux | **Divergence → Alerte Auditor, vérifier nouveau MIC** |

**Taux hors spec : 3/10 (30%) — conforme à l'alerte initiale mission `Taizhou Bright <5L IML seulement`.**

---

## Recommandations pour l'Auditor (ne pas modifier CSV original)

1. **CSV original intact :** aucune modification effectuée. Findings ci-dessus à intégrer dans `fabricants_seaux_PP_8-16L_Chine-AUDITE.csv` par l'Auditor via skill `supplier-qualification` (scores /100).
2. **Top à qualifier en prioritaire :** #03 Xinbei (le plus stable), #01 Enlightening (malgré variante adresse), #04 Rulyda (malgré sous-pages vides), #06 Yunde (malgré 404 détail), #09 Fansheng + #02 Innovation (groupe Suzhou) → 6 entités cœur 8-16L.
3. **Actions Auditor :**
   - Vérifier WHOIS `enlighteningplast.com` vs `cnbucket.com` vs date création Icnplast (Qingdao) — cohérence Optics Valley adresse.
   - Tester `innopack.com` via VPN Chine + whois + demander nouveau domaine si bloqué ModSecurity.
   - Demander à #04 Rulyda catalogue PDF 8L/10L/15L + preuve 20 000m2 / 85 machines 1500T (photos usine datées).
   - Clarifier #05 secondaire MIC : exiger lien MIC buckets actif ou retirer cette source, conserver uniquement `cpbucket.com`.
   - Pour #06 exiger URLs fiches détail corrigées (10L/16L) ou fiche technique PDF.
   - Exclure #07 Bright (showroom deleted) et #08 Jinjie (Hors spec <5L) et #10 Hivic (non prouvé) du shortlist 8-16L ; les conserver dans onglet `Hors spec / Palettes / IML`.
4. **Score provisoire Hunter (avant qualification) :**
   - Vérifié stable : #03 (90/100 potentiel), #01 (85), #06 (80), #09 (85), #04 (75 réserve), #05 (75 divergence)
   - Partiel : #02 (65 — site down)
   - Non vérifié / Hors spec : #07 (20), #08 (40 hors spec), #10 (30)

---

## Annexe — URLs sources re-vérifiées 2026-10-24 (≥2 par fournisseur, extraction html2text datée)

**01** `https://enlighteningplast.com` (31 616c) | `https://enlighteningplast.com/plastic-buckets/` (22 650c) | `https://cnbucket.com` (16 939c) — Vérifié 2026-10-24
**02** `https://www.innopack.com` (153c Not Acceptable) | `https://sz-innovation.en.made-in-china.com` (12 517c) | `https://sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html` (30 897c) | `https://sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html` (13 054c) — Vérifié partiel
**03** `http://www.xbplasticbucket.com` (9 270c) | `http://www.xbplasticbucket.com/products_list/1189881017326063616-12-12.html` (3 900c) | `https://xinbeiplastic.en.made-in-china.com` (14 602c) | `https://xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html` (20 713c) — Vérifié
**04** `https://www.rulydaplastic.com` (7 186c) | `https://rulydaplastic.en.made-in-china.com` (29 924c) | `https://rulydaplastic.en.made-in-china.com/product-list-8.html` (13 418c) — Vérifié
**05** `https://www.cpbucket.com` (12 232c) | `https://www.cpbucket.com/product.html` (9 604c) | `https://www.cpbucket.com/about-us.html` (16 955c) | `https://yunduplastic.en.made-in-china.com` (24 559c FIBC) — Vérifié (divergence notée)
**06** `https://www.yundeplastic.com` (9 384c) | `https://www.yundeplastic.com/product/pp-plastic-bucket/` (14 689c) | `http://www.zjyunde.cn/en/` (6 201c) | `http://www.zjyunde.cn/en/list/?5_1.html` (2 974c) — Vérifié
**07** `https://tzbright.en.made-in-china.com` (2 029c error showroom doesn't exist) | `https://plasticchina.en.alibaba.com` (2c blocked) | raw check `https://tzbright.en.made-in-china.com/product-list-13.html` (32 827c raw error) — Non vérifié
**08** `https://www.hy-gj.com` (5 077c) | `https://www.hy-gj.com/product/plastic-bucket/` (3 562c) | `https://www.hy-gj.com/about/` (4 923c) — Vérifié existence mais Hors spec (max 4.2L)
**09** `https://innopackaging.en.made-in-china.com` (11 947c) | `https://innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html` (12 201c) | `https://innopackaging.en.made-in-china.com/product/cSXEYsJKhmay/China-10L-PP-Food-Grade-Rectangle-Bucket-with-Lid.html` (24 806c) — Vérifié
**10** `https://hivicplastic.en.made-in-china.com` (35 664c) | `https://hivicplastic.en.made-in-china.com/productList` (12 991c) | `https://hivicplastic.en.made-in-china.com/company-Qingdao-Hivic-Plastic-Manufacture-Co-Ltd--info.html` (10 144c) — Non vérifié gamme 8-16L

*Toutes extractions via `curl -sL -A "Mozilla/5.0" | uvx html2text --ignore-links` datées 2026-10-24 et archivées `/tmp/reverif-2026-10-24/*.txt` (à transférer vers `/data/extractions/` si besoin).*

---

**Livrable Hunter terminé — CSV original non modifié, findings prêts pour Auditor.** 
*Contact vérifications : utiliser uniquement données publiques ci-dessus. Ne pas envoyer message fournisseur sans accord manager.*

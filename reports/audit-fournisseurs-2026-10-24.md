# Audit Fournisseurs — Seaux PP 8-16L Chine — 2026-10-24

**Auditeur :** Supplier Auditor (SOURCING LAB AI) — Contrôle indépendant du fichier Hunter  
**Fichier source :** `data/fabricants_seaux_PP_8-16L_Chine-ORIGINAL.csv` (10 fournisseurs)  
**Fichier corrigé :** `reports/fabricants-corrigé-2026-10-24.csv` (séparateur `;`, UTF-8-SIG) + `fabricants-corrigé-2026-10-24.xlsx`  
**Méthode :** Skill `supplier-qualification` — 7 piliers /100 (P1 15 + P2 20 + P3 15 + P4 15 + P5 15 + P6 10 + P7 10)  
**Extraction :** `curl -L` + `html2text` datée **2026-10-24** — 28 URLs vérifiées (HTTP 200/404/403 notés)  
**Règle d'or :** ZÉRO invention — chaque point cite URL exacte. Statuts : `Vérifié` / `Déclaré` / `Non vérifié` / `Contradictoire`

---

## 1) Tableau des scores — Vue d'ensemble

| # | Fabricant | Score /100 | Niveau | P1<br>/15 | P2<br>/20 | P3<br>/15 | P4<br>/15 | P5<br>/15 | P6<br>/10 | P7<br>/10 | Statut Go/No-Go |
|---|-----------|------------|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------------|
| **6** | **Zhejiang Yunde Plastic Industry Technology Co., Ltd.** | **76** | 🟢 Qualifié | 14 Vérifié | 16 Vérifié | 15 Vérifié | 14 Vérifié | 8 Déclaré | 2 Non vérifié | 7 Vérifié | **Go RFQ prioritaire** |
| **1** | **Enlightening Plast Co., Ltd. (Qingdao Icnplast)** | **73** | 🟢 Qualifié | 12 Vérifié | 16 Vérifié | 15 Vérifié | 11 Vérifié | 5 Déclaré | 4 Déclaré | 10 Vérifié | **Go RFQ** |
| **4** | **Qingdao Rulyda Plastic Manufacture Co., Ltd.** | **73** | 🟢 Qualifié | 13 Vérifié | 17 Vérifié | 15 Vérifié | 11 Vérifié | 4 Déclaré | 3 Déclaré | 10 Vérifié | **Go RFQ** |
| **3** | **Xingtai Xinbei Plastic Products Co., Ltd.** | **72** | 🟢 Qualifié | 11 Vérifié | 13 Vérifié | 15 Vérifié | 11 Vérifié | 5 Déclaré | 7 Vérifié | 10 Vérifié | **Go RFQ** |
| **5** | **Zibo Yundu / Foshan Chengpin (CP Bucket)** | **68** | 🟠 À compléter | 9 Contradictoire | 14 Déclaré | 12 Vérifié | 13 Vérifié | 5 Déclaré | 5 Déclaré | 10 Vérifié | **Go conditionnel** |
| **9** | **Suzhou Fansheng Plastic Manufacture Co., Ltd.** | **64** | 🟠 À compléter | 14 Vérifié | 15 Vérifié | 10 Déclaré | 10 Vérifié | 6 Déclaré | 5 Déclaré | 4 Déclaré | **Go groupé avec #2** |
| **2** | **Suzhou Innovation Packaging Materials Co., Ltd.** | **57** | 🟠 À compléter | 10 Déclaré | 11 Déclaré | 10 Déclaré | 10 Déclaré | 3 Déclaré | 6 Déclaré | 7 Vérifié | **Fusionner avec #9** |
| **8** | **Taizhou Huangyan Jinjie Plastic Factory** | **50** | 🟠 À compléter | 12 Vérifié | 10 Vérifié | **0** Hors spec | 9 Vérifié | **11** Déclaré | 1 Non vérifié | 7 Vérifié | **No-Go CDC 8-16L** |
| **10** | **Qingdao Hivic Plastic Manufacture Co., Ltd.** | **31** | 🔴 Non qualifié | 5 Contradictoire | 6 Déclaré | 5 Non vérifié | 6 Déclaré | 1 Déclaré | 4 Déclaré | 4 Déclaré | **No-Go remplacer** |
| **7** | **Taizhou Bright Plastic Co., Ltd.** | **15** | 🔴 Non qualifié | 7 Déclaré | 5 Déclaré | **0** Hors spec | 3 Déclaré | 0 Non vérifié | 0 Non vérifié | 0 Non vérifié | **No-Go remplacer** |

> **Lecture :** 4 qualifiés (Go), 3 à compléter (Go conditionnel), 1 hors-spec technique mais certifié, 2 non qualifiés à remplacer.  
> **Entités indépendantes réelles : 8** (pas 10) — voir §3 Entreprises liées.

---

## 2) Détail 7 piliers par fournisseur

### #1 — Enlightening Plast Co., Ltd. (Qingdao Icnplast) — **73/100 🟢 Qualifié**

| Pilier | Score | Statut | Justification | URLs justificatives |
|--------|-------|--------|---------------|---------------------|
| **P1 Identification** | 12/15 | Vérifié | Raison sociale triple (Enlightening Plast / Qingdao Icnplast / Enlightening Pallet Industry) + 2 adresses usines précises : 396 Emeishan Rd Huangdao Qingdao + 339 Huixian Rd Jiading Shanghai (contact-us) + année 2005 (`We Are The Leading Plastic Bucket Manufacturers Since 2005` sur cnbucket.com/factory). Multi-site non consolidé → -3. | [enlighteningplast.com/contact-us/](https://enlighteningplast.com/contact-us/) ; [cnbucket.com/plastic-buckets-factory/](https://cnbucket.com/plastic-buckets-factory/) |
| **P2 Activité industrielle** | 16/20 | Vérifié | Photos usine + vidéo YouTube `lCZXlWPV11U` embed + 2 usines + machines injection globales + Audited Supplier MIC. Surface exacte non chiffrée → -4. | [enlighteningplast.com/plastic-buckets/](https://enlighteningplast.com/plastic-buckets/) ; [cnbucket.com/plastic-buckets-factory/](https://cnbucket.com/plastic-buckets-factory/) |
| **P3 Conformité 8-16L** | 15/15 | Vérifié | **Site officiel** : 10L Food Grade Round Plastic Bucket ([enlighteningplast.com/plastic-bucket/10l-bucket/](https://enlighteningplast.com/plastic-bucket/10l-bucket/)) + 18.93L PP Bucket Twist-on Lid + gamme 1-30L. 8-16L couvert avec preuve officielle. | [enlighteningplast.com/plastic-buckets/](https://enlighteningplast.com/plastic-buckets/) ; [enlighteningplast.com/plastic-bucket/10l-bucket/](https://enlighteningplast.com/plastic-bucket/10l-bucket/) |
| **P4 Capacités** | 11/15 | Vérifié | Injection molding + HDPE/PP/biodégradable + OEM/ODM Bulk Supply (15 Products) + export global (leading technologies). Capacité pcs/jour non chiffrée → -4. | [enlighteningplast.com/plastic-buckets/](https://enlighteningplast.com/plastic-buckets/) |
| **P5 Certifications** | 5/15 | Déclaré | FDA 21 CFR 177.1520 + EU 10/2011 + BPA-free + UN + ISO 9001 (CERTIFICATIONS + contact-us) **tous en texte sans PDF/numéro/validité/organisme**. Aucun document sourçable → Déclaré 1pt×5. | [enlighteningplast.com/contact-us/](https://enlighteningplast.com/contact-us/) ; [cnbucket.com/plastic-buckets-factory/](https://cnbucket.com/plastic-buckets-factory/) |
| **P6 Commercial** | 4/10 | Déclaré | MOQ `MOQs vary by product` vague (non chiffré) + FOB Qingdao/Shanghai implicite + délai non publié. OEM/ODM contact vendeur = 1pt. | [enlighteningplast.com/contact-us/](https://enlighteningplast.com/contact-us/) |
| **P7 Sources** | 10/10 | Vérifié | 3 URLs distinctes : enlighteningplast.com + cnbucket.com + contact-us + extraction datée 2026-10-24. Excellent. | [enlighteningplast.com/plastic-buckets/](https://enlighteningplast.com/plastic-buckets/) ; [cnbucket.com/plastic-buckets-factory/](https://cnbucket.com/plastic-buckets-factory/) ; [enlighteningplast.com/contact-us/](https://enlighteningplast.com/contact-us/) |

**Recommandation : Go RFQ prioritaire #2. Demander dossier certifs complet (SGS/Intertek + ISO PDF) + grille MOQ.**

---

### #2 — Suzhou Innovation Packaging Materials Co., Ltd. — **57/100 🟠 À compléter**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 10/15 | Déclaré | Adresse Floor 10 Tianmao East Build 71 Nanhu Rd Wuzhong = **bureau**, pas usine (vraie usine = Fansheng Changan Rd 288 Xukou). Année 2013-07 (investi par Fansheng) sourcée fiche produit. Filiale Fansheng → confusion juridique -5. | [sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html](https://sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html) ; [sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html](https://sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html) |
| **P2** | 11/20 | Déclaré | BV Audited MIC-ASR244050 + Diamond 2019 + photos усine MIC + Production Machines. Mais photos = usine Fansheng (maison mère), pas propre → Déclaré. Surface/effectif non chiffrés. | [sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html](https://sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html) |
| **P3** | 10/15 | Déclaré | 10L/15L prouvés **uniquement sur MIC** (10L Food Grade Printed Bucket + variantes 7.5L/15L). Site officiel [innopack.com](https://www.innopack.com) vide/timeout le 2026-10-24 → marketplace seul = 10. | [sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html](https://sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html) |
| **P4** | 10/15 | Déclaré | OEM/ODM IML/Silkscreen/Heat Transfer + PP/PE/metal bucket + FOB/CIF/CFR/EXW. Export Year vide. | Même URLs |
| **P5** | 3/15 | Déclaré | `certified by FDA HACCP ISO9001` = 1 phrase marketing sur fiche produit sans document. Logo `Certificates` vide sur company page. → 3×1=3 Déclaré. | [sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html](https://sz-innovation.en.made-in-china.com/product/WspQmelxaMVh/China-10L-Food-Grade-Printed-Plastic-Bucket-Pail-with-Lid-and-Handle.html) |
| **P6** | 6/10 | Déclaré | MOQ 1000 PCS chiffré (3pts) + FOB/CIF/CFR/EXW (2pts) + OEM 1pt. Délai/paiement non publiés. | Même URLs |
| **P7** | 7/10 | Vérifié | 2 URLs MIC + extraction datée. innopack.com inaccessible → Bon 7 (pas officiel). | [sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html](https://sz-innovation.en.made-in-china.com/company-Suzhou-Innovation-Packaging-Materials-Co-Ltd-.html) |

**Recommandation : Fusionner avec #9 (même groupe Innopack). Go si prix groupé, exiger BV Report ASR244050 + PDF FDA/CE.**

---

### #3 — Xingtai Xinbei Plastic Products Co., Ltd. — **72/100 🟢 Qualifié**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 11/15 | Vérifié | Adresse Chaozhuang village Pingxiang Xingtai Hebei complète (officiel + MIC) + année 2000 (`Since establishment 2000`) + Factory → Co Ltd. Adresse village = petite structure authentique → 11. | [xbplasticbucket.com/products_list/1189881017326063616-12-12.html](http://www.xbplasticbucket.com/products_list/1189881017326063616-12-12.html) ; [xinbeiplastic.en.made-in-china.com/company-Xingtai-Xinbei-Plastic-Products-Co-Ltd-.html](https://xinbeiplastic.en.made-in-china.com/company-Xingtai-Xinbei-Plastic-Products-Co-Ltd-.html) |
| **P2** | 13/20 | Vérifié | TÜV Rheinland **MIC-ASI246720** (vérifiable [verified.chn.tuv.com](https://www.verified.chn.tuv.com/en/)) + 8600 sqm + advanced machinery + photos + video. Surface cross-check MIC ok. Effectif non chiffré → -7. | [xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html](https://xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html) |
| **P3** | 15/15 | Vérifié | **Table capacités 8L-20L détaillée** (PP, MOQ 500) sur fiche produit : 8L 243×220/320g, 10L 260×270/480g, 12L 270×290/500g, 15L 275×325/660g, 16L 282×330/730g, 18L/20L... Gamme 0.5-50L. Excellent. | [xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html](https://xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html) (table Capacity) |
| **P4** | 11/15 | Vérifié | Soufflé + injecté PP/PE + FOB/EXW/CIF/DDP/DAP + export multi-provinces + Business License. OEM implicite, pcs/jour non chiffré → -4. | [xinbeiplastic.en.made-in-china.com/company-Xingtai-Xinbei-Plastic-Products-Co-Ltd-.html](https://xinbeiplastic.en.made-in-china.com/company-Xingtai-Xinbei-Plastic-Products-Co-Ltd-.html) |
| **P5** | 5/15 | Déclaré | FDA Certified Food Grade (texte fiche) + ISO9002:2000 (obsolète!) + ISO 9001/9000 company page sans doc. Aucun PDF/numéro/validité. ISO9002 obsolète = douteuse → 2×1 + TÜV audit 3 =5. | [xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html](https://xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html) |
| **P6** | 7/10 | Vérifié | **MOQ 500 pcs chiffré par ref** dans table (meilleur du panel!) + FOB/EXW/CIF/DDP/DAP + FAQ confirmation MOQ 500. → 3+2+2=7. | [xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html](https://xinbeiplastic.en.made-in-china.com/product/aQupRLHDTjUr/China-Food-Grade-10L-Heavy-Duty-Factory-Direct-Bulk-Order-Round-Plastic-Bucket.html) |
| **P7** | 10/10 | Vérifié | 3 URLs : xbplasticbucket.com (officiel) + MIC company + MIC product + extraction datée. Excellent. | [xbplasticbucket.com/products_list/1189881017326063616-12-12.html](http://www.xbplasticbucket.com/products_list/1189881017326063616-12-12.html) ; [xinbeiplastic.en.made-in-china.com/company-Xingtai-Xinbei-Plastic-Products-Co-Ltd-.html](https://xinbeiplastic.en.made-in-china.com/company-Xingtai-Xinbei-Plastic-Products-Co-Ltd-.html) |

**Recommandation : Go RFQ — meilleur MOQ (500) du panel, idéal pour comparer prix avec Rulyda/Yunde.**

---

### #4 — Qingdao Rulyda Plastic Manufacture Co., Ltd. — **73/100 🟢 Qualifié**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 13/15 | Vérifié | Raison sociale exacte + adresse A1 Building No.1388 Taifa Rd Huangdao Qingdao (officiel + MIC) + année 2017-05-04 sourcée MIC. Très précis → 13. | [rulydaplastic.com](https://www.rulydaplastic.com/) ; [rulydaplastic.en.made-in-china.com/product-list-8.html](https://rulydaplastic.en.made-in-china.com/product-list-8.html) (date 2017-05-04) |
| **P2** | 17/20 | Vérifié | **2 usines 20000m²** + 85 sets injection 1500T + 50+ Precision Molding (site officiel) + Industry-leading Audited Factory MIC. Cohérent cross-check → 17. | [rulydaplastic.com](https://www.rulydaplastic.com/) (2 factories 20000 sqm, 85 sets, 1500T) ; [rulydaplastic.en.made-in-china.com/product-list-8.html](https://rulydaplastic.en.made-in-china.com/product-list-8.html) |
| **P3** | 15/15 | Vérifié | **Site officiel** : 8L Custom Printed Square Clear Fuel Bucket + 10L Transparent Square IML Bucket + 15L Sticker White Pail + 2L/3L/4L/5L → 8-16L couvert. | [rulydaplastic.com](https://www.rulydaplastic.com/) (8L + 10L + 15L fiches) |
| **P4** | 11/15 | Vérifié | Injection + OEM ODM 10 years + export USA/Australia (news) + PP/HDPE + IML/Silk Screen. Tonnage non chiffré → -4. | [rulydaplastic.com](https://www.rulydaplastic.com/) ; [rulydaplastic.en.made-in-china.com/product-list-8.html](https://rulydaplastic.en.made-in-china.com/product-list-8.html) |
| **P5** | 4/15 | Déclaré | ISO9001:2015 mention MIC sans image certif (Management System Certification vide) + Audited Supplier (pas certif produit). Aucun FDA/EU. Site officiel 0 certif. → 1+3=4. | [rulydaplastic.en.made-in-china.com/product-list-8.html](https://rulydaplastic.en.made-in-china.com/product-list-8.html) (ISO9001:2015) ; [rulydaplastic.com](https://www.rulydaplastic.com/) (no cert) |
| **P6** | 3/10 | Déclaré | FOB Price US$0.45-0.5/piece (prix = incoterm implicite) + OEM/ODM. MOQ/délai/paiement/port non explicites. | [rulydaplastic.en.made-in-china.com/product-list-8.html](https://rulydaplastic.en.made-in-china.com/product-list-8.html) |
| **P7** | 10/10 | Vérifié | 3 URLs : rulydaplastic.com officiel + MIC + extraction datée. Excellent (en.rulyda.com HS 404 noté). | [rulydaplastic.com](https://www.rulydaplastic.com/) ; [rulydaplastic.en.made-in-china.com/product-list-8.html](https://rulydaplastic.en.made-in-china.com/product-list-8.html) |

**Recommandation : Go RFQ #1 — leader capacité (20000m²/85 presses). Exiger ISO PDF + tonnage annuel.**

---

### #5 — Zibo Yundu / Foshan Chengpin (CP Bucket) — **68/100 🟠 À compléter**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 9/15 | Contradictoire | Double identité : MIC = Zibo Yundu (Zibo Shandong, historique FIBCs/sacs tissés) vs site officiel = Foshan Chengpin (Foshan Guangdong, Founded 2005/Registered 2018). Adresse Foshan No.4 Jinxiang 1st Rd Sanshui confirmée, mais siège Zibo non géolocalisable + dualité non expliquée → Contradictoire -6. | [cpbucket.com/about-us.html](https://www.cpbucket.com/about-us.html) (Foshan 2005/2018) ; [yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU-PLASTIC-PRODUCTS-CO-LTD-.html](https://yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU-PLASTIC-PRODUCTS-CO-LTD-.html) (Zibo FIBCs) |
| **P2** | 14/20 | Déclaré | 10000m² Workshop + full-auto injection + IML/silk/heat transfer + photos site officiel. MIC Zibo ne montre PAS usine Foshan → Déclaré 14. | [cpbucket.com](https://www.cpbucket.com/) (10000m² Workshop) ; [cpbucket.com/about-us.html](https://www.cpbucket.com/about-us.html) |
| **P3** | 12/15 | Vérifié | Site officiel : 10L Rectangular Pail Snap-On Lid + 16L Oval Anti-Theft + 20L Square/Gamma Seal. 8-16L partiel (10L/16L ok, 8L/12L/15L non listés en fiche) → 12/15. | [cpbucket.com](https://www.cpbucket.com/) (10L Rectangular, 16L Oval) |
| **P4** | 13/15 | Vérifié | 20 years + 200+ countries + OEM/ODM + UN drop test 1.8m + 97% pass rate + gamme coating/chemical/food/ink/detergent/pesticide. Très complet. | [cpbucket.com/about-us.html](https://www.cpbucket.com/about-us.html) (20y, 200 countries, UN test) |
| **P5** | 5/15 | Déclaré | SGS 100% new PP + FDA & EU + UN + ISO 9001 + SGS food-grade + 5:1 lifting ISO 21898 + Industrial License (MIC) → tous sans doc → Déclaré 1×5=5. | [cpbucket.com](https://www.cpbucket.com/) (SGS) ; [yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU-PLASTIC-PRODUCTS-CO-LTD-.html](https://yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU-PLASTIC-PRODUCTS-CO-LTD-.html) |
| **P6** | 5/10 | Déclaré | FOB/CIF/EXW/CFR + Qingdao Port + low MOQ vague + délai/paiement non publiés. | Même URLs |
| **P7** | 10/10 | Vérifié | 3 URLs : cpbucket.com + about-us + MIC yundu + extraction datée. Excellent malgré dualité. | [cpbucket.com](https://www.cpbucket.com/) ; [cpbucket.com/about-us.html](https://www.cpbucket.com/about-us.html) ; [yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU-PLASTIC-PRODUCTS-CO-LTD-.html](https://yunduplastic.en.made-in-china.com/company-ZIBO-YUNDU-PLASTIC-PRODUCTS-CO-LTD-.html) |

**Recommandation : Go conditionnel — clarifier lien juridique Zibo↔Foshan + fournir Business License Foshan Chengpin.**

---

### #6 — Zhejiang Yunde Plastic Industry Technology Co., Ltd. — **76/100 🟢 Qualifié (TOP 1)**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 14/15 | Vérifié | Raison sociale exacte + 2 adresses usine (No.2345 Fulong Rd Cixi Binhai EDZ + 588 Songpu Second Rd Building 1) + année **2014-12-31** + 80M yuan / 10M USD + 30 acres sourcés sur 2 sites officiels cohérents → 14 (-1 divergence investissement). | [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) ; [zjyunde.cn/en/about/?142.html](http://www.zjyunde.cn/en/about/?142.html) |
| **P2** | 16/20 | Vérifié | **20000m² (30 acres)** + 30+ lignes + photos Factory (`/factory/`) + fluorination avancée + labo + Honor certs + image `iso9001-en.jpg`. Effectif non chiffré → -4. | [zjyunde.cn/en/about/?142.html](http://www.zjyunde.cn/en/about/?142.html) (30 acres, 30+ lines) ; [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) |
| **P3** | 15/15 | Vérifié | **Site officiel** : 10L American Style Durable PP Bucket + 16L American Style PP Bucket for Liquids + gamme 1L/2L/3L/5L/18L/20L/25L/35L → 8-16L parfait. | [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) (10L + 16L fiches) |
| **P4** | 14/15 | Vérifié | Injection + **fluorination HDPE** (niche chimique) + OEM/ODM + custom color/IML + 1-35L maîtrisé. Très complet → 14. | [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) ; [zjyunde.cn/en/about/?142.html](http://www.zjyunde.cn/en/about/?142.html) |
| **P5** | 8/15 | Déclaré | **ISO9001 image `iso9001-en.jpg` sur site officiel** (seul avec preuve image! mais numéro/validité illisibles → Déclaré 3) + Honor certs images 2 + lab 1 + fluorination 2 =8. FDA/EU non mentionnés. | [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) (iso9001-en.jpg) ; [zjyunde.cn/en/about/?142.html](http://www.zjyunde.cn/en/about/?142.html) |
| **P6** | 2/10 | Non vérifié | **Aucun MOQ/Incoterm/délai/paiement publiés** (ni officiel ni MIC) → 2 (OEM/ODM implicite seul). Point faible majeur. | [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) (no commercial terms) |
| **P7** | 7/10 | Vérifié | 2 sites officiels (yundeplastic.com + zjyunde.cn) + extraction datée. Pas de MIC → Bon 7. | [yundeplastic.com/product/pp-plastic-bucket/](https://www.yundeplastic.com/product/pp-plastic-bucket/) ; [zjyunde.cn/en/about/?142.html](http://www.zjyunde.cn/en/about/?142.html) |

**Recommandation : Go RFQ prioritaire #1 — pépite technique (fluorination niche + 30 lignes). Exiger grille prix/MOQ + ISO PDF lisible.**

---

### #7 — Taizhou Bright Plastic Co., Ltd. — **15/100 🔴 Non qualifié — HORS SPEC**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 7/15 | Déclaré | Adresse générique Taizhou EDZ 318000 sans rue + année 2016-03-07 via cnverify.com (403 le 2026-10-24, non re-vérifié) + Panjiva TAIZHOU EDZ (53 shipments). Imprécis → 7. | [plasticchina.en.alibaba.com](https://plasticchina.en.alibaba.com) ; Panjiva Bright Plastic Co. Ltd. |
| **P2** | 5/20 | Déclaré | 15+ ans déclaré + injection + printing + 53 shipments Panjiva. Mais 0 photo usine (MIC 404), 0 surface, 0 effectif, 0 BV → 5. | [plasticchina.en.alibaba.com](https://plasticchina.en.alibaba.com) ; [tzbright.en.made-in-china.com/product-list-13.html](https://tzbright.en.made-in-china.com/product-list-13.html) (404) |
| **P3** | 0/15 | Non vérifié | **⛔ HORS SPEC** : MIC showroom **404 `This showroom doesn't exist`** le 2026-10-24 → gamme 8-16L non prouvée. Hunter `Bucket category` = erreur (page morte). Catégories = Bottle/Broom/Dustpan/trash cans/pet supplies → pas de seaux PP 8-16L. | [tzbright.en.made-in-china.com/product-list-13.html](https://tzbright.en.made-in-china.com/product-list-13.html) (**404 vérifié 2026-10-24**) |
| **P4** | 3/15 | Déclaré | Injection + printing générique + Panjiva export avéré. Pas d'OEM seaux prouvé → 3. | [plasticchina.en.alibaba.com](https://plasticchina.en.alibaba.com) |
| **P5** | 0/15 | Non vérifié | 0 certif FDA/EU/ISO/BSCI. Aucun publié. → 0. | [plasticchina.en.alibaba.com](https://plasticchina.en.alibaba.com) (no cert) |
| **P6** | 0/10 | Non vérifié | 0 MOQ/Incoterm/délai/paiement. Showroom mort = 0 info. → 0. | Non communiqué — showroom 404 |
| **P7** | 0/10 | Non vérifié | 1 URL Alibaba + Panjiva, MIC 404 + cnverify 403 → Faible 0. | [plasticchina.en.alibaba.com](https://plasticchina.en.alibaba.com) |

**Recommandation : ⛔ NO-GO — Remplacer immédiatement. Erreur Hunter majeure.**

---

### #8 — Taizhou Huangyan Jinjie Plastic Factory — **50/100 🟠 À compléter — HORS SPEC 8-16L**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 12/15 | Vérifié | Raison sociale double (Jinjie = Gongjie) + adresse Nancheng Industrial Zone Huangyan Taizhou précise + Tel +86-576-84180810 + wanna@hy-gj.com + ICP Zhejiang 06015705. Très complet → 12. | [hy-gj.com/about/](https://www.hy-gj.com/about/) ; [hy-gj.com/product/plastic-bucket/](https://www.hy-gj.com/product/plastic-bucket/) |
| **P2** | 10/20 | Vérifié | Photos Injection Machines (`0_0003_1.jpg`) + IML full-auto lines + Huangyan Hometown of Molds + one-stop. Surface/effectif non chiffrés → -10 → 10. | [hy-gj.com/about/](https://www.hy-gj.com/about/) |
| **P3** | 0/15 | Non vérifié | **⛔ HORS SPEC site officiel** : catalogue hy-gj.com max **4.2L** (GJ-369) ; autres 540ml/1.3L/1.85L/2.7L. **Aucun 8-16L** sur officiel. Alibaba peut avoir plus grand mais non vérifié comme officiel → 0. | [hy-gj.com/product/plastic-bucket/](https://www.hy-gj.com/product/plastic-bucket/) (max 4.2L vérifié 2026-10-24) |
| **P4** | 9/15 | Vérifié | IML injection + diversification (Beverage Cup/Container/Lunch Box/Popcorn Bucket) + Alibaba/1688. Mais pas de seaux 8-16L → -6 → 9. | [hy-gj.com/about/](https://www.hy-gj.com/about/) ; [jinjieplastic.en.alibaba.com](https://jinjieplastic.en.alibaba.com) |
| **P5** | 11/15 | Déclaré | **4 images rapports sur site officiel** : BSCI Social Audit Report + FDA Raw Material Report + Intertek Food Grade + National Food Safety + texte BSCI/FDA/EU + SGS-certified = meilleur P5 du panel! Mais numéros/validités illisibles → Déclaré (pas Vérifié) 4×2+1+2=11. | [hy-gj.com/about/](https://www.hy-gj.com/about/) (4 rapports images + SGS) |
| **P6** | 1/10 | Non vérifié | 0 MOQ/Incoterm/délai/paiement sur officiel → 1 (email seul). | [hy-gj.com/about/](https://www.hy-gj.com/about/) (no commercial terms) |
| **P7** | 7/10 | Vérifié | 2 URLs officielles (hy-gj.com/about + plastic-bucket) + HTKDC + extraction datée → Bon 7. | [hy-gj.com/about/](https://www.hy-gj.com/about/) ; [hy-gj.com/product/plastic-bucket/](https://www.hy-gj.com/product/plastic-bucket/) ; [sourcing.hktdc.com/en/Supplier-Store/Home/Taizhou-Huangyan-Jinjie-Plastic-Factory/1S00OOWSS](https://sourcing.hktdc.com/en/Supplier-Store/Home/Taizhou-Huangyan-Jinjie-Plastic-Factory/1S00OOWSS) |

**Recommandation : No-Go CDC 8-16L, mais garder en base pour mini-contenants IML <5L (intéressant pour diversification + certifs).**

---

### #9 — Suzhou Fansheng Plastic Manufacture Co., Ltd. — **64/100 🟠 À compléter**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 14/15 | Vérifié | Raison sociale exacte + adresse Changan Rd 288 Xukou Wuzhong Suzhou + 2e adresse Taihu Lake Dongshan exit + année **1998-04-22** + USD 3.8M (MIC) → 14. | [innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html](https://innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html) |
| **P2** | 15/20 | Vérifié | **BV Audit MIC-ASR2141740** ([bvcerchina.cn](http://www.bvcerchina.cn) vérifiable) + 6-7 items verified by BV + 63 employees + Production Machines + photos Workshop (2 images) + Diamond Member 2010. | Même URL |
| **P3** | 10/15 | Déclaré | 10L Square Seafood Bucket + 10L PP Rectangle + catégories 16L-20L + 21L-30L **sur MIC uniquement** (pas de site officiel Fansheng dédié, utilise innopack.com vide) → Déclaré 10. | [innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html](https://innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html) (10L + 16L-20L cat) |
| **P4** | 10/15 | Vérifié | PP/PE + tamper-evident + OEM/ODM + FOB/CIF/CFR + Production Machines. Tonnage non chiffré → -5. | Même URL |
| **P5** | 6/15 | Déclaré | ISO/SGS CERTIFICATIONS images (2) + AUDITED SUPPLIER image + BV 6-7 items. Images illisibles (numéros/validités non extraits) → Déclaré 3+3=6. | Même URL (ISO/SGS CERTIFICATIONS image, BV ASR2141740) |
| **P6** | 5/10 | Déclaré | FOB/CIF/CFR + OEM/ODM. MOQ/délai/paiement non publiés → 5. | Même URL |
| **P7** | 4/10 | Déclaré | 2 URLs marketplace (MIC Fansheng + Alibaba) + innopack.com groupe vide → Moyen 4. | [innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html](https://innopackaging.en.made-in-china.com/company-Suzhou-Fansheng-Plastic-Manufacture-Co-Ltd-.html) ; [fsplastic.en.alibaba.com/productgrouplist-922187186/plastic_bucket.html](https://fsplastic.en.alibaba.com/productgrouplist-922187186/plastic_bucket.html) |

**Recommandation : Go groupé avec #2 (même groupe Innopack), négocier prix usine direct, exiger BV Report complet.**

---

### #10 — Qingdao Hivic Plastic Manufacture Co., Ltd. — **31/100 🔴 Non qualifié**

| Pilier | Score | Statut | Justification | URLs |
|--------|-------|--------|---------------|------|
| **P1** | 5/15 | Contradictoire | Adresse générique `Qingdao Shandong China` sans rue + staff 2 + année **contradictoire 2017 (MIC) vs 2008 (moldso.com)** (Hunter noté, confirmé) + Trading implicite → Contradictoire 0 + 5 raison sociale seule. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) (staff 2, générique) ; divergence 2017 vs 2008 |
| **P2** | 6/20 | Déclaré | Audited Supplier + well-equipped facilities (texte générique) + CNC molds déclaré. Mais 0 surface/effectif/machines chiffrés + staff 2 → 6. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) |
| **P3** | 5/15 | Non vérifié | Plastic Bucket catégorie existe mais produits = **Crates pliantes** (Folding Agriculture Vegetable Storage, 60*40*30) + Pallet dominant. Aucune fiche 10L/16L sourçable. → 5 partiel. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) (Bucket cat = Crates) ; [hivic.com](https://hivic.com) (vide 114 bytes) |
| **P4** | 6/15 | Déclaré | PP/HDPE + CNC molds + Pallet/Box/Container/Crates/Waste Bin (pallet-centric) + OEM Available. Pas de procédé seaux 8-16L spécifique → 6. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) |
| **P5** | 1/15 | Déclaré | `All products comply international quality standards` (marketing générique) + excellent quality control (texte sans preuve). 0 FDA/ISO/BSCI/UN/SGS doc. hivic.com vide. → 1. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) ; [hivic.com](https://hivic.com) (vide) |
| **P6** | 4/10 | Déclaré | FOB Price US$2-3.8/pc (prix = incoterm implicite) + OEM Service Available + FOB Qingdao implicite. MOQ/délai non publiés → 4. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) (FOB $2-3.8) |
| **P7** | 4/10 | Déclaré | 2 URLs MIC + Alibaba vide + hivic.com vide 114 bytes → Moyen 4. | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) ; [hivic.en.alibaba.com/company_profile.html](https://hivic.en.alibaba.com/company_profile.html) ; [hivic.com](https://hivic.com) |

**Recommandation : ⛔ NO-GO — Remplacer. Palettier, pas seautier. Surestimation Hunter.**

---

## 3) Entreprises liées & Doublons

### Entreprises liées (2 groupes)

| Groupe | Membres | Preuve |
|--------|---------|--------|
| **Groupe Innopack** | **#2 Suzhou Innovation Packaging** ↔ **#9 Suzhou Fansheng Plastic** | Fansheng = maison mère fondée 1998 (USD 3.8M) ; Innovation = filiale fondée 2013-07 investie par Fansheng (`Innopack Suzhou Co., Ltd, mainly invested by Suzhou Fansheng Plastic Manufacture Co., Ltd`). Même zone Wuzhong Suzhou, même plateforme Made-in-China `innopackaging.en.made-in-china.com` vs `sz-innovation...`, même domaine groupe [innopack.com](https://www.innopack.com). Contacts MIC distincts mais groupe unique. |
| **Groupe CP Bucket** | **#5 Zibo Yundu Plastic (Zibo Shandong)** ↔ **Foshan Chengpin Technology (Foshan Guangdong)** | Double identité légale : fiche MIC = ZIBO YUNDU (historique FIBCs/sacs tissés, 18 years), site officiel = Foshan Chengpin Technology (`Founded 2005 Registered 2018` sur [cpbucket.com/about-us.html](https://www.cpbucket.com/about-us.html)). Contact unique Mr Fan +86 18316967024 + sales@cpbucket.com. Deux Business License non réconciliées. |

### Doublons

**Aucun doublon strict** (même raison sociale + adresse + tel identiques) sur les 10 lignes.  
**Panel réel = 8 entités indépendantes** (10 - 2 groupes liés comptés double).

---

## 4) Infos non prouvées (certifs & capacités)

| Catégorie | Fournisseurs concernés | Détail |
|-----------|----------------------|--------|
| **FDA Déclaré sans PDF** | #1 Enlightening (FDA 21 CFR 177.1520 texte), #2 Innovation (phrase marketing `certified by FDA`), #3 Xinbei (`FDA Certified Food Grade` texte), #5 CP Bucket (SGS/FDA/EU texte), #8 Jinjie (FDA Raw Material Report image illisible) | Aucun rapport SGS/Intertek/FDA avec numéro/validité/organisme sourçable. → **Déclaré, jamais Vérifié.** Exiger en RFQ. |
| **EU 10/2011 Déclaré** | #1 Enlightening (texte), #5 CP Bucket (texte), #8 Jinjie (texte FDA/EU) | Même constat — 0 PDF EU. |
| **ISO 9001 Déclaré** | #1 Enlightening (logo ISO 9001 sans doc), #2 Innovation (phrase `ISO9001` sans doc), #3 Xinbei (ISO 9001/9000 + ISO9002:2000 obsolète!), #4 Rulyda (ISO9001:2015 mention vide), #5 CP Bucket (ISO 9001 texte), #9 Fansheng (ISO/SGS image illisible) | **Seul #6 Yunde a une image `iso9001-en.jpg` sur site officiel** (mais illisible → Déclaré). Aucun ISO Vérifié au sens grille (PDF + numéro + validité + organisme TÜV/SGS/BV). |
| **Autres certifs Déclarés** | #2 HACCP (1 phrase), #8 BSCI/Intertek/National Food Safety (4 images illisibles), #9 BV Audited (vrai audit mais pas certif produit), #5 UN/5:1 lifting test (texte) | BSCI Jinjie = plus solide (image Social Audit Report) mais illisible. |
| **ISO obsolète** | #3 Xinbei : `ISO9002:2000 standard model` (norme retirée en 2000, remplacée par ISO 9001:2000→2015) | Signale documentation ancienne non mise à jour → doute process qualité actuel. |
| **Capacités non prouvées** | #7 Bright : 0 surface, 0 machines chiffrés ; #10 Hivic : staff 2, 0 surface/machines ; #8 Jinjie : surface/effectif non chiffrés ; #2 Innovation : surface usine propre non chiffrée (bureau) | Demander Factory Audit Report BV/SGS/TÜV avec métriques. |

---

## 5) Hors spécifications 8-16L

| # | Fournisseur | Statut CDC | Preuve d'audit 2026-10-24 |
|---|-------------|------------|---------------------------|
| **7** | Taizhou Bright | **Hors spec** | MIC [tzbright.en.made-in-china.com/product-list-13.html](https://tzbright.en.made-in-china.com/product-list-13.html) → **HTTP 404** `This showroom doesn't exist`. Alibaba = Bottle/Broom/Dustpan/trash cans/pet supplies, pas de seaux PP 8-16L. → P3 0/15 |
| **8** | Jinjie Huangyan | **Hors spec** | Site officiel [hy-gj.com/product/plastic-bucket/](https://www.hy-gj.com/product/plastic-bucket/) → max **4.2L** (GJ-369 4.2L, GJ-368 2.7L, GJ-367 1.85L...). **Aucun 8-16L** sur officiel. → P3 0/15 |
| **10** | Hivic Qingdao | **Partiellement hors spec** | [hivicplastic.en.made-in-china.com/productList](https://hivicplastic.en.made-in-china.com/productList) → produits = Folding Vegetable Crates (60*40*30), Pallet dominant, très peu de buckets. Aucune fiche 10L/16L sourçable. → P3 5/15 Non vérifié |
| 1,3,4,6 | Enlightening, Xinbei, Rulyda, Yunde | **Conformes** | Gammes 10L+16L (ou 8L/12L/15L) prouvées sur **site officiel** → P3 15/15 Vérifié |
| 2,5,9 | Innovation, CP Bucket, Fansheng | **Conformes (déclaré)** | Gammes prouvées sur MIC uniquement (pas d'officiel buckets) → P3 10-12/15 Déclaré/Vérifié |

---

## 6) Données manquantes (à exiger en RFQ)

| Donnée | Manque chez | Priorité |
|--------|-------------|----------|
| **MOQ chiffré par ref (8L/10L/12L/15L/16L)** | #1 (vary by product), #4, #5 (low vague), #6 (absent), #7 (404), #8 (absent), #9 (absent), #10 (absent) — seuls #2 (1000 pcs) et #3 (500 pcs) chiffrés | 🔴 Bloquant |
| **Incoterms + port** | #6 (absent), #7 (404), #8 (absent) partiels ; #1/#4/#5 implicites | 🟠 Important |
| **Délai production + validité prix** | Tous sauf partiel #3 (FAQ) | 🟠 Important |
| **Conditions paiement (T/T 30/70, L/C)** | Tous | 🟠 Important |
| **Certificats PDF (FDA/EU/ISO)** | Tous (0 Vérifié) | 🔴 Bloquant food-grade |
| **Surface/effectif/tonnage** | #2 (bureau), #7, #8 partiel, #10 (staff 2) | 🟡 Utile |
| **Site officiel buckets dédié** | #2 (innopack.com vide), #9 (pas de site propre), #10 (hivic.com vide 114 bytes) | 🟡 Utile |

---

## 7) Recommandations Go / No-Go

### ✅ Go RFQ (4 qualifiés)

| Rang | Fournisseur | Score | Action | Message RFQ |
|------|-------------|-------|--------|-------------|
| **1** | **#6 Zhejiang Yunde** | 76 | **Go prioritaire #1** | Pépite fluorination (niche chimique) + 30 lignes 20000m². Exiger : grille MOQ + FOB Ningbo + ISO9001 PDF lisible + test fluorination. Demander échantillon 10L + 16L American Style. |
| **2** | **#1 Enlightening Plast** | 73 | **Go #2** | Solide 2 usines Qingdao+Shanghai, gamme 10L/18.93L officielle. Exiger : FDA/EU/ISO/UN rapports PDF + MOQ grille + FOB Qingdao. |
| **3** | **#4 Qingdao Rulyda** | 73 | **Go #3 (leader capacité)** | 20000m² 85 presses 1500T = capacité max. Exiger : ISO9001:2015 PDF (TÜV/SGS/BV) + tonnage annuel + MOQ + FOB Qingdao. |
| **4** | **#3 Xingtai Xinbei** | 72 | **Go #4 (meilleur MOQ)** | MOQ 500 imbattable + table 8L-20L complète + TÜV ASI246720. Exiger : FDA PDF + ISO9001 actuel (pas 9002) + prix FOB Tianjin/Qingdao. Idéal pour comparer #4. |

### 🟠 Go conditionnel (2 à compléter)

| Fournisseur | Score | Action | Condition |
|-------------|-------|--------|-----------|
| **#5 Zibo Yundu / CP Bucket** | 68 | Go si doc juridique | Fournir Business License Foshan Chengpin + lien capitalistique Zibo Yundu. Exiger certifs SGS/FDA PDF. 10000m² + 10L/16L ok. |
| **#9 Fansheng + #2 Innovation** | 64 + 57 | **Go groupé (1 RFQ)** | Groupe Innopack : contacter Fansheng (maison mère, BV ASR2141740) directement, négocier prix usine. Ne pas RFQ #2 séparément (filiale bureau). Exiger BV Report complet + ISO/SGS PDF. |

### 🔴 No-Go (4 à remplacer/écarter)

| Fournisseur | Score | Motif | Remplacement |
|-------------|-------|-------|--------------|
| **#7 Bright** | 15 | Showroom 404 + pas de seaux 8-16L + 0 certif + Hunter erreur majeure | **Remplacer immédiatement** |
| **#8 Jinjie** | 50 mais P3=0 | Max 4.2L sur officiel → hors CDC 8-16L (spécialiste IML <5L) | Garder en base pour mini-contenants IML, pas pour CDC actuel |
| **#10 Hivic** | 31 | Adresse générique + 2017 vs 2008 + staff 2 + gamme = Crates/pallets, pas seaux | **Remplacer — palettier, pas seautier** |

> **Panel final recommandé pour RFQ : 5 RFQ** (4 qualifiés + 1 groupé #5 + 1 groupé #2/#9 = 6 fournisseurs réels, 5 RFQ). Remplacer #7 et #10 par 2 nouveaux fabricants vérifiés (recherche complémentaire Supplier Hunter).

---

## 8) Méthodologie & Traçabilité

- **Barème 7 piliers /100** : P1 Identification 15 + P2 Activité 20 + P3 Conformité 15 + P4 Capacités 15 + P5 Certifs 15 + P6 Commerce 10 + P7 Sources 10. Arrondi entier, pas de demi-point.
- **Statuts** : `Vérifié` = preuve sourcée (adresse rue, photo usine, fiche produit officielle, BV/TÜV audit) ; `Déclaré` = mention texte sans doc ; `Non vérifié` = absent ; `Contradictoire` = sources incohérentes (prime sur autres).
- **Extraction** : `curl -L -A Mozilla/5.0 --max-time 25` + `html2text` le 2026-10-24. HTTP 200 (28 URLs), 404 (Bright MIC, en.rulyda.com), 403 (cnverify). Fichiers `/tmp/audit_extracts/*.html|txt` conservés.
- **Reproductibilité** : un autre auditeur avec mêmes URLs doit retrouver scores ±5 pts.
- **Fichiers livrés** :
  - `reports/fabricants-corrigé-2026-10-24.csv` (séparateur `;`, UTF-8-SIG, colonnes originales + Score + Niveau + Statut + Commentaire + P1-P7 + URLs)
  - `reports/fabricants-corrigé-2026-10-24.xlsx` (3 feuilles : Scores Synthèse + Grille P1-P7 détaillée + Anomalies & Liens, mise en forme conditionnelle rouge/orange/vert, filtres, impression A3 paysage)
  - `reports/audit-fournisseurs-2026-10-24.md` (ce fichier)
- **Original préservé** : `data/fabricants_seaux_PP_8-16L_Chine-ORIGINAL.csv` non modifié.

---

*Audit réalisé par Supplier Auditor — SOURCING LAB AI — 2026-10-24 — ZÉRO invention, chaque score cite URL exacte.*

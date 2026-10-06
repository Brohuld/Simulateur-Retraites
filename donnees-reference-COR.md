# Données de référence — Simulateur Retraites

Consolidation des données sources utilisées dans le simulateur. Mise à jour : 6 octobre 2026 (version 3).

Les hypothèses du COR sont détaillées, page par page, dans `hypotheses-COR.md`. Le calcul par décile est dans `calculs-par-decile.md` (moteur : `moteur-calcul/`).

---

## 1. Taux de remplacement par décile (TR_REF dans le code)

Pension nette ÷ dernier salaire net, génération 1980, carrière de 43 ans, départ au taux plein (65,5 ans). **Calculés** à partir des règles de calcul des pensions et vérifiés sur les profils types du COR 2026 (le COR ne publie pas de valeurs par décile) — voir `calculs-par-decile.md`.

| Profil | Dernier salaire brut mensuel | Taux de remplacement |
|--------|---------------------|---------------------|
| D1 — bas salaire | ~1 830 € | **80 %** |
| D5 — médian | ~2 930 € | **67 %** |
| D10 — haut salaire | ~9 090 € | **47 %** |

Ces valeurs correspondent à `TR_REF = [80, 67, 47]` dans le simulateur. Seul l'âge de départ agit sur le taux de remplacement au départ (± 5 % de pension par année) ; l'indexation agit pendant la retraite, dans le TRI.

---

## 2. Espérance de vie

### 2a. Espérance de vie moyenne à la naissance (INSEE, bilan démographique 2025)

Source : [INSEE — Espérance de vie à divers âges](https://www.insee.fr/fr/statistiques/2416631)

| Année | Femmes | Hommes |
|-------|--------|--------|
| 1960  | ~73 ans | ~67 ans |
| 1980  | ~78 ans | ~70 ans |
| 2000  | ~83 ans | ~75 ans |
| 2024  | 85,8 ans | 80,2 ans |
| 2025 (p) | 85,9 ans | 80,3 ans |

**Espérance de vie à 60 ans (2025) :** 27,9 ans (femmes) / 23,9 ans (hommes)
**Espérance de vie à 65 ans (2025) :** 23,6 ans (femmes) / 20,0 ans (hommes)

### 2b. Espérance de vie à 55 ans par CSP — Hommes, génération 1942

Source : **DREES, Dossier Solidarité et Santé n°40 (2013)** — génération née en 1942.

| CSP | EV à 55 ans | Âge liquidation | Durée retraite espérée |
|-----|-------------|-----------------|------------------------|
| Cadres et PIS | 28,6 ans | 60,9 ans | **22,7 ans** |
| Professions intermédiaires | 26,8 ans | 59,6 ans | 22,2 ans |
| Employés | 25,7 ans | 59,0 ans | 21,7 ans |
| Agriculteurs | 26,3 ans | 60,6 ans | 20,8 ans |
| Artisans/commerçants | 27,8 ans | 61,2 ans | 21,6 ans |
| **Ouvriers** | **25,3 ans** | **60,4 ans** | **19,9 ans** |
| Ensemble | 26,4 ans | 60,2 ans | 21,2 ans |

**Écart cadres/ouvriers : 2,8 ans de durée de retraite en moins pour les ouvriers.**

> Données plus récentes (INSEE 2020-2022) : l'écart d'EV à 35 ans entre cadres et ouvriers est de **5,3 ans** pour les hommes, **3,0 ans** pour les femmes.

### 2c. Inégalités par niveau de vie

Source : **INSEE/COR, séance du 11 février 2021**

- Écart d'espérance de vie entre les 5 % les plus aisés et les 5 % les plus modestes : **13 ans chez les hommes**
- Lien : [COR — Inégalités et évolutions récentes de l'EV](https://www.cor-retraites.fr/node/551)

---

## 3. Durée passée à la retraite — évolution historique

Source : DREES, INSEE

| Génération / période | Durée moyenne à la retraite |
|---------------------|----------------------------|
| Années 1960-70 | ~12-15 ans |
| Génération 1930 | ~23 ans |
| Génération 1960 | ~25 ans |
| Aujourd'hui (départ ~62 ans 8 mois) | ~22 ans (moyenne H+F) |

Hommes seuls : ~17,5 ans. Femmes : bien plus (EV supérieure).

---

## 4. Ratio cotisants / retraités — données historiques

Source : [INSEE — Cotisants, retraités et rapport démographique tous régimes](https://www.insee.fr/fr/statistiques/2415121) · [COR Rapport 2025](https://www.cor-retraites.fr/sites/default/files/2025-06/RA_2025_def_publi.pdf)

| Année | Cotisants pour 1 retraité |
|-------|--------------------------|
| 1960  | ~4,0 |
| 1970  | ~3,5 |
| 1980  | ~2,8 |
| 1990  | ~2,5 |
| 2000  | ~2,2 |
| 2010  | ~1,9 |
| 2020  | ~1,7 |
| 2023  | ~1,68 |
| 2040* | ~1,5 (estimé) |
| 2070* | ~1,3 (scénario central COR) |

*Interpolation/projection illustrative, pas une donnée officielle point par point.

---

## 5. Données pour le calcul du TRI par décile

Les paramètres par génération et par décile (taux de remplacement rapporté au salaire moyen de carrière, cotisations, perte de valeur annuelle de la pension) sont produits par `moteur-calcul/parametres_simulateur.py` et recopiés dans `TRI_GEN_PARAMS` du simulateur.

### Âges d'entrée et de départ

Génération 1960 (déjà à la retraite) : entrée à 19,25 ans, départ à 62,25 ans (COR, annexe 2026, figure A2.2).

Générations 1980 et suivantes : quatre groupes selon l'âge de fin d'études (Dares 2023), répartis dans chaque décile à partir des catégories socioprofessionnelles (Insee 2024). Entrée à 19,5 / 20,1 / 21,9 / 25,3 ans. Départ au plus tard entre l'âge légal (carrière longue : − 2 ans avant 20 ans, − 1 an avant 21 ans) et l'âge où la durée de 43 ans est atteinte, sans dépasser 67 ans. En plus, 26 % de chaque décile partent à l'âge légal quelle que soit leur durée (décote 11 %, ex-invalides 8 %, inaptes 7 % : Drees, panorama 2025, fiche 17, génération 1953). Détail : `calculs-par-decile.md`, section 2 bis.

Effet sur le solde : 0,8 point de PIB par an d'âge moyen de départ (COR, rapport 2026 p. 124 : 3,0 ans pour 2,4 points en 2070). Un an d'âge légal en plus = + 0,5 an d'âge moyen = + 0,38 point (COR, séance du 26 mars 2026 : + 0,2 à + 0,4). Montée en charge réglable (0 à 20 ans) : elle retarde l'effet, sans changer le résultat de 2070.

### Espérance de vie à utiliser dans le TRI (hommes, par génération)

Source : [INSEE Première n° 1927 (2023)](https://www.insee.fr/fr/statistiques/6655536), scénario central — espérance de vie à 65 ans par génération. On l'utilise comme moyenne de la génération (âge moyen de décès = 65 + EV à 65 ans).

| Génération | EV à 65 ans (hommes) | Âge de décès moyen |
|---|---|---|
| 1960 | 21,2 ans | 86,2 ans |
| 1980 | 23,7 ans | 88,7 ans |
| 2000 | 25,8 ans | 90,8 ans |
| 2020 | 27,7 ans | 92,7 ans |

Écart de chaque décile à la moyenne : espérance de vie à 65 ans par décile de niveau de vie, hommes, 2012-2016 ([INSEE, tables de mortalité par niveau de vie](https://www.insee.fr/fr/statistiques/3311422?sommaire=3311425), fichier `morta_niv_2016.xls` dans ce dossier). Vingtièmes regroupés deux par deux, pondérés par les survivants à 65 ans. Moyenne : 19,0 ans.

| | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
|---|---|---|---|---|---|---|---|---|---|---|
| EV à 65 ans | 16,0 | 16,8 | 17,4 | 18,0 | 18,4 | 18,9 | 19,3 | 19,9 | 20,6 | 21,5 |
| Écart à la moyenne | −3,0 | −2,2 | −1,6 | −1,1 | −0,6 | −0,2 | +0,3 | +0,8 | +1,6 | +2,5 |

Écart appliqué identique aux quatre générations. Limite : l'INSEE classe par niveau de vie du ménage, le simulateur par salaire.

### Taux de cotisation retraite (salarié + employeur)

Taux 2026 (Légisocial) :

- Régime de base : 15,45 % jusqu'au plafond de la sécurité sociale + 2,51 % sur tout le salaire.
- Agirc-Arrco : 10,02 % jusqu'au plafond, 24,29 % au-delà, + 0,35 % sur tout le salaire au-dessus du plafond.
- **Total sous le plafond : 27,98 %.**

Le TRI compte toutes ces cotisations, y compris celles qui n'ouvrent pas de droits. La génération 1960 est ramenée au taux moyen de carrière publié par le COR, soit environ 25 % (RA 2026, figure 3.1).

---

## 6. Âge moyen de départ à la retraite

Source : COR Rapport 2025, DREES Fiche 15

- 2023 (réel) : **62,9 ans** (tous régimes)
- Projection COR 2070 : **64,1 à 64,6 ans** (scénario central)
- Slider de référence dans le simulateur : **64 ans**

---

## 7. Sources principales

- [Rapport annuel COR — Juin 2026](https://www.cor-retraites.fr/rapports-du-cor/rapport-annuel-cor-juin-2026-evolutions-perspectives-retraites-france)
- [Rapport annuel COR — Juin 2025 (PDF)](https://www.cor-retraites.fr/sites/default/files/2025-06/RA_2025_def_publi.pdf)
- [INSEE — Espérance de vie à divers âges](https://www.insee.fr/fr/statistiques/2416631)
- [INSEE — Cotisants, retraités et rapport démographique tous régimes](https://www.insee.fr/fr/statistiques/2415121)
- [INSEE — Espérance de vie à 35 ans par CSP et diplôme](https://www.insee.fr/fr/statistiques/2383438)
- [DREES — Espérance de vie, durée passée à la retraite (dss40, 2013)](https://drees.solidarites-sante.gouv.fr/sites/default/files/2020-08/dss40.pdf)
- [DREES — Fiche 15 : Âge moyen de départ à la retraite](https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-07/Fiche%2015%20-%20L'%C3%A2ge%20moyen%20de%20d%C3%A9part%20%C3%A0%20la%20retraite%20et%20son%20%C3%A9volution.pdf)
- [COR — Inégalités et évolutions récentes de l'espérance de vie (séance 11/02/2021)](https://www.cor-retraites.fr/node/551)
- [INED/ENS Lyon — Ouvriers vs cadres à la retraite (mai 2023)](https://ses.ens-lyon.fr/actualites/rapports-etudes-et-4-pages/les-ouvriers-vivent-moins-longtemps-que-les-cadres-combien-de-temps-passent-ils-a-la-retraite-et-en-in-activite-ined-mai-2023)

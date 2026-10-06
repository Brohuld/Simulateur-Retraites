# Hypothèses du COR — document de référence

*Rédigé le 6 octobre 2026. Ce fichier est la référence unique du dossier pour les hypothèses et les résultats publiés par le Conseil d'orientation des retraites (COR). Chaque valeur renvoie à sa source et à sa page. Le simulateur et les notes du dossier s'appuient sur ce fichier.*

**Conventions de lecture**

- « Lecture graphique » : valeur lue sur une courbe du rapport, précise à ± 0,5 point. Le COR ne publie pas le chiffre exact.
- Les pages sont celles **imprimées** sur le document.
- Les montants sont des flux annuels, sauf mention contraire.

---

## 1. Sources (dossier `Sources/`)

| Fichier | Document |
|---|---|
| `RA_2026_def.pdf` | COR, rapport annuel, juin 2026 — cité « RA 2026 » |
| `Annexe_méthodo_en_ligne_2026.pdf` | COR, annexe méthodologique en ligne du rapport 2026 — citée « Annexe » |
| `RA_2025_def_publi.pdf` | COR, rapport annuel, juin 2025 — cité « RA 2025 » |
| `DREES_retraites_2025.pdf` | Direction de la recherche, des études, de l'évaluation et des statistiques (Drees), *Les retraités et les retraites*, édition 2025 |
| `doc-3923.pdf` | COR, séance du 17 mai 2017, document n° 10 : méthode du taux de rendement interne — cité « Doc 2017 » |
| `Doc_02_Simul macroéco leviers d'équilibre.pdf` | COR, séance du 26 mars 2026, document n° 2 : effets macroéconomiques des leviers d'équilibre (DG Trésor, I-MIP, OFCE) |

## 2. Scénario de référence

| Hypothèse | Valeur | Source |
|---|---|---|
| Fécondité | 1,45 enfant par femme à partir de 2028 | RA 2026 p. 8 ; Annexe p. 6 |
| Solde migratoire | + 150 000 personnes par an | idem |
| Croissance de la productivité horaire du travail | 0,7 % par an | idem |
| Taux de chômage | 7,0 % à partir de 2040 | idem |
| Démographie | Projections de population Insee 2026-2070, scénario central | Annexe p. 24 |

Le rapport 2025 retenait une fécondité de 1,8 et un solde migratoire de + 70 000 par an (RA 2025 p. 117).

## 3. Situation financière du système

| | Valeur | Source |
|---|---|---|
| Dépenses de retraite 2025 | 422 Md€ par an, soit 14,1 % du PIB | RA 2026 p. 9 |
| Déficit 2025 | 5,1 Md€ par an, soit 0,2 % du PIB (hors produits et charges financiers) | RA 2026 p. 17 |

Solde en % du PIB (Annexe p. 6, tableau A2.1) :

| 2024 | 2030 | 2038 | 2048 | 2050 | 2070 |
|---|---|---|---|---|---|
| − 0,1 % | − 0,2 % | − 0,5 % | − 1,1 % | − 1,2 % | − 2,4 % |

Le rapport 2025 prévoyait − 1,4 % en 2070.

**Âge d'équilibre :** pour équilibrer le système par l'âge seul, l'âge moyen de départ devrait atteindre 67,6 ans en 2070, soit 3,0 ans de plus qu'à législation inchangée (RA 2026 p. 124).

## 4. Pilotage de l'Agirc-Arrco retenu en projection (RA 2026 p. 62)

| Période | Valeur de service du point (ce que rapporte un point) | Valeur d'achat du point (ce que coûte un point) |
|---|---|---|
| 2025 | Gelée (1,4386 €) | Suit le salaire moyen du privé |
| 2026 | Inflation hors tabac − 0,4 point | Suit le salaire moyen du privé |
| 2027-2037 | Salaire moyen du privé − 1,16 % par an | Suit le salaire moyen du privé |
| À partir de 2038 | Salaire moyen du privé − 0,86 % par an | Salaire moyen du privé − 0,86 % par an |

**Ce que cela implique :** le rendement de l'Agirc-Arrco (ce que rapporte chaque euro cotisé) baisse jusqu'en 2037, puis se stabilise. L'Agirc-Arrco précise que ces hypothèses sont conventionnelles et n'engagent pas les décisions futures des syndicats et du patronat.

## 5. Les profils types de salariés du privé (Annexe p. 9-12)

Le COR ne calcule pas par décile. Il suit des **profils types**, construits à partir de carrières réelles.

| Profil | Définition exacte | Salaire en fin de carrière |
|---|---|---|
| N° 1 — cadre | Quelques années dans le tiers inférieur des salaires, puis passage cadre et « carrière complète de cadre au salaire moyen du dernier décile » | 2,51 × RMPT |
| N° 2 — non-cadre | « Un salaire égal au salaire moyen du tiers inférieur de la distribution des salaires, à chaque âge » | 0,74 × RMPT |
| Carrière au SMIC | Carrière complète entièrement au SMIC | SMIC |

RMPT : rémunération moyenne par tête de l'ensemble de l'économie. Le COR ne la donne pas en euros.

**Conséquence pour le simulateur :** le profil « non-cadre » n'est pas un salarié médian. C'est la moyenne des 33 % les moins payés, donc à peu près le niveau de D2. Le profil « cadre » correspond au dernier décile (D10).

**Âge d'entrée dans la vie active** (Annexe p. 10, figure A2.2, lecture graphique) :

| Génération | Non-cadre | Cadre | Passage au statut cadre |
|---|---|---|---|
| 1950 | 18,25 ans | 19,75 ans | 26,5 ans |
| 1960 | 19,25 ans | 20 ans | 26,5 ans |
| À partir de 1975 | 22,5 ans | 22,75 ans | 26 ans |

L'entrée correspond à la première année avec plus de trois trimestres cotisés, pour écarter les jobs d'été.

**Salaire selon l'âge, en % de la RMPT** (Annexe p. 12, figure A2.4, lecture graphique, à ± 3 points) :

| Âge | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 et plus |
|---|---|---|---|---|---|---|---|---|---|
| Non-cadre | 52 % | 58 % | 64 % | 66 % | 68 % | 69 % | 70 % | 73 % | 73 % |
| Cadre | 50 % | 58 % | 145 % | 185 % | 195 % | 210 % | 230 % | 250 % | 251 % |

Ces profils, mesurés sur la génération 1962, sont **les mêmes pour toutes les générations** : le salaire à chaque âge suit seulement la RMPT (Annexe p. 11). Le salaire est supposé constant, par rapport à la RMPT, en fin de carrière.

## 6. Taux de remplacement

**Définition du COR** (Annexe p. 22) : pension nette à la liquidation ÷ salaire net moyen des 12 derniers mois.

- Départ au taux plein du régime général, sans décote ni surcote.
- Cotisations Agirc-Arrco au taux moyen.

**Taux de contribution sociale généralisée (CSG) retenu par convention** (Annexe p. 22) :

| Profil | Taux de CSG |
|---|---|
| Cadre | Plein (8,3 %) |
| Non-cadre | Intermédiaire (6,6 %) |
| SMIC | Réduit (3,8 %) |

**Valeurs publiées**

Génération 1964, au taux plein (RA 2026 p. 163, tableau 3.3) :

| Profil | Taux de remplacement |
|---|---|
| Cadre | 51,9 % |
| Non-cadre | 74,7 % |

Par génération, lecture graphique :

| Génération | 1960 | 1980 | 2000 | Source |
|---|---|---|---|---|
| Non-cadre | ≈ 75 % | ≈ 70 % | ≈ 68,7 % | RA 2026 p. 135, figure 3.3 |
| Cadre | ≈ 51,5 % | ≈ 48,5 % | ≈ 46,5 % | RA 2026 p. 136, figure 3.4 |
| SMIC (pension **brute** ÷ salaire net) | ≈ 87 % | ≈ 87,5 % | ≈ 84,3 % | RA 2026 p. 177, figure 3.21 |

Le rapport 2025 donnait pour la génération 1980 : SMIC 79,6 %, chiffre exact cité dans le texte (RA 2025 p. 156) ; non-cadre ≈ 70 % ; cadre ≈ 47,5 % (RA 2025 p. 117-118).

**Drees :** taux de remplacement net médian de 74,7 % pour la génération 1950, carrière complète (Drees, fiche 6).

## 7. Taux de cotisation (RA 2026 p. 132, figure 3.1)

- Profil non-cadre, part salariale et part employeur, en moyenne sur la carrière : de 19 % (génération 1940) à **28 %** (génération 2000). Génération 1955 : 23,6 %.
- Lecture graphique, par génération : 1960 ≈ 25 % (dont régime de base ≈ 15,8 %) ; 1980 ≈ 27,8 % ; 2000 ≈ 28 %.
- Taux légal 2025 sous le plafond de la sécurité sociale : 27,9 %.

## 8. Taux de rendement interne (TRI)

**Définition** (Annexe p. 24) : le taux qui égalise la valeur actuelle des pensions reçues et celle des cotisations versées.

- **Cotisations retenues :** cotisations salariales et patronales, sans les allègements sur les bas salaires (qui augmenteraient le rendement), et sans les impôts et transferts qui financent aussi les retraites (qui le diminueraient) (Annexe p. 24 ; Doc 2017 p. 6). En 2014, les cotisations représentaient 62 % des ressources du régime général et 79 % de celles de l'Arrco (Doc 2017 p. 6).
- **Pensions retenues :** droits propres seulement, sans pension de réversion ni droits familiaux.
- **Règles :** législation inchangée.
- **Durée de vie :** âge au décès = 60 ans + espérance de vie à 60 ans de la génération, **moyenne hommes et femmes confondus** (Insee 2026-2070 ; Annexe p. 24 ; Doc 2017 p. 6). Le COR ne publie pas la valeur retenue.
- **Départ :** au taux plein par la durée, carrière sans interruption (Doc 2017 p. 6).
- **Depuis le rapport 2026,** le rendement est calculé en net ; il l'était en brut auparavant (RA 2026 p. 140, note 140).

**Deux façons d'actualiser, donc deux séries de résultats :**

- **Selon les salaires moyens (SMPT).** Neutralise les différences de croissance entre générations ; c'est l'approche « du point de vue de l'assuré ». **C'est celle qui correspond au simulateur.**
- **Selon les prix.** Donne des valeurs plus élevées.

| Génération | 1960 | 1980 | 2000 | Source |
|---|---|---|---|---|
| Non-cadre, actualisation selon les salaires | ≈ 1,2 % | ≈ 0,8 % | 0,8 % | RA 2026 p. 140, figure 3.7 |
| Non-cadre, actualisation selon les prix | — | — | 1,5 % | Annexe p. 25, figure A2.13 |

**Par profil, génération 2000, actualisation selon les salaires** (RA 2026 p. 141, figure 3.A) :

| Profil | TRI | Espérance de vie retenue | CSG |
|---|---|---|---|
| Cadre | 0,0 % | La plus élevée | Taux plein |
| Non-cadre | 0,8 % | Moyenne | Taux plein |
| SMIC, toutes cotisations | 0,3 % | Celle des ouvriers | Taux réduit |
| SMIC, avec allègements de charges | 2,9 % | Celle des ouvriers | Taux réduit |

Pour ce calcul de rendement, le COR applique le taux plein de CSG au non-cadre, alors qu'il retient le taux intermédiaire pour son taux de remplacement.

**Pourquoi le cadre a le rendement le plus faible** (RA 2026 p. 140) :

- il paie des cotisations au-delà du plafond de la sécurité sociale qui n'ouvrent aucun droit au régime de base ;
- l'Agirc-Arrco, moins rentable que le régime de base, pèse plus lourd dans sa pension.

## 9. Minimum de pension (Drees, fiche 8)

- **Minimum contributif** au 1er janvier 2025, carrière complète : 747,69 € brut par mois, 893,65 € avec la majoration pour périodes cotisées.
- **Plafond :** il n'est versé que si l'ensemble des pensions ne dépasse pas 1 394,86 € par mois.
- **Revalorisation :** depuis la réforme de 2023, il suit le SMIC. Objectif : une pension brute d'au moins 85 % du SMIC net pour une carrière complète au SMIC.

## 10. Variantes de sensibilité (RA 2026 p. 24, figures 2.18 à 2.22)

Écart de **solde** du système par rapport au scénario de référence, en point de PIB. Le COR fait varier une hypothèse à la fois. Lecture graphique du graphique de synthèse p. 24 (± 0,05 point).

| Hypothèse | Variante | 2045 | 2070 |
|---|---|---|---|
| Fécondité (référence 1,45) | 1,7 enfant par femme | + 0,07 | + 0,9 |
| | 1,2 enfant par femme | − 0,03 | − 0,97 |
| Espérance de vie | Basse | + 0,37 | + 0,9 |
| | Haute | − 0,4 | − 0,95 |
| Solde migratoire (référence + 150 000) | + 230 000 par an | + 0,45 | + 1,05 |
| | + 70 000 par an | − 0,47 | − 0,97 |
| Chômage (référence 7 %) | 5 % | + 0,3 | + 0,22 |
| | 10 % | − 0,5 | − 0,3 |
| Productivité (référence 0,7 %) | 1,0 % par an | + 0,26 | + 0,7 |
| | 0,4 % par an | − 0,2 | − 0,68 |

- Solde migratoire : avec 230 000 personnes par an, les dépenses baisseraient d'environ 1,1 point de PIB en 2070 ; « l'écart sur le solde serait positif ou négatif, quasiment à due concurrence » (RA 2026 p. 112).
- Utilisation dans le simulateur : `calibration-leviers.md`.

## 11. Écarts entre le moteur de calcul du dossier et le COR

Le dossier recalcule les profils types du COR avec son propre moteur (`moteur-calcul/`), à partir des règles et des hypothèses ci-dessus. Seules les valeurs ci-dessous ont pu être comparées.

**Taux de remplacement** (pension nette ÷ dernier salaire net ; SMIC : pension brute ÷ salaire net)

| Profil | Génération 1960 : moteur / COR | Génération 1980 : moteur / COR | Génération 2000 : moteur / COR |
|---|---|---|---|
| Non-cadre | 71,2 % / ≈ 75 % | 68,3 % / ≈ 70 % | 66,8 % / ≈ 68,7 % |
| Cadre | 51,3 % / ≈ 51,5 % | 48,2 % / ≈ 48,5 % | 46,5 % / ≈ 46,5 % |
| SMIC | 86,7 % / ≈ 87 % | 82,1 % / ≈ 87,5 % | 80,3 % / ≈ 84,3 % |

- **Cadre :** reproduit.
- **Non-cadre :** sous-estimé de 2 points (4 pour la génération 1960, dont l'historique de l'Agirc-Arrco n'est pas modélisé).
- **SMIC :** sous-estimé de 4 à 5 points pour les générations 1980 et 2000.
- Explication non trouvée dans les sources. Le point commun au non-cadre et au SMIC est le poids du régime de base dans la pension : c'est probablement là que se trouve l'écart.

**Rendement des cotisations, génération 2000** (actualisation selon les salaires)

| Profil | Moteur | COR | Âge de décès retenu par le moteur |
|---|---|---|---|
| Cadre | 0,0 % | 0,0 % | 93,5 ans |
| SMIC, toutes cotisations | 0,3 % | 0,3 % | 89 ans |
| SMIC, avec allègements de charges | 2,9 % | 2,9 % | 89 ans |
| Non-cadre | 0,3 % | 0,8 % | 91 ans |

- Le COR ne publie pas les âges de décès qu'il retient. Ceux du moteur sont choisis pour reproduire le COR, avec 4,5 ans d'écart entre cadre et SMIC (l'Insee mesure 5,3 ans d'écart d'espérance de vie à 35 ans entre cadres et ouvriers).
**Rendement du non-cadre par génération** (moteur avec un âge de décès égal à celui des hommes + 0,2 an ; COR : figure 3.7, lecture graphique)

| Génération | 1960 | 1980 | 2000 |
|---|---|---|---|
| Moteur | 0,7 % | 0,05 % | 0,3 % |
| COR | ≈ 1,2 % | ≈ 0,8 % | 0,8 % |

- Le niveau est sous-estimé de 0,5 à 0,75 point selon la génération. Entre 1980 et 2000, le moteur fait remonter le rendement (+ 0,25 point) alors que le COR le voit stable.
- **Non-cadre : écart de 0,5 point, non expliqué.** Il faudrait un décès à 98,5 ans pour le combler. L'écart se situe surtout dans le régime de base (environ 0,9 % calculé contre 1,4 % publié, lecture graphique de la figure 3.A).
- Testé sans succès : une croissance des salaires plus lente. Elle relève le non-cadre, mais aussi le cadre et le SMIC, qui étaient justes.
- La méthode du COR (Doc 2017) ne contient pas les paramètres du rapport 2026.

## 12. Ce que le COR ne publie pas

- Taux de remplacement ou rendement **par décile** de salaire. Le dossier les calcule lui-même : voir `calculs-par-decile.md`.
- La RMPT en euros.
- Les profils de salaire en valeurs chiffrées : graphique seulement.
- Les valeurs exactes par génération du taux de remplacement et du rendement des profils : graphiques seulement, pour les générations 1940 à 2000. Rien pour la génération 2020.

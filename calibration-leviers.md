# Calibration des leviers du simulateur

*Rédigé le 6 octobre 2026. Ce fichier documente, levier par levier, comment le simulateur calcule l'effet de chaque curseur sur le solde du système (en point de PIB). Pour chaque levier : la source, les valeurs lues, la formule du simulateur, les valeurs de contrôle et les hypothèses propres au dossier. Les hypothèses du COR sont dans `hypotheses-COR.md` ; les variantes de sensibilité utilisées ici sont dans sa section 10.*

**Principe général.** Le solde de référence est celui du COR 2026 (Annexe, tableau A2.1). Chaque curseur ajoute un écart à ce solde. Les écarts des différents curseurs **s'additionnent** : c'est une hypothèse du dossier, le COR ne publie que des variantes un paramètre à la fois.

**Avancement**

| Levier | État |
|---|---|
| Âge légal, durée de cotisation, montée en charge | Recalé en v3 (voir `calculs-par-decile.md`, section 2 bis, et la section 9 ci-dessous) |
| Solde migratoire | **Recalé** (section 1 ci-dessous) |
| Indexation des pensions | **Recalé** (section 2) |
| Taux de cotisation salarié et employeur | **Recalé** (section 3) |
| Fécondité | **Recalé** (section 4) |
| Productivité | **Recalé** (section 6) |
| Chômage | **Recalé** (section 7) |
| Niveau de vie des retraités | **Recalé** (section 5) |

---

## 1. Solde migratoire

### Source

- RA 2026 p. 24, graphique de synthèse « Analyse de sensibilité : écarts de dépenses et de solde » (lecture graphique).
- RA 2026 p. 112-113, section 1.3 et figure 2.20 : avec 230 000 personnes par an, les dépenses baisseraient d'environ 1,1 point de PIB en 2070 ; avec 70 000, elles monteraient d'autant. « L'écart sur le solde serait positif ou négatif, quasiment à due concurrence. »

### Valeurs lues (écart de solde par rapport à la référence de + 150 000 par an)

| Variante | 2045 | 2070 |
|---|---|---|
| + 230 000 par an (+ 80 000) | + 0,45 point | + 1,05 point |
| + 70 000 par an (− 80 000) | − 0,47 point | − 0,97 point |
| **Moyenne des deux, en valeur absolue** | **0,46 point** | **1,01 point** |

Sur la figure 2.20, l'écart est quasi nul jusqu'en 2030, puis croît à peu près en ligne droite jusqu'en 2070.

### Pourquoi l'effet croît avec le temps

Un solde migratoire plus élevé ajoute surtout des personnes d'âge actif. Elles cotisent pendant des décennies avant de partir à la retraite. Le PIB augmente donc plus vite que les dépenses de retraite, et l'écart s'accumule année après année.

### Formule

**Avant (v2)** :

```
T = (année − 2024) / 46
écart = (solde − 150 000) / 50 000 × 0,2 × min(1, (année − 2024) / 8) × (1 − 0,25 × T)
```

Pour + 80 000 personnes, cela donnait + 0,28 point en 2045 et + 0,24 point en 2070. L'effet **diminuait** avec le temps, contrairement au COR, et il était 4 fois trop faible en 2070. Ces coefficients n'avaient pas de source.

**Après (v3)** :

```
écart = (solde − 150 000) / 80 000 × 1,01 × min(1, max(0, (année − 2027) / 43))
```

- 80 000 et 1,01 : moyenne des deux variantes du COR en 2070.
- (année − 2027) / 43 : montée en ligne droite de 0 en 2027 à 1 en 2070.

### Valeurs de contrôle

| Curseur | 2030 | 2045 | 2070 | COR |
|---|---|---|---|---|
| 230 000 par an | + 0,07 | + 0,42 | + 1,01 | + 0,45 (2045), + 1,05 (2070) |
| 70 000 par an | − 0,07 | − 0,42 | − 1,01 | − 0,47 (2045), − 0,97 (2070) |
| 0 (aucune migration nette) | − 0,13 | − 0,79 | − 1,89 | non publié (extrapolation) |
| 300 000 par an | + 0,13 | + 0,79 | + 1,89 | non publié (extrapolation) |

Calcul pour 2045 avec 230 000 : 80 000 / 80 000 × 1,01 × (2045 − 2027) / 43 = 1,01 × 0,419 = 0,42 point. Écart avec le COR : 0,03 à 0,05 point, sous la précision de la lecture graphique.

### Hypothèses du dossier

1. **Effet symétrique** : la même valeur est utilisée à la hausse et à la baisse (le COR donne + 1,05 et − 0,97 ; l'écart est faible).
2. **Effet proportionnel** : au-delà des variantes du COR (en dessous de 70 000 ou au-dessus de 230 000), l'effet est prolongé en ligne droite. Le COR n'a pas testé ces valeurs.
3. **Départ en 2027** : le changement de solde migratoire est supposé s'appliquer dès 2027.
4. **Additivité** avec les autres leviers (voir le principe général).

### Limites

- Le simulateur ne fait pas varier le nombre de retraités nés à l'étranger : il reprend l'effet global du COR sur le solde.
- La lecture graphique est précise à ± 0,05 point environ.

---

## 2. Indexation des pensions

### Ce que mesure le curseur

**Avant (v2)** : une position de − 1 (gel) à + 1 (salaires), sans unité. Le calcul du solde et celui du rendement (TRI) ne lui donnaient pas le même sens : − 0,54 point de PIB en 2070 pour le gel côté solde, soit l'équivalent d'une sous-indexation d'environ 0,3 point par an, alors que le TRI traitait le gel comme une perte de 2 % par an.

**Après (v3)** : l'**écart annuel entre la revalorisation des pensions et l'inflation**, en point par an, de − 2 à + 0,7.

| Position | Signification |
|---|---|
| 0 | Revalorisation sur les prix : règle actuelle, scénario du COR |
| − 2 | Gel des pensions, avec une inflation de 2 % par an (hypothèse du dossier) |
| + 0,7 | À peu près sur les salaires : croissance réelle des salaires de 0,7 % par an (COR) |

Le solde et le TRI utilisent maintenant la même valeur.

### Source

Le COR ne publie pas de variante d'indexation chiffrée en 2026. Le calcul est donc **mécanique**, à partir de trois données :

| Donnée | Valeur | Source |
|---|---|---|
| Dépenses de retraite | 14,1 % du PIB en 2025 et 2030, 14,2 % en 2045, 15,3 % en 2070 | RA 2026 p. 66-68 |
| Part des pensions dans ces dépenses | 401 Md€ sur 422 Md€ en 2025, soit 95 % | RA 2026 p. 66 |
| Survie après 65 ans | Tables de mortalité 2012-2016, ensemble, hommes et femmes | Insee, `morta_niv_2016.xls` |

Ordre de grandeur publié par le COR, pour contrôle : baisser **toutes** les pensions de 8,6 % dès 2026 équilibrerait le système en moyenne jusqu'en 2070 (RA 2026 p. 126, tableau 2.11).

### Mécanisme

Une sous-indexation ne touche pas une pension au moment où elle est liquidée. Elle la réduit **chaque année qui suit** : après a années, la pension vaut (1 − x)^a de ce qu'elle aurait été, x étant l'écart à l'inflation. L'effet sur la masse des pensions dépend donc de l'ancienneté des retraités :

- les premières années, seuls quelques points de revalorisation manquent ;
- l'effet grandit tant que la part des retraités touchés depuis longtemps augmente ;
- il se stabilise une fois que tous les retraités ont pris leur retraite après la mesure (vers 2060).

### Calcul

**Étape 1. Répartition de la masse des pensions selon l'ancienneté de la retraite** (script `moteur-calcul/indexation_stock.py`).

Pour chaque ancienneté a (de 0 à 45 ans) :

```
poids(a) ∝ survie(65 + a) / survie(65) × (1 − 0,74 %)^a
```

- survie : moyenne hommes / femmes des tables Insee ;
- (1 − 0,74 %)^a : une pension ancienne est plus basse qu'une pension récente, car elle a suivi les prix et non les salaires (perte de 0,74 % par an, valeur du moteur pour la génération 1980).

Résultat : ancienneté moyenne de 11,7 ans, pondérée par la masse. 5,0 % de la masse va aux retraités de l'année, 2,8 % à ceux partis il y a 19 ans, presque rien au-delà de 40 ans.

**Étape 2. Variation de la masse des pensions** après n revalorisations (n = année − 2026, première revalorisation touchée : janvier 2027) :

```
variation (%) = 100 × Σ poids(a) × [(1 + écart / 100)^min(a, n) − 1]
```

**Étape 3. Effet sur le solde** :

```
écart de solde (point de PIB) = − variation (%) / 100 × dépenses (% du PIB) × 401 / 422
```

Les dépenses sont interpolées en ligne droite entre les années publiées par le COR.

### Valeurs de contrôle

| Curseur | Masse des pensions 2045 | Masse 2070 | Solde 2030 | Solde 2045 | Solde 2070 |
|---|---|---|---|---|---|
| − 2 (gel) | − 18,6 % | − 20,0 % | + 0,91 | + 2,51 | + 2,91 |
| − 1 | − 9,9 % | − 10,8 % | + 0,46 | + 1,34 | + 1,57 |
| − 0,5 | − 5,1 % | − 5,6 % | + 0,23 | + 0,69 | + 0,82 |
| + 0,7 (≈ salaires) | + 7,8 % | + 8,7 % | − 0,33 | − 1,05 | − 1,27 |

Calcul pour − 1 en 2070 : la masse baisse de 10,8 % ; les pensions valent 15,3 × 401 / 422 = 14,5 % du PIB ; 10,8 % × 14,5 = 1,57 point.

Comparaison avec le COR : une sous-indexation de 0,75 point par an réduit la masse d'environ 8 % à long terme, l'ordre de grandeur des 8,6 % qui équilibrent le système jusqu'en 2070.

Ancien calcul (v2) : gel = + 0,54 point en 2070, soit 5 fois moins que le calcul mécanique.

### Effet sur le rendement (TRI)

La perte annuelle de la pension par rapport aux salaires devient : ERO − écart. Avec un gel, la pension perd 0,74 + 2 = 2,74 % par an ; avec + 0,7, elle ne perd presque plus rien (0,04 %). Les deux extrêmes donnent le même résultat qu'en v2, seule l'échelle du curseur change.

Génération 1980 : TRI de D1 + 0,19 % (référence), − 0,12 % avec − 1, − 0,44 % avec un gel ; D10 − 0,23 %, − 0,59 %, − 0,96 %.

### Hypothèses du dossier

1. **Seules les pensions déjà versées** sont touchées. La valeur d'achat des points Agirc-Arrco et la revalorisation des salaires portés au compte ne changent pas.
2. **Toutes les pensions** sont sous-indexées de la même façon, y compris les pensions de réversion.
3. **Inflation de 2 % par an** pour situer le gel.
4. **Survie 2012-2016** : les gains d'espérance de vie à venir allongeront la retraite, donc l'effet est un peu sous-estimé en 2070.
5. **Pas d'effet sur l'économie** : le COR note qu'une baisse des pensions réduit la consommation et l'activité à court terme (− 0,1 % de PIB pour 6 Md€, RA 2026 p. 121). Le simulateur ne le compte pas.

### Effet sur le niveau de vie des retraités

Voir la section 5 : gel − 13,4 points, − 1 point par an − 7,2 points en 2070.

---

## 3. Taux de cotisation (salarié et employeur)

### Ce que mesure le curseur

Le curseur ajoute des points de cotisation retraite sur l'**ensemble des revenus bruts d'activité** : salariés du privé, fonctionnaires, indépendants. C'est la convention du COR pour son « taux de prélèvement ». Une hausse limitée au privé rapporterait moins.

### Sources

| Donnée | Valeur | Source |
|---|---|---|
| Ressources du système | 13,9 % du PIB en 2025 | RA 2026 p. 7 |
| Taux de prélèvement (ressources ÷ revenus bruts d'activité) | 32,1 % en 2025, 30,0 % en 2070 | RA 2026 p. 81 |
| Hausse du taux de prélèvement pour équilibrer chaque année | + 0,5 point en 2030, + 2,1 en 2045, + 5,6 en 2070 | RA 2026 p. 124 |
| Déficit à combler | 0,2 point de PIB en 2030, 0,9 en 2045, 2,4 en 2070 | RA 2026 p. 7 |
| Effet sur le solde d'une hausse de 6 Md€ (0,2 point de PIB), après effets sur l'économie | Voir tableau ci-dessous | COR, séance du 26 mars 2026, doc n° 2, tableaux 1 et 2 |

### Étape 1. Ce que rapporte 1 point, avant effets sur l'économie

Deux calculs indépendants à partir du COR :

- **Par le taux de prélèvement** : 13,9 % du PIB ÷ 32,1 % = 43,3 %. Les revenus bruts d'activité valent 43 % du PIB.
- **Par l'équilibre** : 2,4 points de PIB ÷ 5,6 points de prélèvement = 0,43 en 2070 ; 0,9 ÷ 2,1 = 0,43 en 2045.

**1 point de cotisation = 0,43 point de PIB**, soit 0,43 % × 2 994 Md€ (PIB 2025) ≈ **13 Md€ par an**. La part reste à 43 % sur toute la projection (12,9 ÷ 30,0 = 43,0 % en 2070).

### Étape 2. Ce qu'il en reste après les effets sur l'économie

Une hausse de cotisation réduit le salaire net ou augmente le coût du travail. L'emploi et les salaires baissent un peu, donc une partie des recettes est perdue. Le COR a fait simuler une hausse de 6 Md€ (0,2 point de PIB) par trois équipes. Écart de solde du système, en point de PIB :

| Hausse de 6 Md€ | Modèle | 1 an | 2 ans | 5 ans | 10 ans | 20 ans | Long terme |
|---|---|---|---|---|---|---|---|
| Cotisations salariales | I-MIP | 0,19 | 0,19 | 0,19 | 0,19 | 0,19 | 0,19 |
| | OFCE | 0,20 | 0,19 | 0,18 | 0,18 | 0,19 | 0,20 |
| Cotisations employeur | I-MIP | 0,16 | 0,16 | 0,16 | 0,16 | 0,16 | 0,16 |
| | OFCE | 0,24 | 0,22 | 0,16 | 0,15 | 0,17 | 0,20 |

La DG Trésor ne publie pas cette ligne.

Part de l'effet qui reste (moyenne des deux modèles de 5 à 20 ans, divisée par 0,2) :

- **cotisations salariales : 0,187 ÷ 0,2 ≈ 93 %** ;
- **cotisations employeur : 0,16 ÷ 0,2 = 80 %**.

### Formule

**Avant (v2)**, sans source :

```
salarié : + 0,088 − 0,012 × T par point
employeur : + 0,132 − 0,038 × T par point     (T = 0 en 2024, 1 en 2070)
```

Soit environ 2,6 à 4 Md€ par point, et un effet patronal plus fort que l'effet salarial, à l'inverse des modèles du COR.

**Après (v3)**, à partir de 2027 :

```
écart de solde = points salarié × 0,43 × 0,93 + points employeur × 0,43 × 0,80
```

### Valeurs de contrôle

| Curseur | 2027 | 2045 | 2070 |
|---|---|---|---|
| + 1 point salarié | + 0,40 | + 0,40 | + 0,40 |
| + 1 point employeur | + 0,34 | + 0,34 | + 0,34 |
| + 5,6 points salarié | + 2,24 | + 2,24 | + 2,24 |

Contrôle : les 5,6 points du COR comblent 2,4 points de PIB **avant** effets sur l'économie (5,6 × 0,43 = 2,41). Le simulateur en garde 2,24, car il compte la perte liée à ces effets. Le COR prévient lui-même que l'ajustement « devra être en pratique plus élevé » pour cette raison (RA 2026 p. 125).

### Effet sur le rendement (TRI)

Les points ajoutés s'ajoutent au taux de cotisation de chaque décile (environ 28 % du salaire brut), sans ouvrir de droits nouveaux. Génération 1980, D5 : TRI de + 0,20 % à + 0,09 % avec 1 point de plus ; − 0,36 % avec 5,6 points.

### Hypothèses du dossier

1. **Assiette** : l'ensemble des revenus d'activité, comme le COR.
2. **Aucun droit nouveau** : la hausse finance le système sans augmenter les pensions.
3. **Part de l'effet qui reste constante** dans le temps (93 % et 80 %), fondée sur les horizons de 5 à 20 ans des modèles.
4. **Additivité** avec les autres leviers.

### Effet sur le niveau de vie des retraités

Aucun dans le simulateur : voir la section 5.

---

## 4. Fécondité

### Source

- RA 2026 p. 110 (section 1.1) : avec 1,2 enfant par femme, « l'écart serait nul jusqu'au milieu des années 2040 environ, puis irait en grandissant pour s'établir à 1 point de PIB à l'horizon 2070 » ; avec 1,7 enfant, les dépenses seraient « moins élevées de 1 point ». Les ressources en part de PIB ne bougent pas : le solde varie d'autant.
- RA 2026 p. 111, figure 2.18 (solde en % du PIB), et p. 24, graphique de synthèse : lecture graphique.

### Pourquoi l'effet est si tardif

Les dépenses de retraite ne changent pas avant 2070 : les enfants nés après 2025 ne seront pas encore retraités. Seul le PIB change, quand ces enfants arrivent sur le marché du travail, à partir du milieu des années 2040. Plus de naissances, c'est plus d'actifs, donc un PIB plus élevé et des dépenses plus faibles en part du PIB.

### Valeurs lues (écart de solde par rapport à la référence de 1,45 enfant par femme)

| Variante | 2045 | 2050 | 2060 | 2070 |
|---|---|---|---|---|
| 1,7 enfant par femme (+ 0,25) | ≈ 0 | ≈ + 0,2 | ≈ + 0,5 | + 0,91 |
| 1,2 enfant par femme (− 0,25) | ≈ 0 | ≈ − 0,2 | ≈ − 0,6 | − 0,98 |

Lecture graphique de la figure 2.18 (précision ± 0,05 point environ). Les courbes se séparent vers 2044, puis s'écartent à peu près en ligne droite. Le graphique p. 24 donne + 0,07 et − 0,03 en 2045.

### Formule

**Avant (v2)** :

```
écart = (fécondité − 1,45) × 3,2 × max(0, (année − 2042) / 28)
```

Pour + 0,25 enfant : + 0,80 point en 2070 (COR : + 0,91), avec un démarrage en 2042 (COR : vers 2044). Coefficient 3,2 sans source.

**Après (v3)** :

```
écart = (fécondité − 1,45) / 0,25 × 0,95 × max(0, (année − 2044) / 26)
```

- 0,25 et 0,95 : moyenne des deux variantes du COR en 2070 ((0,91 + 0,98) / 2 = 0,945, arrondi à 0,95).
- (année − 2044) / 26 : montée en ligne droite de 0 en 2044 à 1 en 2070.

### Valeurs de contrôle

| Curseur | 2045 | 2050 | 2060 | 2070 | COR |
|---|---|---|---|---|---|
| 1,7 | + 0,04 | + 0,22 | + 0,58 | + 0,95 | + 0,07 (2045), ≈ + 0,2 (2050), ≈ + 0,5 (2060), + 0,91 (2070) |
| 1,2 | − 0,04 | − 0,22 | − 0,58 | − 0,95 | − 0,03 (2045), ≈ − 0,2 (2050), ≈ − 0,6 (2060), − 0,98 (2070) |
| 1,8 (COR 2025) | + 0,05 | + 0,31 | + 0,82 | + 1,33 | non publié (extrapolation) |
| 2,1 | + 0,09 | + 0,57 | + 1,52 | + 2,47 | non publié (extrapolation) |

Calcul pour 1,8 en 2060 : 0,35 / 0,25 × 0,95 × (2060 − 2044) / 26 = 1,4 × 0,95 × 0,615 = 0,82 point.

### Curseur

Il va maintenant de 1,2 à 2,1 enfants par femme (v2 : de 1,4 à 2,1), pour couvrir la variante basse du COR.

### Hypothèses du dossier

1. **Effet symétrique** à la hausse et à la baisse (0,91 et 0,98 au COR).
2. **Effet proportionnel** au-delà des variantes du COR (au-dessus de 1,7) : prolongé en ligne droite, non testé par le COR.
3. **Additivité** avec les autres leviers.

---

## 5. Niveau de vie des retraités en 2070

### Ce que mesure l'indicateur

Le niveau de vie moyen des retraités rapporté à celui de l'ensemble de la population (définition du COR).

### Sources

| Donnée | Valeur | Source |
|---|---|---|
| Observé | 100,2 % en 2023 ; 106,5 % avec les loyers imputés | RA 2026 p. 12 |
| Projection de référence | 90,3 % en 2070 | RA 2026 p. 12 et 152 |
| Moteur de la baisse | « dépendrait pour l'essentiel de l'évolution de la pension moyenne relativement au revenu moyen d'activité » | RA 2026 p. 152 |
| Variantes de productivité | 0,4 % : pension relative 50,0 % au lieu de 47,9 %, niveau de vie + 3,1 points ; 1,0 % : 45,1 %, − 3,7 points | RA 2026 p. 199-200 |
| Variantes de chômage | 5 % : − 0,9 point ; 10 % : + 0,9 point (en moyenne) | RA 2026 p. 194-195 |
| Fécondité, espérance de vie | Effet « très limité » | RA 2026 p. 191 et 194 |

### Étape 1. Le lien entre pension relative et niveau de vie relatif

Les deux variantes de productivité du COR donnent ce lien :

| Variante | Pension relative | Écart | Niveau de vie | Écart | Rapport |
|---|---|---|---|---|---|
| 0,4 % | 50,0 % au lieu de 47,9 % | + 4,4 % | + 3,1 points sur 90,3 | + 3,4 % | 0,78 |
| 1,0 % | 45,1 % au lieu de 47,9 % | − 5,8 % | − 3,7 points sur 90,3 | − 4,1 % | 0,70 |

Moyenne : **0,74**. Quand la pension relative augmente de 1 %, le niveau de vie relatif augmente de 0,74 %. Il augmente moins, car les retraités ont aussi d'autres revenus (patrimoine, transferts).

### Étape 2. Les leviers qui changent la pension

```
niveau de vie 2070 = 90,3 × (1 + 0,74 × variation de la pension (%) / 100) + effet productivité + effet chômage
```

**Âge légal et durée** : variation moyenne de la pension des dix déciles des générations 1980 et 2000 (celles qui sont à la retraite en 2070), calculée par le moteur. Travailler plus longtemps donne plus de points Agirc-Arrco ; partir à 67 ans sans la durée complète réduit la pension de base.

**Indexation** : variation de la masse des pensions en 2070 (section 2), à nombre de retraités inchangé.

### Étape 3. Les leviers repris directement du COR

- **Productivité** : − 3,1 / 0,3 = − 10,3 points par point de productivité en dessous de 0,7 % ; − 3,7 / 0,3 = − 12,3 points par point au-dessus.
- **Chômage** : 0,9 / 2 = 0,45 point par point de chômage en dessous de 7 % ; 0,9 / 3 = 0,30 point par point au-dessus. Plus de chômage fait baisser le niveau de vie des actifs, donc celui de l'ensemble de la population.

### Formule

**Avant (v2)** :

```
87,5 + 0,9 × écart d'âge moyen + 9 × indexation (− 1 à + 1) + 11,5 × (0,7 − productivité) − 0,45 × cotisation salarié − 0,20 × cotisation employeur
```

Référence et coefficients sans source. Le signe des cotisations était discutable : une hausse des cotisations salariales réduit le revenu des actifs, ce qui ferait plutôt **monter** le niveau de vie relatif des retraités.

### Valeurs de contrôle

| Scénario | Variation de la pension | Niveau de vie 2070 |
|---|---|---|
| Référence | 0 | 90,3 % |
| Âge légal 65 ans | + 0,7 % | 90,8 % |
| Âge légal 67 ans | + 2,0 % | 91,6 % |
| 45 ans de cotisation | − 0,6 % | 89,9 % |
| 65 ans et 45 ans (Philippe) | 0,0 % | 90,3 % |
| Âge légal 62 ans | − 1,2 % | 89,5 % |
| Indexation − 1 point par an | − 10,8 % | 83,1 % |
| Gel des pensions | − 20,0 % | 76,9 % |
| Productivité 0,4 % | — | 93,4 % (COR : 93,4 %) |
| Productivité 1,0 % | — | 86,6 % (COR : 86,6 %) |
| Chômage 5 % / 10 % | — | 89,4 % / 91,2 % |

Calcul pour l'indexation à − 1 point par an : 90,3 × (1 − 0,74 × 10,8 %) = 90,3 × 0,920 = 83,1 %.

### Hypothèses du dossier

1. **Rapport de 0,74** tiré des variantes de productivité, appliqué aux autres leviers.
2. **Âge et durée** : moyenne simple des déciles des générations 1980 et 2000.
3. **Cotisations : pas d'effet.** Le COR ne publie rien. Une hausse réduit le revenu net des actifs et ferait plutôt monter le niveau de vie relatif des retraités, sans chiffrage disponible.
4. **Fécondité et solde migratoire : pas d'effet**, comme le COR l'indique pour la fécondité.
5. **Additivité** entre leviers.

### Correction faite en même temps : la surcote

Le moteur donnait une surcote de 5 % par an à ceux qui attendent l'âge légal alors qu'ils ont déjà leur durée complète. Ce n'est pas la règle : la surcote ne compte que les années travaillées **après l'âge légal et après la durée complète**. Dans le simulateur, chacun part dès qu'il a le taux plein : la surcote est donc toujours nulle. Les valeurs de référence (taux de remplacement, TRI, tableaux de `calculs-par-decile.md`) ne changent pas, car personne n'avait de surcote avec les règles actuelles. Seuls les scénarios qui relèvent l'âge légal changent : avec 67 ans, la pension moyenne augmente de 2,0 % au lieu de 7,8 %.

---

## 6. Productivité

### Source

RA 2026 p. 24, graphique de synthèse (lecture graphique), et figure 2.22. Écart de solde par rapport à la référence de 0,7 % par an :

| Variante | 2045 | 2070 |
|---|---|---|
| 1,0 % par an (+ 0,3) | + 0,26 | + 0,7 |
| 0,4 % par an (− 0,3) | − 0,2 | − 0,68 |
| **Moyenne, en valeur absolue** | **0,23** | **0,69** |

### Formule

**Avant (v2)** : `(productivité − 0,7) / 0,3 × 0,72 × (année − 2024) / 46`, soit 0,33 point en 2045 (COR : 0,23) et 0,72 en 2070. Coefficient sans source, trop fort en 2045.

**Après (v3)** : `(productivité − 0,7) / 0,3 × k(année)`, avec k sur une ligne brisée : 0 en 2027, 0,23 en 2045, 0,69 en 2070.

### Valeurs de contrôle

| Curseur | 2030 | 2040 | 2045 | 2070 |
|---|---|---|---|---|
| 1,0 % | + 0,04 | + 0,17 | + 0,23 | + 0,69 |
| 0,4 % | − 0,04 | − 0,17 | − 0,23 | − 0,69 |

### Hypothèses du dossier

Effet symétrique (moyenne des deux variantes), ligne droite entre les années publiées, prolongement en ligne droite au-delà de 0,4 % et 1,0 %.

---

## 7. Chômage

### Source

- RA 2026 p. 24, graphique de synthèse : écart de solde de + 0,3 / − 0,5 point en 2045 pour 5 % / 10 % de chômage, + 0,22 / − 0,3 en 2070.
- RA 2026 p. 114, figure 2.21 et texte : en 2070, − 0,3 point avec 10 % et + 0,2 point avec 5 %. Les courbes s'écartent dès 2028-2030 et l'écart est atteint vers 2040, date à laquelle le chômage rejoint sa cible.

### Calcul

Écart par point de chômage :

| | 5 % (− 2 points) | 10 % (+ 3 points) | Moyenne par point |
|---|---|---|---|
| 2045 | 0,3 / 2 = 0,150 | 0,5 / 3 = 0,167 | 0,158 |
| 2070 | 0,22 / 2 = 0,110 | 0,3 / 3 = 0,100 | 0,105 |

### Formule

**Avant (v2)** : `(7 − chômage) / 2 × 0,20 × min(1, (année − 2032) / 10)`, soit 0,10 par point à partir de 2042. Juste en 2070, trop faible de 35 % en 2045, et départ en 2032 au lieu de 2027.

**Après (v3)** : `(7 − chômage) × k(année)`, avec k : 0 en 2027, montée en ligne droite jusqu'à 0,158 en 2040, palier jusqu'en 2045, puis baisse en ligne droite jusqu'à 0,105 en 2070.

La baisse après 2045 reproduit les chiffres du COR ; le rapport n'en détaille pas la cause.

### Valeurs de contrôle

| Curseur | 2030 | 2040 | 2045 | 2070 | COR (2045 / 2070) |
|---|---|---|---|---|---|
| 5 % | + 0,07 | + 0,32 | + 0,32 | + 0,21 | + 0,3 / + 0,22 |
| 10 % | − 0,11 | − 0,47 | − 0,47 | − 0,32 | − 0,5 / − 0,3 |

### Hypothèses du dossier

Effet proportionnel au nombre de points de chômage (moyenne des deux variantes), palier entre 2040 et 2045.

---

## 8. Scénario de référence et conversion en milliards

**Points du COR utilisés** (solde en % du PIB) : 2024 − 0,1 ; 2030 − 0,2 ; 2038 − 0,5 ; 2048 − 1,1 ; 2050 − 1,2 ; 2070 − 2,4 (Annexe, tableau A2.1) ; 2045 − 0,9 (RA 2026 p. 7). Ligne droite entre ces points. La v2 n'utilisait que 2024, 2030, 2045 et 2070.

**PIB 2035** (encadré « Équilibre à 10 ans ») :

- PIB 2025 = 422,2 Md€ ÷ 14,1 % = 2 994 Md€ (RA 2026 p. 66) ;
- PIB 2030 ≈ 6,8 Md€ ÷ 0,2 % = 3 400 Md€ (RA 2026 p. 7), soit + 2,6 % par an en valeur ;
- PIB 2035 ≈ 3 400 × 1,026^5 ≈ **3 870 Md€** (hypothèse du dossier : même rythme jusqu'en 2035).

La v2 retenait 3 762 Md€, à partir d'un déficit 2030 de 6,6 Md€ (le COR écrit 6,8).

**Solde 2035 de référence** : − 0,39 % × 3 870 = − 15,0 Md€ (v2 : − 16,3).

**Exemple Philippe** (65 ans, 45 ans de cotisation), solde 2035 : + 11,5 Md€ en application immédiate, + 7,9 sur 4 ans, + 3,0 sur 8 ans, − 1,8 sur 12 ans, − 5,1 sur 16 ans, − 7,1 sur 20 ans. En 2070 : − 1,28 % du PIB.

---

## 9. Départs à 67 ans (correction du 6 octobre 2026)

### Le problème

Le simulateur suppose des carrières continues depuis l'âge d'entrée. Le groupe entré le plus tard (25,3 ans, 40 % de la génération) n'atteint jamais les 43 ans de cotisation avant 67 ans : tous ses membres attendaient le taux plein automatique. Une fois retirés les 26 % qui partent à l'âge légal, 30 % de la génération partait à 67 ans.

### Ce que disent les sources

| Donnée | Valeur | Source |
|---|---|---|
| Départs à 67 ans, nouveaux retraités récents | 7,6 % des hommes, 10,5 % des femmes | RA 2026 p. 218 |
| Départs au taux plein par l'âge, régime général, génération 1956 | 7 % | Drees, panorama 2025, fiche 17, graphique 2 |
| Départs à l'âge d'annulation de la décote, génération 1953 | 10 % | Drees, panorama 2025, fiche 17, graphique 1 |
| Âge moyen de départ, générations nées à partir de 1975 | 64,6 ans | RA 2026 p. 215 |

### La correction

Dans le groupe entré le plus tard, une partie a des années validées en plus de son emploi : trimestres avant la première année complète, chômage indemnisé, maladie, enfants. Elle atteint sa durée plus tôt. Deux paramètres :

- **part qui attend 67 ans : 30 %** du groupe ;
- **années validées en plus pour les 70 % restants : 2,5 ans**, soit un départ à 65,8 ans au lieu de 67.

Ils sont choisis pour retrouver deux chiffres du COR :

```
départs à 67 ans = 74 % × 40 % × 30 % = 8,9 % de la génération (COR : environ 9 %)
âge moyen = 26 % × 64 + 74 % × (5 % × 62,5 + 28 % × 63,1 + 27 % × 64,9 + 40 % × (30 % × 67 + 70 % × 65,8)) = 64,6 ans (COR : 64,6)
```

Les années validées en plus comptent pour la durée (régime de base) mais pas pour les points Agirc-Arrco, qui ne viennent que de l'emploi.

### Ce qui change

| Indicateur | Avant | Après |
|---|---|---|
| Âge moyen de départ, génération 1980 | 64,8 ans | 64,6 ans |
| Part de départs à 67 ans | 30 % | 8,9 % |
| Un an d'âge légal en plus (solde 2070) | + 0,38 point | + 0,38 point |
| 45 ans de cotisation (solde 2070) | + 0,71 point | + 0,91 point |
| 65 ans et 45 ans (solde 2070) | + 0,92 point | + 1,12 point |
| TRI génération 1980, D1 / D10 | + 0,19 % / − 0,23 % | + 0,23 % / − 0,13 % |
| TRI uniforme à coût nul (repère « réf. ») | + 0,12 % | + 0,18 % |

L'effet de l'âge légal ne change pas : le groupe corrigé part après l'âge légal. L'effet de la durée augmente : les 70 % qui partaient à 65,8 ans sont désormais concernés par une hausse de la durée.

### Hypothèses du dossier

1. **Part de départs à 67 ans** des générations récentes appliquée à la génération 1980. Elle sera sans doute un peu plus élevée en réalité (entrée plus tardive, 43 ans exigés).
2. **Même correction dans tous les déciles**, appliquée au seul groupe entré tard.

# Taux de remplacement et rendement des cotisations par décile

*Calcul du 6 octobre 2026. Ni le COR ni la Drees ne publient ces indicateurs par décile de salaire. Ils sont **calculés** par le moteur du dossier (`moteur-calcul/`), à partir des règles de calcul des pensions et des hypothèses du COR (`hypotheses-COR.md`). Les écarts entre ce moteur et les valeurs publiées par le COR sont dans `hypotheses-COR.md`, section 11.*

Pour relancer tous les calculs : `python3 lancer.py` dans le dossier `moteur-calcul/`.

---

## 1. Résultats

Salariés du privé, génération 1980, personne seule. Taux de remplacement : carrière complète de 43 ans. Rendement : âges d'entrée et de départ propres à chaque décile (section 2 bis).

| Groupe | Salaire net moyen de carrière (€ par mois) | Dernier salaire brut (€ par mois) | Pension brute (€ par mois) | Taux de remplacement : pension nette ÷ dernier salaire net | Taux de remplacement : pension brute ÷ salaire brut moyen de carrière | Âge de décès | Rendement des cotisations |
|---|---|---|---|---|---|---|---|
| D1 | 1 446 | 1 827 | 1 160 | 80 % | 64 % | 85,7 | + 0,23 % |
| D2 | 1 580 | 2 147 | 1 258 | 71 % | 63 % | 86,5 | + 0,16 % |
| D3 | 1 746 | 2 373 | 1 390 | 71 % | 63 % | 87,1 | + 0,19 % |
| D4 | 1 908 | 2 633 | 1 531 | 70 % | 64 % | 87,6 | + 0,30 % |
| D5 | 2 091 | 2 931 | 1 692 | 67 % | 64 % | 88,1 | + 0,25 % |
| D6 | 2 316 | 3 303 | 1 892 | 67 % | 65 % | 88,5 | + 0,35 % |
| D7 | 2 614 | 3 803 | 2 159 | 66 % | 65 % | 89,0 | + 0,40 % |
| D8 | 3 045 | 4 540 | 2 419 | 62 % | 63 % | 89,5 | + 0,35 % |
| D9 | 3 820 | 5 893 | 2 802 | 54 % | 58 % | 90,3 | + 0,08 % |
| D10 | 5 593 | 9 094 | 3 734 | 47 % | 53 % | 91,2 | − 0,13 % |

**Rendement des cotisations, toutes générations** (même méthode ; départ au taux plein ; âge de décès : espérance de vie des hommes de chaque génération, Insee, corrigée par décile)

| Génération | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960 | + 0,47 % | + 0,60 % | + 0,60 % | + 0,64 % | + 0,68 % | + 0,81 % | + 0,83 % | + 0,76 % | + 0,70 % | + 0,54 % |
| 1980 | + 0,23 % | + 0,16 % | + 0,19 % | + 0,30 % | + 0,25 % | + 0,35 % | + 0,40 % | + 0,35 % | + 0,08 % | − 0,13 % |
| 2000 | + 0,39 % | + 0,30 % | + 0,33 % | + 0,45 % | + 0,38 % | + 0,48 % | + 0,53 % | + 0,47 % | + 0,18 % | − 0,02 % |
| 2020 | + 0,58 % | + 0,49 % | + 0,52 % | + 0,60 % | + 0,56 % | + 0,64 % | + 0,68 % | + 0,63 % | + 0,35 % | + 0,11 % |

Valeurs affichées par le simulateur v3 (règles actuelles : âge légal 64 ans, 43 ans de cotisation ; génération 1960 : entrée à 19,25 ans, départ à 62,25 ans).

- **Entre générations,** la génération 1960 est la mieux servie : elle a cotisé à des taux plus faibles (25 % en moyenne sur sa carrière, contre 28 % ensuite) et a pu partir plus tôt. La génération 1980 est la moins bien servie. Les suivantes remontent un peu grâce aux gains d'espérance de vie (+ 2,1 ans entre 1980 et 2000, + 1,9 an entre 2000 et 2020).
- **Le COR, lui, voit le rendement du non-cadre stable** de la génération 1980 à la génération 2000 (0,8 % les deux fois), alors que le moteur le fait remonter de 0,25 point. Cet écart est noté dans `hypotheses-COR.md`, section 11.
- La génération 2020 n'est pas couverte par le COR, dont les graphiques s'arrêtent à 2000. Ses résultats sont une extrapolation à règles inchangées.

**Comment lire le rendement.** C'est le taux auquel il aurait fallu placer ses cotisations pour obtenir exactement les pensions reçues, au-delà de la hausse générale des salaires. 0 % signifie qu'on récupère ce qu'on a versé, revalorisé comme les salaires.

**Pourquoi le rendement est le plus haut au milieu (D4 à D8) :**

1. **En bas (D1-D3),** l'espérance de vie est la plus courte : la pension est versée moins longtemps. Le minimum de pension et les départs anticipés pour carrière longue compensent en partie.
2. **En haut (D9-D10),** une partie des cotisations ne rapporte rien, car le régime de base ne verse rien au-dessus du plafond de la sécurité sociale. Et la pension dépend davantage de l'Agirc-Arrco, moins rentable que le régime de base. Entrés tard, une partie (16 % de D10) attend 67 ans faute d'avoir la durée complète. L'espérance de vie plus longue ne compense pas.
3. **Au milieu,** le salaire reste sous le plafond, et l'espérance de vie est proche de la moyenne ou au-dessus.

## 2. Méthode

**Salaire de chaque groupe.** Les seuils de déciles du salaire net du privé en équivalent temps plein (Insee Première n° 2079, 2024) sont : 1 492, 1 669, 1 823, 1 992, 2 190, 2 442, 2 785, 3 305 et 4 334 €, et 5 593 € pour le seuil des 5 % les mieux payés.

- Chaque groupe prend le milieu entre ses deux seuils.
- D1 se situe entre le SMIC net (≈ 1 400 €, estimé) et 1 492 €.
- D10 prend le seuil des 5 % (5 593 €), c'est-à-dire le milieu du groupe.

Ces salaires, observés tous âges confondus, sont traités comme le salaire moyen de carrière de chaque groupe.

**Évolution du salaire au fil de la carrière** (profils du COR, `hypotheses-COR.md` section 5) :

| Groupe | Profil appliqué |
|---|---|
| D1 | Plat, au niveau du SMIC (profil SMIC du COR) |
| D2, D3 | Profil « non-cadre » du COR, défini comme le salaire moyen du tiers le moins payé |
| D10 | Profil « cadre » du COR, défini comme le salaire moyen du dernier décile |
| D4 à D9 | **Hypothèse du dossier :** mélange des deux profils, de plus en plus proche du profil cadre à mesure que le salaire monte |

**Règles de calcul (législation actuelle) :**

| Élément | Valeur |
|---|---|
| Régime de base | 50 % de la moyenne des 25 meilleures années, plafonnées, revalorisées sur les prix ; pension revalorisée sur les prix |
| Agirc-Arrco | Points à 6,20 % du salaire jusqu'au plafond, 17 % au-delà ; valeur du point selon le pilotage du COR (`hypotheses-COR.md` section 4) |
| Minimum contributif | 893,65 € par mois avec la majoration (2025), plafond tous régimes 1 394,86 €, indexé sur le SMIC |
| Cotisations retenues | Salariales et patronales, sans les allègements (convention du COR) : 27,98 % sous le plafond ; au-dessus, 2,51 % au régime de base (sans droits) et 24,29 % à l'Agirc-Arrco, plus 0,35 % sur tout le salaire |
| CSG sur les pensions | Selon les seuils 2026 pour une personne seule. D1 est exonéré ; taux réduit de D2 à D4, intermédiaire de D5 à D8, plein pour D9 et D10 |
| Âge de décès | Celui du simulateur : espérance de vie des hommes de la génération 1980 (88,7 ans en moyenne, Insee), corrigée de l'écart par décile de niveau de vie (Insee 2012-2016) |
| Actualisation | Selon les salaires moyens, comme le COR (figure 3.7) |
| Croissance réelle des salaires | 0,7 % par an |

## 2 bis. Âges d'entrée et de départ par décile

Le COR donne presque le même âge d'entrée à ses profils non-cadre et cadre. Or l'âge d'entrée décide qui est touché par l'âge légal (ceux qui ont commencé tôt) et par la durée (ceux qui ont commencé tard). Il est donc reconstitué par décile (script `moteur-calcul/entree_par_decile.py`).

1. **Catégorie socioprofessionnelle dans chaque décile.** On part des salaires moyens et des effectifs de l'Insee : cadres 4 629 €, professions intermédiaires 2 633 €, employés 1 941 €, ouvriers 2 051 € net par mois. **Hypothèse du dossier :** salaires log-normaux dans chaque catégorie, avec une dispersion calée sur les déciles Insee (retrouvés à 1,3 point près).
2. **Âge de fin d'études selon la catégorie.** On combine deux graphiques de la Dares (note pour le COR, mai 2023). Le graphique 10 donne la catégorie à 35-45 ans selon l'âge de fin d'études. Le graphique 1 donne la répartition des âges de fin d'études de la génération 1980 : 5 % à 16 ans ou moins, 28 % entre 17 et 19 ans, 27 % entre 20 et 21 ans, 40 % à 22 ans ou plus.
3. **Âge d'entrée dans la vie active.** On ajoute à l'âge de fin d'études le délai d'accès au premier emploi (Dares, graphique 18). **Hypothèse du dossier :** on ajoute aussi un décalage uniforme de 1,5 an, pour retrouver l'âge moyen de la première année complète validée mesuré par la Drees (22,65 ans).

**Départs à l'âge légal quelle que soit la durée.** Les carrières continues ne suffisent pas : beaucoup d'assurés partent dès l'âge légal sans avoir leur durée. Pour la génération 1953 (Drees, panorama 2025, fiche 17, graphique 1), c'est le cas de 26 % des retraités :

- 11 % partis avec une décote ;
- 8 % d'anciens invalides ;
- 7 % de personnes reconnues inaptes au travail.

**Hypothèses du dossier :**

- ce groupe représente 26 % de chaque décile ;
- il part à l'âge légal, avec une pension au prorata des années cotisées, sans décote supplémentaire ;
- son âge d'entrée est l'âge moyen du décile.

Les 74 % restants se répartissent entre les quatre groupes ci-dessous.

**Règle de départ** (législation actuelle) :

- Départ au plus tard entre l'âge légal et l'âge où la durée requise est atteinte, sans dépasser 67 ans (taux plein automatique).
- Dans le groupe entré le plus tard, 70 % ont 2,5 années validées sans emploi (périodes avant la première année complète, chômage, maladie, enfants) et atteignent leur durée plus tôt ; 30 % attendent 67 ans. Ces deux valeurs sont choisies pour retrouver deux chiffres du COR : l'âge moyen de départ des générations nées à partir de 1975 (64,6 ans, RA 2026 p. 215) et la part de départs à 67 ans (environ 9 %, RA 2026 p. 218). Sans ce calage, 30 % de la génération partirait à 67 ans (détail : `calibration-leviers.md`, section 9).
- Retraite anticipée pour carrière longue : âge légal − 2 ans pour un début avant 20 ans, − 1 an pour un début avant 21 ans.

| Groupe (fin d'études) | Entrée | Départ (64 ans, 43 ans de cotisation) |
|---|---|---|
| 16 ans ou moins | 19,5 ans | 62,5 ans (carrière longue) |
| 17-19 ans | 20,1 ans | 63,1 ans (carrière longue) |
| 20-21 ans | 21,9 ans | 64,9 ans (durée atteinte) |
| 22 ans ou plus, 30 % du groupe | 25,3 ans | 67 ans (durée incomplète : 41,7 ans) |
| 22 ans ou plus, 70 % du groupe | 25,3 ans, avec 2,5 années validées sans emploi | 65,8 ans (durée atteinte) |

| | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Âge moyen d'entrée | 21,8 | 21,9 | 21,9 | 21,9 | 22,0 | 22,2 | 22,4 | 22,8 | 23,4 | 24,1 |
| Âge moyen de départ | 64,2 | 64,2 | 64,3 | 64,3 | 64,3 | 64,4 | 64,4 | 64,6 | 64,9 | 65,2 |

- **Âge moyen de départ de la génération : 64,6 ans**, comme le COR pour les générations nées à partir de 1975. Part de départs à 67 ans : 8,9 %.
- **Vérification sur le COR :** un an d'âge légal en plus recule l'âge moyen de 0,5 an. Cela améliore le solde de 0,38 point de PIB en 2070 (0,8 point par an d'âge moyen, RA 2026 p. 124). Le COR donne + 0,2 à + 0,4 point (séance du 26 mars 2026).
- **Écart avec le COR :** le calcul donne 24,1 ans d'entrée pour D10 (profil cadre du COR : 22,75 ans) et 21,9 ans pour D2-D3 (profil non-cadre : 22,5 ans).

**Pension selon le départ :** pension au prorata des années cotisées pour ceux qui partent à 67 ans sans la durée ; points Agirc-Arrco en plus pour chaque année travaillée en plus. Pas de surcote : elle ne compte que les années travaillées après l'âge légal et après la durée complète, et chacun part dès qu'il a le taux plein.

## 3. Fiabilité

- **Les écarts entre déciles sont fiables.** Le moteur reproduit les rendements publiés par le COR pour le cadre et pour le SMIC (génération 2000).
- **Le niveau est probablement sous-estimé :**
  - pour le non-cadre, le moteur trouve 0,5 à 0,75 point de moins que le COR selon la génération (écart non expliqué) ;
  - le simulateur retient l'espérance de vie des hommes, alors que le COR prend la moyenne hommes et femmes, plus élevée.

  Les deux effets jouent dans le même sens. Le premier vaut 0,5 à 0,75 point selon la génération ; le second n'est pas chiffré.
- **Allègements de charges :** non comptés, comme le fait le COR. Comptés, ils relèveraient fortement le rendement des bas salaires (pour le SMIC : 2,9 % au lieu de 0,3 %, génération 2000).

## 4. Limites

- **Carrières continues**, à temps plein, sans chômage ni enfant.
- **D4 à D9** : le mélange des profils est une hypothèse.
- **Taux de remplacement : génération 1980 seulement.** Le rendement est calculé pour les quatre générations.
- **Génération 1960 :** l'historique de l'Agirc-Arrco (rendement plus élevé avant 2019) et l'ancien minimum contributif ne sont pas modélisés ; ses taux de cotisation sont ramenés à la moyenne publiée par le COR (25 %).
- **Carrières hachées :** en dehors du groupe qui part à l'âge légal, le calcul suppose des carrières continues depuis l'entrée. La part de ce groupe est la même dans tous les déciles, faute de source par niveau de salaire.
- **Carrière longue :** les conditions exactes (trimestres cotisés avant 20 ou 21 ans) sont approchées par l'âge d'entrée moyen de chaque groupe.

## Sources

- `hypotheses-COR.md` (COR rapport 2026, annexe méthodologique 2026, rapport 2025, document de séance de 2017 ; Drees 2025)
- [Insee Première n° 2079, Les salaires dans le secteur privé en 2024](https://www.insee.fr/fr/statistiques/8657156)
- [Légisocial, taux de cotisations 2026](https://www.legisocial.fr/reperes-sociaux/taux-cotisations-sociales-urssaf-2026.html)
- [Moneyvox, seuils de CSG 2026 des retraités](https://www.moneyvox.fr/impot/actualites/106683/assurance-retraite-agirc-arrco-voici-votre-taux-officiel-de-csg-2026-selon-vos-revenus)
- Insee, espérance de vie par génération et par niveau de vie : déjà utilisée par le simulateur v2 (`donnees-reference-COR.md`)
- Dares, *Comment l'âge de sortie des études initiales s'articule-t-il avec le début de carrière professionnelle ?*, note pour le COR, mai 2023 (`Sources/`)
- Insee Première n° 2079 : salaires moyens et effectifs par catégorie socioprofessionnelle
- Drees, *Les retraités et les retraites*, édition 2025, fiche 17 : conditions de liquidation de la génération 1953

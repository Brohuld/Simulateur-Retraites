"""Répartition de la masse des pensions selon l'ancienneté de la retraite.

Sert au curseur « indexation » du simulateur : une sous-indexation de x point par an
réduit une pension liquidée il y a a années de (1 - x)^a. L'effet sur la masse dépend
donc de la part de la masse versée à chaque ancienneté a.

Hypothèses du dossier :
- départ à 65 ans (âge moyen de départ du simulateur : 64,8 ans) ;
- survie : tables Insee 2012-2016, ensemble des niveaux de vie, moyenne hommes / femmes ;
- une pension liquidée il y a a années vaut (1 - 0,74 %)^a d'une pension nouvelle
  (perte annuelle par rapport aux salaires avec une indexation sur les prix, ERO du moteur).
"""
import xlrd, os
here = os.path.dirname(os.path.abspath(__file__))
b = xlrd.open_workbook(os.path.join(here, "..", "morta_niv_2016.xls"))

def survie(sheet):
    s = b.sheet_by_name(sheet); out = {}
    for r in range(s.nrows):
        v = s.row_values(r)
        if str(v[0]).strip().isdigit() and isinstance(v[2], float):
            out[int(str(v[0]).strip())] = v[2]
    return out

H, F = survie("H - 2012_2016"), survie("F - 2012_2016")
DEP, ERO, AMAX = 65, 0.0074, 45
w = []
for a in range(AMAX + 1):
    age = DEP + a
    s = 0.5 * H.get(age, 0) / H[DEP] + 0.5 * F.get(age, 0) / F[DEP]
    w.append(s * (1 - ERO) ** a)
tot = sum(w); w = [x / tot for x in w]
moy = sum(a * x for a, x in enumerate(w))
print("Ancienneté moyenne pondérée par la masse : %.1f ans" % moy)
print("POIDS =", "[" + ", ".join("%.4f" % x for x in w) + "]")

def baisse(ecart_pt, n):
    """Variation de la masse (en %) après n revalorisations à ecart_pt point par an de l'inflation."""
    e = ecart_pt / 100
    return 100 * sum(x * ((1 + e) ** min(a, n) - 1) for a, x in enumerate(w))

for e in (-2, -1, -0.5, 0.7):
    print("écart %+.1f pt/an :" % e, " ".join("%d: %+.1f %%" % (2026 + n, baisse(e, n)) for n in (4, 19, 44)))

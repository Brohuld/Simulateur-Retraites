# Âge d'entrée dans la vie active par décile de salaire — génération 1980.
# Sources : Insee Première n° 2079 (2024) ; Dares, note pour le COR, mai 2023 (graphiques 1, 10, 18) ; Drees, panorama 2025 (fiche 12).
import sys; sys.dont_write_bytecode=True
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize

# 1. Insee 2024 : salaire net EQTP moyen et part des effectifs par catégorie
CSP=["cadres","PI","employes","ouvriers"]
MOY=np.array([4629,2633,1941,2051.]); W=np.array([23.0,20.6,27.9,28.6]); W=W/W.sum()
DECILES=np.array([1492,1669,1823,1992,2190,2442,2785,3305,4334.])   # seuils D1..D9

# Hypothèse du dossier : salaires log-normaux dans chaque catégorie ; dispersion calée sur les déciles Insee
def cdf(x,sig):
    mu=np.log(MOY)-sig**2/2
    return sum(W[i]*norm.cdf((np.log(x)-mu[i])/sig[i]) for i in range(4))
def err(s):
    s=np.abs(s); return sum((cdf(d,s)-q)**2 for d,q in zip(DECILES,np.arange(.1,1,.1)))
res=minimize(err,[0.4,0.25,0.2,0.2],method="Nelder-Mead",options={"xatol":1e-6,"fatol":1e-10,"maxiter":5000})
SIG=np.abs(res.x)

# 2. Part de chaque catégorie dans chaque décile
bornes=np.concatenate([[1.0],DECILES,[1e7]])
def p_csp_decile():
    mu=np.log(MOY)-SIG**2/2; out=[]
    for d in range(10):
        a,b=bornes[d],bornes[d+1]
        m=np.array([W[i]*(norm.cdf((np.log(b)-mu[i])/SIG[i])-norm.cdf((np.log(a)-mu[i])/SIG[i])) for i in range(4)])
        out.append(m/m.sum())
    return np.array(out)

# 3. Dares : âge de fin d'études (groupes) — génération 1980 (graphique 1, lecture graphique)
GROUPES=["16 ans ou moins","17-19 ans","20-21 ans","22 ans ou plus"]
P_G=np.array([0.05,0.28,0.27,0.40])
AGE_FIN=np.array([15.8,18.18,20.48,23.85])        # moyenne dans chaque groupe (graphique 1 ; « 25 ans et + » compté 26 ans)
DELAI=np.array([2.25,0.49,-0.03,-0.03])           # délai moyen fin d'études -> premier emploi (graphique 18, sortis 1994-2001)
# Catégorie à 35-45 ans selon la fin d'études (graphique 10), salariés seulement (artisans et agriculteurs retirés)
P_C_SACH_G=np.array([  # cadres, PI, employés, ouvriers
    [2.5,11.5,32.5,45.0],
    [5.0,20.0,33.0,33.0],
    [13.5,31.5,31.5,15.5],
    [40.0,35.0,15.0,5.0]])
P_C_SACH_G=P_C_SACH_G/P_C_SACH_G.sum(1,keepdims=True)
# Bayes : P(groupe | catégorie)
joint=P_C_SACH_G*P_G[:,None]           # [groupe, csp]
P_G_SACH_C=joint/joint.sum(0,keepdims=True)

# 4. Calage sur la Drees : âge moyen de première validation d'une année complète, génération 1976
#    (22,3 ans hommes, 23,0 ans femmes) -> 22,65 ; écart appliqué uniformément (hypothèse du dossier)
ENTREE_BRUTE=AGE_FIN+DELAI
DREES=22.65
DECALAGE=DREES-float(P_G@ENTREE_BRUTE)
ENTREE=ENTREE_BRUTE+DECALAGE

def tableau():
    pcd=p_csp_decile()
    pg=pcd@P_G_SACH_C.T          # [décile, groupe]
    return pcd,pg
if __name__=="__main__":
    print("dispersion log-normale (cadres, PI, employés, ouvriers):",np.round(SIG,3))
    print("vérif. déciles Insee (cible 0,1..0,9):",np.round([cdf(d,SIG) for d in DECILES],3))
    print("décalage de calage Drees : %+.2f an ; âges d'entrée par groupe :"%DECALAGE,np.round(ENTREE,2))
    pcd,pg=tableau()
    print("%-4s %s | %s | entrée moy."%("","  cad   PI  emp  ouv"," ≤16  17-19 20-21  ≥22"))
    for d in range(10):
        print("D%-3d %s | %s | %.1f"%(d+1," ".join("%4.0f"%(100*x) for x in pcd[d])," ".join("%5.0f"%(100*x) for x in pg[d]),pg[d]@ENTREE))

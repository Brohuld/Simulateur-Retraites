# Moteur carrière -> cotisations, pension, TRI (actualisation selon le salaire moyen : tout est exprimé en % de la RMPT de chaque année)
import math
from modele import NC, CA, interp
G=0.007
PASS_R=3864/3200      # plafond / RMPT (RMPT estimée 3 200 €)
SMIC_R=1772/3200
MICO_R=879/3200; SEUIL_R=1371/3200
R2025=1.4386/20.1877
def valeur_rel(y):   # valeur de service du point / RMPT, base 2025 = R2025 (prix rel 2025 = 1)
    v=R2025
    for t in range(2026,y+1):
        if t==2026: v*=1-0.018
        elif t<=2037: v*=1-0.0116
        else: v*=1-0.0086
    return v
def prix_rel(y):
    return 1.0 if y<=2037 else (1-0.0086)**(y-2037)
# Taux moyen de cotisation sur la carrière du non-cadre, par génération (COR RA 2026 fig. 3.1, lecture graphique),
# rapporté au taux légal 2026 sous le plafond (27,98 %) : sert à reproduire les taux plus faibles du passé.
TAU_COR={1960:25.0,1980:27.8,2000:28.0,2020:28.0}
TAU_F=1.0
def taux_cot(s, exo=False):
    """cotisations retraite totales (salarié+employeur) en part de RMPT, sur un salaire s (en RMPT)"""
    return TAU_F*_taux_cot_2026(s,exo)
def _taux_cot_2026(s, exo=False):
    t1=min(s,PASS_R); t2=max(0,min(s,8*PASS_R)-PASS_R)
    if exo:   # allègements : part employeur retraite supposée nulle au SMIC (hypothèse)
        return t1*(0.069+0.0315+0.0086)+s*0.004+t2*(0.0864+0.0108)
    c=t1*(0.1545+0.1002)+s*0.0251+t2*(0.2429)+(s*0.0035 if s>PASS_R else 0)
    return c
def carriere(profil, entree, gen, duree=43):
    ages=[entree+k for k in range(duree)]
    if profil=="SMIC": sal=[SMIC_R]*duree
    elif isinstance(profil,dict): sal=[interp(profil,a)/100 for a in ages]
    else: sal=profil(ages)
    annees=[int(gen+a) for a in ages]
    return ages,sal,annees
def pension_liq(sal,annees):
    n=len(sal); liq=annees[-1]+1
    vals=sorted([min(sal[i],PASS_R)*(1+G)**-(liq-annees[i]) for i in range(n-1)],reverse=True)[:25]
    base=0.5*sum(vals)/25
    pts=sum((min(x,PASS_R)*0.062+max(0,min(x,8*PASS_R)-PASS_R)*0.17)/prix_rel(y) for x,y in zip(sal,annees))
    aa=pts*valeur_rel(liq)
    if base<MICO_R and base+aa<SEUIL_R: base=min(MICO_R,max(base,SEUIL_R-aa))
    return base,aa,liq
def csg(mode):
    return {"plein":(0.091,0.01),"inter":(0.074,0.01),"reduit":(0.043,0.01),"brut":(0,0)}[mode]
def tri(profil,entree,gen,deces,mode_csg,exo=False,duree=43):
    global TAU_F
    TAU_F=min(1.0,TAU_COR.get(gen,28.0)/27.98)
    ages,sal,annees=carriere(profil,entree,gen,duree)
    base,aa,liq=pension_liq(sal,annees)
    t,mal=csg(mode_csg)
    flux=[-taux_cot(s,exo) for s in sal]
    age_liq=ages[-1]+1
    for k in range(int(round(deces-age_liq))):
        y=liq+k
        b=base*(1+G)**-k
        a=aa*valeur_rel(y)/valeur_rel(liq)
        flux.append(b*(1-t)+a*(1-t-mal))
    def npv(r): return sum(f/(1+r)**i for i,f in enumerate(flux))
    lo,hi=-0.1,0.1
    for _ in range(100):
        m=(lo+hi)/2
        if npv(m)>0: lo=m
        else: hi=m
    return 100*m, (base+aa)
if __name__=="__main__":
    for dec in (90,91,92):
        nc=tri(NC,22.5,2000,dec,"plein")[0]
        ca=tri(CA,22.75,2000,dec+2.5,"plein")[0]
        sm=tri("SMIC",22.5,2000,dec-2.8,"reduit")[0]
        smx=tri("SMIC",22.5,2000,dec-2.8,"reduit",exo=True)[0]
        print("décès nc %d : cadre %.2f (0,0) | non-cadre %.2f (0,8) | SMIC %.2f (0,3) | SMIC exo %.2f (2,9)"%(dec,ca,nc,sm,smx))

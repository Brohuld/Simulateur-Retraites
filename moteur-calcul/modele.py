# Taux de remplacement par décile — génération 1980 — profils de carrière du COR (Annexe 2026, fig. A2.4)
import math
G=0.007                      # croissance réelle des salaires (COR)
PASS=3864.0                  # plafond mensuel 2024
RMPT=3200.0                  # estimation (cf. note) — paramètre de sensibilité
R_LIQ=(1.4386/20.1877)*(1.006/1.025)*(1-0.0116)**11   # rendement Agirc-Arrco à la liquidation (2037+)
SMIC_B=1772.0                # SMIC brut mensuel moyen 2024
MICO=893.65*SMIC_B/1801.80; SEUIL=1394.86*SMIC_B/1801.80
NC={20:52,22:55,25:58,27:61,30:64,35:66,40:68,45:69,50:70,52:72,54:74,55:73,67:73}
CA={20:50,22:55,25:58,26:85,27:122,30:145,32:155,35:185,37:190,40:192,42:200,45:210,47:215,50:230,52:245,54:257,55:250,67:251}
def interp(d,a):
    ks=sorted(d)
    if a<=ks[0]: return d[ks[0]]
    for k0,k1 in zip(ks,ks[1:]):
        if a<=k1: return d[k0]+(d[k1]-d[k0])*(a-k0)/(k1-k0)
    return d[ks[-1]]
def net_of_brut(S):
    t1=min(S,PASS); t2=max(0,min(S,8*PASS)-PASS)
    cot=t1*(0.069+0.0315+0.0086)+S*0.004+t2*(0.0864+0.0108)+(S*0.0014 if S>PASS else 0)
    return S-cot-0.097*0.9825*S
def brut_of_net(n):
    lo,hi=n,2*n
    for _ in range(60):
        m=(lo+hi)/2
        if net_of_brut(m)>n: hi=m
        else: lo=m
    return m
def csg(pb,mode):
    if mode=="plein": return 0.091,0.01
    if mode=="inter": return 0.074,0.01
    if mode=="brut": return 0.0,0.0
    rfr=pb*12*0.9
    if rfr<13048: return 0.0,0.0
    if rfr<17057: return 0.043,0.01
    if rfr<26472: return 0.074,0.01
    return 0.091,0.01
def pension(path):
    """path = liste des salaires bruts mensuels (en euros de l'année de liquidation, rapportés à la RMPT de chaque année), du 1er au dernier"""
    n=len(path)
    # base : 25 meilleures années (hors dernière), plafonnées, revalorisées sur les prix
    vals=sorted([min(path[i],PASS)*(1+G)**-(n-1-i) for i in range(n-1)],reverse=True)[:25]
    base=0.5*sum(vals)/25
    aa=sum(min(x,PASS)*0.062+max(0,min(x,8*PASS)-PASS)*0.17 for x in path)*R_LIQ
    mico=False
    if base<MICO and base+aa<SEUIL:
        base=min(MICO,max(base,SEUIL-aa)); mico=True
    return base,aa,mico
def tr(path,mode="auto"):
    base,aa,m=pension(path); pb=base+aa
    t,mal=csg(pb,mode); pn=pb*(1-t)-aa*mal
    fin=path[-1]; fn=net_of_brut(fin)
    avg=sum(path)/len(path)
    return dict(base=base,aa=aa,pb=pb,pn=pn,fin=fin,avg=avg,trnn=pn/fn,trbn=pb/fn,trbb=pb/fin,trbavg=pb/avg,mico=m)
ENTREE=22.5; N=43
AGES=[ENTREE+k for k in range(N)]
def path_profile(prof,scale):  # prof en % RMPT ; scale = RMPT en euros
    return [interp(prof,a)/100*scale for a in AGES]
if __name__=="__main__":
    for R in (3000,3200,3400):
        RMPT=R
        s=tr([SMIC_B]*N,"brut"); nc=tr(path_profile(NC,R),"inter"); ca=tr(path_profile(CA,R),"plein")
        print("RMPT %d | SMIC brut/net %.1f (COR 87,5) | non-cadre net/net %.1f (COR 70) fin %d brut | cadre net/net %.1f (COR 48,5) fin %d brut"%(R,100*s['trbn'],100*nc['trnn'],nc['fin'],100*ca['trnn'],ca['fin']))

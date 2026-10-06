# Produit les paramètres du module « équité » du simulateur (v3) à partir du moteur.
import sys; sys.dont_write_bytecode=True
import tri as T, tri_deciles as D
from modele import brut_of_net
CSGR={"brut":0,"reduit":0.043,"inter":0.074,"plein":0.091}
def params(g):
    e=D.ENTREE[g]; eng={k:(r,m) for k,r,m,d in D.run(g)}
    TRN=[];TAU=[];ERO=[];ENG=[]
    for i,(k,n) in enumerate(D.MIDS):
        avgb=brut_of_net(n); prof=[avgb/3200*x for x in D.shape_for(k,avgb,e)]
        ages,sal,an=T.carriere(lambda a,p=prof:p,e,g)
        b,a,liq=T.pension_liq(sal,an)
        T.TAU_F=min(1,T.TAU_COR[g]/27.98)
        avg=sum(sal)/len(sal); tau=sum(T.taux_cot(s) for s in sal)/sum(sal)
        r,mode=eng[k]; c=CSGR[mode]
        TRN.append(round(100*((b+a)*(1-c)-a*(0.01 if c else 0))/avg,1))
        TAU.append(round(100*tau,2))
        ERO.append(round(100*(0.007*(b/(b+a))+0.0086*(a/(b+a))),3))
        ENG.append(round(r,2))
    return dict(entree=e,depart=e+43,TRN=TRN,TAU=TAU,ERO=ERO,ENG=ENG)
if __name__=="__main__":
    import json
    print(json.dumps({g:params(g) for g in (1960,1980,2000,2020)},indent=0))

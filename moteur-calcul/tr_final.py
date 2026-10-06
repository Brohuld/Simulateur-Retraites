import math
import tri as T
from tri_deciles import MIDS, shape_for, csg_auto, RMPT
from modele import brut_of_net, net_of_brut
def tr_decile(gen=1980,entree=22.5):
    rows=[]
    for k,n in MIDS:
        avgb=brut_of_net(n); prof=[avgb/RMPT*x for x in shape_for(k,avgb,entree)]
        ages,sal,an=T.carriere(lambda a,p=prof:p,entree,gen)
        b,a,liq=T.pension_liq(sal,an)
        pb=(b+a)*RMPT; mode=csg_auto(pb); t,mal=T.csg(mode)
        pn=(b+a)*(1-t)*RMPT-a*mal*RMPT
        fin=sal[-1]*RMPT; fn=net_of_brut(fin); avg=sum(sal)/len(sal)*RMPT
        rows.append((k,n,round(fin),round(pb),100*pn/fn,100*pb/avg))
    return rows
def ancres():
    from tri import NC,CA
    res={}
    for gen,e_nc,e_ca in ((1960,19.25,20),(1980,22.5,22.75),(2000,22.5,22.75)):
        def trnn(p,e,mode):
            ages,sal,an=T.carriere(p,e,gen); b,a,liq=T.pension_liq(sal,an); t,mal=T.csg(mode)
            pn=(b+a)*(1-t)-a*mal; fn=net_of_brut(sal[-1]*RMPT)/RMPT
            return 100*pn/fn,100*(b+a)/fn
        res[gen]=(trnn(NC,e_nc,"inter")[0],trnn(CA,e_ca,"plein")[0],trnn("SMIC",e_nc,"brut")[1])
    return res
if __name__=="__main__":
    for r in tr_decile(): print("%-4s net %5d fin brut %5d pension brute %5d  net/net %.1f  brut/moy %.1f"%r)
    for g,v in ancres().items(): print(g,"nc %.1f cadre %.1f SMIC %.1f"%v)

import math
import tri as T
from tri import *
from modele import brut_of_net, net_of_brut
RMPT=3200
MIDS=[("D1",1446),("D2",1580),("D3",1746),("D4",1908),("D5",2091),("D6",2316),("D7",2614),("D8",3045),("D9",3820),("D10",5593)]
EV_ECART=[-3.0,-2.2,-1.6,-1.1,-0.6,-0.2,0.3,0.8,1.6,2.5]
DECES_MOY={1960:86.2,1980:88.7,2000:90.8,2020:92.7}
def shape_for(k,avgb,entree):
    ages=[entree+i for i in range(43)]
    if k=="D1": return [1.0]*43
    nc=[interp(NC,a) for a in ages]; ca=[interp(CA,a) for a in ages]
    nc=[x/(sum(nc)/43) for x in nc]; ca=[x/(sum(ca)/43) for x in ca]
    lo=math.log(brut_of_net(1746)); hi=math.log(brut_of_net(5593))
    w=0.0 if k in("D2","D3") else min(1,(math.log(avgb)-lo)/(hi-lo))
    return [(1-w)*a+w*b for a,b in zip(nc,ca)]
def csg_auto(pb_eur):
    rfr=pb_eur*12*0.9
    if rfr<13048: return "brut"
    if rfr<17057: return "reduit"
    if rfr<26472: return "inter"
    return "plein"
ENTREE={1960:19.25,1980:22.5,2000:22.5,2020:22.5}
def run(gen=1980,entree=None,exo=False):
    entree=entree or ENTREE[gen]
    out=[]
    for i,(k,n) in enumerate(MIDS):
        avgb=brut_of_net(n)
        prof=[avgb/RMPT*x for x in shape_for(k,avgb,entree)]
        f=lambda ages,prof=prof: prof
        _,pb=T.tri(f,entree,gen,DECES_MOY[gen]+EV_ECART[i],"plein",exo)
        mode=csg_auto(pb*RMPT)
        r,_=T.tri(f,entree,gen,DECES_MOY[gen]+EV_ECART[i],mode,exo)
        out.append((k,r,mode,DECES_MOY[gen]+EV_ECART[i]))
    return out
if __name__=="__main__":
    old=[1.38,1.4,1.43,1.51,1.53,1.37,1.19,1.08,0.73,0.53]
    for (k,r,m,d),o in zip(run(),old):
        print("%-4s décès %.1f CSG %-6s TRI %.2f %%  (simulateur v2 : %.2f %%)"%(k,d,m,r,o))

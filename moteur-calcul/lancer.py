import sys; sys.dont_write_bytecode=True
# Lance tous les calculs de calculs-par-decile.md. Usage : python3 lancer.py
import tr_final, tri_deciles, tri
print("== Taux de remplacement par décile, génération 1980 ==")
for r in tr_final.tr_decile(): print("%-4s net %5d | dernier brut %5d | pension brute %5d | net/net %.1f %% | brut/moyenne carrière %.1f %%"%r)
print("== Profils COR (taux de remplacement) : non-cadre, cadre, SMIC ==")
for g,v in tr_final.ancres().items(): print(g,"%.1f / %.1f / %.1f"%v)
print("== Rendement des cotisations, profils COR, génération 2000 ==")
print("cadre %.2f | non-cadre %.2f | SMIC %.2f | SMIC avec allègements %.2f"%(tri.tri(tri.CA,22.75,2000,93.5,"plein")[0],tri.tri(tri.NC,22.5,2000,91,"plein")[0],tri.tri("SMIC",22.5,2000,89,"reduit")[0],tri.tri("SMIC",22.5,2000,89,"reduit",True)[0]))
for g in (1960,1980,2000,2020):
    print("== Rendement des cotisations par décile, génération %d =="%g)
    for k,r,m,d in tri_deciles.run(g): print("%-4s décès %.1f | CSG %-6s | TRI %.2f %%"%(k,d,m,r))

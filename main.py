import temps_status
import sim_humitat
import activ_riego

pluja=temps_status.pluja
print(pluja)

if pluja > 0 or sim_humitat.sim_humitat > 95:
    activ_riego.riego = False

else:
    activ_riego.riego = True


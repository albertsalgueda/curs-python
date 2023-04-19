from temps_status  import get_status
import sim_humitat
import activ_riego

try:
    poblacio, temp, humitat, presio, data, pluja, condicions = get_status("Pau")

except Exception as e:   
    print("Hi ha hagut un error", e)

print(poblacio)    

print(pluja)


if pluja > 0 or sim_humitat.sim_humitat > 95:
    activ_riego.riego = False

else:
    activ_riego.riego = True


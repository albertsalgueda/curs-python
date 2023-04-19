from temps_status  import get_status
#from temporitzador import temporitzador
from sim_humitat import sim_humitat
#from activ_riego import riego

poble_ripoll = "42.19706849706395,2.191078679466587"
poble_pau = "42.316218626549905, 3.116762888571179"
poble_pluja = "42,18"

poblacio, temp, humitat, presio, data, pluja, condicions = get_status(poble_pau)

try:

    if pluja > 0 or sim_humitat > 70:
        riego = False
        print("Desactivando riego....")
            
    else:
        riego = True
        print("Activando riego....")
        temp_reg = "True, 3600"
        temp_dia = "True, 86400"

except Exception as e:   
    print("Hi ha hagut un error >>>>>", e)
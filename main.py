import requests
import json

from temps_status import get_status
from temporitzador import temporitzador
from sim_humitat import sim_humitat
#from activ_riego import riego

poble_ripoll = "42.19706849706395,2.191078679466587"
poble_pau = "42.316218626549905, 3.116762888571179"
poble_pluja = "42,18"



def get_rain(data):
    try:
        humitat_ard = data["humitat"]
        fruit = data["fruit"]
        status = data["status"]
        ubi = data["ubi"]
    except: 
        return "bad request"
    
    #mirar poblacio

    poblacio, temp, humitat, presio, data, pluja, condicions = temporitzador(get_status, "ubi")
    #mirar api si plou

    if pluja > 0 or humitat_ard >80:
        status=0
        return {"status": status}
        
    else:
        status=1
        return{"status":status}
    
    fruit= data.get("fruit, none)")
    
   


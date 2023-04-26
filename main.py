from temps_status import get_status
from temporitzador import temporitzador
from fruit import fruit

poble_ripoll = "42.19706849706395,2.191078679466587"
poble_pau = "42.316218626549905, 3.116762888571179"
poble_pluja = "42,18"



def get_rain(data):
    try:
        humitat_ard = data["humitat"]
        fruits = data["fruit"]
        status = data["status"]
        ubi = data["ubi"]
        
    except: 
        return "bad request"
    
    #mirar poblacio

    poblacio, temp, humitat, presio, data_mesura, pluja, condicions = temporitzador(get_status, "ubi")
    #mirar api si plou
    
    if pluja > 0 or fruit <= humitat_ard:
        status=0
        return {"status": status}
      
    else:
        status=1
        return{"status":status}

    fruits[data].get("fruit, none)")




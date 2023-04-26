from temps_status import get_status


poble_ripoll = "42.19706849706395, 2.191078679466587"
poble_pau = "42.316218626549905, 3.116762888571179"
poble_pluja = "42,18"



def get_rain(data):
    try:
        temperatura = data["temperatura"]
        humitat = data["humitat"]
        fruit = data["fruit"]
        status = data["status"]
        ubi = data["ubi"]
    except: 
        return "bad request"
    
    #mirar poblacio

    pluja = int(get_status("ubi")) #mirar api si plou

    print(f"La pluja es {pluja}")

    if int(pluja) > 0 and float(humitat) >80:
        status=0
        return {"status": status}
        
    else:
        status=1
        return{"status":status}
    
    
    
   


# Permet escollir sobre quin dels cultius es volen mirar les condicions per encendre el reg i en retorna l'humitat òptima

data={"tomàquet":50,"esbarginia":55,"carbassó":75,"meló":65,"xindria":65,"olivera":65,"vinya":60}

def cultius():
    try:
        data_key_str = ', '.join(data.keys())
        while True:
            print(f"Cultius disponibles: {data_key_str}")
            cultiu= input("Quin cultiu hi ha? ")
            if cultiu in data:
                humitat_optima=data[cultiu] 
                return humitat_optima,cultiu
            else:
                print("No tenim dades d'aquest cultiu")
    except Exception as e:
        print(f"Hi ha hagut un error intentant seleccionar el cultiu >>>>> {e}")
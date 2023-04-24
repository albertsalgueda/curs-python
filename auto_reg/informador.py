# Informa de les condicions meteorològiques i de les necessitats d'humitat òptima del cultiu escollit

def informador(poblacio, pais, temp, humitat, presio, data, pluja, condicions,humitat_optima,cultiu):
    try:
        print(f"{poblacio} ({pais}) a data i hora {data}: \n Condicions ambientals: {condicions} \n Temperatura: {temp} ºC \n Humitat relativa: {humitat} % \n Pressió atmosfèrica: {presio} mbars \n Precipitació: {pluja} mm \n L'humitat òptima del {cultiu} és del {humitat_optima} %")
    except Exception as e:
        print(f"Hi ha hagut un error amb l'informador >>>>> {e}")

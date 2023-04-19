# Funció temporitzadora que faci un request de la funció en la que s'utilitzi amb el temps especificat en segons

from prova import temps_status

pluja = temps_status("Ripoll")

def temporitzador(funcio): # Primer argument nom de la funció i segon argument temps d'espera en segons
    import requests
    from time import sleep
    while True:
        funcio # És on llegirà la funció on es vol aplicar el temporitzador 
        sleep(2) # El temps de descans en segons
        return print(pluja)

temporitzador(temps_status("Ripoll"))
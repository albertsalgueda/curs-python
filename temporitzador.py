from time import sleep

# Funció temporitzadora que faci un request de la funció en la que s'utilitzi amb el temps especificat en segons.

def temporitzador(funcio,*args): # Per trucar la funció s'ha d'especificar el nom de la funció i l'arguments o arguments que necessita separat per coma
    while True:
        try:
            funcio(*args)
            sleep(2)
        except Exception as e:
            print(f"Hi ha hagut un error >>>>> {e}")

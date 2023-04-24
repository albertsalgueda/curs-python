# En funció de la pluja i de les condicions d'humitat comparades amb l'humitat òptima del cultiu seleccionat encèn o apaga el reg
# En funció de si el reg s'encèn o no defineix el temps d'espera per la següent consulta sobre condicions meteorològiques

from time import sleep

def reg(pluja,humitat,humitat_optima):
    try:
        if pluja > 0 or humitat > humitat_optima:
            estat_reg = False
            temps = 2
            print("Desactivant reg...")
            return estat_reg, temps
                
        elif pluja == 0 and humitat < humitat_optima:
            estat_reg = True
            temps = 3600*24
            print("Activant reg...")
            return estat_reg, temps
        sleep(2)

    except Exception as e:   
        print(f"Hi ha hagut un error amb l'activador de reg >>>>> {e}")
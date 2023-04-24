# 

from time import sleep

def temporitzador(estat_reg, temps):
    try:
        if estat_reg == True:
            sleep(temps)
        elif estat_reg == False:
            sleep(temps)
    except Exception as e:
        print(f"Hi ha hagut un error amb el temporitzador >>>>> {e}") 

def fruit():

    data={"tomaquet":50,"esbarginia":55, "carbasso":75,"melo":65,"xindria":65,"olivera":65,"vinya":60}

    while True:
        cultius=data.keys()
        #print(f"Cultius disponibles:{cultius}")
        cultiu= input ("Quin cultiu hi ha?")
        if cultiu in cultius:
            humitat_optima=data[cultiu] 
            #print (f"la humitat optima en % es: {humitat_optima}")
        break
    else:
        print ("Aquests cultiu ho hi es")

    return humitat_optima


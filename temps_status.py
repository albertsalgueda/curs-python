import requests
import json

def get_status(poble):
    response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8e3a9372e503477ca0f210354231404&q={poble}&days=1&aqi=no&alerts=no")


    poblacio = response.json()["location"]["name"]
    pais = response.json()["location"]["country"]
    temp = response.json()["current"]["temp_c"]
    humitat = response.json()["current"]["humidity"]
    presio = response.json()["current"]["pressure_mb"]
    data= response.json()["current"]["last_updated"]
    pluja = response.json()["current"]["precip_mm"]
    condicions = response.json()["current"]["condition"]["text"]

    if pluja == 0:
        print(f"No plou a {poblacio}")
    else:
        print(f"Hi ha una precipitació de: {pluja} (mm/h) en la poblaciò de:  · {poblacio} · ({pais})")
       
        #print(f"Està a: {temp} graus centigrads")
        #print(f"i té una humitat del: {humitat} %")
        #print(f"i hi ha una presiò atmosfèrica de: {presio} mbars")
        #print(f"Mesura: {data}")
        #print(f"Hi ha una precipitació de: {pluja}")
        #print(f"Condicions Ambientals: {condicions}")
    return poblacio, temp, humitat, presio, data, pluja, condicions





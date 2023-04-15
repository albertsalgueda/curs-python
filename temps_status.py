import requests
import json

poble = input("Entra població (castellà) o entra lon i lat:")
#if poble == "ripoll":
#    poble = "42.19706849706395,2.191078679466587"
    

response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8e3a9372e503477ca0f210354231404&q={poble}&days=1&aqi=no&alerts=no")


poblacio = response.json()["location"]["name"]
temp = response.json()["current"]["temp_c"]
humitat = response.json()["current"]["humidity"]
presio = response.json()["current"]["pressure_mb"]
data= response.json()["current"]["last_updated"]
pluja = response.json()["current"]["precip_mm"]
condicions = response.json()["current"]["condition"]["text"]

print(f"Estàs consultant en aquesta població:\n_____{poblacio}_____")
print(f"Està a: {temp} graus centigrads")
print(f"i té una humitat del: {humitat} %")
print(f"i hi ha una presiò atmosfèrica de: {presio} mbars")
print(f"Mesura: {data}")
print(f"Hi ha una precipitació de: {pluja}")
print(f"Condicions Ambientals: {condicions}")


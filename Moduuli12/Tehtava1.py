import json
import requests

pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vitsi = requests.get(pyynto)
    if vitsi.status_code==200:
        json_vitsi = vitsi.json()
        print("Tässä on Chuck Norris vitsisi: ")
        print(json_vitsi["value"])

except requests.exceptions.RequestException as e:
    print("Chuck ei ole vitsituulella")
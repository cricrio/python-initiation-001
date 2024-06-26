## Install requests in venv with this command 'python -m pip install requests'
import requests

r = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
)


data = r.json()

latitude = data.get("latitude")
longitude = data.get("longitude")

print(data)

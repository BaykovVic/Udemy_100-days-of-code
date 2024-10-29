import requests


API_KEY = "<YOUR API KEY>"
LOCATION = "MOSCOW,RU"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "appid": API_KEY,
    "q": LOCATION,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "appid": API_KEY,
    "lat": 55.7522,
    "lon": 37.6156,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
weather_data = response.json()


# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
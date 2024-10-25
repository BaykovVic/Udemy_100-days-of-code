import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
if response.status_code == 404:
    raise Exception("That resources does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to acceed to this resource.")

data = response.json()
longitude = data["iss_position"]["longitude"]

latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 55.755825
MY_LONG = 37.617298
MY_EMAIL = '<EMAIL>'
MY_PASSWORD = '<PASSWORD>'

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])
    print(iss_lat, iss_lon)

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lon <= MY_LONG + 5:
        return True
    return False


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_hour = sunrise.split("T")[1].split(":")[0]
    sunset_hour = sunset.split("T")[1].split(":")[0]
    time_now_hour = datetime.now().hour
    print(time_now_hour, sunset_hour)
    if time_now_hour <= sunrise_hour and time_now_hour >= sunset_hour:
        return True
    return False

while True:
    time.sleep(6)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="The ISS is above you in the sky")


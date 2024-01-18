import requests
from datetime import datetime
import smtplib

email_add = "xxxxxxxxxxxxxxxx@gmail.com"
to_add = "xxxxxxxxxxxxxxx@gmail.com"
email_pw = "xxxxxxxxxxxxxxxxx"
SUBJECT = "LOOK UP"
# MESSAGE = "ISS is currently going over your position step out and look up to see the magnificant human creation"
MESSAGE = "Hey there stargazer!\n\nGuess what? The International Space Station (ISS) is currently passing right over your location!\n\nGrab a comfy chair, step outside, and look up at the night sky. You're about to witness a magnificent human creation, the ISS, cruising through space.\n\nFeel the awe as this high-flying spaceship orbits above you. It's like a shooting star, but much cooler because it's a space station"

MY_LAT = "000000"
MY_LNG = "00000000"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_position_close_to_iss(iss_lat, iss_lon, my_lat, my_lon, margin=15):
    lat_diff = abs(float(my_lat) - iss_lat)
    lon_diff = abs(float(my_lon) - iss_lon)

    return lat_diff <= margin and lon_diff <= margin


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "Asia/Jayapura"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


if is_position_close_to_iss(iss_latitude, iss_longitude, MY_LAT, MY_LNG):
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user=email_add, password=email_pw)
            connections.sendmail(from_addr=email_add, to_addrs=to_add, msg=f"Subject:{SUBJECT}\n\n {MESSAGE}")
        print("mail sent")


print(f"Iss Latitude : {iss_latitude} \n")
print(f"Iss Longitude : {iss_longitude} \n")

print(f"My Latitude : {MY_LAT} \n")
print(f"My Longitude : {MY_LNG} \n")

print(f"Time now Hour: {time_now.hour}")
print(f"Time now : {time_now}")

print(f"sunset : {sunset}")
print(f"sunrise : {sunrise}")
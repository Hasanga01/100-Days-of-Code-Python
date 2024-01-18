import requests
import datetime as dt

URL = "https://api.sunrise-sunset.org/json"
MY_LAT = "0000000"
MY_LNG = "00000000"

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "Asia/Dili"
}
response = requests.get(url=URL, params=params)
res = response.json()
sunrise = res["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = res["results"]["sunset"].split("T")[1].split(":")[0]

now = dt.datetime.now()
print(f"noW_TIME : {now.time().hour}")

print(sunrise)
print(sunset)

import requests
import smtplib
import datetime as dt

app_password = "xxxxxxxxxxxx"
email_me = "xxxxxxxxxxxx@gmail.com"
email_to = "xxxxxxxxxxxx@gmail.com"
SUBJECT = "Rain Alert"
MESSAGE = "Bring your umbrella it will rain today"

latitude = "xxxxx"
longitude = "xxxxx"

api_key = "xxxxxxxxxxxxxxxxxxxxxxxx"

url_6 = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}"

response = requests.get(url_6)
WILL_RAIN = False

if response.status_code == 200:
    res = response.json()
    print(response.status_code)

    target_date = dt.datetime.now().date()

    # Iterate through each forecast entry
    for entry in res["list"]:
        # Extract the date from the forecast entry
        entry_date = entry["dt_txt"].split()[0]
        entry_time = entry["dt_txt"].split()[1]

        weather = entry["weather"]
        weather_id = weather[0]["id"]

        print(f"Date: {entry_date}")
        print(f"Weather ID: {weather_id}")

        if weather_id < 700:
            # print(f"Rainy in {entry_time}\n")
            WILL_RAIN = True

        else:
            print(weather[0]["main"])

else:
    print(f"Error: {response.status_code}")

if WILL_RAIN:
    print("bring your umbrella")
    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=email_me, password=app_password)
        connections.sendmail(from_addr=email_me, to_addrs=email_to, msg=f"Subject: {SUBJECT}\n\n {MESSAGE}")

print(dt.datetime.now().date())

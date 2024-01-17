##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import random
import smtplib

app_password = "... ... ... ..."
email_name = "xxxxxxxxx@gmail.com"
email_to_send = "xxxxxxxxxxxx@gmail.com"

now = dt.datetime.now()

day = now.day
month = now.month

print(day)
print(month)

data = pd.read_csv("birthdays.csv")
print(data)

file_names = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for index, row in data.iterrows():
    if row.month == month and row.day == day:
        name = row["name"]
        email = row.email

        random_file = random.choice(file_names)

        with open(f"letter_templates/{random_file}", mode='r') as mail_file:
            print("file opened")
            mail_template = mail_file.read()

        final_mail = mail_template.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user=email_name, password=app_password)
            connections.sendmail(from_addr=email_name,
                                 to_addrs=email_to_send,
                                 msg=f"Subject:Happy Birthday\n\n {final_mail}")

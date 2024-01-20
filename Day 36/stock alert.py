import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

app_password = "xxxxxxxxxxxxxxxxx"
email_me = "xxxxxxxxxxxxx@gmail.com"
email_to = "xxxxxxxxxxxxx@gmail.com"
SUBJECT = "Lucky Boy"
MESSAGE = "your stocks have gone up more than 5%"

news_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
news_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&q=tesla&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey=xxxxxxxxxxxxxxxx'
r = requests.get(url)
data = r.json()

print(data)

print("\n")

new2 = requests.get(news_url)
k = new2.json()



last_stock_18 = data["Time Series (60min)"]["2024-01-18 19:00:00"]["4. close"]

last_stock_17 = data["Time Series (60min)"]["2024-01-17 19:00:00"]["4. close"]

print(f"17 :{last_stock_17}")
print(f"17 :{last_stock_18}")

print(type(last_stock_17))
print(type(last_stock_18))

stock_deviation = round(float(float(last_stock_18) - float(last_stock_17)) / float(last_stock_17) * 100)
print(stock_deviation)


def stock_status():
    if stock_deviation > 0:
        print(f"{STOCK}: 🔺{abs(stock_deviation)}%")
    elif stock_deviation < 0:
        print(f"{STOCK}: 🔻{abs(stock_deviation)}%")
    else:
        pass


def send_mail():
    with smtplib.SMTP("smtp.google.com") as connections:
        connections.starttls()
        connections.login(user=email_me, password=app_password)
        connections.sendmail(from_addr=email_me, to_addrs=email_to,
                             msg=f"Subject : {SUBJECT}\n\n{MESSAGE}\n {get_news()}")


def get_news():
    for article in k["articles"]:
        title = article["title"]
        description = article["description"]

        stock_status()
        print(
            f"HeadLine: {title}\n"
            f"Brief: {description}\n")


if stock_deviation > 0 and stock_deviation >= 5:
    send_mail()

send_mail()
get_news()


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

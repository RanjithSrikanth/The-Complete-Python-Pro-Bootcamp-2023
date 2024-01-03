from twilio.rest import Client
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "VV44IY2DLQQN0XVR"
NEWS_API_KEY = "2c827bc6109e40dd850e3c32e0f58b9e"
account_sid = "ACcb6d810a204002f2ac0d033e07a684f2"
auth_token = "dd233d277b432303489b5102e988ebd4"


stock_api_parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_api_parameters)
response_d = response.json()["Time Series (Daily)"]
# print(response.json())
# data = response_d["Time Series (Daily)"]["2023-03-24"]["4. close"]
# print(response_d)
list = [v for (k, v) in response_d.items()]
# print(list)
yesterday_v = list[0]["4. close"]
day_before_yesterday_v = list[1]["4. close"]
# print(yesterday_v, day_before_yesterday_v)
# print(int(day_before_yesterday_v) - int(yesterday_v))
diffrence  = (float(yesterday_v) - float(day_before_yesterday_v))
print(diffrence)

diffrence_p = round((diffrence / float(yesterday_v)) * 100)
print(diffrence_p)
updown = None
if diffrence > 0:
    updown = "🔺"
else:
    updown = "🔻"
n_parameter = {
    "apiKey" : NEWS_API_KEY,
    "q" : COMPANY_NAME,
}
if abs(diffrence_p) > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=n_parameter)
    article = news_response.json()["articles"]
    three_articles = article[:3]
    # print(three_articles)
    fmessage = [f"{STOCK} : {updown}{diffrence_p}%\nHeadline : {article['title']}. \nBrief : {article['description']}." for article in three_articles]
    client = Client(account_sid, auth_token)
    for i in fmessage:
        message = client.messages \
            .create(
            body = i,
            from_='+14753488807',
            to='+919585148852'
        )



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


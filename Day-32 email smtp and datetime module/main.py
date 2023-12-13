import datetime as dt
import smtplib
import pandas
import random

my_mail = "kingking6566gg@gmail.com"
password = "iglteqeyhcjkukzj"

now = dt.datetime.now()
today = (now.month, now.day)
print(today)
data = pandas.read_csv("birthday.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
if today in birthdays_dict:
    bday_person = birthdays_dict[today]
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filepath) as letter:
        data = letter.read()
        content = data.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=bday_person["email"],
                            msg=f"Subject:Happy Birthday !!!\n\n{content}")




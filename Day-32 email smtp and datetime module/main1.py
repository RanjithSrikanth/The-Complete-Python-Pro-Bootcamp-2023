# import smtplib
#
#
# my_mail = "kingking6566gg@gmail.com"
# password = "iglteqeyhcjkukzj"
# # connection = smtplib.SMTP("smtp.gmail.com", 587)
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_mail, password=password)
#     connection.sendmail(
#         from_addr=my_mail, to_addrs="ranjiranji28@yahoo.com", msg="Subject:Hello\n\nThis is the body of the email")
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(month)
# day_of_week = now.weekday()
# print(day_of_week)
#
# dob = dt.datetime(year=2003, month=9, day=28)
# print(dob)



#
# import datetime as dt
# import random
# import smtplib
#
# my_mail = "kingking6566gg@gmail.com"
# password = "iglteqeyhcjkukzj"
#
# now = dt.datetime.now()
# day = now.weekday()
# # print(day)
# if day == 0:
#     with open("quotes.txt", mode="r") as file:
#         data = file.readlines()
#         random_q = random.choice(data)
#     connection = smtplib.SMTP("smtp.gmail.com", 587)
#     connection.starttls()
#     connection.login(user=my_mail, password=password)
#     connection.sendmail(from_addr=my_mail, to_addrs="ranjiranji28@yahoo.com",
#                         msg=f"Subject:Monday Motivation\n\n{random_q}")
#     connection.close()

import requests
from datetime import datetime
import smtplib
import time

my_mail = "kingking6566gg@gmail.com"
password = "iglteqeyhcjkukzj"

MY_LAT = 20.593683
MY_LONG = 78.962883


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if iss_latitude >= MY_LAT + 5 or iss_latitude <= MY_LAT - 5:
        if iss_longitude >= MY_LONG + 5 or iss_longitude <= MY_LONG - 5:
            return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise, sunset)
    time_now = datetime.now()
    hour = time_now.hour
    # print(hour)

    if hour >= sunset and hour <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=my_mail,
                                msg=f"Subject:Alert!!!\n\nThe space station on above your head in the sky!!!")


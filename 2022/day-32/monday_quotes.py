import random
import smtplib
import datetime as dt

MY_EMAIL = "emmanuels0n.gr@gmail.com"
PASSWORD = "DioBrando69-"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:

    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"subject:Monday Motivation\n\n{quote}")

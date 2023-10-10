# import smtplib
#
# my_email = "emmanuels0n.gr@gmail.com"
# password = "DioBrando69-"
#
# # connection = smtplib.SMTP("smtp.gmail.com")  # Is different for every email provider
# with smtplib.SMTP("smtp.gmail.com") as connection:  # To avoid the need of close the connection
#     connection.starttls()   # Transport Layer Security, secures the connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="emmanuels0n.gr@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")
#
# # connection.close()

import datetime as dt

now = dt.datetime.now()  # Inside the date time module dt, there is the .datetime class, and a method called .now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=1995, month=9, day=15, hour=4)


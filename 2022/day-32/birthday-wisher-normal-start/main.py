##################### Normal Starting Project ######################

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "emmanuels0n.gr@gmail.com"
PASSWORD = "DioBrando69-"

today = datetime.now()
print(today)
today_tuple = (today.month, today.day)
print(today_tuple)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
if today_tuple in birthdays_dict:
    print("it_is")
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!!\n\n{contents}")






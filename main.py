import random
import smtplib
import datetime
import pandas
# 1. Update the birthdays.csv with your friends & family's details.
today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day):data_row for (index,data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        replaced = contents.replace("[NAME]", birthday_person["name"])
    my_email = "vache.nft@gmail.com"
    password = "rtymlvegtiexliie"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="grigoryanvache10.01@yahoo.com",
                            msg=f"Subject:Birthday wish\n\n{replaced}")



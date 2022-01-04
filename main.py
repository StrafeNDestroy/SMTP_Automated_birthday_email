from datetime import datetime
import pandas
import random
import smtplib
# Email Login Credentials
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# Creation of dictionary with key (month,day) and value = data in row
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# check if tuple key is in birhtday dictonary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
# Creation of file path based on random index
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
# Sending of Letter and altered contents
# smtp email address smtp.gmail.com
    with smtplib.SMTP("YOUR SENDING SMTP EMAIL ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        print("Email Sent")

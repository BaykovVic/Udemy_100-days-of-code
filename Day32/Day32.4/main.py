from datetime import datetime
import pandas as pd
import random
import smtplib

##################### Extra Hard Starting Project ######################
today = datetime.now()
today_tuple =  (today.month, today.day)

my_email = "<YOUR SENDER EMAIL HERE>"
my_password = "<YOUR PASSWORD HERE>"
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, "r") as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=content)




import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()

my_email = "<YOUR SENDER EMAIL HERE>"
my_password = "<YOUR PASSWORD>"

to_email = "<YOUR DESTINATION EMAIL HERE>"
if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=quote)
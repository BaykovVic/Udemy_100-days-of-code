import smtplib

my_email = "<YOUR SENDER EMAIL HERE>"

# You can generate app password using your email provider
my_password = "<YOUR PASSWORD HERE>"

to_email = "<YOUR DESTINATION EMAIL HERE>"
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Hello")
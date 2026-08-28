# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os



gmail_username = os.environ.get("GMAIL_USERNAME")
gmail_password = os.environ.get("GMAIL_PASSWORD")
google_app_password = os.environ.get("GOOGLE_APP_PASSWORD")
yahoo_username = os.environ.get("YAHOO_USERNAME")
yahoo_password_for_sending_email = os.environ.get("YAHOO_PASSWORD_FOR_SENDING_EMAIL")
yahoo_password = os.environ.get("YAHOO_PASSWORD")
gmail_smtp_address = "smtp.gmail.com"
yahoo_smtp_address = "smtp.mail.yahoo.com"
letters = len(os.listdir("letter_templates"))

with open("birthdays.csv") as bdays:
    birthdays = pandas.read_csv(bdays)
    birthdays_dict = birthdays.to_dict(orient="records")

today = dt.datetime.now()
choice = random.randint(1, letters)
letter_chosen = f"letter_templates/letter_{choice}.txt"

for record in birthdays_dict:
    if record["day"] == today.day and record["month"] == today.month:
        with open(letter_chosen, "r") as text:
            letter = text.read()
            letter_to_send = letter.replace("[NAME]", record["name"])
            email = record["email"]

        with smtplib.SMTP(yahoo_smtp_address) as connection:
            connection.starttls()  # makes the connection secure. In case the email gets intercepted no one can read it.
            connection.login(user=yahoo_username, password=yahoo_password_for_sending_email)
            connection.sendmail(
                from_addr=yahoo_username,
                to_addrs=email,
                msg=f"Subject:Happy Birthday! \n\n{letter_to_send}")

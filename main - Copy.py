my_email="" # your email address
my_password = "" #your password
my_client = "" # client email to send to
app_password = "" # eamil password

##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
# 1. Update the birthdays.csv
birthday_csv = "D:/Python/100 days Python Challenge/Intermediate/day 32/Birthday wisher/birthdays.csv"
letter_address = "D:/Python/100 days Python Challenge/Intermediate/day 32/Birthday wisher/letter_templates/letter_1.txt"
birthday_file= pd.read_csv(birthday_csv)
print(birthday_file.day)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today =now.day
if today ==birthday_file.day[0]:
    print("Today is the birthday") 
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(letter_address, "r") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", "Ben")
# 4. Send the letter generated in step 3 to that person's email address.
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs=my_client, msg=f"Subject: Happy Birthday\n\n {letter}")





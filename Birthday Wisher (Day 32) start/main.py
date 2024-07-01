# import smtplib

# my_email="gmpatel404@gmail.com"
# password="yemf cavz kchr kufw"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="bilalfaizan58@gmail.com",msg="Subject:Hello\n\nThis is the body of email")
#     connection.close()


# import datetime as dt

# now=dt.datetime.now()
# year=now.year
# month=now.month
# day=now.day
# day_of_week=now.weekday()
# print(day_of_week)

# date_of_birth=dt.datetime(year=2024,month=1,day=17)
# print(date_of_birth)








# Automated quotes sender project👇
# import datetime as dt
# import random
# import smtplib

# MY_EMAIL="gmpatel404@gmail.com"
# MY_PASSWORD="yemf cavz kchr kufw"

# now=dt.datetime.now()
# weekday=now.weekday()
# if weekday==6:
#     with open("quotes.txt") as quotes_file:
#         all_quotes=quotes_file.readlines()
#         quote=random.choice(all_quotes)
#         print(quote)
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(MY_EMAIL,MY_PASSWORD)
#             connection.sendmail(from_addr=MY_EMAIL,to_addrs="bilalfaizan58@gmail.com",msg=f"Subject:Monday Motivation\n\n{quote}")



# Automated birthday wisher project👇
from datetime import datetime
import random
import pandas
import smtplib

MY_EMAIL="gmpatel404@gmail.com"
MY_PASSWORD="yemf cavz kchr kufw"

today=datetime.now()
today_tuple=(today.month,today.day)
data=pandas.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
  birthday_person=birthdays_dict[today_tuple]
  file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
  with open(file_path) as letter_file:
    contents=letter_file.read()
    contents=contents.replace("[NAME]",birthday_person["name"])

  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=birthday_person["email"],
      msg=f"Subject:Happy birthday!\n\n{contents}")


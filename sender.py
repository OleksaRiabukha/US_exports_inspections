#!/home/wheatman/PycharmProjects/New_life/venv/bin/python3.8
import yagmail
import schedule
import time
from output import generate_output
import os.path
from datetime import datetime
import requests

grains_type = ["WHEAT", "CORN", "SOYBEANS"]

# set the receiver, subject and files for email
receiver = ""
subject = "US weekly exports inspections"
file = ["Wheat.xlsx", "Corn.xlsx", "Soybeans.xlsx"]

# set time after which script will be rescheduled for Tuesday
upper_time = datetime.strptime("15:20", "%H:%M").time()


# run whole script if there were updates on the website, it sends all to email
# Otherwise, it waits and reschedules script for Tuesday
def send_files_and_text(target_mail, title, attachment):
    print("we are here")
    if updates_checker():
        print("generate output")
        body = generate_output(grains_type)
        yag = yagmail.SMTP(user="", password="")
        yag.send(
                to=target_mail,
                subject=title,
                contents=body,
                attachments=attachment
            )
        print("sent")
        remove_files()
        scheduler()
        print("scheduled")
    elif upper_time < datetime.now().time():
        print("Scheduling for Tue")
        schedule.every().tuesday.at("15:00").do(send_files_and_text, receiver, subject, file)
        while True:
            schedule.run_pending()
            print("waiting for update")
            time.sleep(1)
    else:
        time.sleep(20)
        print("sleeping 20")
        send_files_and_text(receiver, subject, file)


# removes files
def remove_files():
    print('deleting')
    os.remove('./CY2021.csv')
    os.remove('./CY2020.csv')
    os.remove('./CY2019.csv')
    os.remove('./Wheat.xlsx')
    os.remove('./Corn.xlsx')
    os.remove('./Soybeans.xlsx')


# schedules script for 16:00 London time
def scheduler():
    print("Rescheduling for Monday")
    schedule.every().monday.at("15:00").do(send_files_and_text, receiver, subject, file)
    while True:
        schedule.run_pending()
        print("sleeping in while loop of func")
        time.sleep(1)


# checks if files were updated
def updates_checker():
        url = "https://fgisonline.ams.usda.gov/ExportGrainReport/CY2021.csv"
        r = requests.head(url, verify=False)
        r2 = r.headers['Last-Modified']
        date_of_update = datetime.strptime(r2[5:-4], '%d %b %Y %H:%M:%S').date()
        today = datetime.today().date()
        # if you need to test output, change date to the last updated on the website in last_up varibale and
        # put it instead of today variable in if statement do the same in data.py sheet
        # last_up = datetime.strptime("2021-01-11", "%Y-%m-%d").date()
        if today == date_of_update:
            return True
        else:
            return False


# calls function to run all the script
send_files_and_text(receiver, subject, file)


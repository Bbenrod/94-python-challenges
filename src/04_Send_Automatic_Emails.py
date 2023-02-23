import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

# Send Automatic Emails using Python


def automatic_email():
    EMAIL_SO = os.environ.get("EMAIL")
    PASSWORD_SO = os.environ.get("EMAIL_PASSWORD")

    user = input("TYPE YOUR USER:\t").upper()
    email = input("TYPE YOU MAIL:\t")
    message = (
        f"Subject: Sending emails using Python.\nHELLO {user}, THIS MAIL WAS SEND USING PYTHON.")

    # Set connection
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # Activate encriptation
    connection.starttls()
    # Sing in
    connection.login(user=EMAIL_SO, password=PASSWORD_SO)
    # Send mail
    connection.sendmail(from_addr=EMAIL_SO, to_addrs=email, msg=message)
    # Close connection
    connection.quit()

    print("EMAIL SENT!")


if __name__ == "__main__":
    automatic_email()

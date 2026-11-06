from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
load_dotenv(override=True)


class Messenger:
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
    EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

    def send_email(cls, subject, text_body, html_body):
        msg = EmailMessage()
        msg["From"] = cls.EMAIL_ADDRESS
        msg["To"] = cls.EMAIL_ADDRESS
        msg["Subject"] = subject
        msg.set_content(text_body)
        msg.add_alternative(html_body, subtype="html")

        with smtplib.SMTP(cls.EMAIL_SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(cls.EMAIL_ADDRESS, cls.EMAIL_APP_PASSWORD)
            server.send_message(msg)

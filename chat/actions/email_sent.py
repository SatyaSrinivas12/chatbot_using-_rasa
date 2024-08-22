import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_via_gmail(recipient_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWD')

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")



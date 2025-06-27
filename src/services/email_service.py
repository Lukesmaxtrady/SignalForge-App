import smtplib
from email.mime.text import MIMEText

def send_email(recipient: str, subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "noreply@signalforge.app"
    msg['To'] = recipient
    with smtplib.SMTP('smtp.yourprovider.com') as server:
        server.login('your_username', 'your_password')
        server.send_message(msg)

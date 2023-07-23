import smtplib, ssl
from password import password


def send_email(user_email, message):
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        # server.connect("smtp.gmail.com", port)
        server.login("ticket.updater.noreply@gmail.com", password)
        server.sendmail("ticket.updater.noreply@gmail.com", user_email, message)

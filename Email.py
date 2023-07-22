import smtplib, ssl


def send_email(user_email, message):
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("", port, context=context) as server:
        server.login("02diggiethebiggy@gmail.com", "animenorrisnuts")
        server.sendmail("02diggiethebiggy@gmail.com", user_email, message)

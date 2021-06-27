import smtplib, ssl, os

EMAIL = os.getenv('EMAIL')

port = 465
smtp_server = "smtp.seznam.cz"
password = "endysoft123"
sender_email = "notification.test@seznam.cz"


def send_email(subject: str, body: str):
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.seznam.cz", port, context=context) as server:
        server.login(sender_email, password)
        text = "Subject: " + subject
        text += "\n\n"
        text += body
        server.sendmail(sender_email, EMAIL , text)

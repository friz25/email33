import smtplib
import os
from email.mime.text import MIMEText


def send_email():
    sender = "frizmob@gmail.com"
    password = "friz48625"
    To = "alisa.shelepa@gmail.com"

    # password = os.getenv('EMAIL_PASSWORD')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # text = """
    # <!doctype html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport"
    #           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    #     <meta http-equiv="X-UA-Compatible" content="ie=edge">
    #     <title>Document</title>
    # </head>
    # <body>
    #     <h1 style="color: green">Привет!!!</h1>
    #     <span><u>Как у вас дела??</u></span>
    # </body>
    # </html>
    # """

    try:
        with open("email_template.html") as file:
            template = file.read()

    except IOError:
        return "the template file doesn't found!"

    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = To
        msg["Subject"] = "Алиске от ВИТИ"
        server.sendmail(sender, To, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\n[-] Check yout login or password correctness!"


def main():
    print(send_email())


if __name__ == '__main__':
    main()

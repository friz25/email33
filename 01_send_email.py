import smtplib
import os
from email.mime.text import MIMEText

def send_email(message):
    sender = "frizmob@gmail.com"
    password = "friz48625"
    # password = os.getenv('EMAIL_PASSWORD')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Смотри что чудит Анжелка с бухгалтерии!"
        server.sendmail(sender, sender, msg.as_string())
        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\n[-] Check yout login or password correctness!"



def main():
    message = input("Введите сообщение: ")
    print(send_email(message=message))

if __name__ == '__main__':
    main()
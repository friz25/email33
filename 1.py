import smtplib
import os

def send_email(message):
    sender = "frizmob@gmail.com"
    password = "friz48625"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)

        return "message was sent successfully"
    except Exception as _ex:
        return f"{_ex}\nCheck login or password correctness!"



def main():
    message = input("Введите сообщение: ")
    print(send_email(message=message))

if __name__ == '__main__':
    main()
import smtplib
import os
import mimetypes
import time

from pyfiglet import Figlet #красивый вывод заголовка в терминале
from tqdm import tqdm #прогресс бар при обработке файлов
from email import encoders
from email.mime.text import MIMEText  # позволяет на русском письмо отправить
from email.mime.multipart import MIMEMultipart  # позволяет файлы прикрепить к письму
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase


def send_email(text=None, template=None):
    sender = "frizmob@gmail.com"
    password = "friz48625"
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
        with open(template) as file:
            template = file.read()

    except IOError:
        # return "the template file doesn't found!"
        template = None

    try:
        server.login(sender, password)
        # msg = MIMEText(template, "html")
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = sender
        msg["Subject"] = "Алиске от ВИТИ"

        if text:
            msg.attach(MIMEText(text))
        if template:
            msg.attach(MIMEText(template, "html"))

        print("Collecting...")
        for file in tqdm(os.listdir("attachments")):
            time.sleep(0.4)
            filename = os.path.basename(file)
            ftype, encoding = mimetypes.guess_type(file)  # определим тип файла
            file_type, subtype = ftype.split("/")  # application pdf

            if file_type == "text":
                with open(f"attachments/{file}", encoding='UTF-8') as f:
                    file = MIMEText(f.read())
            elif file_type == "image":
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEImage(f.read(), subtype)
            elif file_type == "audio":
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEAudio(f.read(), subtype)
            elif file_type == "application":
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEApplication(f.read(), subtype)
            else:
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEBase(f.read(), subtype)
                    file.set_payload(f.read())
                    encoders.encode_base64(file)

            # with open(f"attachments/{file}", "rb") as f:
            #     file = MIMEBase(f.read(), subtype)
            #     file.set_payload(f.read())
            #     encoders.encode_base64(file)

            file.add_header('content-disposition', 'attachment', filename=filename)
            msg.attach(file)
        print("Sending...")
        server.sendmail(sender, sender, msg.as_string())
        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\n[-] Check yout login or password correctness!"


def main():
    font_text = Figlet(font="slant")
    print(font_text.renderText("SEND EMAIL"))
    text = input("Type your text or press enter: ")
    template = input("Type template name or press enter: ")
    print(send_email(text=text, template=template))


if __name__ == '__main__':
    main()

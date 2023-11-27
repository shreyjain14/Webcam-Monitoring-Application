import smtplib
import ssl
from email.message import EmailMessage
import imghdr


def send_message(image_path):
    host = "smtp.gmail.com"
    port = 587

    username = "<sender email>"
    password = "<sender token>"

    receiver = "<receiver email>"

    message = EmailMessage()
    message["Subject"] = "Someone Entered your Room!"
    message.set_content("AAAGH")

    with open(image_path, "rb") as file:
        content = file.read()

    message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_message("images/45.png")

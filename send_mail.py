import os
import smtplib
from email.message import EmailMessage
import imghdr
pw = os.getenv(PyPass)
sender = "alexlsouthall@yahoo.com"
receiver = "allalexandersouth@gmail.com"

def mail_send(IMAGE):
    email_msg = EmailMessage()
    email_msg["Subject"] = "Someone is here"
    email_msg.set_content("Some movement was detected")

    with open(IMAGE, "rb") as file:
        content = file.read()
    email_msg.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))


    gmail = smtplib.SMTP("smpt.mail.yahoo.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, pw)
    gmail.send(sender, receiver, email_msg.as_string())
    gmail.quit()



if __name__ == "__main__":
    mail_send("images/img_1.png")
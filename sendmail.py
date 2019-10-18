import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

emailid = "sidhu1397@gmail.com"
psswd = "agent 47"

s = smtplib.SMTP('in-v3.mailjet.com', 587)

s.starttls()
s.login(emailid, psswd)

msg = MIMEMultipart()

msg['FROM'] = emailid
msg['To'] = "sgtdavis322@gmail.com"
msg['SUBJECT'] = "This is a test email from smtplib"
body = """Dear subscriber,
                      Your cpu usage is currently above threshold.Please close non-imperative programs to maintain system stability.
                      This is a system generated mail do not reply.
        """
msg.attach(MIMEText(body, 'plain'))
s.send_message(msg)
print("mail was successfully sent")
del msg
s.quit()

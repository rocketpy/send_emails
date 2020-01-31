import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


subject = 'subject'
user_email = 'my_email'
password_email = 'my_password'
target_email = 'target_email'

msg = MIMEMultipart()
msg['From'] = user_email
msg['To'] = target_mail
msg['Subject'] = subject

body = 'Some text !'
msg.attach(MIMEText(body, 'plain'))

filename = 'filename'
attachment  = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user_email, password_email)

server.sendmail(user_email, target_email, text)
server.quit()

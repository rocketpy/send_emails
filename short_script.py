import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


msg = MIMEMultipart()

password = "password"
msg['From'] = "from_address"
msg['To'] = "to_address"
msg['Subject'] = "Attached Photo"
msg.attach(MIMEImage(file("abc.jpg").read()))
file = "file path"
fp = open(file, 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

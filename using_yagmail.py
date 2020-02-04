#  https://pypi.org/project/yagmail/
#  pip install yagmail


import yagmail


receiver = "your@gmail.com"
body = "Hello World !"
filename = "file_name.pdf"

yag = yagmail.SMTP("my_email@gmail.com")
yag.send(
    to=receiver,
    subject="Test with attachment",
    contents=body, 
    attachments=filename,
)



#  example taked from official docs !!!
import yagmail


yag = yagmail.SMTP()  # yag = yagmail.SMTP('mygmailusername', 'mygmailpassword')

contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('to@someone.com', 'subject', contents)

# Alternatively, with a simple one-liner:
yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)

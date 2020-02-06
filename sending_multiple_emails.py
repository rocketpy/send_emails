import csv
import ssl
import smtplib 


message = "Hi {name}, your grade is {grade}"

my_address = "my_email@gmail.com"
my_password = input("Type your password and press enter: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(my_address, my_password)
    
    with open("file_name.csv") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for name, email, grade in reader:
            server.sendmail(from_address,
                            email,
                            message.format(name=name,grade=grade))

#  first need sign up for a free !!   https://sendgrid.com/free/?source=sendgrid-python
#  take your request an API key  !!!
#  https://sendgrid.com/marketing/sendgrid-services-cro/#compare-plans

import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("YOUR_API_KEY"))

my_email = Email("my_email@gmail.com")
to_email = Email("to_some@gmail.com")
subject = "Some text"
content = Content("text/plain", "Here's a test email !")
mail = Mail(my_email, subject, to_email, content)

response = sg.client.mail.send.post(request_body=mail.get())


#  for debugging
print(response.body)
print(response.headers)
print(response.status_code)

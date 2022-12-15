import smtplib, ssl #importing the module

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_add = "schliessfach@fs-ei.de" #storing the sender's mail id
receiver_add = "lbeck@fs-ei.de" #"xlugggix@gmail.com" #storing the receiver's mail id
password = "Wd@OE_7411" #storing the password to log in
host = "mail.fs-ei.de"
port = 465

msg_to_be_sent ='''
Hello, receiver!
Hope you are doing well.
Welcome to PythonGeeks!
'''

message = MIMEMultipart("alternative")
message["Subject"] = "Schliessfach Verlängerung"
message["From"] = sender_add
message["To"] = receiver_add

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login("lbeck", password)

    server.sendmail(sender_add, receiver_add, message.as_string())
    
import smtplib, ssl #importing the module

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER = "schliessfach@fs-ei.de"
***REMOVED***
***REMOVED***
HOST = "mail.fs-ei.de"
PORT = 465

# Plain-text and HTML version of message
PLAIN_TEXT_MSG = """\
Hallo,
hier noch dein Vertrag fürs Schliessfach.
Lies dir gerne auch nochmal die Nutzerbedingungen durch https://fs-ei.de/de/services/lockers_guidelines/ .
Falls du Fragen hast oder irgendwas kaput ist melde dich gerne (schliessfach@fs-ei.de).

Gruß

LUGGGI (Lukas Beck)"""
HTML_MSG = """\
<html>
    <body>
        <p>Hallo,<br>
        hier noch dein Vertrag fürs Schliessfach.<br>
        Lies dir gerne auch nochmal die Nutzerbedingungen durch <a href="https://fs-ei.de/de/services/lockers_guidelines/">Nutzerbedingungen</a>. <br>
        Falls du Fragen hast oder irgendwas kaput ist melde dich gerne (<a href = "mailto: schliessfach@fs-ei.de">schliessfach@fs-ei.de</a>).<br>
        <br>
        Gruß<br>
        <br>
        LUGGGI (Lukas Beck)
        </p>
    </body>
</html>
"""

class Email:
    'send a predefined email to a new locker user with their contract'
    def send_message(self, receiver: str, file_dir: str, contract_name: str):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Schliessfach Vertrag und Nutzerbedingungen"
        message["From"] = SENDER
        message["To"] = receiver

        # Turn these into plain/html MIMEText objects
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(MIMEText(PLAIN_TEXT_MSG, "plain"))
        message.attach(MIMEText(HTML_MSG, "html"))

        # Open PDF file in binary mode
        with open(file_dir + "/" + contract_name, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            "attachment; filename= " + contract_name,
        )

        # Add attachments to message
        message.attach(part)

        # Create a secure SSL context and send email 
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
            server.login(USER, PASSWORD)
            server.sendmail(SENDER, receiver, message.as_string())
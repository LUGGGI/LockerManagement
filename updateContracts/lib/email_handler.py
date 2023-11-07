'''
This Module handles email communication for Locker

Author: Lukas Beck
Date: 16.07.2023
'''
from lib.email_messages import Message, new_contract, check_with_new_contract

import smtplib, ssl
import imaplib
import time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, make_msgid

SENDER = "schliessfach@fs-ei.de"
***REMOVED***
***REMOVED***
HOST = "mail.fs-ei.de"
PORT = 465

DEBUG = False # debug with MailTrap


class Email:
    'send a predefined email to a new locker user with their contract'

    def send_finished_contract(self, receiver: str, contract: str):
        '''Send the contract to the email receiver.
        
        :receiver: email-address to send to
        :contract: contract to send
        '''
        self.send_email(receiver, message=new_contract, subject="Schliessfach Vertrag und Nutzerbedingungen", attachment=contract)
        

    def send_email(self, receiver: str, message: Message, subject: str, attachment: str=None):
        '''Create an send an eMail.
        
        :receiver: email-address to send to
        :message: Message object with plain text and html versions
        :subject: Subject of eMail
        :attachment: attachment to add to email
        '''

        email = MIMEMultipart()
        email["Subject"] = subject
        email["From"] = SENDER
        email["To"] = receiver
        email["Date"] = formatdate(localtime=True)
        email["Message-ID"] = make_msgid(domain="fs-ei.de/schliessfach")

        # Turn these into plain/html MIMEText objects
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        email.attach(MIMEText(message.plain_text, "plain"))
        # email.attach(MIMEText(message.html, "html"))

        if attachment:
            # Open PDF file in binary mode
            with open(attachment, "rb") as file:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                "attachment; filename= " + attachment.split("/")[-1],
            )

            # Add attachments to message
            email.attach(part)

        
        if not DEBUG:
            # Create a secure SSL context and send email 
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
                server.login(USER, PASSWORD)
                server.sendmail(SENDER, receiver, email.as_string())

            # Move email to Sent folder
            with imaplib.IMAP4_SSL(HOST, 993) as server:
                server.login(USER, PASSWORD)
                server.append("Sent", '\\Seen', imaplib.Time2Internaldate(time.time()), email.as_string().encode("utf8"))
        else:
            # send email unsecured for MailTrap
            with smtplib.SMTP("sandbox.smtp.mailtrap.io", PORT) as server:
                server.login("704ed9de148a06", "963b4f6dc7f4e8")
                server.sendmail(SENDER, receiver, email.as_string())

if __name__ == "__main__":
    email = Email()
    email.send_finished_contract("beck-lukas@gmx.net", "ContractsNew/Formular_normal_sign.pdf")
'''
This Module handles email communication for Locker

Author: Lukas Beck
Date: 16.07.2023
'''
try:
    from Code.lib.email_messages import new_contract
except ModuleNotFoundError:
    from email_messages import new_contract

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
    '''Send emails.'''

    def __init__(self) -> None:
        '''Initializes the Email handler.'''
        self.emails: list = []


    def create_contract_email(self, email_address: str, contract: str):
        '''Send given contract per email.
        
        Args:
            email_address(str): Email address to send to.
            filename(str): name of the filename to send.
        '''
        send_email = input("Send Email? (Y/n): ")
        if send_email.lower() != "n":            
            self.create_email(email_address, message=new_contract, subject="Schliessfach Vertrag und Nutzerbedingungen", attachment=contract)
        

    def create_email(self, receiver: str, message: str, subject: str, attachment: str=None):
        '''Creates an email saves it to self.emails list.
        
        Args:
            receiver: email address to send to.
            message: message string.
            subject: subject of the email.
            attachment: path to attachment to add to email.
        '''

        email = MIMEMultipart()
        email["Subject"] = subject
        email["From"] = SENDER
        email["To"] = receiver
        email["Date"] = formatdate(localtime=True)
        email["Message-ID"] = make_msgid(domain="fs-ei.de/schliessfach")

        # Turn into plain MIMEText objects
        email.attach(MIMEText(message, "plain"))

        if attachment:
            # Open PDF file in binary mode
            with open(attachment, "rb") as file:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # reduce filename to ascii characters
            filename = self.convert_to_ascii(attachment.split("/")[-1])

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                "attachment; filename= " + filename,
            )

            # Add attachments to message
            email.attach(part)

        self.emails.append(email)


    def send_emails(self):
        '''Send emails saved in self.emails list.'''
        
        if not DEBUG:
            # Create a secure SSL context and send email 
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(HOST, PORT, context=context) as smtp_server:
                smtp_server.login(USER, PASSWORD)
                # Move email to Sent folder
                with imaplib.IMAP4_SSL(HOST, 993) as imap_server:
                    imap_server.login(USER, PASSWORD)
                    for email in self.emails:
                        smtp_server.sendmail(SENDER, email["To"], email.as_string())
                        imap_server.append("Sent", '\\Seen', imaplib.Time2Internaldate(time.time()), email.as_string().encode("utf8"))
                        print(f" -> Sent ({email['To']})")
                  
        else:
            # send email unsecured for MailTrap
            with smtplib.SMTP("sandbox.smtp.mailtrap.io", PORT) as smtp_server:
                smtp_server.login("704ed9de148a06", "963b4f6dc7f4e8")
                for email in self.emails:
                    smtp_server.sendmail(SENDER, email["To"], email.as_string())
                    print(f" -> Sent ({email['To']})")


    def convert_to_ascii(self, text: str) -> str:
        '''Tries to convert the text to ascii.
        
        Args:
            text(str): text to be converted.
        Returns:
            str: converted string.
        Raises:
            Exception: Text couldn't be converted.
        '''    
        if text.isascii():
            return text
        
        text = text.replace('ä', "ae")
        text = text.replace('ö', "oe")
        text = text.replace('ü', "ue")
        text = text.replace('é', "e")
        text = text.replace('è', "e")
        text = text.replace('ß', "ss")
        
        if text.isascii() == False:
            raise Exception(f"Can't convert {text} to ascii")
        return text
    

if __name__ == "__main__":
    email = Email()
    print(email.convert_to_ascii("lukäöüéèßs"))
    # email.create_email("lbeck@fs-ei.de", "Hello test", "TEst123", "../ContractsNew/Formular_normal_sign.pdf")
    # email.create_contract_email("beck-lukas@gmx.net", "../ContractsNew/Formular_normal_sign.pdf")
    # email.send_emails()
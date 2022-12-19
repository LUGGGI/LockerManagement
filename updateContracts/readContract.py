'''
readContract

This Module reads the data from the "Schliessfaecher" from and holds it

Author: Lukas Beck
Date: 17.12.2022
'''

from PyPDF2 import PdfReader
from datetime import datetime


class Contract:
    'gets the information from a contract and holds it'
    
    def __init__(self, file: str) -> None:
        self.fields = {}
        try:
            reader = PdfReader(file)
        except:
            raise Exception("File: " + file + " is not a contract")

        fields = reader.get_form_text_fields()
        try:
            self.fields["number"] = int(fields["Schließfachnummer"])
            self.fields["name"] = str(fields["Name"])
            self.fields["since"] = datetime.strptime(fields["Datum"], "%d.%m.%Y")
            self.fields["email"] = str(fields["MailAdresse"])
        except:
            raise Exception(file + ": One of the main fields is not found (Number, Name, Date, Email)")
        self.fields["collateral"] = int(50)
        self.fields["rented"] = int(1)

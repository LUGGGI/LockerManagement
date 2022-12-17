'''
readContract

This Module reads the data from the "Schliessfaecher" from and holds it

Author: Lukas Beck
Date: 17.12.2022
'''


from types import NoneType
from PyPDF2 import PdfReader
from datetime import datetime


class Contract:
    'gets the information from a contract and holds it'
    
    def __init__(self, file: str) -> None:
        self.fields = {}
        try:
            reader = PdfReader(file)
            fields = reader.get_form_text_fields()

            self.fields["number"] = int(fields["Schließfachnummer"])
            self.fields["name"] = str(fields["Name"])
            self.fields["since"] = datetime.strptime(fields["Datum"], "%d.%m.%Y")
            self.fields["email"] = str(fields["MailAdresse"])

            self.fields["collateral"] = int(50)
            self.fields["rented"] = int(1)
        except Exception as e:
            print("  Error: " + str(e))
            raise

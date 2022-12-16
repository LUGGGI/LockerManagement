# getDataFromForm
#
# This Program reads the date from the "Schliessfaecher" From and Saves it
#
# Author: Lukas Beck
# Date: 16.10.2022


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
            # self.fields["extended"] = NoneType
            self.fields["email"] = str(fields["MailAdresse"])

            self.fields["collateral"] = int(50)
            self.fields["rented"] = int(1)
        except Exception as e:
            print("  Error: " + str(e))
            self.fields["number"] = int(0)
            self.fields["name"] = str("Default")
            self.fields["since"] = datetime.strptime("01.01.2001", "%d.%m.%Y")
            self.fields["email"] = str("Default@default.de")

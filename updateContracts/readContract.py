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
    
    def __init__(self, file: str, check_if_closed=False) -> None:
        self.entries = {}
        try:
            reader = PdfReader(file)
        except:
            raise Exception("File: " + file + " is not a contract")

        fields = reader.get_form_text_fields()
        try:
            self.entries["number"] = int(fields["Schließfachnummer"])
            self.entries["name"] = str(fields["Name"])
            self.entries["since"] = datetime.strptime(fields["Datum"], "%d.%m.%Y")
            self.entries["email"] = str(fields["MailAdresse"])
        except:
            raise Exception(file + ": One of the main fields is not found (Number, Name, Date, Email)")
        self.entries["collateral"] = int(50)
        self.entries["rented"] = int(1)

        if check_if_closed:
            if fields["Datum_3"] != None:
                print("Contract " + file + " is closed")
                self.clear_contract()
            else:
                return
        
        print(self.entries)

    def clear_contract(self):
        self.entries["name"] = None
        self.entries["since"] = None
        self.entries["email"] = None
        self.entries["collateral"] = None
        self.entries["rented"] = None
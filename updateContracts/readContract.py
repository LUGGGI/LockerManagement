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
            self.fields["extended"] = NoneType
            self.fields["email"] = str(fields["MailAdresse"])
        except Exception as e:
            print("  Error: " + str(e))
            self.fields["number"] = int(0)
            self.fields["name"] = str("Default")
            self.fields["since"] = datetime.strptime("01.01.2001", "%d.%m.%Y")
            self.fields["extended"] = NoneType
            self.fields["email"] = str("Default@default.de")
    
    def add_remaining_values(self, number_keys: int):
        self.fields["collateral"] = int(50)
        # self.fields["comment"] = NoneType
        if number_keys < 1:
            raise Exception("No keys left")
        self.fields["keys"] = number_keys - 1
        self.fields["rented"] = int(1)

        is_fs = input(self.fields["name"] + " is from fs (y/N): ")
        if is_fs.lower() == "y":
            self.fields["fs"] = 1
            
        # self.fields["problem"] = NoneType
        # self.fields["revoked"] = NoneType
        # self.fields["cleared"] = NoneType

    def print(self):
        print("  Number: %3s, Name: %20s, Email: %30s, Date: %10s" 
            % (self.fields["number"], self.fields["name"], self.fields["email"], self.fields["since"].date()))

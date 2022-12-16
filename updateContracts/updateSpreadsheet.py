# Import the openpyxl library
from datetime import datetime
from xmlrpc.client import Boolean
import openpyxl


class UpdateSpreadsheet:
    'handles interaction with excel file'
    COLUMNS = {
        # key:          (type, column)
        "number":       (int, 'A'),
        "name":         (str, 'B'),
        "since":        (datetime, 'C'),
        "extended":     (datetime, 'D'),
        "email":        (str, 'E'),
        "collateral":   (int, 'F'),
        "comment":      (str, 'G'),
        "keys":         (int, 'H'),
        "rented":       (int, 'I'),
        "fs":           (int, 'J'),
        "problem":      (int, 'K'),
        "revoked":      (int, 'L'),
        "cleared":      (int, 'M'),
    }

    number_of_rows = 409
    number_of_cols = 13
    def __init__(self, file: str) -> None:
        self.workbook = openpyxl.load_workbook(file)
        self.worksheet = self.workbook.active
        self.file = file

    def print(self):
        'print the whole excel file'
        for row in self.worksheet.iter_rows(max_row=self.number_of_rows, max_col=self.number_of_cols, values_only=True):
            for cell in row:
                print("%s, " %cell, end =" ")
            print()

    def get_entry(self, number: int) -> dict:
        'returns a dictionary with all values for one row/entry in the sheet'
        entry = {}
        column = 'A'
        for value in self.worksheet[number+1]:
            entry[self.worksheet[column+"1"].value] = value.value
            column  = chr(ord(column)+1) # get next letter in alphabet
        return entry

    def update_entry(self, entry: dict) -> bool:
        ''
        row =  str(entry["number"]+1)
        self.check_entry(entry)

        current_values = self.get_entry(entry["number"])
        updated = False
        for key, value in entry.items():
            if value != current_values[key]: # only update value if different
                self.worksheet[self.COLUMNS[key][1]+row] = value
                print("update: %10s: %30s, replacing: %s" %(key, value, current_values[key]))
                updated = True
        if updated: # entry["name"] != current_values["name"]:
            if current_values["keys"] < 1:
                raise Exception("No keys left")
            self.worksheet[self.COLUMNS["keys"][1]+row] = current_values["keys"]-1
            print("update: %10s: %30s, replacing: %s" %("keys", current_values["keys"]-1, current_values["keys"]))  
        
        return updated

        


    def check_entry(self, entry: dict, check_order=False):
        'checks if the key and the associated type of the value are those specified in columns, can also check the order'
        if check_order:
            for key_given, key_check in zip(entry, self.COLUMNS):
                if key_given != key_check:
                    raise Exception("key must be %s but is %s" %(key_check, key_given))

        for key, value in entry.items():
            # print(type(value), columns[key][0])
            if not isinstance(value, self.COLUMNS[key][0]):
                raise Exception("type must be %s but is %s; Value is %s" %(self.COLUMNS[key][0], type(value), value))
            


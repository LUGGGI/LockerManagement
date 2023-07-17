'''
This Module handles the interaction with the spreadsheet.
Allows for reading, updating and checking of entries

Author: Lukas Beck
Date: 16.07.2023
'''

from datetime import datetime
import openpyxl


class Spreadsheet:
    'handles interaction with spreadsheets'
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

    def update_entry(self, new_entry: dict) -> bool:
        'gets an entry dictionary and updates the spreadsheet accordingly'
        row =  str(new_entry["number"]+1)
        # self.check_entry(entry)

        spreadsheet_entry = self.get_entry(new_entry["number"])
        updated = False
        extended = False

        if new_entry["name"] == spreadsheet_entry["name"]:
            if new_entry["since"] != spreadsheet_entry["since"]:
                new_entry["extended"] = new_entry["since"]
                new_entry["since"] = spreadsheet_entry["since"]
                print(f"Contract extended with date: {new_entry['extended']}")
                extended = True

        for key, value in new_entry.items():
            if value != spreadsheet_entry[key]: # only update value if different
                self.worksheet[self.COLUMNS[key][1]+row] = value
                print("update: %10s: %30s, replacing: %s" %(key, value, spreadsheet_entry[key]))
                updated = True
        
        if updated and not extended:
            # code for closing contract
            if new_entry["rented"] == None:
                self.worksheet[self.COLUMNS["keys"][1]+row] = spreadsheet_entry["keys"]+1
                self.worksheet[self.COLUMNS["fs"][1]+row] = None
                print("update: %10s: %30s, replacing: %s" %("keys", spreadsheet_entry["keys"]+1, spreadsheet_entry["keys"])) 
                print("update: %10s: %30s, replacing: %s" %("fs", None, spreadsheet_entry["fs"]))  
                return True
            
            # change number of keys in fs-office
            if spreadsheet_entry["keys"] < 1:
                raise Exception("No keys left")
            self.worksheet[self.COLUMNS["keys"][1]+row] = spreadsheet_entry["keys"]-1
            print("update: %10s: %30s, replacing: %s" %("keys", spreadsheet_entry["keys"]-1, spreadsheet_entry["keys"])) 

            # check if someone is from fs
            is_fs = input(new_entry["name"] + " is from fs (y/N): ")
            if is_fs.lower() == "y":
                new_entry["fs"] = 1
                self.worksheet[self.COLUMNS["fs"][1]+row] = int(1)
                print("update: %10s: %30s, replacing: %s" %("fs", 1, spreadsheet_entry["fs"]))  
        
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
            
    def get_table(self):
        '''Returns the whole locker table'''
        table = []
        for row in self.worksheet.iter_rows(max_row=self.number_of_rows, max_col=self.number_of_cols, values_only=True):
            table.append(row)
        return table
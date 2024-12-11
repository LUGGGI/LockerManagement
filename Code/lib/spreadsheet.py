'''
This Module handles the interaction with the spreadsheet.
Allows for reading, updating
'''
__author__ = "Lukas Beck"
__date__ = "11.12.2024"

from datetime import datetime
import openpyxl


class Spreadsheet:
    '''Handles interaction with spreadsheets.
    '''
    '''Methods:
    print_whole_sheet()
    remove_entry(locker_nr: int) -> bool
    extend_entry(locker_nr: int) -> bool
    update_entry(updated_entry: dict) -> bool
    get_entry(locker_nr: int) -> dict
    get_table() -> list[dict]
    '''

    COLUMNS = {
        # key:          column
        "number":       'A',
        "name":         'B',
        "since":        'C',
        "extended":     'D',
        "email":        'E',
        "collateral":   'F',
        "comment":      'G',
        "keys":         'H',
        "rented":       'I',
        "fs":           'J',
        "problem":      'K',
        "revoked":      'L',
        "cleared":      'M',
        "damage":       'N',
        "extend_code":  'O',
        "extend_check": 'P',
    }

    COLUMNS_TYPES = {
        "number":       int,
        "name":         str,
        "since":        datetime,
        "extended":     datetime,
        "email":        str,
        "collateral":   int,
        "comment":      str,
        "keys":         int,
        "rented":       int,
        "fs":           int,
        "problem":      int,
        "revoked":      int,
        "cleared":      int,
        "damage":       int,
        "extend_code":  int,
        "extend_check": int,
    }

    number_of_rows = 409
    number_of_cols = 16

    def __init__(self, file: str) -> None:
        self.workbook = openpyxl.load_workbook(file)
        self.worksheet = self.workbook.active
        self.file = file


    def print_whole_sheet(self):
        '''Print the whole excel file.'''
        for row in self.worksheet.iter_rows(max_row=self.number_of_rows, max_col=self.number_of_cols, values_only=True):
            for cell in row:
                print("%s, " %cell, end =" ")
            print()
    

    def remove_entry(self, locker_nr: int) -> bool:
        '''Removes the entry for the given locker number from the spreadsheet.
        
        Args:
            locker_nr(int): Number of the locker.
        '''
        spreadsheet_entry = self.get_entry(locker_nr)
        closed_entry = {
            "number": locker_nr,
            "name": None,
            "since": None,
            "extended": None,
            "email": None,
            "collateral": None,
            "rented": None,
            "keys": spreadsheet_entry["keys"]+1,
            "fs": None
        }
        return self.update_entry(closed_entry)


    def extend_entry(self, locker_nr: int) -> bool:
        '''Extends the given locker by updating the extended date.
        
        Args:
            locker_nr(int): Number of the locker to extend.
        '''
        entry = dict({"number": locker_nr, "extended": datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)})
        return self.update_entry(entry)


    def update_entry(self, updated_entry: dict) -> bool:
        '''Updates the spreadsheet according to the given entry.
        
        Args:
            updated_entry(dict): Values to update the spreadsheet with.
        Returns:
            bool: True if entry was updated, False if not.
        Raises:
            KeyError: If key is not found in the spreadsheet.
            TypeError: If type of value is not as specified in COLUMNS_TYPES.
        '''
        updated = False
        # get row number of entry (is locker number +1)
        row =  str(updated_entry["number"]+1)

        # get the old entry found in the spreadsheet
        current_entry = self.get_entry(updated_entry["number"])

        for key, value in updated_entry.items():
            # check if key is a valid key
            try:
                current_entry[key]
            except KeyError:
                raise KeyError(f"Key {key} not found in current spreadsheet entry")
            
            # Check if the the associated type of the value are those specified in COLUMNS_TYPES.
            if not isinstance(value, self.COLUMNS_TYPES[key]):
                raise TypeError(f"Type must be {self.COLUMNS_TYPES[key]} but is {type(value)}; Value is {value}")
            
            
            # update value only if different
            if value != current_entry[key]:
                self.worksheet[self.COLUMNS[key]+row] = value
                print("update: %10s: %30s, replacing: %s" %(key, value, current_entry[key]))
                updated = True
        
        return updated


    def get_entry(self, locker_nr: int) -> dict:
        '''Returns a dictionary with all values for given row/entry in the spreadsheet.
        
        Args:
            locker_nr(int): Number of the locker.
        Returns:
            dict: values in given row/entry.
        '''
        entry = {}
        column = 'A'
        for value in self.worksheet[locker_nr+1]:
            try:
                key = self.worksheet[column+"1"].value
                if self.COLUMNS[key] != column:
                    raise ValueError(f"Key value pair {key}: {column} not found in COLUMN dictionary, please update it")
            except KeyError:
                raise KeyError(f"Key {key} not found in current spreadsheet entry")
            except ValueError:
                raise
            # get key from first row and value from current row
            entry[self.worksheet[column+"1"].value] = value.value
            column  = chr(ord(column)+1) # get next letter in alphabet

        return entry


    def get_table(self) -> list[dict]:
        '''Returns the whole locker table as a list of dictionaries
        
        Returns:
            list[dict]: List of all entries in the spreadsheet.
        '''
        table = []
        for row in range(self.number_of_rows):
            table.append(self.get_entry(row))
        return table
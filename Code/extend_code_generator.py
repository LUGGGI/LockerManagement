'''
This program generates extend codes for all contracts and saves them in the spreadsheet.
'''
__author__ = "Lukas Beck"
__date__ = "12.12.2024"

import logging
import random

from Code.lib.locker_parent import LockerParent


class ExtendCodeGenerator(LockerParent):
    def __init__(self):
        super().__init__()

        print(f"This Program generates extend codes for all contracts and saves them in the spreadsheet.")
        
        self.load_spreadsheet()
        
        table = self.spreadsheet.get_table()
        print("Table loaded.")


        rented = list(filter(lambda x: x["rented"] == 1, table))
        entry_list = list(filter(lambda x: x["problem"] != 1, rented))

        # for testing get only one contract
        entry_list = list(filter(lambda x: x["number"] == 23, entry_list))
        print(entry_list)

        random_number_list = random.sample(range(999999), self.spreadsheet.number_of_rows)

        updated = False

        for entry, random_number in zip(entry_list, random_number_list):
            entry["extend_code"] = random_number
            entry["extend_check"] = 0
            # TODO: change update_entry to not update the keys
            updated = self.spreadsheet.update_entry(entry)

        if updated:
            self.save_spreadsheet()

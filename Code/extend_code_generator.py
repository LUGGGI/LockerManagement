'''
This program generates extend codes for all contracts and saves them in the spreadsheet.
'''
__author__ = "Lukas Beck"
__date__ = "06.02.2025"

import random

from Code.lib.locker_parent import LockerParent


class ExtendCodeGenerator(LockerParent):
    def __init__(self):
        super().__init__()

        print(f"This Program generates extend codes for all contracts and saves them in the spreadsheet.")
        
        self.load_spreadsheet()
        
        table = self.spreadsheet.get_table()
        print("Table loaded.")

        # get only rented lockers
        rented = list(filter(lambda x: x["rented"] == 1, table))
        # get only lockers that are not problem lockers (problem doesn't require extend code)
        entry_list = list(filter(lambda x: x["problem"] != 1, rented))

        # for testing get only one contract
        # entry_list = list(filter(lambda x: x["number"] == 23, entry_list))
        # print(entry_list)

        # ask if the user wants to generate new extend codes
        choice = input("Generate new extend codes? (y/N):").lower()
        if choice == "y":
            # get a list of random numbers to avoid duplicates
            random_number_list = random.sample(range(999999), self.spreadsheet.number_of_rows)

            updated = False

            for entry, random_number in zip(entry_list, random_number_list):
                entry["extend_code"] = random_number
                entry["extend_check"] = 0
                
                updated = self.spreadsheet.update_entry(entry)

            if updated:
                self.save_spreadsheet()

        choice = input("Export extend codes to csv? (y/N):").lower()
        if choice == "y":
            with open("extend_codes.csv", "w") as file:
                for entry in entry_list:
                    file.write(f"{entry['number']},{entry['extend_code']}\n")
            print(" -> Exported")

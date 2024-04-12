'''
This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached
'''
__author__ = "Lukas Beck"
__date__ = "17.10.2023"

import logging
from datetime import datetime

from Code.lib.locker_parent import LockerParent


NEW_CONTRACT_DIR = "../ContractsNew"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "../Locker.xlsx"

class ExtendContract(LockerParent):
    def __init__(self):
        super().__init__(SAVED_CONTRACT_DIR, SAVED_CONTRACT_DIR)

        print(f"This Programm extends contracts in the spreadsheet.")
        
        self.load_spreadsheet()

        while (True):
            try:
                locker_nr = input("Enter Locker number or enter EXIT to quit and save the spreadsheet: ")
                if locker_nr.lower() == "exit":
                    break
                entry = self.spreadsheet.get_entry(int(locker_nr))
                print(entry)
                
                if input("Extend this Contract? (Y/n)").lower() != "n":
                    entry["extended"]  = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    print(f"Updated entry: \n{entry}")

            except Exception as e:
                logging.exception(e)
                continue
        
        self.save_spreadsheet()


if __name__ == "__main__":
    ExtendContract()
    input("Press enter to exit: ")  
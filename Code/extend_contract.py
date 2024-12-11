'''
This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached
'''
__author__ = "Lukas Beck"
__date__ = "11.12.2024"

import logging

from Code.lib.locker_parent import LockerParent



class ExtendContract(LockerParent):
    def __init__(self):
        super().__init__()

        print(f"This Programm extends contracts in the spreadsheet.")
        
        self.load_spreadsheet()

        updated = False

        while (True):
            try:
                locker_nr = int(input("Enter Locker number or press enter to quit and save the spreadsheet: "))
                
                entry = self.spreadsheet.get_entry(locker_nr)
                print(entry)
                
                if input("Extend this Contract? (Y/n)").lower() != "n":
                    self.spreadsheet.extend_entry(locker_nr)
                    print(f"Extended entry: \n{locker_nr}")
                    updated = True
            except (TypeError, ValueError):
                # if no locker number is entered break the loop
                break
            except Exception as e:
                logging.exception(e)
                continue

        if updated:
            self.save_spreadsheet()


if __name__ == "__main__":
    ExtendContract()
    input("Press enter to exit: ")  
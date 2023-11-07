'''
This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached
'''
__author__ = "Lukas Beck"
__date__ = "17.10.2023"

import logging
from os import rename

from lib.locker_parent import LockerParent
from lib.contract_handler import Contract


NEW_CONTRACT_DIR = "../ContractsNew"
SAVED_CONTRACT_DIR = "../Contracts"


class AddContract(LockerParent):
    def __init__(self):
        super().__init__(NEW_CONTRACT_DIR, SAVED_CONTRACT_DIR)

        print(f"This Programm adds the contracts in the {self.work_folder} folder to the spreadsheets.")
        
        self.load_spreadsheet()

        
        for filename in self.filenames:
            try:
                if not any(chr.isdigit() for chr in filename): # skip non contract files
                    continue
                print(filename)
                # read contract
                contract = Contract(f"{self.work_folder}/{filename}")
                contract.read()

                # add contract name to filename 
                if filename.split('.')[0].isdigit(): # check if filename is only digits
                    name = contract.entries["name"].replace(' ', '_')
                    new_filename = filename.split('.')[0] + '_' + name + ".pdf"
                    
                    rename(self.work_folder + '/' + filename, self.work_folder + '/' + new_filename)
                    filename = new_filename


                # check entry and update the spreadsheet
                updated = self.spreadsheet.update_entry(contract.entries)

                if updated:
                    self.save_spreadsheet()     
                    self.send_contract(contract.entries["email"], filename)
                    self.move_contract(filename)
                            
            except Exception as e:
                logging.exception(e)
                continue


if __name__ == "__main__":
    AddContract()
    input("Press enter to exit: ")  
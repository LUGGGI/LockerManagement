'''
This Program reads all the contracts in the "Contracts" folder.
Then it removes for all closed contracts the entry from the spreadsheet.
It moves the closed contracts into the ContractsOld folder.
'''
__author__ = "Lukas Beck"
__date__ = "17.10.2023"

import logging

from Code.lib.locker_parent import LockerParent
from Code.lib.contract_handler import Contract, NotClosedError

OLD_CONTRACT_DIR = "../ContractsOld"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "../Locker.xlsx"

class RemoveContracts(LockerParent):
    def __init__(self):
        super().__init__(SAVED_CONTRACT_DIR, OLD_CONTRACT_DIR)

        print(f"This Programm checks the {self.work_folder} folder for closed contracts.")
        
        self.load_spreadsheet()

        
        for filename in self.filenames:
            try:
                if not any(chr.isdigit() for chr in filename): # skip non contract files
                    continue
                print(filename)
                # read contract and check if closed
                contract = Contract(self.work_folder + "/" + filename)
                try:
                    contract.read(check_if_closed=True)
                except NotClosedError:
                    continue

                # remove entry from the spreadsheet
                updated = self.spreadsheet.remove_entry(contract.entries["number"])

                if updated:
                    self.save_spreadsheet()
                    self.move_contract(filename)
                            
            except Exception as e:
                logging.exception(e)
                continue

if __name__ == "__main__":
    RemoveContracts()
    input("Press enter to exit: ")  
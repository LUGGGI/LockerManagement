'''
This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached

Author: Lukas Beck
Date: 17.10.2023
'''
import logging
from os import listdir, rename
from shutil import move

from contract_handler import Contract
from spreadsheet import Spreadsheet
from email_handler import Email
from fs_server_handler import upload_file


NEW_CONTRACT_DIR = "../ContractsNew"
OLD_CONTRACT_DIR = "../ContractsOld"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "../Locker.xlsx"

class Main:
    def __init__(self, work_folder: str, save_folder: str):
        '''Initializes the module.'''
        self.spreadsheet: Spreadsheet = None
        self.work_folder = work_folder
        self.save_folder = save_folder
        self.filenames = listdir(self.work_folder)


    def load_spreadsheet(self):
        '''Loads the spreadsheet from the defined SPREADSHEET path.'''
        for _ in range (5):
            try:
                self.spreadsheet = Spreadsheet(SPREADSHEET)
            except PermissionError:
                input("Please close all programs that have the spreadsheet open and start program again, press Enter to continue: ")
                continue
            except Exception as error:
                logging.exception(error)
                quit()
            else:
                break

    def save_spreadsheet(self):
        '''Saves the changed workbook to the spreadsheet file.'''
        save = input("Save entry to Spreadsheet? (Y/n): ")
        if save.lower() != "n":       
            self.spreadsheet.workbook.save(self.spreadsheet.file)  
            print(" -> Saved")

            
    def move_contract(self, filename: str):
        '''Move file to save folder.
        
        Args:
            filename(str): Name of the contract file.
        '''
        move_file = input(f"Move to {self.save_folder}(Y/n):") 
        if move_file.lower() != "n":
            for _ in range(3):
                try: 
                    move(self.work_folder + "/" + filename, self.save_folder + "/" + filename)
                    print(" -> Moved")
                    return
                except:
                    logging.error("!!  ERROR: " + filename + " can't be moved, close all programs that have it open")
                    input("press Enter to continue: ")
            raise Exception(filename + " can't be moved")


if __name__ == "__main__":
    main = Main()
    input("Press enter to exit: ")  
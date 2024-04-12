'''
Parent class for all locker programs.
'''
__author__ = "Lukas Beck"
__date__ = "07.11.2023"

import logging
from os import listdir
from shutil import move

from Code.lib.spreadsheet import Spreadsheet

NEW_CONTRACT_DIR = "../ContractsNew"
OLD_CONTRACT_DIR = "../ContractsOld"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "Locker.xlsx"

class LockerParent:
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


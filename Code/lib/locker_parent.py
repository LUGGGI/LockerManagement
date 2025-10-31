'''
Parent class for all locker programs.
'''
__author__ = "Lukas Beck"
__date__ = "23.08.2025"

import logging
from os import listdir
from shutil import move

from Code.lib.spreadsheet import Spreadsheet
from Code.lib.fs_server_handler import FsServerHandler

NEW_CONTRACT_DIR = "." # . is current directory
OLD_CONTRACT_DIR = "ContractsOld"
SAVED_CONTRACT_DIR = "Contracts"
SPREADSHEET = "Locker.xlsx"

# Find variables for email and fs_server  in their respective files

class LockerParent:
    def __init__(self, work_folder: str=NEW_CONTRACT_DIR, save_folder: str=SAVED_CONTRACT_DIR):
        '''Initializes the module.'''
        self.spreadsheet: Spreadsheet = None
        self.work_folder = work_folder
        self.save_folder = save_folder
        self.filenames = listdir(self.work_folder)

        self.fs_server_handler = FsServerHandler()

    def __del__(self):
        '''Destructor to clean up resources if necessary.'''
        if self.spreadsheet:
            try:
                self.spreadsheet.workbook.close()
                print("Spreadsheet closed.")
            except Exception as error:
                logging.exception("Error while closing spreadsheet: " + str(error))
        self.upload_database()
        self.fs_server_handler.sftp.close()

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
                    if self.save_folder != OLD_CONTRACT_DIR: # upload only if not moving to old contracts
                        self.fs_server_handler.upload_file(self.save_folder + "/" + filename)
                    else:
                        self.fs_server_handler.remove_from_active_add_to_old(self.save_folder + "/" + filename)
                    return
                except:
                    logging.error("!!  ERROR: " + filename + " can't be moved, close all programs that have it open")
                    input("press Enter to continue: ")
            raise Exception(filename + " can't be moved")
        
    def upload_database(self):
        '''Uploads the database to the fs server.'''
        if self.spreadsheet:
            self.fs_server_handler.upload_database(SPREADSHEET)


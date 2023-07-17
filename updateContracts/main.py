'''
This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached

Author: Lukas Beck
Date: 16.07.2023
'''
import logging
from os import listdir, rename
from shutil import move

from contract_handler import Contract
from spreadsheet import Spreadsheet
from email_handler import Email


NEW_CONTRACT_DIR = "../ContractsNew"
OLD_CONTRACT_DIR = "../ContractsOld"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "../Locker.xlsx"

class Main:
    def __init__(self):
        
        for _ in range (5):
            try:
                spreadsheet = Spreadsheet(SPREADSHEET)
            except PermissionError:
                input("Please close all programs that have the spreadsheet open and start program again, press Enter to continue: ")
                continue
            except Exception as error:
                logging.exception(error)
                quit()
            else:
                break
            

        email = Email()

        self.work_folder = NEW_CONTRACT_DIR
        self.save_folder = SAVED_CONTRACT_DIR
        check_if_closed = False
        filenames = listdir(self.work_folder)

        # if there are no contracts in ContractsNew then the program will scan for contracts to remove

        if filenames.__len__() <= 4:
            self.work_folder = SAVED_CONTRACT_DIR
            self.save_folder = OLD_CONTRACT_DIR
            check_if_closed = True
            filenames = listdir(self.work_folder)

        
        for filename in filenames:
            try:
                if not any(chr.isdigit() for chr in filename): # skip non contract files
                    continue
                print(filename)
                # read contract
                contract = Contract(self.work_folder + "/" + filename)
                contract.read(check_if_closed)

                # add contract name to filename 
                if filename.split('.')[0].isdigit(): # check if filename is only digits
                    name = contract.entries["name"].replace(' ', '_')
                    new_filename = filename.split('.')[0] + '_' + name + ".pdf"
                    
                    rename(self.work_folder + '/' + filename, self.work_folder + '/' + new_filename)
                    filename = new_filename


                # check entry and update the spreadsheet
                updated = spreadsheet.update_entry(contract.entries)

                if updated:
                    save = input("Save entry to file? (Y/n): ")
                    if save.lower() != "n":       
                        spreadsheet.workbook.save(spreadsheet.file)  
                        print(" -> Saved")      
                    if contract.entries["rented"] == 1:
                        send_email = input("Send Email? (Y/n): ")
                        if send_email.lower() != "n":
                            email.send_finished_contract(contract.entries["email"], f"{self.work_folder}/{filename}")
                            print(" -> Sent")

                    move_file = input("Move to " + self.save_folder + " folder? (Y/n): ") 
                    if move_file.lower() != "n":
                        self.move_contract(filename)
                            
            except Exception as e:
                logging.exception(e)
                continue

            
    def move_contract(self, filename):
        'move file to save folder'    
        for _ in range(3):
            try: 
                move(self.work_folder + "/" + filename, self.save_folder + "/" + filename)
                print(" -> Moved")
                return
            except:
                logging.error("!!  ERROR: " + filename + " can't be moved, close all programs that have it open")
                input("press Enter to continue: ")
        raise Exception(filename + " can't be moved")
    
    def close_contract(self):
        pass

main = Main()
input("Press enter to exit: ")  
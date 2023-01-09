'''
UpdateContracts

This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached

Author: Lukas Beck
Date: 17.12.2022
'''

from os import listdir, rename
from shutil import move

from readContract import Contract
from updateSpreadsheet import UpdateSpreadsheet
from sendEmail import Email


NEW_CONTRACT_DIR = "../ContractsNew"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "../Locker.xlsx"

class Main:
    def __init__(self):

        try:
            spreadsheet = UpdateSpreadsheet(SPREADSHEET)
        except:
            input("!!!  ERROR: Please close all programs that have the spreadsheet open and start program again, press Enter to exit: ")
            quit()

        email = Email()

        filenames = listdir(NEW_CONTRACT_DIR)
        for filename in filenames:
            try:
                if not any(chr.isdigit() for chr in filename): # skip non contract files
                    continue
                print(filename)
                # read contract
                contract = Contract(NEW_CONTRACT_DIR + "/" + filename)
                print(contract.fields)

                # add contract name to filename 
                if filename.split('.')[0].isdigit(): # check if filename is only digits
                    name = contract.fields["name"].replace(' ', '_')
                    new_filename = filename.split('.')[0] + '_' + name + ".pdf"
                    
                    rename(NEW_CONTRACT_DIR + '/' + filename, NEW_CONTRACT_DIR + '/' + new_filename)
                    filename = new_filename


                # check entry and update the spreadsheet
                updated = spreadsheet.update_entry(contract.fields)

                if updated:
                    save = input("Save entry to file? (Y/n): ")
                    if save.lower() != "n":       
                        spreadsheet.workbook.save(spreadsheet.file)  
                        print(" -> Saved")      

                    send_email = input("Send Email? (Y/n): ")
                    if send_email.lower() != "n":
                        email.send_message(contract.fields["email"], NEW_CONTRACT_DIR, filename)
                        print(" -> Sent")

                move_file = input("Move to Contracts folder? (Y/n): ") 
                if move_file.lower() != "n":
                    self.move_contract(filename)
                            
            except Exception as e:
                print("!!!  ERROR: " + str(e))
                continue

            
    def move_contract(self, filename):
        'move file to contracts folder'    
        for _ in range(3):
            try: 
                move(NEW_CONTRACT_DIR + "/" + filename, SAVED_CONTRACT_DIR + "/" + filename)
                print(" -> Moved")
                return
            except:
                input("!!  ERROR: " + filename + " can't be moved, close all programs that have it open and press Enter: ")
        raise Exception(filename + " can't be moved")

main = Main()
input("Press enter to exit: ")  
'''
UpdateContracts

This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached

Author: Lukas Beck
Date: 17.12.2022
'''

from os import listdir
from shutil import move

from readContract import Contract
from updateSpreadsheet import UpdateSpreadsheet
from sendEmail import Email



NEW_CONTRACT_DIR = "../ContractsNew"
SAVED_CONTRACT_DIR = "../Contracts"
SPREADSHEET = "../Locker.xlsx"


spreadsheet = UpdateSpreadsheet(SPREADSHEET)
email = Email()

filenames = listdir(NEW_CONTRACT_DIR)
for filename in filenames:
    if not any(chr.isdigit() for chr in filename): # skip non contract files
        continue
    
    # read contract
    try:
        contract = Contract(NEW_CONTRACT_DIR + "/" + filename)
    except:
        break
    print(contract.fields)

    updated = spreadsheet.update_entry(contract.fields)

    if updated or True:
        save = input("Save entry to file? (y/N): ")
        if save.lower() == "y":       
            spreadsheet.workbook.save(spreadsheet.file)        

        send_email = input("Send Email? (y/N): ")
        if send_email.lower() == "y": 
            email.send_message("beck-lukas@gmx.net", NEW_CONTRACT_DIR, filename)
            # email.send_message(contract.fields["email"], NEW_CONTRACT_DIR, filename)

    move_file = input("Move to Contracts folder? (Y/n): ") 
    if move_file.lower() != "n":       
        move(NEW_CONTRACT_DIR + "/" + filename, SAVED_CONTRACT_DIR + "/" + filename)


input("Press enter to exit: ")        
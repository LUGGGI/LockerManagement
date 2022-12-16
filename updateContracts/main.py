from os import listdir
from shutil import move

from readContract import Contract
from updateSpreadsheet import UpdateSpreadsheet
from sendEmail import Email



NEW_CONTRACT_DIR = "ContractsNew"
SAVED_CONTRACT_DIR = "Contracts"
SPREADSHEET = "Schließfächer_new.xlsx"

contracts = []

spreadsheet = UpdateSpreadsheet(SPREADSHEET)
email = Email()

filenames = listdir(NEW_CONTRACT_DIR)
for filename in filenames:
    if filename == "Formular_digital_sign.pdf" or filename == "Formular_normal_sign.pdf" or filename == "Nutzungsbedingungen.pdf":
        continue
    
    # read contract
    contract = Contract(NEW_CONTRACT_DIR + "/" + filename)
    contracts.append(contract)

    # add remaining values
    # old_number_of_keys = spreadsheet.get_entry(contract.fields["number"])["keys"]
    contract.add_remaining_values()

    print(contract.fields)

    updated = spreadsheet.update_entry(contract.fields)

    if not updated:
        continue

    save = input("Save entry to file? (y/N): ")
    if save.lower() == "y":       
        spreadsheet.workbook.save(spreadsheet.file)        

    send_email = input("Send Email? (y/N): ")
    if send_email.lower() == "y": 
        email.send_message(contract.fields["email"], NEW_CONTRACT_DIR, filename)

    move_file = input("Move to Contracts folder? (Y/n): ") 
    if move_file.lower() != "n":       
        move(NEW_CONTRACT_DIR + "/" + filename, SAVED_CONTRACT_DIR + "/" + filename)
        

'''
This Program reads all the contracts in the "ContractsNew" folder.
It can add the values to the Locker.xlsx and send an email to the contract holder with the contract attached

Author: Lukas Beck
Date: 16.07.2023
'''
import logging
import datetime
from os import listdir, rename
import shutil
import copy

from contract_handler import Contract
from spreadsheet import Spreadsheet
from email_handler import Email
from email_messages import check_with_new_contract_25, check_with_new_contract, check_with_new_contract_fs_25, check_with_new_contract_fs


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
            
        table = spreadsheet.get_table()
        
        
        all_rented = list(filter(lambda x: x[8] == 1, table))
        no_error = list(filter(lambda x: x[10] != 1, all_rented))
        all_not_fs = list(filter(lambda x: x[9] != 1, no_error))
        all_fs = list(filter(lambda x: x[9] == 1, no_error))
        all_old = list(filter(lambda x: x[2] < datetime.datetime(2022, 10, 20), all_fs))

        old_50 = list(filter(lambda x: x[5] == 50, all_old))
        old_25 = list(filter(lambda x: x[5] == 25, all_old))

        data_for_new_contracts_25 = []
        for entry in old_25:
            data_for_new_contracts_25.append({"number": entry[0], "name": entry[1], "email": entry[4], "comment": entry[6]})
            
        data_for_new_contracts_50 = []
        for entry in old_50:
            data_for_new_contracts_50.append({"number": entry[0], "name": entry[1], "email": entry[4], "comment": entry[6]})

        for entry in data_for_new_contracts_25:
            if entry["number"] == 1:
                continue
            shutil.copy(f"{NEW_CONTRACT_DIR}/Formular_normal_sign.pdf", f"{NEW_CONTRACT_DIR}/{entry['number']}.pdf")
            # contract = Contract(f"{NEW_CONTRACT_DIR}/{entry['Schließfachnummer']}.pdf")
            # contract.write(entry)
            message = copy.copy(check_with_new_contract_fs_25)
            message.plain_text = message.plain_text.replace("{name}", entry["name"])
            message.plain_text = message.plain_text.replace("{number}", str(entry["number"]))
            message.html = message.html.replace("{name}", entry["name"])
            message.html = message.html.replace("{number}", str(entry["number"]))
            # print(message.plain_text)
            subject = "Schließfachverlängerung (locker renewal)"
            Email().send_email(entry["email"], message, subject, f"{NEW_CONTRACT_DIR}/{entry['number']}.pdf")
            print(f"{entry['number']}: {entry['name']}, Done")

            


        for entry in data_for_new_contracts_50:
            if entry["number"] == 2:
                continue
            shutil.copy(f"{NEW_CONTRACT_DIR}/Formular_normal_sign.pdf", f"{NEW_CONTRACT_DIR}/{entry['number']}.pdf")
            # contract = Contract(f"{NEW_CONTRACT_DIR}/{entry['Schließfachnummer']}.pdf")
            # contract.write(entry)
            message = copy.copy(check_with_new_contract_fs)
            message.plain_text = message.plain_text.replace("{name}", entry["name"])
            message.plain_text = message.plain_text.replace("{number}", str(entry["number"]))
            message.html = message.html.replace("{name}", entry["name"])
            message.html = message.html.replace("{number}", str(entry["number"]))
            # print(message.plain_text)
            subject = "Schließfachverlängerung (locker renewal)"
            Email().send_email(entry["email"], message, subject, f"{NEW_CONTRACT_DIR}/{entry['number']}.pdf")
            print(f"{entry['number']}: {entry['name']}, Done")

            

        return
        
        

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
                contract = Contract(self.work_folder + "/" + filename, check_if_closed)

                # add contract name to filename 
                if filename.split('.')[0].isdigit(): # check if filename is only digits
                    name = contract.entries["name"].replace(' ', '_')
                    new_filename = filename.split('.')[0] + '_' + name + ".pdf"
                    
                    rename(self.work_folder + '/' + filename, self.work_folder + '/' + new_filename)
                    filename = new_filename


                # check entry and update the spreadsheet
                updated = spreadsheet.update_entry(contract.entries)

                if updated:
                    # save = input("Save entry to file? (Y/n): ")
                    # if save.lower() != "n":       
                    #     spreadsheet.workbook.save(spreadsheet.file)  
                    #     print(" -> Saved")      
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
                shutil.move(self.work_folder + "/" + filename, self.save_folder + "/" + filename)
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
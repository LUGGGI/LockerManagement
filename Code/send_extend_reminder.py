'''
Send emails to people with contracts in the spreadsheet.
'''
__author__ = "Lukas Beck"
__date__ = "10.11.2023"

import datetime

from lib.locker_parent import LockerParent
from lib.contract_handler import Contract
from lib.email_handler import Email
from lib.email_messages import check_with_new_contract_25, check_with_new_contract, check_with_new_contract_fs_25, check_with_new_contract_fs


NEW_CONTRACT_DIR = "../ContractsNew"
SAVED_CONTRACT_DIR = "../Contracts"

class SendExtendReminder(LockerParent):
    def __init__(self):
        super().__init__(NEW_CONTRACT_DIR, SAVED_CONTRACT_DIR)
        
        print(f"This Programm sends extend reminders.")

        self.load_spreadsheet()
            
        table = self.spreadsheet.get_table()
        
        print("Table loaded.")
        
        rented = list(filter(lambda x: x[8] == 1, table))
        no_error = list(filter(lambda x: x[10] != 1, rented))
        old = list(filter(lambda x: x[2] < datetime.datetime(2022, 10, 20), no_error))
        not_extended = list(filter(lambda x: (x[3] == None) or (x[3] < datetime.datetime(2022, 10, 20)), old))

        all_not_fs = list(filter(lambda x: x[9] != 1, not_extended))
        all_fs = list(filter(lambda x: x[9] == 1, not_extended))


        all_fs_50 = list(filter(lambda x: x[5] == 50, all_fs))
        all_fs_25 = list(filter(lambda x: x[5] == 25, all_fs))

        all_not_fs_50 = list(filter(lambda x: x[5] == 50, all_not_fs))
        all_not_fs_25 = list(filter(lambda x: x[5] == 25, all_not_fs))

        print("\nFS")
        self.send_emails(all_fs_50, check_with_new_contract_fs)
        print("\nFS_25")
        self.send_emails(all_fs_25, check_with_new_contract_fs_25)
        print("\nNOT_FS")
        self.send_emails(all_not_fs_50, check_with_new_contract)
        print("\nNOT_FS_25")
        self.send_emails(all_not_fs_25, check_with_new_contract_25)
        

            
    def send_emails(self, entries: list, message: str):
        '''Sends emails to the given entries.
        
            Args:
                entries: list of contract holders to send message to.
                message: message to send:
        '''
        email = Email()
        for entry in entries:
            print(entry)
            message_with_data = message.replace("{number}", str(entry[0]))
            message_with_data = message_with_data.replace("{name}", entry[1])
            email.create_email(
                receiver=entry[4], 
                message=message_with_data, 
                subject="Schließfachverlängerung (locker renewal)", 
                attachment="../ContractsNew/Formular_normal_sign.pdf"
            )

        send = input("Send emails to listed contracts? (Y/n): ")
        if send.lower() != "n":               
            email.send_emails()





if __name__ == "__main__":
    SendExtendReminder()
    input("Press enter to exit: ")  
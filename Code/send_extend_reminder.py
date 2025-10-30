'''
Send emails to people with contracts in the spreadsheet.
'''
__author__ = "Lukas Beck"
__date__ = "06.02.2025"

import datetime

from Code.lib.locker_parent import LockerParent
from Code.lib.email_handler import Email
from Code.lib.email_messages import check_with_new_contract_25, check_with_new_contract, check_with_new_contract_fs_25, check_with_new_contract_fs


class SendExtendReminder(LockerParent):
    def __init__(self):
        super().__init__()
        
        print(f"This program sends extend reminders with the extend codes.")

        self.load_spreadsheet()
            
        table = self.spreadsheet.get_table()
        print("Table loaded.")

        # get only rented lockers
        table = list(filter(lambda x: x["rented"] == 1, table))
        # get only lockers that are not problem lockers (problem doesn't require extend code)
        table = list(filter(lambda x: x["problem"] != 1, table))

        # for testing get only one contract
        # entry_list = list(filter(lambda x: x["number"] == 23, entry_list))
        # print(entry_list)

        # get only lockers that are older than 5 months
        table = list(filter(lambda x: x["created"] < datetime.datetime.now()-datetime.timedelta(weeks=22), table))

        # TODO: Add new logic that ask for time
        # get only lockers that are not extended in the last 5 months
        table = list(filter(lambda x: x["extended"] < datetime.datetime.now()-datetime.timedelta(weeks=22), table))

        # get only lockers that are fs (fs = Fachschaft)
        table_from_fs = list(filter(lambda x: x["fs"] == 1, table))

        # get only lockers that are not fs (fs = Fachschaft)
        table_not_from_fs = list(filter(lambda x: x["fs"] != 1, table))


        print(table_not_from_fs)
        

            
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
                subject="Info über Entzug deines Schließfachs", 
                attachment="../ContractsNew/Formular_normal_sign.pdf"
            )

        send = input("Send emails to listed contracts? (Y/n): ")
        if send.lower() != "n":               
            email.send_emails()





if __name__ == "__main__":
    SendExtendReminder()
    input("Press enter to exit: ")  
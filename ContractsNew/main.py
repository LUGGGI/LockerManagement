'''
Execute programs
'''
__author__ = "Lukas Beck"
__date__ = "07.11.2023"

from Code.add_contract import AddContract
from Code.extend_contract import ExtendContract
from Code.remove_contract import RemoveContracts
from Code.send_extend_reminder import SendExtendReminder

if __name__ == "__main__":
    while(True):
        print("This program handles interaction between spreadsheets and contracts, it can:"
            + "\nA: Add a contract"
            + "\nE: Extend a contract"
            + "\nR: Remove a contract"
            + "\nS: Send extend reminder"
            + "Press enter to exit: "
            )
        choice = input("Please enter the letter for the wanted function (A/E/R/S): ").lower()
        if choice == "a":
            AddContract()
        elif choice == "e":
            ExtendContract()
        elif choice == "r":
            RemoveContracts()
        elif choice == "s":
            SendExtendReminder()
        else:
            break

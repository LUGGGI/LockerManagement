'''
Execute programs
'''
__author__ = "Lukas Beck"
__date__ = "07.11.2023"

from add_contract import AddContract
from extend_contract import ExtendContract
from remove_contract import RemoveContracts

if __name__ == "__main__":
    while(True):
        print("This program handles interaction between spreadsheets and contracts, it can:"
            + "\nA: Add a contract"
            + "\nE: Extend a contract"
            + "\nR: Remove a contract"
            + "Press enter to exit: "
            )
        choice = input("Please enter the letter for the wanted function (A/E/R): ").lower()
        if choice == "a":
            AddContract()
        elif choice == "e":
            ExtendContract()
        elif choice == "r":
            RemoveContracts()
        else:
            break

'''
Execute programs

This program needs the following directory structure:
- Contracts
- ContractsNew
    - Code
    - Locker.xlsx
    - main.py
- ContractsOld
'''
__author__ = "Lukas Beck"
__date__ = "13.09.2024"

import logging

try:
    from Code.add_contract import AddContract
    from Code.extend_contract import ExtendContract
    from Code.remove_contract import RemoveContracts
    from Code.send_extend_reminder import SendExtendReminder
    from Code.extend_code_generator import ExtendCodeGenerator
    from Code.extend_update_from_file import ExtendUpdateFromFile


    # input("Press Enter to start the program.")
    ExtendUpdateFromFile()
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")

except Exception as e:
    logging.exception("Fatal error in main program: " + str(e))
    input("Press Enter to exit.")
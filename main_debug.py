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

from Code.add_contract import AddContract
from Code.extend_contract import ExtendContract
from Code.remove_contract import RemoveContracts
from Code.send_extend_reminder import SendExtendReminder
from Code.extend_code_generator import ExtendCodeGenerator

if __name__ == "__main__":
    AddContract()

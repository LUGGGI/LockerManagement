import os

from readContract import Contract
from updateSpreadsheet import UpdateSpreadsheet



dir = "../ContractsNew"

contracts = []

filenames = os.listdir(dir)
for filename in filenames:
    if filename == "Formular_digital_sign.pdf" or filename == "Formular_normal_sign.pdf" or filename == "Nutzungsbedingungen.pdf":
        continue

    contracts.append(Contract(dir + "/" + filename))


spreadsheet = UpdateSpreadsheet("Schließfächer_new.xlsx")

for contract in contracts:
    contract.add_remaining_values(2)
    print(contract.fields)



# spreadsheet.print()
# entry = spreadsheet.get_entry(1)
# print(entry)
# entry["numbers"] = int(2)
# spreadsheet.check_entry(entry, check_order=False)
# print(entry)
# spreadsheet.update_entry(entry)

# entry = spreadsheet.get_entry(8)
# print(entry)

for contract in contracts:
    spreadsheet.update_entry(contract.fields)
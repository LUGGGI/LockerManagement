'''
This Module handles the data from the "Schliessfaecher" from

Author: Lukas Beck
Date: 16.07.2023
'''

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, IndirectObject
from datetime import datetime


class Contract:
    '''Handles entry from contract form'''
    
    def __init__(self, file: str) -> None:
        self.file = file
        self.entries = {}

    def read(self, check_if_closed=False):
        
        try:
            reader = PdfReader(self.file)
        except:
            raise Exception("File: " + self.file + " is not a contract")

        fields = reader.get_form_text_fields()
        try:
            self.entries["number"] = int(fields["Schließfachnummer"])
            self.entries["name"] = str(fields["Name"])
            self.entries["since"] = datetime.strptime(fields["Datum"], "%d.%m.%Y")
            self.entries["email"] = str(fields["MailAdresse"])
        except:
            raise Exception(self.file + ": One of the main fields is not found (Number, Name, Date, Email)")
        self.entries["collateral"] = int(50)
        self.entries["rented"] = int(1)

        if check_if_closed:
            if fields["Datum_3"] != None:
                print("Contract " + self.file + " is closed")
                self.clear_contract()
            else:
                return
        
        print(self.entries)

    def write(self, entry: dict):
        '''Write data in entry into Form, panics if field (key) is not found
        
        :entry: data to write to the file
        '''

        reader = PdfReader(self.file)
        if "/AcroForm" in reader.trailer["/Root"]: # result: following "IF code is executed
            reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        writer = PdfWriter()
        self.set_need_appearances_writer(writer)
        if "/AcroForm" in writer._root_object: # result: False - following "IF" code is NOT executed
            writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        
        writer.add_page(reader.pages[0])
        
        writer.update_page_form_field_values(writer.pages[0], entry)

        with open(self.file, "wb") as output_stream:
            writer.write(output_stream)


    def set_need_appearances_writer(self, writer: PdfWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
        try:
            catalog = writer._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer
        

    def clear_contract(self):
        self.entries["name"] = None
        self.entries["since"] = None
        self.entries["email"] = None
        self.entries["collateral"] = None
        self.entries["rented"] = None
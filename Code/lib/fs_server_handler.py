"""
This Module handles the transfer of files to the fs server.
Private/ public key combo is used for authentication.

Author: Lukas Beck
Date: 23.08.2025
"""

import os
from json import load

import sftpretty

SERVER = "ivie.ei.faveve.uni-stuttgart.de"
LOCKER_DIR = "/import/fs-ei/service/schliessfaecher/Locker"
FOLDER_ACTIVE = f"{LOCKER_DIR}/Contracts"
FOLDER_OLD = f"{LOCKER_DIR}/ContractsOld"
# Login file has to be a json file with the following structure: # password is not needed for this function
# {
#     "user": "username",
#     "password": "password"
# }
LOGIN_FILE = "C:/Users/LUGGGI/.ssh/login.json" # file should not be in git repository
PRIVATE_KEY_FILE = "C:/Users/LUGGGI/.ssh/id_rsa" # private key file for authentication

FILE_PERMISSIONS = 600 # rw-------
LOCAL_FOLDER = "Contracts" # local folder to sync with server

class FsServerHandler:
    """Handles the upload of files to the fs server."""

    def __init__(self) -> None:
        """Initializes the FsServerHandler."""
        # get user and password from login file
        with open(LOGIN_FILE, "r") as file:
            login = load(file)
            self.user = login["user"]

        self.sftp = sftpretty.Connection(host=SERVER, username=self.user, private_key=PRIVATE_KEY_FILE)
        print("Connected to fs server.")

    def upload_file(self, file: str):
        """Uploads file to server with correct permissions.
        
        Args:
            file (str): PDF file to upload
        """
        # check if file exists locally and is a pdf file
        if not os.path.isfile(file) or not file.lower().endswith(".pdf"):
            print(f"File {file} does not exist or is not a PDF file.")
            return

        self.sftp.chdir(FOLDER_ACTIVE)
        self.sftp.put(file)

        command = f"chmod {FILE_PERMISSIONS} {FOLDER_ACTIVE}/{file}"
        self.sftp.execute(command=command)
        print(" -> Uploaded")

    def remove_from_active_add_to_old(self, file_path: str):
        """Removes file from active folder and adds new file to old folder.

        Args:
            file (str): PDF file to move
        """
        file = os.path.basename(file_path) # get only filename from path

        self.sftp.chdir(FOLDER_ACTIVE)
        if file not in self.sftp.listdir():
            print(f"File {file} does not exist on server.")
            return
        self.sftp.remove(file)
        self.sftp.chdir(FOLDER_OLD)
        self.sftp.put(file_path)

        command = f"chmod {FILE_PERMISSIONS} {FOLDER_OLD}/{file}"
        self.sftp.execute(command=command)

        print(f" -> Moved {file} to ContractsOld")

    def sync_active_folder(self):
        """Syncs the active contracts folder with the local folder.
        
        List inconsistencies between local and server folder.

        Then aks if local or server files are currently correct and syncs the other side to it.
        """
        self.sftp.chdir(FOLDER_ACTIVE)
        server_files = self.sftp.listdir()
        print("Files on server:")
        print(server_files)

        local_files = os.listdir(LOCAL_FOLDER)
        print("Files locally:")
        print(local_files)

        ignore_files = [".dummy", "orginale"]

        to_upload = [f for f in local_files if f not in server_files and f not in ignore_files]
        to_download = [f for f in server_files if f not in local_files and f not in ignore_files]

        if not to_upload and not to_download:
            print("Folders are already in sync.")
            return

        if to_upload:
            print("Files not found on server:")
            print(to_upload)
        if to_download:
            print("Files not found on local:")
            print(to_download)

        choice = input("Which side is correct? (l)ocal/(s)erver: ")
        if choice.lower() == "l":
            # upload missing files to server
            for file in to_upload:
                self.upload_file(f"{LOCAL_FOLDER}/{file}")
            # remove files from server that are not local
            for file in to_download:
                self.sftp.remove(file)
                print(f" -> Removed {file} from server")
        elif choice.lower() == "s":
            for file in to_download:
                self.sftp.get(file)
                # copy to local folder
                os.replace(file, f"{LOCAL_FOLDER}/{file}")
                print(f" -> Downloaded {file}")
            # remove local files that are not on server
            for file in to_upload:
                os.remove(f"{LOCAL_FOLDER}/{file}")
                print(f" -> Removed {file} locally")
        else:
            print("Invalid choice. No action taken.")

    def upload_database(self, database_file: str):
        """Uploads the database file to the server.

        Args:
            database_file (str): Path to the database file.
        """
        if not os.path.isfile(database_file):
            print(f"Database file {database_file} does not exist.")
            return

        self.sftp.chdir(LOCKER_DIR)
        self.sftp.put(database_file)

        command = f"chmod {FILE_PERMISSIONS} {LOCKER_DIR}/{database_file}"
        self.sftp.execute(command=command)
        print(" -> Uploaded database file.")


    def close(self):
        """Closes the connection to the server."""
        self.sftp.close()
        print("Connection closed.")
        

if __name__ == "__main__":

    fs_server_handler = FsServerHandler()
    # fs_server_handler.upload_file("Formular.pdf")
    # fs_server_handler.move_file_to_contracts_old("Formular.pdf")
    # fs_server_handler.sync_active_folder()
    fs_server_handler.upload_database("Locker.xlsx")
    fs_server_handler.close()
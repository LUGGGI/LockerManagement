'''
This Module handles the transfer of files to the fs server.
Private/ public key combo is used for authentication.

Author: Lukas Beck
Date: 11.08.2023
'''

from paramiko import SSHClient
from scp import SCPClient
from json import load

SERVER = "ivie.ei.faveve.uni-stuttgart.de"
FOLDER = "/import/fs-ei/service/schliessfaecher/Locker/ContractsNew"
USER = "lbeck"
# Login file has to be a json file with the following structure: # password is not needed for this function
# {
#     "user": "username",
#     "password": "password"
# }
LOGIN_FILE = "C:/Users/LUGGGI/.ssh/login.json" # file should not be in git repository

def upload_file(file: str):
    '''Uploads file to server with correct permissions.
    
    :file: file to upload
    '''
    # get user and password from login file
    with open(LOGIN_FILE, "r") as file:
        login = load(file)
        user = login["user"]

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=SERVER, username=user)

    # SCPClient takes a paramiko transport as an argument
    scp = SCPClient(ssh.get_transport())
    scp.put(file, FOLDER)
    print(" -> Uploaded")

    command = f"chmod 775 {FOLDER}/{file}"
    output = ssh.exec_command(command=command)
    # print(output)

    scp.close()
    # ssh.close()
        

if __name__ == "__main__":

    upload_file("C:/Users/LUGGGI/Downloads/invoice.pdf")
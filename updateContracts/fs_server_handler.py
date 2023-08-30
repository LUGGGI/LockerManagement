'''
This Module handles the transfer of files to the fs server

Author: Lukas Beck
Date: 11.08.2023
'''

from paramiko import SSHClient
from scp import SCPClient

SERVER = "ivie.ei.faveve.uni-stuttgart.de"
FOLDER = "/import/fs-ei/service/schliessfaecher/Locker/ContractsNew"
***REMOVED***

def upload_file(file: str):
    '''Uploads file to server with correct permissions.
    
    :file: file to upload
    '''
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=SERVER, username=USER)

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
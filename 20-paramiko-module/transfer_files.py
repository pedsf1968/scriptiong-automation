# SFTP file transfer
# Need to install paramiko with pip
# Need to install ssh on remote server
import sys
import getpass
import paramiko

# get login
if len(sys.argv)>2:
    conn_login=sys.argv[2]
else:
    conn_login='devops'

# get hostname ip
if len(sys.argv)>1:
    conn_ip=sys.argv[1]
else:
    conn_ip='10.1.88.41'

conn_password=getpass.getpass("Enter the password: ")
conn_home='/home/'+conn_login

def connectToRemote(hostname,login,password,port=22):
    ssh_id = paramiko.SSHClient()
    # To avoid host SSH key control
    ssh_id.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_id.connect(hostname=hostname,username=login,password=password,port=port)
    return ssh_id

def disconnectToRemote(ssh_id):
    ssh_id.close()
    return None

def execCommandToRemote(ssh_id,command):
    stdin,stdout,stderr=ssh_id.exec_command(command)
    command_output=stdout.readlines()
    for each_lines in command_output:
        print(each_lines)
    return None

def sftpConnectToRemote(ssh_id):
    return ssh_id.open_sftp()

def sftpDisconnectToRemote(ssh_id):
    ssh_id.close()
    return None

def testSftpPut(sftp_id):
    # Put file on remote HOME
    file_src="transfer_files.py"
    remote_dest=conn_home+"/demo.txt"
    print(f"\nPut file {file_src} on remote host in {remote_dest}")
    sftp_id.put(file_src,remote_dest)
    return None

def testSftpget(sftp_id):
    # get file
    remote_dest=conn_home+"/demo.txt"
    print(f"\nGet file {remote_dest} on remote and copy on local directory")
    sftp_id.get(remote_dest,'paramiko_downloaded_file.txt')
    return None

def testSftpChdir(sftp_id):
    # Go to home directory
    print(f"\nGet remote location and change to {conn_home}")
    print(sftp_id.getcwd())
    sftp_id.chdir(conn_home)
    print(sftp_id.getcwd())
    return None

def main():
    # SSH conbnection
    ssh_id=connectToRemote(conn_ip,conn_login,conn_password)

    # execute commands on remote
    execCommandToRemote(ssh_id,'free -m')
    execCommandToRemote(ssh_id,'whoami')
    disconnectToRemote(ssh_id)

    # SFTP connection
    sftp_id=sftpConnectToRemote(ssh_id)
    # file transfert
    testSftpPut(sftp_id)
    testSftpChdir(sftp_id)
    testSftpget(sftp_id)

    # disconnect
    sftpDisconnectToRemote(sftp_id)
    disconnectToRemote(ssh_id)

if __name__=='__main__':
    main()
#!/usr/bin/python3
import sys
import getpass
import paramiko

# get login
if len(sys.argv)>2:
    conn_login=sys.argv[2]
else:
    conn_login='isa'

# get hostname ip
if len(sys.argv)>1:
    conn_ip=sys.argv[1]
else:
    conn_ip='10.1.88.41'

conn_password=getpass.getpass("Enter the password: ")
conn_home='/home/'+conn_login
#conn_key_filename='C:\\Users\\Paul-Emmanuel\\.ssh\\devops_rsa'
conn_key_filename='/home/isa/.ssh/id_ed25519'

def connectToRemote(hostname,login,password,port=22):
    ssh_id = paramiko.SSHClient()
    # To avoid host SSH key control
    ssh_id.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_id.connect(hostname=hostname,username=login,password=password,port=port)
    return ssh_id

def connectToRemoteWithKey(hostname,login,key_filename,port=22):
    ssh_id = paramiko.SSHClient()
    # To avoid host SSH key control
    ssh_id.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_id.connect(hostname=hostname,username=login,key_filename=key_filename,port=port)
    return ssh_id


def disconnectToRemote(ssh_id):
    ssh_id.close()
    return None

def execCommandToRemote(ssh_id,command):
    stdin,stdout,stderr=ssh_id.exec_command(command)
    command_output=stdout.readlines()
    print("The output is: ")
    print(stdout.readlines())
    print("THe error is: ")
    print(stderr.readlines())

    for each_lines in command_output:
        print(each_lines)
    return None


def main():
    # SSH conbnection
    #ssh_id=connectToRemote(conn_ip,conn_login,conn_password)
    ssh_id=connectToRemoteWithKey(conn_ip,conn_login,conn_key_filename)

    execCommandToRemote(ssh_id,'whoami')
    execCommandToRemote(ssh_id,'uptime')
    execCommandToRemote(ssh_id,'free -m')

    # disconnect
    disconnectToRemote(ssh_id)

if __name__=='__main__':
    main()
#!/usr/local/bin/python3
import shutil
  

def main():
    src="D:\\DATA-DEV\\python\\scripting-automation\\20-paramiko-module\\transfer_files.py"
    dest="D:\\DATA-DEV\\python\\scripting-automation\\21-shutil-module\\transfer_files.py.bak"

    #copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'

    #copyfile-->copy --> copy2
    # Dont preserve rights and date
    #shutil.copyfile(src,dest)

    # same permissions for src and dest
    #shutil.copy(src,dest)   
    
    # same meta data for dest as well (timestamp and rights)
    #shutil.copy2(src,dest)   
    
    # Copy only the rights of src to dest file
    #shutil.copymode(src,dest)

    # Copy only timestamp of src to dest file
    #shutil.copystat(src,dest)

    # Copy only content 
    #f1=open('xyz.txt','r')
    #f2=open('pqr.txt','w')
    #shutil.copyfileobj(f1,f2)

    # Copy all tree 
    # src="D:\\DATA-DEV\\python\\scripting-automation"
    # shutil.copytree(src,'D:\\DATA-DEV\\tmp')

    # Remove tree
    #shutil.rmtree('D:\\DATA-DEV\\tmp')

    return None

if __name__=='__main__':
    main()
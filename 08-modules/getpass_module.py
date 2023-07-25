# Read password
import getpass

'''print(dir(getpass))'''
db_password_prompt="Enter the database password: "
db_password=getpass.getpass(prompt=db_password_prompt)
print(f"The entered password is {db_password}")

# getuser() check enviromnment variables LOGNAME, USER, LNAME and USERNAME
print(f"{getpass.getuser()}")





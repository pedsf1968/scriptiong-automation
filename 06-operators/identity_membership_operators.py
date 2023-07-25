# Identity and membership operators

# Identity operators is/is not
value=4
print(f"\nType of {value}: {type(value)}")
print(f"{value} is integer: {type(value) is int}")
print(f"{value} is not string: {type(value) is not str}")

value=3.8
print(f"\nType of {value}: {type(value)}")
print(f"{value} is float: {type(value) is float}")
print(f"{value} is not string: {type(value) is not str}")

value="Hello"
print(f"\nType of {value}: {type(value)}")
print(f"{value} is string: {type(value) is str}")
print(f"{value} is not integer: {type(value) is not int}")

# Membership operators in / not in
value=4
my_list=[1,2,3,7,5,6,7,8,9]
print(f"\n{value} is member of {my_list}: {value in my_list}")
value=7
print(f"\n{value} is member of {my_list}: {value in my_list}")

valid_java=['1.6','1.7','1.8','1.9']
host_java='1.5'
print(f"\nHost {host_java} and valid java {valid_java}")
if host_java in valid_java:
    print("Host has compatible java version")
else:
    print("Host is not compatible with java version")

db_users=['db_admin','db_conf','db_install']
random_user="Martin"

print(f"\nUser {random_user} not in {db_users}")
if random_user not in db_users:
    print("User not allowed")
else:
    print("User is allowed to start and stop db")
    
import sys

nb_args=len(sys.argv)

# Get the action 
if nb_args>2:
    usr_action=sys.argv[2]
else:
    usr_action=input("Enter your action on the string l/lower, u/upper or t/title: ")

# Get the string
if nb_args>1:
    usr_string=sys.argv[1]
else:
    usr_string=input("Enter your string: ")

if usr_action in ["l","lower"]:
    print(usr_string.lower())
elif usr_action in ["u","upper"]:
    print(usr_string.upper())
elif usr_action in ["t","title"]:
    print(usr_string.title())
else:
    print("Enter valid option lower upper or title")

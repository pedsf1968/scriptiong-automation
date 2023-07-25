usr_string=input("Enter your string: ")
usr_action=input("Enter your action on the string l/lower, u/upper or t/title: ")

if usr_action in ["l","lower"]:
    print(usr_string.lower())
elif usr_action in ["u","upper"]:
    print(usr_string.upper())
elif usr_action in ["t","title"]:
    print(usr_string.title())
else:
    print("Enter valid option lower upper or title")

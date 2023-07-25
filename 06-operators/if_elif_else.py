usr_str=input("Enter your string: ")
usr_cnf=input("Do you want to convert your given string in title format? say yes or no: ")

yes_answer=['y','Y','yes','YES']
no_answer=['n','N','no','NO']

if usr_cnf in yes_answer:
    print(usr_str.title())
elif usr_cnf in no_answer:
    print(usr_str)
else:
    print("Output other string")

a=eval(input("Enter first number: "))
b=eval(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} and {b} are equal")


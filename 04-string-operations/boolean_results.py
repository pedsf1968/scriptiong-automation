# startswith(VALUE): return True or False if the string is starting with VALUE
# islower(): return True if the string is in lower case
# isupper(): return True if the string is in upper case
# istitle(): return True if the string is a title
# isspace(): return True if the string is spaces
# isalpha(): return True if the string is letters
# isnumeric(): return True if the string is number
# help(VALUE): print help about VALUE

# String start testing
my_str="Python"
my_str_start='P'
print(f"The string {my_str} is it starting with {my_str_start}? : {my_str.startswith(my_str_start)}")
my_str_start='Pyt'
print(f"The string {my_str} is it starting with {my_str_start}? : {my_str.startswith(my_str_start)}")
my_str_start='thon'
print(f"The string {my_str} is it starting with {my_str_start}? : {my_str.startswith(my_str_start)}")

# String case testing
my_str="Python"
print(f"The string {my_str} is lower? : {my_str.islower()}")
my_str=my_str.lower()
print(f"The string {my_str} is lower? : {my_str.islower()}")
my_str="Python"
print(f"The string {my_str} is upper? : {my_str.isupper()}")
my_str=my_str.upper()
print(f"The string {my_str} is upper? : {my_str.isupper()}")
my_str="Python"
print(f"The string {my_str} is title? : {my_str.istitle()}")
my_str=my_str.upper()
print(f"The string {my_str} is title? : {my_str.istitle()}")
my_str="Python"
print(f"The string {my_str} is space? : {my_str.isspace()}")
my_str="  "
print(f"The string {my_str} is space? : {my_str.isspace()}")
my_str="Python"
print(f"The string {my_str} is alphanumeric? : {my_str.isalpha()}")
my_str="Python scripting"
print(f"The string {my_str} is alphanumeric? : {my_str.isalpha()}")
my_str="Python"
print(f"The string {my_str} is numeric? : {my_str.isnumeric()}")
my_str="132"
print(f"The string {my_str} is numeric? : {my_str.isnumeric()}")
my_str="132.456"
print(f"The string {my_str} is numeric? : {my_str.isnumeric()}")
# Print string help
help(str)
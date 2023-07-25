
string_number=input("Enter a numbers: ")

list_number=string_number.split(' ')

for number in list_number:
    rem=int(number)%2
    if rem==0:
        print(f"{number} is event")
    else:
        print(f"{number} is odd")





usr_number=eval(input("Enter a number: "))
number_range=[0,1,2,3,4,5,6,7,8,9]

# Very bad writing because all tests are done
'''
if usr_number==0:
    print("zero")
if usr_number==1:
    print("one")
if usr_number==2:
    print("two")
if usr_number==3:
    print("three")
if usr_number==4:
    print("four")
if usr_number==5:
    print("five")
if usr_number==6:
    print("six")
if usr_number==7:
    print("seven")
if usr_number==8:
    print("eight")
if usr_number==9:
    print("nane")
if usr_number not in number_range:
    print(f"Number {usr_number} out of range {number_range}")
'''

# use elif to limit number of testing conditions
'''
if usr_number==0:
    print("zero")
elif usr_number==1:
    print("one")
elif usr_number==2:
    print("two")
elif usr_number==3:
    print("three")
elif usr_number==4:
    print("four")
elif usr_number==5:
    print("five")
elif usr_number==6:
    print("six")
elif usr_number==7:
    print("seven")
elif usr_number==8:
    print("eight")
elif usr_number==9:
    print("nane")
elif usr_number not in number_range:
    print(f"Number {usr_number} out of range {number_range}")
'''
# better use dictionnary
number_name={0: 'zero',1: 'one',2: 'two',3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'height',9: 'nine'}
number_range=number_name.keys()

if usr_number not in number_range:
    print(f"Number {usr_number} out of range {number_range}")
else:
    print(f"Your number is: {number_name.get(usr_number)}")

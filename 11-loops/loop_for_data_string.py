my_string="Working with for loop"

'''
for each_char in my_string:
    print(each_char)
'''
# print(" ".join(my_string))
# print("\n".join(my_string))

'''
my_list=[1,2,3,4,5]
# Print all values of the list
for each_value in my_list:
    print(each_value)
'''
# With list of tuple
my_list=[(1,2),(7,6),(9,4)]
print(f"Print all items of the list {my_list}")
for each_item in my_list:
    print(each_item)

for f,s in my_list:
    print(f,s)

print(f"Print first part of items of the list {my_list}")
for f,s in my_list:
    print(f)

print(f"Print second part of items of the list {my_list}")
for f,s in my_list:
    print(s)

# With list of list
my_list=[[1,2],[7,6],[9,4]]
print(f"Print all items of the list {my_list}")
for each_item in my_list:
    print(each_item)

for f,s in my_list:
    print(f,s)

# with dictionnaries
my_dict={'a':1,'b':2,'c':3}
print(f"Print all keys of the dictionnary {my_dict}")
for each_item in my_dict:
    print(each_item)

print(f"Print all keys of a dictionnary {my_dict}")
for each_item in my_dict.keys():
    print(each_item)

print(f"Print all values of a dictionnary {my_dict}")
for each_item in my_dict.values():
    print(each_item)

print(f"Print all items of a dictionnary {my_dict}")
for each_item in my_dict.items():
    print(each_item)

print(f"Print keys and values of a dictionnary {my_dict}")
for key,value in my_dict.items():
    print(key,value)

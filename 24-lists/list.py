# index(VALUE): give the index of the VALUE
# index(VALUE,START): give the index of the VALUE after index START
# count(VALUE): count number of occurence of VALUE
# clear(): empty the list
# copy(): create a new list with the copy of other
# id(OBJECT): return the ID
# append(VALUE): append VALUE to the list
# insert(POSITION,VALUE): insert VALUE at POSITION
# extend(LIST): add LIST to other list
# remove(VALUE): remove VALUE from list
# pop(): remove last value from list
# reverse(): reverse the list
# sort(): sort the list
# List usage

my_list=[]
print(f"All values of empty list: {my_list}, boolean is {bool(my_list)}")
my_list=[3,4,5,'python','devops',6.7]
print(f"All values of my list: {my_list}, boolean is {bool(my_list)}")


# Access list elements
my_index=0
print(f"\nValues of my list at index [{my_index}]: {my_list[my_index]}")
my_index=3
print(f"Values of my list at index [{my_index}]: {my_list[my_index]}")
my_index=-1
print(f"Values of my list at index [{my_index}]: {my_list[my_index]}")
my_index=-2
print(f"Values of my list at index [{my_index}]: {my_list[my_index]}")
my_index1=3
my_index2=0
print(f"\nValues of my list at index [{my_index1}]: {my_list[my_index1]}")
print(f"Values of my list at index [{my_index1}][{my_index2}]: {my_list[my_index1][my_index2]}")
my_index2=1
print(f"Values of my list at index [{my_index1}][{my_index2}]: {my_list[my_index1][my_index2]}")
my_index2=2
print(f"Values of my list at index [{my_index1}][{my_index2}]: {my_list[my_index1][my_index2]}")

# Get part of list
print(f"\nAll values of my list: {my_list}")
print(f"All values of my list: {my_list[:]}")
my_index1=1
print(f"Values starting at index [{my_index1}]: {my_list[my_index1:]}")
my_index1=0
print(f"Values starting at index [{my_index1}]: {my_list[my_index1:]}")
my_index1=1
my_nb_elements=3
print(f"{my_nb_elements} elements of the list starting at index [{my_index1}]: {my_list[my_index1:my_nb_elements]}")
my_index1=0
my_nb_elements=2
print(f"{my_nb_elements} elements of the list starting at index [{my_index1}]: {my_list[my_index1:my_nb_elements]}")

# Modification of values
print(f"\nAll values of my list: {my_list}")
my_list[0]=45
print(f"Modified list: {my_list}")

print(dir(my_list))

# Get first index of value
my_list=[3,5,2,7,3,8,9]
my_value=5
print(f"\n{my_list} the value {my_value} is at index: [{my_list.index(my_value)}]")
my_value=3
my_index=1
print(f"\n{my_list} the value {my_value} after index {my_index} are at index: [{my_list.index(my_value, my_index)}]")

# count values in list
my_list=[3,5,2,7,3,8,9]
my_value=3
print(f"\n{my_list} the value {my_value} apear in: {my_list.count(my_value)} location(s)")

# Empty the list
print(f"\n{my_list}")
my_list.clear()
print(f"After clear the list is : {my_list}")

# Copy list
my_list=[3,5,2,7,3,8,9]
my_new_list1=my_list
my_new_list2=my_list.copy()
print(f"My first list: {my_list} with ID: {id(my_list)}")
print(f"My list1: {my_new_list1} with ID: {id(my_new_list1)}")
print(f"My list2 the copy: {my_new_list2} with ID: {id(my_new_list2)}")
my_list[1]=9
print(f"My first list after modification: {my_list} with ID: {id(my_list)}")
print(f"My list1 affected: {my_new_list1} with ID: {id(my_new_list1)}")
print(f"My list2 the copy not affected: {my_new_list2} with ID: {id(my_new_list2)}")

# Append to list
my_list=[3,5,2,7,3,8,9]
print(f"My list {my_list} before append")
my_value=78
my_list.append(my_value)
print(f"My list {my_list} after append {my_value}")

# Insert to list
my_value=37
my_position=1
my_list.insert(my_position,my_value)
print(f"My list {my_list} after insert {my_value} at position {my_position}")

# Extend list with other
my_list1=[1,2,3,4,5]
my_list2=[6,7,8,9]
print(f"\nMy list {my_list1} before extend")
my_list1.extend(my_list2)
print(f"My list {my_list1} after extend with {my_list2}")

# Remove values
my_list=[1,2,3,4,5,6,7,8,9]
my_value=6
print(f"\nMy list {my_list} before remove {my_value}")
my_list.remove(my_value)
print(f"My list {my_list} after remove {my_value}")

# Remove last value
my_list=[1,2,3,4,5,6,7,8,9]
print(f"\nMy list {my_list} before remove last value")
my_list.pop()
print(f"My list {my_list} after remove last value")
my_list.pop()
print(f"My list {my_list} after remove last value")

# Reverse list
my_list=[1,2,3,4,5,6,7,8,9]
print(f"\nMy list {my_list} before reverse")
my_list.reverse()
print(f"My list {my_list} after reverse")

# Sort list
my_list=[3,5,2,7,3,8,9]
print(f"\nMy list {my_list} before sort")
my_list.sort()
print(f"My list {my_list} after sort")
my_list=[3,5,2,7,3,8,9]
print(f"\nMy list {my_list} before sort")
my_list.sort(reverse=True)
print(f"My list {my_list} after sort in reverse")

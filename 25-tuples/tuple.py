
my_tuple=()
print(f"Empty tuple: {my_tuple} contain values? {bool(my_tuple)}")
my_tuple=(1,2,3,4)
print(f"Tuple: {my_tuple} contain values? {bool(my_tuple)}")

print(f"Type of tuple:{type(my_tuple)}")
print(f"Operation with tuple:\n{dir(my_tuple)}")

# Get values from tuple
my_tuple=(1,2,[3,4,5],6,7,8,9)
print(f"All tuple {my_tuple}")
my_index=0
print(f"Tuple {my_tuple} value at index [{my_index}]: {my_tuple[my_index]}")
my_index=2
print(f"Tuple {my_tuple} value at index [{my_index}]: {my_tuple[my_index]}")
my_index=2
my_sub_element=2
print(f"Tuple {my_tuple} value at index [{my_index}] and sub element [{my_sub_element}]: {my_tuple[my_index][my_sub_element]}")

# Count values
my_tuple=(1,2,3,4,5,6,3,8,9)
my_value=3
print(f"Count how many {my_value} in tuple {my_tuple} is: {my_tuple.count(my_value)}")

# Get index
my_tuple=(1,2,3,4,5,6,3,8,9)
my_value=3
print(f"Where is {my_value} in tuple {my_tuple} is at index [{my_tuple.index(my_value)}]")
my_start=4
print(f"Where is next {my_value} after position [{my_start}] in tuple {my_tuple} is at index [{my_tuple.index(my_value,my_start)}]")

# Length
my_tuple=(1,2,3,4,75,6,43,8,9)
my_index=3
my_nb_values=4
my_last_index=6
print(f"Sub-tuple of first {my_nb_values} values of {my_tuple} is {my_tuple[:my_nb_values]}")
print(f"Sub-tuple starting at index [{my_index}] in {my_tuple} is {my_tuple[my_index:]}")
print(f"Sub-tuple starting at index [{my_index}] and ending before index [{my_last_index}] in {my_tuple} is {my_tuple[my_index:my_last_index]}")

my_str="python is easy and it is popular language"
my_str_cont="is"
print(f"Count string {my_str_cont} in {my_str}: {my_str.count(my_str_cont)}")
my_str_cont="p"
print(f"Count string {my_str_cont} in {my_str}: {my_str.count(my_str_cont)}")
my_str_cont="t"
print(f"Count string {my_str_cont} in {my_str}: {my_str.count(my_str_cont)}")
my_str_cont="a"
print(f"Count string {my_str_cont} in {my_str}: {my_str.count(my_str_cont)}")
my_str_cont="easy"
print(f"Count string {my_str_cont} in {my_str}: {my_str.count(my_str_cont)}")

# Use index 
my_str_index="p"
print(f"Get index of {my_str_index} in {my_str}: {my_str.index(my_str_index)}")
my_index_after=1
print(f"Get index of {my_str_index} after index {my_index_after} in {my_str}: {my_str.index(my_str_index,my_index_after)}")
my_index_after=26
print(f"Get index of {my_str_index} after index {my_index_after} in {my_str}: {my_str.index(my_str_index,my_index_after)}")
my_str_index="is"
print(f"Get index of {my_str_index} in {my_str}: {my_str.index(my_str_index)}")

# Use find that return -1 if not find and 0 if a string is found
my_str_find="p"
print(f"Get index of {my_str_find} in {my_str}: {my_str.find(my_str_find)}")
my_find_after=2
print(f"Get index of {my_str_find} after index {my_find_after} in {my_str}: {my_str.find(my_str_find,my_find_after)}")
my_find_after=26
print(f"Get index of {my_str_find} after index {my_find_after} in {my_str}: {my_str.find(my_str_find,my_find_after)}")
my_find_after=28
print(f"Get index of {my_str_find} after index {my_find_after} in {my_str}: {my_str.find(my_str_find,my_find_after)}")
my_str_find="z"
print(f"Get index of {my_str_find} in {my_str}: {my_str.find(my_str_find)}")
my_str_find="popular"
print(f"Get index of {my_str_find} in {my_str}: {my_str.find(my_str_find)}")

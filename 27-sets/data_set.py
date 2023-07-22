# Set of datas
#
# set(LIST): convert LIST in set
# intersection(SET): intersection of 2 sets
# union(SET): union of 2 sets

my_set={4,5,7,6,2,7,6}

print(f"Print without duplicate values: {my_set}")
print(f"My set {my_set} containt values {bool(my_set)}")
print(f"My empty set containt values {bool({})}")
print(f"The data type is {type(my_set)}")

my_list=[4,5,9,7]
my_set_from_list=set(my_list)
print(f"Convert list {my_list} in set {my_set_from_list}")
my_list=[4,5,9,7,9,4,5]
my_set_from_list=set(my_list)
print(f"Convert list {my_list} in set {my_set_from_list} and remove duplicates values")

print(f"Opérations on Set:\n{dir(set)}")

# Union and intersection of two sets
my_set1={4,9,7,6}
my_set2={3,2,7,6}
print(f"{my_set1} union {my_set2} is: {my_set1.union(my_set2)}")
print(f"{my_set1} inter {my_set2} is: {my_set1.intersection(my_set2)}")

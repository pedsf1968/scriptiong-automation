# Dictionnaries
#
# keys(): print all keys of a dictionnary
# values(): print all values of a dictionnary
# items(): print dictionary items 
# copy(): make a copy 
# pop(KEY): remove item with KEY
# popitem(): remove last item
# setdefault(): set item if not define

my_dict={}
print(f"\nEmpty dictionary {my_dict} contain values? {bool(my_dict)}")

my_dict={
    'fuit':'apple',
    'animal':'dog',
    'colour':'purple',
    1:'one',
    'two':2
}
print(f"\nThe dictionary {my_dict} contain values? {bool(my_dict)}")
print(f"The dictionary length is: {len(my_dict)}")

# Access values
my_key='animal'
print(f"\nIn the dictionary {my_dict} the value at key {my_key} is {my_dict[my_key]}")
my_key=1
print(f"In the dictionary {my_dict} the value at key {my_key} is {my_dict.get(my_key)}")
my_key='1'
print(f"In the dictionary {my_dict} the value at key {my_key} is {my_dict.get(my_key)}")
my_key='sense'
print(f"In the dictionary {my_dict} the value at key {my_key} is {my_dict.get(my_key)}")

# Operations on dictionnaries
print(f"\nOperations on dictionary are:\n {dir(my_dict)}")

# Add key/value or change value
my_key='three'
my_value='33'
print(f"\nDictionary {my_dict} before adding value {my_value} with the key {my_key}")
my_dict[my_key]=my_value
print(f"Dictionary {my_dict} after adding value")
my_value='44'
my_dict[my_key]=my_value
print(f"Dictionary {my_dict} after changing value")

# Display keys and values
print(f"\nPrint all keys of the dictionary {my_dict}: {my_dict.keys()}")
print(f"Print all values of the dictionary {my_dict}: {my_dict.values()}")
print(f"Print dictionary items {my_dict}: {my_dict.items()}")

# Copy dictionnary
my_copy=my_dict.copy()
print(f"\nPrint dictionary {my_copy} of ID: {id(my_dict)}")
print(f"Print copy of dictionary {my_copy} of ID: {id(my_copy)}")

# Update a dictionnary with another
my_new_dict={
    'four':'4'
}
print(f"\nDictionary {my_dict} before update with other {my_new_dict}")
my_dict.update(my_new_dict)
print(f"Dictionary {my_dict} after update")

# Remove last item
my_key='four'
my_dict.pop(my_key)
print(f"Dictionary {my_dict} after pop {my_key}")
my_removed_item=my_dict.popitem()
print(f"Dictionary {my_dict} after pop last item {my_removed_item}")

# Create dictionnary from keys
keys=['a','e','i','o','u']
new_dict=dict.fromkeys(keys)
print(f"Create new empty dictionnary with keys: {keys}:\n{new_dict}")
new_dict['e']='letter e'
print(f"Set value in dictionnary {new_dict}")

# Set default value
new_dict={}
print(f"\nNew empty dictionnary {new_dict}")
my_key='e'
my_value='elephant'
new_dict.setdefault(my_key,my_value)
print(f"Set value {my_value} for the key {my_key} if not present in dictionnary {new_dict}")
my_value='iguane'
new_dict.setdefault(my_key,my_value)
print(f"Set value {my_value} for the key {my_key} if not present in dictionnary {new_dict}")




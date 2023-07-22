# lower(): change string to lower case
# upper(): change string to upper case
# swapcase(): swap case of a string
# title(): change first char to upper case
# capitalize(): change first char to upper of all words
# casefold(): change all to lower case but more agressive
# dir(VALUE): give all fonctions can be apply to a VALUE

# Lower and upper case
my_string="Python scripting tutorial"
my_string_lower=my_string.lower()
my_string_upper=my_string.upper()

print(f'Lower case of {my_string}: {my_string.lower()}')
print(f'Upper case of {my_string}: {my_string.upper()}')
print(f'Swap case of {my_string}: {my_string.swapcase()}')
print(f'Title case of {my_string}: {my_string.title()}')
print(f'Capitalize case of {my_string_upper}: {my_string_upper.capitalize()}')
print(f'Casefold case of {my_string_upper}: {my_string_upper.casefold()}')

# The string is not modified
print(my_string)

my_string_lower=my_string.lower()
print(my_string_lower)
print(f'Operation available on string {dir(my_string)}')

'''
'__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
'''
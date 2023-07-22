# Use single, double and triple double quotes
my_name='Zola'
my_new_name="Python Developer"
my_info="""
I started my carrier as a system validator
and 
moved into devops
"""
print(f'my name is: {my_name}\nmy new name is: {my_new_name}\nmy info is: {my_info}')

# String empty is always False
my_str=""
my_new_str=" "
print(f'my_str: {bool(my_str)}\nmy_new_str: {bool(my_new_str)}')

# Using index to read characters of a string from 0 to N
my_fav_scripting="Python scripting"
print(f'{my_fav_scripting}')
print(f'the first character is: {my_fav_scripting[0]}')
print(f'the 4 character is: {my_fav_scripting[5]}')
print(f'the last is {my_fav_scripting[-1]}')
print(f'the first 3 characters is: {my_fav_scripting[0:3]}')
print(f'the first 4 characters is: {my_fav_scripting[:4]}')
my_str_len=len(my_fav_scripting)
print(f'the string length is: {my_str_len}')
print(f'{my_fav_scripting[-my_str_len:-5]}')
print(f'{my_fav_scripting[-my_str_len:-1]}')

# Concatenate
my_str1="Python"
my_str2="scripting"
my_space=" "
my_str3=my_str1+" "+my_str2
print(f'{my_str3}')
my_space=" "
my_str4=my_str1+my_space+my_str2
print(f'{my_str4}')



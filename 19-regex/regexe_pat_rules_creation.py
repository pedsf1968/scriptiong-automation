# Regular expression uses
# re.findall(PATTERN,STRING): find PATTERN in STRING

import re
my_text="This . is a python and it is easy to learn and it is popular one for dev and automation"

my_pattern= 'i[ston]' 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind is,it,io and in in the text")
print(re.findall(my_pattern,my_text))
print(f"Number of strings found: {len(re.findall(my_pattern,my_text))}")

my_text="This . is a python xay it is xcy easy to xqy learn xfy and it is popular one for dev xqy and automationxqy"
my_pattern="x[abcdeflmnopq]y" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind xay to xfy and xly to xqy in the text")
print(re.findall(my_pattern,my_text))
my_pattern="x[a-fl-q]y"
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind xay to xfy and xly to xqy in the text")
print(re.findall(my_pattern,my_text))

my_text="This . is a pyth1on xay it is 2 6 easy to xqy 7 learn xfy and it 6 is popular one 8 for dev xq3y and aut756omationxqy"
my_pattern="[0-9]" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all numbers in the text")
print(re.findall(my_pattern,my_text))
my_pattern="\d" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all numbers in the text")
print(re.findall(my_pattern,my_text))


my_text="This . is a Pyth1on xay it is 2 6 easy to xqy 7 learn xfy and it 6 is popular one 8 for dev xq3y and aut756omationxqy"
my_pattern="[A-Z]" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all upper case letters in the text")
print(re.findall(my_pattern,my_text))

my_text="This . is a Pyth1on xay it is 2 6 easy to xqy 7_+*=$* learn xfy and it 6 is popular one 8 for dev xq3y and aut756omationxqy"
my_pattern="\w" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind any single letter, digit or underscore in the text")
print(re.findall(my_pattern,my_text))

my_text="This . is a python and it is easy to learn and it is popular one for dev a5d automation azd"
my_pattern="a\wd" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all 3 letters words starting with a and ending with d in the text")
print(re.findall(my_pattern,my_text))

my_text="This . is a python and it is easy to learn and it is popular one for dev a5d automation azd"
my_pattern="\w\w\w" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all 3 chars strings in the text")
print(re.findall(my_pattern,my_text))
my_pattern="..." 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all 3 chars strings in the text")
print(re.findall(my_pattern,my_text))


#      =""
'''
my_pattern='\.'
print(re.findall(my_pattern,my_text))
'''
my_text="This is a ip address of my db1 server: 255.255.255.255  2456234512341234"
my_pattern="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all IP address in the text")
print(re.findall(my_pattern,my_text))

my_text="This is python @ 345 _ - ("
my_pattern="\w" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind any single letter, digit or underscore in the text")
print(re.findall(my_pattern,my_text))
my_pattern="\W" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind any character that are not in \w in the text")
print(re.findall(my_pattern,my_text))
my_pattern="." 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind any char and spaces in the text")
print(re.findall(my_pattern,my_text))

my_text="456 90 this is about deciaml re98gex"
my_pattern="\d\d" 
print(f"\nTEXT: {my_text}\nPATTERN: {my_pattern}\nFind all numbers of 2 digits in the text")
print(re.findall(my_pattern,my_text))

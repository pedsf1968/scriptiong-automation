import re

my_str="This is python and we are having python2 and python3 version"
my_pat=r'\bpython[23]?\b'


print(f"\nFind first string with pattern {my_pat} in text: {my_str}")
print(re.search(my_pat,my_str))
print(f"How many string match: {len(re.findall(my_pat,my_str))}")

print(f"\nFind all strings with pattern {my_pat} in text: {my_str}")
print(re.findall(my_pat,my_str))

print("\n Find all objects and informations")
for each_ob in re.finditer(my_pat,my_str):
	print(f'The match is: {each_ob.group()} starting index: {each_ob.start()}, ending index {each_ob.end()-1}')
# Use pattern object
# re.compile(pattern, flags=0)

import re
my_str="This is about python. Python is easy to learn  and we have two major versions: python2 and python3 "
my_pat=r'\bPython[23]?\b'

help(re.compile)

print(my_str)
print(f"Find all string matching {my_pat}\n{re.findall(my_pat,my_str)}")
print(f"\nFind first object matching {my_pat}\n{re.search(my_pat,my_str)}")
print(f"\nFind all string matching {my_pat} ignore case\n{re.findall(my_pat,my_str,flags=re.I)}")
print(f"\nFind first object matching {my_pat}  ignore case\n{re.search(my_pat,my_str,flags=re.I)}")

print(f"\nSplit using {my_pat}\n{re.split(my_pat,my_str)}")

# Create pattern object to reuse it
pat_ob=re.compile(my_pat,flags=re.I)
print(f"\nMy pattern object with {my_pat} and ignoring case: {pat_ob}")
print(f"\nSeach using my pattern object\n{pat_ob.search(my_str)}")
print(f"\nFind using my pattern object\n{pat_ob.findall(my_str)}")


# It's the same re.findall(my_pat,my_str)  <===> re.complie(my_pat).findall(my_str)


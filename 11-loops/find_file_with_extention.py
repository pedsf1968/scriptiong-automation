# Display files with specified extention

import os
import sys

my_path=input("Enter your path: ")
# Test if path is file or directory
if not os.path.exists(my_path):
    print("The path is not valid!")
    sys.exit(0)
elif os.path.isfile(my_path):
    print("The path is a file. Enter only directory for the path!")
    sys.exit(0)

my_extention=input("Enter the extention .py/.sh/.log/.txt: ")
my_files=os.listdir(my_path)
# Test if there are files
if len(my_files)==0:
    print(f"There is no files in the path!")
    sys.exit(0)

file_found=[]

for file in my_files:
    if file.endswith(my_extention):
        file_found.append(file)

if len(file_found)==0:
    print(f"There is no files with the extension {my_extention} in the path!")
else:
    print(f"Files with the {my_extention} in {my_path}:\n{file_found}")



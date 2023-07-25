import os
import sys

path=input("Enter your directory path: ")

# Tests if the entered path exist
if os.path.exists(path):
    file_list=os.listdir(path)
else:
    print("Provide a valid path!")
    sys.exit(0)

for file in file_list:
    absolut_path=os.path.join(path,file)
    if os.path.isfile(absolut_path):
        print(f"FILE: {absolut_path}")
    else:
        print(f"DIRECTORY: {absolut_path}")
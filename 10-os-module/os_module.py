# operations with os module
# sep: return the curent separator
# getcwd(): return curent working directory
# chdir(PATH): change curent working directory to PATH
# listdir(PATH): list content of PATH directory or curent
# mkdir(PATH): create recursive directory PATH
# makedirs(PATH): create recursive directory PATH
# rmdir(PATH): remove recursive directory PATH
# removedirs(PATH): remove recursive directory PATH
# environ: Return environment

import os


# Getint Os separator / Linux \ windows
os_separator=os.sep
print(f"The OS separator is: {os_separator}")

# Get curent directory and change directory
new_path="c:"
old_path=os.getcwd()
print(f"The curent working directory is: {os.getcwd()} changing to {new_path}")
os.chdir(new_path)
print(f"The curent working directory is: {os.getcwd()}")
os.chdir(old_path)
print(f"The curent working directory is: {os.getcwd()}")

# Display the content of directory
print(f"\nCurrent directory content {os.listdir()}")
print(f"New directory content {os.listdir(new_path)}")

# Create directory mkdir/makedir and delete directory rmdir removedir
new_dir="new-dir"
print(f"\nCurrent directory content {os.listdir()} before creating {new_dir}")
os.mkdir(new_dir)
print(f"\nCurrent directory content {os.listdir()} after creation od {new_dir}")
os.rmdir(new_dir)
print(f"\nCurrent directory content {os.listdir()} after removing {new_dir}")

# Get environment
print(f"Environment : {os.environ}")

print(dir(os))




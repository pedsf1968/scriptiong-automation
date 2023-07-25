# operation with os.path
import os
path="D:\\DATA-DEV\python\\scripting-automation\\41-os-module\\os_path.py"

print(f"Separator {os.path.sep}")
print(f"\nPath is :{path}")
print(f"Basename is {os.path.basename(path)}")
print(f"Dirname is {os.path.dirname(path)}")

# join and split path without separator
path1=os.path.dirname(path)
path2=os.path.basename(path)
print(f"\nThe complete path of {path1} + {path2} is {os.path.join(path1,path2)}")
print(f"Split in dirname and basename {path}: {os.path.split(path)}")


print(f"\nIs {path} exist? {os.path.exists(path)}")

if os.path.isfile(path):
    print(f"{path} is a file")
else:
    print(f"{path} is a directory")
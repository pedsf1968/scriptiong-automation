import os

path="D:\\DATA-DEV\\python\\scripting-automation\\41-os-module"
print(list(os.walk(path)))
for r,d,f in os.walk(path):
    print(f"\nIn root {r}")
    if len(d)!=0:
        print(f"\tThe directories are")
        for each_dir in d:
            print(f"\t\t{each_dir}")
    else:
        print("\tno subdirectories")
    if len(f)!=0:
        print(f"\tThe files are")
        for each_file in f:
            print(f"\t\t{each_file}")
    else:
        print("\tno files")



import os
import platform

host_os=platform.system()

if host_os=="Windows":
    # Search all drives for windows
    root_paths = [ chr(x) + ":\\" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
else:
    # Only one path in Linux
    root_paths=["/"]

req_file=input("Enter your file name to search: ")

for path in root_paths:
    print(f"Search file {req_file} in {path}")
    for r,d,f in os.walk(path):
        for each_file in f:
            if each_file==req_file:
                print(os.path.join(r,each_file))
                exit(0)


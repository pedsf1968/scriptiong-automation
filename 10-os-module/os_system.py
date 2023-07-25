# Execute commands depending on os

import platform
import os

host_os=platform.system()

if host_os=="Windows":
    print(f"Clear screan : {os.system('cls')}")
    print("Windows system")
    print(f"Display local path : {os.system('dir')}")
else:
    print(f"Clear screan : {os.system('clear')}")
    print("Linux system")
    print(f"Display local path : {os.system('ls')}")
    print(f"Local path : {os.system('pwd')}")


result=os.system('datee')
print(f"Result of wrong command {result}")


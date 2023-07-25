# Read command line arguments
import sys

print(f"The script name is : {sys.argv[0]}")
nb_args=len(sys.argv)

if nb_args < 2:
    print("Command without arguments")
else:
    print(f"First argument is: {sys.argv[1]}")




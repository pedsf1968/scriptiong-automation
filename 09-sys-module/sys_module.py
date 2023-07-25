# sys module give informations about python system
import sys

'''print(dir(sys))'''

print(f"The Python version is {sys.version}")
print(f"The Pythonversion_info is {sys.version_info}")
print(f"\nThe modules are {sys.modules}")
print(f"\nThe python environement path are {sys.path}")

# Exit the Python script
exit_code=0
sys.exit(exit_code)

import platform

'''print(dir(platform))'''
print(f"The processor is {platform.processor()}")
print(f"The architecture is {platform.architecture()}")
print(f"The machine is {platform.machine()}")
print(f"The node is {platform.node()}")
print(f"\nThe system is {platform.system()}")
print(f"The release is {platform.release()}")
print(f"The platform is {platform.platform()}")
print(f"\nPython version is {platform.python_version()}")
print(f"Python version tuple is {platform.python_version_tuple()}")
print(f"\nThe uname is {platform.uname()}")

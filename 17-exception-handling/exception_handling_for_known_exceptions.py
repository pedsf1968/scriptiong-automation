# 1-NameError
# 2-TypeError
# 3-FileNotFoundError
# 4-ZeroDivisionError
# 5-ModuleNotFoundError

print("\nName Error exception")
try:
	print(a)
except NameError as e:
	print("Variable is not defined")
	print(e)

print("\nType Error exception")
try:
	print(4+"hi")
except TypeError as e:
	print("Adding number and string is not possible")
	print(e)

print("\nFileNotFound exception")
try:
	open('asdfas.txt')
except FileNotFoundError as e:
	print("File is not present to open it")
	print(e)

print("\nZeroDivisionError exception")
try:
	print(5/0)
except ZeroDivisionError as e:
	print("Division with zero is not possible")
	print(e)


print("\nModuleNotFoundError exception")
try:
	import fabric
except ModuleNotFoundError as e:
	print("Please install fabric to use it")
	print(e)
finally:
	print("Finally this will executes")


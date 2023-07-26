# Exception handling

print("Welcome to exceptions concept")
print("\nTesting zero division")
try:
	print(4/0)
except:
	print("ZeroDivisionError: division by zero")

print("\nTesting openning file")
req_file="test.txt"
try:
	fo=open(req_file)
except:
	print(f"FileNotFoundError: [Errno 2] No such file or directory: {req_file}")

print("\nPrint exception")
try:
	fo=open(req_file)
except Exception as e:
	print(e)


print("\nIndex out of range")
my_list=[3,4,5]
try:
	print(my_list[4])
except Exception as e:
	print(e)


print("\nError importing module")
try:
	import fabric
except Exception as e:
	print(e)









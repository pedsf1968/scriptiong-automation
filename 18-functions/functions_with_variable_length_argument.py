def display(*arg):
	for each in arg:
		print(each,type(each))
	return None

print("Call with no argument")
display()
print("\nCall with 1 argument")
display(4)
print("\nCall with 3 numbers")
display(4,5,67)
print("\nCall with different types of arguments")
print('-------------')
display("hi",4.65)
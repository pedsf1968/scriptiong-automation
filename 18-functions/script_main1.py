def addition(a,b):
	print(f'The addition of {a} and {b} is: {a+b}')
	return None

def substraction(a,b):
	print(f'The sub of {a} and {b} is: {a-b}')
	return None

# Define main function to not call the code below when importing module
def main():
	x=7
	y=6

	addition(x,y)
	substraction(x,y)

# If we execute the script, the main function is called
if __name__=="__main__":
	main()
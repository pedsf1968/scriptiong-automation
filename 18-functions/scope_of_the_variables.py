# Function without parameter
def myfunction1():
	x=60  #This is local variable
	print("Welcome to functions")
	print("x value from function 1: ",x)
	#myfunction2()
	return None

# Function with parameter
def myfunction2(x):  #Parameter
	print("Thank you!!")
	print("x value from function 2: ",x)
	return None

def main():
	#global x
	x=10
	print("x value from main:",x) 
	myfunction1()
	myfunction2(x)  #Argument
	return None


main()












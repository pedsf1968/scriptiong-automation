
# Function with simple default argument
def display(a=1):
	print("The value of a is: ",a)
	return None

display(4)
display(5)
display()

# Function with default argument nether the first
def add_numbers(a,b=0):
	result=a+b
	print("The result is: ",result)
	return None
add_numbers(4,5)
add_numbers(5)
add_numbers(7)

# Function with string default argument
def working_on_some(user="root"):
	print(f"working with {user}")
	return None

working_on_some("weblogic_admin")
working_on_some()
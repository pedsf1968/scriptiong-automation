# We can use the name of the arguments in the call of the function
def display(a,b):
	print(f'a={a}')
	return None

display(3,4)

# We must use the same arguments names
display(a=3,b=5)
display(b=6,a=3)
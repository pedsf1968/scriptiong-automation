# Arguments is dictionnary
def display(**karg):
	print(karg)
	return None

def display2(a,**karg):
	print(a,karg)
	return None

print("\nCall function with 2 numbers and the arguments names")
display(b=5,a=4)
print("\nCall function with 3 numbers and the arguments names")
display(a=4,b=5,c=6)
print("\nCall function with numbers, strings and arguments names")
display(x=5,y="Hi",z=6.7,user="root")
display2(54,x=5,y="Hi",z=6.7,user="root")
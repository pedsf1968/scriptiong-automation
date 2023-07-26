import script_main1
def multiplication(a,b):
	print(f'The multiplication of {a} and {b} is: {a*b}')
	return None

def main():
	x=50
	y=90
	script_main1.addition(x,y)
	script_main1.substraction(x,y)
	multiplication(x,y)

if __name__=="__main__":
	main()
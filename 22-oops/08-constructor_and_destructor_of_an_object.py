# Using constructor to instantiate object and destructor

class Person(object):
	# Constructor that initialise the object
	def __init__(self,name,age):
		print("an object has been created")
		self.name=name
		self.age=age		
		return None
	# Destructor to be called to delete object
	def __del__(self):
		print("object has been deleted")
		return None

def main():
	# Call constructor with arguments
	per1=Person('Jhon',26)
	return None

if __name__=='__main__':
	main()
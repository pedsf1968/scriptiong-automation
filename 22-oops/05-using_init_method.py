# using __init__ method to create object

class Emp(object):
	def __init__(self,name,salary):
		print("Initialisation method")
		self.name=name
		self.salary=salary
		return None
	def display(self):
		print(f"The name is: {self.name}\nThe salary is: {self.salary}")
		return None
	def salaryChange(self,salary):
		print("Increase salary only")
		if salary>self.salary:
			self.salary=salary
		return None		

def main():
	# Instantiation require 2 arguments
	emp1=Emp('Ramu',56000)
	emp2=Emp("Naren",90000)
	
	emp1.display()
	emp1.salaryChange(57000)
	emp1.display()
	#emp2.display()

if __name__=='__main__':
	main()
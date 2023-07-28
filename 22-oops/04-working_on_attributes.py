class emp:
	# count is a value of the class and not the object
	count=0
	def init(self,name,age,salary):
		self.name=name
		self.age=age 
		self.salary=salary
		self.increase_count_for_emp()
		return None
	def increase_count_for_emp(self):
		emp.count=emp.count+1
		return None
	def display_details(self):
		print(f'\nThe name is: {self.name}\nThe age is: {self.age}\nThe salary is: {self.salary}')
		return None

def main():
	emp1=emp()
	emp2=emp()

	print(emp.count)
	emp1.init('John',34,45000)
	emp1.display_details()
	print(emp.count)
	emp2.init('William',25,54000)
	emp2.display_details()
	print(emp.count)
	emp1.increase_count_for_emp()
	print(emp.count)
	return None

if __name__=='__main__':
	main()




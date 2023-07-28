# With encapsulation we can't call variable or method prefixed by __ outside the class
# You must use fonction to get values.
class Person(object):
	def assing_name_and_age(self,name,age):
		# Accessible out of the class with object.name
		self.name=name
		# Can't access variables prefixed by __ out of the class
		self.__age=age
		self.__display()
		return None
	def getAge(self):
		return self.__age
	def __display(self):
		print(self.name,self.__age)
		return None
	def getInfo(self):
		self.__display()
		return None

def main():
	per1=Person()
	per1.assing_name_and_age('John',32)

	#per1.__display()
	print(per1.name)
	print(per1.getAge())
	per1.getInfo()
	return None

if __name__=='__main__':
	main()
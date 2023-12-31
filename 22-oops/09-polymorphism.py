# Polymorphism allow to define same methods in different classes
# It's known as Method Overriding
# The two classes have the sames methods

class Tomcat(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
	def display(self):
		print("This is from tocmat class")
		print(self.home)
		print(self.version)
		return None 
	
class Apache(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
	def display(self):
		print("This is from apache class")
		print(self.home)
		print(self.version)
		return None 

def main():
	tom_ob=Tomcat('/home/tomcat9','7.6')
	apa_ob=Apache("/etc/httpd",'2.4')

	tom_ob.display()
	apa_ob.display()
	return None

if __name__=='__main__':
	main()
# re-use pre-define class to create an other

class Tomcat(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 
	def display(self):
		print(self.home)
		print(self.version)
		return None 

# Class derived from Tomcat Class
class Apache(Tomcat):
	# Overriding different methods then parent class
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None 


def main():
	tom_ob=Tomcat('/home/tomcat9','7.6')
	apa_ob=Apache("/etc/httpd",'2.4')

	tom_ob.display()
	# Method display inherit from parent class Tomcat
	apa_ob.display()
	return None

if __name__=='__main__':
	main()
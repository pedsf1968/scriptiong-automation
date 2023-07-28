# Use OOPS concept
import os

# The class group functions
# self is always the first argument for a class function
class Tomcat:
	def init(self,server_xml):
		self.tcf=server_xml
		self.th=os.path.dirname(os.path.dirname(server_xml))
		return None

	def display_details(self):
		print(f'\nThe tomcat config file is: {self.tcf}\nThe tomcat home is: {self.th}')
		return None		

def main():
	# Create null object calling the class
	tomcat7=Tomcat()
	tomcat9=Tomcat()
	
	# Initialise objets data
	tomcat7.init("/home/Automation/tomcat7/conf/server.xml")
	tomcat9.init("/home/Automation/tomcat9/conf/server.xml")
	# We can access all variables
	print(tomcat7.th)
	print(tomcat9.tcf)
	print(tomcat9.th)
	print(tomcat7.tcf)
	tomcat9.display_details()
	tomcat7.display_details()
	return None

if __name__=="__main__":
	main()

# The first function initialises data and the second read the informations
# We can't save the information for 2 tomcat at the same time
# we must use objects
import os

def get_details_for_each_tomcat(server_xml):
	# Make variables global to be accessible for display_details()
	global tcf,th
	tcf=server_xml
	# Get parents directories
	th=os.path.dirname(os.path.dirname(server_xml))
	return None

def display_details():
	print(f'The tomcat config file is: {tcf}\nThe tomcat home is: {th}')
	return None		

def main():
	tomcat7="/home/Automation/tomcat7/conf/server.xml"
	tomcat9="/home/Automation/tomcat9/conf/server.xml"

	get_details_for_each_tomcat(tomcat7)
	display_details()
	get_details_for_each_tomcat(tomcat9)
	display_details() 
	return None

if __name__=="__main__":
	main()

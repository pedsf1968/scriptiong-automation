import os
import time
import platform

def mycode(cmd1,cmd2):
	print("Please wait. Cleaning the screen....")
	time.sleep(2)
	os.system(cmd1)
	print("Please wait finding the list of dir and files")
	time.sleep(2)
	os.system(cmd2)

if platform.system()=="Windows":
	mycode("cls","dir")
else:
	mycode('clear','ls -lrt')


# Better writing
commands={
	'clear':{
		'Linux': 'clear',
		'Windows': 'cls',
		'description': "Please wait. Cleaning the screen...."
	},
	'ls':{
		'Linux': 'ls -lrt',
		'Windows': 'dir',
		'description': "Please wait finding the list of dir and files"
	}
}

def myNewCode(cmd_name):
	print(commands[cmd_name]['description'])
	time.sleep(2)
	try:
		os.system(commands[cmd_name][platform.system()])
	except:
		print("No platform to execute!")
	return None

myNewCode("clear")
myNewCode("ls")



try:
	a=9
	print(a)
except NameError:
	print("Variable is not defined")
except Exception as e:
	print("Other exception occured:",e)
else:
	# execute only if there is an exception 
	print("This will execute if there is no exceptions in try block")
finally:
	# execute always
	print("This will executes always")

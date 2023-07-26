# Create a custom exception

# Raise directly an exception if age below 30
age=23
if age>30:
	print("Valid age")
else:
	raise ValueError("Age is less than 30")

# use assert to raise exception
age=20
try:
	assert age>30
	print("Valid age")
except AssertionError:
	print("Raised with assert because age is less than 30")
except:
	print("Exception occured")


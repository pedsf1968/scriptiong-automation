x=3
y=4.5
language_name="Python scripting"
print("\n1 - Print all variables individually")
print(x,y,language_name)
print("\n2 - Print variables in string")
print("{} {} {}".format(x,y,language_name))
print("\n3 - Print variables with special characters")
print("{} \n{} \t{}".format(y,language_name,x))
print("\n4 - Use function to interpret string")
print(f"The x value is:{x}, the y value is:{y} \nThe language is {language_name}")
print("The same thing using variable for the output")
output_message=f"The x value is:{x}, the y value is:{y} \nThe language is {language_name}"
print(output_message)
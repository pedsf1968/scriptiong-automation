# bool(VALUE): return True if VALUE is not empty else False

var_x=4.5
print(var_x)
print("Get variable address")
print(id(var_x))
id_var_x=id(var_x)
print(id_var_x)

print("\nNumbers data types")
var_integer=9
print("Integer variable",var_integer,type(var_integer))
var_float=4.6
print("Floating variable",var_float,type(var_float))
var_complex=3.7j
print("Complex variable",var_complex,type(var_complex))

print("\nBoolean data type")
var_boolean=True
print(var_boolean,type(var_boolean))
var_boolean=False
print(var_boolean,type(var_boolean))

print("\nString data type")
var_string="This is a string with spaces"
print(var_string,type(var_string))

print("\nWe can convert number to string")
var_string_integer=str(var_integer)
print("Integer variable",var_integer,type(var_integer))
print("New variable",var_string_integer,type(var_string_integer))

print("We can convert data types")
var_boolean1=bool(var_integer)
var_boolean2=bool(0)
print(var_integer,type(var_integer)," Positive interger to boolean", var_boolean1, type(var_boolean1))
print( 0, type(0)," Zero integer to boolean",var_boolean2, type(var_boolean2))
print( var_float, int(var_float)," Float to integer", type(int(var_float)))
print("Nothing is always false in boolean")
print("Zero", bool(0))
print("None", bool(None))
print("Empty", bool())
print("Parenthesis", bool(()))
print("Brackets", bool([]))
print("Calibraces", bool({}))
print("Null string", bool(""))





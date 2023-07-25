# Logical-operators and/or/not
# all(CONDITION,...): True if all CONDITIONS is True
# any(CONDITION,...): True if one CONDITIONS is True

a=eval(input("Enter first value: "))
b=eval(input("Enter second value: "))

my_list=[1,2,3,7,5,6,7,8,9]


if a > b and a in my_list:
    print(f"Value {a} > {b} and in {my_list}")

if a < b or a in my_list:
    print(f"Value {a} < {b} or in {my_list}")

if a < b and a not in my_list:
    print(f"Value {a} < {b} and not in {my_list}")

# list of conditions
print(f"All conditions must be True all([2<3,4<5,7>2,9>2]) : {all([2<3,4<5,7>2,9>2])}")
print(f"At least one condition is True with any([2>3,4>5,7>2,9<2]) : {any([2>3,4>5,7>2,9<2])}")


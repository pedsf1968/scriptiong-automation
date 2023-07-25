# Arithmetic and assignment operators

# Assignment opérator
a=eval(input("Enter first value: "))
b=eval(input("Enter second value: "))

# Arithmetic operators
c=a+b
print(f"Addition: {a} + {b} = {c}")
c=a-b
print(f"Substraction: {a} - {b} = {c}")
c=a*b
print(f"Multiplication: {a} * {b} = {c}")
c=a/b
print(f"Division: {a} / {b} = {c}")
c=a**b
print(f"Exponential: {a}**{b} = {c}")
c=a%b
print(f"Modulo: {a}%{b} = {c}")
c=a//b
print(f"Floor division: {a}//{b} = {c}")
print(f"Division {a} by {b} = {a//b}*{b}+{a%b}")

# Assignment opérator
c=a
c+=b
print(f"Increment: {a} by {b} = {c}")
c=a
c-=b
print(f"Decrement: {a} by {b} = {c}")
c=a
c*=b
print(f"Multiplication: {a} by {b} = {c}")
c=a
c/=b
print(f"Division: {a} by {b} = {c}")
c=a
c%=b
print(f"Modulo: {a} by {b} = {c}")


# Comparison operators
# ord(CHAR): return ASCII code of CHAR
# chr(ASCIIL): return CHAR of ASCII code

a=input("Enter first value: ")
b=input("Enter second value: ")

print(f"Greater: {a} > {b}: {a>b}")
print(f"Less: {a} < {b}: {a<b}")
print(f"Equal: {a} == {b}: {a==b}")
print(f"Not equal: {a} != {b}: {a!=b}")
print(f"Greater or equal: {a} >= {b}: {a>=b}")
print(f"Less or equal: {a} <= {b}: {a<=b}")

print(f"'a' < 'b' ? {'a'<'b'} : {ord('a')}<{ord('b')}")
print(f"'aa' < 'b' ? {'aa'<'b'}")
print(f"'aba' < 'aab' ? {'aba'<'aab'}")
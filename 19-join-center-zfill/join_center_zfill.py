# join(): join char with others
# zfill(N): fill string with zero to complete a string of N chars

# Use join
x="python"
y="-".join(x)
print(f'x: {x} and y: {y}')
y="*".join(x)
print(f'x: {x} and y: {y}')
y="\n".join(x)
print(f'x: {x} and y: {y}')
y="\t".join(x)
print(f'x: {x} and y: {y}')

# Use of center
my_str1="python"
my_str2="python scripting"
my_str3="string operation"
print(f"Center 20 \n{my_str1.center(20)}\n{my_str2.center(20)}\n{my_str3.center(20)}")
print(f"Center 80 \n{my_str1.center(80)}\n{my_str2.center(80)}\n{my_str3.center(80)}")

# Use of zfill
print(f"zfill 20 \n{my_str1.zfill(20)}\n{my_str2.zfill(20)}\n{my_str3.zfill(20)}")


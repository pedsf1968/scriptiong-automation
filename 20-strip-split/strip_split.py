# Remove characters with strip
my_str="   python  "
print(f"Remove spaces from string \'{my_str}\': \'{my_str.strip()}\'")
my_str="python"
remove_str="p"
print(f"Remove \'{remove_str}\' from string \'{my_str}\': \'{my_str.strip(remove_str)}\'")
remove_str="n"
print(f"Remove \'{remove_str}\' from string \'{my_str}\': \'{my_str.strip(remove_str)}\'")
remove_str="z"
print(f"Remove \'{remove_str}\' from string \'{my_str}\': \'{my_str.strip(remove_str)}\'")

# Remove strings with strip, rstrip and lstrip
my_str="python scripting is easy"
remove_str="easy"
print(f"Remove \'{remove_str}\' from string \'{my_str}\': \'{my_str.strip(remove_str)}\'")
my_str="python scripting is easy python"
remove_str="python"
print(f"Remove right \'{remove_str}\' from string \'{my_str}\': \'{my_str.rstrip(remove_str)}\'")
print(f"Remove left \'{remove_str}\' from string \'{my_str}\': \'{my_str.lstrip(remove_str)}\'")
print(f"Remove left and right \'{remove_str}\' from string \'{my_str}\': \'{my_str.strip(remove_str)}\'")

# Remove several letters
my_str="pythonyy"
print(f"Remove p and y from {my_str}: {my_str.strip('p').strip('y')}")

# Split a string
my_str="python is easy"
print(f"Split string with default space {my_str}: {my_str.split()}")
my_str="python is easy"
my_str_split="is"
print(f"Split string {my_str} with {my_str_split}: {my_str.split(my_str_split)}")
my_str_split="easy"
print(f"Split string {my_str} with {my_str_split}: {my_str.split(my_str_split)}")
my_str="python is easy and is very popular"
my_str_split="is"
print(f"Split string {my_str} with {my_str_split}: {my_str.split(my_str_split)}")

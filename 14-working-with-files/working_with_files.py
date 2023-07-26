
file_root=input("Enter a new file name: ")

print("Create file and remove content")
req_file=file_root+"0.txt"
fo=open(req_file, 'w')
fo.close()

print("Read file")
print(f"\nContent of the file {req_file}")
fo=open(req_file, 'r')
fo.close()


print("\nCreate file, remove content and test the open mode")
req_file=file_root+"1.txt"
fo=open(req_file, 'w')
print(f"The {req_file} file is readable? {fo.readable()}")
print(f"The {req_file} file is writable? {fo.writable()}")
fo.close()

print(f"\nContent of the file {req_file}")
fo=open(req_file, 'r')
print(f"The {req_file} file is readable? {fo.readable()}")
print(f"The {req_file} file is writable? {fo.writable()}")
fo.close()


print("\nCreate file, remove content and Write lines")
req_file=file_root+"2.txt"
fo=open(req_file, 'w')
fo.write("1-Write line by line\n")
fo.write("2-This is the first line\n")
fo.write("3-This is the second line\n")
fo.write("4-This is the third line")
fo.close()

print(f"\nContent of the file {req_file}")
fo=open(req_file, 'r')
print(fo.read())
fo.close()


print("\nCreate file, remove content and Write lines")
req_file=file_root+"3.txt"
content=["Write a list of lines with loop","This is the first line","This is the second line","This is the third line"]
fo=open(req_file, 'w')
for each_line in content:
    fo.write(each_line+"\n")
fo.close()

print(f"\nContent of the file {req_file}")
fo=open(req_file, 'r')
print(fo.read())
fo.close()

req_file=file_root+"4.txt"
content=["Write a list of lines\n","This is the first line\n","This is the second line\n","This is the third line\n"]
fo=open(req_file, 'w')
fo.writelines(content)
fo.close()

print(f"\nContent of the file using a variable {req_file}")
fo=open(req_file, 'r')
data=fo.read()
fo.close()
print(data)

print("\nAppend lines")
req_file=file_root+"4.txt"
content=["Write a list lines with loop","This is the first line","This is the second line","This is the third line"]
fo=open(req_file, 'a')
for each_line in content:
    fo.write("Append"+each_line+"\n")
fo.close()

print(f"\nContent of the file {req_file}")
fo=open(req_file, 'r')
print(fo.read())
fo.close()

# Not a good practice
print(f"\nRead only 2 lines of file {req_file}")
fo=open(req_file, 'r')
print(fo.readline())
print(fo.readline())
fo.close()

print("\nRead lines using list to loop on each lines")
fo=open(req_file, 'r')
data=fo.readlines()
fo.close()

print("\nDisplay 3 lines")
for each in range(3):
    print(data[each].strip("\n"))

print(f"\nDisplay last lines\n{data[-1]}")

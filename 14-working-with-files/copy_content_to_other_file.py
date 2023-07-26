file_root=input("Enter a new file name: ")

src_file=file_root
dest_file=file_root+"_dest.txt"

# Default mode is read
sfo=open(src_file)
content=sfo.read()
sfo.close()


dfo=open(dest_file, 'w')
dfo.write(content)
dfo.close()

print(f"\nContent of source file {src_file}")
sfo=open(src_file)
print(sfo.read())
sfo.close()

print(f"\nContent of the destination file {dest_file}")
dfo=open(dest_file, 'r')
print(dfo.read())
dfo.close()


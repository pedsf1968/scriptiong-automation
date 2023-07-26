# next(DATA): return content of the first line and move the cursor to the second

import csv 
req_file="D:\\DATA-DEV\\python\\scripting-automation\\15-csv\\new_info.csv"

fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
print("\nGet content in list format")
print(list(content))
fo.close()

fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
print("\nGet only the header")
print(f'The header is:\n {list(content)[0]}')
fo.close()

fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
header=next(content)
print("\nGet the header and the number of rows")
print("The header is: ",header)
print("The no of rows are: ",len(list(content)))
fo.close()

fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
print("\nMove the cursor and get the file content")
next(content)
for each in content:
	print(each)
fo.close()

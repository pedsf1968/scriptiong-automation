import csv

req_file="D:\\DATA-DEV\\python\\scripting-automation\\15-csv\\info.csv"

fo=open(req_file,'r')

# By default delimiter is "," 
print("\nUse csv to convert lines in columns")
csv_reader=csv.reader(fo,delimiter=",")
for each_row in csv_reader:
	print(each_row)
fo.close()

print("\nWe can use simple reader with split function")
fo=open(req_file,'r')
content=fo.readlines()
fo.close()

for each_lines in content:
	print(each_lines.strip("\n").split(","))



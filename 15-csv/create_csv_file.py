import csv

req_file="D:\\DATA-DEV\\python\\scripting-automation\\15-csv\\demo1.csv"
print("Write several lines")
# Add newline="" with Python 3
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['S_No',"Name",'Age'])
csv_writer.writerow([1,"John",23])
csv_writer.writerow([2,"Cliton",24])
fo.close()

fo=open(req_file,'r')
csv_reader=csv.reader(fo)
for each_row in csv_reader:
	print(each_row)
fo.close()

req_file="D:\\DATA-DEV\\python\\scripting-automation\\15-csv\\demo2.csv"


print("Write multiples lines with specific delimiter")
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter="|")
my_data=[['S_No',"Name",'Age'],[1,"John",23],[2,"Cliton",24]]
csv_writer.writerows(my_data)
fo.close()

fo=open(req_file,'r')
csv_reader=csv.reader(fo,delimiter="|")
for each_row in csv_reader:
	print(each_row)
fo.close()


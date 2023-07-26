import json

req_file="D:\\DATA-DEV\\python\\scripting-automation\\16-json\\example.json"

print("\nRead all file and convert into dictionnary")
fo=open(req_file,'r')
print(json.load(fo))
fo.close()

field="squadName"
print(f"\nSearch field: {field}")
fo=open(req_file,'r')
print(json.load(fo).get(field))
fo.close()
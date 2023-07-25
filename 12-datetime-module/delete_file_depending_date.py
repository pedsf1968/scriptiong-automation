import os
import sys
from datetime import datetime

req_path=input("Enter your path: ")
req_age=eval(input("Enter how many days: "))
today=datetime.now()

if not os.path.exists(req_path):
    print("Path is not valid!")
    sys.exit(1)

if os.path.isfile(req_path):
    print("Please provide a direcory!")
    sys.exit(2)

for each_file in os.listdir(req_path):
    complete_path=os.path.join(req_path,each_file)
    if os.path.isfile(complete_path):
        creation_date=datetime.fromtimestamp(os.path.getctime(complete_path))
        day_old=(today-creation_date).days
        if day_old > req_age:
            print(f"{complete_path} should be deleted but no")
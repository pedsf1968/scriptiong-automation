from datetime import datetime

# Need pip install pytz
import pytz

# datetime operations
print(dir(datetime))

# Get all informations in datetime
print(f"today: {datetime.today()}")
print(f"Now: {datetime.now()}")
print(f"Now year: {datetime.now().year}")
print(f"Now month: {datetime.now().month}")
print(f"Now day: {datetime.now().day}")
print(f"Now hour: {datetime.now().hour}")
print(f"Now minute: {datetime.now().minute}")
print(f"Now second: {datetime.now().second}")

# Set date time format
print("\nSpecify custom format")
print(datetime.now().strftime("%y-%m-%d"))
print(datetime.now().strftime("%c"))

# Set different time zone
print("\nChange time zone")
print(pytz.all_timezones)
my_timezone=input("\nSelect a time zone: ")

if my_timezone=="":
    my_timezone="Asia/Seoul" 

ist=pytz.timezone(my_timezone)
print(f"Now in {my_timezone}: {datetime.now(ist)}")

# Get date from timestamp
timestamp=155555
print(f"Date for timestamp {timestamp}: {datetime.fromtimestamp(timestamp)}")
print(f"Date max: {datetime.max}")
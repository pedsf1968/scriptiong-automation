# break: stop the loop
# continue: skip one step
# pass: don't execute the loop

# break get out the loop
'''
for each in [3,4,56,7,8]:
	print(each)
	if each==56:
		break

print("after loop")
'''

# Exit the loop if the value is found

'''
paths=['/usr/bin','/usr/bin/httpd','/home/users/xyz/weblogic/config.xml']
for each_path in paths:
	print("now working on: ",each_path)
	if 'httpd' in each_path:
		print(each_path)
		break
print("outside of for loop")
'''

# Infinit loop that break at 100 value
'''
cnt=1
while True:
	print(cnt)
	if cnt==100:
		break
	cnt=cnt+1
'''

# Skip one step with continue
'''
for each in range(1,11):
	if each ==7:
		continue
		print("this is the line inside of your if condition after continue keyword")
	print(each)
'''


# to don't do anything without error using pass
'''
if True:
	pass
'''
'''
for each in range(3):
	pass 
'''












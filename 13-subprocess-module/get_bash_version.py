import subprocess

# Command to execute use list with shell=False string
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# Command to execute use string with shell=True
# cmd="bash --version"
# sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)


return_code=sp.wait()
out,err=sp.communicate()

if return_code==0:
   # no error
   for each_line in out.splitlines():
      if "version" in each_line  and "release" in each_line:
         print(each_line.split()[3])
         print(each_line.split()[3].split('(')[0])
else:
   print("Command was failed and error is: ",err)

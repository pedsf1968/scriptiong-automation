import subprocess

cmd="dir"
# shell=True open a new shell to execute process
# use True alway on Windows
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

return_code=sp.wait()
out,err=sp.communicate()

print(f"The return code: {return_code}")
print(f"The output:\n{out}")
print(f"The error:\n{err}")

print("\nOutput as a list")
print(f"The output:\n{out.splitlines()}")
print(f"The error:\n{err.splitlines()}")

#sfile="D:\DATA-DEV\python\scripting-automation\14-working-with-files\random.txt"
#dfile="D:\DATA-DEV\python\scripting-automation\14-working-with-files\newrandom.txt"
sfile=input("Enter your source file: ")
dfile=input("Enter your destination file: ")
sfo=open(sfile,'r')
content=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()
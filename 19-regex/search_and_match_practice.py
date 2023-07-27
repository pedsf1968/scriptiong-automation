# re.match(PATTERN,TEXT,FLAG): search only the start
import re

def findStringInText(pattern,text,description="",flag=""):
    if flag=="":
        print(f"\n{description}\nTEXT: {text}\nPATTERN: {pattern}")
        print(re.findall(pattern,text))
    else:
        print(f"\n{description}\nTEXT: {text}\nPATTERN: {pattern}\nFLAG: {flag}")
        print(re.findall(pattern,text,flag))
    return None

def matchObject(pattern,text,description,flag=""):
	findStringInText(pattern,text,description,flag)
	if flag=="":
		match_ob=re.search(pattern,text)
	else:
		match_ob=re.search(pattern,text,flag)
	
	print(match_ob)

	if match_ob:
		print("match from the pattern: ",match_ob.group())
		print('Starting index: ',match_ob.start())
		print('Ending index: ',match_ob.end()-1)
		print("Length: ",match_ob.end()-match_ob.start())
	else:
		print("No match found")
	return None
 

def main():

	text="This is for python2 and there are two major vers python3 and python in future python4"
	pattern=r'\bpython\b'
	matchObject(pattern,text,"Find all python in the text")
	pattern=r'\bpython[23]\b'
	print(f"Print only the match at the start of the first line: {re.match(pattern,text)}")
	

	text="""This is for
python2 and there are two major
vers python3 and python in future python4"""
	pattern=r'\bpython\b'
	matchObject(pattern,text,"Find all python in multiline text")
	pattern=r'\bpython[23]?\b'
	matchObject(pattern,text,"Find all versions of python 2 and 3 in the text")
	
	text="""PYTHON2 and there are two major
vers python3 and python in future python4"""
	pattern=r'\bpython[23]?\b'
	flag=re.IGNORECASE
	matchObject(pattern,text,"Find all versions of python 2 and 3 in the text ignore case",flag)

if __name__=="__main__":
   main()

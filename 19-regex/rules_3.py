# {N}: repeat exactly N times
# {N,M}: repeat N to M times
# +: repeat onece or more
# ?: repeat onece or none
# *: repeat 0 or more
import re

def findStringInText(pattern,text,description):
    print(f"\nTEXT: {text}\nPATTERN: {pattern}\n{description}")
    print(re.findall(pattern,text))

def main():
    text="This is a pythonnnn and python aaa haaaafd xyzaaaaaaaa"

    findStringInText(r'\bpython{4}\b',text,"Find text starting python and ending with 4 letters")
    findStringInText(r'\bxyza{8}\b',text,"Find text starting xyza and ending with 8 letters")
    
    text="xaz asdfa sdf xaaz xaaaaaaaz xaaaaz  xz"
    findStringInText(r'\bxa{2,}z\b',text,"Find text starting xa and ending with z with 2 or more a")
    findStringInText(r'xa{1,}z',text,"Find text starting xa and ending with z with 1 or more a")
    findStringInText(r'xa*z',text,"Find text starting x and ending with z with 0 or more a")
    findStringInText(r'xa?z',text,"Find text starting x and ending with z with 0 or 1 a")
                    

if __name__=="__main__":
	main()
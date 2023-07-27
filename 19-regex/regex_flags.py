# re.IGNORECASE or re.I: no case sensitive 
# re.MULTILINE or re.M: to work with multiline text
# re.LOCALE or re.L : behaviour depend on locale like \w \W \b \s \S
# re.DOTALL or re.S: the "." match all caracter and newline
# re.UNICODE or re.U: \w \W \b \B \d \D \s \S depend of unicode properties
# re.VERBOSE or re.X: allow verbose regular expressions
import re

def findStringInText(pattern,text,description="",flag=""):
    if flag=="":
        print(f"\nTEXT: {text}\nPATTERN: {pattern}\n{description}")
        print(re.findall(pattern,text))
    else:
        print(f"\nTEXT: {text}\nPATTERN: {pattern}\nFLAG: {flag}\n{description}")
        print(re.findall(pattern,text,flag))

def main():
    text="this is a string ThIs is a new staring THIS"

    findStringInText(r'this',text,"Find all string with find ignore case",re.I)
    findStringInText(r'this',text,"Find all string with find ignore case",re.IGNORECASE)


    text="""this is a string EnD
this is second line enD
This is third line end
asfasd this end"""

    findStringInText(r'^this',text,"Find all strings starting with this in multiline text",re.MULTILINE)
    findStringInText(r'^this',text,"Find all strings starting with this in multiline text ignore case",re.M|re.I)
    findStringInText(r'end$',text,"Find all strings ending with end in multiline text ignore case",re.M|re.I)

if __name__=="__main__":
	main()
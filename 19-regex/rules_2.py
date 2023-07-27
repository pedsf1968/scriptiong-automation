# Rules to create a pattern
# ^: begin with
# $: end of the string or newline
# \b: empty string at the begenning or the end of a word
# \B: no spaces between a word
# \t: match tab
# \n: match new line
# \r: match return

import re

def findStringInText(pattern,text,description):
    print(f"\nTEXT: {text}\nPATTERN: {pattern}\n{description}")
    print(re.findall(pattern,text))


def main():
    text='it is a python and it is easy to learn'
    findStringInText("^i[ts]",text,"Find text starting with it or is")

    text='isa python andlearn it learn is easy to learn'
    findStringInText("learn",text,"Find learn")
    findStringInText("learn$",text,"Find text ending with learn")
    
    findStringInText("\\blearn\\b",text,"Find learn in single word in text")
    # using raw string with r
    findStringInText(r"\blearn\b",text,"Find learn in single word in text")
    text='isa python andlearn itlearnis easy to learn'
    findStringInText(r"\Blearn\B",text,"Find learn string without space in text")

    text='isa python andl\tearn itlearnis\teasy to learn'
    findStringInText(r"\t",text,"Find tabulation in text")
    text='isa python andl\tearn itlearnis\neasy to learn'
    findStringInText(r"\n",text,"Find new line in text")

if __name__=="__main__":
	main()
# Use of split sub and subn
# split(pattern, string, maxsplit=0, flags=0)
# sub(pattern, repl, string, count=0, flags=0)
# subn(pattern, repl, string, count=0, flags=0)
import re

# Splitting text with pattern
def splittingText(description,pattern,string,maxsplit=0,flags=0):
    print(f"\n{description}\nTEXT: {string}\nPATTERN: {pattern}\nMAXSPLIT: {maxsplit}\nFLAGS: {flags}")
    print(re.split(pattern,string,flags,maxsplit))        
    return None

def testSplittingText():
    # help(re.split)
    my_str="This is python and python is very easy and we are having python2 and Python3 version"
    my_pat=r'python'
    splittingText(my_pat,my_str,"Split text with pattern")

    my_pat=r'python[23]?'
    splittingText("Split text with pattern ignoring case",my_pat,my_str,flags=re.IGNORECASE)
    splittingText("Split text with pattern ignoring case and maxsplit 2",my_pat,my_str,maxsplit=2,flags=re.IGNORECASE)
    return None

# Substitute pattern by string
def substituteString(description,pattern,substitute,string,count=0,flags=0):
    print(f"\n{description}\nTEXT: {string}\nPATTERN: {pattern}\nNEW STRING: {substitute}\nCOUNT: {count}\nFLAGS: {flags}")
    print(re.sub(pattern,substitute,string,count,flags))        
    return None

def substituteNString(description,pattern,substitute,string,count=0,flags=0):
    print(f"\n{description}\nTEXT: {string}\nPATTERN: {pattern}\nNEW STRING: {substitute}\nCOUNT: {count}\nFLAGS: {flags}")
    print(re.sub(pattern,substitute,string,count,flags))        
    return None

def testSubstituteString():
    # help(re.sub)
    # help(re.subn)
    my_str="This is Python and python is very easy and we are having python2 and Python3 version"
    my_pattern='python[23]?'
    my_substitute_str='JAVA'
    substituteString("Substitute string by other",my_pattern,my_substitute_str,my_str)
    substituteString("Substitute string by other ignoring case",my_pattern,my_substitute_str,my_str,flags=re.IGNORECASE)
    substituteString("Substitute string by other ignoring case",my_pattern,my_substitute_str,my_str,count=0,flags=re.IGNORECASE)
    substituteString("Substitute string by other ignoring case only 2 values",my_pattern,my_substitute_str,my_str,count=1,flags=re.IGNORECASE)
    substituteString("Substitute string by other ignoring case only 2 values",my_pattern,my_substitute_str,my_str,count=2,flags=re.IGNORECASE)

    substituteNString("Substitute string by other ignoring case",my_pattern,my_substitute_str,my_str,flags=re.IGNORECASE)
    substituteNString("Substitute string by other ignoring case only 2 values",my_pattern,my_substitute_str,my_str,count=1,flags=re.IGNORECASE)
    substituteNString("Substitute string by other ignoring case only 2 values",my_pattern,my_substitute_str,my_str,count=2,flags=re.IGNORECASE)

    return None

def main():
    testSplittingText()
    testSubstituteString()
    


if __name__=="__main__":
	main()
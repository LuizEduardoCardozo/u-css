import re

def findOnString(regex,string):
    if(re.findall(regex,string) != []): return True
    else: return False

def findOneLineCommentary(line):
    reCommentLineStart, reCommentLineEnd  = "^\/\*", "\*\/$"
    if((findOnString(reCommentLineStart,line)) & (findOnString(reCommentLineEnd,line)) ): return True
    else: return False

def removeIdentation(string):
    for _ in range(len(re.findall(" ",string))):
        if(findOnString("^"+chr(32),string)):
            string = string[1:]
    return string

def stylesSheetParser(styles_file):
    code = open(styles_file,"r")

    isInsinde = False
    insideCode = []
    codes = []

    for line in code.readlines():
        if(findOnString("{$",line)):
            isInsinde = True
        if(findOnString("}$",line)):
            isInsinde = False
            insideCode.append(codes)
            codes = []
        if(isInsinde):
            #line = "".join([a for a in line.split(" ") if a != ""])
            line = removeIdentation(line)
            codes.append(line[:len(line)-2])
    return (insideCode)

def getCssClasses(styles_file):
    classes = []
    for line in (stylesSheetParser(styles_file)):
        if(line != []):
            title = line[0]
            if(title[0] == "."):
                classes.append(title[1:])

    return list(dict.fromkeys(classes))

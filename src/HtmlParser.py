import re

def parseClasses(html,classRegex):

    inputHTML = open(html,"r")
    html = inputHTML.readlines()
    inputHTML.close()

    classes = []
    for line in html:
        find = re.search(classRegex,line)
        if find != None:
            _class = (find.group())[7:len(find.group())-1] 
            for c in _class.split(" "):
                classes.append(c)

    return list(dict.fromkeys(classes))   
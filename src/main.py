#!/usr/bin/env python3

from Ucss import uCss

from sys import argv as arg

if len(arg) != 3: 
    print("Error, missing arguments")
    exit(1)

classRegex = "class=\".*?\""

html = arg[1]
css = arg[2]

for _class in uCss(html,css,classRegex):
    print(_class)

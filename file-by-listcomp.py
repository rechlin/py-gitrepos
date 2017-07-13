#!/usr/bin/python3

import fileinput
import os
import glob


ScriptFolder = os.path.dirname(os.path.realpath(__file__))
ListFileName = "git-repos.txt"
file = ScriptFolder + "/" + ListFileName

repoList = []


with fileinput.input(file) as f:
    repoList = [line.strip() for line in f if len(line.strip()) > 0 and line.strip()[0] != '#']

lineNum = 0
for line in repoList:
    lineNum += 1
    print("{} {}".format(lineNum,line))
    



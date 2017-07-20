#!/usr/bin/python3
import os
import glob

repoList = []
topDir = "/home/rob/projects"

topDirGlob = topDir + '/**/.git'
print('Debug: glob: ', topDirGlob)

for filename in glob.iglob(topDirGlob, recursive=True):
    repoList.append(filename)

for path in repoList:
    print(path)

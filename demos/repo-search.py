#!/usr/bin/python3
import os
import glob

repoList = []
leadText = self.leadText
topdir = "~/projects"

topDirGlob = topDir + '/**/.git'
if debug:
    print('glob: ', topDirGlob)

for filename in glob.iglob(topDirGlob, recursive=True):
    repoList.append(filename)

for path in repoList:
    print(path)

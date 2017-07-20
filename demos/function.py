#!/usr/bin/python3
import fileinput

def repoListFromFile(rFile):
    repoList = []

    with fileinput.input(rFile) as f:
        for line in f:
            repoList.append(line.strip())
            
    return repoList

# main code
repoListFile = "git-repos.txt"

repoList = repoListFromFile(repoListFile)

for path in repoList:
    print(path)

#!/usr/bin/python3
import fileinput

repoListFile = "git-repos.txt"
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        repoList.append(line.strip())

for path in repoList:
    print('  ',path)

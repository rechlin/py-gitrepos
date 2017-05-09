#!/usr/bin/python3

import pygit2
import fileinput
# from datetime import datetime, timezone, timedelta

repoListFile = "projects-git.repos.txt"

lineNum = 0

repoList = []
debug = False
changeStatusLead = "     - "


with fileinput.input(repoListFile) as f:
    for line in f:
        lineNum += 1;

        lineText = line.strip('\n')
        
        if debug:
            print("line #", lineNum, " ", lineText)
            
        if len(lineText) == 0:
            pass
        elif lineText[0] == '#':
            pass
        else:
            repoList.append(lineText)

for path in repoList:
    print("repo at ", path)

    repoPath = pygit2.discover_repository(path)
    repo = pygit2.Repository(repoPath)
    if repo.is_empty:
        print(changeStatusLead,"Empty Git Repo")
    else:
        changeStatus = ''
        repoStatus = repo.status()
        repoChangeCount = len(repoStatus)
        
        if debug:
            print('Status: ', repoStatus)
            print("Count: ", repoChangeCount)

        if repoChangeCount > 0:
            changeStatus = "There are %s changes"
            print(changeStatusLead, changeStatus % repoChangeCount)
        else:
            changeStatus = "No changes"
            print(changeStatusLead, changeStatus )

print("end")





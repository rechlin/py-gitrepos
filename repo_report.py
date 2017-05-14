#!/usr/bin/python3

import pygit2
import fileinput
import os

if not ('debug' in locals() or 'debug' in globals()):
    debug = False


def repoListFromFile(file):
    lineNum = 0
    repoList = []
    
    if debug:
        print('in repoListFromFile, file is ', file)
    
    with fileinput.input(file) as f:
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
                
        return repoList


def processRepoList(repoList):
    changeStatusLead = "     - "

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

    
def main():
    ListFileName = "git-repos.txt"
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    repoListFile = ScriptFolder + "/" + ListFileName
    
    if debug:
        print("List file with path: ", repoListFile)


    repoList = repoListFromFile(repoListFile)

    processRepoList(repoList)

    print("end")


if __name__ == "__main__":
    main()


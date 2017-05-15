#!/usr/bin/python3

import os.path
import fileinput
import sys
import glob
import argparse
from lib_git_repo import repoListFromFile, processRepoList

debug = True


def repoSearch(topDir):
    """ Return a list of paths to git repos in topDir """
    results = []
    topDirGlob = topDir + '/**/.git'
    if debug:
        print('glob: ', topDirGlob)
    
    for filename in glob.iglob(topDirGlob, recursive=True):
        results.append(filename)

    return(results)


def args(listFile):
    """ Check input, return path or other info """
    parser = argparse.ArgumentParser()
    parser.add_argument('path', 
            nargs='*',
            help="Path(s) to one or more folders that contain one or more git repos",
            default=argparse.SUPPRESS)
    
    args = parser.parse_args()
    return(args)
    


def helpMsg(listFile):
    """ Print help message """
    print('No param: process the files in the default help file: ',listFile)
    print('One param: name of a folder that has a git repo or folders with repos')
    print('First param is help, --help, -h: print this message')


def main():
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    ListFileName = "git-repos.txt"
    repoListFile = ScriptFolder + "/" + ListFileName

    toDo = args(repoListFile)

    if debug:
        print('args is: ', toDo)
    
    if toDo == 'noListFile':
        print('The list file was not found')
        helpMsg(repoListFile)
        
    elif toDo == 'listFile':
        repoList = repoListFromFile(repoListFile)
        processRepoList(repoList)
    
    else:
        repoList = repoListFromFile(repoListFile)
        processRepoList(repoList)
        
    return()



#----------------------------------
if __name__ == "__main__":
    main()


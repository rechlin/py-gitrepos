#!/usr/bin/python3

import os.path
import fileinput
import sys
import argparse
from lib_git_repo import repoInfo

debug = False


def getArgs(listFile):
    """ Check input, return path or other info """
    parser = argparse.ArgumentParser(
        description='Report number of changes in repos',
        epilog="With no arguments, will process file list in: " + listFile)
    parser.add_argument('paths',
            nargs='*',
            help="Path(s) to one or more folders that contain one or more git repos",
            default=argparse.SUPPRESS)

    myArgs = parser.parse_args()
    return myArgs


def main():
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    ListFileName = "git-repos.txt"
    repoListFile = ScriptFolder + "/" + ListFileName

    toDo = getArgs(repoListFile)
    params = vars(toDo)
    
    ri = repoInfo()

    if debug:
        print('args is: ', toDo)
        print('params is: ', params)

    if len(params) == 0:
        if debug:
            print('No argument')
        print('-- Processing repo list file: ', repoListFile)
        repoList = ri.repoListFromFile(repoListFile)
        ri.processRepoList(repoList)
    elif 'paths' in params:
        if debug:
            print('path arguments: ', params['paths'])
        print('-- Processing repos in folders')
        for path in params['paths']:
            print('-- topDir: ', path)
            repoList = ri.repoSearch(path)
            ri.processRepoList(repoList)



#----------------------------------
if __name__ == "__main__":
    main()


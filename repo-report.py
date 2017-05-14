#!/usr/bin/python3

import os.path
import fileinput
import sys
import glob
import argparse
from git_repo_lib import repoListFromFile, processRepoList

debug = False


def repoSearch(topDir):
    """ Return a list of paths to git repos in topDir and sub folders """
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
    parser.addargument('path', 
            nargs='+',
            help="Path(s) to one or more folders that contain one or more git repos")
    
    args = parser.parse_args()
    

def deadcode2():
    """ More code to harvest from in args() """
    if debug:
        print("num inputs: ", numArgs)
        print("script: ", sys.argv[0])

    if numArgs == 1:
        if os.path.exists(listFile):
            return('listFile')
        else:
            return('noListFile')
    elif numArgs > 1:
        for arg in sys.argv[1:]:
            if debug:
                print("This arg: ", arg)
            
            if "=" in sys.argv[1]:
                param, topDir = sys.argv[1].split("=")
                
                if debug:
                    print("    param: ", param)
                    print("    value: ", topDir)
                
                if param == "topDir":
                    if os.path.exists(topDir):
                        print('Processing files in top folder: ', topDir)
                        repoList = repoSearch(topDir)
                        
                        if debug:
                            print('repolist from search of topDir: ', topDir)
                            print('    ',repoList)
                            
                        processRepoList(repoList)
                    else:
                        print('Error: top folder not found: ', topDir)
                        return()
                            
                else:
                    print("param is not topDir")
                    processRepoList(repoListFile)
                
    else:
        if debug:
            print('no params on command line')
            print('repoListFile: ', repoListFile)

        repoList = repoListFromFile(repoListFile)
        processRepoList(repoList)
    


def helpMsg(listFile):
    """ Print help message """
    print('No param: process the files in the default help file: ',listfile)
    print('One param: name of a folder that has a git repo or folders with repos')
    print('First param is help, --help, -h: print this message')


def main():
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    ListFileName = "git-repos.txt"
    repoListFile = ScriptFolder + "/" + ListFileName

    toDo = args(repoListFile)
    
    if toDo == 'noListFile':
        print('The list file was not found')
        helpMsg(repoListFile)
        
    elif toDo == 'listFile':
        repoList = repoListFromFile(repoListFile)
        processRepoList(repoList)
    
    else:
        helpMsg(repoListFile)
        
    return()
    
    
def deadcode():
    ''' copy from here for cliInput and toDo '''
    numArgs = len(sys.argv)

    if debug:
        print("num inputs: ", numArgs)
        print("script: ", sys.argv[0])

    if numArgs > 1:
        if sys.argv[1] in ['-h', '--help']:
            print('testing')
        for arg in sys.argv[1:]:
            if debug:
                print("This arg: ", arg)
            
            if "=" in sys.argv[1]:
                param, topDir = sys.argv[1].split("=")
                
                if debug:
                    print("    param: ", param)
                    print("    value: ", topDir)
                
                if param == "topDir":
                    if os.path.exists(topDir):
                        print('Processing files in top folder: ', topDir)
                        repoList = repoSearch(topDir)
                        
                        if debug:
                            print('repolist from search of topDir: ', topDir)
                            print('    ',repoList)
                            
                        processRepoList(repoList)
                    else:
                        print('Error: top folder not found: ', topDir)
                        return()
                            
                else:
                    print("param is not topDir")
                    processRepoList(repoListFile)
                
    else:
        if debug:
            print('no params on command line')
            print('repoListFile: ', repoListFile)

        repoList = repoListFromFile(repoListFile)
        processRepoList(repoList)
    
    print("repos end")
        

#----------------------------------
if __name__ == "__main__":
    main()

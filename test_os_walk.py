#!/usr/bin/python3

import os.path
import fileinput
import sys
import glob
from repo_report import repoListFromFile, processRepoList

debug = True


def repoSearch(topDir):
    """ Return a list of paths to git repos in topDir and sub folders """
    results = []
    topDirGlob = topDir + '/**/.git'
    if debug:
        print('glob: ', topDirGlob)
    
    for filename in glob.iglob(topDirGlob, recursive=True):
        results.append(filename)

    return(results)



def main():
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    ListFileName = "git-repos.txt"
    repoListFile = ScriptFolder + "/" + ListFileName

    numArgs = len(sys.argv)

    if debug:
        print("num inputs: ", numArgs)
        print("script: ", sys.argv[0])

    if numArgs > 1:
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
                            
                        processRepoList(repoListFile)
                    else:
                        print('Error: top folder not found: ', topDir)
                        return()
                            
                else:
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

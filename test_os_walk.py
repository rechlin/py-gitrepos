#!/usr/bin/python3

from os.path import isfilepath, exists

# check for a top directory on command line interface

import sys

debug = True


            
 
def repoSearch(topDir):
    """ Return a list of paths to git repos in topDir and sub folders """
    result = []
    
    
    
def processRepoList(listFile):
    """ 
    Extract a list of folders from the repo list file.
    
    Return the list.
    """
    if not os.path.isfilepath(repoListFile):
        print('Error: repo list file not found: ', listFile
        return
    
    with fileinput.input(listFile) as f:
        for line in f:
            lineNum += 1;

            lineText = line.strip('\n')
            
            print(lineNum, ' ', lineText


def main():
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    ListFileName = "git-repos.txt"
    repoListFile = ScriptFolder + "/" + ListFileName

    numArgs = len(sys.argv)

    if debug:
        print("num inputs: ", numArgs)
        print("script: ", sys.argv[0])

    if numArgs > 1:
        for arg in sys.argv[1:]
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
                    repoSearch(topDir)
                else:
                    print('Error: top folder not found: ', topDir)
                    processRepoList(repoListFile)
                        
            else:
                processRepoList(repoListFile)
                
    else:
        processRepoList(repoListFile)
    
    print("end")
        

#----------------------------------
if __name__ == "__main__":
    main()

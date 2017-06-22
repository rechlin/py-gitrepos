#!/usr/bin/python3

import pygit2
import fileinput
import os
import glob

if not ('debug' in locals() or 'debug' in globals()):
    debug = False


class repoInfo:
    """ Report information about git repos """

    def __init__(self):
        self.leadText = "     - "


    def repoListFromFile(self, file):
        """
        - read a file
        - create a repoList from the contents
        - return the list
        """
        leadText = self.leadText
        lineNum = 0
        repoList = []

        if debug:
            print('in repoListFromFile, file is ', file)

        if not os.path.exists(file):
            print('File not found: ', file)
            exit()

        with fileinput.input(file) as f:
            for line in f:
                lineNum += 1;

                # remove leading and trailing whitespace, including \r\n
                lineText = line.strip()

                if debug:
                    print("line #", lineNum, " ", lineText)

                if len(lineText) == 0:
                    pass
                elif lineText[0] == '#':
                    pass
                else:
                    repoList.append(lineText)

            return repoList


    def repoSearch(self, topDir):
        """
        Return a list of paths to git repos that are:
        - in the topDir(s) provided on command line,  or
        - in sub-folders of the topDir(s) provided
        """

        results = []
        leadText = self.leadText

        if not os.path.exists(topDir):
            print(leadText, 'Error: Folder does not exist: ', topDir)
            exit()
        elif not os.path.isdir(topDir):
            print(leadText, 'Error: Not a folder: ', topDir)
            exit()

        topDirGlob = topDir + '/**/.git'
        if debug:
            print('glob: ', topDirGlob)

        for filename in glob.iglob(topDirGlob, recursive=True):
            results.append(filename)

        return(results)


    def processRepoList(self, repoList):
        """
        Report on:
        - all repos in list,
        - all repos in sub-folders of folder provided on command line
        """

        leadText = self.leadText

        for path in repoList:
            print("repo at ", path)

            if not os.path.exists(path):
                print(leadText, 'Folder/file does not exist: ', path)
                continue

            try:
                repoPath = pygit2.discover_repository(path)
            except KeyError:
                print(leadText, 'Error: No repo in ', path)
                print(leadText, 'Possibly more than one repo in nested folders?')
                continue
            except Exception as e:
                print(leadText, 'Error: Not sure what error', e)

                raise

            repo = pygit2.Repository(repoPath)
            if repo.is_empty:
                print(leadText,"Empty Git Repo")
            else:
                changeStatus = ''
                repoStatus = repo.status()
                repoChangeCount = len(repoStatus)

                if debug:
                    print('Status: ', repoStatus)
                    print("Count: ", repoChangeCount)

                if repoChangeCount > 0:
                    changeStatus = "%s changes"
                    print(leadText, changeStatus % repoChangeCount)
                else:
                    changeStatus = "No changes"
                    print(leadText, changeStatus )


def main():
    """
    If someone runs this library directly:
    - process a repoList from the usual file, if present
    """

    ListFileName = "git-repos.txt"
    ScriptFolder = os.path.dirname(os.path.realpath(__file__))
    repoListFile = ScriptFolder + "/" + ListFileName

    if debug:
        print("List file with path: ", repoListFile)

    repos = repoInfo()
    repoList = repos.repoListFromFile(repoListFile)
    repos.processRepoList(repoList)

    print("end")


if __name__ == "__main__":
    main()

#!/usr/bin/python3

import pygit2
import fileinput
# from datetime import datetime, timezone, timedelta

repoListFile = "projects-git.repos.txt"

lineNum = 0

repoList = []
debug = False


with fileinput.input(repoListFile) as f:
    for line in f:
        lineNum += 1;

        lineText = line.strip('\n')
        if debug:
            print("line #", lineNum, " ", lineText)
        
        repoList.append(lineText)

for path in repoList:
    print("repo at ", path)

    repoPath = pygit2.discover_repository(path)
    repo = pygit2.Repository(repoPath)
    if repo.is_empty:
        print("     - Empty Git Repo")
    else:
        changeStatus = ''
        print(repo.describe(committish=None, max_candidates_tags=None, describe_strategy=None, pattern=None, only_follow_first_parent=None, show_commit_oid_as_fallback=None, abbreviated_size=None, always_use_long_format=None, dirty_suffix=None ) )

        if repo.describe(committish=None,dirty_suffix="dirty").endswith( "dirty"):
            changeStatus = "There are changes"
        else:
            changeStatus = "No changes"
        print("     - ", changeStatus)

print("end")





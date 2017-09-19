### Python as a Second Language

Presenter: **Rob Echlin**

v1.1
---
## Common tasks
* Reading a text file
* Display
* Walking a directory tree
* Functions

Note:
* Experienced developers need clear examples, not lots of lessons


---
## Reading a text file

```python
import fileinput

repoListFile = "git-repos.txt"
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        repoList.append(line.strip())
```
@[1]
@[3]
@[4]

@[6]
@[7]
@[8]

Note:
1 - using the fileinput module from Python standard library
3 - the name of the file we will be reading
4 - an empty array we can insert lines into
6 - open the file for input, and give it a short name, f
  - colon marks the beginning of a group of lines, that the input/assignment applies to
  - "with" is a way to apply the open file, and the rename, just to the loop
7 - do this for each line in the file, new group nested in the previous
8 - only one line to be repeated
    - strip any whitespace from both ends of the line
    - the stripped line becomes the next item in the array

---
## Print the text file

```python
import fileinput

repoListFile = "git-repos.txt"
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        repoList.append(line.strip())

for path in repoList:
    print(path)
```
@[1-9]
@[10]
@[11]

Note:
1-9 - Identical to previous slide?

10 - another for loop, no need to attach anything to it, it just uses the existing array
11 - Whatcha gonna do?

---
## Walking a directory tree

```python
import os
import glob

repoList = []
topDir = "/home/rob/projects"

topDirGlob = topDir + '/**/.git'
print('Debug: glob: ', topDirGlob)

for filename in glob.iglob(topDirGlob, recursive=True):
    repoList.append(filename)

for path in repoList:
    print(path)
```

---
## Functions

```python
#!/usr/bin/python3
import fileinput

def repoListFromFile(rFile):
    repoList = []
    with fileinput.input(rFile) as f:
        for line in f:
            repoList.append(line.strip())
    return repoList

# main code
repoList = repoListFromFile("git-repos.txt")
for path in repoList:
    print(path)
```
---
### Author

* https://gitpitch.com/rob_echlin_open_source_training/py-gitrepos-lab/master?grs=gitlab&t=sky
* https://gitlab.com/rob_echlin_open_source_training/py-gitrepos-lab
* http://rob.echlin.ca/

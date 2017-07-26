### Ottawa Python: 
### Python as a Second Language

Presenter: **Rob Echlin**

July 27, 2017

---

## Part 1: Common tasks
* Reading a text file
* Walking a directory tree
* Using a third-party library
* Finding tools from the Python Library

Note:
* Experienced developers need clear examples, not lots of lessons


---
## Reading a text file

```python
import fileinput

repoListFile = "git.repos.txt"
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
#!/usr/bin/python3
import fileinput

repoListFile = "git.repos.txt"
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        repoList.append(line.strip())

for path in repoList:
    print(path)
```

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
## Using a third-party library

---
## Finding tools from the Python Library

---
## Part 2: Structuring your code
* Checking your input
* Creating a function
• Creating a Class
* Using a class you created
* Description of function or class
* Common functions and variables for the Object

---
## Creating a function

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
## Creating a Class

---
## Using a class you created

---
## Description of function or class

---
## Common functions and variables for the Object


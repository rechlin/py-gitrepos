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
## Finding tools from the Python Library (1)

Use search to find a specific thing in the documentation
* "site:docs.python.org input file"
* Apparently DuckDuckGo ignores "site:"
* Google found: "10.2 fileinput - iterate over lines from multiple input streams ..."
* https://docs.python.org/3.5/library/fileinput.html
* Python >> 2.7 Documentation >> The Python Standard Library >> 11. File and Directory Access
  * The "2.7" is a drop down list - use it to get to 3.5, which is on my Linux system

Note:
This is a hard thing.
If you know what is in each of several modules, you have a basis for guessing.


---
## Finding tools from the Python Library (2)
Search Everywhere!
* Blogs
 Quora, Stack Overflow

---
## Using a third-party library

---
## Part 2: Structuring your code
* Checking your input
* Creating a function
* Creating a Class
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


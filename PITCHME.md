### Ottawa Python: 
### Python as a Second Language

Presenter: **Rob Echlin**

July 27, 2017

Ottawa Python Authors Group (OPAG)

---
## Outline

### Part 1: Common Tasks
Break

### Part 2: Code Structure
end?

### Future plans


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
## Finding tools from the Python Library (1)

Use search on docs.python.org
* "site:docs.python.org input file"
  * Apparently DuckDuckGo ignores "site:"
* Google found: "10.2 fileinput ..."
* Python >> 2.7 Documentation >> ...
  * Click "2.7": change to 3.5 or preferred
* https://docs.python.org/3.5/library/fileinput.html

Note:
This is a hard thing.
If you know what is in each of several modules, you have a basis for guessing.


---
## Finding tools from the Python Library (2)
Search Everywhere!
* Blogs
* Quora
* Stack Overflow
* Suggestions?

---
## Using a third-party library
Here: pygit2, depends on gitlib2
* Requires complete version match!
  * pip3: pygit 0.25.1
  * apt show libgit2*
    * 0.24.1-2
  * Download source and build manually
  * cmake .  ; make  ; make test
  * sudo make install

---
## Part 2: Code Structure

Take a break here?

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
```
class repoInfo:

    def repoListFromFile(self, file):
        print('Hello, Classics')
```

Note:
Just add in the "Class", and indent stuff

---
## Using a class you created
* Class name: repoInfo
* Class file: lib_git_repo.py
  * same folder as the main program
* Import your file:
  * ```from lib_git_repo import repoInfo```
* Use the class:
  * ```ri = repoInfo()```
  * ```rList = ri.rListFromFile(listFile)```

---
## Description of function or class
```
class repoInfo:
    """ Report information about git repos """

    def repoListFromFile(self, file):
        """
        - read a file
        - create a repoList from the contents
        - return the list
        """
        print('Hello, Classicists')
```

---
## Common bits for the Object
```
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
        print(self.leadText, 'Good morning, Klaus')
```

---
### Future Plans
* About GitPitch
* Production code
* Pytest


---
### End

* https://gitpitch.com/rob_echlin_open_source_training/py-gitrepos-lab/master?grs=gitlab&t=sky
* https://gitlab.com/rob_echlin_open_source_training/py-gitrepos-lab
* http://rob.echlin.ca/

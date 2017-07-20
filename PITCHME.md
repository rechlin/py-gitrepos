### Ottawa Python: 
### Python as a Second Language

Presenter: **Rob Echlin**

July 27, 2017

---

## Part 1: Common tasks
* Reading a text file
* Walking a directory tree
* Using a third-party library

Note:
* For experienced developers, you need simple examples, not lots of lessons


---
## Reading a text file

```python
import fileinput

repoListFile = "projects-git.repos.txt"
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

repoListFile = "projects-git.repos.txt"
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        repoList.append(line.strip())

for path in repoList:
    print(path)
```


---
## Walking a directory tree

---
## Using a third-party library

---
## Part 2: Structuring your code
* Using tools from the Python Library
* Creating a function
• Creating a Class
* Using a class you created
* Description of function or class
* Common functions and variables for the Object

---
## Using tools from the Python Library

---
## Creating a function

---
## Creating a Class

---
## Using a class you created

---
## Description of function or class

---
## Common functions and variables for the Object


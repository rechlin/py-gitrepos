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
lineNum = 0
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        lineNum += 1;
        repoList.append(line.strip())
```

---
## Displaying the text file

```python
#!/usr/bin/python3
import fileinput

repoListFile = "projects-git.repos.txt"
lineNum = 0
repoList = []

with fileinput.input(repoListFile) as f:
    for line in f:
        lineNum += 1;
        repoList.append(line.strip())

for path in repoList:
    print(path)
```


---
## Walking a directory tree

---
## Using a third-party library
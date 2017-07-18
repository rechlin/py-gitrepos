### Ottawa Python: 
### Python as a Second Language

Presenter: **Rob Echlin**

July 27, 2017

---

## Part 1: Common tasks
* Reading a text file
* Walking a directory tree
* Using a third-party library

---
## Reading a text file

```python
import fileinput

repoListFile = "projects-git.repos.txt"
lineNum = 0
repoList = []
debug = False

with fileinput.input(repoListFile) as f:
    for line in f:
        lineNum += 1;
        repoList.append(line.strip())
```


---
## Walking a directory tree

---
## Using a third-party library
# Python Git Repos Status

A Python script to list the status (are there changes?) of a list of git repos.

* Script name: **repo-report.py**

* The list of repos is stored in a file called: git-repos.txt

## Prepration
Store the script and list in a folder on your path, in the same folder.

## Usage
* repo-report.py
  * Process the list of folders in git-repos.txt
* repo-report.py -h
  * Also: --help
* repo-report.py path1 /path/2 /path/3/.git
  * Paths to folders with a git repo, or repos in sub-folders

## Extra features
* Ignores blank lines
* Ignores lines starting with '#'

Examples from Linux:
* Your projects: /home/me/projects
* Your web sites: /var/www

# Known Issues
Please report any issues you find!

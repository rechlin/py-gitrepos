# Python Git Repos Status

A Python 3 script to list the status (are there changes?) of a list of git repos.

* Script name: **repo-report.py**

* The list of repos is stored in a file called: git-repos.txt


## Preparation
* Install libgit2  0.25.1
* Install pygit2   0.25.1
* Store the script in a folder on your path
* Optionally store a list of repos in git-repos.txt in the same folder


## Python as a Second Language
This script has been used as a source of examples for a presentation 
for experienced programmers who want to learn Python,
called "Python as a Second Language".

The file "PITCHME.md", in this folder, contains the MarkDown text used
to generate the presentation.

More info:
* [About GitPitch](https://gitpitch.com/)
* View the [![GitPitch](https://gitpitch.com/assets/badge.svg)](https://gitpitch.com/rob_echlin_open_source_training/py-gitrepos-lab/master?grs=gitlab&t=sky)

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


## Examples of potential paths from Linux:
* Your projects: /home/me/projects
* Your web sites: /var/www


## Known Issues
* Unit tests are not complete
* Please report any issues you find!

= Python Git Repos Status

A Python script to list the status (are there changes?) of a list of git repos.

The list is stored in a file called: git-repos.txt

== Extra features:
- Ignores blank lines
- Ignores lines starting with '#'

== Parameters:
- The script does not take parameters 

== Known issues:
- Requires \n at the end of all lines, 
  - This means it may mess up on Mac or Windows
  - Last line with a path must have \n on it (In other words, not be the last line)
- the following cases are not accounted for:
  - just spaces
  - a non-path such as a line of poetry
  - a path to a non-existent location, such as /user/locla (spellos)

== Future development
- Provide a (smaller) list of folders where your repos are to be found (examples are from Linux)
  then find the ".git" folders in Python directly
  - Your projects: /home/me/projects
  - Your web sites: /var/www
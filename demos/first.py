#!python 

name = raw_input('What is your name? ') + " "

try:
    myVar = int(name)
except ValueError:
    myVar = name

print myVar + myVar

print myVar * 3


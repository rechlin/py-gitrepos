#!/usr/bin/python3
# Looping along with 2 Comp Sci legends

print('Must install ansicolors')
print('from colors import color')

import fileinput
from colors import color
# import print_function

string = []

# get the text
with fileinput.input("loop.txt") as f:
    for line in f:
        string.append(line.strip())

# output some of it
myString = string[0]
print( 'myString = ', myString)

#for i in range(16):
#    print(color('Color #%d' % i, fg=i))

count = 1
a, b = 0, 1
while b <= len(myString):
    a, b = b, a + b
    # print('{} {}'.format(a, b))
    
    print(color(myString[0:b] +'\n', fg=count))
    count += 1
    
    

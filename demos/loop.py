#!/usr/bin/python3
# Looping along with 2 Comp Sci legends

# Must install ansicolors
# -> sudo pip3 install ansicolors

from colors import color
import time


# output some of it
myString = "Fiber Natcchos? Series-ly?"
print( '')

# extra vars
colorNum = 1

# Fibonacci numbers - second-last and last
a, b = 0, 1

while b <= len(myString):
    a, b = b, a + b
    # print('{} {}'.format(a, b))

    # increasing delay, by Fibonacci
    time.sleep(0.05 * b)

    # color choice by count, length by Fibonacci
    print(color(myString[0:b], fg=colorNum))
    print()
    colorNum += 2

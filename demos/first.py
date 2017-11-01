#!python

name = raw_input('What  waas your real name? ')

try:
    myVar = int(name)
except ValueError:
    myVar = name

print myVar + "_" + myVar
print "-----------------------"

print ( str(88) + myVar + "      ") * 4

people = [ 'Nathan', 'Heather', 'Aidan','Jadon']

contacts = {'nathan':'334' , 'Heather': '555'}

print

for person in people:
    print 'Name: ', person

print
print 'and now for the dictionary'
for person, num in contacts.iteritems():
    print 'Name: ', person, num

print people[0]

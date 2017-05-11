#!/usr/bin/env python
# Years till 100
import sys

# name = sys.argv[1]
# age = int(sys.argv[2])
# diff = 100 - age

# print '\'Sup', name + ', you have', diff , ' years until you become 100 years old!'


if len(sys.argv) > 1:
	name = sys.argv[1]
else:
	name = raw_input('Please input your name: ')

if len(sys.argv) > 2:
	age = int(sys.argv[2])
else:
	age = int(raw_input('Please enter you age: '))

sayHello = 'Hello ' + name + '. '

age1 = 100 - age
age2 = age - 100

if age == 100:
 sayAge = 'You are already 100 years old!'
elif age < 100:
 	sayAge = 'You will be 100 in ' + str(age1) + ' years!'
else:
 	sayAge = 'Daamn you turned 100 ' + str(age2) + ' years ago!'

print sayHello, sayAge
 	
 
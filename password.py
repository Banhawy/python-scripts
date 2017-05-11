#!/usr/bin/env python
# Program asks user for a password to continue. Example use of if/else statements

import sys

validPassword = 'omak' #This is the correct password

inputPassword = raw_input('Da5al om el password: ')

if inputPassword == validPassword:
	print 'You have access!'
else:
	print 'ETLA3 BARRA YA KOS!'
	sys.exit(0)

print 'Welcome ya ro7 omak!'
	
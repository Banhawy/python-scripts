#! /usr/bin/env python

import sys

cars = ['mercedes', 'volkswagen', 'scooter', 'mazda', 'honda']

answer = raw_input('Welcome to LINGLING Dealership!\nWhat car do you want to buy or lease today?\n')

if answer not in cars:
	print('Sorry we do not have that car here. Goodbye!')
else: 
	print('Alright! Here\'s your new ' + answer +'!')
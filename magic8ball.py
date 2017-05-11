#! /usr/bin/env python

import sys, random

def magic8ball(number):
	if number == 1:
		return "Do it!"
	elif number == 2:
		return "JUST. DO IT!"
	elif number == 3:
		return 'Maybe'
	elif number == 4:
		return 'Yes. But sometimes no...'
	elif number == 5:
		return 'Yes Daddy!'
	elif number == 6:
		return 'NO YOU DUMB FUCK!'
	elif number == 7:
		return 'Nah'
	elif number == 8:
		return 'Contemplate your life. Then ask me again'

while True:
	answer = raw_input('\nDo you want to shake the magic 8 ball?\n')
	if answer == 'yes':
		randomNum = random.randint(1,8)
		print(str(randomNum))
		response = magic8ball(randomNum)
		print(response)
	else:
		break

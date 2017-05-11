#! /usr/bin/env python

import random, sys

maxRange = int(raw_input('Choose any number up to 1000: '))

#Condition to Check if Input is bigger than 1000
if maxRange > 1000:
	print('We don\'t take numbers bigger than 1000.\nGood day, sir.')
	sys.exit()	
secretNumber = random.randint(1, maxRange)
midRange = maxRange/2
lowerBound = 0
upperBound = 0
print('I\'m thinking of a number between 1 and '+ str(maxRange) + '. GUESS WHAT IT IS.')

for i in range(1,11):
	guess = input()
	if guess > secretNumber:
		print('Wrong number. Go lower.\n Number of attempts: ' + str(i))
		upperBound = guess
		if guess == midRange:
			hint = (maxRange + midRange)/2
		else:
			hint = (lowerBound + upperBound)/2
		print('Try ' + str(hint))
			
	elif guess < secretNumber:
		print('Nope. Go higher.\n Number of attempts: ' + str(i))
		lowerBound = guess
		if guess == midRange:
			hint = (maxRange + midRange)/2
		else:
			hint = (lowerBound + upperBound)/2
		print('Try ' + str(hint))

	else:
		break
if guess == secretNumber:
	print('Good job. You guessed the number in ' + str(i) + ' attempts.')
else:
	print('You lost. The number was '+ str(secretNumber))
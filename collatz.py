#! /usr/bin/env python

import sys

def collatz(number):
	#Loop that implemets collatz sequence until number reaches 1
	while number != 1:
		even = number%2 == 0
		if even:
			number = number/2
			print(str(number))
		else:
			number = 3 * number + 1
			print(str(number))

try:
	rakam = int(raw_input("Enter a number:\n"))
	collatz(rakam)
except ValueError:
	print("Error: Input must be an integer.")

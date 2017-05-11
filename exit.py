#!/usr/bin/env python

import sys

while True:
	print("Type exit to exit.")
	exit = raw_input();
	if exit == 'exit':
		sys.exit()
	print("You typed " + exit + '.\n')

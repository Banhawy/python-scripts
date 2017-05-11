#!/usr/bin/env python
import sys

name = ''                           # (1)
while name != 'your name':          # (2)
    #print('')
    name = raw_input('Please type your name.\n')                  # (3)
print('Thank you!')  
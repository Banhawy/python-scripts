#! /usr/bin/env python

heart = "\xE2\x99\xA5"
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', heart, heart, '.', '.', '.'],
        [heart, heart, heart, heart, '.', '.'],
        [heart, heart, heart, heart, heart, '.'],
        ['.', heart, heart, heart, heart, heart],
        [heart, heart, heart, heart, heart, '.'],
        [heart, heart, heart, heart, '.', '.'],
        ['.', heart, heart, '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def myLove():
	for x in range(6):
		for y in range (9):
			print(grid[y][x]),
		print('')

myLove()

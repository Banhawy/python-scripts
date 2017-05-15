#! /usr/bin/env python

heart = "\xE2\x99\xA5"
i = "Adham"
u = "Alison"
grid2 = [['.', '.', '.', '.', '.', '.'],
        ['.', heart, heart, '.', '.', '.'],
        [heart, heart, heart, heart, '.', '.'],
        [heart, heart, heart, heart, heart, '.'],
        ['.', heart, heart, heart, heart, heart],
        [heart, heart, heart, heart, heart, '.'],
        [heart, heart, heart, heart, '.', '.'],
        ['.', heart, heart, '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid1 = [['.', '.', '.', '.', '.', '.'],
        [i, '.', '.', '.', '.', i],
        [i, '.', '.', '.', '.', i],
        [i, '.', '.', '.', '.', i],
        ['.', i, i, i, i, '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid3 = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        [u, u, u, u, u, '.'],
        ['.', '.', '.', '.', '.', u],
        ['.', '.', '.', '.', '.', u],
        [u, u, u, u, u, '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

buff = [['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.']]


def myLove(arr):
	for x in range(6):
		for y in range (len(arr)):
			print(arr[y][x]),
		print('')
def ham(arr):
        for x in range(5):
                for y in range (len(arr)):
                        print(arr[y][x]),
                print('')
        
ham(buff)
myLove(grid1)
ham(buff)
myLove(grid2)
ham(buff)
ham(grid3)
ham(buff)
# print(str(len(grid2[0])))

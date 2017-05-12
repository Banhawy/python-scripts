#! /usr/bin/env Python

def getList(list):
	sentence = ''
	for i in list:
		if i == list[-1]:
			sentence += 'and ' + i
		else:
			sentence += i + ', '
	print(sentence)

pets = ['cats', 'doge']

getList(pets)
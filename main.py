import os, sys

def more(text,numlines=5):
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk: print(line)
		if lines and raw_input('More? [Y|y]: ') not in ["Y", "y", ""]: break
		print '========================================'


def flopen():
	pt = raw_input('Enter the directory: ')
	#pth = sys.argv[1]
	#os.chdir(sys.argv[1])
	os.chdir(pt)
	print os.getcwd()
	#print os.listdir(os.getcwd())
	print os.listdir(pt)
	fname = raw_input('Enter the filename: ')
	txt = open(pt+'/'+fname).read()
	return txt


if __name__ == '__main__':
#	import sys, os
	text = flopen()
	more(text, 5)
	'''
	more(open(sys.argv[1]+'/'+sys.argv[2]).read(), 5)
	'''
	
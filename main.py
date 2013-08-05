'''
	Algorithm:
	1. Get the directory
	2. Switch to the directory
	3. List the files
	4. Get the filename
	5. If the filename is '..' go higher and get back to step 1
	6. If the filename is 'directory' go to the directory and get back to step 1
	7. If the filename is a file - return txt
'''
import os, sys

def more(text,numlines=5):
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk: print(line)
		if lines and raw_input('More? [Y|y]: ') not in ["Y", "y", ""]: break
		print '========================================'

def init():
	os.chdir('/')
	print os.getcwd()
	pth = os.getcwd()
	print os.listdir(pth)
	lst = os.listdir(pth)

	for item in lst:
		if os.path.isfile(item):
			print item + " - a file"	
		else:
			print item + " - a folder"	


def file_name():
	pt = raw_input('Enter the directory: ')
	fpt = os.getcwd()+'/'+pt
	print "fpt is (before while) "+ fpt
	print "fpt is a directory - " + os.path.isdir(fpt)
	while os.path.isdir(fpt):
		os.chdir(fpt)
		print os.getcwd()
		print "fpt is " + fpt
		print os.listdir(fpt)
		lst = os.listdir(fpt)

		for item in lst:
			if os.path.isfile(item):
				print item + " - a file"
			else:
				print item + " - a folder"	
	
		pt = raw_input('Enter the directory or filename: ')
		fpt = fpt + "/" + pt

		if pt == '..':
			print "not ready"
		elif os.path.isdir(fpt+"/"+pt):
			fpt = fpt + "/" + pt
		else:
			return fpt


def file_open(fnm):
	txt = open(fnm).read()
	return txt


if __name__ == '__main__':
	init()
#	import sys, os
	fnm = file_name()
	text = file_open(fnm)
	more(text, 5)
	'''
	more(open(sys.argv[1]+'/'+sys.argv[2]).read(), 5)
	'''
	
'''
Simple file viewer
'''
import os, sys

def file_open(fnm):
	txt = open(fnm).read()
	return txt

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
	pth = os.getcwd()
	lst = os.listdir(pth)
	print pth
	print lst
	'''
	for item in lst:
		if os.path.isfile(item):
			print item + " - a file"	
		else:
			print item + " - a folder"	
	'''
	return pth

def file_name(fpt):
	pt = raw_input('Enter the directory or filename: ')
	fpt = fpt+'/'+pt
	print "fpt is (before while) "+ fpt
	print "fpt is a directory - " + str(os.path.isdir(fpt))
	while True:
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
		print pt
		#fpt = fpt + "/" + pt
		print fpt
		if pt == '..':
			print "not ready"
		elif os.path.isdir(fpt + "/" + pt):
			fpt = fpt + "/" + pt
		else:
			return fpt + "/" + pt




if __name__ == '__main__':
	dpth = init()
	fnm = file_name(dpth)
	text = file_open(fnm)
	more(text, 5)
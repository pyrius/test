import os, sys

'''
if sys.argv[1]:
	print "1st arg " + sys.argv[1]
if sys.argv[2]:
	print "2nd arg " + sys.argv[1]

print len(dir(sys))
'''

path = os.getcwd()
dir = sys.argv[1]
print path
#print os.listdir(dir)
files = os.listdir(dir)
print files
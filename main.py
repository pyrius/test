import os, sys

path = os.getcwd()
dir = sys.argv[1]
print path
#print os.listdir(dir)
files = os.listdir(dir)
print files
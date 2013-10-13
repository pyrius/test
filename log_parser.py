#!/usr/bin/env python
from datetime import datetime
import re, sys


def print_header():
	print '-' * 60
	print "\tBegining log parsing"
	print '-' * 60


def print_footer(dif):
	print '-' * 60
	print "\tEnd of log parsing. Time elapsed - " + str(dif)
	print '-' * 60

def usage_help():
	print "command usage: ./log_parser [file_name]"

def open_file(f_name):
	with open('log.txt') as f:
		content = f.readlines()
	return content

def add_inter_dct(line, int_ptr, int_dct):
	t_lst = int_ptr.findall(line)
	if t_lst:
		if t_lst[0] in int_dct:
			int_dct[t_lst[0]] += 1
		else: 
			int_dct[t_lst[0]] = 1	

if __name__ == '__main__':
	if len(sys.argv[]) < 1:
		usage_help()
		sys.exit(0) 

	print_header()
	t1 = datetime.now()
	content = open_file(sys.argv[1])
	ctr = 1
	int_dct = {}
	int_ptr = re.compile('Ethernet\S*')
	st_log = False

	for st in content:
		if re.search(r'show logging log', st):
			st_log = True

		if st_log:
			if re.search(r'ETHPORT-5-IF_DOWN_LINK_FAILURE:\s', st):
				rg = re.search(r'ETHPORT-5-IF_DOWN_LINK_FAILURE:\s', st)
				print "Line " + str(ctr) + " -- " + st
				add_inter_dct(st, int_ptr, int_dct)
			ctr += 1

	print int_dct
	t2 = datetime.now()
	dif = t2 - t1
	print_footer(dif)
	
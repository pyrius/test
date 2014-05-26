#!/usr/bin/env python

import datetime
import time
import sys 
import calendar
from operator import itemgetter


def open_file():
	if len(sys.argv):
		#fname = "./nfcap"
		fl = open(sys.argv[1],"r")
		return fl

def print_header(flp):
	print flp.readline()


def init_values():	
	time1 = calendar.timegm(datetime.datetime.timetuple(datetime.datetime.now() - datetime.timedelta(days=365) ))
	time2 = calendar.timegm(datetime.datetime.timetuple(datetime.datetime.now() - datetime.timedelta(days=366)))

	return time1, time2



flpt = open_file()
print_header(flpt)

tm1, tm2 = init_values()
err_ctr = 0
l_ctr = 0
tshift_lst = []
tshift_dc = {}


#print calendar.timegm(time2)

#lst = flpt.readlines()
for lst in flpt:
	tlist = lst.split()
	try:
		ttime = calendar.timegm(time.strptime(tlist[2]+ ' ' + tlist[3].split('.')[0],'%Y-%m-%d %H:%M:%S'))
	except:
		pass
	#print ttime
	
	if ttime < tm1:
		tdiff = tm1 - ttime
		#print tdiff
		err_ctr += 1
		'''
		if tdiff not in tshift_lst:
			tshift_lst.append(tdiff)
		'''
		
		if tdiff in tshift_dc.keys():
			tshift_dc[tdiff][0] += 1
			#tshift_dc[tdiff][1].append((tlist[6],tlist[8]))
		else:
			tshift_dc[tdiff] = []
			tshift_dc[tdiff].append(1)
			#tshift_dc[tdiff].append([])
			#tshift_dc[tdiff][1].append((tlist[6],tlist[8]))
		
	#	print "ok ====> " + str(ttime) + ' ' + str(tm1)
	'''
	else:
		print "nok ===>" + str(ttime) + ' ' + str(tm1)
	'''


	tm2 = tm1
	tm1 = ttime
	l_ctr += 1



for item in tshift_dc.keys():
	print str(item) + ' === > ' + str(tshift_dc[item][0])
	#for litem in tshift_dc[item][1]:
		#print "=>" + str(litem)

print '==============================='
print "Total errors: " + str(err_ctr)
print "Total lines: " + str(l_ctr)
print "Unique shifts quantity: " + str(len(tshift_dc.keys())) 


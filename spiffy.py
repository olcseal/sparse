#!/usr/bin/python

# author: sseal
# spiffy.py [sp.conf parser]

import re

openfile = open('sp.conf', 'r')

sp = openfile.read().splitlines()

print "SP.CONF loaded!"
hesi = raw_input("Press any key to show conf file: ")

for i in sp:
	if i != '':
		m = re.search('(.*\{)(.*)(\})(.*$)', i)
		x = m.group(2)
		y = m.group(4)
		print x + " = " + y
	else:
		print ""
		
	

#openfile.read()
#openfile.readline()
#openfile.readlines()
#openfile.tell()
#openfile.seek()
#lines = f.read().splitlines()

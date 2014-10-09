#!/usr/bin/python

# author: Sean Seal
# email: sseal@arbor.net
# sparse.py [sp.conf parser]
#----------------------------------------------------

import sys, getopt, string


#####################################################
# helpMessage
#
# Display the help message from the
# -h option
#----------------------------------------------------
def helpMessage():
    print '''
Usage sparse [option] [argument]
argument is required only with the -s option

Options:
	-h, --help		-- displays this help message
	--version		-- displays version
	-s			-- show (expects an argument)
Arguments for -s:
	devices			-- display device information
	indices			-- displays all indices in sp.conf
	leader			-- displays leader information
	all			-- displays all sp.conf information
'''
    sys.exit(0)
#----------------------------------------------------


#####################################################
# prepFile
#
# Remove all empty lines from initial sp.conf read,
# strip all the extra characters, and finally create
# a new list of lists for every entry in the file.
#----------------------------------------------------
def prepFile():
	openfile = open('sp.conf', 'r')
	l = openfile.read().splitlines()
	openfile.close()

	# remove empty lines
	i = 0 
	x = l.count('')
	while i < x:
		l.remove('')
		i += 1

	# strip extra characters
	i = 0 
	for c in l:
		l[i] = l[i].replace('::set ', '')
		l[i] = l[i].replace('{' , '')
		l[i] = l[i].replace('}', '')
		i += 1

	# create new list of lists
	nl = []
	for x in l:
		y = x.split()
		nl.append([y[0].split('.'), y[1:]])

	# return prepped list from sp.conf file
	return nl
#----------------------------------------------------

#####################################################
# getIndices
#
# Create a list of all indicies found
#----------------------------------------------------
def getIndices(nl):
	indl = []
	for c in nl:
		if c[0][-1] =='indices':
			indl.append(c)
			nl.remove(c)
	return indl
#----------------------------------------------------

#####################################################
# getLeader
#
# Print information for the leader
#----------------------------------------------------
def getLeader(sp, ind):
	# Gather only collector info from sp list
	collector_list = []
	for c in sp:
		if c[0][0] =='collector':
			collector_list.append(c)

	# Pull collector indices from indices list
	collector_indices = []
	for c in ind:
		if c[0][0] == 'collector':
			collector_indices.append(c)

	# Get leader info from collector list
	# using collector indices
	for c in collector_list:
		if c[0][-1] == 'leader':
			leader = c
	for c in collector_list:
		if c[0][1] == leader[1][-1] and c[0][-1] == 'name':
			leader_name = c[1][0]
		if c[0][1] == leader[1][-1] and c[0][-1] == 'type':
			leader_type = c[1][0]
		if c[0][1] == leader[1][-1] and c[0][-1] == 'ip':
			leader_ip = c[1][0]

	print('Leader')
	print('=' * 53)
	print('%-25s : %25s' % ('Leader name', leader_name))
	print('%-25s : %25s' % ('Leader address', leader_ip))
	print('%-25s : %25s' % ('Device gid', leader[1][-1]))
	print('%-25s : %25s' % ('Device type', leader_type))
	print('-' * 53 + '\n')
#----------------------------------------------------


#####################################################
# getDevices
#
# Print information for deployment devices
#----------------------------------------------------
def getDevices(sp, ind):
	# Gather only collector info from sp list
	collector_list = []
	for c in sp:
		if c[0][0] =='collector':
			collector_list.append(c)

	# Pull collector indices from indices list
	collector_indices = []
	for c in ind:
		if c[0][0] == 'collector':
			collector_indices.append(c)

	print('Devices')
	print('=' * 53)
	print('%-25s : %25s' % ('Number of devices', len(collector_indices[0][1])))
	for c in collector_list:
		print(c)
	print(collector_indices)
	print('\n')
#----------------------------------------------------

# MAIN ##############################################

try:
	options, xarguments = getopt.getopt(sys.argv[1:],
	'hs', ['help', 'version'])
except getopt.error:
	print '''
Error: You tried to use an unknown option or the
argument for an option that requires it was missing.
Try \'sparse -h or --help\' for more information.'''
	sys.exit(0)

for a in options[:]:
	if a[0] == '-h':
		helpMessage()

for a in options[:]:
	if a[0] == '--help':
		helpMessage()

for a in options[:]:
	if a[0] == '-s' and a[1] !='':
		print a[0]+' = '+a[1]
		options.remove(a)
		break
	elif a[0] == '-s' and a[1] =='' and not xarguments:
		print('-s expects and argument')
		sys.exit(0)
	elif a[0] == '-s' and a[1] =='' and xarguments:
		if xarguments[0] == 'all':
			sp_list = prepFile()
			sp_indices = getIndices(sp_list)
			getLeader(sp_list, sp_indices)
			getDevices(sp_list, sp_indices)
			sys.exit(0)
		elif xarguments[0] == 'indices':
			sp_list = prepFile()
			sp_indices = getIndices(sp_list)
			for c in sp_indices:
				print(c) 
			sys.exit(0)
		elif xarguments[0] == 'devices':
			sp_list = prepFile()
			sp_indices = getIndices(sp_list)
			getDevices(sp_list, sp_indices)
			sys.exit(0)
		elif xarguments[0] == 'leader':
			sp_list = prepFile()
			sp_indices = getIndices(sp_list)
			getLeader(sp_list, sp_indices)
			sys.exit(0)
		else:
			print('invalid argument supplied...')
			sys.exit(0)

for a in options[:]:
	if a[0] == '--version':
		print 'sparse version 1.0 beta'
		sys.exit(0)

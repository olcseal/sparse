#!/usr/bin/python

# author: Sean Seal
# email: sseal@arbor.net
# sparse.py [sp.conf parser]
#-----------------------------------------

# remEmpty
#
# Remove all empty lines from initial
# sp.conf read.
#-----------------------------------------
def remEmpty(l):
    i = 0
    x = l.count('')
    while i < x:
        l.remove('')
        i += 1
#-----------------------------------------

# stripExtras
#
# Remove ::set , {, and } from sp.conf
# that was read into a list.
#-----------------------------------------
def stripExtras(l):
    i = 0
    for c in l:
        l[i] = l[i].replace('::set ', '')
        l[i] = l[i].replace('{' , '')
        l[i] = l[i].replace('}', '')
        i += 1
#-----------------------------------------

# makeList
#
# Make a list of lists from sp.conf
#-----------------------------------------
def makeList(l):
    nl = []
    for x in l:
        nl.append(x.split())
    return nl
#-----------------------------------------

# getIndices
#
# Create a list of all indicies found
#-----------------------------------------
def getIndices(l):
    
    i = 0
    nl = []
    for c in l:
        tmp = l[i][0].split('.')
        if tmp[-1] == 'indices':
            nl.append(l[i])
            l.remove(c)
        i += 1
    return nl
#-----------------------------------------


#-----------------------------------------
# MAIN
#-----------------------------------------
openfile = open('sp.conf', 'r')
sp = openfile.read().splitlines()

remEmpty(sp)
stripExtras(sp)
sp_list = makeList(sp)
sp_indices = getIndices(sp_list)

for c in sp_list:
    print(c)

print('')

for c in sp_indices:
    print(c)



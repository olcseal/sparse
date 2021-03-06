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
    b = []
    i = 0
    x = l.count('')
    while i < x:
        b.append(l.index(''))
        l.remove('')
        i += 1
    return b
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

# getIndices
#
# Create a list of all indicies found
#-----------------------------------------
def getIndices(l):
    sptmp = []
    for x in l:
        sptmp.append(x.split())

    i = 0
    nl = []
    for c in sptmp:
        tmp = sptmp[i][0].split('.')
        if tmp[-1] == 'indices':
            nl.append(sptmp[i])
        i += 1
    return nl
#-----------------------------------------

# getAaa
#
# Create a dictionary for all the aaa
# entries.
#-----------------------------------------
def getAaa(l):
    tlist = l
    aaa = {}
    index = 0    
    
    for i in tlist:
        line = tlist[index]
        if line[:3] == 'aaa':
            tmpList = line.split()
            if len(tmpList) > 2:
                values = tmpList[1:]
                aaa[tmpList[0]] = values
            else:
                aaa[tmpList[0]] = tmpList[1]
        index += 1
    return aaa
#-----------------------------------------

# getAcfg
#
# Create a dictionary for all the auto
# config entries.
#-----------------------------------------
def getAcfg(l):
    tlist = l
    acfg = {}
    index = 0

    for i in tlist:
        line = tlist[index]
        if line[:10] == 'autoconfig':
            tmpList = line.split()
            if len(tmpList) > 2:
                values = tmpList[1:]
                acfg[tmpList[0]] = values
            else:
                acfg[tmpList[0]] = tmpList[1]
        index += 1
    return acfg 
#-----------------------------------------

# getBlobs
#
# Create a dictionary for all the blob
# entries.
#-----------------------------------------
def getBlob(l):
    tlist = l 
    blob = {}
    index = 0    
        
    for i in tlist:
        line = tlist[index]
        if line[:4] == 'blob':
            tmpList = line.split()
            if len(tmpList) > 2:
                values = tmpList[1:]
                blob[tmpList[0]] = values
            else:
                blob[tmpList[0]] = tmpList[1]
        index += 1
    return blob 
#-----------------------------------------

#-----------------------------------------
# MAIN
#-----------------------------------------
openfile = open('sp.conf', 'r')
sp = openfile.read().splitlines()

print(len(sp))

blank = remEmpty(sp)
stripExtras(sp)
spind = getIndices(sp)


print('blank')
print(blank)
print(len(sp))

index = 0 
while index < 10:
    print(sp[index])
    index += 1

for c in spind:
    print(c)


#-----------------------------------------


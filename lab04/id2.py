#!/usr/bin/python
# Geun Jeon
# Week 4 Lab Part 2 Q3
# CS265
import sys
def fileOpen(f):
	try:
		f = open("ids", "r")
		return f
	except IOError:
		print "No file named after ids, please type in the file name below:"
		f=open(raw_input(), "r")
		return f
		
f = ''
f=fileOpen(f)
l = f.readline()
d={}

while l:
	l = l.strip(' \t\n' )
	k = l.split(" ", 1)
	d[int(k[0])] = k[1]
	l = f.readline()

for key in sorted(d):
	print "%d %s" %(key, d[key])

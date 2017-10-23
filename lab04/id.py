#!/usr/bin/python
# Geun Jeon
# Week 4 Lab Part 2 Q3
# CS265

f = open("ids", "r")
l = f.readline()
d={}

while l:
	l = l.strip(' \t\n' )
	k = l.split(" ", 1)
	d[int(k[0])] = k[1]
	l = f.readline()

for key in sorted(d):
	print "%d %s" %(key, d[key])

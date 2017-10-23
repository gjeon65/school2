#!/usr/bin/python
# s1.py
# Geun Jeon
# Week 4 Lab Part 2 Q1


f = open("students" , "r")
l = f.readline()
sum = 0
nScore = 0

while l :
	l = l.strip(' \t\n' )
	for i in l.split(' '):
		if(i.isdigit()):
			sum += int(i)
			nScore += 1
	print l.split()[0], sum/nScore
	l = f.readline()

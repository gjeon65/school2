#!/usr/bin/python
import os
import sys
import random
import time
#global variables
#True while attemps available if not false; use to determine final output
gameStatusFlag = True

#initialize instaces obj		
class myClass:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.board=[]
		self.posMove=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
		self.location = (0,0)
		self.true = True
		self.gameStatusFlag = True
		self.initBoard()
	
	def initBoard(self):
		self.board=[['x' for i in range(self.rows)]for j in range(self.cols)]
		self.board[0][0] = 1


	def visitMark(self):
		count=0
		for i in range(0, self.rows):
			for j in range(0,self.cols):
				if self.board[rows][cols].visited:
					count = count+1
		return count
	#display board background
	def display(self):
		for row in self.board:
			print row
	#checks if the knight can move in certain direction
	def validMove(self,location):
		valid = []
		for move in self.posMove:
			y=(location[0]+move[0])
			x=(location[1]+move[1])
			if(y >= self.cols):
				continue
			elif(y < 0):
				continue
			elif(x >= self.rows):
				continue
			elif(x < 0):
				continue
			else:
				try:
					if(self.board[y][x] == 'x'):
						valid.append(move)
				except:
					continue

		return valid
	
	def move(self,location,i):
		try:
			posMove = self.validMove(location)
			randMove=posMove[random.randint(0,len(posMove)-1)]
			y = location[0]+randMove[0]
			x = location[1]+randMove[1]
			self.location=(y,x)
			self.board[y][x]=i
		except:
			self.true=False

	def stat(self):
		global gameStatusFlag
		gameStatusFlag = True
		i=0
		while self.true:
			self.move(self.location,i)
			i += 1
		for end in self.board:
			if 'x' in end:
				gameStatusFlag=False
				break

def main(rows, cols, attempts):
	for i in range(attempts):
		game = myClass(rows, cols)
		game.stat()
		if gameStatusFlag:
			print "Success"
			game.display()
			break
		else:
			continue
	if not gameStatusFlag:
			print "Failure"
			game.display()
if __name__ == '__main__':
	main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

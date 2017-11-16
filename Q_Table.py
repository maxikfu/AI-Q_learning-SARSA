import numpy as np
import time
import sys
from tkinter import *
import pandas as pd

#visualizing Q-table in canvas parallel to main screen
class Q_Table:
	def __init__(self,xtitle):
		self.qTable = Tk(  )
		#self.frame = Frame(self.qTable)
		self.title = xtitle
		pixels = 110   # pixels
		height = 5  # grid height
		weight = 5  # grid width
		self.qTable.title(self.title)
		self.qTableCanvas = Canvas(self.qTable,height=height*pixels,width=weight*pixels)
		self.qTable.configure(bg="white")
		# create grids
		for c in range(0, weight * pixels, pixels):
			x0, y0, x1, y1 = c, 0, c, height * pixels
			self.qTableCanvas.create_line(x0, y0, x1, y1, fill="black")
			for r in range(0, height * pixels, pixels):
				x0, y0, x1, y1 = 0, r, height * pixels, r
				self.qTableCanvas.create_line(x0, y0, x1, y1)
		#creating diagonals		
		for c in range(0, weight * pixels+pixels, pixels):
			x0, y0, x1, y1 = c, 0, 0, c
			self.qTableCanvas.create_line(x0, y0, x1, y1, fill="black")
		for c in range(0, height * pixels, pixels):
			x0, y0, x1, y1 = height * pixels, c, c,height * pixels 
			self.qTableCanvas.create_line(x0, y0, x1, y1, fill="black")

		for c in range(0, weight * pixels+pixels, pixels):
			x0, y0, x1, y1 = 0,c , weight * pixels-c, weight * pixels
			self.qTableCanvas.create_line(x0, y0, x1, y1, fill="black")
		for c in range(0, weight * pixels, pixels):
			x0, y0, x1, y1 = c,0 , weight * pixels, weight * pixels-c
			self.qTableCanvas.create_line(x0, y0, x1, y1, fill="black")

		#putting values on canvas
		rows=[]
		for i in range(height):
			for j in range(weight):
				rows.append(str(i+1)+str(j+1))
		self.canvasQId = pd.DataFrame(0,index = rows,columns = ['N','S','E','W'])
		#moving on y axis
		y = pixels/2
		yy = 1
		while  y< height*pixels:
			x = pixels-(pixels/2)/2
			xx = 1
			col = 'E'
			while x < height*pixels-(pixels/2)/2:
				value = self.qTableCanvas.create_text(x,y,fill="black",font="Times 10 italic bold",text=0)
				row = str(xx)+str(yy)
				self.canvasQId.ix[row,col] = value
				x+=pixels/2
				if col == 'E':
					col = 'W'
					xx+=1
				else:
					col = 'E'
			y+= pixels
			yy+=1
		#moving on x axis
		x = pixels/2
		xx=1
		while  x< height*pixels:
			y = pixels-(pixels/2)/2
			yy=1
			col = 'S'
			while y < height*pixels-(pixels/2)/2:
				value = self.qTableCanvas.create_text(x,y,fill="black",font="Times 10 italic bold",text=0)
				row = str(xx)+str(yy)
				self.canvasQId.ix[row,col] = value
				y+=pixels/2
				if col =='S':
					col = 'N'
					yy+=1
				else:
					col ='S'
			x+= pixels
			xx+=1	
		self.qTableCanvas.pack()
	#update values 
	def updateValues(self,q_table):
			for index, row in q_table.iterrows():
				a = ['N','S','W','E']
				if index in ['11','21','31','41','51']:
					a.remove('N')
				if index in ['15','25','35','45','55']:
					a.remove('S')
				if index in ['11','12','13','14','15']:
					a.remove('W')
				if index in ['51','52','53','54','55']:
					a.remove('E')
				maxValue = max(q_table.ix[index,a])
				for col in q_table:
					if col != 'P' and col !='D':
						if maxValue == q_table.ix[index,col]:
							self.qTableCanvas.itemconfigure(self.canvasQId.ix[index,col],text=round(q_table.ix[index,col],3),fill='Green')
						else:
							self.qTableCanvas.itemconfigure(self.canvasQId.ix[index,col],text=round(q_table.ix[index,col],3),fill='Red')


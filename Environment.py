import numpy as np
import time
import sys
from tkinter import *



class World:
	UNIT = 60   # pixels
	environment_height = 5  # grid height
	environmant_weight = 5  # grid width
	pickUpLocations = [[1,1],[1,4],[3,3],[5,5]]
	dropOffLocations = [[1,5],[4,4]]
	totalBlocks=0
	root = Tk(  )
	root.title("PD World")
	canvas = Canvas(root,height=environment_height*UNIT,width=environmant_weight*UNIT)
	root.configure(bg="white")
	# create grids
	for c in range(0, environmant_weight * UNIT, UNIT):
		x0, y0, x1, y1 = c, 0, c, environment_height * UNIT
		canvas.create_line(x0, y0, x1, y1, fill="black")
		for r in range(0, environment_height * UNIT, UNIT):
			x0, y0, x1, y1 = 0, r, environment_height * UNIT, r
			canvas.create_line(x0, y0, x1, y1)
	#putting pick up locations into world
	pickUp_1_1 = canvas.create_rectangle(0, 0,60, 60, fill='lightblue')
	pickUp_1_1_NumBoxes = canvas.create_text(50,10,fill="black",font="Times 10 italic bold",text=4)
	pickUp_1_4 = canvas.create_rectangle(0, (4-1)*UNIT,60, 240, fill='lightblue')
	pickUp_1_4_NumBoxes = canvas.create_text(50,190,fill="black",font="Times 10 italic bold",text=4)
	pickUp_3_3 = canvas.create_rectangle(120, 120,180, 180, fill='lightblue')
	pickUp_3_3_NumBoxes = canvas.create_text(170,130,fill="black",font="Times 10 italic bold",text=4)
	pickUp_5_5 = canvas.create_rectangle(240, 240,300, 300, fill='lightblue')
	pickUp_5_5_NumBoxes = canvas.create_text(290,250,fill="black",font="Times 10 italic bold",text=4)

	pickUpId=[pickUp_1_1_NumBoxes,pickUp_1_4_NumBoxes,pickUp_3_3_NumBoxes,pickUp_5_5_NumBoxes]
	#putting drop off locations
	dropOff_1_5 = canvas.create_rectangle(0, 240,60, 300, fill='lightgreen')
	dropOff_1_5_NumBoxes = canvas.create_text(50,250,fill="black",font="Times 10 italic bold",text=0)
	dropOff_4_4 = canvas.create_rectangle(180, (4-1)*UNIT,240, 240, fill='lightgreen')
	dropOff_4_4_NumBoxes = canvas.create_text(230,190,fill="black",font="Times 10 italic bold",text=0)
	dropOffId=[dropOff_1_5_NumBoxes,dropOff_4_4_NumBoxes]
	canvas.pack()

	def currentAgentLocation(self): #returning agent position in more common coordinates
		agentLoc = self.canvas.coords(self.agentID)
		agentLoc[0] = (agentLoc[0]+UNIT/2)/UNIT
		agentLoc[1] = (agentLoc[1]+UNIT/2)/UNIT
		return agentLoc
	def isPickUpLocationApplicable(self,agent):
		if ([agent.x,agent.y] in self.pickUpLocations) and not agent.block:
			i=self.pickUpLocations.index([agent.x,agent.y])
			if int(self.canvas.itemcget(self.pickUpId[i],"text"))>0:
				return True
		return False
	def isDropOffLocationApplicable(self,agent):
		i=0
		if ([agent.x,agent.y] in self.dropOffLocations) and (agent.block) :
			i=self.dropOffLocations.index([agent.x,agent.y])
			numBoxes=int(self.canvas.itemcget(self.dropOffId[i],"text"))
			if numBoxes<8:
				return True
		return False
	def isNorthApplicable(self,agent):
		if agent.y != 1:
			return True
		return False
	def isSouthApplicable(self,agent):
		if agent.y != self.environment_height:
			return True
		return False
	def isEastApplicable(self,agent):
		if agent.x != self.environmant_weight:
			return True
		return False
	def isWestApplicable(self,agent):
		if agent.x != 1:
			return True
		return False
	def availableActions(self,agent):
		actions = []
		if self.isNorthApplicable(agent):
			actions.append("N")
		if self.isSouthApplicable(agent):
			actions.append("S")
		if self.isEastApplicable(agent):
			actions.append("E")
		if self.isWestApplicable(agent):
			actions.append("W")
		if self.isPickUpLocationApplicable(agent):
			actions.append("P")
		if self.isDropOffLocationApplicable(agent):
			actions.append("D")
		return actions
	def availableAct(self,x,y,block):
		actions = []
		if y != 1:
			actions.append("N")
		if y != self.environment_height:
			actions.append("S")
		if x != self.environmant_weight:
			actions.append("E")
		if x != 1:
			actions.append("W")
		i=0
		if ([x,y] in self.dropOffLocations) and block:
			i=self.dropOffLocations.index([x,y])
			numBoxes=int(self.canvas.itemcget(self.dropOffId[i],"text"))
			if numBoxes<8:
				actions.append("D")
		if ([x,y] in self.pickUpLocations) and not block:
			i=self.pickUpLocations.index([x,y])
			if int(self.canvas.itemcget(self.pickUpId[i],"text"))>0:
				actions.append("P")
		return actions
	def reset(self,agent):
		agent.x = 5
		agent.y = 1
		self.canvas.coords(agent.id,270,30)
		#print(self.canvas.coords(agent.id))
		for iD in self.pickUpId:
			self.canvas.itemconfigure(iD,text=4)
		for iD in self.dropOffId:
			self.canvas.itemconfigure(iD,text=0)
			
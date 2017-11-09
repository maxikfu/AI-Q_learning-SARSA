#from Environment import *

pickUpDropOffReward = 12
movingReward = -1


class Agent:
	#initializing agent with attributes
	def __init__(self,world):
		#setting the agent location
		self.id=world.canvas.create_text(270,30,fill="black",font="Times 20 italic bold",text="A")
		self.x = 5#agent coordinates in the world
		self.y = 1
		self.block = False #if True means carring block at this moment
		self.bankAccount = 0 #reward agent recived at the end of program(way how to compare experiments)
		
	#carring block
	def North(self,world): #make agent move north
		if self.y != 1:
			self.y = self.y - 1
			world.canvas.move(self.id,0,-60)
			self.bankAccount += movingReward
	def South(self,world): #make agent to move south 
		if self.y != world.environment_height:
			self.y = self.y + 1
			world.canvas.move(self.id,0,60)
			self.bankAccount += movingReward
	def West(self,world): #make agent to move west 
		if self.x != 1:
			self.x = self.x - 1
			world.canvas.move(self.id,-60,0)
			self.bankAccount += movingReward
	def East(self,world): #make agent to move east 
		if self.x != world.environmant_weight:
			self.x = self.x + 1
			world.canvas.move(self.id,60,0)
			self.bankAccount += movingReward
	def PickUp(self,world):#picking up item if in pick up location and if it is possible
		i=0
		if ([self.x,self.y] in world.pickUpLocations) and not self.block :
			i=world.pickUpLocations.index([self.x,self.y])
			numBoxes=int(world.canvas.itemcget(world.pickUpId[i],"text"))
			if numBoxes>0:
				newValue = numBoxes-1
				world.canvas.itemconfigure(world.pickUpId[i],text=newValue)
				self.block=True
				world.canvas.itemconfigure(self.id,text="Ab")
				self.bankAccount += pickUpDropOffReward
	def DropOff(self,world): #drop off item if in fropOff location
		i=0
		if ([self.x,self.y] in world.dropOffLocations) and (self.block) :
			i=world.dropOffLocations.index([self.x,self.y])
			numBoxes=int(world.canvas.itemcget(world.dropOffId[i],"text"))
			if numBoxes<8:
				newValue = numBoxes+1
				world.totalBlocks = world.totalBlocks + 1 
				world.canvas.itemconfigure(world.dropOffId[i],text=newValue)
				self.block=False
				world.canvas.itemconfigure(self.id,text="A")
				self.bankAccount += pickUpDropOffReward
	#returns new state but, with no changing agent location
	def new_State_Creator(self,action):
		if action == 'P' or action == 'D':
			return self.x,self.y
		elif action == 'N':
			return self.x,self.y-1
		elif action == 'S':
			return self.x,self.y+1
		elif action == 'W':
			return self.x-1,self.y
		elif action == 'E':
			return self.x+1,self.y

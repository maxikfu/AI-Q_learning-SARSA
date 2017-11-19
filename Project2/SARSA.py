import pandas as pd
import numpy as np
import random

class SARSA():
	def __init__(self,alp,gam):
		#here we will create q tables for all states...
		rows = []
		self.alpha = alp
		self.gamma = gam
		self.pickUpDropOffReward = 12
		self.moveReward = -1
		for i in range(5):
			for j in range(5):
				rows.append(str(i+1)+str(j+1))
		self.q_table_block = pd.DataFrame(0,index = rows,columns = ['N','S','E','W','P','D'],dtype=np.float64)
		self.q_table_nonBlock = pd.DataFrame(0,index = rows,columns = ['N','S','E','W','P','D'],dtype=np.float64)
	#returns max Q value from all available actions in next state
	#returns max value and column with max value pics random for the same values
	def max_q_fromactions(self,actions,state,block):
		if block:
			maxValue = max(self.q_table_block.ix[state,actions])
			maxAction = random.sample([act for act in actions if self.q_table_block.ix[state,act] == maxValue],1).pop()
			return [maxValue, maxAction]
		else:
			maxValue = max (self.q_table_nonBlock.ix[state,actions])
			maxAction = random.sample([act for act in actions if self.q_table_nonBlock.ix[state,act] == maxValue],1).pop()
			return [maxValue, maxAction]
	def PRANDOM(self,world,x,y,block):
		availableActions = world.availableAct(x,y,block)
		if 'P' in availableActions:
			return 'P'
		elif 'D' in availableActions:
			return 'D'
		else:
			return random.sample(availableActions,1).pop()
	def acceptingLowerQValue(slef,availableActions,maxValueAction):
		r = random.random()
		if 0.85 >= r:
			return maxValueAction
		else:
			availableActions.remove(maxValueAction)
			action = random.sample(availableActions,1).pop()
			return action
	def PEPLOIT(self,world,x,y,block):
		availableActions = world.availableAct(x,y,block)
		if 'P' in availableActions:
			return 'P'
		elif 'D' in availableActions:
			return 'D'
		else:
			currentState = str(x)+str(y)
			maxValue, maxValueAction = self.max_q_fromactions(availableActions,currentState,block)
			chooseAction=self.acceptingLowerQValue(availableActions,maxValueAction)
			return chooseAction
	def sarsa_learning_process(self,world,agent,policy,action):
		currentState = str(agent.x)+str(agent.y)
		if action == 'P':
			reward = self.pickUpDropOffReward
			block = True
		elif action == 'D':
			reward = self.pickUpDropOffReward
			block = False
		else:
			reward = self.moveReward
			block = agent.block
		newStateX,newStateY = agent.new_State_Creator(action)
		if policy == 'PRANDOM':
			actionInNewState = self.PRANDOM(world,newStateX,newStateY,block)
		else:
			actionInNewState = self.PEPLOIT(world,newStateX,newStateY,block)
		new_State = str(newStateX)+str(newStateY)
		if block:
			res = self.q_table_block.ix[new_State,actionInNewState]
		else:
			res = self.q_table_nonBlock.ix[new_State,actionInNewState]
		if agent.block:
			self.q_table_block.ix[currentState,action] = self.q_table_block.ix[currentState,action]+self.alpha*(reward+self.gamma*res-self.q_table_block.ix[currentState,action])
		else:
			self.q_table_nonBlock.ix[currentState,action] = self.q_table_nonBlock.ix[currentState,action]+self.alpha*(reward+self.gamma*res-self.q_table_nonBlock.ix[currentState,action])
		#make a move
		if action == 'P':
			agent.PickUp(world)
		elif action == 'D':
			agent.DropOff(world)
		elif action == 'N':
			agent.North(world)
		elif action == 'S':
			agent.South(world)
		elif action == 'W':
			agent.West(world)
		else:
			agent.East(world)
		return actionInNewState
import pandas as pd
import numpy as np
import random

#Q learning with 2 q tables and all learning algorithms I guess...
class Q_learning:
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
	def max_q_fromactions(self,actions,state,block,agent):
		if block:
			maxValue = max(self.q_table_block.ix[state,actions])
			maxAction = random.sample([act for act in actions if self.q_table_block.ix[state,act] == maxValue],1).pop()
			return [maxValue, maxAction]
		else:
			maxValue = max (self.q_table_nonBlock.ix[state,actions])
			maxAction = random.sample([act for act in actions if self.q_table_nonBlock.ix[state,act] == maxValue],1).pop()
			return [maxValue, maxAction]
	#learning process'

	def q_learning_process(self,action,world,agent):
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
		availableActionsInNewState = world.availableAct(newStateX,newStateY,agent.block)
		res = self.max_q_fromactions(availableActionsInNewState,str(newStateX)+str(newStateY),block,agent)[0]
		
		if agent.block:
			self.q_table_block.ix[currentState,action] = (1-self.alpha)*self.q_table_block.ix[currentState,action]+self.alpha*(reward+self.gamma*res)
		else:
			self.q_table_nonBlock.ix[currentState,action] = (1-self.alpha)*self.q_table_nonBlock.ix[currentState,action]+self.alpha*(reward+self.gamma*res)

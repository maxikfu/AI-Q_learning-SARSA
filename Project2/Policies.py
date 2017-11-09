import random

#contains policyes what will return next action
class Policy:
	def PRANDOM(self,world,agent,q_learning):
		actionList=[]
		if world.isPickUpLocationApplicable(agent):
			#apply pick up operator
			q_learning.q_learning_process('P',world,agent)
			agent.PickUp(world)
		elif world.isDropOffLocationApplicable(agent):
			#apply drop off operator
			q_learning.q_learning_process('D',world,agent)
			agent.DropOff(world)
		else:
			if world.isNorthApplicable(agent):
				actionList.append("N")
			if world.isSouthApplicable(agent):
				actionList.append("S")
			if world.isEastApplicable(agent):
				actionList.append("E")
			if world.isWestApplicable(agent):
				actionList.append("W")
			action=random.sample(actionList,1).pop()
			if action == "N":
				q_learning.q_learning_process('N',world,agent)
				agent.North(world)
			elif action == "S":
				q_learning.q_learning_process('S',world,agent)
				agent.South(world)
			elif action == "W":
				q_learning.q_learning_process('W',world,agent)
				agent.West(world)
			else:
				q_learning.q_learning_process('E',world,agent)
				agent.East(world)

	def PEPLOIT():
		return None
	def PGREEDY(self,world,agent,q_learning):#choose move with bigger q value
		#actionList=[]
		if world.isPickUpLocationApplicable(agent):
			#apply pick up operator
			q_learning.q_learning_process('P',world,agent)
			agent.PickUp(world)
		elif world.isDropOffLocationApplicable(agent):
			#apply drop off operator
			q_learning.q_learning_process('D',world,agent)
			agent.DropOff(world)
		else:# choose action with highest Q value
			#need to get available actions in this state
			actionList = world.availableActions(agent)
			#print(actionList)
			currentState = str(agent.x)+str(agent.y)
			maxValue, maxValueAction = q_learning.max_q_fromactions(actionList,currentState,agent.block,agent)
			#print(maxValueAction, maxValue)
			q_learning.q_learning_process(maxValueAction,world,agent) #computng Q value for current state and putting it in the tables
			if maxValueAction == "N": #we just move agent in new location
				agent.North(world)
			elif maxValueAction == "S":
				agent.South(world)
			elif maxValueAction == "W":
				agent.West(world)
			else:
				agent.East(world)
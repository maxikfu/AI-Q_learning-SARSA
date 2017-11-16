from AgentOperators import Agent 
from Environment import *
from Policies import *
from Q_Learning import *
from Q_Table import *
import time



world = World()
policy = Policy()
agent = Agent(world)
q_learning = Q_learning(0.3,0.5)
q_table_visual_not_block = Q_Table("Q table NOT carrying Block")
q_table_visual_block = Q_Table("Q table IS carrying Block")
result = False
start_time = time.time()
orig_stdout = sys.stdout
fout = open('Stat.txt', 'w')
sys.stdout = fout
iteration = 1
stepsToFinish = 0
totalSteps = 0
while not result and totalSteps <=6000:
	if totalSteps == 3000:
		print("Totoal steps reached 3000. Printing mid Q tables in files")
		fo = open('Ex1Mid_Q_table_NO_BLOCK.txt', 'w')
		sys.stdout = fo
		print(q_learning.q_table_nonBlock)
		fo.close()
		fo = open('Ex1Mid_Q_table_BLOCK.txt', 'w')
		sys.stdout = fo
		print(q_learning.q_table_block)
		fo.close()
		sys.stdout = fout
		world.reset(agent)
		iteration+=1
		world.totalBlocks=0
		agent.bankAccount = 0
		stepsToFinish = 0
		world.root.update()
		runningTime= time.time() - start_time
		#time.sleep(20)
	if totalSteps <3000 :
		policy.PRANDOM(world,agent,q_learning)
	else:
		#time.sleep(10)
		policy.PGREEDY(world,agent,q_learning)
	#policy.PEPLOIT(world,agent,q_learning)
	world.root.update()
	q_table_visual_not_block.updateValues(q_learning.q_table_nonBlock)
	q_table_visual_not_block.qTable.update()
	q_table_visual_block.updateValues(q_learning.q_table_block)
	q_table_visual_block.qTable.update()
	stepsToFinish += 1
	totalSteps+=1
	if world.totalBlocks== 16:
		#result = True	
		world.reset(agent)
		runningTime= time.time() - start_time
		print("Iteration number:"+ str(iteration) +  " Steps taken to complite  " + str(stepsToFinish)+" Time running = "+str(runningTime)+ " bankAccount = "+str(agent.bankAccount))
		iteration+=1
		start_time = time.time()
		world.totalBlocks=0
		agent.bankAccount = 0
		stepsToFinish = 0
		world.root.update()
		#time.sleep(3)
fout.close()
fout = open('Ex1Final_Q_table_NO_BLOCK.txt', 'w')
sys.stdout = fout
print(q_learning.q_table_nonBlock)
fout.close()
fout = open('Ex1Final_Q_table_BLOCK.txt', 'w')
sys.stdout = fout
print(q_learning.q_table_block)
fout.close()
world.root.mainloop()


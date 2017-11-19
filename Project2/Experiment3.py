from AgentOperators import Agent 
from Environment import *
from Policies import *
from SARSA import *
from Q_Table import *
import time
import io
from PIL import Image


world = World()
agent = Agent(world)
sarsa = SARSA(0.3,0.5)
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
policy = 'PRANDOM'
action = sarsa.PRANDOM(world,agent.x,agent.y,agent.block)
while not result and totalSteps <=6000:
	if totalSteps == 200:
		print("Totoal steps reached 3000. Printing mid Q tables in files")
		ps=q_table_visual_not_block.qTableCanvas.postscript(colormode='color')
		img = Image.open(io.BytesIO(ps.encode('utf-8')))
		img.save('MidNonBlock.png',"png",quality=99)
		fo = open('Mid_Q_table_NO_BLOCK.txt', 'w')
		sys.stdout = fo
		print(sarsa.q_table_nonBlock)
		fo.close()
		fo = open('Mid_Q_table_BLOCK.txt', 'w')
		ps=q_table_visual_block.qTableCanvas.postscript(colormode='color')
		img = Image.open(io.BytesIO(ps.encode('utf-8')))
		img.save('MidBlock.png',"png",quality=99)
		sys.stdout = fo
		print(sarsa.q_table_block)
		fo.close()
		sys.stdout = fout
		world.root.update()
		runningTime= time.time() - start_time
		policy = 'PEPLOIT'
	action = sarsa.sarsa_learning_process(world,agent,policy,action)
	world.root.update()
	q_table_visual_not_block.updateValues(sarsa.q_table_nonBlock)
	q_table_visual_not_block.qTable.update()
	q_table_visual_block.updateValues(sarsa.q_table_block)
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
		action = sarsa.PEPLOIT(world,agent.x,agent.y,agent.block)
		world.root.update()
		#time.sleep(3)
fout.close()
fout = open('Final_Q_table_NO_BLOCK.txt', 'w')
ps=q_table_visual_not_block.qTableCanvas.postscript(colormode='color')
img = Image.open(io.BytesIO(ps.encode('utf-8')))
img.save('FinalNONBlock.png',"png",quality=99)
sys.stdout = fout
print(sarsa.q_table_nonBlock)
fout.close()
fout = open('Final_Q_table_BLOCK.txt', 'w')
ps=q_table_visual_block.qTableCanvas.postscript(colormode='color')
img = Image.open(io.BytesIO(ps.encode('utf-8')))
img.save('FinalBlock.png',"png",quality=99)
sys.stdout = fout
print(sarsa.q_table_block)
fout.close()


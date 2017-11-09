from AgentOperators import Agent 
from Environment import *
from Policies import *
from Q_Learning import *
from Q_Table import *

world = World()
policy = Policy()
agent = Agent(world)
q_learning = Q_learning()
q_table_visual_not_block = Q_Table("Q table NOT carrying Block")
q_table_visual_block = Q_Table("Q table IS carrying Block")
result = False
while not result:
	time.sleep(0.1)
	#policy.PRANDOM(world,agent,q_learning)
	policy.PGREEDY(world,agent,q_learning)
	world.root.update()
	q_table_visual_not_block.updateValues(q_learning.q_table_nonBlock)
	q_table_visual_not_block.qTable.update()
	q_table_visual_block.updateValues(q_learning.q_table_block)
	q_table_visual_block.qTable.update()
	if world.totalBlocks== 16:
		world.reset(agent)
		world.root.update()
		time.sleep(3)

print(agent.bankAccount)
#print(q_learning.q_table_nonBlock)
#print(q_learning.q_table_block)
#world.after(100,do_one_frame) 
world.root.mainloop()
#q_table_visual.qTable.mainloop()

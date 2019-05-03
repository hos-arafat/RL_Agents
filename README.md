The project should be organized in the following folder structure:
Arafat (main project folder)
|
|--------lib
|          |plotting.py
|	   |simulation.py
|          |envs
|            |simple_rooms.py
|            |windy_gridworld.py
|	     |cliff_walking.py
|--------experiments.py
|--------sarsa_agent.py
|--------Q_learning_agent.py
|--------README.txt
_________________________________________________________________________________________________________________________________________________
The project requires the following libraries:
Gym
Numpy
Pandas
Matplotlib
__________________________________________________________________________________________________________________________________________________
The main file to run is experiments.py. It is located in the Arafat_1803850_RL_Project (main project folder) folder

Required arguments:

'--interactive': 'Set it to 'True' to render and see the agent while it learns and acts in the environment (Not required. Default value of False)

'--env': Environment to run the agent on (required). Three environments are available: - Simple Gridworld
										       - Windy Gridworld
										       - Cliff Walking
legal values for the --env argument: 
    For the Cliff Walking Env : "cliffwalking" "cliffwalkingenv"     "cliff"      "cliffs"     
    For the Windy Gridworld Env : "windygridworld"  "windygridworldenv"     "windygrid"    "windy"     
    For the Simple Gridworld Env : "simplemaze" "simplegrid" "simplegridworld" "simplegridworldenv" "simpleroomsenv"  "simpleroom"  "maze"  "grid"

'--agent':Type of Agent Algorithm to execute (required). Two algorithms are available: - SARSA
									      	       - Q Learning
legal values for the --env argument: 
	For the SARSA Agent      >> any string that starts with an "S" (or "s")
	For the Q Learning Agent >> any string that stars with "Q" (or "q")

'--iter': Number of iterations to run the algorithm for (required integer)

'--epsilon': Value of exploration probability Epsilon (Not required float. Default value of 0.9)

'--alpha' : Value for the learning rate Alpha (Not required float. Default value of 0.5)

'--decay' : How often / the number of time steps after which Epsilon is decayed (Not required integer. Default value of 50)
_____________________________________________________________________________________________________________________________________________________
Example Usage:
##############
Interactive mode of the Sarsa agent on the Simple Girdworld environment for 20 iterations
 python experiments.py --env=grid --interactive=True --agent=s --iter=20 --epsilon=0.9 --alpha=0.5 --decay=30

Non-Interactive mode of the Q Learning agent on the Cliff Walking environment for 340 iterations
 python experiments.py --env=cliff --agent=q --iter=340 --epsilon=0.7 --alpha=0.5 --decay=30

Non-Interactive mode of the SARSA agent on the Cliff Walking environment for 200 iterations
 python experiments.py --env=wind --agent=sarsa --iter=200 --epsilon=1.0 --alpha=0.5 --decay=30

Results in the Report can be replicated using the following commands:
######################################################################
python experiments.py --env=CliffWalking --agent=sarsa --iter=1000 --epsilon=0.9 --alpha=0.5 --decay=30
python experiments.py --env=CliffWalking --agent=q --iter=1000 --epsilon=0.7 --alpha=0.5 --decay=30
----------------------------------------------------------------------------------------------------------
python experiments.py --env=Windy Gridworld --agent=q --iter=1000 --epsilon=0.9 --alpha=0.5 --decay=30
python experiments.py --env=Windy Gridworld --agent=sarsa --iter=2000 --epsilon=0.9 --alpha=0.5 --decay=30



______________________________________________________________________________________________________________________________________________________
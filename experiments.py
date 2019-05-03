import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse

if "../" not in sys.path:
    sys.path.append("../")

import gym

from lib.envs.simple_rooms import SimpleRoomsEnv
from lib.envs.windy_gridworld import WindyGridworldEnv
from lib.envs.cliff_walking import CliffWalkingEnv
from lib.simulation import Experiment

from sarsa_agent import SarsaAgent
from Q_learning_agent import QLearningAgent

parser = argparse.ArgumentParser(description='Apply masks to video using MaskRCNN')
parser.add_argument('--interactive', dest='interactive', type=bool, default=False, help='Set to \'True\' to render the agent while it learns')
parser.add_argument('--env', dest='env', type=str, help='Environment to run the agent on', required=True)
parser.add_argument('--agent', dest='agent', type=str, help='Type of Agent Algorithm', required=True)
parser.add_argument('--iter', dest='iter', type=int, default=100, help='Number of iterations', required=True)
parser.add_argument('--epsilon', dest='epsilon', type=float, default=0.9, help='Value for Epsilon')
parser.add_argument('--alpha', dest='alpha', type=float, default=0.5, help='Value for Alpha')
parser.add_argument('--decay', dest='decay', type=int, default=50, help='How often to decay Epsilon')

args = parser.parse_args()
interactive = args.interactive
env_string = args.env.lower().replace(" ", "")
agent_string = args.agent.lower().replace(" ", "")
num_iter = args.iter
epsilon = args.epsilon
alpha = args.alpha
decay = args.decay


def get_env(argument):
    switcher = {
    "cliffwalking": CliffWalkingEnv(),
    "cliffwalkingenv": CliffWalkingEnv(),
    "cliff" : CliffWalkingEnv(),
    "cliffs": CliffWalkingEnv(),
    "windygridworld": WindyGridworldEnv(),
    "windygridworldenv": WindyGridworldEnv(),
    "windygrid": WindyGridworldEnv(),
    "windy": WindyGridworldEnv(),
    "simplemaze": SimpleRoomsEnv(),
    "simplegrid": SimpleRoomsEnv(),
    "simplegridworld": SimpleRoomsEnv(),
    "simplegridworldenv": SimpleRoomsEnv(),
    "simpleroomsenv": SimpleRoomsEnv(),
    "simpleroom": SimpleRoomsEnv(),
    "maze": SimpleRoomsEnv(),
    "grid": SimpleRoomsEnv()
    }
    return switcher.get(argument)

env = get_env(env_string)

if agent_string.startswith('q'):
    print("Running Q Learning on {} environment for {} epochs".format(env_string, num_iter))
    agent = QLearningAgent(range(env.action_space.n), epsilon=epsilon, alpha = alpha, decay_every=decay)
    experiment = Experiment(env, agent)
    experiment.run_qlearning(num_iter, interactive)
    #print("Running Q Learning")
elif agent_string.startswith('s'):
    print("Running SARSA on {} environment for {} epochs".format(env_string, num_iter))
    agent = SarsaAgent(range(env.action_space.n), epsilon=epsilon, alpha = alpha, decay_every=decay)
    experiment = Experiment(env, agent)
    experiment.run_sarsa(num_iter, interactive)
    #print("Running SARSA")

else:
    print("Invalid Agent argument")

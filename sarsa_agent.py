import numpy as np
import sys

if "../" not in sys.path:
    sys.path.append("../")

from lib.envs.simple_rooms import SimpleRoomsEnv
from lib.envs.windy_gridworld import WindyGridworldEnv
from lib.envs.cliff_walking import CliffWalkingEnv
from lib.simulation import Experiment


from collections import defaultdict


class Agent(object):

    def __init__(self, actions):
        self.actions = actions
        self.num_actions = len(actions)

    def act(self, state):
        raise NotImplementedError


class SarsaAgent(Agent):

    def __init__(self, actions, epsilon=0.9, decay_every=100, alpha=0.5, gamma=0.99):
        super(SarsaAgent, self).__init__(actions)

        ## Initialize empty Q value dictionary here
        ## In addition, initialize the value of epsilon, alpha and gamma
        self.q_value = defaultdict(lambda: np.zeros(len(actions)))

        self.epsilon = epsilon
        if self.epsilon >= 0.5:
            self.epsilon_decay = True
        else:
            self.epsilon_decay = False

        self.step_counter = 0
        self.decay_every = decay_every

        self.alpha = alpha
        self.gamma = gamma

    def stateToString(self, state):
        mystring = ""
        if np.isscalar(state):
            mystring = str(state)
        else:
            for digit in state:
                mystring += str(digit)
        return mystring

    def act(self, state):
        stateStr = self.stateToString(state)
        self.step_counter += 1
        if self.epsilon_decay:
            if self.step_counter % self.decay_every == 0:
                self.epsilon = max(.01, self.epsilon * .98)
        ## Implement epsilon greedy policy her
        if np.random.random() < self.epsilon:
            action = np.random.randint(0,len(self.actions))
        else:
            action = np.argmax(self.q_value[stateStr])

        return action

    def learn(self, state1, action1, reward, state2, action2):
        state1Str = self.stateToString(state1)
        state2Str = self.stateToString(state2)

        ## Implement the sarsa update here
        td_target = reward + self.gamma * self.q_value[state2Str][action2]
        td_delta = td_target - self.q_value[state1Str][action1]
        self.q_value[state1Str][action1] += self.alpha * td_delta
        """
        SARSA Update
        Q(s,a) <- Q(s,a) + alpha * (reward + gamma * Q(s',a') - Q(s,a))
        or
        Q(s,a) <- Q(s,a) + alpha * (td_target - Q(s,a))
        or
        Q(s,a) <- Q(s,a) + alpha * td_delta
        """

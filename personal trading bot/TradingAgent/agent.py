#This file contains the AI Agent
import numpy as np
import random
from collections import defaultdict
class Agent:
    def __init__(self, nA=3, alpha=0.1, gamma=1, eps=1.0, state_size=(2, 2, 2, 2), state_actions_size=(3,)):
        #TODO innit
        self.gamma = gamma
        self.alpha = alpha
        self.nA = nA
        self.state_size = state_size
        self.state_actions_size = state_actions_size
        self.Q = np.zeros(shape=state_size + state_actions_size)
        self.eps = eps

    def select_action(self, state):
        #TODO implement buy, hold or sell using expected sarsa
        if self.eps > random.random(): #to verify
            action = np.random.choice(self.nA)
        else:
            action = np.argmax(self.Q[state])  # mine #trying to implement Q-learning

        return action

    def step(self, state, action, next_state, reward, done):
        #TODO update the Q-table and assign next state
        if not done:
            current = self.Q[state][action]  # estimate in Q-table (for current state, action pair)
            policy_s = np.ones(self.nA) * self.eps / self.nA  # current policy (for next state S')
            policy_s[np.argmax(self.Q[next_state])] = 1 - self.eps + (self.eps / self.nA)  # greedy action
            Qsa_next = np.dot(self.Q[next_state], policy_s)  # get value of state at next time step
            target = reward + (self.gamma * Qsa_next)  # construct target
            # print(np.max(self.Q[next_state]))
            # target = reward + self.gamma*np.max(self.Q[next_state])
            self.Q[state][action] = self.Q[state][action] + self.alpha * (target - self.Q[state][action])

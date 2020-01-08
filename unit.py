'''
The Unit class is responsible for:
	-Updating the individual unit
		-Making decisions
		-Moving/rotating
'''

import numpy as np
import random
import math
from neural_network import NeuralNetwork


class Unit:
	def __init__(self, position, weights1=np.random.rand(10,8), weights2=np.random.rand(8,4)):
		self.brain = NeuralNetwork(weights1, weights2)
		self.position = position

		self.hunger_decrease = 0.5
		self.health_decease = 10
		self.health_increase = 10

		self.max_hunger = 100
		self.max_health = 100

		self.starvation_limit = 50
		self.health_gain_limit = 75

		self.health = self.max_health
		self.hunger = self.max_hunger

		self.score = 0
		self.alive = True


	def __lt__(self, other): #Used for sorting the units after the best scores
		return self.score < other.score


	def update(self, inputs):
		#res = self.brain.think(inputs) #Make a disition using the Neural network

		# Move according to the neural networka result

		self.hunger -= self.hunger_decrease

		if self.hunger > self.health_gain_limit and self.health < self.max_health:
			self.health += self.health_increase # Gain health if not starving
		elif self.hunger <= 0:
			self.health -= self.health_decease # Loose health if hunger is less than zero

		if self.health <= 0:
			self.die()

	
	def die(self):
		self.alive = False


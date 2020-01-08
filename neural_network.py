'''
The NeuralNetwork class is only responsible for calculating an output from the given inputs
'''

import numpy as np


class NeuralNetwork:

	def __init__(self, weights1, weights2):
		self.weights1 = weights1
		self.weights2 = weights2


	@staticmethod
	def sigmoid(x):
		return 1 / (1 + np.exp(-x))


	#1. Calculate the dot product of the input matrix and the first weights matrix
		#Meaning to multiply each row in the first matrix with each column in the second matrix and summarizing all the factors
		#By doing this each value in the input matrix will affect the ouput value depending on its corresponding weight
		#This will also shrink the matricies from [A, B] & [B, C] to [A, C]

	#2. Pass the resulting matrix through an "activation function", in this case the sigmoid functino
		#This scales all the values in the given matrix between 0 and 1
		
	#3. Repeat these two steps for the second layer of weights resulting in a single value

	def think(self, a):
		layer1 = NeuralNetwork.sigmoid(np.dot(a, self.weights1))
		return NeuralNetwork.sigmoid(np.dot(layer1, self.weights2))



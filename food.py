'''
The FoodManager class is responsible for:
	-Keeping a reference to all current food
	-Spawning new food
	-Deals with pickups
'''

from game_math import dist_between
import random


class Food:
	def __init__(self, position):
		self.position = position

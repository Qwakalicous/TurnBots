'''
The Generation class is responsible for:
	-Keeping a reference to all current units
	-Checking for collisions with enemies
	-Creating new generations (both random and from parent generations)
'''

import random
import numpy as np
from game_math import dist_between
from unit import Unit


class GenerationManager:
	def __init__(self, game, population_size):
		self.game = game
		self.population_size = population_size
		#self.previous_generation = None
		self.current_generation = self.create_random_generation()
		

	# Move each unit
	def update_units(self):
		for i in reversed(range(len(self.current_generation.units))):
			unit = self.current_generation.units[i]
			if unit.alive:
				sub_mat  = self.game.grid.get_sub_matrix(unit.position[0] - 1, unit.position[1] - 1, 3, 3).as_list() # Get a sub matrix of the surrounding 3x3 matrix
				surrounding_tiles = surrounding_tiles[:4] + surrounding_tiles[5:] # Removes its own position from the list of tiles

				inputs = surrounding_tiles + [unit.health, unit.hunger]
				unit.update(inputs)


	def create_random_generation(self):
		return Generation([self.create_random_unit() for _ in range(self.population_size)])


	def create_child_generation(self, parent_generation):
		#self.previous_generation = self.parent_generation #Store previous generation just in case

		ranked_old_units = parent_generation.units.sort() #Sort them based on their score to get the best candidates

		new_units = []
		for i in range(self.population_size):
			new_pos = [random.randint(0, self.game.screen_size[0]), random.randint(0, self.game.screen_size[1])]
			new_weights1 = random_weights_variation(ranked_old_units[random.randint(0, 2)].weights1) #Get the weights of a random top 3 unit from the old generation
			new_weights2 = random_weights_variation(ranked_old_units[random.randint(0, 2)].weights2)
			
			new_units.append(Unit(new_pos, new_weights1, new_weights2))

		return Generation(new_units)


	def create_random_unit(self):
		taken_pos = []
		
		new_pos = [random.randint(0, self.game.grid_size),
					random.randint(0, self.game.grid_size)]
		return Unit(new_pos)


	def random_weights_variation(self, old_weights):
		new_weights = old_weights.copy()

		for i in range(new_weights.shape[0]):
			for j in range(new_weights.shape[1]):
				if random.randint(0, 10) <= 0: #10% chance of "mutation"
					new_weights[i][j] *= (random.random() - 0.5)
					
		return new_weights			


			
class Generation:
	def __init__(self, units):
		self.units = units
#		self.overall_score = 0

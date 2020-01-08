'''
The Game class is responsible for:
	-Controlling the game
	-Rendering all entities
	-Handeling user inputs
'''

import random
import pygame
import math
from generation import GenerationManager
from food import Food
from unit import Unit
from game_math import Matrix


class Game:
	def __init__(self):
		self.grid_size = 20
		self.tile_size = 30
		self.margin = 10

		self.grid = Matrix.create_none_matrix(self.grid_size, self.grid_size)
		
		pygame.init()	
		self.screen = pygame.display.set_mode((self.grid_size * self.tile_size + self.margin * 2 + 200, self.grid_size * self.tile_size + self.margin * 2))

		self.food_count = 15
		
		self.foods = [Food([random.randint(0, self.grid_size), random.randint(0, self.grid_size)]) for _ in range(self.food_count)]
		self.generation_manager = GenerationManager(self, population_size=20)


	def run_game(self):
		done = False
		clock = pygame.time.Clock()

		while not done: #Game loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						done = True
			# GAME LOGIC
			self.generation_manager.update_units()

			# RENDERING
			self.screen.fill((0, 0, 0)) # Reset screen (fill black)

			self.draw_food()
			self.draw_units()
			self.draw_grid()

			pygame.display.flip()
			clock.tick(60)

			#Get user input to move on to next turn
			input("Press [Enter] to move on")


	def draw_units(self):
		for unit in self.generation_manager.current_generation.units:
			color = (0, 0, 255) if unit.alive else (0, 0, 100)
			draw_pos = [unit.position[i] * self.tile_size + self.margin for i in range(len(unit.position))]
			pygame.draw.circle(self.screen, color, draw_pos, 8) # Draw the units


	def draw_food(self):
		for food in self.foods:
			draw_pos = [food.position[i] * self.tile_size + self.margin for i in range(len(food.position))]
			pygame.draw.circle(self.screen, (255, 0, 0), tuple(draw_pos), 8) # Draw the food
		

	def draw_grid(self):
		for i in range(self.grid_size + 2):
			color = (150, 150, 150) if i != self.grid_size + 1 else (255, 255, 255)

			pygame.draw.line(self.screen, color, (i * self.tile_size, 0), (i * self.tile_size, self.grid_size * self.tile_size))
			pygame.draw.line(self.screen, color, (0, i * self.tile_size), (self.grid_size * self.tile_size, i * self.tile_size))



if __name__ == "__main__":
	game = Game()
	game.run_game()

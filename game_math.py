import math
import random


def dist_between(a, b):
	return math.sqrt((a.position[0] - b.position[0]) ** 2 + (a.position[1] - b.position[1]) ** 2)



class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix


	def __repr__(self):
		res = "Matrix of dimension [{0}, {1}]\n".format(self.get_rows(), self.get_cols())
		for i in range(self.get_rows()):
			res += str(self.matrix[i]) + "\n"
		return res


	def get_cols(self):
		return len(self.matrix[0])


	def get_rows(self):
		return len(self.matrix)


	def get_sub_matrix(self, row_index, col_index, rows, cols):
		return Matrix([[self.matrix[row_index + j][col_index + i] for i in range(cols)] for j in range(rows)])


	def get_element(self, row, col):
		return self.matrix[row][col]


	def as_list(self):
		res = []
		for row in range(self.get_rows()):
			for col in range(self.get_cols()):
				res.append(self.get_element(row, col))
		return res


	@staticmethod
	def create_none_matrix(rows, cols):
		return Matrix([[None for i in range(cols)] for j in range(rows)])


	@staticmethod
	def create_random_matrix(rows, cols):
		return Matrix([[random.random() for i in range(cols)] for j in range(rows)])

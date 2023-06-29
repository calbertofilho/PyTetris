import pygame
from Classes.colors import Colors

class Grid:
	def __init__(self):
		self.rows = 20
		self.cols = 10
		self.size = 30
		self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
		self.colors = Colors.get_cell_colors()

	# Só para teste
	def print_grid(self):
		'''Função que testa a criação do modelo de grade para o jpgp'''
		for row in range(self.rows):
			for column in range(self.cols):
				print(self.grid[row][column], end = " ")
			print()

	def draw(self, screen):
		for row in range(self.rows):
			for column in range(self.cols):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(column * self.size + 1, row * self.size + 1, self.size - 1, self.size - 1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

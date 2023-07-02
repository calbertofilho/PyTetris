from Classes.colors import Colors
from Classes.position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.state = 0
        self.colors = Colors.get_cell_colors()

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.size, self.size - 1, self.size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

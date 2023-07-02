import pygame
from Classes.colors import Colors
from Classes.position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.state += 1
        if self.state == len(self.cells):
             self.state = 0

    def undo_rotation(self):
        self.state -= 1
        if self.state == -1:
            self.state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.size, offset_y + tile.row * self.size, self.size - 1, self.size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

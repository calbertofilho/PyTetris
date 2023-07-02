import pygame, os, random
from Classes.grid import Grid
from Classes.Blocks.i_block import I_Block
from Classes.Blocks.j_block import J_Block
from Classes.Blocks.l_block import L_Block
from Classes.Blocks.o_block import O_Block
from Classes.Blocks.s_block import S_Block
from Classes.Blocks.t_block import T_Block
from Classes.Blocks.z_block import Z_Block

class Game:
	def __init__(self):
		self.grid = Grid()
		self.blocks = [I_Block(), J_Block(), L_Block(), O_Block(), S_Block(), T_Block(), Z_Block()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()

		self.game_over = False
		self.score = 0

		self.main_theme = pygame.mixer.Sound(os.path.join(os.getcwd(), 'Assets/sounds/theme.wav'))
		self.rotate_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'Assets/sounds/rotate.wav'))
		self.clear_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'Assets/sounds/clear.wav'))
		self.success_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'Assets/sounds/success.wav'))

		self.main_theme.play(-1)

	def get_random_block(self):
		if len(self.blocks) == 0:
			self.blocks = [I_Block(), J_Block(), L_Block(), O_Block(), S_Block(), T_Block(), Z_Block()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	def draw(self, screen):
		self.grid.draw(screen)
		self.current_block.draw(screen,0,0)

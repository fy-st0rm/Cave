import pygame, sys, random

from light import *
from Player import *
from Map_generator import *
from Inventory import *


class Game:
	def __init__(self):
		self.loop = True

		# Some fps stuff
		self.clock = pygame.time.Clock()
		self.fps = 60
		self.font = pygame.font.Font(os.path.join("res/UI/Font/FFFFORWA.TTF"),10)

		# Player
		self.player = Player(display, pygame.Rect(50, 50, 16, 16))

		# Map generator
		self.map_generator = Map(display)

		# Camera
		self.scroll = [0, 0]

		# Light
		self.light = Light(display)
    
		# Inventory things
		self.invent_x = DISPLAY_SIZE[0]/7#Back Ground image locationX
		self.invent_y = DISPLAY_SIZE[1]/7#Back Ground imgae locattionY

		self.inventory = Inventory(display, self.font, self.invent_x, self.invent_y)
		
	def __event(self):
		# Main game event system
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				self.loop = False

			self.inventory.event(event)
			self.player.event(event)
			
	def __display_fps(self):
		# Function to show fps
		fps = self.font.render(str(int(self.clock.get_fps())), True, (255, 255, 255))
		display.blit(fps, (10, 10))

	def __renders(self):
		# Everthing to draw here:

		# Rendering map
		tile_rects = []		# The variable thats stores the hitbox info of walls
		self.map_generator.generate_terrain(tile_rects, self.scroll)
		
		# Rendering player
		self.player.draw(self.scroll, tile_rects, self.map_generator.game_map)

		# Rendering light
		lightX = (self.player.rect.x + (self.player.rect.w/2)) -self.scroll[0]
		lightY = (self.player.rect.y + (self.player.rect.h/2))-self.scroll[1]
		self.light.draw([lightX, lightY])

		# Rendering inventory
		self.inventory.draw()

		self.__display_fps()

	def run(self):
		# Main Game loop:
		while self.loop:

			self.clock.tick(self.fps)
			display.fill(pygame.Color("lightblue"))

			self.__event()

			# Camera actions
			self.scroll[0] += (self.player.rect.x - self.scroll[0] - DISPLAY_SIZE[0] / 2) / 10
			self.scroll[1] += (self.player.rect.y - self.scroll[1] - DISPLAY_SIZE[1] / 2) / 10

			self.__renders()

			screen.blit(pygame.transform.scale(display, WIN_SIZE), (0, 0))
			pygame.display.update()



if __name__ == "__main__":

	pygame.init()

	WIN_SIZE = (800, 600)
	DISPLAY_SIZE = (300, 188)
	screen = pygame.display.set_mode(WIN_SIZE)
	pygame.display.set_caption("Cave")

	display = pygame.Surface(DISPLAY_SIZE)

	game = Game()
	game.run()


		

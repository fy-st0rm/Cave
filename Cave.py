import pygame
from light import *


class Game:
	def __init__(self):
		self.loop = True

		self.clock = pygame.time.Clock()
		self.fps = 60

	def __event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.loop = False

			self.light.event(event)

	def run(self):
		while self.loop:
			self.clock.tick(self.fps)
			display.fill(pygame.Color("lightblue"))

			self.__event()

			screen.blit(pygame.transform.scale(display, WIN_SIZE), (0, 0))
			pygame.display.update()


if __name__ == "__main__":
	pygame.init()

	WIN_SIZE = (800, 600)
	screen = pygame.display.set_mode(WIN_SIZE)
	pygame.display.set_caption("The Glowing One")

	display = pygame.Surface((400, 288))

	game = Game()
	game.run()



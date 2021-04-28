import pygame

from light import *
from Player import *


class Game:
	def __init__(self):
		self.loop = True

		self.clock = pygame.time.Clock()
		self.fps = 60

		self.player = Player(display, pygame.Rect(50, 50, 16, 16))

		# Camera
		self.scroll = [0, 0]

	def __event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.loop = False

			self.player.event(event)

	def run(self):
		x,y = 50,50
		while self.loop:
			self.clock.tick(self.fps)
			display.fill(pygame.Color("lightblue"))

			self.__event()

			self.scroll[0] += (self.player.rect.x - self.scroll[0] - DISPLAY_SIZE[0] / 2) / 10
			self.scroll[1] += (self.player.rect.y - self.scroll[1] - DISPLAY_SIZE[1] / 2) / 10

			self.player.draw(self.scroll)

			pygame.draw.rect(display, (0, 255, 0), [x-self.scroll[0], y-self.scroll[1], 50, 20])

			screen.blit(pygame.transform.scale(display, WIN_SIZE), (0, 0))
			pygame.display.update()


if __name__ == "__main__":
	pygame.init()

	WIN_SIZE = (800, 600)
	DISPLAY_SIZE = (400, 288)
	screen = pygame.display.set_mode(WIN_SIZE)
	pygame.display.set_caption("The Glowing One")

	display = pygame.Surface(DISPLAY_SIZE)

	game = Game()
	game.run()



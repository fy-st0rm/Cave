import pygame
import os


class Light:
	def __init__(self, surface):
		self.surface = surface

		self.w, self.h = pygame.display.get_surface().get_size()

		self.lights = [
			pygame.image.load(os.path.join("res/light.png")),
			pygame.image.load(os.path.join("res/light2.png")),
			pygame.image.load(os.path.join("res/light3.png"))
		]

		self.l_no = 1
		self.light = self.lights[self.l_no]

		self.lw = self.light.get_width()
		self.lh = self.light.get_height()

	def event(self, e):
		if e.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				self.l_no += 1
				if self.l_no > 2:
					self.l_no = 0

				self.light = self.lights[self.l_no]

	def draw(self, pos):
		filter = pygame.Surface((self.w, self.h))
		filter.fill(pygame.color.Color("black"))

		_pos = [pos[0], pos[1]]

		_pos[0] -= self.lw/2
		_pos[1] -= self.lh/2

		#_pos[0] += pos.w/2
		#_pos[1] += pos.h/2

		filter.blit(self.light, _pos)

		self.surface.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
